# Scientific Intelligence Survey — Complete Prompt Extraction

Source: arXiv:2503.24047v3 PDF Figures 2-3 Sec 2.1 taxonomy Sec 2.4 verifier cathode running example

---

## 1. Planner Taxonomy Prompts

### P1 Instructional / Schema-Driven — Battery Example

**System Prompt Template Battery Schema:**

```text
You are a battery materials expert.

Procedural Schema:
1. Crystal Structure Design → 2. DFT Screening → 3. Synthesis Planning → 4. Electrochemical Testing

Tool Inventory: [VASP, XRD_Simulator, Autolab_API]
Constraints: Avoid Co (cost), target voltage >4V
Research Goal: "Design and synthesize a high-capacity cathode material for Li-ion batteries (>200 mAh/g, stable for 500+ cycles)"

You must follow the schema exactly. Output Plan as STEP1 xxx -> STEP2 xxx -> ...

Rules:
- Use predefined workflow templates encoding domain methodologies
- Use standardized response formats specifying expected output structures (e.g., ReAct's Thought-Action-Observation format Yao et al 2023b)
- Follow tool usage schemas defining available operations and their invocation patterns
- Adhere to domain-specific guidelines prescribing best practices and constraints

Do not invent steps outside schema. Do not skip verification.

Begin planning.
```

**Generalized P1 Prompt:**

```text
You are following an instructional/schema-driven plan.

Schema: {{schema_steps}}
Tool inventory: {{tools}}
Constraints: {{constraints}}
Domain guidelines: {{guidelines}}

Task: {{task}}

Instantiate a plan by following predefined instructional patterns. Provide executable steps with tool calls.

Format:
Thought: Why this step follows schema
Action: ToolName[args]
Observation: Expected output
(repeat)

Final Plan: STEP1 ... -> STEP2 ... -> ...
```

Representative: AutoLabs, Coscientist Boiko Suzuki Sonogashira, CRISPR-GPT, GeneGPT, k-agents, LLMSat, ORGANA, ResearchAgent, StarWhisper

---

### P2 Context-Augmented — Cathode Example

**Augmented Prompt:**

```text
AUGMENTED PROMPT
[Historical] NMC811 failed @400 cycles (capacity fade)
[Historical] LFP stable but capacity only 160 mAh/g
[KB] Target conductivity: σ >1000 mS/cm for rate capability
[KB] Voltage window: 4.0-4.3V vs Li/Li+
[KBs] Records from HoneyComb domain KB / CellVoyager Template Library Tool Ocean persistent context
Design new material avoiding NMC811's Mn dissolution issue while exceeding LFP capacity...

Research Goal: {{research_goal}}
Context records: {{historical_records}}
KB facts: {{kb_facts}}

Plan: STEP1 xxx -> STEP2 xxx -> ...
```

**Generalized P2:**

```text
You are a context-augmented planner.

Research Goal: {{goal}}
Historical context (past experiments, failures, successes):
{{historical_data}}
Knowledge base facts (domain KB, literature, Template Library, Tool Ocean):
{{kb_data}}
Target constraints: {{constraints}}

Understanding context essential:
- Historical records show what failed/succeeded and why
- KB facts include quantitative thresholds
- Records include name, role, affiliation, research interests, citation situation, collaboration history serving as context for collaborative idea generation (CoI example)

Approach:
- Read historical failures avoid repeating
- Review KB facts define design space pruned by constraints
- Synthesize improved plan explicitly addresses past failure modes while meeting KB thresholds

Provide context as follows:
Historical: {{historical}}
KB: {{kb}}

With context, formulate plan builds upon history but avoids pitfalls meets KB criteria.
Before crafting, revisit research goal focal point.

Then generate plan with rationale:
Plan:
Rationale:
```

Examples: CellVoyager, CoI, Coscientist, GeoSim.AI, HoneyComb, IR-Agent, PaSa, ResearchAgent academic graph entity store 50,091 papers, SciMON, STELLA, VirSci

---

