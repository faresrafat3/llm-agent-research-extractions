# Scientific Intelligence Survey — Research Summary

## Paper identity
- Title: Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents
- ArXiv: 2503.24047v3 Feb 2 2026 (v1 Mar31 2025)
- License CC BY 4.0
- Authors: Shuo Ren*, Can Xie* equal, Pu Jian, Zhenjiang Ren, Chunlin Leng, Jiajun Zhang corresponding
- Affiliations: SKL Multimodal AI Systems, Foundation Model Research Center CAS, UCAS, Wuhan AI Research
- Scope: >120 papers, >40 benchmarks

## Motivation vs other surveys
- General agent surveys: Wang 2024a, Xi 2023, Guo 2024, Hu 2024a, Li 2024e, Xie 2024, Cheng 2024, Shen 2024, Gridach 2025 focus broad dialogue/coding
- Scientific agent surveys:
  - Luo 2025 emphasizes discrete tasks hypothesis generation experimental design peer review
  - Wang 2025c Hitchhiker's Guide lifecycle Assistant/Partner/Avatar
  - Wei 2025 Agentic Science paradigm tools to autonomous partners domain-oriented life/chem/materials/physics
- This survey: mechanism-centric architectural foundations planner, memory, action space, verifier for rigor reproducibility ethical alignment
- Connecting high-level capabilities to underlying design principles, complements lifecycle role-based, advancing design-focused taxonomy trustworthy scientifically valid performance

## Contributions
1. Mechanism-oriented taxonomy: 4 mechanisms not roles/lifecycle
2. Component-wise construction blueprint: multiple sub-types each component mix-and-match fit-for-purpose agents running end-to-end cathode-design example illustrates every component recipe book
3. Literature & benchmark atlas: >120 papers >40 benchmarks fine-grained mechanism-level categories signature characteristics curated map enables domain experts locate transferable techniques baselines
4. Ethics and reproducibility as design imperatives: extends framing ethics bias mitigation reproducibility not peripheral but intrinsic design constraints embedded architecture verification modules
5. Research outlook: open challenges future directions integration interdisciplinary knowledge dynamic adaptation standardized reproducibility protocols

## Architecture Figure1 typical
Workflow:
- User query scientific problem text+associated data Input
- Planner decomposes into sub-tasks retrieves context knowledge from Memory executes actions via Action Space APIs simulators lab instruments search engines LLM itself can function as part Action Space reasoning computation intermediate analysis
- Actions generate intermediate results examined by Verifier accuracy consistency scientific plausibility
- Verified results stored in Memory refine future decisions
- If verification indicates further actions corrections Planner generates new plans re-invokes Action Space iterative until Verifier confirms output meets validity reproducibility final integrated result returned
- Note multimodal perception intrinsic capability Planner conceptual simplicity (previous multimodal agents separate perceptron Xie et al 2024)

## Planner families Section 2.1
Prompt-Native P1-P6 + Learned L1-L2

### P1 Instructional / Schema-Driven
- Templates: structured workflow templates literature→hypothesis→design→validation, standardized response formats ReAct Thought-Action-Observation, tool usage schemas, domain guidelines
- Mechanistically single LLM agent explicit planning instructions system prompts procedural schemas stages permissible actions transition conditions
- Examples: AutoLabs Panapitiya supervisor, Coscientist Boiko Suzuki Sonogashira, CRISPR-GPT Huang, GeneGPT Jin genomic APIs, k-agents Cao, LLMSat Maranto, ORGANA Darvish, ResearchAgent Baek systematic reading, StarWhisper Wang astronomy telescope operation
- Running example: Battery Schema Persona battery expert Procedural Schema 1 Crystal Design→2 DFT→3 Synthesis→4 Testing Tool Inventory [VASP,XRD_Simulator,Autolab_API] Constraints Avoid Co cost target >4V Plan STEP1...

