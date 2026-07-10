# Tree of Thoughts (ToT) — Full Prompt, Logic, Flow, and Graph Extraction

Paper: [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) (NeurIPS 2023)  
Code: https://github.com/princeton-nlp/tree-of-thought-llm  
Audited commit: `8050e67d0e3a0fddc424d7fa5801538722a4c4cc`  
GitHub: ~6,024 stars (verified 2026-07-10)

## Why this package

ToT generalizes Chain-of-Thought into a **search tree over intermediate thoughts**, with:

1. **Thought generation** (sample independent thoughts *or* propose sequential next steps),
2. **State evaluation** (independent value scoring *or* multi-candidate voting),
3. **Search** (BFS with beam width `b`, or DFS with pruning for crosswords).

It is a foundational reasoning/search paper that LATS later extends with MCTS + environment feedback + reflection. Extracting ToT completes the search-family arc in the ARSENAL stack (ToT → LATS).

## Package contents

```text
tot-full-extraction/
├── README.md
├── research_summary.md
├── prompts_complete.md
├── python_logic_flow_complete.md
├── python_logic_inventory.json
├── deep_dive_task_matrix.md
├── graph_english.md
├── graph_english.mmd
├── graph_arabic.md
├── graph_arabic.mmd
├── final_completeness_check_ar.md
├── QUALITY_REVIEW_AR.md
├── raw_prompt_files/          # prompts + bfs + run + DFS notebook
├── raw_data_samples/          # small data slices
└── archives/tot_full_extract.zip
```

## Tasks in the official repo

| Task | Search | Generate | Evaluate | Key metric |
|---|---|---|---|---|
| Game of 24 | BFS (beam) | propose | value (sure/likely/impossible) | exact 24 expression |
| Creative Writing | BFS | sample (std/CoT) | vote | coherency score 1–10 |
| Mini Crosswords | DFS (+ prune) | propose | value + confidence | letter/word/game reward |

## Recommended reading order

1. `research_summary.md`
2. `deep_dive_task_matrix.md`
3. `prompts_complete.md`
4. `python_logic_flow_complete.md`
5. `graph_english.md` / `graph_arabic.md`
6. `final_completeness_check_ar.md`
7. `QUALITY_REVIEW_AR.md`

## Related extractions in this project series

- LATS (builds on ToT with MCTS): https://github.com/faresrafat3/lats-full-extraction
- Meta-Prompting (also uses Game of 24): https://github.com/faresrafat3/meta-prompting-full-extraction
- ARSENAL unified pipeline: https://github.com/faresrafat3/arsenal-unified-master-pipeline
- Consolidated archive: https://github.com/faresrafat3/llm-agent-research-extractions

## Quality policy

- Source code is the source of truth.
- Paper used as research context and cross-check.
- Runtime logs under `logs/` are not mixed into operational prompts (trajectories only).
- Mermaid graphs are high-level maps; line-level detail is in Markdown/JSON inventories.
