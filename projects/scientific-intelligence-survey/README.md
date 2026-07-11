# Scientific Intelligence Survey — Full Prompt, Logic, Flow, and Graph Extraction

Paper: **Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents**  
ArXiv: https://arxiv.org/abs/2503.24047 (v3 Feb 02 2026)  
License: CC BY 4.0  
Authors: Shuo Ren, Can Xie (equal), Pu Jian, Zhenjiang Ren, Chunlin Leng, Jiajun Zhang (corresponding)  
Affiliations: SKL Multimodal AI Systems, Foundation Model Research Center CAS, UCAS, Wuhan AI Research  
Survey scope: >120 representative papers, >40 domain benchmarks, mechanism-centric taxonomy

## Why this package

First *mechanism-centric* survey (vs lifecycle/role/domain). Proposes 4 architectural mechanisms:

1. **Planner** (6 prompt-native P1-P6 + 2 learned L1-L2)
2. **Memory** (short/working, episodic, semantic KG, procedural skill library, hybrid)
3. **Action Space** (5 types: internal reasoning, external tool API, code execution, simulation, physical robotic lab)
4. **Verifier** (4 types: self-critique, tool-based, human-in-loop/expert oversight, multi-agent critique + VLM)

Provides **component-wise construction blueprint** recipe book: mix-and-match sub-types to build fit-for-purpose agents. Running **cathode-design example** (high-capacity Li-ion >200 mAh/g stable 500+ cycles) illustrates every component.

Unlike general LLM agent surveys, focuses on why scientific agents differ: domain knowledge, advanced tool sets, robust validation, heterogeneous data.

Also atlas of benchmarks (>40) and applications (Chem/Materials, Life/Bio, Physical sciences) and ethics/reproducibility as design imperatives.

This extraction completes ARSENAL mapping and directly expands CONSTITUTION Part 6.

## Package contents

```text
scientific-intelligence-survey-full-extraction/
├── README.md
├── research_summary.md
├── prompts_complete.md
├── python_logic_flow_complete.md
├── python_logic_inventory.json
├── deep_dive_task_matrix.md
├── graph_english.md/.mmd
├── graph_arabic.md/.mmd
├── final_completeness_check_ar.md
├── QUALITY_REVIEW_AR.md
├── raw_prompt_files/
│   ├── planner_P1_schema_driven.txt
│   ├── planner_P2_context_augmented.txt
│   ├── planner_P3_deliberative_reflective.txt
│   ├── planner_P4_search_based.txt
│   ├── planner_P5_role_interactive.txt
│   ├── planner_P6_programmatic.txt
│   ├── planner_L1_SFT_domain_trained.txt
│   ├── planner_L2_RL_preference.txt
│   ├── memory_types.txt
│   ├── action_space_types.txt
│   ├── verifier_V1_self_critique.txt
│   ├── verifier_V2_tool_based.txt
│   ├── verifier_V3_HITL_expert.txt
│   ├── verifier_V4_multi_agent_critique.txt
│   └── cathode_design_running_example.md
├── raw_data_samples/
│   ├── benchmarks_list.json
│   ├── applications_map.json
│   └── taxonomy_planner.json
└── archives/scientific_intelligence_full_extract.zip
```

## Taxonomy snapshot

### Planner P1-P6 Prompt-Native
- P1 Instructional/Schema-Driven: AutoLabs, Coscientist, CRISPR-GPT, GeneGPT, k-agents, LLMSat, ORGANA, ResearchAgent, StarWhisper — predefined workflow templates ReAct, tool schemas, domain guidelines
- P2 Context-Augmented: CellVoyager, CoI, Coscientist, GeoSim.AI, HoneyComb, IR-Agent, PaSa, ResearchAgent, SciMON, STELLA, VirSci — historical + KB facts: target conductivity σ>1000 mS/cm, voltage 4.0-4.3V, NMC811 failed @400 cycles fade
- P3 Deliberative/Reflective: AtlasAgent, CellForge, dZiner, k-agents, MoRA, LLMatDesign, OriGene, VirSci, OpenFOAMGPT 2.0 — meta-prompts "Evaluate plan logical consistency feasibility", "Identify failure modes revise", MoRA flags scores routing
- P4 Search-Based: AI Scientist-v2, CheMatAgent, ChemReasoner, GeoAgent, InternAgent, Mephisto, SGA — Tree-of-Thought, MCTS, beam search, quantum-chemical feedback adsorption energies, experiment manager 4 stages, HE-MCTS Policy+Execution
- P5 Role-Interactive/Multi-Agent: AI co-scientist, AIGS, AtomAgents, El Agente, Foam-Agent, InternAgent, IR-Agent, LLM-RDF, MechAgents, MedAgents, ProtAgents, Robin, STELLA, TAIS, VirSci, xChemAgents — tournament debate 4 agents 2 for 2 against judge, multi-round votes yes/no until consensus, critics novelty feasibility impact
- P6 Programmatic (Code/DSL/DAG): AIGS, AlphaEvolve, Biomni, Chemist-X, K-Dense Analyst, ORGANA, SGA — LLM CODE GENERATOR "Generate DFT+Synthesis pipeline as Python script" → DSL_Pipeline().add(DFT_Screening...)