### P2 Context-Augmented
- Encode historical searched context prompts
- Context: historical records NMC811 failed @400 cycles capacity fade LFP stable 160 mAh/g + KB Target conductivity σ>1000 mS/cm rate capability voltage 4.0-4.3V vs Li/Li+
- Improves accuracy reproducibility but challenges selection coherence large noisy windows dilute focus inconsistencies factual drift
- Examples: CellVoyager Alber self-evolving Template Library Tool Ocean persistent context, CoI Li person research interests citation history context collaborative idea generation, Coscientist, GeoSim.AI, HoneyComb Zhang domain KB, IR-Agent Noh, PaSa He search, ResearchAgent Baek academic graph entity store 50,091 papers, SciMON Wang, STELLA Jin Template Library Tool Ocean

### P3 Deliberative / Reflective
- Augment decomposition with self-evaluation iterative refinement critique revision cycles mirrors researchers refining designs self-assessment before execution
- Multi-turn generate→critique alternating meta-prompts "Evaluate plan logical consistency feasibility" "Identify failure modes revise accordingly"
- Critique informs subsequent generation loops until quality thresholds met iteration limits self-supervision without external feedback within LLM own evaluation
- Variants: chain-of-thought self-reflection iterative idea plan refinement (Lu Yamada Gottweis Novikov Xin Alber Ansari Zhang Jia Chen Jaiswal Darvish Zhang 2025e Wang Su); error-driven replanning failures trigger revision cycles (Ye Liu Panapitiya Roohani McNaughton Tang Kang Kim Peng Maranto Li Yang Sun Hu Pandey Feng Ma); explicit reflection stages dedicated critique prompts assessment before proceeding (Tang Kang Kim Sprueill Roohani Ansari); VLM-based reflection multimodal evaluation Yamada
- Examples: LLMatDesign Jia self-reflection previous design decisions adapt rapidly zero-shot; dZiner Ansari iterative reviewing history chain-of-thought stopping convergence criteria no improvements max iterations human feedback; AtlasAgent Yin chain-of-thought few/zero-shot evaluation batch correction quality biological preservation over-correction risks atlas-scale single-cell integration; MoRA Jaiswal Mixture Refinement Agents two-step advanced models identify errors flags scores prioritized agent routing activates appropriate agents progressively; OriGene Zhang self-evolving continuously refine experimental strategies prior outcomes; VirSci Su team discussion inter-intra refinement dialogues novelty assessment compare ideas related papers vote reasoning; CellForge Tang graph-structured debates Design proposes Critics review score revisions until consensus; OpenFOAMGPT 2.0 Feng self-correcting simulation loops error-driven iterative refinement Configuration Generation Automated Execution Management Error-Driven Refinement
- Running example: Initial Li-rich oxide Reflect flaws Cycles 480 (<500) Safety O2 risk Revise Mg-doping Al2O3 coating Reflect 550 ✓ Converged Yes Final Plan
- Enhances robustness reduces failures but reflection quality depends LLM introspective capabilities may fail domain expertise empirical validation beyond linguistic

