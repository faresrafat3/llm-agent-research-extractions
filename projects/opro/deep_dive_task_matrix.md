# OPRO — Deep Dive Task / Phase Matrix

## Universal OPRO algorithm

| Phase | Code | Input | Output | Loop | Key decision | Stop |
|---|---|---|---|---|---|---|
| Load data | optimize_instructions.main | dataset, task | raw_data, indices | no | gsm8k/bbh/mmlu | — |
| Bind models | main | scorer/optimizer names | call_*_func | no | GPT vs palm | — |
| Score seeds | run_evolution | initial_instructions | (ins, score, -1) | over seeds | — | — |
| Build meta-prompt | gen_meta_prompt | history, exemplars | meta_prompt | no | type/pos/few-shot | — |
| Propose | optimizer LLM | meta_prompt, T | raw text | generate while | parse tags | remaining=0 |
| Filter | run_evolution | candidates | to_evaluate | over cands | length/digit/INS/dup | — |
| Score | evaluate_single_instruction | instruction, train idx | accuracy | batches | metrics path | retries |
| Update history | run_evolution | score | old_instructions_and_scores | no | threshold for next meta | — |
| Periodic eval | run_evolution | eval_index | eval scores | every eval_interval | — | steps done |

---

## 1. Instruction optimization (main paper app)

| Item | Detail |
|---|---|
| Entry | `optimize_instructions.py` |
| Core | `run_evolution` + `gen_meta_prompt` |
| Scorer prompt | `gen_prompt` with instruction_pos |
| Default seed | `"Let's solve the problem."` |
| Datasets | GSM8K, BBH (27 tasks in repo data), MMLU |
| Objective | maximize train accuracy (0–1, shown ×100 in meta-prompt text) |
| Paper histories | `misc/prompt_history/BBH-*-s-text-bison-o-palm-2-l-it.txt` |

### Few-shot selection for meta-prompt exemplars

| Criteria | Behavior |
|---|---|
| `accumulative_most_frequent` | indices wrong most often since start |
| `current_most_frequent` | wrong most often under instructions currently in meta-prompt |
| `constant` | fixed random seed 0 subset of train |
| `random` | re-sample each step |

---

## 2. Linear regression demo

| Item | Detail |
|---|---|
| Variables | w, b |
| History | sorted by value (lower better) |
| Proposal | `[w, b]` |
| Meta-prompt | minimize function; no code |

---

## 3. TSP demo

| Item | Detail |
|---|---|
| Solution | permutation trace |
| Tags | `<trace> ... </trace>` |
| Objective | minimize length; visit each point once |

---

## 4. Evaluation-only path

`evaluate_instructions.py`: load instructions, score on train and/or test folds with same `evaluate_single_instruction` machinery — no evolution.

---

## 5. Mapping to APE / ARSENAL

| Capability | APE | OPRO |
|---|---|---|
| Candidate generation | LLM from demos (forward) | LLM from scored history meta-prompt |
| Scoring | likelihood / UCB bandits | task accuracy via scorer LLM |
| Iteration | generate then rank (bandits explore) | multi-step evolution |
| ARSENAL L1 | baseline one-shot | iterative mode when budget allows |

Recommended cascade: **APE warm-start → OPRO refine**, or **OPRO alone** with seed instructions.

---

## 6. Config cheat sheet (instruction opt)

```
--optimizer gpt-3.5-turbo | gpt-4 | text-bison
--scorer text-bison | gpt-*
--dataset gsm8k | bbh | mmlu
--task train | <bbh_task> | <mmlu_subject>
--instruction_pos Q_begin | Q_end | before_Q | A_begin
--meta_prompt_type both_instructions_and_exemplars | instructions_only
num_search_steps, num_generated_instructions_in_each_step
old_instruction_score_threshold, max_num_instructions
optimizer_llm_temperature[_schedule|_end]
few_shot_qa_pairs, few_shot_selection_criteria
```
