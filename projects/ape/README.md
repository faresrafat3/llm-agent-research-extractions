# APE — Complete Prompt, Logic, Flow, and Graph Extraction

Paper: https://arxiv.org/abs/2211.01910  
Source code: https://github.com/keirp/automatic_prompt_engineer  
Audited commit: `eac521c79a78965245ce7745dcc9f6b0792c7ec7`

## Files

- `research_summary.md` — paper/system summary.
- `prompts_complete.md` — prompt sources and Python prompt builders.
- `raw_prompt_files/` — selected raw prompt/source examples.
- `raw_data_samples/` — copied input datasets/benchmarks.
- `python_logic_flow_complete.md` — AST-assisted logic extraction.
- `python_logic_inventory.json` — machine-readable inventory.
- `deep_dive_task_matrix.md` — operational deep dive.
- `graph_english.md` / `graph_english.mmd` — Mermaid graph in English.
- `graph_arabic.md` / `graph_arabic.mmd` — Mermaid graph in Arabic.
- `final_completeness_check_ar.md` — Arabic completeness check.
- `final_audit_review_ar.md` — Arabic final audit review.
- `QUALITY_REVIEW_AR.md` — Arabic quality review.

## Notes

APE treats prompts as programs. Generation via LLM from demos, evaluation via likelihood or UCB bandits.