### P4 Search-Based
- Exploration over plan spaces generating evaluating multiple candidates selecting optimal Tree-of-Thought ToT Yao 2023a MCTS beam search sequential decision-making under uncertainty expanding promising branches pruning low-quality
- Construct search trees nodes partial plans edges extensions adding sub-tasks refining parameters generate multiple alternative extensions each node evaluates heuristic scoring learned value models selectively expands high-scoring branches (Yamada Sprueill Chen Team Sun Ma)
- Examples: ChemReasoner Sprueill hierarchical search tree each node distinct hypothesis query plans catalyst type inclusion/exclusion relational operators quantum-chemical feedback atomistic simulations adsorption energies reaction barriers stability rewards prune unpromising pathways iteratively refine; AI Scientist-v2 Yamada agentic tree-search experiment manager coordinating expansion 4 stages Preliminary Investigation Hyperparameter Tuning Research Agenda Execution Ablation Studies each stage generates multiple candidates executes parallel evaluates results VLM figure quality selects best-performing nodes further expansion; CheMatAgent Wu HE-MCTS decoupling tool planning Policy Model execution Execution Model; InternAgent Team idea innovation generate ideas then evolve iterative hierarchical idea evolution tree; Mephisto Sun deliberate reasoning tree search accumulates knowledge self-play dynamically updates knowledge base; SGA Ma integrates search with simulators generating alternative experimental designs simulating outcomes each branch expands only physically plausible using simulation feedback guidance; GeoAgent Chen LLMs MCTS dynamic adjustments task programming geospatial beam search combined execution filtering child node sampling prompt updating MCTS expansion comprehensive error traceback analysis dynamically refine subtask
- Enables systematic exploration principled selection explicit evaluation but high computational costs requires effective evaluation functions scalability challenges high-dimensional
- Running example: ROOT Cathode >200 branches LFP 0.5 NMC 0.7 Co-free 0.65 NMC-Mg 0.82 NMC-Al 0.75 DFT E_cal -3.1 eV Cycles 520 max reward path

### P5 Role-Interactive / Multi-Agent
- Distribute planning across distinct LLM agent instances specialized functions collaborative dialogue planner proposes critic identifies flaws executor provides feasibility feedback mirrors scientific team dynamics different expertise collectively design experiments iterative discussion consensus-building unlike P1 single agent follows schema under one persona P5 multiple agents different responsibilities co-construct plans
- Sophisticated multi-agent critique architectures: AI co-scientist Gottweis tournament debate 4 debate agents 2 for 2 against judge declares winners meta-review synthesizes insights multiple rounds identifying recurring patterns optimizing performance; MedAgents Tang multi-round discussions several expert agents votes yes/no preliminary summary report modification opinions if vote no report revised iteratively until all experts agree max attempts; VirSci structured idea refinement critic agents evaluate novelty feasibility impact low filtered high refined; CellAgent Xiao multi-agent critique Evaluator assesses quality current results allows Executor optimize hyperparameter tuning tool selection automated high-quality scRNA-seq; Sparks Ghafarollahi Buehler generation-reflection each core paired reflection agent evaluating clarity novelty feasibility technical correctness completeness adherence standards; AccelMat Kumbhar specialized critics Diversity Feasibility Scientific Rigor; STELLA Jin Dev Agent environment building code creation model training report writing Critic assessing intermediate results flaws actionable feedback; AtomAgents Ghafarollahi Buehler Critic role-based verification evaluating plan proposed Planner completeness correctness; AutoLabs Panapitiya supervisor orchestrates sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification
- Provides comprehensive error coverage diverse perspectives sophisticated collaborative reasoning but coordination overhead managing multiple agents synthesizing conflicting feedback increased costs multiple instances potential echo chambers share underlying model biases despite different role prompts motivating integration human oversight external tools authoritative validation
- Running example: Materials Designer Safety Critic Synthesis Engineer Evaluation debate D:✓ C:✗ E:? Consensus Plan Revise Mn-rich LiNiO2-Mg Proposal

### P6 Programmatic Code/DSL/DAG
- Generate machine-executable plan representations LLM CODE GENERATOR prompt "Generate DFT+Synthesis pipeline as Python script" → EXECUTABLE ARTIFACT workflow=DSL_Pipeline() workflow.add(DFT_Screening(candidates=100 criteria capacity >200)) .... OR DAG explicit task dependencies
- Examples: AIGS Liu AlphaEvolve Novikov Biomni Huang Chemist-X Chen K-Dense Analyst Li ORGANA Darvish SGA Ma

