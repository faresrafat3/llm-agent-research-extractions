# Tree of Thoughts — Python Logic Flow Complete

Audited commit: `8050e67d0e3a0fddc424d7fa5801538722a4c4cc`

---

## 1. Entry: `run.py`

```
parse_args()
  backend ∈ {gpt-4, gpt-3.5-turbo, gpt-4o}
  task ∈ {game24, text, crosswords}
  naive_run?
  prompt_sample ∈ {standard, cot}
  method_generate ∈ {sample, propose}
  method_evaluate ∈ {value, vote}
  method_select ∈ {sample, greedy}
  n_generate_sample, n_evaluate_sample, n_select_sample
  task_start_index, task_end_index

run(args):
  task = get_task(args.task)
  for i in [start, end):
    if naive_run: ys, info = naive_solve(...)
    else:         ys, info = solve(...)
    infos = [task.test_output(i, y) for y in ys]
    log JSON; accumulate avg/any accuracy
  print usage cost
```

---

## 2. Model layer: `models.py`

- `gpt(prompt, model, temperature, max_tokens, n, stop)` → list[str]
- Batches `n` in chunks of 20 via ChatCompletion
- `@backoff` on OpenAI errors
- Global `completion_tokens`, `prompt_tokens`; `gpt_usage` cost table per backend

---

## 3. Core ToT+BFS: `methods/bfs.py` → `solve`

```
x = task.get_input(idx)
ys = ['']                    # frontier of partial solutions
for step in range(task.steps):

  # ----- GENERATE -----
  if method_generate == 'sample':
    new_ys = flatten(
      get_samples(task, x, y, n_generate_sample, prompt_sample, stop=task.stops[step])
      for y in ys)
  elif method_generate == 'propose':
    new_ys = flatten(get_proposals(task, x, y) for y in ys)

  # ----- EVALUATE -----
  if method_evaluate == 'vote':
    values = get_votes(task, x, new_ys, n_evaluate_sample)
  elif method_evaluate == 'value':
    values = get_values(task, x, new_ys, n_evaluate_sample)

  # ----- SELECT -----
  if method_select == 'sample':
    select_ids ~ Multinomial(values / sum(values), k=n_select_sample)
  elif method_select == 'greedy':
    select_ids = argsort(values)[:n_select_sample]  # top-b

  ys = [new_ys[i] for i in select_ids]
  log step info

return ys, {steps: infos}
```

### Helpers

| Function | Behavior |
|---|---|
| `get_samples` | standard or cot wrap → `gpt(..., n=n_generate_sample, stop=stop)` → prepend parent `y` |
| `get_proposals` | propose wrap → one completion → split lines → each line becomes child `y + line + '\n'` |
| `get_value` | value wrap → `n_evaluate_sample` completions → unwrap; **cache** by value_prompt |
| `get_values` | loop candidates; **local cache** zeros duplicate `y` (value forced 0) |
| `get_votes` | vote wrap all ys → unwrap vote counts per candidate |

### `naive_solve`

Single-shot: `get_samples` from empty `y` only (no tree).

---

## 4. Game of 24 task logic

**Data:** `data/24/24.csv` column `Puzzles` (4 numbers).  
**steps = 4**, stops = `['\n']*4`.

### Propose path nuance
```
current = get_current_numbers(y or x)  # parse "left: a b c"
if current == '24':
  prompt = cot_prompt(original x) + 'Steps:' + y   # write final Answer
else:
  prompt = propose_prompt(current)
```

### Value path nuance
```
if last line has no 'left:':  # final answer
  value_last_step_prompt(x, answer)
else:
  value_prompt(current_numbers)
```

### Reward `test_output`
- Parse last line expression before `=`
- Digits must match original puzzle multiset
- `sympy.simplify(expr) == 24` → r=1 else 0

---

## 5. Creative Writing task logic

**Data:** lines in `data/text/data_100_random_text.txt` (forced ending sentences).  
**steps = 2**, stops = `['\nPassage:\n', None]` → step0 plans, step1 writes passage.

### Evaluation
- ToT uses **vote** across candidates (not numeric value).
- `test_output` scores final passage with `score_prompt` ×5, mean = r.

### Vote unwrap
Regex `best choice is .*(\d+)`; accumulate counts; invalid prints warning.

---

## 6. Mini Crosswords task + env

### Env state
- `board`: 25 letters / `_`
- `ans`: 10 words of length 5 (5 horiz + 5 vert)
- `status`: 0 unfilled, 1 filled, 2 filled-then-changed
- `steps`, ground truth board

### `step(action)`
- Parse `h#./v#. word` (5 letters)
- Write onto board; recompute ans; update status (conflict → 2)
- Rewards: r_all board match, r_letter /25, r_word /10
- Done if solved or steps ≥ 20

### Propose unwrap
Parse confidence lines → aggregate scores → sort desc → top `n_max_propose`.

### DFS (notebook `search_crosswords-dfs.ipynb`)
```
dfs(...):
  candidates_to_scores = GPT propose n=8 aggregated
  backup board
  for action in sorted(candidates):
    env.step(action)
    if under time_limit and steps<10 and no status==2:
      count = env.prompt_status()  # value each partial word
      record info
      if not prune or count['impossible'] < 1:
        dfs recurse
      actions.pop()
    restore board
```

Pruning: stop expanding if any partial fill is judged **impossible**.

---

## 7. Decision catalog

| ID | Decision | Location |
|---|---|---|
| D1 | naive_run vs ToT solve | run.py |
| D2 | method_generate sample vs propose | bfs.solve |
| D3 | prompt_sample standard vs cot | get_samples |
| D4 | method_evaluate value vs vote | bfs.solve |
| D5 | method_select greedy vs sample | bfs.solve |
| D6 | value cache hit? | get_value |
| D7 | duplicate candidate y? → value 0 | get_values |
| D8 | Game24 current=='24'? → cot final | propose_prompt_wrap |
| D9 | Game24 last step (no left:)? → last value prompt | value_prompt_wrap |
| D10 | Game24 4 lines without answer? → value 0 | value_outputs_unwrap |
| D11 | Crosswords action format valid? | env.step |
| D12 | Crosswords prune if impossible≥1 | dfs |
| D13 | Crosswords max_per_state / time_limit / steps≥10 | dfs |
| D14 | Vote/score regex match? | unwrap helpers |

---

## 8. Loop inventory

| Loop | Bound | File |
|---|---|---|
| task index range | end-start | run.py |
| ToT steps | task.steps | bfs.solve |
| frontier ys generate | len(ys) | bfs.solve |
| value over candidates | len(new_ys) | get_values |
| gpt batch while n>0 | n, chunk 20 | models.chatgpt |
| DFS recursion | time_limit, steps, prune | notebook |
| DFS candidate for-loop | sorted proposals | notebook |
| Text score n=5 | fixed | text.test_output |
| Crosswords prompt_status over 10 clues | 10 | env |

---

## 9. I/O summary

| Stage | Input | Output |
|---|---|---|
| get_input | idx | problem string x |
| generate | x, y partial | new_ys children |
| evaluate | x, new_ys | values[] |
| select | values, b | frontier ys |
| test_output | idx, y | {r, ...} |
| run log | all | JSON trajectories + usage |
