# Pattern Extraction — Strongest Patterns from All 10 Systems

This document extracts the *best loops, decision points, prompts, and logic flows* from each system for fusion into ARSENAL.

---

## 1. AI Scientist v2 — Progressive Stage Shell

### Best loops
- **Outer stage loop**: Stage 1 (draft) → 2 (baseline/hyperparam) → 3 (creative improve) → 4 (ablation).
- **Substage loop** inside each stage.
- **Node loop** (BFTS): draft / debug / improve / tune / ablate.
- **Ideation reflection loop**: generate idea → SearchSemanticScholar or FinalizeIdea.
- **Citation loop**: up to ~20 Semantic Scholar rounds.
- **Writeup reflection loop**: write → reflect → revise.
- **Multi-seed evaluation** on best node before advancing.

### Best decision points
- Stage complete? → multi-seed eval + plot aggregation → next stage.
- Substage complete? → create next substage.
- Best node found? → continue or abort.
- ACTION == SearchSemanticScholar vs FinalizeIdea.
- writeup_type: normal vs ICBINB.
- skip_writeup / skip_review flags.

### Best prompts / schemas
- Ideation system + reflection prompts.
- BFTS draft / debug / improve / hyperparam / ablation prompts.
- Metric parsing schemas.
- Plotting + VLM feedback prompts.
- Citation gathering prompts.
- Writeup + writeup-reflection prompts.
- Peer-review and meta-review prompts.

### Role in ARSENAL
**L6 Progressive Stage Shell** — wraps all other layers into an end-to-end production pipeline with evaluation, aggregation, writeup, and review.

---

## 2. Self-Refine — Local Polisher

### Best loops
```
y0 = M(p_gen || x)
for t = 0..max:
  fb_t = M(p_fb || x || y_t)
  if stop(fb_t, t): break
  y_{t+1} = M(p_refine || x || history)
return y_t
```

### Best decision points
- Fixed max iterations vs task-specific stop indicator.
- CommonGen: both concept + commonsense feedback == `none`.
- GSM: feedback contains `it is correct`.
- PIE: `this code is not slow` / max attempts.
- Visual: missing rendered image or exception budget.

### Best prompts
- `p_gen` (init), `p_fb` (multi-aspect feedback), `p_refine` (history-aware iterate).
- Multi-aspect scoring (pronunciation, spelling, relation, connotation…).
- Visual Self-Refine: TikZ → render → GPT-4V critique → refine; `fix_latex` repair.

### Best logic
- Same model as generator + critic + refiner (no extra trained model).
- History concatenation to avoid repeated mistakes.
- Parse-retry decorator for fragile structured outputs.

### Role in ARSENAL
**L4 Local Polisher** — applied to every candidate leaf / expert draft / stage artifact before acceptance.

---

## 3. Reflexion — Episodic Verbal Memory

### Best loops
```
memory = []
for trial in 1..T:
  trajectory = actor(task, memory)
  feedback = env/executor(trajectory)
  if success: return
  reflection = verbalize(feedback, trajectory)
  memory.append(reflection)
```

### Best decision points
- Success vs failure vs max trials / max steps.
- `use_memory` on/off.
- Already-successful env skip (AlfWorld multi-env).
- Heuristic stuck / repetition detection.
- Memory window (e.g. last 3 reflections).

### Best prompts
- Actor prompts (ReAct / CoT / domain-specific).
- Reflection few-shot examples (AlfWorld, WebShop, programming).
- Self-reflection from unit-test / compiler feedback (programming).

### Best logic
- Verbal RL — no weight updates.
- EnvironmentHistory with bounded memory.
- Cross-domain: sequential decisions, shopping, QA, code.

### Role in ARSENAL
**L5 Episodic Verbal Memory** — outer trial wrapper; failed tree searches and refine failures produce reflections that condition next trial.

---

## 4. Meta-Prompting — Conductor / Expert Dispatch