### L1 SFT Domain-Trained
- AstroMLab de Haan, BioGPT Luo, Chemma Zhang LLaMA-2-7b fine-tuned 34B tokens chemical literature retrosynthesis yield prediction condition generation autonomous exploration closed/open, DrugAssist Ye, DrugPilot Li, GatorTronGPT Peng, GeoMinLM Fu, MatChat Chen, NatureLM Xia, ToRA Gou etc internalize planning through training domain-specific trajectories

### L2 RL Preference-Optimized
- BioScientist Agent Zhang, CheMatAgent Wu, Chemma Zhang, CycleResearcher Weng, ReFT Luong, STEP-DPO Lai, Flow-DPO Deng, Sci-MARL Bae, MolRL-MGPT Hu, PaSa He etc internalize through reward signals

## Memory 5 types
- M1 Working Short-term: context window scratchpad Thought-Action-Observation
- M2 Episodic: Reflexion verbal reflections trial history lessons last K window
- M3 Semantic Knowledge: vector DB KG HoneyComb domain KB STELLA Template Library Tool Ocean self-evolving expand knowledge skills CoI person interests
- M4 Procedural Skill library: Voyager skill description at most 6 sentences main procedure single block plain text stored skill library retrieve-by-similarity
- M5 Hybrid combination hierarchical

## Action Space 5 types
- A1 Internal Reasoning: LLM itself reasoning computation intermediate analysis chain-of-thought
- A2 Tool API: 18+ chemoinformatics tools ChemCrow VASP XRD_Simulator Autolab_API GeneGPT genomic PaSa search Semantic Scholar etc Action ToolName[args] Observation
- A3 Code Execution: Python executor DSL pipelines ORGANA sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps executable includes imports handle errors
- A4 Simulation: DFT simulator quantum-chemical feedback battery simulations adsorption energies reaction barriers structural stability GeoSim.AI OpenFOAMGPT Configuration Generation Automated Execution Management Error-Driven Refinement simulate outcomes each branch expand only physically plausible using feedback guidance SGA
- A5 Physical Lab: Coscientist robotic lab Suzuki Sonogashira AutoLabs high-throughput liquid handlers self-correction translating natural language instructions executable protocols ORGANA natural language chemist clarification updates experiments safety require human approval hazardous operations

## Verifier 4 types
- V1 Self-critique: chain-of-thought self-reflection explicit critique stages VLM figure quality
- V2 Tool-based: simulation feedback atomistic adsorption energies barriers stability rewards prune code tests heuristic scoring comprehensive error traceback GeoAgent dynamic refine subtask If fails trigger error-driven replanning Verified Yes/No + evidence
- V3 HITL Expert Oversight: integration patterns spectrum continuous oversight selective intervention exception-based modalities: approval gates experimental protocols safety-critical pause presentation synthesis procedures robotic control sequences hazardous awaiting explicit human approval; evaluation feedback research outputs human domain experts assess scientific quality novelty validity qualitative critiques refinement; collaborative human-AI iteration multi-turn dialogues guidance constraints corrections shaping exploration; intervention debugging error resolution automated self-correction fails manual edit code adjust parameters redirect; examples Agent Laboratory Schmidgall ML research feedback guidance each stage, StarWhisper astronomers telescope operation natural language requests specific control sequences presentation verification approval, ORGANA REASONER prompts user investigate decide further actions if outcomes mismatch, BIA human intervention critical junctures subset segmentation indispensable, ChemCrow panel 4 expert chemists Correctness reasoning Degree completion fix invalid actions before robotic execution, dZiner closed-loop human-in-loop chemist review proposed candidates reasoning feedback suggesting modifications, Chemma active learning chemists feedback wet experiment results fine-tuning, MAPPS scientists evaluation ranking refinement explicit approval before expensive simulations syntheses, MatPilot human-machine collaboration
- V4 Multi-Agent Critique: MedAgents role-playing multi-round yes/no votes modification iteratively until consensus max attempts; VirSci structured idea refinement critic novelty feasibility impact low filtered high refined; CellAgent Evaluator Executor hyperparameter tuning tool selection automated high-quality scRNA-seq; Sparks generation-reflection paired clarity novelty feasibility technical correctness completeness adherence; AccelMat specialized critics Diversity Feasibility Scientific Rigor; STELLA Dev Agent environment building code creation model training report writing Critic assesses intermediate flaws actionable feedback; AtomAgents Critic role-based verification completeness correctness; AutoLabs supervisor sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification; AI co-scientist tournament debate 4 debate 2 for 2 against judge meta-review synthesizes insights multiple rounds recurring patterns optimize