### P3 Deliberative / Reflective

**System:**

```text
You are a deliberative planner with self-evaluation mechanisms enabling iterative plan refinement through explicit critique and revision cycles.
```

**Generate Initial Plan:**

```text
Generate Initial Plan for:
Research Goal: {{goal}}
Schema/Constraints: {{schema}}
Provide full initial task decomposition.
```

**Reflect — Evaluate flaws meta-prompts:**

```text
Evaluate this experimental plan for logical consistency and feasibility
OR
Identify potential failure modes and revise accordingly.

Current Plan:
{{current_plan}}

Reflect: Evaluate flaws
- Check cycles / capacity / safety / stability / cost / reproducibility
- Identify quantitative shortfalls vs targets (e.g., Cycles: 480 (<500) failure, Safety: O2 release risk)

Provide critique with specific flaws and scores.
```

**Revise:**

```text
Revise plan based on critique:
Previous Plan: {{plan}}
Critique: {{critique}}
Revise with improvements:
- Example: Mg-doping + Al2O3 coating to address Mn dissolution and O2 release
- Overcome cycle deficiency
Provide revised plan. Then re-evaluate: Cycles={{cycles}} ?
Converged? Yes/No
Final Plan with reflection if Yes else loop.
```

Implementation variants:
- Chain-of-thought self-reflection iterative refinement (Lu Yamada Gottweis Novikov Xin Alber Ansari Zhang Jia Chen Jaiswal Darvish Zhang 2025e Wang Su)
- Error-driven replanning failures trigger revision (Ye Liu Panapitiya Roohani McNaughton Tang Kang Kim Peng Maranto Li Yang Sun Hu Pandey Feng Ma)
- Explicit reflection stages dedicated critique prompts (Tang Kang Kim Sprueill Roohani Ansari)
- VLM-based reflection multimodal (Yamada)

Examples: LLMatDesign Jia self-reflection previous design decisions adapt rapidly zero-shot; dZiner Ansari iterative reviewing history CoT stopping convergence no further improvements max iterations human feedback; AtlasAgent Yin CoT few/zero-shot evaluation batch correction quality; MoRA Jaiswal Mixture Refinement Agents two-step advanced models identify errors flags scores prioritized routing; OriGene Zhang self-evolving continuously refine strategies; VirSci Su team discussion inter-intra-refinement novelty assessment compare ideas related papers vote reasoning; CellForge Tang graph-structured debates Design proposes Critics review score revisions until consensus; OpenFOAMGPT 2.0 Feng self-correcting loops error-driven iterative refinement Configuration Generation Automated Execution Management Error-Driven Refinement

Running example: Generate Initial Li-rich oxide Reflect - Cycles 480 (<500) Safety O2 risk Revise Mg-doping + Al2O3 coating Reflect Cycles 550 Converged Yes Final Plan

---

### P4 Search-Based

**System:**

```text
You are a search-based planner reformulating plan generation as exploration over plan spaces, systematically generating and evaluating multiple candidate plans before selecting optimal solutions. Adopt Tree-of-Thought (ToT), MCTS, beam search treating planning as sequential decision-making under uncertainty.
```

**User:**

