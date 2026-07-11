# STORM — Full Prompt, Logic, Flow, and Graph Extraction

Paper: **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models**  
ArXiv: https://arxiv.org/abs/2402.14207 (NAACL 2024)  
Code: https://github.com/stanford-oval/storm (knowledge-storm package)  
Audited: v2 Apr 8 2024, 27 pages, 8,683 KB  
Demo: https://storm.genie.stanford.edu (70k+ users)

## Why this package

STORM solves underexplored **pre-writing stage** before generating Wikipedia-like long-form grounded articles: how to research topic and prepare outline prior to writing. Traditional RAG fails because much information cannot be surfaced via simple topic searches; direct prompting LLMs produces basic What/When/Where questions limited planning capacity.

STORM introduces **STORM paradigm = Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking** with two stages:

1. **Pre-writing:** research via perspective-guided question asking + simulated conversations grounded on trusted Internet sources, curated into outline
2. **Writing:** outline + references → full-length article with citations section-by-section

Key innovations:

1. **Perspective discovery** by surveying related Wikipedia pages from similar topics: generate related topics → extract their tables of contents via Wikipedia API → concatenate TOCs → prompt LLM to identify N perspectives that collectively contribute comprehensive article + p0 basic fact writer
2. **Simulated conversations** iterative research: Wikipedia writer guided by perspective asks questions, expert grounded on Internet sources answers via search_and_sift, multi-turn N+1 conversations {C0,C1,..,CN} with M rounds each (hyperparameters N=5 M=5)
3. **Outline curation** via LLM intrinsic knowledge: draft outline OD given only topic t → refined outline O given topic + OD + conversations
4. **Full article generation** section-by-section: section title + subheadings used retrieve relevant docs from R via Sentence-BERT embeddings, LLM generates section with citations, concatenated, delete repeated info improve coherence, synthesize lead summary

This extraction feeds CONSTITUTION Part 6 knowledge synthesis / tracking.

## Package contents

```text
storm-full-extraction/
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
│   ├── GenRelatedTopicsPrompt.txt
│   ├── GenPerspectivesPrompt.txt
│   ├── GenQnPrompt.txt
│   ├── GenQueriesPrompt.txt
│   ├── GenAnswerPrompt.txt
│   ├── DirectGenOutlinePrompt.txt
│   ├── RefineOutlinePrompt.txt
│   ├── algorithm1_pseudocode.py
│   └── prewriting_vs_writing_stage.md
├── raw_data_samples/
│   ├── freshwiki_sample.json
│   ├── outline_eval_metrics.json
│   └── conversation_example.json
└── archives/storm_full_extract.zip
```

## Tasks

| Task | Setup | Domain | Eval |
|---|---|---|---|
| Perspective discovery | Given topic t, survey related Wikipedia articles | All domains | Diversity perspectives coverage |
| Information-seeking conversation simulation | N+1 perspectives basic + 5 perspectives, M=5 rounds per perspective, question asker + expert | All | Depth breadth questions vs direct prompting What When Where |
| Outline creation | Draft OD from topic only + Refine O from topic+OD+conversations | All | Heading soft recall Sentence-BERT paraphrase-MiniLM-L6-v2, heading entity recall FLAIR NER vs human-written ground truth |
| Full-length article generation | Topic + Outline + References R, retrieve docs per section via Sentence-BERT similarity, generate section with citations | All | Automatic Prometheus 13B open evaluator Interest Coherence Organization Relevance Focus Coverage trimmed 2000 words, citation recall precision Gao et al Mistral 7B, expert Wikipedia editors organized +25% absolute, broad coverage +10% vs outline-driven RAG baseline |

## Implementation

- Zero-shot prompting using DSPy framework Khattab et al 2023
- Hyperparameters N=5 perspectives M=5 conversation rounds
- LM: chat model gpt-3.5-turbo for question asking, gpt-3.5-turbo-instruct for other parts, also experiment gpt-4 for drafting refining outline
- Retrieval: simulated topic expert grounded on You.com search API, compatible other search engines BingSearch VectorRM SerperRM BraveRM etc (knowledge-storm rm.py), ground truth Wikipedia article excluded search results
- FreshWiki dataset curating recent high-quality Wikipedia articles to avoid data leakage: top 100 most-edited pages per month Feb 2022-Sep 2023, filter B-class quality ORES, exclude list articles no subsections, plain text only
- Modular installation pip install knowledge-storm, support litellm integration language models embedding models

## Recommended reading order

1. research_summary.md
2. deep_dive_task_matrix.md
3. prompts_complete.md
4. python_logic_flow_complete.md
5. graph_english.md / graph_arabic.md
6. final_completeness_check_ar.md

## Related extractions

- GAPMAP (explicit gap extraction → perspective failure identification): https://github.com/faresrafat3/gapmap-full-extraction
- ResearchAgent (context-augmented planner → STORM perspective): https://github.com/faresrafat3/researchagent-full-extraction
- Scientific Intelligence Survey (P2 Context-Augmented, P5 Role-Interactive, P3 Reflective, V2 tool-based, V3 HITL): https://github.com/faresrafat3/scientific-intelligence-survey-full-extraction
- SciMON/SciPIP (iterative novelty boosting vs perspective-guided questioning): https://github.com/faresrafat3/scimon-scipip-full-extraction
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions

## Quality policy

- Source truth: PDF Listings 1-2 prompts + Algorithm 1 pseudocode + Figure 2 overview + Sec 3.1-3.4
- Paper used as verification
- No hallucination beyond paper description
