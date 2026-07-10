# ARSENAL — Unified Architecture

## 1. System overview

ARSENAL is a six-layer nested agent architecture. Outer layers set goals, budgets, and memory; inner layers execute search, polish, and tool use.

```
┌──────────────────────────────────────────────────────────────────┐
│ L6  PROGRESSIVE STAGE SHELL  (AI Scientist v2)                   │
│  stages · multi-seed · plots · citations · writeup · peer review │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ L5  MEMORY (Reflexion verbal + Voyager skills/curriculum)  │  │
│  │  trials · reflections · optional skill library             │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │ L0  TECHNIQUE ROUTER  (Prompt Report)                │  │  │
│  │  │  family select · method select · layer activation    │  │  │
│  │  │  ┌────────────────────────────────────────────────┐  │  │  │
│  │  │  │ L1  INSTRUCTION OPTIMIZER  (APE + OPRO)        │  │  │  │
│  │  │  │  APE one-shot/bandit · OPRO meta-evolve        │  │  │  │
│  │  │  │  ┌──────────────────────────────────────────┐  │  │  │  │
│  │  │  │  │ L2  META CONDUCTOR  (Meta-Prompting)     │  │  │  │  │
│  │  │  │  │  decompose · expert dispatch · tools     │  │  │  │  │
│  │  │  │  │  ┌────────────────────────────────────┐  │  │  │  │  │
│  │  │  │  │  │ L3  TREE SEARCH  (ToT + LATS)      │  │  │  │  │  │
│  │  │  │  │  │  ToT beam/DFS · LATS UCT/MCTS      │  │  │  │  │  │
│  │  │  │  │  │  ┌──────────────────────────────┐  │  │  │  │  │  │
│  │  │  │  │  │  │ L4  LOCAL POLISHER           │  │  │  │  │  │  │
│  │  │  │  │  │  │  (Self-Refine)               │  │  │  │  │  │  │
│  │  │  │  │  │  │  gen → fb → refine → stop    │  │  │  │  │  │  │
│  │  │  │  │  │  └──────────────────────────────┘  │  │  │  │  │  │
│  │  │  │  │  └────────────────────────────────────┘  │  │  │  │  │
│  │  │  │  └──────────────────────────────────────────┘  │  │  │  │
│  │  │  └────────────────────────────────────────────────┘  │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

## 2. Component contracts

### L0 Technique Router
```
Input:  task_spec, modality, budget, safety_flags
Output: route {
  families: [...],
  methods: [...],
  activate: {ape, opro, meta, tot, lats, refine, reflexion, voyager, stages},
  ensemble_n, cot_variant, ...
}
```

### L1 Instruction Optimizer (APE baseline + OPRO iterative)
```
Input:  demos | task_desc, eval_template, mode ∈ {ape, opro, cascade}, config
Output: best_prompts[], scores[], demo_fn?, evolution_history?

mode=ape:     generate → dedup → likelihood|UCB → rank
mode=opro:    seed score → meta_prompt evolve → filter → rescore (steps)
mode=cascade: APE warm-start → OPRO refine under eval budget
```

### L2 Meta Conductor
```
Input:  query, meta_instruction, tools, max_rounds
Output: final_answer | expert_log[], message_history
Side:   may call L3, L4, Python, search tools
```

### L3 Tree Search (ToT baseline + LATS full)
```
Input:  root_state, mode ∈ {tot, lats, cascade}, prompts, env?, budgets
Output: best_trajectory, tree, failed_trajectories[]
Side:   may call L4 on leaves; emit failures for L5

mode=tot:  generate(sample|propose) → evaluate(value|vote) → select(beam|sample) [BFS/DFS]
mode=lats: select_UCT → expand → value/env → rollout → backprop → optional reflect
mode=cascade: run tot; if score < τ or interactive → lats
```

### L4 Local Polisher (Self-Refine)
```
Input:  x, y0?, p_gen, p_fb, p_refine, max_iters, stop_fn
Output: y_final, feedback_history[], scores
```

### L5 Memory (Reflexion verbal + Voyager procedural)
```
Input:  task, actor, env, memory[], max_trials, skill_bank?
Output: success?, best_result, updated memory[], optional new skills