```text
Search-Based Planning Task:
Research Goal: {{goal}} [ROOT: Cathode >200 mAh/g]
Construct search tree nodes partial plans edges extensions adding sub-tasks refining parameters.
At each node generate multiple alternative extensions:
- LFP Variant, NMC Variant, Co-free Layered, NMC-Mg, NMC-Al etc.
Evaluate them using heuristic scoring functions or learned value models or quantum-chemical feedback or VLM figure quality:
- Score: 0.5, 0.7, 0.65, 0.82, 0.75 etc.
- DFT_SIMULATOR E_cal, Cycles, adsorption energies, reaction energy barriers, structural stability, rewards pruning
Selectively expand high-scoring branches while pruning low-quality alternatives.
Mechanism: Hierarchical search tree query plans include catalyst type inclusion/exclusion criteria relational operators. Use quantum-chemical feedback atomistic simulations evaluating adsorption energies assign rewards prune unpromising pathways iteratively refine hypothesis space (ChemReasoner). Experiment manager coordinating expansion across 4 stages Preliminary Investigation Hyperparameter Tuning Research Agenda Execution Ablation Studies each stage generates multiple candidates executes parallel evaluates results including VLM-assessed figure quality selects best nodes further expansion (AI Scientist-v2). Hierarchical Evolutionary MCTS decoupled tool planning Policy Model execution Execution Model (CheMatAgent HE-MCTS). Idea innovation agent generate ideas then evolve iterative hierarchical idea evolution tree (InternAgent). Deliberate reasoning via tree search accumulates knowledge self-play dynamically updates knowledge base (Mephisto). Search with simulators generates alternative designs simulates outcomes each branch expands only physically plausible using simulation feedback guidance (SGA, GeoAgent beam search execution filtering child node sampling prompt updating MCTS expansion comprehensive error traceback analysis dynamically refine each subtask)
Plan evaluation loop:
1. Expand root with candidates
2. Simulate/Heuristic score each
3. Prune low-scoring < threshold
4. Select max reward path
5. Recurse until convergence or budget
Final: Final Plan with max reward path, e.g., DFT_SIMULATOR E_cal=-3.1 eV Cycles 520
Return search tree + final plan + scores.
```

Examples: AI Scientist-v2 Yamada, CheMatAgent Wu HE-MCTS, ChemReasoner Sprueill, GeoAgent Chen MCTS geospatial, InternAgent Team hierarchical idea evolution, Mephisto Sun self-play, SGA Ma search with simulators.

Running example: ROOT >200 branches scores Final Plan max reward.

---

### P5 Role-Interactive / Multi-Agent

**System Role assignment:**

```text
You are part of role-interactive planner distributing plan generation across multiple distinct LLM agent instances specialized functions collaborative dialogue planner proposes critic identifies flaws executor provides feasibility feedback. Mirrors scientific team dynamics different expertise collectively design experiments iterative discussion consensus-building.

Roles:
- Materials Designer proposes crystal structures doping strategies
- Safety Critic evaluates O2 release thermal runaway toxicity
- Synthesis Engineer assesses feasibility steps equipment cost
- Device Tester evaluates electrochemical performance predictions
- Diversity Critic Feasibility Critic Scientific Rigor Critic (AccelMat)
- Dev Agent environment building code creation model training report writing (STELLA)
- Critic Agent assesses intermediate results flaws actionable feedback (STELLA)
- Judge Agent evaluates debate arguments declares winners
- Meta-review Agent synthesizes insights multiple rounds identifies recurring patterns optimizes performance

Interaction protocol: message-passing until convergence, tournament-style debate, multi-round voting yes/no.
```

**Proposal phase:**

```text
Role: Materials Designer
Task: Propose Li-rich oxide variant >200 mAh/g >500 cycles avoiding Co cost.
Generate proposal: Proposal: LiNiO2-Mg doped layered oxide with Al2O3 coating...
```

**Critique phase:**

```text
Role: Safety Critic
Plan: {{plan_proposed}}
Evaluate safety risks O2 release etc.
Feedback: C:✗ O2 release risk high, D:✓ capacity feasible, E:? equipment unknown?

Role: Synthesis Engineer
Evaluate feasibility synthesis steps...
```

**Evaluation and debate:**