## Benchmarks >40
- Foundational reasoning SciBench, hypothesis SciMON, experimental automation MLE-bench training models datasets running experiments, remote sensing geospatial tool-augmented Singh et al, security robustness RAS-Eval, computational reproducibility Core-bench validating published results credibility, trustworthiness SciTrust 2.0 truthfulness adversarial robustness scientific safety ethics exploration capabilities
- Limitations: static datasets pre-defined tasks may not fully capture dynamic iterative nature real-world lab, end-to-end performance obscuring nuanced failures individual steps, diversity domains challenges standardizing metrics fairly compare across fields. Future adaptive continuously updated benchmarks mimic authentic workflows dynamic multi-turn interactions agents iteratively refine hypotheses experimental feedback lab processes domain-specific metrics cross-disciplinary tasks

## Applications Figures 12-14
- Chemistry Materials: Chemical Synthesis Reaction Optimization AutoLabs ChemCrow 18+ Coscientist Suzuki Sonogashira Chemma LLaMA-2-7b 34B retrosynthesis OSDA zeolite ChemReasoner catalytic GNN feedback LLM-RDF GPT-4 multi-agent ChemAgents Literature Reader Experiment Designer Computation Performer Robot Operator xChemAgents Selector Validator quantum; Molecular Design dZiner inverse design ChemDFM 34B tokens free-form dialogue MolRL-MGPT; Materials Discovery AccelMat AILA AtomAgents ChatMOF MOF HoneyComb LLMatDesign self-reflection MatChat MatPilot MatterChat MAPPS scientists evaluation ranking explicit approval PriM
- Life Biomedical: Drug Discovery AI co-scientist BioScientist Agent DrugAgent DrugPilot DrugAssist GatorTronGPT MedAgents role-playing yes/no OriGene self-evolving Robin STELLA; Genomics Bioinformatics AtlasAgent chain-of-thought batch correction quality BIA human intervention critical BioAgents BioDiscoveryAgent BioMaster BiomedRAG Biomni CellAgent Evaluator Executor scRNA-seq CellVoyager Template Library Tool Ocean GeneGPT K-Dense Analyst TAIS TransAgent; Protein Engineering CRISPR ADAM CellForge graph-structured debates CRISPR-GPT ProtAgents Sparks generation-reflection
- Physics Geospatial ML engineering Astronomy StarWhisper etc.

## Ethics
- Safety chemical/biological experiments dual-use bias mitigation reproducibility as design constraints embedded verification modules intrinsic not peripheral concerns

## Outlook
- Integration interdisciplinary knowledge dynamic adaptation standardized reproducibility protocols adaptive benchmarks domain-specific metrics cross-disciplinary tasks

## Relation to ARSENAL and CONSTITUTION
- Provides blueprint for planner taxonomy feeding C2.1 Technique Router P1-P6 concrete implementations for C5.1 Meta-Conductor expert dispatch
- Memory M2 episodic = C3.3 verbal reflection + C3.4 actor with memory window M4 procedural = C3.6 skill description
- Action Space A2-A5 = tool integration for C5.4 curriculum C5.6 execution spine
- Verifier V1-V4 = C2.5 evidence validation answer check + C3.1 multi-aspect critique + C3.3 + C4.5 peer review + V3 HITL high-stakes
- Full map enables building any scientific agent mixing matching components
