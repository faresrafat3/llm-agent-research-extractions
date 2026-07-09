# LATS — Research / System Summary

Paper: https://arxiv.org/abs/2310.04406  
Code: https://github.com/lapisrocks/LanguageAgentTreeSearch  
Audited commit: `853d81614607dd27433faf17c7b0a7d660f95d22`

## Core idea

Language Agent Tree Search (LATS) unifies reasoning, acting, and planning in language agents by integrating Monte Carlo Tree Search with LM-generated thoughts/actions, LM value functions, external environment feedback, and self-reflection.

## General loop

1. Start from a root state/question/problem.
2. Select a node using UCT/tree policy.
3. Expand by prompting the LM for candidate thoughts/actions/code.
4. Evaluate candidate nodes with LM value prompts and/or environment feedback.
5. Roll out promising candidates through environment/executor.
6. If success is found, return trajectory/solution.
7. Otherwise backpropagate reward/value.
8. Generate self-reflections from failed trajectories when useful.
9. Repeat until iterations/max depth/exhaustion.

## Implemented domains

- HotPotQA interactive question answering.
- WebShop navigation.
- Programming tasks including HumanEval/MBPP/LeetCode in Python/Rust/Go.
- Baselines/variants: ToT, RAP, DFS, Reflexion, simple generation.
