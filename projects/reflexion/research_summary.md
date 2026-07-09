# Reflexion — Research / Paper Summary

Paper: https://arxiv.org/abs/2303.11366  
Code: https://github.com/noahshinn/reflexion  
Audited commit: `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

## Core idea

Reflexion is verbal reinforcement learning for language agents. Instead of updating model weights, the agent converts environment/test/reward feedback into natural-language reflections, stores those reflections in episodic memory, and uses them as context in subsequent trials.

## General loop

1. Initialize task/environment/problem.
2. Run an agent episode/attempt with current memory.
3. Collect feedback: success/failure, scalar reward, observation trajectory, compiler/test output, or self-evaluation.
4. Generate verbal reflection summarizing why the attempt failed or how to improve.
5. Store reflection in memory.
6. Repeat next trial using memory.
7. Stop after success, max trials, max steps, or exhausted task set.

## Implemented task families

- AlfWorld sequential decision-making.
- WebShop interactive shopping.
- HotPotQA reasoning with CoT/ReAct/reflection.
- Programming tasks: HumanEval, MBPP, LeetCode, Python/Rust.
- Baselines: simple, immediate refinement, immediate reflexion, reflexion, reflexion-UCS/test-generation.

## Feedback sources

- Binary success/failure.
- Environment history and observations.
- Heuristic stuck/repetition detection.
- Unit test failures and compiler/runtime errors.
- Model-generated tests/evaluations.
- Reflexion memory buffer.
