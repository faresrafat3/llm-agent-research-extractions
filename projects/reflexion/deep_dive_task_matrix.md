# Reflexion — Deep Dive Task Matrix

## Universal Reflexion algorithm

| Component | Meaning | Code manifestations |
|---|---|---|
| Actor/Agent | LLM generates action/code/answer | AlfWorld/WebShop action loops, HotPotQA agents, programming generators |
| Environment/executor | produces observation/reward/error | AlfWorld env, WebShop env, HotPotQA search/env, Python/Rust executors |
| Evaluator | success/failure/test feedback | `done`, `reward`, `is_success`, unit tests, exact match, compiler output |
| Reflection generator | converts feedback to natural language memory | `generate_reflections.py`, programming `self_reflection`, HotPotQA reflect agents |
| Memory | stores reflections for future trials | env config `memory`, HotPotQA memory strings, programming previous reflections |
| Trial loop | repeat attempts | main scripts with `num_trials`, `max_iters`, pass@k loops |

---

## AlfWorld

Files: `alfworld_runs/main.py`, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py`, `alfworld_runs/env_history.py`, `alfworld_runs/prompts/*.json`.

Flow:

1. Parse CLI args: `num_trials`, `num_envs`, `run_name`, `use_memory`, resume info, model.
2. Initialize or resume `env_configs`, each with memory, success, skip flags.
3. `while trial_idx < num_trials`: run trial.
4. `run_trial` loops over envs.
5. Skip envs already successful.
6. Select base prompt by game prefix.
7. `alfworld_run` creates `EnvironmentHistory` with at most last 3 memories.
8. Step loop `while cur_step < 49`: prompt LLM for action, env.step, record observation.
9. Stop if `done`; fail if history exhausted or max steps.
10. If `use_memory`, `update_memory` generates reflections for failed histories and appends to env memory.

Key decisions: resume vs new run; already success skip; prefix prompt selection; done vs exhausted vs max step; use memory or not.

Outputs: trial logs, world logs, env_results JSON with memory and success state.

---

## WebShop

Files: `webshop_runs/main.py`, `webshop_runs/webshop_trial.py`, `webshop_runs/generate_reflections.py`, `webshop_runs/env_history.py`, `webshop_runs/base_prompt.txt`, `webshop_runs/reflection_few_shot_examples.txt`.

Flow parallels AlfWorld but with shopping/search/click actions and WebShop environment. The agent runs episodes, accumulates observations/actions, detects success/failure, then optionally generates reflection memory from failed attempts.

Key decisions: trial loop, environment loop, done/success, use memory, reflection update, action parsing/environment response.

Outputs: env result logs and reflection memory.

---

## HotPotQA

Files: `hotpotqa_runs/agents.py`, `hotpotqa_runs/prompts.py`, `hotpotqa_runs/fewshots.py`, `hotpotqa_runs/react.py`, `hotpotqa_runs/environment.py`, `hotpotqa_runs/llm.py`, notebooks and root logs.

Implements CoT and ReAct-style QA agents with optional context and reflection. Agents generate reasoning/actions/answers, environment/search gives observations, and memories/reflections from previous failed trials are included in future prompts.

Key decisions: CoT vs ReAct; context vs no context; base vs last-trial vs reflexion memory; correct answer/evaluation; max trials.

Outputs: joblib/text logs with answer trajectories and reflection memory.

---

## Programming Reflexion

Files: `programming_runs/main.py`, `reflexion.py`, `reflexion_ucs.py`, `simple.py`, `immediate_refinement.py`, `immediate_reflexion.py`, generators, executors.

Flow:

1. Load benchmark problem.
2. Generate initial code solution.
3. Execute tests via language executor.
4. If pass, record success.
5. If fail, generate natural-language self-reflection from code and test feedback.
6. Use reflection and feedback to generate next code attempt.
7. Repeat up to max iterations/pass@k.

Variants:

- simple: one-shot generation.
- immediate refinement: use feedback immediately without long-term memory.
- immediate reflexion: generate reflection and retry.
- reflexion: iterative memory-based retry.
- reflexion-UCS: uses generated tests / unit-test selection style feedback.

Key decisions: compile/runtime/test pass; max_iters; model type; language executor; parse generated code; sample count; visible/hidden tests.

Outputs: JSONL results, code candidates, test feedback, reflections, pass/fail metrics.

---

## Cross-cutting mechanisms

- Memory buffer is textual, not learned weights.
- Reflection is generated only after feedback/failure in most Reflexion paths.
- Prompts combine few-shot examples + task context + memory + current trajectory.
- LLM calls use OpenAI chat/completion wrappers or model abstractions.
- Logs/root artifacts are prior outputs; they are documented as artifacts rather than copied as prompt templates.
