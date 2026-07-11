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
