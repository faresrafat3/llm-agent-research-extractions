# Project Index

| Project | Source | Main extraction folder | Standalone repo | Key outputs |
|---|---|---|---|---|
| AI Scientist v2 | `SakanaAI/AI-Scientist-v2` | `projects/ai-scientist-v2/` | https://github.com/faresrafat3/ai-scientist-v2-prompts-extraction | prompts, BFTS logic, graphs, graph gap audit |
| Self-Refine | `madaan/self-refine` | `projects/self-refine/` | https://github.com/faresrafat3/self-refine-full-extraction | prompts, raw prompt files, notebook/docs audit, graphs, deep dive |
| Reflexion | `noahshinn/reflexion` | `projects/reflexion/` | https://github.com/faresrafat3/reflexion-full-extraction | prompts/configs, raw files, logic flow, graphs, deep dive |
| Meta-Prompting | `suzgunmirac/meta-prompting` | `projects/meta-prompting/` | https://github.com/faresrafat3/meta-prompting-full-extraction | prompts/configs, raw data samples, logic flow, graphs, deep dive |
| Voyager | `MineDojo/Voyager` | `projects/voyager/` | https://github.com/faresrafat3/voyager-full-extraction | curriculum, skill library, iterative prompting, EN/AR graphs |
| Tree of Thoughts (ToT) | `princeton-nlp/tree-of-thought-llm` | `projects/tot/` | https://github.com/faresrafat3/tot-full-extraction | prompts, BFS/DFS logic, EN/AR graphs, paper scripts, audit |
| LATS | `lapisrocks/LanguageAgentTreeSearch` | `projects/lats/` | https://github.com/faresrafat3/lats-full-extraction | prompts, raw data samples, MCTS/LATS logic, graphs, deep dive |
| OPRO | `google-deepmind/opro` | `projects/opro/` | https://github.com/faresrafat3/opro-full-extraction | meta-prompt evolution, instruction scoring, LR/TSP, EN/AR graphs |
| APE | `keirp/automatic_prompt_engineer` | `projects/ape/` | https://github.com/faresrafat3/ape-full-extraction | prompt generation templates, likelihood/bandit evaluation, logic flow, graphs, deep dive |
| Prompt Report | `arxiv:2406.06608` | `projects/prompt-report/` | https://github.com/faresrafat3/prompt-report-full-extraction | 58 LLM techniques + 40 multimodal, 33 vocab terms, taxonomy graphs EN/AR, deep dive |
| GAPMAP | `lhunter-lab/GAPMAP` `arxiv:2510.25055` | `projects/gapmap/` | https://github.com/faresrafat3/gapmap-full-extraction | explicit gap extraction JSON schema, TABI Claim/Grounds/Warrant/Bucket 3-shot, full-paper pilot GPT-4o multi-modal + author survey, ROUGE-L 0.55 / entailment 0.4, Stanza 1000-word chunking |
| ResearchAgent | `JinheonBaek/ResearchAgent` `arxiv:2404.07738` | `projects/researchagent/` | https://github.com/faresrafat3/researchagent-full-extraction | problem/method/experiment generation Tables 6-8, ReviewingAgents Tables 9-11, criteria Tables 12-15 induced via 10 human pairs, entity store K sparse matrix Eq1 Eq2 co-occurrence vs embedding retrieval 50,091 papers, iterative refinement saturation after 3 steps |
| Scientific Intelligence Survey | `arxiv:2503.24047` | `projects/scientific-intelligence-survey/` | https://github.com/faresrafat3/scientific-intelligence-survey-full-extraction | planner taxonomy P1-P6 L1-L2 with cathode running example Figure3, memory M1-M5, action space A1-A5, verifier V1-V4 HITL V3 approval gates evaluation feedback collaborative iteration intervention + V4 multi-agent critique tournament debate, >40 benchmarks >120 papers, applications map |
| STORM | `stanford-oval/storm` `arxiv:2402.14207` | `projects/storm/` | https://github.com/faresrafat3/storm-full-extraction | perspective discovery GenRelatedTopics + GenPerspectives N=5 + p0 basic fact writer, simulated conversations GenQn + GenQueries + GenAnswer M=5 rounds N+1=6 perspectives total ~30 Q/A, search_and_sift YouRM You.com search API search_top_k 10, draft OD + refine O # ## ###, section-by-section generation Sentence-BERT retrieval citations + polish + lead, FreshWiki top100 per month Feb2022-Sep2023 B-class ORES, heading soft recall paraphrase-MiniLM-L6-v2 cosine + entity recall FLAIR NER, Prometheus 13B Interest Coherence Organization Relevance Focus Coverage trimmed 2000 words, citation recall precision Gao Mistral 7B, expert organized +25% broad +10% vs RAG, source bias transfer over-association challenges, Co-STORM collaborative discourse protocol mind map hierarchical shared conceptual space |
| SciMON / SciPIP | `eaglew/clbd` `arxiv:2305.14259` `arxiv:2410.23166` | `projects/scimon-scipip/` | https://github.com/faresrafat3/scimon-scipip-full-extraction | background context M problems motivations experimental settings constraints + seed term v focus point, inspiration retrieval semantic neighbors KG neighbors citation neighbors Table8 Example Zhou et al 2022 underlined similar ground truth, idea generation Given [context] a [new idea] Δ vs prior work, iterative novelty boosting compare I with prior {(Background_i, idea_i)} if overlapping update more novel like good researcher Iteration1 Iteration2 ASUBD attention RL Ground Truth monotonic segmentation, in-context contrastive CL SN KG CT Table9 R-L BERT T5+SN+CL 0.228 best, human evaluation relevance utility novelty technical depth Table10 Irish language learning helpful/unhelpful Table8, biomedical 80% positive PubTator 3 KG extraction sentence classifier, quintuple keywords backgrounds ideas concise methods references ~78K papers top-tier AI individually encoded vectors, entity extraction τ2 ≤5 words ≥2 words ≤5 entities nouns, summary problem main idea format The problem of [problem] can be addressed by [main idea/approach], motivations details, concise methods τ3 example style transform, background transformation teacher student, multi-granularity retrieval SE semantic-entity CC citation co-occurrence CL clustering Table4 Recall10 0.381 SCIMON-like 0.377 ResearchAgent-like 0.419 SciPIP Ours 0.544 0.615 0.657 0.684 more thorough, dual-path idea generation ~10 ideas clear innovative valid comprehensive cue words summaries backgrounds contributions methods integrating content retrieved papers + internal knowledge avoiding stacking, non-matching ideas more valuable novel not appear human, error analysis generic suggestions woven specifics copied directly context Data preprocessing Clean text etc simple logical modifications high latency→low latency |

