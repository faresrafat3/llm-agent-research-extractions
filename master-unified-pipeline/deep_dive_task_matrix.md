# ARSENAL — Deep Dive Task / Phase Matrix

## Universal phase matrix

| Phase | Layer | Source system | Function | Input | Output | Loop | Key decision | Stop condition |
|---|---|---|---|---|---|---|---|---|
| 0 Route | L0 | Prompt Report | `technique_router` | task_spec, modality, budget | route flags + methods | no | which family/method? | always once per trial |
| 1 Optimize instruction | L1 | APE | `find_prompts` | demos, templates, config | ranked prompts, demo_fn | yes: subsamples + eval rounds | likelihood vs bandits | eval budget / top-k stable |
| 2 Conduct | L2 | Meta-Prompting | `meta_model_generate` | query, meta_instruction | expert calls / final answer | yes: meta rounds | expert vs final vs error | final answer / max rounds |
| 3 Dispatch expert | L2 | Meta-Prompting | expert extract + call | expert block | expert output | nested | Python expert? | — |
| 4 Tool exec | L2 | Meta-Prompting | `execute_code_with_timeout` | code | stdout/err | no | run code flag? | timeout |
| 5a ToT generate | L3 | Tree of Thoughts | `get_samples` / `get_proposals` | frontier ys | children | per step | sample vs propose | — |
| 5b ToT evaluate | L3 | Tree of Thoughts | `get_values` / `get_votes` | new_ys | values | per child / batch | value vs vote; cache | — |
| 5c ToT select | L3 | Tree of Thoughts | greedy / multinomial | values, b | frontier | per step | greedy vs sample | steps done |
| 5d mode choose | L3 | ToT+LATS | `choose_search_mode` | task, route, score | tot\|lats\|cascade | no | offline vs interactive; cascade τ | — |
| 6 Tree select | L3 | LATS | `select_UCT` | tree | node | yes: while not expand-ready | terminal? exhausted? | — |
| 7 Tree expand | L3 | LATS | `expand_LM` | node, expand_prompt | children | yes: width | reflection available? | — |
| 8 Tree value | L3 | LATS | `get_value` | child, value_prompt / env | score | yes: children | cache hit? | — |
| 9 Tree rollout | L3 | LATS | `rollout` | node, env | reward, trajectory | yes: depth | success mid-rollout? | max depth / terminal |
| 10 Tree backprop | L3 | LATS | `backpropagate` | reward | updated visits/values | yes: to root | — | root reached |
| 10 Local polish | L4 | Self-Refine | gen→fb→refine | x, y, prompts | y_final, history | yes: max_iters | stop(fb,t)? | stop indicator / max |
| 11 Trial reflect | L5 | Reflexion | `verbal_reflect` | trajectory, feedback | reflection text | per failed trial | use_memory? | success / max trials |
| 12 Memory update | L5 | Reflexion | append + window | reflection, memory | memory[-K:] | no | window size | — |
| 13 Stage step | L6 | AI Scientist v2 | BFTS node step | parent node, stage goal | child node | yes: node loop | draft/debug/improve/tune/ablate | stage/substage complete |
| 14 Multi-seed | L6 | AI Scientist v2 | multi_seed_eval | best node | seed metrics | yes: seeds | best node exists? | all seeds done |
| 15 Plot / aggregate | L6 | AI Scientist v2 | plot + VLM feedback | metrics, data | figures | yes: retry | VLM ok? | — |
| 16 Citations | L6 | AI Scientist v2 | Semantic Scholar loop | idea, report | BibTeX | yes: ~20 rounds | enough cites? | max rounds |
| 17 Writeup | L6 | AI Scientist v2 | write + reflect | artifacts, template | LaTeX/PDF | yes: reflection | page limit / quality | max reflects |
| 18 Peer review | L6 | AI Scientist v2 | LLM/VLM review | paper | review JSON | optional meta-review | accept criteria | — |

---

