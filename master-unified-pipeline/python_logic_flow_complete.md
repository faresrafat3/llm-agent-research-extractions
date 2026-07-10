# ARSENAL — Python Logic Flow Complete

Operational logic for the unified master pipeline. Pseudocode mirrors real patterns extracted from the 7 source systems.

---

## 1. Entry point

```python
def arsenal_main(task: Task, config: ArsenalConfig) -> ArsenalResult:
    journal = StageJournal()
    if config.stages.enabled:
        return run_stages(task, config, journal)
    # single-shot mode: one trial stack without multi-stage shell
    memory = []
    result, memory = run_trial_stack(task, config, memory, stage=None)
    return ArsenalResult(artifacts={"single": result}, memory=memory, journal=journal)
```

---

## 2. L6 — Progressive stage shell

```python
def run_stages(task, config, journal):
    stage = Stage.DRAFT
    artifacts = {}
    while stage is not None:
        memory = []
        best = None
        for trial in range(config.reflexion.max_trials):
            result, memory = run_trial_stack(task, config, memory, stage)
            if is_success(result, task, stage):
                best = result
                break
            if not config.reflexion.enabled:
                best = result
                break
        artifacts[stage.name] = best
        journal.record_stage(stage, best)

        if best is None:
            journal.abort("no_best_node")
            break

        if config.stages.multi_seed:
            seed_metrics = multi_seed_eval(best, config.stages.multi_seed)
            journal.record_seeds(stage, seed_metrics)

        plots = maybe_plot_aggregate(best, journal, config)
        journal.record_plots(stage, plots)

        stage = next_stage(stage, config)  # DRAFT→TUNE→IMPROVE→ABLATE→None

    paper, review = None, None
    if config.stages.writeup:
        paper = writeup_pipeline(artifacts, task, config)
        if config.stages.peer_review:
            review = peer_review(paper, config)
    return ArsenalResult(artifacts=artifacts, paper=paper, review=review, journal=journal)
```

### Stage decisions
- `stage_complete(stage, journal)` — enough successful nodes / goals met.
- `best is None` → abort pipeline.
- `next_stage` returns None after ABLATE or if stages.list exhausted.

---

## 3. L5 — Trial stack with verbal memory

```python
def run_trial_stack(task, config, memory, stage):
    task_ctx = task.with_memory(memory[-config.reflexion.memory_window:])

    # L0
    route = technique_router(task_ctx, stage, config)

    # L1
    prompts = config.default_prompts
    demo_fn = None
    if route.activate.ape and config.ape.enabled:
        prompts, demo_fn = ape_find_prompts(task_ctx, config.ape)

    # L2 (+ L3/L4 inside)
    if route.activate.meta and config.meta:
        result = meta_conductor(task_ctx, prompts, route, config)
    elif route.activate.lats:
        result = lats_search(task_ctx, prompts, config.lats)
        result = self_refine(result, task_ctx, prompts, config.refine)
    else:
        draft = lm_generate(prompts.gen, task_ctx)
        result = self_refine(draft, task_ctx, prompts, config.refine) if route.activate.refine else draft

    # L4 final polish
    if route.activate.refine and not getattr(result, "already_refined", False):
        result = self_refine(result, task_ctx, prompts, config.refine)

    if is_success(result, task_ctx, stage):
        return result, memory

    # L5 reflect
    if route.activate.reflexion and config.reflexion.enabled:
        reflection = verbal_reflect(result, task_ctx)
        memory = memory + [reflection]
    return result, memory
```

---

## 4. L0 — Technique router

```python
def technique_router(task, stage, config) -> Route:
    if config.router.force_families:
        families = config.router.force_families
        activate = config.router.force_activate or default_activate(families)
        return Route(families=families, methods=[], activate=activate, rationale="forced")

    raw = lm_json(P0_ROUTER, task_spec=task.spec, modality=task.modality,
                  demos_available=bool(task.demos), tools=task.tools,
                  token_budget=config.budget.tokens, ...)
    activate = raw["activate"]
    # safety clamps
    if not task.demos:
        activate["ape"] = False
    if stage is None and not config.stages.enabled:
        activate["stages"] = False
    return Route(**raw, activate=Activate(**activate))
```

---

## 5. L1 — APE find_prompts

