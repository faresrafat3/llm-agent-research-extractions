# Scientific Intelligence Survey — Python Logic Flow Complete

Survey no official codebase but logic flow of taxonomy and component blueprint extracted Sections 2-5 Figures 1-3 12-14

---

## 0. Overview architecture Figure1 workflow

```
User submits query scientific problem text+associated data Input system
 |
Planner decomposes task into sub-tasks retrieves relevant context or knowledge from Memory executes actions through Action Space APIs simulators lab instruments search engines LLM itself can also function as part Action Space reasoning computation intermediate analysis
 |
Actions generate intermediate results examined by Verifier ensure accuracy consistency scientific plausibility
 |
Verified results stored in Memory refine future decisions
 |
If verification indicates further actions corrections Planner generates new plans re-invokes Action Space iterative continues until Verifier confirms output meets standards validity reproducibility
 |
Final integrated result returned

Note multimodal perception intrinsic capability Planner conceptual simplicity (previous multimodal agents separate perceptron Xie et al 2024)
Four core components: Planner Memory Action Space Verifier Figure1
```

---

## 1. Planner logic

### P1-P6 Prompt-Native

Prompt-native construct task decomposition workflow orchestration entirely through carefully designed prompts leveraging LLM in-context learning capabilities generate structure plans without parameter modification providing direct interpretability researchers inspect modify planning logic through prompt editing rapid adaptability new domains

Six major subtypes distinct approaches plan construction Figure3 instructional/schema-driven encode procedural templates directly prompts; context-augmented encode historical searched context prompts; deliberative/reflective incorporate self-critique cycles refine plans; search-based explore multiple alternative plan candidates; role-interactive distribute planning across collaborative agent ensembles; programmatic generate machine-executable plan representations Note some works use more than one type only exemplify typical type

#### P1 Instructional Schema-Driven flow

```
System prompt Persona battery materials expert + Procedural Schema 1 Crystal Design→2 DFT→3 Synthesis→4 Testing + Tool Inventory [VASP XRD_Simulator Autolab_API] + Constraints Avoid Co cost target >4V
Input research goal Design high-capacity cathode >200 mAh/g stable 500+ cycles
Planner instantiates plans following predefined instructional patterns single LLM agent explicit planning instructions system prompts including procedural schemas outlining workflow stages permissible actions each stage transition conditions between stages + standardized response formats ReAct Thought-Action-Observation + tool usage schemas + domain guidelines best practices constraints
Output Plan STEP1 xxx -> STEP2 -> ...
Example AutoLabs Coscientist CRISPR-GPT GeneGPT k-agents LLMSat ORGANA ResearchAgent StarWhisper
```

#### P2 Context-Augmented flow

```
System prompt + Augmented prompt Historical NMC811 failed @400 cycles fade LFP stable 160 mAh/g KB Target conductivity sigma>1000 rate capability KB Voltage window 4.0-4.3V vs Li/Li+
KBs Records HoneyComb domain KB CellVoyager Template Library Tool Ocean persistent context STELLA
Contextual prompting improves accuracy reproducibility but challenges selection coherence large noisy windows dilute focus inconsistencies factual drift
Flow encode historical searched context prompts → generate plan avoiding past failures while meeting KB thresholds
Representative CellVoyager CoI Coscientist GeoSim.AI HoneyComb IR-Agent PaSa ResearchAgent SciMON STELLA VirSci
```

#### P3 Deliberative Reflective flow

```
Generate Initial Plan Li-rich oxide
→ Reflect Evaluate flaws meta-prompts Evaluate plan logical consistency feasibility Identify failure modes revise accordingly
→ Critique outputs inform subsequent generation rounds refinement loops continue until quality thresholds met iteration limits
→ Self-supervision mechanism enables improvement without external feedback within LLM own evaluation capabilities

Variants:
- CoT self-reflection iterative idea plan refinement Lu Yamada Gottweis Novikov Xin Alber Ansari Zhang Jia Chen Jaiswal Darvish Zhang 2025e Wang Su
- Error-driven replanning execution failures trigger revision cycles Ye Liu Panapitiya Roohani McNaughton Tang Kang Kim Peng Maranto Li Yang Sun Hu Pandey Feng Ma
- Explicit reflection stages dedicated critique prompts assessment before proceeding Tang Kang Kim Sprueill Roohani Ansari
- VLM-based reflection multimodal evaluation Yamada

Examples LLMatDesign self-reflection previous materials design decisions adapt rapidly zero-shot dZiner iterative reviewing history CoT stopping convergence criteria no further improvements max iterations human feedback AtlasAgent CoT few/zero-shot evaluation batch correction quality MoRA Mixture Refinement Agents two-step advanced models identify errors flags scores prioritized routing OriGene self-evolving VirSci team discussion novelty assessment compare ideas related papers vote reasoning CellForge graph-structured debates Design proposes Critics review score revisions until consensus OpenFOAMGPT self-correcting simulation loops error-driven iterative refinement Configuration Generation Automated Execution Management Error-Driven Refinement

Enhances robustness reduces failures but reflection quality depends LLM introspective capabilities may fail domain expertise empirical validation beyond linguistic

Running example Figure3: Generate Initial Li-rich oxide → Reflect cycles 480 fail safety O2 risk → Revise Mg-doping Al2O3 coating → Reflect cycles 550 ok Converged Yes Final
```

