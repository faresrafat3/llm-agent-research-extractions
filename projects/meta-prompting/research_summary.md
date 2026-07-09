# Meta-Prompting — Research / System Summary

Paper: https://arxiv.org/abs/2401.12954  
Code: https://github.com/suzgunmirac/meta-prompting  
Audited commit: `40422564938d772c3e3e6b9614b1df48b8dd6a08`

## Core idea

Meta-prompting is a task-agnostic scaffolding method where one language model acts as a Meta Model or conductor. It breaks a task into subtasks, calls expert instances of the same LM with tailored instructions, integrates expert outputs, verifies them, and returns a final answer.

## Algorithm

1. Wrap input query with meta-prompting instruction.
2. Meta Model produces either an expert call, a final answer, or an invalid response.
3. If expert call: extract expert name/instructions and query the expert in isolation.
4. If expert is Python and asks to run code: execute code and append output.
5. Append expert output plus intermediate feedback to message history.
6. Repeat until final-answer indicator appears or max round limit is reached.
7. Extract final answer.

## Compared methods

- Standard prompting.
- Zero-shot chain-of-thought.
- Expert static prompting.
- Expert dynamic prompting.
- Multipersona prompting.
- Meta-prompting without Python.
- Meta-prompting with Python expert.

## Tasks

Game of 24, Checkmate-in-One, BBH tasks, Python Programming Puzzles, MGSM, sonnet writing, word sorting, geometric shapes, multistep arithmetic.