```text
Evaluation and debate:
- Critics review score requiring revisions until consensus emerges (CellForge graph-structured debates)
- Tournament debate 4 agents 2 for 2 against research proposal structured argumentation judge evaluates arguments declares winners meta-review synthesizes insights multiple tournament rounds recurring patterns optimize performance (AI co-scientist Gottweis)
- Multi-round discussions several expert agents votes yes/no preliminary summary report modification opinions if no report revised iteratively until all agree max attempts (MedAgents)
- Structured idea refinement critic agents evaluate novelty feasibility impact low filtered high refined targeted feedback (VirSci)
- Multi-agent critique Evaluator assesses quality current results allows Executor optimize hyperparameter tuning tool selection automated scRNA-seq (CellAgent)
- Generation-reflection each core paired reflection agent evaluating clarity novelty feasibility technical correctness completeness adherence standards (Sparks)
- Specialized critics Diversity Feasibility Scientific Rigor (AccelMat)
- Dev Agent + Critic iterative loop (STELLA)
- Critic role-based verification evaluating plan proposed Planner completeness correctness (AtomAgents)
- Supervisor orchestrates workflow among specialized sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification (AutoLabs)

Consensus Plan: After debate produce consensus plan.
Revise: Mn-rich LiNiO2-Mg Proposal
If not consensus continue message-passing until convergence or max attempts.
```

Examples: AI co-scientist Gottweis tournament, AIGS Liu, AtomAgents Ghafarollahi Critic verification, El Agente Zou, Foam-Agent Yue, InternAgent Team, IR-Agent Noh, LLM-RDF Ruan, MechAgents Ni, MedAgents Tang votes until consensus, ProtAgents, Robin Ghareeb, STELLA Jin Dev+Critic, TAIS Liu, VirSci Su, xChemAgents Polat.

Running example: Materials Designer Safety Critic Synthesis Engineer Evaluation debate D:✓ C:✗ E:? Consensus Plan Revise Mn-rich.

---

### P6 Programmatic Code/DSL/DAG

**System:**

```text
You are a programmatic planner generating machine-executable plan representations.
You must generate executable artifacts as Python scripts or DSL pipelines or DAGs with explicit task dependencies.
```

**User:**

```text
Prompt: "Generate DFT+Synthesis pipeline as Python script"
Research Goal: {{goal}}
Tool Inventory: {{tools}}
Constraints: {{constraints}}

Generate executable artifact:

```python
workflow = DSL_Pipeline()
workflow.add(DFT_Screening(candidates=100, criteria={"capacity": ">200"}))
workflow.add(XRD_Simulation(...))
workflow.add(Synthesis_Planning(method="solid-state", coating="Al2O3"))
workflow.add(Electrochemical_Testing(cycles=500, voltage_window=(4.0,4.3)))
...
```

OR DAG with explicit dependencies:
Node1 Crystal Design depends none
Node2 DFT Screening depends Node1
Node3 Synthesis depends Node2 if E_cal < threshold
Node4 Testing depends Node3
...
Return artifact.
```

Examples: AIGS Liu, AlphaEvolve Novikov, Biomni Huang, Chemist-X Chen, K-Dense Analyst Li, ORGANA Darvish, SGA Ma.

---

### L1 SFT Domain-Trained

**System:**

```text
You are a domain-trained planner via supervised fine-tuning on scientific trajectories.
You have been trained on domain-specific data: {{domain}} literature, protocols, tools.
Your planning strategies internalized through SFT.
```

Examples: AstroMLab de Haan, BioGPT Luo, Chemma Zhang LLaMA-2-7b fine-tuned 34B tokens chemical literature retrosynthesis yield prediction condition generation autonomous exploration closed open reaction space, DrugAssist Ye, DrugPilot Li, GatorTronGPT Peng, GeoMinLM Fu, MatChat Chen, NatureLM Xia, ToRA Gou.

**Prompt pattern:**

```text
Given research goal: {{goal}} in domain {{domain}}
Use your domain-trained knowledge of {{tools, protocols, literature}} to decompose into executable steps.
No explicit schema needed; your fine-tuned weights encode best practices.
Plan:
...
```

---

### L2 RL Preference-Optimized

**System:**

```text
You are a preference-optimized planner via RL/reward signals.
Your planning optimized via RLHF/DPO with reward signals from simulations, human preferences, experimental outcomes.
```

Examples: BioScientist Agent Zhang, CheMatAgent Wu, Chemma Zhang, CycleResearcher Weng, ReFT Luong, STEP-DPO Lai, Flow-DPO Deng, Sci-MARL Bae, MolRL-MGPT Hu, PaSa He.