## Exact key file paths

### AI Scientist v2

- Prompts: `projects/ai-scientist-v2/ai_scientist_v2_prompts_complete.md`
- Logic: `projects/ai-scientist-v2/logic_flow_extract/python_logic_flow_complete.md`
- Graph EN: `projects/ai-scientist-v2/logic_flow_extract/graph_english.md`
- Graph AR: `projects/ai-scientist-v2/logic_flow_extract/graph_arabic.md`
- Deep dive: `projects/ai-scientist-v2/deep_dive_task_matrix.md`
- Completeness: `projects/ai-scientist-v2/final_completeness_check_ar.md`

### Self-Refine

- Prompts: `projects/self-refine/prompts_complete.md`
- Raw prompt files: `projects/self-refine/raw_prompt_files/`
- Logic: `projects/self-refine/python_logic_flow_complete.md`
- Graph EN: `projects/self-refine/graph_english.md`
- Graph AR: `projects/self-refine/graph_arabic.md`
- Deep dive: `projects/self-refine/deep_dive_task_matrix.md`
- Completeness: `projects/self-refine/final_completeness_check_ar.md`

### Reflexion

- Prompts: `projects/reflexion/prompts_complete.md`
- Raw prompt/config files: `projects/reflexion/raw_prompt_files/`
- Logic: `projects/reflexion/python_logic_flow_complete.md`
- Graph EN: `projects/reflexion/graph_english.md`
- Graph AR: `projects/reflexion/graph_arabic.md`
- Deep dive: `projects/reflexion/deep_dive_task_matrix.md`
- Completeness: `projects/reflexion/final_completeness_check_ar.md`

### Meta-Prompting

- Prompts: `projects/meta-prompting/prompts_complete.md`
- Raw prompt/config files: `projects/meta-prompting/raw_prompt_files/`
- Raw data samples: `projects/meta-prompting/raw_data_samples/`
- Logic: `projects/meta-prompting/python_logic_flow_complete.md`
- Graph EN: `projects/meta-prompting/graph_english.md`
- Graph AR: `projects/meta-prompting/graph_arabic.md`
- Deep dive: `projects/meta-prompting/deep_dive_task_matrix.md`
- Completeness: `projects/meta-prompting/final_completeness_check_ar.md`

### LATS

- Prompts: `projects/lats/prompts_complete.md`
- Raw prompt files: `projects/lats/raw_prompt_files/`
- Raw data samples: `projects/lats/raw_data_samples/`
- Logic: `projects/lats/python_logic_flow_complete.md`
- Graph EN: `projects/lats/graph_english.md`
- Graph AR: `projects/lats/graph_arabic.md`
- Deep dive: `projects/lats/deep_dive_task_matrix.md`
- Completeness: `projects/lats/final_completeness_check_ar.md`
- Final audit: `projects/lats/final_audit_review_ar.md`

