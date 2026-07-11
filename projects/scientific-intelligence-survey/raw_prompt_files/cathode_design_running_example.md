# Cathode Design Running Example - Consolidated

Research Goal: "Design and synthesize a high-capacity cathode material for Li-ion batteries (>200 mAh/g, stable for 500+ cycles)"

## P1 Instructional Schema-Driven

SYSTEM PROMPT Battery Schema
Persona: "You are a battery materials expert..."
Procedural Schema:
1. Crystal Structure Design → 2. DFT Screening → 3. Synthesis Planning → 4. Electrochemical Testing
Tool Inventory: [VASP, XRD_Simulator, Autolab_API]
Constraints: Avoid Co (cost), target voltage >4V
Plan: STEP1 xxx -> STEP2 xxx -> ...

## P2 Context-Augmented

AUGMENTED PROMPT
[Historical] NMC811 failed @400 cycles (capacity fade)
[Historical] LFP stable but capacity only 160 mAh/g
[KB] Target conductivity: σ >1000 mS/cm for rate capability
[KB] Voltage window: 4.0-4.3V vs Li/Li+
[KBs] Records from HoneyComb domain KB / CellVoyager Template Library Tool Ocean persistent context
Design new material avoiding NMC811's Mn dissolution issue while exceeding LFP capacity...
Plan: STEP1 xxx -> STEP2 xxx -> ...

## P3 Deliberative Reflective

Generate Initial Plan: Li-rich oxide
Reflect: Evaluate flaws
- Cycles: 480 (<500)
- Safety: O2 release risk
Revise: Mg-doping + Al2O3 coating
Reflect: Cycles=550 ✓
Converged? Yes
Final Plan with reflection

## P4 Search-Based

[ROOT: Cathode >200 mAh/g]
[LFP Variant] (Score: 0.5)
[NMC Variant] (0.7)
[Co-free Layered] (0.65)
[NMC-Mg] (0.82)
[NMC-Al] (0.75)
DFT_SIMULATOR E_cal=-3.1 eV Cycles:520
Final Plan with max reward path

## P5 Role-Interactive Multi-Agent

Materials Designer
Safety Critic
Synthesis Engineer
Evaluation and debate → D:✓ C:✗ E:? Consensus Plan
Revise: Mn-rich LiNiO2-Mg Proposal

## P6 Programmatic

LLM CODE GENERATOR Prompt: "Generate DFT+Synthesis pipeline as Python script"
EXECUTABLE ARTIFACT
```python
workflow = DSL_Pipeline()
workflow.add(DFT_Screening(candidates=100, criteria={"capacity": ">200"}))
workflow.add(XRD_Simulation(...))
workflow.add(Synthesis_Planning(method="solid-state", coating="Al2O3"))
workflow.add(Electrochemical_Testing(cycles=500, voltage_window=(4.0,4.3)))
...
```
OR DAG with explicit task dependencies
Node1 Crystal Design depends none
Node2 DFT Screening depends Node1
Node3 Synthesis depends Node2 if E_cal < threshold
Node4 Testing depends Node3

## Blueprint for building any scientific agent mix-and-match all components