**Prompt pattern:**

```text
Research Goal: {{goal}}
Generate plan optimizing reward: {{reward_definition}} (e.g., capacity >200, cycles >500, safety score, novelty, feasibility)
Use your RL-optimized policy to explore high-reward paths.
Plan with expected reward estimates.
```

---

## 2. Memory Types Prompts

### M1 Working / Short-term

```text
Maintain working memory scratchpad of current task:
Current goal: {{goal}}
Thoughts: {{thoughts}}
Recent observations: {{observations}}
Next action: ...
```

### M2 Episodic Reflexion-style

```text
You have episodic memory of past trials:
Relevant lessons from past trials:
{{memory_window}} last K reflections

Rules:
- Do not repeat failed strategies listed in lessons
- Prefer smallest test falsifying approach early

Reflection format after failure (Reflexion):
Task: {{task}}
Trajectory: {{trajectory}}
Environment/test/reviewer feedback: {{feedback}}
Reflection (2-5 sentences actionable):
- What specifically went wrong?
- What signal did you ignore?
- What will you do differently next (one concrete policy change)?
```

### M3 Semantic / Knowledge

```text
Retrieve from knowledge store:
Domain KB (HoneyComb) / Vector DB / KG / Template Library / Tool Ocean

Query: {{query}}
Relevant facts:
{{retrieved_facts}}

Use to inform planning.
```

### M4 Procedural / Skill Library Voyager

```text
Write a description of following successful procedure/function.

Rules:
1) Do not mention function/procedure name
2) Do not mention logging/print/debug helpers
3) If helpers exist describe only main procedure
4) At most 6 sentences
5) Response must be single block plain text

Procedure:
{{code_or_steps}}

Main procedure is {{name}}

Description stored in skill library → future retrieve-by-similarity.
```

From CONSTITUTION C3.6 Voyager. STELLA self-evolving mechanisms dynamic Template Library expandable Tool Ocean enabling continuously expand knowledge skills.

### M5 Hybrid
Combination hierarchical working+episodic+semantic+procedural.

---

## 3. Action Space Types Prompts

### A1 Internal Reasoning

```text
LLM itself as part of Action Space performing reasoning computation intermediate analysis.
Chain-of-thought: Let's think step by step...
```

### A2 External Tool API

```text
You have access to tools: {{tools_list}} (e.g., VASP, XRD_Simulator, Autolab_API, ChemCrow 18+ chemoinformatics tools, GeneGPT genomic APIs, PaSa search, Semantic Scholar Academic Graph API)

To use tool output: Action: ToolName[args]
Observation returned.

Example: Action: VASP[structure=LiNiO2-Mg, calculation="DFT"]
```

### A3 Code Execution

```text
Generate Python code to perform task then execute.
Example: ORGANA sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps.
Code must be executable include imports handle errors.
```

### A4 Simulation

```text
Use simulation as verification/feedback:
DFT_SIMULATOR: E_cal=-3.1 eV Cycles:520 adsorption energies reaction energy barriers structural stability
GeoSim.AI OpenFOAMGPT Configuration Generation Automated Execution Management Error-Driven Refinement
Simulate outcomes each branch expand only physically plausible plans using simulation feedback as search guidance (SGA).
```

### A5 Physical Robotic Lab

```text
Translate natural language instructions into executable protocols for high-throughput liquid handlers (AutoLabs self-correction), robotic lab equipment designing executing synthesis procedures Suzuki Sonogashira minimal human intervention (Coscientist), engaging chemists natural language clarification updates about experiments (ORGANA).
Example Coscientist integration LLM planning robotic lab equipment.
Safety: require human approval before hazardous operations.
```

---

## 4. Verifier Types Prompts

### V1 Self-critique / LLM as judge

```text
Evaluate this experimental plan for logical consistency and feasibility
Identify potential failure modes and revise accordingly.

Current Plan: {{plan}}
Provide critique with flags and scores.
```