#### P4 Search-Based flow

```
Reformulate plan generation exploration over plan spaces systematically generating evaluating multiple candidate plans before selecting optimal
Mechanistically search trees nodes partial plans edges plan extensions adding sub-tasks refining parameters Generate multiple alternative extensions each node evaluates heuristic scoring learned value models selectively expands high-scoring branches (Yamada Sprueill Chen Team Sun Ma)
Example implementations:
- ChemReasoner hierarchical search tree each node distinct hypothesis query plans catalyst type inclusion/exclusion relational operators quantum-chemical feedback atomistic simulations adsorption energies reaction barriers stability rewards prune unpromising iteratively refine
- AI Scientist-v2 agentic tree-search experiment manager coordinating expansion 4 stages Preliminary Investigation Hyperparameter Tuning Research Agenda Execution Ablation Studies each stage generates multiple candidates executes parallel evaluates VLM figure quality selects best nodes further expansion
- CheMatAgent HE-MCTS decoupling tool planning Policy Model execution Execution Model
- InternAgent idea innovation generate ideas then evolve iterative hierarchical idea evolution tree
- Mephisto deliberate reasoning tree search accumulates knowledge self-play dynamically updates knowledge base
- SGA integrates search with simulators generating alternative designs simulating outcomes each branch expands only physically plausible using simulation feedback guidance
- GeoAgent integrates LLMs MCTS facilitating dynamic adjustments task programming geospatial beam search combined execution filtering child node sampling prompt updating MCTS expansion comprehensive error traceback analysis dynamically refine subtask
Enables systematic exploration principled selection explicit evaluation however high computational costs requires effective evaluation functions scalability challenges
Running example ROOT Cathode >200 branches scores 0.5 0.7 0.65 0.82 0.75 DFT E_cal -3.1 eV cycles 520 max reward path
```

#### P5 Role-Interactive Multi-Agent flow

```
Distribute plan generation across distinct LLM agent instances specialized functions collaborative dialogue planner proposes critic identifies flaws executor provides feasibility feedback mirrors scientific team dynamics different expertise collectively design experiments iterative discussion consensus-building unlike P1 single agent follows schema under one persona P5 multiple agents different responsibilities co-construct plans

Sophisticated multi-agent critique architectures:
- AI co-scientist Gottweis tournament debate 4 debate agents 2 for 2 against judge declares winners meta-review synthesizes insights multiple rounds identifying recurring patterns optimizing performance
- MedAgents Tang multi-round discussions several expert agents votes yes/no preliminary summary report modification opinions if vote no report revised iteratively until all agree max attempts
- VirSci structured idea refinement critic agents evaluate novelty feasibility impact low filtered high refined
- CellAgent multi-agent critique Evaluator assesses quality current results allows Executor optimize hyperparameter tuning tool selection automated high-quality scRNA-seq
- Sparks generation-reflection each core paired reflection agent evaluating clarity novelty feasibility technical correctness completeness adherence standards
- AccelMat specialized critics Diversity Feasibility Scientific Rigor
- STELLA Dev Agent environment building code creation model training report writing Critic assessing intermediate results flaws actionable feedback
- AtomAgents Critic role-based verification evaluating plan proposed Planner completeness correctness
- AutoLabs supervisor orchestrates sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification

Provides comprehensive error coverage diverse perspectives sophisticated collaborative reasoning but coordination overhead managing multiple agents synthesizing conflicting feedback increased costs multiple instances potential echo chambers share biases despite different role prompts motivating integration human oversight external tools authoritative validation

Running example Materials Designer Safety Critic Synthesis Engineer Evaluation debate D:✓ C:✗ E:? Consensus Plan Revise Mn-rich LiNiO2-Mg Proposal
```

