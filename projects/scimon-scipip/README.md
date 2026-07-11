
# SciMON / SciPIP — Full Prompt, Logic, Flow, and Graph Extraction

Papers: 
- **SciMON: Scientific Inspiration Machines Optimized for Novelty**  
  ArXiv: https://arxiv.org/abs/2305.14259 (v7 Jun 3 2024, ACL 2024 Long)
- **SciPIP: An LLM-based Scientific Paper Idea Proposer**  
  ArXiv: https://arxiv.org/abs/2410.23166 (v2 Feb 17 2025, deep integration semantic retrieval citation awareness)
- Related user request arXiv:2305.14579 was idling vehicles -- actual SciMON is 2305.14259, SciPIP 2410.23166 both scientific claim tracking / paper idea generation

Code: SciMON https://github.com/eaglew/clbd (CLBD), SciPIP database construction

Audited: SciMON 21 pages 8,624 KB v3, SciPIP 17 Feb 2025 v2

## Why this package

Traditional literature-based discovery LBD focused on binary link prediction severely limiting expressivity hypotheses, e.g., drug-disease links via ABC model Swanson 1986 co-occurrence intermediate concept B, word vectors Tshitoyan et al 2019, link prediction models Wang et al 2019 Sybrandt et al 2020 Xu et al 2023, scientific KG link prediction Nadkarni et al 2021, lack nuanced contexts target application settings requirements constraints motivations challenges Sosa and Altman 2022 open-ended problem settings unbounded hypothesis spaces optimizing novelty

SciMON takes dramatic departure: input background contexts (problems, motivations, experimental settings, goals) optionally seed term v focus point, output natural language ideas grounded in literature natural language, not merely paraphrase background novel w.r.t B and broader corpus. Framework: Background Context → Inspiration Retrieval (semantic neighbors, KG neighbors, citation neighbors) → Idea Generation → Iterative Novelty Boosting comparing to prior literature (Background_i, idea_i) updating until sufficient novelty achieved. Like good researcher would do. Also in-context contrastive model encourages novelty w.r.t background context.

SciPIP enhances SciMON limitations: existing retrieval keyword-based neglects crucial semantic information incomplete, even semantic vector entire sections multifaceted difficult capture key points effective encoding quality retrieval performance impact. Idea generation relies internal knowledge metadata overlooking valuable insights full texts. SciPIP proposes: construction comprehensive literature database ~78K papers top-tier AI conferences, LLM re-summarize each paper into structured quintuple keywords, backgrounds, ideas, concise methods, references individually preprocessed encoded vectors stored database precise efficient retrieval. Multi-granularity retrieval leveraging keywords semantic embeddings citation relations thorough. Dual-path framework integrates content retrieved papers + extensive internal knowledge LLM boosting novelty feasibility practical value. Experiments NLP CV domains multitude innovative useful ideas.

This extraction feeds CONSTITUTION Part 6 knowledge tracking claim / idea generation / retrieval novelty optimization.

## Package contents

```text
scimon-scipip-full-extraction/
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
│   ├── scimon_problem_setting.txt
│   ├── scimon_inspiration_retrieval_semantic_KG_citation.txt
│   ├── scimon_idea_generation_initial.txt
│   ├── scimon_iterative_novelty_boosting.txt
│   ├── scimon_in_context_contrastive.txt
│   ├── scipip_quintuple_summarization_keywords_background_ideas_methods_refs.txt
│   ├── scipip_entity_extraction_tau2.txt
│   ├── scipip_concise_methods_tau3_example_style_transform.txt
│   ├── scipip_background_transformation_teacher_student.txt
│   ├── scipip_summary_problem_main_idea_format.txt
│   ├── scipip_background_motivations_details.txt
│   ├── scipip_idea_proposer_dual_path_10_ideas.txt
│   └── evaluation_human_automated_ROUGE_BERTScore.txt
├── raw_data_samples/
│   ├── scimon_background_context_seed_term_example.json
│   ├── scimon_inspirations_example.json
│   ├── scimon_novelty_iterations_example.json
│   ├── scipip_quintuple_example.json
│   ├── scipip_entity_extraction_example.json
│   └── scipip_idea_example_10.json
└── archives/scimon_scipip_full_extract.zip
```