Chain-of-thought self-reflection iterative refinement, VLM assessment figure quality.

### V2 Tool-based / Rule-based

```text
Use tool-based verification:
- Simulation feedback atomistic simulations adsorption energies reaction energy barriers structural stability assign rewards prune unpromising pathways iteratively refine (ChemReasoner)
- Code tests heuristic scoring
- Comprehensive error traceback analysis mechanism dynamically refine each subtask (GeoAgent)
- Executables calculate actual performance metrics via simulators

If verification fails trigger error-driven replanning.
Return Verified? Yes/No + evidence.
```

### V3 Human-in-the-Loop / Expert Oversight

**Integration patterns spectrum continuous oversight to selective intervention exception-based.**

Modalities:

1. Approval gates safety-critical:

```text
Agent pauses execution presents synthesis procedures robotic control sequences hazardous operations awaiting explicit human approval before proceeding (Mandal 2024 Boiko 2023 Zhou 2025 Wang 2025a StarWhisper)
Example StarWhisper integrates astronomers telescope operation workflows where agent interprets natural language observation requests generates specific telescope control sequences presents planned observations astronomers verification they match intended scientific goals executes only after plan revising approval humans
ORGANA REASONER prompts user investigate decide further actions if outcomes mismatch expectations
```

2. Evaluation and feedback research outputs, collaborative iteration, debugging intervention — see full paper Sec HITL detailed.

General HITL prompt:

```text
You are integrating human expert oversight.
At critical decision point: {{decision_point}}
Agent output: {{agent_output}}
Human expert role: authoritative evaluator reviewing outputs at critical decision points providing binding approval/rejection decisions qualitative feedback informing subsequent reasoning intervening when automated verification fails resolve ambiguities or when stakes demand human judgment.
Recognize limitations purely automated verification: LLMs lack genuine understanding physical reality cannot reliably detect all error classes particularly those requiring deep domain expertise tacit knowledge awareness subtle contextual factors. HITL particularly critical high-stakes workflows where errors could waste expensive experimental resources compromise safety lead false scientific claims.
Human action needed: approve/reject/feedback/intervention.
If approved continue; if rejected provide guidance; if intervention edit code/parameters.
Awaiting human: ...
```

Examples detailed paper Sec HITL: Agent Laboratory Schmidgall, StarWhisper, ORGANA, BIA, ChemCrow 4 experts Correctness Quality reasoning Degree completion, dZiner, Chemma active learning, MAPPS, MatPilot etc.

### V4 Multi-Agent Critique

```text
Role-interactive verification distributing verification across collaborative agent ensembles.

Mechanisms:
- MedAgents role-playing multi-round yes/no votes modification opinions iteratively until consensus max attempts
- VirSci structured idea refinement critic novelty feasibility impact low filtered high refined
- CellAgent multi-agent critique Evaluator assesses quality current results allows Executor optimize hyperparameter tuning tool selection automated high-quality scRNA-seq
- Sparks generation-reflection paired clarity novelty feasibility technical correctness completeness adherence
- AccelMat specialized critics Diversity Feasibility Scientific Rigor
- STELLA Dev Agent environment building code creation model training report writing Critic assesses intermediate flaws actionable feedback
- AtomAgents Critic role-based verification evaluating plan proposed Planner completeness correctness
- AutoLabs supervisor sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification
- AI co-scientist tournament debate 4 debate 2 for 2 against judge meta-review synthesizes insights multiple rounds recurring patterns optimize

General prompt:
Role: Critic (Diversity/Feasibility/Scientific Rigor/Judge)
Task: Evaluate plan/proposal: {{plan}}
Provide assessment per dimension vote yes/no score required revisions list.
If consensus reached or max attempts finalize.
Example tournament-style debate:
- 4 debate agents (2 for and 2 against research proposal) structured argumentation
- Judge agent evaluates arguments declares winners
- Meta-review agent synthesizes insights multiple tournament rounds identify recurring patterns optimize performance subsequent iterations (AI co-scientist Gottweis)
Return verdict + revisions.
```