```python
def ape_find_prompts(task, ape_cfg):
    eval_t = EvalTemplate(ape_cfg.eval_template)
    demos_t = DemosTemplate(ape_cfg.demos_template)
    gen_t = ape_cfg.prompt_gen_template
    if gen_t is None:
        gen_t = eval_t.convert_to_generation_template()  # [PROMPT]→[APE]
    else:
        gen_t = GenerationTemplate(gen_t)

    # generate
    prompts = []
    for _ in range(ape_cfg.num_subsamples):
        demos = subsample(task.prompt_gen_data or task.demos, ape_cfg.num_demos)
        query = gen_t.fill(full_DEMO=demos_t.fill(demos), ...)
        prompts += llm.generate_text(query, n=ape_cfg.num_prompts_per_subsample)
    prompts = list(dict.fromkeys(prompts))  # dedup preserve order

    # evaluate
    few_shot = task.few_shot_data or task.prompt_gen_data or task.demos
    if ape_cfg.eval_method == "likelihood":
        result = likelihood_evaluator(prompts, eval_t, task.eval_data, few_shot, ape_cfg)
    elif ape_cfg.eval_method == "bandits":
        result = bandits_evaluator(prompts, eval_t, task.eval_data, few_shot, ape_cfg)
    else:
        raise ValueError(ape_cfg.eval_method)

    ranked = result.sorted()  # descending score
    demo_fn = make_demo_fn(eval_t, ranked[0].prompt, few_shot)
    return ranked, demo_fn


def bandits_evaluator(prompts, eval_t, data, few_shot, cfg):
    arms = [BanditArm(p) for p in prompts]
    for _ in range(cfg.bandit_rounds):
        chosen = ucb_select(arms)
        n = cfg.num_prompts_per_round
        if n < 1:
            n = max(1, int(n * len(prompts)))
        batch = sample_eval_batch(data, cfg.samples_per_eval)
        scores = score_likelihood_batch(chosen, batch, eval_t, few_shot)
        update_ucb(chosen, scores)
    return BanditsEvaluationResult(arms)
```

---

## 6. L2 — Meta conductor

```python
def meta_conductor(task, prompts, route, config):
    messages = [system(prompts.meta or P2_META), user(task.query_with_memory())]
    for round_i in range(config.meta.max_rounds):
        out = meta_model_generate(messages, config)
        kind, payload = parse_meta_output(out)  # expert | final | invalid

        if kind == "final":
            return FinalResult(payload, messages=messages)

        if kind == "invalid":
            messages.append(assistant(out))
            messages.append(user(P2_FORMAT_ERROR))
            continue

        # expert call
        name, instruction = payload
        if name.lower() in {"expert python", "python"} and config.meta.python_expert:
            expert_out = expert_python(instruction, config)
        elif name.lower() in {"treesearch", "lats"} or route.activate.lats:
            expert_out = lats_search(Task.from_instruction(instruction, task), prompts, config.lats)
            expert_out = self_refine(expert_out, task, prompts, config.refine)
            expert_out.already_refined = True
        else:
            expert_out = lm_generate(P2_EXPERT.format(name=name, instructions=instruction))
            if route.activate.refine:
                expert_out = self_refine(expert_out, task, prompts, config.refine)
                expert_out.already_refined = True

        messages.append(assistant(out))
        messages.append(user(P2_INTERMEDIATE.format(name=name, expert_output=expert_out)))

    return FinalResult(extract_best_effort(messages), messages=messages, truncated=True)


def expert_python(instruction, config):
    code_msg = lm_generate(instruction)
    if "Please run this code!" in code_msg:
        code = extract_code(code_msg)
        stdout, err = execute_code_with_timeout(code, config.meta.python_timeout)
        return f"{code_msg}\n\n[stdout]\n{stdout}\n[stderr]\n{err}"
    return code_msg
```

---

## 7. L3 — LATS / MCTS

```python
def lats_search(task, prompts, lats_cfg):
    root = Node(state=task.initial_state(), visits=0, value=0.0)
    failed = []
    reflections = []

    for _ in range(lats_cfg.iterations):
        node = select_uct(root)
        if node.is_terminal_success:
            return TrajectoryResult(node.trajectory(), tree=root, failed=failed)

        if node.is_terminal_fail or node.exhausted:
            node.prune()
            continue

        children = expand_lm(node, prompts.expand, reflections, width=lats_cfg.expansion_width)
        for c in children:
            c.value_est = get_value(c, prompts.value, env=task.env, cache=True)

        leaf = max(children, key=lambda c: c.value_est)
        reward, traj = rollout(leaf, task.env, max_depth=lats_cfg.max_depth)
        if reward >= task.success_threshold:
            return TrajectoryResult(traj, tree=root, failed=failed)

        backpropagate(leaf, reward)
        failed.append(traj)
        if should_reflect(failed, reflections, lats_cfg):
            reflections.append(self_reflect_trajectory(traj, prompts.reflect))

    best = best_trajectory(root)
    return TrajectoryResult(best, tree=root, failed=failed, partial=True)


def select_uct(node, c=1.4):
    while node.children and not node.is_expandable:
        if all(ch.terminal for ch in node.children):
            return node  # backtrack signal
        node = max(node.children, key=lambda ch: uct(ch, c))
    return node


def uct(node, c):
    if node.visits == 0:
        return float("inf")
    return node.value / node.visits + c * sqrt(log(node.parent.visits) / node.visits)


def backpropagate(node, reward):
    while node is not None:
        node.visits += 1
        node.value += reward
        node = node.parent
```

