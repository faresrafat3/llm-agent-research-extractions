# OPRO — Python Logic Flow Complete

Audited commit: `a76bdce2cbf6d4a0d1e570a6fcfe17be9c2abdd7`

---

## 1. Entry points

| Script | Role |
|---|---|
| `optimization/optimize_instructions.py` | CLI + dataset load + `run_evolution` |
| `evaluation/evaluate_instructions.py` | Score fixed instruction list on folds |
| `optimization/optimize_linear_regression.py` | OPRO on (w,b) MSE |
| `optimization/optimize_tsp.py` | OPRO on tour traces |
| `prompt_utils.py` | OpenAI / PaLM call + retry |

Flags (instruction opt, core):  
`optimizer`, `scorer`, `dataset`, `task`, `instruction_pos`, `meta_prompt_type`, API keys.

---

## 2. `run_evolution` (instruction optimization)

### 2.1 Setup
- Assert dataset ∈ {mmlu, bbh, gsm8k}
- Save `configs_dict.json`
- Build train/eval index; BBH expands multi-task multiple-choice masks
- Structures: `old_instructions_and_scores`, `meta_prompts`, `instruction_score_dict`, wrong-question counters, eval dicts

### 2.2 Score initial instructions
```
for instruction in initial_instructions:
  df = evaluate_single_instruction(... train_index ...)
  score = mean(df.accuracy)
  append (instruction, score, step=-1)
  update wrong_questions_from_start_counter
  save CSV by instruction filename
```

### 2.3 Evolution loop
```
for i_step in range(num_search_steps):
  # temperature schedule
  if linear_increase:
    T = T0 + (i_step/num_steps)*(T_end-T0)
  else: T = T0

  # optional few-shot index selection
  if few_shot_qa_pairs:
    select few_shot_index_list by criteria:
      accumulative_most_frequent | current_most_frequent | constant | random

  meta_prompt = gen_meta_prompt(...)
  meta_prompts.append((meta_prompt, i_step))

  # generate candidates
  remaining = num_generated_instructions_in_each_step
  while remaining > 0:
    raw_outputs = call_optimizer_server_func(meta_prompt, temperature=T)
    parse tags / brackets → generated_instructions_raw
    remaining -= ...

  # dedupe by MD5 filename hash
  # filter: len<=500; gsm8k no digits; no "INS" substring
  to_evaluate_instructions = filtered

  # optional eval generated/old on few-shot only
  # train-score each new instruction
  for instruction in to_evaluate_instructions:
    df = evaluate_single_instruction(... train_index ...)
    score = mean accuracy
    append to old_instructions_and_scores
    update wrong-question counters

  # periodic eval fold if i_step % eval_interval == 0
  # save checkpoints / histories
```

### 2.4 Parse optimizer output
- GPT: slice between `<INS>`…`</INS>` or `<Start>`…`</Start>` (missing tags → start/end fallbacks)
- text-bison: extract square-bracket text

---

## 3. `gen_meta_prompt` decisions

| Condition | Effect |
|---|---|
| `instruction_pos` ∉ allowed | assert fail |
| `meta_prompt_type` both vs instructions_only | different template family |
| optimizer GPT vs text-bison | different headers/closings and exemplar wording |
| `few_shot_qa_pairs` | include exemplar section |
| `instructions_before_exemplars` | order of sections |
| `old_instruction_score_threshold` | drop low-score history from meta-prompt |
| `max_num_instructions` | keep top-scoring tail after sort |
| `num_score_buckets` | bucketize displayed scores |
| dataset mmlu/bbh/gsm8k | how question/answer pulled for exemplars |

---

## 4. `evaluate_single_instruction` / scoring

```
for each eval index (batched, optional parallel):
  prompt = gen_prompt(data, instruction, idx, include_qa, instruction_pos, dataset)
  raw = call_scorer_server_func(prompt)
  optional second prompt for final answer extraction
  parse prediction via metrics.normalize
  accuracy vs true answer
return DataFrame[raw_prompt, raw_answer, parsed_answer, true_answer, accuracy]
```

Retries: `max_retry` with `sleep_time` on failures.

### Metrics notes (`metrics.py`)
- Number-included accuracy for GSM-style  
- Bracketed choice extraction for MC  
- Bool / number adaptive normalization  
- GPT `\boxed{}` handling when flagged  

---

## 5. Linear regression optimizer (pattern)

```
initialize random (w,b) evaluations
for steps:
  meta_prompt = history of (w,b,value) sorted
  optimizer proposes new [w,b]
  parse brackets; evaluate objective; add to set
```

Stop: step budget / unique pairs.

---

## 6. TSP optimizer (pattern)

```
initialize traces
for steps:
  meta_prompt with prior traces + lengths
  propose <trace>...</trace>
  validate permutation of points; score length; keep
```

---

## 7. Model API layer (`prompt_utils`)

| Function | Behavior |
|---|---|
| `call_openai_server_single_prompt` | ChatCompletion; recursive retry on Timeout/RateLimit/API/Connection/ServiceUnavailable/OSError |
| `call_openai_server_func` | map over list of prompts |
| `call_palm_server_from_cloud` | text-bison-001 generate_text; bare except retry sleep 10 |

---

## 8. Decision catalog

| ID | Decision |
|---|---|
| D1 | dataset gsm8k / bbh / mmlu |
| D2 | optimizer vs scorer model |
| D3 | instruction_pos placement |
| D4 | meta_prompt_type both vs instructions_only |
| D5 | few_shot on/off + selection criteria |
| D6 | temperature schedule constant vs linear_increase |
| D7 | include history score ≥ threshold |
| D8 | skip long / digit / INS / duplicate candidates |
| D9 | multiple-choice metric path vs free-form |
| D10 | extract_final_answer_by_prompting_again |
| D11 | evaluate_in_parallel (False for GPT scorer) |
| D12 | periodic eval fold interval |
| D13 | A_begin uses Start tags vs INS tags |
| D14 | API error → retry sleep |

---

## 9. Loop inventory

| Loop | Bound |
|---|---|
| initial instruction scoring | len(initial_instructions) |
| evolution steps | num_search_steps |
| generate while remaining | num_generated_instructions_in_each_step |
| score new instructions | len(to_evaluate_instructions) |
| eval indices | train/eval/test sizes |
| OpenAI/PaLM retries | unbounded recursive until success (practical) |
| LR/TSP optimization steps | configured step counts |

---

## 10. I/O summary

| Stage | Input | Output |
|---|---|---|
| gen_meta_prompt | history scores, exemplars config | meta_prompt string |
| optimizer call | meta_prompt, T | raw text |
| parse | raw text | candidate instruction / (w,b) / trace |
| gen_prompt | instruction + example idx | scorer prompt |
| evaluate_single_instruction | instruction + indices | accuracy DF |
| run_evolution | kwargs config | histories, best scores, files under save_folder |
