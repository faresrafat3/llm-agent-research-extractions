# ARSENAL — Unified Master Pipeline Research Summary

## Problem

Each of the ten systems solves a *different slice* of the LLM-agent problem:

| System | Solves | Blind spot alone |
|---|---|---|
| Prompt Report | *What technique to use* | Does not execute loops |
| APE | *What instruction to write (one-shot/bandit)* | No multi-step score-conditioned search |
| OPRO | *How to iteratively improve instructions via meta-prompts* | Costly eval loop; needs a scorer |
| Meta-Prompting | *How to decompose and dispatch* | Shallow search / no long-term memory |
| Tree of Thoughts | *How to search offline thought space* | No env reward / UCT / failure reflection |
| LATS | *How to search interactive / long-horizon space* | Expensive; needs good prompts & memory |
| Self-Refine | *How to polish a single draft* | No multi-trial memory or tree search |
| Reflexion | *How to learn across trials (verbal)* | No automatic prompt search; no skill library |
| Voyager | *How to grow open-ended skills + curriculum* | Domain-tied (Minecraft); heavy env |
| AI Scientist v2 | *How to run a full research pipeline* | Domain-specific; inherits all of the above needs |

None of them alone is a complete agentic arsenal. Together they cover:

**routing → prompt optimization (APE/OPRO) → decomposition → tree search → local polish → trial + skill memory (Reflexion/Voyager) → multi-stage production + review.**

## Unification thesis

> Treat every hard task as a *staged production pipeline* (AI Scientist v2), where each stage is *routed* by technique family (Prompt Report), *prompt-optimized* (APE and/or OPRO), *decomposed by a conductor* (Meta-Prompting), *searched under uncertainty* (ToT and/or LATS), *locally refined* (Self-Refine / Voyager critic loop), *remembered* via verbal trials (Reflexion) and optional *skill library + curriculum* (Voyager).

## ARSENAL in one paragraph

**ARSENAL** (Automatic Reasoning, Search, Evaluation, Navigation, and Adaptive Learning) is a six-layer master pipeline. A **technique router** (Prompt Report) chooses the active family. An **instruction optimizer** produces working prompts via **APE** (one-shot/bandit) and/or **OPRO** (iterative meta-prompt evolution on score history). A **meta conductor** (Meta-Prompting) decomposes work into expert subcalls. Under uncertainty, **L3 tree search** uses **ToT** offline and/or **LATS** interactive; candidates are **locally polished** (Self-Refine; Voyager-style env critique for code). **L5 memory** combines **Reflexion** verbal reflections with optional **Voyager skill library + automatic curriculum** for open-ended procedural growth. The outer shell is **AI Scientist v2** progressive stages with multi-seed eval, writeup, and peer review.

## Layer map

```
L0  Technique Router .............. Prompt Report
L1  Instruction Optimizer ......... APE (baseline) + OPRO (iterative)
L2  Meta Conductor / Experts ...... Meta-Prompting
L3  Tree Search Engine ............ ToT (baseline) + LATS (full)
L4  Local Polisher ................ Self-Refine (+ Voyager critic pattern)
L5  Memory ........................ Reflexion (verbal) + Voyager (skills/curriculum)
L6  Progressive Stage Shell ....... AI Scientist v2
```

## Inputs / Outputs

**Inputs**

- Task description / problem / research idea / user query
- Optional demos (for APE)
- Optional tools (Python, search, env, code executor)
- Config: budgets (tokens, rounds, tree depth, refine iters, trials, stages)

**Outputs**

- Best instruction/prompt (APE and/or OPRO)
- Expert call log (Meta-Prompting)
- Search tree + best trajectory (LATS)
- Refined final artifact (Self-Refine)
- Reflection memory bank (Reflexion)
- Skill library / curriculum progress (Voyager)
- Stage artifacts: metrics, plots, paper, peer review (AI Scientist v2)

## Core loops (unified)

1. **Outer stage loop** (AI Scientist v2): Stage 1 draft → Stage 2 tune → Stage 3 improve → Stage 4 ablate → writeup → review.
2. **Trial loop** (Reflexion): for trial in 1..T with memory.
3. **Tree iteration** (L3): ToT generate→evaluate→select beam/DFS **or** LATS UCT→expand→value→rollout→backprop→optional reflect.
4. **Expert round** (Meta-Prompting): meta call → expert call → append feedback → until final answer.
5. **Refine loop** (Self-Refine): generate → feedback → stop? → refine → history.
6. **Prompt search**: APE generate→dedup→likelihood/UCB **or** OPRO meta-prompt evolve on scores **or** cascade APE→OPRO.
7b. **Skill curriculum** (Voyager, optional): propose task → iterative code → critic → store skill.
8. **Technique route** (Prompt Report): classify task → pick family → pick method.

## Decision points (unified)

- Which technique family? (Prompt Report)
- Need prompt search? APE / OPRO / cascade / off
- Need decomposition? (Meta conductor on/off)
- Need tree search or single-path? (LATS vs direct)
- Stop refine? (Self-Refine stop criteria)
- Success / store reflection? (Reflexion)
- Store skill / propose next curriculum task? (Voyager)
- Stage complete / advance stage? (AI Scientist v2)
- Multi-seed eval / writeup / peer review? (AI Scientist v2)

## Why this is stronger than any single system

| Capability | Alone | In ARSENAL |
|---|---|---|
| Technique selection | Manual | Automatic (Prompt Report) |
| Prompt quality | Hand-written | APE and/or OPRO-optimized |
| Decomposition | Ad-hoc | Meta conductor + experts |
| Exploration | Greedy or none | ToT beam / LATS UCT |
| Local quality | One-shot | Self-Refine multi-aspect |
| Cross-trial learning | None or weights | Verbal memory + optional skill library |
| End-to-end production | Task-specific | Progressive stages + review |

## Scope of this package

This package is a *research extraction and design synthesis*, not a runnable product. It documents:

- strongest patterns from each of the 10 audited systems,
- a complete master architecture,
- master prompts,
- full logic flow and inventory,
- English + Arabic Mermaid graphs,
- Arabic completeness and quality audits.

Source of truth for each system remains the individual extraction repos under `faresrafat3/*-full-extraction` and the consolidated `llm-agent-research-extractions`.
