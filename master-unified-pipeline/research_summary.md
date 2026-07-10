# ARSENAL — Unified Master Pipeline Research Summary

## Problem

Each of the eight systems solves a *different slice* of the LLM-agent problem:

| System | Solves | Blind spot alone |
|---|---|---|
| Prompt Report | *What technique to use* | Does not execute loops |
| APE | *What instruction to write* | Does not act in environments |
| Meta-Prompting | *How to decompose and dispatch* | Shallow search / no long-term memory |
| Tree of Thoughts | *How to search offline thought space* | No env reward / UCT / failure reflection |
| LATS | *How to search interactive / long-horizon space* | Expensive; needs good prompts & memory |
| Self-Refine | *How to polish a single draft* | No multi-trial memory or tree search |
| Reflexion | *How to learn across trials* | No automatic prompt search or deep tree |
| AI Scientist v2 | *How to run a full research pipeline* | Domain-specific; inherits all of the above needs |

None of them alone is a complete agentic arsenal. Together they cover:

**routing → prompt optimization → decomposition → tree search → local polish → trial memory → multi-stage production + review.**

## Unification thesis

> Treat every hard task as a *staged production pipeline* (AI Scientist v2), where each stage is *routed* by technique family (Prompt Report), *prompt-optimized* (APE), *decomposed by a conductor* (Meta-Prompting), *searched under uncertainty* (ToT baseline and/or LATS full), *locally refined* (Self-Refine), and *improved across trials via verbal memory* (Reflexion).

## ARSENAL in one paragraph

**ARSENAL** (Automatic Reasoning, Search, Evaluation, Navigation, and Adaptive Learning) is a six-layer master pipeline. A **technique router** (Prompt Report taxonomy) chooses the active family. An **instruction optimizer** (APE generate/evaluate/rank) produces the working prompts. A **meta conductor** (Meta-Prompting) breaks the task into expert subcalls, including tool/Python experts. Under uncertainty, a **tree search engine** explores candidates — **ToT** (BFS/DFS deliberate thoughts) for offline puzzles, **LATS** (MCTS/UCT + env + reflection) for interactive horizons; each leaf/candidate is **locally polished** (Self-Refine generate→feedback→refine). Failures become **verbal episodic memory** (Reflexion) that conditions later trials. The outer shell is a **progressive multi-stage production pipeline** (AI Scientist v2) with multi-seed evaluation, aggregation, writeup, and peer review.

## Layer map

```
L0  Technique Router .............. Prompt Report
L1  Instruction Optimizer ......... APE
L2  Meta Conductor / Experts ...... Meta-Prompting
L3  Tree Search Engine ............ ToT (baseline) + LATS (full)
L4  Local Polisher ................ Self-Refine
L5  Episodic Verbal Memory ........ Reflexion
L6  Progressive Stage Shell ....... AI Scientist v2
```

## Inputs / Outputs

**Inputs**

- Task description / problem / research idea / user query
- Optional demos (for APE)
- Optional tools (Python, search, env, code executor)
- Config: budgets (tokens, rounds, tree depth, refine iters, trials, stages)

**Outputs**

- Best instruction/prompt (APE)
- Expert call log (Meta-Prompting)
- Search tree + best trajectory (LATS)
- Refined final artifact (Self-Refine)
- Reflection memory bank (Reflexion)
- Stage artifacts: metrics, plots, paper, peer review (AI Scientist v2)

## Core loops (unified)

1. **Outer stage loop** (AI Scientist v2): Stage 1 draft → Stage 2 tune → Stage 3 improve → Stage 4 ablate → writeup → review.
2. **Trial loop** (Reflexion): for trial in 1..T with memory.
3. **Tree iteration** (L3): ToT generate→evaluate→select beam/DFS **or** LATS UCT→expand→value→rollout→backprop→optional reflect.
4. **Expert round** (Meta-Prompting): meta call → expert call → append feedback → until final answer.
5. **Refine loop** (Self-Refine): generate → feedback → stop? → refine → history.
6. **Prompt search** (APE): generate candidates → dedup → evaluate (likelihood/UCB) → rank.
7. **Technique route** (Prompt Report): classify task → pick family → pick method.

## Decision points (unified)

- Which technique family? (Prompt Report)
- Need prompt search? (APE on/off)
- Need decomposition? (Meta conductor on/off)
- Need tree search or single-path? (LATS vs direct)
- Stop refine? (Self-Refine stop criteria)
- Success / store reflection? (Reflexion)
- Stage complete / advance stage? (AI Scientist v2)
- Multi-seed eval / writeup / peer review? (AI Scientist v2)

## Why this is stronger than any single system

| Capability | Alone | In ARSENAL |
|---|---|---|
| Technique selection | Manual | Automatic (Prompt Report) |
| Prompt quality | Hand-written | APE-optimized |
| Decomposition | Ad-hoc | Meta conductor + experts |
| Exploration | Greedy or none | LATS UCT tree |
| Local quality | One-shot | Self-Refine multi-aspect |
| Cross-trial learning | None or weights | Verbal episodic memory |
| End-to-end production | Task-specific | Progressive stages + review |

## Scope of this package

This package is a *research extraction and design synthesis*, not a runnable product. It documents:

- strongest patterns from each of the 8 audited systems,
- a complete master architecture,
- master prompts,
- full logic flow and inventory,
- English + Arabic Mermaid graphs,
- Arabic completeness and quality audits.

Source of truth for each system remains the individual extraction repos under `faresrafat3/*-full-extraction` and the consolidated `llm-agent-research-extractions`.