### Learned Planners L1-L2
- L1 SFT/Domain-Trained: AstroMLab, BioGPT, Chemma LLaMA-2-7b 34B tokens, DrugAssist, DrugPilot, GatorTronGPT, GeoMinLM, MatChat, NatureLM, ToRA
- L2 RL/Preference-Optimized: BioScientist Agent, CheMatAgent, Chemma, CycleResearcher, ReFT, STEP-DPO, Flow-DPO, Sci-MARL, MolRL-MGPT, PaSa

### Memory (5 types)
- M1 Working/Short-term: context window scratchpad
- M2 Episodic: Reflexion verbal reflections trial history last K
- M3 Semantic/Knowledge: KG, vector DB, HoneyComb KB, STELLA Template Library Tool Ocean
- M4 Procedural/Skill library: Voyager skill description, STELLA Tool Ocean self-evolving
- M5 Hybrid

### Action Space (5 types)
- A1 Internal reasoning: LLM itself
- A2 External Tool API: 18+ chemoinformatics tools ChemCrow, VASP, XRD_Simulator, Autolab_API
- A3 Code execution: Python executor DSL
- A4 Simulation: DFT simulator quantum-chemical feedback
- A5 Physical robotic lab: Coscientist robotic lab Suzuki Sonogashira, AutoLabs liquid handlers

### Verifier (4 types V1-V4)
- V1 Self-critique: chain-of-thought self-reflection, VLM figure quality
- V2 Tool-based: simulation feedback adsorption energies stability, code tests, GeoAgent error traceback
- V3 Human-in-the-Loop: approval gates safety-critical, evaluation feedback, collaborative iteration, debugging intervention. Examples Agent Laboratory Schmidgall, StarWhisper astronomers, ORGANA REASONER, BIA, ChemCrow 4 experts, dZiner, Chemma active learning, MAPPS explicit approval before expensive simulations
- V4 Multi-agent critique: MedAgents voting, VirSci novelty feasibility impact, CellAgent Evaluator Executor, Sparks generation-reflection paired, AccelMat Diversity Feasibility Scientific Rigor critics, STELLA Dev+Critic, AtomAgents Critic, AutoLabs supervisor

## Benchmarks (>40) and Applications

- MLE-bench ML engineering, RAS-Eval security, Core-bench reproducibility, SciTrust 2.0 trustworthiness
- Chemistry/Materials: AutoLabs, ChemCrow, Coscientist, Chemma LLaMA-2-7b, ChemReasoner catalytic search, etc.
- Life/Bio: AI co-scientist, MedAgents voting, CellAgent scRNA-seq, CellVoyager Template Library Tool Ocean, etc.

## Running example cathode

GOAL: "Design high-capacity cathode >200 mAh/g stable 500+ cycles"
P1 Persona battery expert Procedural Schema 1 Crystal Design→2 DFT→3 Synthesis→4 Testing Tool Inventory [VASP, XRD_Simulator, Autolab_API] Constraints Avoid Co target >4V
P2 [Historical] NMC811 failed @400 cycles fade LFP stable 160 mAh/g [KB] conductivity σ>1000 mS/cm voltage 4.0-4.3V
P3 Initial Li-rich oxide Reflect cycles 480 (<500) safety O2 risk Revise Mg-doping Al2O3 coating Reflect 550 ✓
P4 ROOT >200 branches LFP 0.5 NMC 0.7 Co-free 0.65 NMC-Mg 0.82 NMC-Al 0.75 DFT E_cal -3.1 eV cycles 520 max reward
P5 Materials Designer Safety Critic Synthesis Engineer debate D:✓ C:✗ E:? Consensus Revise Mn-rich LiNiO2-Mg
P6 CODE GENERATOR "Generate DFT+Synthesis pipeline as Python script" → workflow=DSL_Pipeline().add(DFT_Screening...)

## Related

- GAPMAP P2 context-augmented + V2 verifier
- ResearchAgent P2 context-augmented + P5 role-interactive + P3 deliberative 3-step saturation
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions
- ARSENAL: https://github.com/faresrafat3/arsenal-unified-master-pipeline
