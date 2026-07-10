# OPRO — Research / System Summary

Paper: https://arxiv.org/abs/2309.03409  
Code: https://github.com/google-deepmind/opro  
Audited commit: `a76bdce2cbf6d4a0d1e570a6fcfe17be9c2abdd7`

## Core idea

**Optimization by PROmpting (OPRO):** describe an optimization problem in natural language; an LLM iteratively proposes new solutions conditioned on a **meta-prompt** that lists previous solutions and their objective values (scores). New solutions are evaluated, scored, and added back into the meta-prompt.

Main application: **instruction / prompt optimization** for LLM scorers on GSM8K, BIG-Bench Hard, and MMLU. Also demonstrated on classical objectives: **linear regression** (minimize MSE via (w,b)) and **TSP** (minimize tour length).

Paper headline results (context): optimized prompts can beat human-designed prompts by up to ~8% on GSM8K and up to ~50% on BBH (depending on model pairings).

## Architecture in code

```
optimize_instructions.main
  → load dataset (gsm8k / bbh / mmlu), split train/eval/test
  → bind call_scorer_server_func, call_optimizer_server_func
  → opt_utils.run_evolution(...)

run_evolution
  → score initial_instructions
  → for i_step in num_search_steps:
       gen_meta_prompt(...)
       optimizer LLM → parse <INS>...</INS> or [text]
       filter candidates
       evaluate_single_instruction on train
       update history / optional few-shot wrong-question stats
       periodic eval fold
```

Supporting:

- `eval_utils.gen_prompt` — place instruction at before_Q / Q_begin / Q_end / A_begin  
- `eval_utils.evaluate_single_instruction` — batch score accuracy  
- `metrics.get_normalized_prediction` — parse free-form answers  
- `prompt_utils` — OpenAI ChatCompletion + PaLM text-bison with retries  

## Meta-prompt types

| Type | Typical optimizer | Contents |
|---|---|---|
| `both_instructions_and_exemplars` | GPT-3.5/4 or text-bison | Prior (instruction, score) + optional few-shot wrong/right QA exemplars |
| `instructions_only` | Pretrained-style | Compact “create a piece of text at {position} for {task}” + scored history |

Instruction positions: `before_Q`, `Q_begin`, `Q_end`, `A_begin` (A_begin uses `<Start>` tags for GPT).

## Optimization domains

| Domain | Entry | Solution form | Objective |
|---|---|---|---|
| Instruction opt | `optimize_instructions.py` | natural language instruction | train accuracy |
| Linear regression | `optimize_linear_regression.py` | `[w, b]` | lower function value |
| TSP | `optimize_tsp.py` | `<trace>...</trace>` | shorter tour |

## Key loops

1. **Evolution steps** `for i_step in range(num_search_steps)`  
2. **Generate until N candidates** `while remaining_num_instructions_to_generate > 0`  
3. **Score each candidate** on train indices  
4. **Evaluate entry** over instruction list × dataset fold  
5. **API retries** on timeout/rate-limit/errors  

## Key decisions

- Optimizer vs scorer model (can differ)  
- Meta-prompt type; instruction position; include_qa  
- Few-shot selection: accumulative_most_frequent / current_most_frequent / constant / random  
- Temperature schedule: constant vs linear_increase  
- Skip long instructions (>500), GSM8K digits, leaked `INS`, MD5 duplicates  
- Score threshold for including old instructions in meta-prompt  
- Bucketize scores vs full float  
- Multiple-choice vs free-form metrics  

## Inputs / Outputs

**Inputs:** dataset, task, API keys, optimizer/scorer names, instruction_pos, meta_prompt_type, initial_instructions, split ratios, search steps, temperatures.  

**Outputs:** per-instruction CSV accuracies, configs_dict.json, history of (instruction, score, step), meta_prompts list, best instructions by train/eval score, optional `misc/prompt_history` logs from paper runs.

## Strengths for extraction / ARSENAL

- Clean **meta-prompt as optimizer state** pattern.  
- Explicit complement to **APE** (one-shot candidate gen vs multi-step score-conditioned search).  
- Fits ARSENAL **L1** as iterative instruction search when demos/scores available.