## Tasks

| Task | Input | Output | Retrieval | Evaluation |
|---|---|---|---|---|
| Background collection + IE KG | ACL Anthology 67,408 papers 1952-2022 Semantic Scholar Academic Graph API non-commercial, PubMed 5,708 1988-2024 Entrez, IE system PubTator 3 Islamaj et al Wei et al Luo Lai, sentence classifier background context selection Huang et al 2020, fine-tune biomedical LLM Chen et al 2023 test split past pretraining cutoff biomedical domain generalization | Background contexts M motivations experimental settings constraints + seed term v optional focus | Seed term + Context | Background contexts past problems motivations focus points Problems motivations focus points |
| Inspiration retrieval | Background context seed term | Inspirations past scientific papers: semantic neighbors, KG neighbors, citation neighbors | Semantic similarity graphs, KG, citation networks, related problems and solutions along with contexts from scientific KG, semantic neighbors st automatic speech recognition low-resource tagging etc, KG neighbors nmt-based text normalization task-oriented dialog etc, citation neighbors Contextual Augmentation Data Augmentation Words Paradigmatic Relations etc | Retrieval relevance underlined similar ground truth Table8 example |
| Idea generation | Background context + inspirations + seed term | Initial idea natural language new idea grounded literature "Given [context], a [new idea], Δ vs prior work..." | Inspirations grounded existing literature | Human evaluation relevance utility novelty technical depth, automated ROUGE-L BERTScore BARTScore ROUGE BERT with SciBERT encoder |
| Iterative novelty boosting | Idea I generated at step t + existing research literature prior papers (Background_i, idea_i) | Updated idea more novel relative prior work until sufficient novelty achieved, like good researcher would do | Compare I with existing research literature if strongly overlapping update | Comprehensive evaluation reveal GPT-4 overall low technical depth novelty methods partially mitigate |
| In-context contrastive augmentation | Background context + inspirations + contrastive examples | Novelty w.r.t background context encouraging novelty model CL, SN semantic inspirations KG KG inspirations CT citation inspirations | Contrastive examples encourage novelty reducing reliance copying | Table9 automatic evaluation challenging gold subsets R-L↑ BERT↑ GPT4ZS 0.120 0.581 0.130 0.583 GPT4FS 0.143 0.618 etc T5 0.223 0.672† 0.246 0.685 T5+CL 0.225† 0.671† T5+SN+CL 0.228† 0.671† 0.258† 0.686† T5+KG+CL 0.223† 0.248 0.681† T5+CT+CL etc differences not statistically significant p≤0.05 compared each other but still significant compared other models t-test |
| SciPIP quintuple construction | ~78K papers top-tier AI conferences | Structured quintuple keywords, backgrounds, ideas, concise methods, references individually preprocessed encoded vectors stored database | LLM re-summarize each paper | Precise efficient retrieval |
| SciPIP multi-granularity retrieval | Research problem | Retrieved literature comprehensive leveraging keywords semantic embeddings citation relations thorough exhaustive | Multi-granularity retrieval algorithm ensures more thorough results vs keyword-based neglects semantic incomplete even semantic vector entire sections multifaceted difficult capture key points | Literature retrieval results Table4 groundtruth real citations tested papers Recall10 recall rate top10 ranked among retrieved compared ground truth citations Recall10 means recall rate top10 AI Scientist Not Applicable SCIMON-like 0.381 0.481 0.548 0.587 0.616 ResearchAgent-like 0.377 0.484 0.550 0.598 0.622 SciPIP Ours 0.419 0.544 0.615 0.657 0.684 ablation Table5 SE semantic-entity based retrieval CC citation co-occurrence CL clustering Since AI Scientist does not perform literature retrieval when generating ideas results primarily on SCIMON and ResearchAgent etc |
| SciPIP dual-path idea generation | Research problem rationales + related papers summaries backgrounds contributions methods cue words | ~10 ideas clear innovative valid comprehensive about 10 entries Idea1 Idea2 ... integrating content retrieved papers + internal knowledge LLM | Content retrieved papers + extensive internal knowledge LLM integration boosts novelty feasibility practical value | Experiments NLP CV domains multitude innovative useful ideas |

