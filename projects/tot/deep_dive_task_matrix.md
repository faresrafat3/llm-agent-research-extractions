# Tree of Thoughts — Deep Dive Task / Phase Matrix

## Universal ToT algorithm

| Phase | Code | Input | Output | Loop | Key decision |
|---|---|---|---|---|---|
| Load task | `get_task` | task name | Task instance | no | game24/text/crosswords |
| Get problem | `get_input(idx)` | idx | x | no | — |
| Init frontier | `solve` | — | ys=[''] | no | — |
| Generate | `get_samples` / `get_proposals` | x, y | children | per frontier state | sample vs propose |
| Evaluate | `get_values` / `get_votes` | x, new_ys | values | per child / batch | value vs vote; cache |
| Select | greedy or multinomial | values, b | new frontier | no | greedy vs sample |
| Advance step | `for step in steps` | — | — | task.steps | — |
| Test | `test_output` | idx, y | reward dict | per final y | task-specific |
| Log | `run` | infos | JSON | task range | naive vs ToT |

---

## 1. Game of 24

| Item | Detail |
|---|---|
| Files | `tasks/game24.py`, `prompts/game24.py`, `scripts/game24/*.sh` |
| Input | 4 numbers string e.g. `4 5 6 10` |
| Output | 3 ops + Answer line equaling 24 |
| Generate | **propose** sequential next arithmetic step |
| Evaluate | **value** sure/likely/impossible on remaining numbers; last-step judge |
| Select | **greedy** top `n_select_sample` (paper b=5 typical) |
| steps | 4 (3 ops + answer) |
| Reward | sympy simplify == 24 and digit multiset match |
| Paper config sketch | propose1_value3_greedy5 |

### Special decisions
- Remaining numbers parsed from `(left: ...)`
- When left is 24 → switch to CoT prompt to emit Answer
- Duplicate partial strings get value 0 in batch (local cache)
- Global `value_cache` keyed by full value_prompt string

---

## 2. Creative Writing

| Item | Detail |
|---|---|
| Files | `tasks/text.py`, `prompts/text.py`, `scripts/text/*.sh` |
| Input | sentence that must end each of 4 paragraphs |
| Output | plan + coherent 4-paragraph passage |
| Generate | **sample** with standard or cot; stop after plan at step 0 |
| Evaluate | **vote** among candidates |
| Select | greedy by vote counts |
| steps | 2 (plan → passage) |
| Reward | mean coherency score 1–10 from score_prompt ×5 |

### Special decisions
- `stops[0]='\nPassage:\n'` forces plan-only first thought
- Vote conclusion line must contain choice id
- Optional compare_prompt for pairwise (not main BFS path)

---

## 3. Mini Crosswords

| Item | Detail |
|---|---|
| Files | `tasks/crosswords.py`, `prompts/crosswords.py`, DFS notebook |
| Input | 5h + 5v clues |
| State | 5×5 board, 10 answer slots, status flags |
| Generate | **propose** actions `h#./v#. word (confidence)` |
| Evaluate | confidence aggregation + **value** sure/maybe/impossible for prune |
| Search | **DFS** (notebook), not BFS solve |
| Reward | r_letter, r_word, r_game |
| Done | solved or steps≥20; DFS also time_limit / max_per_state |

### DFS decisions
- Skip if any status==2 (constraint violation from overwrite)
- Prune if `impossible` count ≥ 1 when prune=True
- max_per_state caps branching per node
- Cache propose results by rendered obs

---

## 4. Baselines (same prompts)

| Mode | Flags | Behavior |
|---|---|---|
| Standard IO | naive_run + prompt_sample=standard | one-shot full answer |
| CoT | naive_run + prompt_sample=cot | one-shot with steps/thoughts |
| ToT-BFS | solve + generate/evaluate/select | tree beam search |
| ToT-DFS | notebook dfs | crosswords only |

---

## 5. Mapping to ARSENAL / LATS

| ToT concept | LATS extension | ARSENAL layer |
|---|---|---|
| BFS beam select | UCT select | L3 |
| propose/sample generate | LM expand thoughts/actions | L3 |
| value/vote | LM value + env reward | L3 |
| — | rollout + backprop | L3 |
| — | self-reflection on failures | L3∩L5 |
| task.steps fixed depth | max_depth / iterations | L3 |

---

## 6. Config cheat sheet (from README)

```
--method_generate sample|propose
--method_evaluate value|vote
--method_select greedy|sample
--n_generate_sample N
--n_evaluate_sample M
--n_select_sample b   # beam width
--naive_run
--prompt_sample standard|cot
```

## 7. Paper shell configs (exact flags from `scripts/`)

| Shell | Flags (essence) |
|---|---|
| `game24/bfs.sh` | propose, value, greedy, `n_evaluate_sample=3`, `n_select_sample=5`, idx 900–1000 |
| `game24/standard_sampling.sh` | naive, standard, `n_generate_sample=100` |
| `game24/cot_sampling.sh` | naive, cot, `n_generate_sample=100` |
| `text/bfs.sh` | sample, vote, greedy, `n_generate_sample=5`, `n_evaluate_sample=5`, `n_select_sample=1`, cot, `temperature=1.0`, idx 0–100 |
| `text/standard_sampling.sh` | naive, standard, n=10, temp=1.0 |
| `text/cot_sampling.sh` | naive, cot, n=10, temp=1.0 |
| `crosswords/standard_sampling.sh` | naive, standard, n=10, idx 0–20 |
| `crosswords/cot_sampling.sh` | naive, cot, n=10, idx 0–20 |
| DFS notebook | `prune=True/False`, `max_per_state=3`, `time_limit=100`, propose n=8 |

## 8. Crosswords render helpers (env surface)

| Method | Purpose |
|---|---|
| `render_board` / `render_gt_board` | current vs ground-truth 5×5 |
| `render_clues` | h1–h5 / v1–v5 clue list |
| `render_ans` / `render_gt_ans` | clue + filled word by status filter |
| `render` | board + Unfilled/Filled/Changed sections (fed to propose_prompt) |
| `set_status` | sync env to trajectory y before propose/evaluate |
| `get_ans` | derive 10 words from board (rows + cols) |