### Best loops
```
messages = [meta_instruction, query]
while rounds < max:
  out = MetaModel(messages)
  if final_answer: return
  if expert_call:
    expert_out = Expert(instruction)
    if Python and "Please run this code!": exec + append
    messages += expert_out + intermediate_feedback
  else: append format error and retry
```

### Best decision points
- Expert call vs final answer vs invalid.
- Expert Python vs normal expert.
- `Please run this code!` → execute with timeout.
- num_return_sequences > 1 → summarizer expert.
- Round budget exceeded → stop.
- Fresh-eyes mode / include expert name.

### Best prompts
- `meta-prompting-instruction.txt` (conductor).
- `meta-prompting-with-no-python-expert-instruction.txt`.
- `expert-choose-expert.txt`, `expert-generic-instruction.txt`.
- Multipersona / zero-shot-CoT baselines.

### Best logic
- Single LM as conductor + all experts (role isolation via prompts).
- Intermediate feedback after every expert output.
- Tool expert (Python) as first-class citizen.

### Role in ARSENAL
**L2 Meta Conductor** — decomposes stage goals into expert subtasks; experts may invoke L3/L4/tools.

---

## 5. Tree of Thoughts — Classic Deliberate Search (L3 baseline)

### Best loops
```
ys = ['']  # frontier
for step in task.steps:
  new_ys = generate(ys)   # sample independent OR propose next steps
  values = evaluate(new_ys)  # value each state OR vote among candidates
  ys = select_top_b(new_ys, values)  # greedy beam or multinomial
return ys
# Crosswords variant: DFS + prune if any partial fill is "impossible"
```

### Best decision points
- `method_generate`: sample vs propose.
- `method_evaluate`: value vs vote.
- `method_select`: greedy vs sample.
- Value cache hit / duplicate candidate → value 0.
- Game24: remaining numbers == 24 → switch to final CoT answer prompt.
- DFS prune when impossible count ≥ 1; max_per_state / time_limit.

### Best prompts
- Game24: standard, cot, propose, value, value_last_step.
- Creative writing: standard, cot, vote, score, compare.
- Crosswords: standard, cot, propose, value (sure/maybe/impossible).

### Best logic
- Thoughts as intermediate search nodes (not only final answers).
- Beam width `b = n_select_sample` as explicit budget knob.
- Clean generate × evaluate × select axes — easy to compose.

### Role in ARSENAL
**L3-baseline** — prefer ToT when the problem is **offline / puzzle-like** (fixed steps, no interactive env), or as a cheaper deliberate-search mode before escalating to LATS.

---

## 5b. LATS — Interactive MCTS Tree Search (L3 full)

### Best loops
```
root = Node(state)
for iteration in 1..N:
  node = select_UCT(root)
  if terminal success: return trajectory
  children = expand_LM(node)
  values = evaluate_LM_or_env(children)
  reward = rollout(best_child)
  backpropagate(reward)
  if failures: optional self_reflection
```

### Best decision points
- Terminal success / terminal fail / exhausted branch.
- UCT selection among non-terminal children.
- Value cache hit vs recompute.
- Generate reflection if unique failures exceed threshold.
- Max depth / max iterations.

### Best prompts
- Expansion (thoughts/actions/code) — ReAct/CoT style.
- Value / scoring prompts.
- Self-reflection from failed trajectories.
- Domain prompts: HotPotQA, WebShop, programming generators.

### Best logic
- Unifies reasoning + acting + planning via MCTS.
- LM as policy (expand) and value (evaluate).
- External env feedback + reflection memory.
- **Extends ToT**: UCT instead of fixed beam, env reward, rollout, backprop, failure reflections.

### Role in ARSENAL
**L3-full Tree Search Engine** — use when the conductor marks a subtask as **interactive, long-horizon, or env-grounded** (tools, web, code tests, multi-step agents).

---

## 6. APE — Instruction Optimizer