---

## 8. L4 — Self-Refine

```python
def self_refine(candidate, task, prompts, refine_cfg):
    if isinstance(candidate, TrajectoryResult):
        y = candidate.best_text()
    else:
        y = candidate if isinstance(candidate, str) else candidate.text

    history = []
    y_t = y
    # if no draft, generate
    if y_t is None:
        y_t = lm_generate(prompts.gen or P4_GEN, x=task.x)

    for t in range(refine_cfg.max_iters):
        fb = lm_generate(prompts.fb or P4_FB, x=task.x, y_t=y_t, aspects=task.aspects)
        history.append((y_t, fb))
        if stop_refine(fb, t, refine_cfg, task):
            break
        y_t = lm_generate(
            prompts.refine or P4_REFINE,
            x=task.x,
            history=format_history(history),
        )
    out = RefinedResult(y_t, history=history)
    out.already_refined = True
    return out


def stop_refine(fb, t, cfg, task):
    if t + 1 >= cfg.max_iters:
        return True
    if cfg.stop_mode in ("indicator", "hybrid"):
        phrase = task.stop_phrase or cfg.default_stop_phrase
        if phrase and phrase.lower() in fb.lower():
            return True
    return False
```

---

## 9. L5 — Verbal reflection

```python
def verbal_reflect(result, task):
    return lm_generate(
        P5_REFLECT,
        task=task.spec,
        trajectory=getattr(result, "trajectory", result),
        feedback=getattr(result, "feedback", extract_feedback(result)),
    )
```

---

## 10. L6 production tail

```python
def writeup_pipeline(artifacts, task, config):
    citations = []
    for _ in range(config.stages.citation_rounds):
        batch = semantic_scholar_search(task.idea, artifacts)
        citations = merge_bib(citations, batch)
        if enough_citations(citations):
            break
    paper = lm_generate(P6_WRITEUP, idea=task.idea, summaries=summarize(artifacts),
                        figures=collect_figures(artifacts), bib=citations)
    for _ in range(config.stages.writeup_reflections):
        paper = lm_generate(P6_WRITEUP_REFLECT, paper=paper, constraints=config.stages.page_limits)
    return paper


def peer_review(paper, config):
    review = lm_generate(P6_PEER_REVIEW, paper=paper)
    if config.stages.vlm_review:
        review = merge(review, vlm_figure_review(paper.figures))
    return review
```

---

## 11. Loop / condition inventory (quick ref)

| ID | Loop | Bound | Break |
|---|---|---|---|
| S1 | stages | stage list | abort / done |
| S2 | trials | max_trials | success |
| S3 | ape subsamples | num_subsamples | — |
| S4 | ape bandit rounds | bandit_rounds | — |
| S5 | meta rounds | max_rounds | final answer |
| S6 | mcts iterations | iterations | success terminal |
| S7 | rollout depth | max_depth | terminal |
| S8 | refine iters | max_iters | stop phrase |
| S9 | citation rounds | citation_rounds | enough cites |
| S10 | writeup reflect | writeup_reflections | quality ok |
| S11 | multi-seed | multi_seed | — |

| ID | Condition |
|---|---|
| C1 | demos available → allow APE |
| C2 | eval_method likelihood \| bandits |
| C3 | meta output expert \| final \| invalid |
| C4 | expert Python + run flag |
| C5 | route.lats or expert TreeSearch |
| C6 | UCT infinite if visits==0 |
| C7 | terminal success / fail / exhausted |
| C8 | stop_refine phrase / max |
| C9 | use_memory / window K |
| C10 | best node exists for multi-seed |
| C11 | next stage or None |

---

## 12. Error handling

```python
@retry(parse_errors=3)
def lm_json(prompt, **kw): ...

def execute_code_with_timeout(code, timeout):
    try:
        return run_sandbox(code, timeout=timeout)
    except Timeout:
        return "", "TIMEOUT"
    except Exception as e:
        return "", repr(e)

def safe_stage_step(fn, journal):
    try:
        return fn()
    except Exception as e:
        journal.record_error(e)
        return None
```