verbal (Reflexion): on fail → reflection → memory[-K:] for next trial
procedural (Voyager, optional):
  curriculum.propose_next_task → retrieve skills → act/critic loop → add_skill on success
```

### L6 Stage Shell (AI Scientist v2)
```
Input:  idea/task, stage_config, skip_flags
Output: stage_artifacts, metrics, plots, paper?, peer_review?
```

## 3. Canonical execution algorithm

```python
def arsenal_run(task, config):
    # L6 — stages
    stage = Stage.DRAFT
    artifacts = {}
    while stage is not None:
        # L5 — trials with memory
        memory = []
        best = None
        for trial in range(config.max_trials):
            # L0 — route
            route = technique_router(task, stage, config)

            # L1 — optional prompt optimization (APE / OPRO / cascade)
            if route.activate.opro and route.activate.ape:
                seeds, _ = ape_find_prompts(task.demos, config.ape)
                prompts, demo_fn = opro_evolve(seeds, task, config.opro)
            elif route.activate.opro:
                prompts, demo_fn = opro_evolve(config.default_prompts, task, config.opro)
            elif route.activate.ape:
                prompts, demo_fn = ape_find_prompts(task.demos, config.ape)
            else:
                prompts = config.default_prompts
                demo_fn = None

            # L2 — meta conductor
            def expert_handler(expert_name, instruction):
                if expert_name == "TreeSearch" or route.activate.lats:
                    traj = lats_search(instruction, config.lats)
                    # L4 polish best leaf
                    return self_refine(traj.best, config.refine)
                if expert_name == "Python":
                    return run_python(instruction)
                # default expert + L4
                draft = lm_generate(instruction)
                return self_refine(draft, config.refine)

            result = meta_conductor(task, prompts, expert_handler, config.meta)

            # L4 final polish
            if route.activate.refine:
                result = self_refine(result, config.refine)

            if is_success(result, task):
                best = result
                break

            # L5 reflect
            if route.activate.reflexion:
                reflection = verbal_reflect(result, task)
                memory.append(reflection)
                task = task.with_memory(memory[-config.memory_window:])

        artifacts[stage] = best

        # L6 stage completion
        if stage_complete(stage, artifacts):
            multi_seed_eval(best, config)
            stage = next_stage(stage, config)
        else:
            stage = None  # abort

    # L6 production tail
    if config.writeup:
        paper = writeup(artifacts, config)
        paper = writeup_reflect(paper, config)
        review = peer_review(paper, config)
        return paper, review, artifacts
    return artifacts
```

## 4. Data flow

```
User Task / Research Idea
        │
        ▼
   [L0 Router] ── family, methods, layer flags
        │
        ▼
   [L1 APE|OPRO|cascade] ── best instruction(s) + optional history
        │
        ▼
   [L2 Meta] ───┬── Expert A ──► [L3 ToT|LATS] ── leaves ──► [L4 Refine]
                ├── Expert B ──► generate ──► [L4 Refine]
                └── Expert Python ──► exec
        │
        ▼
   Final candidate ──► [L4 Refine]
        │
   success? ──no──► [L5 Reflect] ── verbal memory ──► next trial
        │ yes
        ▼
   optional [Voyager add_skill / curriculum next]
        │
        ▼
   Stage artifact ──► multi-seed / plots
        │
   more stages? ──yes──► next stage
        │ no
        ▼
   Citations → Writeup → Reflect → Peer Review → Deliverable
