# L3 Search Family Map — ToT vs LATS

Goal: make **one clear decision** inside ARSENAL L3 instead of treating “tree search” as a single blob.

Sources:
- ToT extraction: `projects/tot/` · https://github.com/faresrafat3/tot-full-extraction
- LATS extraction: `projects/lats/` · https://github.com/faresrafat3/lats-full-extraction

---

## 1) Shared skeleton (both are “deliberate search”)

```
state / partial solution
   → GENERATE candidate next thoughts/actions
   → EVALUATE how promising
   → SELECT what to expand next
   → (optional) STOP / return best
```

| Axis | ToT | LATS |
|---|---|---|
| Generate | sample **or** propose | LM expand (thoughts/actions/code) |
| Evaluate | value labels **or** vote | LM value **+ env reward** |
| Select | greedy beam **or** multinomial | **UCT** tree policy |
| Search shell | BFS beam / DFS prune | MCTS iterations + rollout + backprop |
| Memory of failure | (none built-in) | self-reflection on failed trajectories |
| Environment | optional (crosswords env only) | first-class (Wiki/WebShop/executors) |

---

## 2) When ARSENAL should pick which mode

| Situation | Prefer | Why |
|---|---|---|
| Fixed-step puzzle / math / constrained writing | **ToT** | Beam over thoughts is enough; cheaper; clear step budget |
| Need comparative ranking of full drafts | **ToT + vote** | Vote prompt is built for multi-candidate comparison |
| Interactive env (web, game, tools) | **LATS** | Needs env feedback + multi-turn actions |
| Code with unit tests / long debug | **LATS** | Rollout + backprop + reflection on failures |
| Very large action space, deep horizon | **LATS** | UCT balances explore/exploit better than fixed beam |
| Strict token budget / no env | **ToT** | Fewer mechanisms; beam width `b` is simple knob |
| Want reflection across tree failures without full Reflexion trial | **LATS** | Built-in failed-trajectory reflection |
| Want cross-trial memory after whole search fails | **either + L5 Reflexion** | Outer trial wrapper |

Router hint (L0 → L3 flags):

```yaml
activate:
  tot: true   # offline deliberate
  lats: false
# or
activate:
  tot: false
  lats: true  # interactive / env
# or cascade:
activate:
  tot: true
  lats: true  # try ToT first; escalate to LATS if ToT score < threshold
```

---

## 3) Composition recipes (in-scope for ARSENAL)

### Recipe A — Pure ToT
`L0 → (L1?) → L2? → L3-ToT → L4 refine → L5?`

### Recipe B — Pure LATS
`L0 → (L1?) → L2? → L3-LATS → L4 refine leaves → L5 reflect trials`

### Recipe C — Cascade (recommended default under uncertainty)
1. Run **ToT** with small `b` and `steps`.
2. If `best_value < τ` or task marked interactive → escalate **LATS**.
3. Always polish leaves with **L4**.
4. On full failure → **L5** reflection for next trial.

### Recipe D — ToT inside LATS expand (advanced)
Use ToT-style `propose` as the expansion operator, then UCT/backprop as in LATS.

---

## 4) Prompt / logic assets to wire

| Need | Pull from ToT package | Pull from LATS package |
|---|---|---|
| Next-step propose | `prompts/game24.propose`, crosswords.propose | expand / ReAct action prompts |
| State value labels | sure/likely/impossible maps | LM value prompts + env score |
| Comparative vote | `text.vote_prompt` | (use ToT vote or SC) |
| Beam select | `bfs.solve` greedy top-b | — |
| UCT select | — | `select_uct` |
| Failure verbalize | — | LATS reflection + Reflexion P5 |

---

## 5) Stop / budget knobs (unified)

| Knob | ToT | LATS |
|---|---|---|
| Width | `n_select_sample` (b) | expansion_width / UCT c |
| Depth | `task.steps` | max_depth |
| Eval samples | `n_evaluate_sample` | value samples / rollouts |
| Iterations | = steps (BFS) | MCTS N |
| Prune | DFS impossible | exhausted terminal |

---

## 6) Non-goals (out of scope here)

- Implementing a new MCTS library from scratch.
- Replacing LATS paper results.
- Merging repositories physically — only **pattern fusion** in ARSENAL docs/graphs.

---

## 7) One-line rule

> **ToT thinks carefully on a page; LATS acts carefully in a world.**  
> ARSENAL L3 picks ToT for the page, LATS for the world, and may cascade page → world.

---

## 8) L1 Instruction family — APE vs OPRO

| Axis | APE | OPRO |
|---|---|---|
| Generation | LLM from demos (forward) | LLM from **scored history** meta-prompt |
| Scoring | likelihood / UCB bandits | task accuracy via scorer LLM |
| Iteration | generate pool then rank | multi-step evolution |
| State | candidate set | meta-prompt trajectory of (instruction, score) |
| Best when | demos exist, tight budget | scorer + step budget available |

### L1 one-line rule
> **APE finds a good instruction quickly; OPRO climbs from scored attempts.**  
> Cascade: APE seeds → OPRO refine.

---

## 9) L5 Memory family — Reflexion vs Voyager

| Axis | Reflexion | Voyager |
|---|---|---|
| Memory type | verbal reflections | executable skills + descriptions |
| Loop | trial → fail → reflect → retry | curriculum task → act/critic → add skill |
| Retrieval | last-K text in prompt | embedding top-k skills |
| Best when | sparse failures, language advice helps | reusable procedures + env/executor |

### L5 one-line rule
> **Reflexion remembers what went wrong in words; Voyager remembers what worked as code.**  
> Use both when open-ended agents should grow a skill bank across tasks.