### Best loops
```
prompts = []
for _ in num_subsamples:
  demos = subsample(data)
  prompts += LLM.generate(generation_template, demos)
prompts = dedup(prompts)
scores = evaluate(prompts)  # likelihood or UCB bandits
return sorted(prompts by score), demo_fn
```

### Best decision points
- `prompt_gen_template is None` → convert eval_template.
- `eval_method`: likelihood vs bandits (UCB).
- `few_shot_data is None` → use prompt_gen_data.
- `num_prompts_per_round < 1` → scale by num_prompts.
- Bandit arm selection via UCB.

### Best prompts / templates
- `GenerationTemplate` with `[APE]`, `[full_DEMO]`, `[INPUT]`, `[OUTPUT]`.
- `EvalTemplate` with `[PROMPT]`, `[INPUT]`, `[OUTPUT]`.
- `DemosTemplate` for few-shot packing.
- Forward generation mode default.

### Best logic
- Instructions as natural-language programs.
- Likelihood scoring: log p(output | prompt+input).
- Bandits: efficient evaluation under budget.
- Returns both best prompts and a reusable `demo_fn`.

### Role in ARSENAL
**L1 Instruction Optimizer** — runs once per task/stage (or on schedule) to produce high-quality working prompts for L2–L5.

---


---

## 6b. OPRO — Iterative Meta-Prompt Instruction Optimizer

### Best loops
```
score initial_instructions on train
for step in 1..num_search_steps:
  meta_prompt = history of (instruction, score) [+ optional few-shot QAs]
  candidates = optimizer_llm(meta_prompt)
  filter (length, digits, tag leaks, duplicates)
  score each candidate with scorer_llm
  append to history
return best instructions by score
```

### Best decision points
- `meta_prompt_type`: both_instructions_and_exemplars vs instructions_only.
- `instruction_pos`: before_Q / Q_begin / Q_end / A_begin.
- Few-shot selection: accumulative_most_frequent / current_most_frequent / constant / random.
- Temperature schedule: constant vs linear_increase.
- Skip rules: len>500, GSM8K digits, leaked "INS", MD5 duplicates.
- Score threshold for including old instructions in the meta-prompt.

### Best prompts
- GPT meta headers + `<INS>...</INS>` / `<Start>...</Start>` closings.
- text-bison score-ordered texts + square-bracket request.
- Scorer `gen_prompt` placements around Q/A.
- LR/TSP meta-prompts as same pattern on non-NL objectives.

### Best logic
- Solutions **condition** the next proposals (unlike APE one-shot pool).
- Optimizer LLM ≠ scorer LLM allowed.
- Explicit evolution budget (`num_search_steps`, candidates per step).

### Role in ARSENAL
**L1-iterative** — use when evaluation signal exists and budget allows multi-step search.  
**Cascade:** APE warm-start → OPRO refine, or OPRO alone from seed instructions.

---

## 6c. Voyager — Skill Library + Automatic Curriculum (L5 procedural)

### Best loops
```
while iterations:
  task, context = curriculum.propose_next_task(state)  # auto curriculum
  skills = skill_library.retrieve(context)
  for retry in 1..max_retries:                         # iterative prompting
    code = action_llm(state, skills, errors, critique)
    events = env.step(code)
    success, critique = critic(events, task)
  if success: skill_library.add(code, description)
```

### Best decision points
- First hard-coded bootstrap task vs LLM curriculum.
- Inventory-full forced housekeeping tasks.
- Warm-up gates for which observations enter curriculum prompt.
- Critic auto vs manual; action parse success.
- Add skill only on success; skip deposit-like chores; version name collisions.

### Best prompts
- Action template + response format (Mineflayer JS).
- Critic JSON `{reasoning, success, critique}`.
- Curriculum next-task + QA ask/answer + task decomposition.
- Skill description prompt for embedding/retrieval.