### APE

- Prompts: `projects/ape/prompts_complete.md`
- Raw prompt files: `projects/ape/raw_prompt_files/`
- Raw data samples: `projects/ape/raw_data_samples/`
- Logic: `projects/ape/python_logic_flow_complete.md`
- Graph EN: `projects/ape/graph_english.md`
- Graph AR: `projects/ape/graph_arabic.md`
- Deep dive: `projects/ape/deep_dive_task_matrix.md`
- Completeness: `projects/ape/final_completeness_check_ar.md`
- Final audit: `projects/ape/final_audit_review_ar.md`

### Prompt Report

- Prompts: `projects/prompt-report/prompts_complete.md`
- Raw prompt files: `projects/prompt-report/raw_prompt_files/` (includes paper PDF + taxonomy)
- Raw data samples: `projects/prompt-report/raw_data_samples/`
- Logic: `projects/prompt-report/python_logic_flow_complete.md`
- Graph EN: `projects/prompt-report/graph_english.md`
- Graph AR: `projects/prompt-report/graph_arabic.md`
- Deep dive: `projects/prompt-report/deep_dive_task_matrix.md`
- Completeness: `projects/prompt-report/final_completeness_check_ar.md`
- Final audit: `projects/prompt-report/final_audit_review_ar.md`

### Tree of Thoughts (ToT)

- Folder: `projects/tot/`
- Repo: https://github.com/faresrafat3/tot-full-extraction
- Paper: https://arxiv.org/abs/2305.10601
- Prompts: `projects/tot/prompts_complete.md`
- Raw prompts/scripts: `projects/tot/raw_prompt_files/`
- Logic: `projects/tot/python_logic_flow_complete.md`
- Graph EN: `projects/tot/graph_english.md`
- Graph AR: `projects/tot/graph_arabic.md`
- Deep dive: `projects/tot/deep_dive_task_matrix.md`
- Completeness: `projects/tot/final_completeness_check_ar.md`
- Audit: `projects/tot/AUDIT_REVIEW_AR.md`

### Voyager

- Prompts: `projects/voyager/prompts_complete.md`
- Raw prompts/agents: `projects/voyager/raw_prompt_files/`
- Skill samples: `projects/voyager/raw_data_samples/`
- Logic: `projects/voyager/python_logic_flow_complete.md`
- Graph EN: `projects/voyager/graph_english.md`
- Graph AR: `projects/voyager/graph_arabic.md`
- Deep dive: `projects/voyager/deep_dive_task_matrix.md`
- Completeness: `projects/voyager/final_completeness_check_ar.md`

### OPRO

- Prompts/meta-prompts: `projects/opro/prompts_complete.md`
- Raw code: `projects/opro/raw_prompt_files/`
- Logic: `projects/opro/python_logic_flow_complete.md`
- Graph EN: `projects/opro/graph_english.md`
- Graph AR: `projects/opro/graph_arabic.md`
- Deep dive: `projects/opro/deep_dive_task_matrix.md`
- Completeness: `projects/opro/final_completeness_check_ar.md`

### GAPMAP

- Folder: `projects/gapmap/`
- Repo: https://github.com/faresrafat3/gapmap-full-extraction
- Paper: https://arxiv.org/abs/2510.25055
- Prompts: `projects/gapmap/prompts_complete.md`
- Raw prompts: `projects/gapmap/raw_prompt_files/ex_gap_xtract.py + prompt_explicit_full.txt + prompt_implicit_TABI_3shot.txt + prompt_implicit_fullpaper.txt + chunking_logic.py`
- Logic: `projects/gapmap/python_logic_flow_complete.md`
- Inventory: `projects/gapmap/python_logic_inventory.json`
- Graph EN: `projects/gapmap/graph_english.md` + `graph_english.mmd`
- Graph AR: `projects/gapmap/graph_arabic.md` + `graph_arabic.mmd`
- Deep dive: `projects/gapmap/deep_dive_task_matrix.md`
- Samples: `projects/gapmap/raw_data_samples/ipbes_sample.json + covid_sample.json + implicit_paragraph_sample.json`
- Completeness: `projects/gapmap/final_completeness_check_ar.md` + `QUALITY_REVIEW_AR.md`

### ResearchAgent