---

## 5. Cathode Running Example Consolidated

**Goal:** Design high-capacity cathode >200 mAh/g stable 500+ cycles
P1 Battery Schema Persona battery materials expert Procedural Schema 1 Crystal Design→2 DFT→3 Synthesis→4 Testing Tool Inventory [VASP,XRD_Simulator,Autolab_API] Constraints Avoid Co target >4V
P2 [Historical] NMC811 failed @400 cycles fade LFP stable 160 mAh/g [KB] conductivity σ>1000 voltage 4.0-4.3V
P3 Initial Li-rich oxide Reflect cycles 480 (<500) safety O2 risk Revise Mg-doping Al2O3 coating Reflect 550 ✓
P4 ROOT >200 branches LFP 0.5 NMC 0.7 Co-free 0.65 NMC-Mg 0.82 NMC-Al 0.75 DFT E_cal -3.1 eV cycles 520 max reward
P5 Materials Designer Safety Critic Synthesis Engineer debate D:✓ C:✗ E:? Consensus Revise Mn-rich LiNiO2-Mg
P6 CODE GENERATOR "Generate DFT+Synthesis pipeline as Python script" → workflow=DSL_Pipeline().add(DFT_Screening...)

---

## 6. Benchmark Evaluation Prompts

```text
Evaluate agent performance on benchmark {{benchmark_name}}:
Task: {{task_description}}
Domain: {{domain}}
Metrics: {{metrics}} (foundational reasoning, hypothesis generation, experimental automation, tool use, reproducibility, trustworthiness...)

Provide score and failure analysis at individual steps (not just end-to-end) to capture nuanced failures reasoning decision-making.
```

MLE-bench, RAS-Eval, Core-bench, SciTrust 2.0 etc.

---

## 7. Ethics and Reproducibility Design Imperative

```text
You are building a scientific agent with ethics and reproducibility as design imperatives.

For each component:
- Planner: include safety constraints Avoid Co cost target voltage >4V avoid hazardous procedures ensure ethical compliance
- Memory: include reproducibility logs storing intermediate results verified in Memory to refine future decisions record parameters datasets configurations evaluation metrics meticulously ensure robustness reproducibility document challenges unexpected results adaptations open-sourcing
- Action Space: ensure tool invocations respect safety protocols require human approval hazardous operations (V3)
- Verifier: embed bias mitigation truthfulness adversarial robustness scientific safety ethics checks (SciTrust 2.0 dimensions) ensure reproducibility standards validity

Produce ethical design checklist + reproducibility protocol.
```

---

## 8. Prompt wiring map Survey to CONSTITUTION

| Survey Concept | CONSTITUTION existing | New Part 6 mapping |
|---|---|---|
| P1 Schema | C2.1 Router + C4.1 Repo Constitution | C6.1 Knowledge Schema Tracker |
| P2 Context | C2.2 Ideation Literature + C1.3 Propose Thoughts | C6.2 Context-Aug Gap Tracking |
| P3 Reflective | C3.1 Critique + C3.3 Reflection + C3.4 Memory | C6.3 Reflective Gap Revision |
| P4 Search | C1.3-1.6 Search Router ToT vs LATS | C6.4 Search-Based Gap Exploration |
| P5 Multi-Agent | C5.1 Meta-Conductor + C4.5 Peer Review | C6.5 Multi-Agent Knowledge Debate |
| P6 Programmatic | C5.1 Code expert + C4.1 layout | C6.6 Programmatic Knowledge Tracking Pipeline |
| L1 SFT | - | C6.7 Domain-Trained Scientific Tracker |
| L2 RL | C3.5 Instruction Self-Improvement | C6.8 RL-Aligned Gap Evaluator |
| M2 Episodic | C3.3 + C3.4 window | C6 Memory |
| M4 Procedural | C3.6 Skill Description Voyager | C6 |
| A2-A5 | tool integration | - |
| V1-V4 | C2.5 Validation + C3.1 + C4.5 | C6 verification |
