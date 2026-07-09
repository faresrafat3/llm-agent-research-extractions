# Consolidated Research Summary — LLM Agent Research Extractions

This repository consolidates prompt, logic, flow, and graph extraction packages for four LLM agent/self-improvement systems:

1. AI Scientist v2 — autonomous scientific discovery via staged agentic tree search.
2. Self-Refine — iterative generation, self-feedback, and refinement.
3. Reflexion — verbal reinforcement learning with episodic reflection memory.
4. Meta-Prompting — task-agnostic conductor/expert scaffolding with optional Python execution.

## Common theme

All four systems use language models not merely as direct answer generators, but as structured components in larger control loops:

- AI Scientist v2 uses LLMs/VLMs as researchers, coders, experiment managers, plotters, citation gatherers, writers, and reviewers.
- Self-Refine uses the same LLM as generator, feedback provider, and refiner.
- Reflexion uses verbal reflections as memory to improve future trials without weight updates.
- Meta-Prompting uses one LM as a conductor that delegates subtasks to expert instances and integrates their outputs.

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