#### P6 Programmatic flow

```
Generate machine-executable plan representations LLM CODE GENERATOR Prompt Generate DFT+Synthesis pipeline as Python script → EXECUTABLE ARTIFACT workflow=DSL_Pipeline() workflow.add(DFT_Screening(candidates=100 criteria capacity>200)) OR DAG explicit task dependencies
Examples AIGS Liu AlphaEvolve Novikov Biomni Huang Chemist-X Chen K-Dense Analyst Li ORGANA Darvish SGA Ma
```

### Learned Planners L1-L2

L1 SFT Domain-Trained AstroMLab BioGPT Chemma LLaMA-2-7b fine-tuned 34B tokens chemical literature retrosynthesis yield prediction condition generation autonomous exploration closed/open DrugAssist DrugPilot GatorTronGPT GeoMinLM MatChat NatureLM ToRA internalize planning through training domain-specific trajectories

L2 RL Preference-Optimized BioScientist Agent CheMatAgent Chemma CycleResearcher ReFT STEP-DPO Flow-DPO Sci-MARL MolRL-MGPT PaSa internalize through reward signals

---

## 2. Memory logic 5 types

```
M1 Working Short-term context window scratchpad Thought-Action-Observation current goal thoughts recent observations next action

M2 Episodic Reflexion verbal reflections trial history lessons last K window rules do not repeat failed strategies prefer smallest test falsifying approach early reflection format Task trajectory feedback 2-5 sentences actionable what wrong signal ignored policy change

M3 Semantic Knowledge vector DB KG HoneyComb domain KB STELLA Template Library Tool Ocean self-evolving expand knowledge skills CoI person interests

M4 Procedural Skill library Voyager skill description Rules 1) Do not mention function name 2) Do not mention logging helpers 3) If helpers exist describe only main procedure 4) At most 6 sentences 5) Single block plain text Procedure code_or_steps Main procedure is name Description stored skill library retrieve-by-similarity

M5 Hybrid combination hierarchical working+episodic+semantic+procedural
```

---

## 3. Action Space logic 5 types

```
A1 Internal Reasoning LLM itself reasoning computation intermediate analysis chain-of-thought

A2 Tool API 18+ chemoinformatics ChemCrow VASP XRD_Simulator Autolab_API GeneGPT genomic PaSa search Semantic Scholar Academic Graph API etc Action ToolName[args] Observation

A3 Code Execution Python executor DSL pipelines ORGANA sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps executable includes imports handle errors

A4 Simulation DFT simulator quantum-chemical feedback battery simulations adsorption energies reaction barriers stability GeoSim.AI OpenFOAMGPT Configuration Generation Automated Execution Management Error-Driven Refinement simulate outcomes each branch expand only physically plausible using feedback guidance SGA

A5 Physical Lab Coscientist robotic lab Suzuki Sonogashira AutoLabs high-throughput liquid handlers self-correction translating natural language instructions executable protocols ORGANA natural language chemist clarification updates experiments safety require human approval hazardous operations
```

---

## 4. Verifier logic 4 types Figure1 loop

