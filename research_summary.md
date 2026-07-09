# Consolidated Research Summary — LLM Agent Research Extractions

This repository consolidates prompt, logic, flow, and graph extraction packages for seven LLM agent/self-improvement systems:

1. AI Scientist v2 — autonomous scientific discovery via staged agentic tree search.
2. Self-Refine — iterative generation, self-feedback, and refinement.
3. Reflexion — verbal reinforcement learning with episodic reflection memory.
4. Meta-Prompting — task-agnostic conductor/expert scaffolding with optional Python execution.
5. LATS — Language Agent Tree Search unifying reasoning, acting, and planning via MCTS.
6. APE — Automatic Prompt Engineer, treating prompts as programs optimized via LLM generation + likelihood/bandit evaluation.
7. Prompt Report — systematic survey: 58 LLM prompting techniques + 40 multimodal, 33 vocabulary terms, full taxonomy.

## Common theme

All seven systems use language models not merely as direct answer generators, but as structured components in larger control loops:

- AI Scientist v2 uses LLMs/VLMs as researchers, coders, experiment managers, plotters, citation gatherers, writers, and reviewers.
- Self-Refine uses the same LLM as generator, feedback provider, and refiner.
- Reflexion uses verbal reflections as memory to improve future trials without weight updates.
- Meta-Prompting uses one LM as a conductor that delegates subtasks to expert instances and integrates their outputs.
- LATS uses LLMs as agents, value functions, and optimizers inside a Monte Carlo Tree Search.
- APE uses LLMs to propose natural-language instructions, then searches over candidates via likelihood scoring or UCB bandits.
- Prompt Report systematizes the entire field: 58 text techniques across ICL, Thought Generation, Decomposition, Ensembling, Self-Criticism, Answer Engineering — plus 40 multilingual/multimodal/agent techniques — providing a unified taxonomy and decision roadmap.

## Repository purpose

The goal of this consolidated repo is to make each system's hidden control flow explicit:

- prompts,
- loops,
- conditions,
- decision points,
- inputs/outputs,
- raw prompt/config sources,
- Mermaid graphs,
- final quality reviews.

See `PROJECT_INDEX.md` for exact per-project paths.