- Folder: `projects/researchagent/`
- Repo: https://github.com/faresrafat3/researchagent-full-extraction
- Paper: https://arxiv.org/abs/2404.07738 NAACL 2025
- Prompts: `projects/researchagent/prompts_complete.md` (Tables 6-15)
- Raw prompts: `projects/researchagent/raw_prompt_files/prompt_problem_identification.txt + prompt_method_development.txt + prompt_experiment_design.txt + prompt_reviewing_problem.txt + prompt_reviewing_method.txt + prompt_reviewing_experiment.txt + prompt_criteria_induction.txt + prompt_evaluation_scoring.txt + prompt_evaluation_pairwise.txt + entity_retrieval_logic.py`
- Logic: `projects/researchagent/python_logic_flow_complete.md`
- Inventory: `projects/researchagent/python_logic_inventory.json`
- Graph EN/AR: `projects/researchagent/graph_english.md/.mmd + graph_arabic.md/.mmd`
- Deep dive: `projects/researchagent/deep_dive_task_matrix.md`
- Samples: `core_paper_sample.json + entity_store_sample.json + idea_example_drosophila.json`
- Completeness: `final_completeness_check_ar.md` + `QUALITY_REVIEW_AR.md`

### Scientific Intelligence Survey

- Folder: `projects/scientific-intelligence-survey/`
- Repo: https://github.com/faresrafat3/scientific-intelligence-survey-full-extraction
- Paper: https://arxiv.org/abs/2503.24047
- Prompts: `projects/scientific-intelligence-survey/prompts_complete.md` (P1-P6 L1-L2 M1-M5 A1-A5 V1-V4 cathode example)
- Raw prompts: `planner_P1_schema_driven.txt + P2_context_augmented + P3_deliberative_reflective + P4_search_based + P5_role_interactive + P6_programmatic + L1_SFT + L2_RL + memory_types + action_space_types + verifier_V1_self_critique + V2_tool_based + V3_HITL_expert + V4_multi_agent_critique + cathode_design_running_example.md`
- Logic: `python_logic_flow_complete.md`
- Inventory: `python_logic_inventory.json`
- Graph EN/AR: `graph_english.md/.mmd + graph_arabic.md/.mmd`
- Deep dive: `deep_dive_task_matrix.md`
- Samples: `benchmarks_list.json + applications_map.json + taxonomy_planner.json`

### STORM

- Folder: `projects/storm/`
- Repo: https://github.com/faresrafat3/storm-full-extraction
- Paper: https://arxiv.org/abs/2402.14207
- Prompts: `projects/storm/prompts_complete.md` (GenRelatedTopics + GenPerspectives N=5 + GenQn M=5 + GenQueries + GenAnswer + DirectGenOutline + RefineOutline + section generation + polish + lead)
- Raw prompts: `GenRelatedTopicsPrompt.txt + GenPerspectivesPrompt.txt + GenQnPrompt.txt + GenQueriesPrompt.txt + GenAnswerPrompt.txt + DirectGenOutlinePrompt.txt + RefineOutlinePrompt.txt + algorithm1_pseudocode.py + prewriting_vs_writing_stage.md`
- Logic: `python_logic_flow_complete.md`
- Inventory: `python_logic_inventory.json`
- Graph EN/AR: `graph_english.md/.mmd + graph_arabic.md/.mmd`
- Deep dive: `deep_dive_task_matrix.md`
- Samples: `freshwiki_sample.json + outline_eval_metrics.json + conversation_example.json`
- Completeness: `final_completeness_check_ar.md` + `QUALITY_REVIEW_AR.md`

### SciMON / SciPIP

- Folder: `projects/scimon-scipip/`
- Repo: https://github.com/faresrafat3/scimon-scipip-full-extraction
- Papers: https://arxiv.org/abs/2305.14259 + https://arxiv.org/abs/2410.23166
- Prompts: `projects/scimon-scipip/prompts_complete.md` (SciMON problem setting + inspiration retrieval semantic KG citation Table8 Example Zhou et al 2022 underlined + idea generation Given [context] a [new idea] Δ vs prior work + iterative novelty boosting compare I with prior literature + in-context contrastive CL + SciPIP quintuple keywords backgrounds ideas concise methods references ~78K papers + entity extraction τ2 + summary problem main idea format The problem of [problem] can be addressed by [main idea/approach] + background motivations details + concise methods τ3 example style transform + background transformation teacher student + multi-granularity retrieval SE CC CL Table4 Recall10 + dual-path idea proposer ~10 ideas clear innovative valid comprehensive)
- Raw prompts: `scimon_problem_setting.txt + scimon_inspiration_retrieval.txt + scimon_iterative_novelty_boosting.txt + scipip_entity_extraction_tau2.txt + scipip_idea_proposer_dual_path.txt + ...`
- Logic: `python_logic_flow_complete.md`
- Inventory: `python_logic_inventory.json`
- Graph EN/AR: `graph_english.md/.mmd + graph_arabic.md/.mmd`
- Deep dive: `deep_dive_task_matrix.md`
- Samples: `scimon_background_context_example.json + scipip_quintuple_example.json + quintuple retrieval results + idea examples`
- Completeness: `final_completeness_check_ar.md` + `QUALITY_REVIEW_AR.md`