### Best logic
- **Procedural memory** (executable skills) compounds across tasks.
- Automatic curriculum keeps tasks novel and feasible.
- Env-grounded generate→execute→critique loop (Self-Refine cousin with real feedback).

### Role in ARSENAL
**L5-procedural + curriculum** — optional open-ended growth path beside Reflexion verbal memory.  
Use when the domain supports reusable skills and an environment/executor (code, tools, games, agents).

## 7. The Prompt Report — Technique Router

### Best structure (not a loop — a taxonomy)
Six text technique families + multimodal/agent/eval:

1. **In-Context Learning** — Zero/Few-Shot, KNN/Vote-K, SG-ICL, APE instruction selection
2. **Thought Generation** — CoT, Zero-Shot CoT, Analogical, Step-Back, Auto-CoT…
3. **Decomposition** — Least-to-Most, Plan-and-Solve, ToT, PoT, Skeleton-of-Thought…
4. **Ensembling** — Self-Consistency, DiVeRSe, USP, Prompt Paraphrasing…
5. **Self-Criticism** — Self-Refine, CoVe, Self-Verification, Reflexion, ReAct…
6. **Answer / Prompt Engineering** — verbalizer, extractor, APE, OPRO, Meta-Prompting, Promptbreeder

Plus agents (ReAct, tools), multilingual, multimodal, evaluation (LLM-as-Judge, G-Eval).

### Best decision points (routing)
- Task needs reasoning? → Thought Generation.
- Task is complex multi-step? → Decomposition (+ maybe LATS).
- High variance answers? → Ensembling (Self-Consistency).
- Quality-sensitive draft? → Self-Criticism (Self-Refine / Reflexion).
- Instruction unknown? → Prompt Optimization (APE and/or OPRO).
- Tools / env needed? → Agents (ReAct / Meta experts / Voyager skills).
- Non-English / multimodal? → specialized families.

### Role in ARSENAL
**L0 Technique Router** — first gate; selects which families and which ARSENAL layers to activate for the current task/stage.

---

## Fusion rules (how patterns combine)

| When | Activate | From |
|---|---|---|
| Task arrives | L0 Router | Prompt Report |
| Instruction quality low / demos, cheap budget | L1-baseline APE | APE |
| Need iterative prompt search / score history | L1-iterative OPRO | OPRO |
| Warm-start then refine prompts | L1 cascade APE→OPRO | APE + OPRO |
| Task multi-part / needs tools | L2 Conductor | Meta-Prompting |
| Large search space / offline puzzle | L3-baseline ToT | Tree of Thoughts |
| Interactive / long-horizon / env tools | L3-full LATS | LATS |
| Candidate draft exists | L4 Self-Refine | Self-Refine |
| Code/skill with env critique | L4+Voyager critic pattern | Voyager |
| Trial failed | L5 Reflexion verbal memory | Reflexion |
| Open-ended multi-task skill growth | L5 Voyager curriculum+skills | Voyager |
| Multi-phase production needed | L6 Stages | AI Scientist v2 |
| Final artifact | Peer review + VLM | AI Scientist v2 |

### Nested call order (canonical)

```
L6 stage
  └─ L5 trial (Reflexion memory [+ optional Voyager skill bank])
       └─ L0 route technique
            └─ L1 optimize prompt (optional)
                 ├─ mode=APE | OPRO | cascade APE→OPRO
            └─ L2 meta conductor
                 ├─ expert: L3 tree search
                 │    ├─ mode=ToT  if offline/puzzle
                 │    └─ mode=LATS if interactive
                 │         └─ each leaf: L4 refine
                 ├─ expert: direct generate + L4 refine
                 ├─ expert: tool/Python
                 └─ expert: Voyager-style skill retrieve + env act (optional)
            └─ L4 final polish
       └─ on fail: L5 verbal reflect → next trial
       └─ on success (open-ended): optional Voyager add_skill + curriculum next
  └─ stage complete → multi-seed / next stage / writeup / review
```