## Implementation SciMON

- Automated data collection collecting examples past problems proposed ideas from scientific papers for both fine-tuning and in-context training LLMs training them take problem descriptions output proposed ideas address them
- Observe state-of-art LLMs GPT-4 OpenAI 2023 struggle generating novel scientific ideas contribute new modeling framework generating hypotheses makes progress improving ability Figure1
- Given background problem description models first dynamically retrieve inspirations from past literature in form related problems solutions along with contexts from scientific KG these retrieved inspirations serve ground generated ideas existing literature Then endow models ability iteratively boost novelty of generated ideas Given idea I at step t model compares I with existing research literature if strongly overlapping model tasked updating idea more novel relative prior work much like good researcher would do Also introduce in-context contrastive model encourages novelty w.r.t background context
- Focus AI/NLP ideas facilitate analysis AI researchers themselves also demonstrate generalization biomedical domain Design extensive evaluation experiments using human annotators domain expertise assess relevance utility novelty technical depth Methods substantially improve ability LLMs task however analyses show ideas still far behind scientific papers terms novelty depth utility raising fundamental challenges building models generate scientific ideas
- Data: 67,408 ACL Anthology papers 1952-2022 Semantic Scholar Academic Graph API under API license non-commercial Terms of Use https://allenai.org/terms dataset only non-commercial purposes human evaluation voluntary participants fair wage Further collect 5,708 PubMed papers 1988-2024 Entrez Programming Utilities API data usage guidelines
- Fine-tuning T5-based models + CL in-context contrastive augmentation + SN semantic inspirations + KG KG inspirations + CT citation inspirations

## Implementation SciPIP

- Rapid advancement LLMs opened possibilities automating proposal innovative scientific ideas process involves two key phases literature retrieval and idea generation However existing approaches fall short due reliance keyword-based search tools during retrieval phase neglects crucial semantic info frequently results incomplete retrieval outcomes Similarly idea generation phase current methodologies depend solely internal knowledge LLMs or metadata retrieved papers overlooking significant valuable insights contained within full texts
- Approach begins construction comprehensive literature database that supports advanced retrieval based not only keywords but also semantics citation relationships Complemented introduction multi-granularity retrieval algorithm ensuring more thorough exhaustive retrieval results For idea generation phase propose dual-path framework effectively integrates both content retrieved papers and extensive internal knowledge LLMs Integration significantly boosts novelty feasibility practical value proposed ideas
- Collect approximately 78K papers several top-tier academic conferences AI field utilize LLMs to re-summarize each paper into structured quintuple consisting of keywords, backgrounds, ideas, concise methods, references These components individually preprocessed e.g. encoded into vectors and stored database enable more precise efficient retrieval Based on constructed database propose multi-granularity retrieval method comprehensively leverages keywords semantic embeddings citation relations enabling thorough literature retrieval etc
- For idea generation dual-path framework integration

## Recommended reading order

1. research_summary.md
2. deep_dive_task_matrix.md
3. prompts_complete.md
4. python_logic_flow_complete.md
5. graph_english.md / graph_arabic.md

## Related extractions

- GAPMAP gap identification → SciMON background context problems motivations focus points
- ResearchAgent entity-centric knowledge store K co-occurrence vs SciMON inspiration retrieval semantic KG citation + SciPIP quintuple keywords backgrounds ideas concise methods refs + multi-granularity retrieval keywords semantic embeddings citation relations thorough
- STORM perspective-guided question asking vs SciMON iterative novelty boosting different optimization novelty vs breadth organization
- Scientific Intelligence Survey P2 Context-Augmented (historical records KB) + P4 Search-Based (tree over plan spaces) + P3 Deliberative Reflective (generate initial reflect flaws revise) + L1 SFT fine-tuning T5 + V1 self-critique + V2 tool-based
- Consolidated https://github.com/faresrafat3/llm-agent-research-extractions
