# ResearchAgent — Full Prompt, Logic, Flow, and Graph Extraction

Paper: **ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models**  
ArXiv: https://arxiv.org/abs/2404.07738 (v2 Feb 9 2025, NAACL 2025)  
Source code: https://github.com/JinheonBaek/ResearchAgent  
Audited commit: official arXiv + repo snapshot (uses GPT-4 Nov 06 2023 training cutoff Apr 2023, papers after May 01 2023)  
Authors: Jinheon Baek (KAIST), Sujay Kumar Jauhar, Silviu Cucerzan (MSR), Sung Ju Hwang (KAIST/DeepAuto)

## Why this package

ResearchAgent is the **first open-ended LLM research idea generator** that produces **Problem + Method + Experiment Design** from a core paper + citation graph + entity store, then iteratively refines via **ReviewingAgents** aligned with human preferences via criteria induction.

It models three researcher behaviors:
1. **Deep related work understanding** via academic graph (Semantic Scholar references/citations)
2. **Encyclopedic concept view** via entity-centric knowledge store (BLINK linker) co-occurrence matrix K ∈ R^{m×m}
3. **Peer feedback community** via multiple LLM ReviewingAgents with human-aligned criteria

This extraction feeds CONSTITUTION Part 6 (knowledge tracking → problem identification pipeline).

## Package contents

```text
researchagent-full-extraction/
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
│   ├── prompt_problem_identification.txt
│   ├── prompt_method_development.txt
│   ├── prompt_experiment_design.txt
│   ├── prompt_reviewing_problem.txt
│   ├── prompt_reviewing_method.txt
│   ├── prompt_reviewing_experiment.txt
│   ├── prompt_criteria_induction.txt
│   ├── prompt_evaluation_scoring.txt
│   ├── prompt_evaluation_pairwise.txt
│   └── entity_retrieval_logic.py
├── raw_data_samples/
│   ├── core_paper_sample.json
│   ├── entity_store_sample.json
│   └── idea_example_drosophila.json
└── archives/researchagent_full_extract.zip
```

## Knowledge sources

- **Core papers**: 300 sampled high-impact papers >20 citations after May 01 2023 (LLM cutoff Apr 2023, following Qi et al 2023), avg 87 references each, abstract avg 2.17 entities
- **Entity-centric store K**: 50,091 papers May–Dec 2023 + references, BLINK linker tags entities from titles+abstracts, builds sparse matrix co-occurrence counts + single entity counts
- **Entities**: topics, keywords, persons, events, etc.

## Pipeline

```
Core paper l0 + references {l1..ln} over Semantic Scholar Academic Graph
  → Entity extraction EL(l) → multiset E
  → Build K co-occurrence
  → Retrieval Ret({l0..ln};K) top-k external entities via Bayes approx P(ej|ei)P(ei) or embedding sim
  → ResearchAgent LLM(T({l0..ln}, Ret(...)))
  → Generate Problem → Method → Experiment each with rationale
  → ReviewingAgents evaluating 5 criteria per idea type → reviews + feedback + 5-point Likert
  → Iterative refinement (saturation after ~3 steps)
  → Evaluation human + model (GPT-4 judge) scoring + pairwise win ratio
```

## Evaluation criteria (5 per idea type)

| Idea | Metrics |
|---|---|
| Problem | Clarity, Relevance, Originality, Feasibility, Significance |
| Method | Clarity, Validity, Rigorousness, Innovativeness, Generalizability |
| Experiment | Clarity, Validity, Robustness, Feasibility, Reproducibility |

Human-induced criteria (Tables 13-15) align model judges to human preferences via 10 human-annotated pairs per criterion.

## Key results

- Full ResearchAgent > w/o Entity Retrieval > Naive (core only)
- Gains especially in Originality/creativity (entities provide cross-domain pollination)
- Refinement steps improve up to 3 iterations then saturation (Du et al 2023 pattern)
- Human-human Spearman 0.83/0.76/0.67 problems/methods/experiments scoring, κ pairwise 0.62/0.62/0.41; Human-model scoring 0.64/0.58/0.49, pairwise 0.71/0.62/0.52 → model proxy reasonable
- Entity retrieval ablation: w/o References drop biggest, w/o Entities second, random entities still better than none (LLM filters noise)
- High-resource domains (CS, Medicine, Eng) > low-resource (Physics, Chem, Math) likely due LLM pretraining distribution
- Outperforms SciMON and Hypothesis Proposer baselines on clarity/relevance/originality/feasibility/significance (Table 3: ResearchAgent 4.11/4.88/4.77/4.05/4.81 vs others lower)

## Recommended reading order

1. `research_summary.md`
2. `deep_dive_task_matrix.md`
3. `prompts_complete.md`
4. `python_logic_flow_complete.md`
5. `graph_english.md` / `graph_arabic.md`
6. `final_completeness_check_ar.md`

## Related

- GAPMAP (gap identification → problem formulation): https://github.com/faresrafat3/gapmap-full-extraction
- Scientific Intelligence Survey (P2/P5 planners): https://github.com/faresrafat3/scientific-intelligence-survey-full-extraction
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions

## Quality policy

- Source of truth: PDF extracted prompts Tables 6-11 + entity retrieval equations (1)(2) + criteria Tables 12-15
- Paper used as verification
- No fabricated prompts; all reconstructable from PDF
