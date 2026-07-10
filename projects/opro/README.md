# OPRO — Full Prompt, Logic, Flow, and Graph Extraction

Paper: [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409)  
Code: https://github.com/google-deepmind/opro  
Audited commit: `a76bdce2cbf6d4a0d1e570a6fcfe17be9c2abdd7`  
GitHub stars: ~762 (verified 2026-07-10) · License: Apache-2.0

## Why this package

OPRO treats an LLM as a **black-box optimizer**: at each step the model proposes new solutions from a **meta-prompt** that contains previous solutions and their scores. The main application is **prompt/instruction optimization** (GSM8K, BBH, MMLU); the same pattern is demonstrated on **linear regression** and **TSP**.

This extraction maps every meta-prompt template, evolution loop, scoring path, decision, and I/O surface to the same standard as  
https://github.com/faresrafat3/voyager-full-extraction

## Package contents

```text
opro-full-extraction/
├── README.md
├── research_summary.md
├── prompts_complete.md
├── python_logic_flow_complete.md
├── python_logic_inventory.json
├── deep_dive_task_matrix.md
├── graph_english.md / .mmd
├── graph_arabic.md / .mmd
├── final_completeness_check_ar.md
├── QUALITY_REVIEW_AR.md
├── raw_prompt_files/     # prompt_utils, optimization, evaluation, sample histories
├── raw_data_samples/     # BBH / AQuA / MMLU slices
└── archives/opro_full_extract.zip
```

## Code map

| Area | Path |
|---|---|
| Instruction optimization entry | `opro/optimization/optimize_instructions.py` |
| Evolution + meta-prompt | `opro/optimization/opt_utils.py` (`run_evolution`, `gen_meta_prompt`) |
| Linear regression demo | `opro/optimization/optimize_linear_regression.py` |
| TSP demo | `opro/optimization/optimize_tsp.py` |
| Instruction evaluation entry | `opro/evaluation/evaluate_instructions.py` |
| Scoring / prompt assembly | `opro/evaluation/eval_utils.py`, `metrics.py` |
| Model APIs | `opro/prompt_utils.py` |
| Optimization histories | `misc/prompt_history/` |

## Core idea (one loop)

```
evaluate initial instructions on train split
for step in 1..num_search_steps:
  build meta_prompt from (instruction, score) pairs [+ optional few-shot QAs]
  optimizer_llm(meta_prompt) → new candidate instructions
  filter (length, digits on gsm8k, "INS" leak, duplicates)
  score each candidate with scorer_llm on train
  append (instruction, score) to history
  periodically eval on held-out fold
return best instructions by score
```

## Relation to APE / ARSENAL

- **APE**: generate candidates once from demos, score likelihood/bandits.  
- **OPRO**: iterative **meta-prompt search** — solutions condition the next proposals.  
- ARSENAL: strengthens **L1 Instruction Optimizer** as a multi-step alternative/complement to APE.

## Recommended reading order

1. `research_summary.md`  
2. `deep_dive_task_matrix.md`  
3. `prompts_complete.md`  
4. `python_logic_flow_complete.md`  
5. `graph_english.md` / `graph_arabic.md`  
6. `final_completeness_check_ar.md`  
7. `QUALITY_REVIEW_AR.md`  

## Related extractions

- APE: https://github.com/faresrafat3/ape-full-extraction  
- Prompt Report: https://github.com/faresrafat3/prompt-report-full-extraction  
- ARSENAL: https://github.com/faresrafat3/arsenal-unified-master-pipeline  
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions  

## Quality policy

- Source code is the source of truth.  
- Paper used as research context.  
- Full BBH/MMLU corpora stay upstream; samples only.  
- Mermaid graphs are high-level maps; details in Markdown/JSON.  
