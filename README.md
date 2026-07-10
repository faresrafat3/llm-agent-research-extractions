# LLM Agent Research Systems — High-Quality Prompt, Logic, Flow, and Graph Extractions

This repository is a consolidated research/audit archive for seven important LLM agent and self-improvement systems:

1. AI Scientist v2
2. Self-Refine
3. Reflexion
4. Meta-Prompting
5. LATS / Language Agent Tree Search
6. APE / Automatic Prompt Engineer
7. The Prompt Report — Systematic Survey of Prompt Engineering Techniques

Every project is structured to the same quality standard as much as the original repository structure allows:

- research/system summary,
- complete prompt extraction,
- Python logic/flow extraction,
- deep-dive task or phase matrix,
- Mermaid graph in English,
- Mermaid graph in Arabic,
- final Arabic audit/completeness checklist,
- quality review notes,
- raw prompt/config files where applicable.

## Projects

| Project | Folder | Standalone repo |
|---|---|---|
| AI Scientist v2 | `projects/ai-scientist-v2/` | https://github.com/faresrafat3/ai-scientist-v2-prompts-extraction |
| Self-Refine | `projects/self-refine/` | https://github.com/faresrafat3/self-refine-full-extraction |
| Reflexion | `projects/reflexion/` | https://github.com/faresrafat3/reflexion-full-extraction |
| Meta-Prompting | `projects/meta-prompting/` | https://github.com/faresrafat3/meta-prompting-full-extraction |
| LATS | `projects/lats/` | https://github.com/faresrafat3/lats-full-extraction |
| APE | `projects/ape/` | https://github.com/faresrafat3/ape-full-extraction |
| Prompt Report | `projects/prompt-report/` | https://github.com/faresrafat3/prompt-report-full-extraction |

## Recommended reading order

### AI Scientist v2

1. `projects/ai-scientist-v2/README.md`
2. `projects/ai-scientist-v2/research_summary.md`
3. `projects/ai-scientist-v2/deep_dive_task_matrix.md`
4. `projects/ai-scientist-v2/ai_scientist_v2_prompts_complete.md`
5. `projects/ai-scientist-v2/logic_flow_extract/python_logic_flow_complete.md`
6. `projects/ai-scientist-v2/logic_flow_extract/graph_english.md`
7. `projects/ai-scientist-v2/logic_flow_extract/graph_arabic.md`
8. `projects/ai-scientist-v2/final_completeness_check_ar.md`
9. `projects/ai-scientist-v2/QUALITY_REVIEW_AR.md`

### Self-Refine

1. `projects/self-refine/README.md`
2. `projects/self-refine/research_summary.md`
3. `projects/self-refine/deep_dive_task_matrix.md`
4. `projects/self-refine/deep_dive_paper_appendix_notes.md`
5. `projects/self-refine/prompts_complete.md`
6. `projects/self-refine/python_logic_flow_complete.md`
7. `projects/self-refine/graph_english.md`
8. `projects/self-refine/graph_arabic.md`
9. `projects/self-refine/final_completeness_check_ar.md`
10. `projects/self-refine/QUALITY_REVIEW_AR.md`

### Reflexion

1. `projects/reflexion/README.md`
2. `projects/reflexion/research_summary.md`
3. `projects/reflexion/deep_dive_task_matrix.md`
4. `projects/reflexion/prompts_complete.md`
5. `projects/reflexion/python_logic_flow_complete.md`
6. `projects/reflexion/graph_english.md`
7. `projects/reflexion/graph_arabic.md`
8. `projects/reflexion/final_completeness_check_ar.md`
9. `projects/reflexion/QUALITY_REVIEW_AR.md`


### Meta-Prompting

1. `projects/meta-prompting/README.md`
2. `projects/meta-prompting/research_summary.md`
3. `projects/meta-prompting/deep_dive_task_matrix.md`
4. `projects/meta-prompting/prompts_complete.md`
5. `projects/meta-prompting/python_logic_flow_complete.md`
6. `projects/meta-prompting/graph_english.md`
7. `projects/meta-prompting/graph_arabic.md`
8. `projects/meta-prompting/final_completeness_check_ar.md`
9. `projects/meta-prompting/QUALITY_REVIEW_AR.md`


### LATS

1. `projects/lats/README.md`
2. `projects/lats/research_summary.md`
3. `projects/lats/deep_dive_task_matrix.md`
4. `projects/lats/prompts_complete.md`
5. `projects/lats/python_logic_flow_complete.md`
6. `projects/lats/graph_english.md`
7. `projects/lats/graph_arabic.md`
8. `projects/lats/final_completeness_check_ar.md`
9. `projects/lats/QUALITY_REVIEW_AR.md`

### APE

1. `projects/ape/README.md`
2. `projects/ape/research_summary.md`
3. `projects/ape/deep_dive_task_matrix.md`
4. `projects/ape/prompts_complete.md`
5. `projects/ape/python_logic_flow_complete.md`
6. `projects/ape/graph_english.md`
7. `projects/ape/graph_arabic.md`
8. `projects/ape/final_completeness_check_ar.md`
9. `projects/ape/QUALITY_REVIEW_AR.md`

### Prompt Report

1. `projects/prompt-report/README.md`
2. `projects/prompt-report/research_summary.md`
3. `projects/prompt-report/deep_dive_task_matrix.md`
4. `projects/prompt-report/prompts_complete.md`
5. `projects/prompt-report/python_logic_flow_complete.md`
6. `projects/prompt-report/graph_english.md`
7. `projects/prompt-report/graph_arabic.md`
8. `projects/prompt-report/final_completeness_check_ar.md`
9. `projects/prompt-report/QUALITY_REVIEW_AR.md`

## ARSENAL — Unified Master Pipeline

The seven extractions are also fused into one operational master system:

- Folder: `master-unified-pipeline/`
- Standalone repo: https://github.com/faresrafat3/arsenal-unified-master-pipeline
- English graph: `master-unified-pipeline/graphs/MASTER_UNIFIED_ENGLISH.md`
- Arabic graph: `master-unified-pipeline/graphs/MASTER_UNIFIED_ARABIC.md`

Layers: L0 Prompt Report router → L1 APE → L2 Meta-Prompting → L3 LATS → L4 Self-Refine → L5 Reflexion → L6 AI Scientist v2 stages.

## Master graphs

- `MASTER_GRAPH_ENGLISH.md`
- `MASTER_GRAPH_ARABIC.md`

## Final reviews

- `FINAL_REVIEW_AND_COMPLETENESS_AR.md`
- `QUALITY_STANDARD_AR.md`

## Archives

ZIP deliverables are stored in:

```text
archives/
```

## Quality policy

- Source code is treated as the source of truth.
- Papers/docs are used as research context and cross-checks.
- Runtime outputs/logs are not mixed with operational prompts unless they contain important examples.
- Mermaid graphs are designed to be readable high-level maps; line-level details are in Markdown/JSON inventories.

## Root-level consolidated files

- `research_summary.md` — consolidated summary across all seven systems.
- `deep_dive_task_matrix.md` — comparative matrix.
- `prompts_complete.md` — index pointing to project prompt extractions.
- `python_logic_flow_complete.md` — index pointing to project logic reports.
- `graph_english.md` / `graph_arabic.md` — root aliases of the master graphs.
- `final_completeness_check_ar.md` — consolidated Arabic completeness check.
- `QUALITY_REVIEW_AR.md` — consolidated Arabic quality review.
