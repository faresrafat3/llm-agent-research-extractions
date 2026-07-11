# GAPMAP — Full Prompt, Logic, Flow, and Graph Extraction

Paper: **GAPMAP: Mapping Scientific Knowledge Gaps in Biomedical Literature Using Large Language Models**  
ArXiv: https://arxiv.org/abs/2510.25055 (NeurIPS 2025 Workshop AI for Science)  
Source code: https://github.com/lhunter-lab/GAPMAP  
Audited commit: `b0145b435a0c92de3d71365fb65940ef66c5166f` (Oct 31 2025)  
Paper Date: Oct 29 2025

## Why this package

GAPMAP is the first systematic study that separates **explicit gaps** (author-signaled lexical cues) from **implicit gaps** (unstated, context-inferred). It introduces:

1. **Explicit extraction** with strict JSON schema + RoBERTa-validated ignorance cues
2. **TABI — Toulmin-Abductive Bucketed Inference** for implicit gaps: Claim / Grounds → Warrant + Bucket (more_probable vs least_probable)
3. **Context-aware evaluation**: ROUGE-L F1 (0.55 threshold) for explicit, bi-directional NLI entailment (RoBERTa large, 0.4) for implicit
4. **Long-context strategy**: Stanza sentence-aligned chunking ~1000 words, full-paper pilot with GPT-4o + author survey

This extraction is part of the knowledge-tracking arc in the ARSENAL stack and feeds directly into CONSTITUTION.md Part 6.

## Package contents

```text
gapmap-full-extraction/
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
├── raw_prompt_files/
│   ├── ex_gap_xtract.py              # official explicit extraction script
│   ├── prompt_explicit_full.txt
│   ├── prompt_implicit_TABI_3shot.txt
│   ├── prompt_implicit_fullpaper.txt
│   └── chunking_logic.py
├── raw_data_samples/
│   ├── ipbes_sample.json
│   ├── covid_sample.json
│   └── implicit_paragraph_sample.json
└── archives/gapmap_full_extract.zip
```

## Tasks in official repo

| Task | Unit | Domain | Size | Metric |
|---|---|---|---|---|
| Explicit IPBES | paragraph | Biodiversity | 657 statements / 286 paras | ROUGE-L F1 |
| Explicit COVID-19 | section (up to 8K) | COVID-19 | 2894 statements / 1786 studies | Accuracy (cue-dict validated) |
| Implicit paragraph manual | paragraph | Biomedical | 212 paras / 137 articles | Entailment Accuracy |
| Implicit full-text pilot | full paper | STEM mixed 19 domains | 24 papers (23 used) | Author agreement % |

## Models benchmarked

- Closed: GPT-5, GPT-4o, GPT-4o-mini
- Open: Llama-3.3-70B-Instruct, Llama-4 Scout 17B MoE (16 experts), Llama-3.1-8B, Gemma-2-9B-it
- Evaluation models: RoBERTa-large for bi-directional entailment, Stanza for segmentation

## Recommended reading order

1. `research_summary.md`
2. `deep_dive_task_matrix.md`
3. `prompts_complete.md`
4. `python_logic_flow_complete.md`
5. `graph_english.md` / `graph_arabic.md`
6. `final_completeness_check_ar.md`
7. `QUALITY_REVIEW_AR.md`

## Related extractions

- ResearchAgent (problem identification from gaps): https://github.com/faresrafat3/researchagent-full-extraction
- Scientific Intelligence Survey (planner/memory/verifier map): https://github.com/faresrafat3/scientific-intelligence-survey-full-extraction
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions
- ARSENAL master: https://github.com/faresrafat3/arsenal-unified-master-pipeline

## Quality policy

- Source code is source of truth (ex_gap_xtract.py)
- Paper used as research context and cross-check for TABI template
- No hallucinations: all prompts verbatim or directly derived from script + paper description
- Mermaid graphs are high-level maps; line-level detail in Markdown/JSON

## Quick reproduce

```bash
pip install stanza openai pandas
export OPENAI_API_KEY=...
python raw_prompt_files/ex_gap_xtract.py  # configure csv_file_path / output_dir inside
```