```

## 5. Shared memory model

| Store | Owner | Contents | Window |
|---|---|---|---|
| `route_cache` | L0 | task → route | session |
| `prompt_bank` | L1 | ranked prompts + scores (+ OPRO history) | persistent per task family |
| `message_log` | L2 | meta + expert messages | per trial |
| `search_tree` | L3 | nodes, values, visits | per trial |
| `refine_history` | L4 | y_t, fb_t pairs | per candidate |
| `reflection_memory` | L5 | verbal reflections | last K across trials |
| `skill_library` | L5-Voyager | code skills + descriptions + embeddings | persistent |
| `curriculum_state` | L5-Voyager | completed/failed tasks, QA cache | run/persistent |
| `stage_journal` | L6 | nodes, metrics, plots, summaries | full run |

## 6. Stop conditions (unified)

| Layer | Stop when |
|---|---|
| L4 | max_iters OR task stop phrase OR score plateau |
| L3 | success terminal OR max iterations OR tree exhausted |
| L2 | final-answer indicator OR max meta rounds |
| L5 | success OR max trials |
| L1 | APE eval budget / OPRO search steps exhausted OR top-k stable |
| L6 | stage 4 complete OR no best node OR skip flags |

## 7. Configuration skeleton

```yaml
arsenal:
  router:
    force_families: null  # or list
  ape:
    enabled: true
    num_subsamples: 5
    num_prompts_per_subsample: 10
    eval_method: bandits  # or likelihood
    bandit_rounds: 20
  opro:
    enabled: false  # or cascade with ape
    num_search_steps: 20
    num_generated_per_step: 8
    meta_prompt_type: both_instructions_and_exemplars
    instruction_pos: Q_begin
    score_threshold: 0.1
  meta:
    max_rounds: 15
    python_expert: true
    fresh_eyes: false
  lats:
    enabled_auto: true  # router may force
    iterations: 50
    max_depth: 8
    expansion_width: 5
  refine:
    max_iters: 4
    stop_mode: hybrid  # fixed | indicator | hybrid
  reflexion:
    max_trials: 5
    memory_window: 3
  voyager:
    enabled: false
    skill_top_k: 5
    task_max_retries: 4
    curriculum: auto
  stages:
    enabled: true
    list: [draft, tune, improve, ablate]
    multi_seed: 3
    writeup: true
    peer_review: true
```

## 8. Failure modes and mitigations

| Failure | Mitigation |
|---|---|
| Bad instruction | L1 APE re-search and/or OPRO evolve; Prompt Report re-route |
| Infinite expert loop | L2 max_rounds + format-error retry budget |
| Tree explosion | L3 depth/iteration caps; UCT exploration constant |
| Refine thrashing | L4 history + stop indicators + max_iters |
| Memory pollution | L5 window K; only store failures; skill versioning / skip chores |
| Stage stall | L6 no-best-node abort; skip flags; human checkpoint |

## 9. Evaluation hooks

- **Unit**: L4 multi-aspect scores; L3 env reward; L1 prompt scores.
- **Trial**: L5 success rate / pass@k.
- **Stage**: L6 metrics + multi-seed mean/std.
- **Artifact**: LLM-as-Judge / G-Eval / peer-review schema (Prompt Report + AI Scientist v2).
- **System**: cost (tokens, tool calls), latency, success under budget.

## 10. Mapping back to source extractions

| ARSENAL component | Primary extraction folder |
|---|---|
| L0 Router | `projects/prompt-report/` |
| L1 APE (baseline) | `projects/ape/` |
| L1 OPRO (iterative) | `projects/opro/` |
| L2 Meta | `projects/meta-prompting/` |
| L3 ToT (baseline) | `projects/tot/` |
| L3 LATS (full) | `projects/lats/` |
| L4 Self-Refine | `projects/self-refine/` |
| L5 Reflexion (verbal) | `projects/reflexion/` |
| L5 Voyager (skills/curriculum) | `projects/voyager/` |
| L6 Stages | `projects/ai-scientist-v2/` |
