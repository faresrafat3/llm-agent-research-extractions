# LATS — Deep Dive Task / Flow Matrix

## Universal LATS / MCTS loop

| Step | Purpose | Code concepts | Decisions |
|---|---|---|---|
| Selection | choose promising node | `select_node`, UCT | terminal/exhausted/all-terminal? |
| Expansion | sample new thoughts/actions | `get_samples`, `expand_node` | standard vs CoT prompt, reflection available? |
| Evaluation | score candidates | `get_value`, value prompts | cache hit? duplicate candidate? |
| Rollout | simulate trajectory | `rollout`, env/executor | success, max depth, terminal, error |
| Backprop | update tree values | `backpropagate` | propagate until root |
| Reflection | learn from failures | failed trajectories/reflection map/self_reflection | unique failures, reflection threshold |

## HotPotQA

Files: `hotpot/lats.py`, `hotpot/hotpot.py`, `hotpot/base.py`, `hotpot/tot.py`, `hotpot/rap.py`, `hotpot/wikienv.py`, `hotpot/wrappers.py`.

Flow: reset Wiki environment for question; root node stores question; MCTS iterations select/expand/evaluate/rollout; actions interact with Wiki env; failed trajectories can produce self-reflections; success is exact match/reward.

Key loops: iteration loop, selection while-loop, step retry loop, rollout depth loop, unique trajectory loop.

Key decisions: terminal reward 1, terminal reward 0 backtrack, all children terminal, cache value, generate reflection if failures exceed current reflection map, done/exhausted/max depth.

## WebShop

Files: `webshop/lats.py`, `webshop/base.py`, `webshop/prompt.py`, `webshop/webshop.py`.

Flow parallels HotPotQA but actions are web navigation/search/click operations and reward is shopping task score. Prompts include examples for actions and observations.

Decisions: valid action, terminal purchase/done, score thresholds, reflection from failed shopping trajectories.

## Programming

Files: `programming/mcts.py`, `programming/dfs.py`, `programming/main.py`, `programming/generators/*`, `programming/executors/*`.

Flow: load benchmark problem; generate code candidates; execute tests; score/pass/fail; reflect on failed implementations; tree search/DFS explores solution space; return successful implementation or best attempt.

Decisions: compile/runtime/test pass, max iterations, max depth, parse generated code, language executor type, self-reflection enabled, internal vs real tests.

## Inputs

- task data JSON/JSONL.
- question/problem prompt.
- environment state and observations.
- generated thought/action/code.
- failed trajectories.
- unit test feedback.

## Outputs

- final answer/action trajectory/code solution.
- reward/value/EM/pass status.
- logs and JSONL result artifacts.
- reflection text and tree nodes.