```
Actions generate intermediate results examined Verifier ensure accuracy consistency scientific plausibility Verified results stored Memory refine future decisions If verification indicates further actions corrections Planner generates new plans re-invokes Action Space iterative continues until Verifier confirms output meets validity reproducibility

V1 Self-critique LLM as judge chain-of-thought self-reflection explicit critique stages VLM assessment figure quality

V2 Tool-based Rule-based simulation feedback atomistic adsorption energies barriers stability rewards prune code tests heuristic scoring comprehensive error traceback GeoAgent dynamic refine subtask If fails trigger error-driven replanning Return Verified Yes/No + evidence

V3 Human-in-Loop Expert Oversight integration patterns spectrum continuous oversight selective intervention exception-based modalities:
- Approval gates experimental protocols safety-critical pause presentation synthesis procedures robotic control sequences hazardous awaiting explicit human approval
- Evaluation feedback research outputs human domain experts assess scientific quality novelty validity qualitative critiques refinement
- Collaborative human-AI iteration multi-turn dialogues guidance constraints corrections shaping exploration Zhang Chemma active learning wet experiment results Pham Gottweis Novikov etc
- Intervention debugging error resolution automated self-correction fails manual edit code adjust parameters redirect

Examples Agent Laboratory Schmidgall ML research feedback guidance each stage StarWhisper astronomers telescope operation natural language requests specific control sequences presentation verification approval ORGANA REASONER prompts user investigate decide further actions if outcomes mismatch BIA human intervention critical junctures subset segmentation indispensable ChemCrow panel 4 expert chemists Correctness reasoning Degree completion fix invalid actions before robotic execution dZiner closed-loop human-in-loop chemist review proposed candidates reasoning feedback suggesting modifications Chemma active learning chemists feedback wet experiment results fine-tuning MAPPS scientists evaluation ranking refinement explicit approval before expensive simulations syntheses MatPilot human-machine collaboration

Mechanistically HITL integrates human interaction points into otherwise-automated workflows varied along spectrum continuous selective exception Common modalities approval gates evaluation feedback collaborative iteration intervention debugging

General HITL prompt: At critical decision point agent output Human expert authoritative evaluator reviewing outputs binding approval/rejection decisions qualitative feedback informing subsequent reasoning intervening when automated verification fails ambiguities high-stakes decisions demand human judgment Recognize fundamental limitations purely automated verification LLMs lack genuine understanding physical reality cannot reliably detect all error classes requiring deep domain expertise tacit knowledge awareness subtle contextual factors HITL particularly critical high-stakes workflows where errors could waste expensive experimental resources compromise safety lead false scientific claims Human action approve/reject/feedback/intervention If approved continue if rejected provide guidance if intervention edit code parameters Awaiting human

V4 Multi-Agent Critique role-interactive verification distributing verification across collaborative ensembles mechanisms MedAgents role-playing multi-round yes/no votes modification iteratively until consensus max attempts VirSci structured idea refinement critic novelty feasibility impact low filtered high refined CellAgent multi-agent critique Evaluator assesses quality current results allows Executor optimize hyperparameter tuning tool selection automated high-quality scRNA-seq Sparks generation-reflection paired clarity novelty feasibility technical correctness completeness adherence AccelMat specialized critics Diversity Feasibility Scientific Rigor STELLA Dev Agent environment building code creation model training report writing Critic assesses intermediate flaws actionable feedback AtomAgents Critic role-based verification completeness correctness AutoLabs supervisor sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification AI co-scientist tournament debate 4 debate 2 for 2 against judge meta-review synthesizes insights multiple rounds recurring patterns optimize

Provides comprehensive error coverage diverse perspectives sophisticated collaborative reasoning patterns however coordination overhead synthesizing conflicting feedback increased costs multiple instances potential echo chambers share biases despite different role prompts motivating integration human oversight external tools authoritative validation

Loop continues until Verifier confirms meets standards validity reproducibility then final integrated result returned user
```

---

## 5. Benchmarks & Applications logic

Benchmarks >40 categories foundational reasoning SciBench hypothesis SciMON experimental automation MLE-bench training models datasets running experiments tool-augmented agents remote sensing geospatial Singh et al security robustness RAS-Eval computational reproducibility Core-bench validating published results credibility trustworthiness SciTrust 2.0 truthfulness adversarial robustness scientific safety ethics exploration

Limitations static datasets pre-defined tasks may not fully capture dynamic iterative nature real-world research end-to-end performance obscuring nuanced failures individual steps diversity domains challenges standardizing metrics fairly compare across fields Future adaptive continuously updated benchmarks mimic authentic workflows dynamic multi-turn interactions agents iteratively refine hypotheses experimental feedback lab processes domain-specific metrics cross-disciplinary

Applications categories Chemistry Materials Life Biomedical Physical etc detailed Sec4 Figures 12-14 each system orchestrates end-to-end workflows literature review synthesis planning experimental execution results analysis accelerating discovery cycles maintaining safety reproducibility

Workflow example Coscientist pioneering autonomous chemical experimentation integrating LLM planning robotic lab equipment designing executing synthesis procedures Suzuki Sonogashira minimal human ChemCrow deploying 18+ specialized chemoinformatics tools synthesis planning drug design materials tasks versatile tool integration chemical reasoning etc

---

## 6. Ethics Reproducibility design imperatives logic

Safety chemical/biological experiments dual-use bias mitigation reproducibility as design constraints embedded within agent architecture verification modules intrinsic not peripheral concerns

Ethics checklist + reproducibility protocol: planner include safety constraints, memory include reproducibility logs storing intermediate verified results, action space respect safety protocols require human approval hazardous operations V3, verifier embed bias mitigation truthfulness adversarial robustness scientific safety ethics checks SciTrust 2.0 dimensions ensure reproducibility standards validity

Outlook integration interdisciplinary knowledge dynamic adaptation standardized reproducibility protocols adaptive benchmarks domain-specific metrics cross-disciplinary