## Layer activation matrix (by task type)

| Task type | L0 families | L1 APE | L2 Meta | L3 ToT | L3 LATS | L4 Refine | L5 Reflexion | L6 Stages |
|---|---|---|---|---|---|---|---|---|
| Simple QA | ICL + CoT | optional | off | off | off | optional | off | off |
| Math / GSM / Game24-like | CoT + Decomposition | optional | optional | **on** | off/cascade | on | optional | off |
| Creative constrained writing | Thought + Ensembling | optional | optional | **on** (vote) | off | on | off | off |
| Code generation | Agents + Self-Criticism | optional | Python expert | optional | **on** | on | on | optional |
| Interactive env (AlfWorld/WebShop) | Agents + Self-Criticism | off | optional | off | **on** | optional | on | off |
| Multi-hop QA (HotPotQA) | Agents + Decomposition | off | optional | optional | **on** | optional | on | off |
| Instruction induction | Prompt Optimization | **on** | off | off | off | off | off | off |
| Research experiment | All + Evaluation | on | on | on | on | on | on | **on** |
| Paper writeup | Decomposition + Self-Criticism + Eval | optional | on | off | off | on | optional | writeup+review |
| Multimodal figure | Multimodal + Self-Criticism | off | on | off | off | visual refine | optional | VLM review |

---

## Decision catalog (complete)

### L0 Router
- modality ∈ {text, code, image, multi}?
- needs_tools?
- needs_decomposition?
- high_uncertainty / large_action_space?
- demos_available?
- production_pipeline?

### L1 APE
- prompt_gen_template provided?
- eval_method = likelihood | bandits?
- few_shot_data provided?
- num_prompts_per_round scale?

### L2 Meta
- output type: expert_call | final_answer | invalid?
- expert == Python?
- contains `Please run this code!`?
- num_return_sequences > 1 → summarize?
- rounds >= max?

### L3 ToT + LATS
- mode tot | lats | cascade?
- ToT: sample vs propose; value vs vote; greedy vs sample beam?
- ToT DFS prune if impossible ≥ 1?
- cascade score < τ → escalate LATS?
- LATS: node terminal success / fail / exhausted?
- LATS: UCT pick among children; value cache hit?
- LATS: generate reflection from unique failures?

### L4 Self-Refine
- n_attempts == 0 → init else iterate
- stop phrase in feedback?
- score parse success?
- max_iters reached?

### L5 Reflexion
- success?
- trials remaining?
- use_memory?
- env already successful (skip)?

### L6 Stages
- stage complete?
- substage complete?
- best node found?
- next stage exists?
- writeup / review enabled?

---

## Nested loop nesting order

```
for stage in stages:                          # L6
  memory = []
  for trial in trials:                        # L5
    route = router(task, stage)               # L0
    if route.ape:
      prompts = ape_search(...)               # L1  (subsamples × eval)
    for meta_round in meta_rounds:            # L2
      if expert TreeSearch:
        for mcts_iter in N:                   # L3
          select → expand → value → rollout → backprop
          for leaf in new_leaves:
            for r in refine_iters:            # L4
              feedback → refine
      elif expert Python:
        exec once
      else:
        generate
        for r in refine_iters:                # L4
          feedback → refine
    final refine                              # L4
    if fail: reflect → memory                 # L5
  multi_seed; plots                           # L6
writeup; peer_review                          # L6
```

---

## I/O summary per layer

| Layer | Primary inputs | Primary outputs | Side effects |
|---|---|---|---|
| L0 | task_spec | route | route_cache |
| L1 | demos, templates | prompts, demo_fn | prompt_bank |
| L2 | query, prompts | answer, expert_log | message_log, tool calls |
| L3 | state, env | trajectory, tree | failed_trajectories |
| L4 | draft, x | polished y | refine_history |
| L5 | trial result | memory update | reflection_memory |
| L6 | idea/task | artifacts, paper, review | stage_journal, files |
