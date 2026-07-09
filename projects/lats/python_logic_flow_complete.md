# LATS — Complete Python Logic / Flow / Loops / Conditions / I-O Extraction

Source repo: `https://github.com/lapisrocks/LanguageAgentTreeSearch`  
Audited commit: `853d81614607dd27433faf17c7b0a7d660f95d22`

## System summary

LATS implements tree-search language agents for HotPotQA, WebShop, and programming tasks. The core loop uses selection, expansion, LM value evaluation, rollout/simulation, environment/test feedback, self-reflection, and backpropagation. Baselines include ReAct, ToT, RAP, DFS, Reflexion, and simple generation.

## Python files

- `hotpot/base.py`
- `hotpot/hotpot.py`
- `hotpot/hotpotqa.py`
- `hotpot/lats.py`
- `hotpot/models.py`
- `hotpot/rap.py`
- `hotpot/run.py`
- `hotpot/tot.py`
- `hotpot/wikienv.py`
- `hotpot/wrappers.py`
- `programming/dfs.py`
- `programming/executors/__init__.py`
- `programming/executors/executor_types.py`
- `programming/executors/executor_utils.py`
- `programming/executors/factory.py`
- `programming/executors/go_executor.py`
- `programming/executors/leet_executor.py`
- `programming/executors/py_executor.py`
- `programming/executors/rs_executor.py`
- `programming/generators/__init__.py`
- `programming/generators/factory.py`
- `programming/generators/generator_types.py`
- `programming/generators/generator_utils.py`
- `programming/generators/go_generate.py`
- `programming/generators/model.py`
- `programming/generators/parse.py`
- `programming/generators/py_generate.py`
- `programming/generators/rs_generate.py`
- `programming/human-eval/human_eval/__init__.py`
- `programming/human-eval/human_eval/data.py`
- `programming/human-eval/human_eval/evaluate_functional_correctness.py`
- `programming/human-eval/human_eval/evaluation.py`
- `programming/human-eval/human_eval/execution.py`
- `programming/human-eval/setup.py`
- `programming/immediate_refinement.py`
- `programming/immediate_reflexion.py`
- `programming/main.py`
- `programming/mcts.py`
- `programming/reflexion.py`
- `programming/root/get_acc.py`
- `programming/simple.py`
- `programming/test_acc.py`
- `programming/utils.py`
- `setup.py`
- `webshop/base.py`
- `webshop/lats.py`
- `webshop/models.py`
- `webshop/prompt.py`
- `webshop/run.py`
- `webshop/webshop.py`

---

## File: `hotpot/base.py`

**Lines:** 13  

### Imports
- `import os`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `Task` L2 bases=[]
##### `__init__(self)` (L3)
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `__len__(self)` (L6)
- Inputs: parameters `__len__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `get_input(self, idx)` (L9)
- Inputs: parameters `get_input(self, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `test_output(self, idx, output)` (L12)
- Inputs: parameters `test_output(self, idx, output)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.

### Functions
- None

---

## File: `hotpot/hotpot.py`

**Lines:** 534  

### Imports
- None

### Module assignments
- L1: `standard_prompt = ''' Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input} '''`
- L5: `reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning step...`
- L59: `cot_prompt = ''' Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search. (2) Lookup[keyword], which returns the next sent...`
- L104: `cot_prompt_short = ''' Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search. (2) Lookup[keyword], which returns the nex...`
- L139: `cot_prompt_feedback_short = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not,...`
- L177: `cot_prompt_feedback = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it wi...`
- L226: `vote_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search. (2) Lookup[ke...`
- L234: `compare_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search. (2) Lookup...`
- L242: `score_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search. (2) Lookup[k...`
- L250: `value_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some s...`
- L295: `value_prompt_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will retu...`
- L337: `value_prompt_reasoning = '''You are an advanced reasoning agent that can improve based on self refection. Analyze the trajectories of your previous solutions to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the ...`
- L397: `value_prompt_reasoning_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it...`
- L459: `value_prompt_reasoning_feedback_short = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If n...`
- L498: `rap_prompt = ''' Solve a question answering task with interleaving Thought and Action steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search. (2) Lookup[keyword], which returns the next sentence conta...`

### Prompt-like assignments
- L1 `standard_prompt`: `standard_prompt = ''' Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input} '''`
- L5 `reflection_prompt`: `reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either because ...`
- L59 `cot_prompt`: `cot_prompt = ''' Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If n...`
- L104 `cot_prompt_short`: `cot_prompt_short = ''' Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists...`
- L139 `cot_prompt_feedback_short`: `cot_prompt_feedback_short = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity]...`
- L177 `cot_prompt_feedback`: `cot_prompt_feedback = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], whic...`
- L226 `vote_prompt`: `vote_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the...`
- L234 `compare_prompt`: `compare_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns ...`
- L242 `score_prompt`: `score_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns th...`
- L250 `value_prompt`: `value_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searches the e...`
- L295 `value_prompt_feedback`: `value_prompt_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], which searc...`
- L337 `value_prompt_reasoning`: `value_prompt_reasoning = '''You are an advanced reasoning agent that can improve based on self refection. Analyze the trajectories of your previous solutions to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason abou...`
- L397 `value_prompt_reasoning_feedback`: `value_prompt_reasoning_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[entity], w...`
- L459 `value_prompt_reasoning_feedback_short`: `value_prompt_reasoning_feedback_short = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: (1) Search[enti...`
- L498 `rap_prompt`: `rap_prompt = ''' Solve a question answering task with interleaving Thought and Action steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it wil...`

### Classes
- None

### Functions
- None

---

## File: `hotpot/hotpotqa.py`

**Lines:** 236  

### Imports
- `import os`
- `import re`
- `from base import Task`
- `from hotpot import *`
- `from models import gpt`
- `import logging`
- `from transformers import GPT2Tokenizer`
- `import random`

### Module assignments
- L10: `tokenizer = GPT2Tokenizer.from_pretrained("gpt2")`
- L15: `max_token_length = 4000`

### Prompt-like assignments
- L71 `failed_trajectories`: `failed_trajectories = "\n".join([f"{question}\n{traj}\n" for traj in z])`
- L72 `failed_trajectories`: `failed_trajectories = [f"Question: {traj}" for traj in failed_trajectories.split("Question: ")[1:]]`
- L158 `prompt`: `prompt = compare_prompt + f'Action 1:{last_actions[0]}\n\nAction 2:{last_actions[1]}\n'`
- L77 `reflect_prompt`: `reflect_prompt = reflection_prompt.format(trajectory=traj)`
- L102 `prompt`: `prompt = cot_prompt_feedback.format(trajectories=trajectories, input=input)`
- L187 `prompt`: `prompt = value_prompt_reasoning_feedback.format(s="", trajectories=failed_trajectories, input=inp)`
- L192 `failed_trajectories`: `failed_trajectories = "\n".join([f"{question}\n{traj}\nThus the correctness score is 1\n" for traj in z])`
- L194 `prompt`: `prompt = value_prompt_feedback.format(s="", trajectories=failed_trajectories, input=inp)`
- L205 `prompt`: `prompt = value_prompt_reasoning.format(s="", input=inp)`
- L99 `traj_with_reflection`: `traj_with_reflection = reflection_mapping['trajectory'] + "FAILED TRAJECTORY\nReflection: " + reflection_mapping['reflection'] + "\n\n"`
- L109 `prompt`: `prompt = cot_prompt_feedback_short.format(trajectories=trajectories, input=input)`
- L190 `prompt`: `prompt = value_prompt_reasoning_feedback_short.format(s="", trajectories=failed_trajectories, input=inp)`
- L197 `failed_trajectories`: `failed_trajectories = "\n".join([f"{question}\n{traj}\nThus the correctness score is 1\n" for traj in z[:2]])`
- L199 `prompt`: `prompt = value_prompt_feedback.format(s="", trajectories=failed_trajectories, input=inp)`
- L107 `traj_with_reflection`: `traj_with_reflection = reflection_mapping['trajectory'] + "FAILED TRAJECTORY\nReflection: " + reflection_mapping['reflection'] + "\n\n"`

### Classes
#### Class `HotPotQATask` L19 bases=['Task']
- Docstring: Input (x)   : a text instruction
Output (y)  : a text generation
Reward (r)  : # TODO
Input Example: 
Output Example: 
##### `__init__(self)` (L27)
- Docstring: file: a text file, each line is some sentences
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `super`
##### `__len__(self)` (L36)
- Inputs: parameters `__len__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L37: `len(self.data)`
- Main call graph hints: `len`
##### `get_input(self, idx)` (L39)
- Inputs: parameters `get_input(self, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L40: `self.data[idx]`
##### `test_output(self, idx, output)` (L42)
- Inputs: parameters `test_output(self, idx, output)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L59: `info`
- Loops:
  - L47: {'line': 47, 'type': 'for', 'target': 'score_output', 'iter': 'score_outputs', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L51: IF `match`; body=2 else=1
- LLM/model/env calls:
  - L45: `gpt`
- Main call graph hints: `gpt`, `print`, `output.split`, `re.match`, `int`, `scores.append`, `sum`, `len`, `match.groups`
##### `standard_prompt_wrap(x, y)` (L62)
- Inputs: parameters `standard_prompt_wrap(x, y)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L63: `standard_prompt.format(input=x) + y`
- Main call graph hints: `standard_prompt.format`
##### `generate_self_reflection(z, question)` (L66)
- Inputs: parameters `generate_self_reflection(z, question)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L89: `reflection_mapping`
- Loops:
  - L74: {'line': 74, 'type': 'for', 'target': 'traj', 'iter': 'failed_trajectories', 'body_len': 5, 'orelse_len': 0}
- LLM/model/env calls:
  - L79: `gpt`
- Main call graph hints: `random.sample`, `Constant.join`, `min`, `reflection_prompt.format`, `gpt`, `reflection_mapping.append`, `len`, `failed_trajectories.split`
##### `cot_prompt_wrap(x, y, reflection_mapping_list)` (L92)
- Inputs: parameters `cot_prompt_wrap(x, y, reflection_mapping_list)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L111: `prompt`
  - L116: `prompt`
- Loops:
  - L98: {'line': 98, 'type': 'for', 'target': 'reflection_mapping', 'iter': 'reflection_mapping_list', 'body_len': 2, 'orelse_len': 0}
  - L106: {'line': 106, 'type': 'for', 'target': 'reflection_mapping', 'iter': 'reflection_mapping_list[:3]', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L97: IF `reflection_mapping_list`; body=4 else=3
  - L103: IF `get_token_length(prompt) > max_token_length`; body=4 else=0
  - L114: IF `get_token_length(prompt) > max_token_length`; body=1 else=0
- Main call graph hints: `cot_prompt_feedback.format`, `cot_prompt.format`, `get_token_length`, `print`, `cot_prompt_feedback_short.format`, `cot_prompt_short.format`
##### `vote_prompt_wrap(x, ys)` (L118)
- Inputs: parameters `vote_prompt_wrap(x, ys)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L124: `prompt`
- Loops:
  - L120: {'line': 120, 'type': 'for', 'target': '(i, y)', 'iter': 'enumerate(ys, 1)', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `enumerate`
##### `vote_outputs_unwrap(vote_outputs, n_candidates)` (L127)
- Inputs: parameters `vote_outputs_unwrap(vote_outputs, n_candidates)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L138: `vote_results`
- Loops:
  - L129: {'line': 129, 'type': 'for', 'target': 'vote_output', 'iter': 'vote_outputs', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L132: IF `match`; body=2 else=1
  - L134: IF `vote in range(n_candidates)`; body=1 else=0
- Main call graph hints: `re.match`, `print`, `int`, `range`, `match.groups`
##### `compare_prompt_wrap(x, ys)` (L141)
- Inputs: parameters `compare_prompt_wrap(x, ys)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L159: `prompt`
- Loops:
  - L146: {'line': 146, 'type': 'for', 'target': 'y', 'iter': 'ys', 'body_len': 2, 'orelse_len': 0}
  - L149: {'line': 149, 'type': 'for', 'target': 'line', 'iter': 'lines', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L151: IF `'Action' in line`; body=2 else=0
- Main call graph hints: `len`, `y.split`, `last_actions.append`, `line.split[...].strip`, `line.split`
##### `compare_output_unwrap(compare_output)` (L163)
- Inputs: parameters `compare_output_unwrap(compare_output)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L165: `0`
  - L167: `1`
  - L169: `0.5`
  - L172: `-1`
- Decisions / conditions:
  - L164: IF `'more correct trajectory is 1' in compare_output`; body=1 else=1
  - L166: IF `'more correct trajectory is 2' in compare_output`; body=1 else=1
  - L168: IF `'two trajectories are similarly correct' in compare_output`; body=1 else=2
- Main call graph hints: `print`
##### `value_prompt_wrap(x, y, z, reflections)` (L175)
- Inputs: parameters `value_prompt_wrap(x, y, z, reflections)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L207: `prompt`
- Loops:
  - L182: {'line': 182, 'type': 'for', 'target': '(traj, ref)', 'iter': 'zip(z, reflections)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L178: IF `len(z) != 0`; body=5 else=0
  - L191: IF `len(z) != 0 and False`; body=4 else=2
  - L189: IF `get_token_length(prompt) > max_token_length`; body=1 else=0
  - L195: IF `get_token_length(prompt) > max_token_length`; body=5 else=0
- Main call graph hints: `x.split`, `len`, `zip`, `value_prompt_reasoning_feedback.format`, `Constant.join`, `value_prompt_feedback.format`, `value_prompt_reasoning.format`, `get_token_length`, `value_prompt_reasoning_feedback_short.format`, `print`
##### `value_outputs_unwrap(evaluate_prompt)` (L211)
- Inputs: parameters `value_outputs_unwrap(evaluate_prompt)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L214: `1.0`
  - L216: `0.9`
  - L218: `0.8`
  - L220: `0.7`
  - L222: `0.6`
  - L224: `0.5`
  - L226: `0.4`
  - L228: `0.3`
  - L230: `0.2`
  - L232: `0.1`
  - L234: `-1`
- Decisions / conditions:
  - L213: IF `'10' in evaluate_prompt`; body=1 else=1
  - L215: IF `'9' in evaluate_prompt`; body=1 else=1
  - L217: IF `'8' in evaluate_prompt`; body=1 else=1
  - L219: IF `'7' in evaluate_prompt`; body=1 else=1
  - L221: IF `'6' in evaluate_prompt`; body=1 else=1
  - L223: IF `'5' in evaluate_prompt`; body=1 else=1
  - L225: IF `'4' in evaluate_prompt`; body=1 else=1
  - L227: IF `'3' in evaluate_prompt`; body=1 else=1
  - L229: IF `'2' in evaluate_prompt`; body=1 else=1
  - L231: IF `'1' in evaluate_prompt`; body=1 else=1

### Functions
#### `get_token_length(text)` (L12)
- Inputs: parameters `get_token_length(text)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L13: `len(tokenizer.encode(text))`
- Main call graph hints: `len`, `tokenizer.encode`

---

## File: `hotpot/lats.py`

**Lines:** 415  

### Imports
- `import itertools`
- `import numpy as np`
- `from functools import partial`
- `from models import gpt`
- `import wikienv, wrappers`
- `import requests`
- `import logging`
- `import random`

### Module assignments
- L10: `env = wikienv.WikiEnv()`
- L11: `env = wrappers.HotPotQAWrapper(env, split="train")`
- L12: `env = wrappers.LoggingWrapper(env)`
- L16: `reflection_map = []`
- L17: `failed_trajectories = []`

### Prompt-like assignments
- L32 `value_prompt`: `value_prompt = task.value_prompt_wrap(x, y, unique_trajectories, reflection_map)`
- L38 `value_outputs`: `value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)`
- L72 `samples`: `samples = gpt(prompt, n=n_generate_sample, stop=stop)`
- L305 `sampled_actions`: `sampled_actions = get_samples(task, prompt, f"Thought {node.depth + 1}: ", n, prompt_sample=args.prompt_sample, stop="Observation")`
- L355 `child_prompts`: `child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]`
- L356 `votes`: `votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)`
- L362 `votes`: `votes = votes + [0] * (len(node.children) - len(votes))`
- L64 `reflection_map`: `reflection_map = task.generate_self_reflection(unique_trajectories, x)`
- L89 `state`: `self.state = {'thought': '', 'action': '', 'observation': ''} if state is None else state`
- L199 ``: `reward, terminal_node = rollout(max(node.children, key=lambda child: child.value), args, task, idx, max_depth=4)`
- L208 `all_nodes`: `all_nodes = [(node, node.value) for node in collect_all_nodes(root)]`
- L288 `child_prompts`: `child_prompts = [generate_prompt(child) for child in new_states if not child.is_terminal and child is not None]`
- L313 `thought_line`: `thought_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith(f"Thought {node.depth + 1}")), '')`
- L314 `action_line`: `action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)`
- L53 `value`: `value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)`
- L68 `prompt`: `prompt = task.cot_prompt_wrap(x, y, reflection_map)`
- L129 `thought`: `thought = line.split(", thought=")[1].split(", action=")[0].strip()`
- L130 `action`: `action = line.split(", action=")[1].split(", observation=")[0].strip()`
- L131 `observation`: `observation = line.split(", observation=")[1].split(")")[0].strip()`
- L214 `best_node`: `best_node = max(terminal_nodes_with_reward_1, key=lambda x: x.value)`
- L291 `values`: `values = get_values(task, node.question, child_prompts, args.n_evaluate_sample)`
- L325 `action_type`: `action_type = action_line.split('[')[0] if '[' in action_line else action_line`
- L326 `action_param`: `action_param = action_line.split('[')[1].split(']')[0] if '[' in action_line else ""`
- L328 ``: `obs, r, done, info = step(env, f"{action_type.lower()}[{action_param}]")`
- L335 `new_node`: `new_node = Node(state=new_state, question=node.question, parent=node)`
- L397 `value`: `node.value = (node.value * (node.visits - 1) + value) / node.visits`
- L391 `value`: `node.value = (node.value * (node.visits - 1) + (-1)) / node.visits`
- L394 `value`: `node.value = (node.value * (node.visits - 1) + value) / node.visits`

### Classes
#### Class `Node` L87 bases=[]
##### `__init__(self, state, question, parent)` (L88)
- Inputs: parameters `__init__(self, state, question, parent)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `uct(self)` (L101)
- Inputs: parameters `uct(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L104: `self.value / self.visits + np.sqrt(2 * np.log(self.parent.visits) / self.visits)`
  - L103: `self.value`
- Decisions / conditions:
  - L102: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `np.sqrt`, `np.log`
##### `__str__(self)` (L106)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L107: `f"Node(depth={self.depth}, value={self.value:.2f}, visits={self.visits}, thought={self.state['thought']}, action={self.state['action']}, observation={self.state['observation']})"`
##### `to_dict(self)` (L109)
- Inputs: parameters `to_dict(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L110: `{'state': self.state, 'question': self.question, 'parent': self.parent.to_dict() if self.parent else None, 'children': [child.to_dict() for child in self.children], 'visits': self.visits, 'value': self.value, 'depth': self.depth, 'is_terminal': self.is_terminal, 'reward': self.reward, 'em': self.em}`
- Main call graph hints: `self.parent.to_dict`, `child.to_dict`

### Functions
#### `step(env, action)` (L19)
- Inputs: parameters `step(env, action)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L23: `env.step(action)`
- Loops:
  - L21: {'line': 21, 'type': 'while', 'test': 'attempts < 10', 'body_len': 1, 'orelse_len': 0}
- Exception handling:
  - L22: handlers=['requests.exceptions.Timeout'] final=0
- I/O/env/executor calls:
  - L23: `env.step`
- Main call graph hints: `env.step`
#### `get_value(task, x, y, n_evaluate_sample, cache_value)` (L27)
- Inputs: parameters `get_value(task, x, y, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L44: `value`
  - L36: `task.value_cache[value_prompt]`
- Decisions / conditions:
  - L35: IF `cache_value and value_prompt in task.value_cache`; body=1 else=0
  - L42: IF `cache_value`; body=1 else=0
- LLM/model/env calls:
  - L38: `gpt`
- Main call graph hints: `get_unique_trajectories`, `task.value_prompt_wrap`, `logging.info`, `gpt`, `task.value_outputs_unwrap`
#### `get_values(task, x, ys, n_evaluate_sample, cache_value)` (L46)
- Inputs: parameters `get_values(task, x, ys, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L56: `values`
- Loops:
  - L49: {'line': 49, 'type': 'for', 'target': 'y', 'iter': 'ys', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L50: IF `y in local_value_cache`; body=1 else=2
- Main call graph hints: `values.append`, `get_value`
#### `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` (L58)
- Inputs: parameters `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L73: `[y + _ for _ in samples]`
- Decisions / conditions:
  - L62: IF `len(unique_trajectories) > len(reflection_map) and len(unique_trajectories) < 4`; body=2 else=0
  - L65: IF `prompt_sample == 'standard'`; body=1 else=1
  - L67: IF `prompt_sample == 'cot'`; body=1 else=1
- LLM/model/env calls:
  - L72: `gpt`
  - L64: `task.generate_self_reflection`
- Main call graph hints: `get_unique_trajectories`, `logging.info`, `gpt`, `print`, `task.generate_self_reflection`, `task.standard_prompt_wrap`, `len`, `task.cot_prompt_wrap`, `ValueError`
#### `get_unique_trajectories(failed_trajectories, num)` (L75)
- Inputs: parameters `get_unique_trajectories(failed_trajectories, num)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L85: `unique_trajectories`
- Loops:
  - L78: {'line': 78, 'type': 'for', 'target': 'traj', 'iter': 'failed_trajectories', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L80: IF `final_answer not in seen_final_answers`; body=2 else=0
  - L83: IF `len(unique_trajectories) >= num`; body=1 else=0
- Main call graph hints: `set`, `traj.get`, `unique_trajectories.append`, `seen_final_answers.add`, `len`, `node_trajectory_to_text`
#### `node_trajectory_to_text(node_string)` (L123)
- Inputs: parameters `node_trajectory_to_text(node_string)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L143: `'\n'.join(formatted_lines)`
- Loops:
  - L126: {'line': 126, 'type': 'for', 'target': 'line', 'iter': 'lines', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L135: IF `depth != 0`; body=3 else=0
  - L136: IF `thought`; body=1 else=0
  - L138: IF `action`; body=1 else=0
  - L140: IF `observation`; body=1 else=0
- Exception handling:
  - L127: handlers=['IndexError'] final=0
- Main call graph hints: `node_string.split`, `Constant.join`, `int`, `line.split[...].split[...].strip`, `formatted_lines.append`, `line.split[...].split`, `line.split`
#### `collect_all_nodes(node)` (L145)
- Docstring: Recursively collect all nodes starting from the given node.
- Inputs: parameters `collect_all_nodes(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L150: `nodes`
- Loops:
  - L148: {'line': 148, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `nodes.extend`, `collect_all_nodes`
#### `collect_trajectory(node)` (L152)
- Inputs: parameters `collect_trajectory(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L157: `'\n'.join(reversed(trajectory))`
- Loops:
  - L154: {'line': 154, 'type': 'while', 'test': 'node', 'body_len': 2, 'orelse_len': 0}
- Main call graph hints: `Constant.join`, `trajectory.append`, `reversed`, `str`
#### `lats_search(args, task, idx, iterations, to_print)` (L159)
- Inputs: parameters `lats_search(args, task, idx, iterations, to_print)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L232: `(best_child.state, best_child.value, all_nodes, best_child.reward, best_child.em)`
  - L188: `(node.state, node.value, all_nodes, node.reward, node.em)`
  - L205: `(terminal_node.state, terminal_node.value, [], terminal_node.reward, terminal_node.em)`
  - L215: `(best_node.state, best_node.value, all_nodes, best_node.reward, best_node.em)`
- Loops:
  - L174: {'line': 174, 'type': 'for', 'target': 'i', 'iter': 'range(iterations)', 'body_len': 17, 'orelse_len': 0}
  - L178: {'line': 178, 'type': 'while', 'test': 'node is None or (node.is_terminal and node.reward != 1)', 'body_len': 2, 'orelse_len': 0}
  - L192: {'line': 192, 'type': 'while', 'test': 'node.is_terminal or not node.children', 'body_len': 3, 'orelse_len': 0}
  - L217: {'line': 217, 'type': 'for', 'target': '(j, (node, value))', 'iter': 'enumerate(all_nodes)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L165: IF `to_print`; body=1 else=0
  - L226: IF `best_child.reward == 1`; body=1 else=1
  - L230: IF `best_child is None`; body=1 else=0
  - L182: IF `node is None`; body=2 else=0
  - L186: IF `node.is_terminal and node.reward == 1`; body=2 else=0
  - L203: IF `terminal_node.reward == 1`; body=2 else=0
  - L212: IF `terminal_nodes_with_reward_1`; body=3 else=0
- I/O/env/executor calls:
  - L197: `evaluate_node`
- Main call graph hints: `partial`, `env.reset`, `Node`, `logging.basicConfig`, `range`, `collect_all_nodes`, `all_nodes_list.extend`, `max`, `print`, `logging.info`, `select_node`, `expand_node`, `evaluate_node`, `rollout`, `terminal_nodes.append`, `backpropagate`, `enumerate`, `str`
#### `select_node(node)` (L234)
- Inputs: parameters `select_node(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L260: `node`
  - L251: `node_with_reward_1`
- Loops:
  - L235: {'line': 235, 'type': 'while', 'test': 'node and node.children', 'body_len': 9, 'orelse_len': 0}
  - L255: {'line': 255, 'type': 'while', 'test': 'node.is_terminal and node.reward != 1', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L241: IF `len(terminal_children) == len(node.children)`; body=4 else=0
  - L249: IF `node_with_reward_1`; body=2 else=0
  - L243: IF `node.parent`; body=1 else=0
- Main call graph hints: `logging.info`, `next`, `max`, `len`, `node.parent.children.remove`, `child.uct`, `node.uct`
#### `expand_node(node, args, task)` (L262)
- Inputs: parameters `expand_node(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L267: `None`
- Decisions / conditions:
  - L263: IF `node.depth >= 7`; body=4 else=0
- LLM/model/env calls:
  - L268: `generate_new_states`
- Main call graph hints: `generate_new_states`, `node.children.extend`, `logging.info`, `print`
#### `rollout(node, args, task, idx, max_depth)` (L271)
- Inputs: parameters `rollout(node, args, task, idx, max_depth)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L300: `(sum(rewards) / len(rewards), node)`
  - L286: `(state.reward, state)`
- Loops:
  - L276: {'line': 276, 'type': 'while', 'test': 'not node.is_terminal and depth < max_depth', 'body_len': 12, 'orelse_len': 0}
  - L281: {'line': 281, 'type': 'while', 'test': 'len(new_states) == 0', 'body_len': 1, 'orelse_len': 0}
  - L284: {'line': 284, 'type': 'for', 'target': 'state', 'iter': 'new_states', 'body_len': 1, 'orelse_len': 0}
  - L290: {'line': 290, 'type': 'while', 'test': 'len(values) == 0', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L296: IF `depth == max_depth`; body=1 else=0
  - L285: IF `state.is_terminal`; body=1 else=0
- LLM/model/env calls:
  - L282: `generate_new_states`
  - L288: `generate_prompt`
- Main call graph hints: `logging.info`, `values.index`, `rewards.append`, `len`, `generate_new_states`, `generate_prompt`, `get_values`, `max`, `sum`
#### `generate_new_states(node, args, task, n)` (L302)
- Inputs: parameters `generate_new_states(node, args, task, n)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L351: `list(unique_states.values())`
- Loops:
  - L310: {'line': 310, 'type': 'for', 'target': 'action', 'iter': 'sampled_actions', 'body_len': 7, 'orelse_len': 0}
- Decisions / conditions:
  - L319: IF `unique_key in unique_states`; body=1 else=0
  - L324: IF `action_line`; body=15 else=0
  - L339: IF `r == 1`; body=1 else=0
  - L345: IF `new_node.is_terminal and r == 0`; body=2 else=0
- LLM/model/env calls:
  - L304: `generate_prompt`
- I/O/env/executor calls:
  - L328: `step`
- Main call graph hints: `generate_prompt`, `get_samples`, `logging.info`, `list`, `node.state.copy`, `next`, `tried_actions.append`, `unique_states.values`, `step`, `Node`, `line.split[...].strip`, `info.get`, `collect_trajectory`, `failed_trajectories.append`, `action.split`, `line.startswith`, `action_line.split`, `action_line.split[...].split`, `action_type.lower`, `line.split`
#### `evaluate_node(node, args, task)` (L354)
- Inputs: parameters `evaluate_node(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L377: `sum(votes) / len(votes) if votes else 0`
- Loops:
  - L363: {'line': 363, 'type': 'for', 'target': '(i, child)', 'iter': 'enumerate(node.children)', 'body_len': 1, 'orelse_len': 0}
- LLM/model/env calls:
  - L355: `generate_prompt`
- Main call graph hints: `get_values`, `logging.info`, `enumerate`, `generate_prompt`, `sum`, `len`
#### `print_tree(node, level)` (L380)
- Inputs: parameters `print_tree(node, level)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L383: {'line': 383, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `print`, `print_tree`
#### `backpropagate(node, value)` (L386)
- Inputs: parameters `backpropagate(node, value)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L387: {'line': 387, 'type': 'while', 'test': 'node', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L389: IF `node.is_terminal`; body=1 else=2
  - L390: IF `node.reward == 0`; body=2 else=2
- Main call graph hints: `logging.info`
#### `generate_prompt(node)` (L402)
- Inputs: parameters `generate_prompt(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L415: `question + '\n'.join(reversed(trajectory))`
- Loops:
  - L405: {'line': 405, 'type': 'while', 'test': 'node', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L407: IF `node.state['thought']`; body=1 else=0
  - L409: IF `node.state['action']`; body=1 else=0
  - L411: IF `node.state['observation'] and node.depth != 0`; body=1 else=0
- Main call graph hints: `trajectory.append`, `Constant.join`, `new_segment.append`, `reversed`

---

## File: `hotpot/models.py`

**Lines:** 65  

### Imports
- `import os`
- `import openai`
- `import backoff`
- `from transformers import GPT2Tokenizer`
- `import warnings`

### Module assignments
- L7: `completion_tokens = prompt_tokens = 0`
- L8: `MAX_TOKENS = 4000`
- L9: `tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')`
- L24: `api_key = os.getenv("OPENAI_API_KEY", "")`
- L30: `api_base = os.getenv("OPENAI_API_BASE", "")`

### Prompt-like assignments
- L59 `cost`: `cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03`
- L61 `cost`: `cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.0015`
- L63 `cost`: `cost = completion_tokens / 1000 * 0.004 + prompt_tokens / 1000 * 0.003`

### Top-level logic
- L25 If: `if api_key != "": openai.api_key = api_key else: print("Warning: OPENAI_API_KEY is not set")`
- L31 If: `if api_base != "": print("Warning: OPENAI_API_BASE is set to {}".format(api_base)) openai.api_base = api_base`

### Classes
- None

### Functions
#### `tokens_in_text(text)` (L11)
- Docstring: Accurately count the number of tokens in a string using the GPT-2 tokenizer.

:param text: The input text.
:return: The exact number of tokens in the text.
- Inputs: parameters `tokens_in_text(text)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L22: `len(tokens)`
- LLM/model/env calls:
  - L20: `GPT2Tokenizer.from_pretrained`
- Main call graph hints: `len`, `warnings.catch_warnings`, `warnings.filterwarnings`, `GPT2Tokenizer.from_pretrained`, `tokenizer.encode`
#### `completions_with_backoff(**kwargs)` (L36)
- Inputs: parameters `completions_with_backoff(**kwargs)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L37: `openai.ChatCompletion.create(**kwargs)`
- LLM/model/env calls:
  - L37: `openai.ChatCompletion.create`
- I/O/env/executor calls:
  - L37: `openai.ChatCompletion.create`
- Main call graph hints: `backoff.on_exception`, `openai.ChatCompletion.create`
#### `gpt(prompt, model, temperature, max_tokens, n, stop)` (L39)
- Inputs: parameters `gpt(prompt, model, temperature, max_tokens, n, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L41: `chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)`
- LLM/model/env calls:
  - L41: `chatgpt`
- Main call graph hints: `chatgpt`
#### `chatgpt(messages, model, temperature, max_tokens, n, stop)` (L43)
- Inputs: parameters `chatgpt(messages, model, temperature, max_tokens, n, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L54: `outputs`
- Loops:
  - L46: {'line': 46, 'type': 'while', 'test': 'n > 0', 'body_len': 6, 'orelse_len': 0}
- LLM/model/env calls:
  - L49: `completions_with_backoff`
- Main call graph hints: `min`, `completions_with_backoff`, `outputs.extend`
#### `gpt_usage(backend)` (L56)
- Inputs: parameters `gpt_usage(backend)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L64: `{'completion_tokens': completion_tokens, 'prompt_tokens': prompt_tokens, 'cost': cost}`
- Decisions / conditions:
  - L58: IF `backend == 'gpt-4'`; body=1 else=1
  - L60: IF `backend == 'gpt-3.5-turbo'`; body=1 else=1
  - L62: IF `backend == 'gpt-3.5-turbo-16k'`; body=1 else=0

---

## File: `hotpot/rap.py`

**Lines:** 353  

### Imports
- `import itertools`
- `import numpy as np`
- `from functools import partial`
- `from models import gpt`
- `import wikienv, wrappers`
- `import requests`
- `import logging`

### Module assignments
- L15: `reflection_map = []`

### Prompt-like assignments
- L20 `value_prompt`: `value_prompt = task.value_prompt_wrap(x, y, unique_trajectories, reflection_map)`
- L26 `value_outputs`: `value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)`
- L57 `samples`: `samples = gpt(prompt, n=n_generate_sample, stop=stop)`
- L250 `sampled_actions`: `sampled_actions = get_samples(task, prompt, f"Thought {node.depth + 1}: ", args.n_generate_sample, prompt_sample=args.prompt_sample, stop="Observation")`
- L294 `child_prompts`: `child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]`
- L295 `votes`: `votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)`
- L301 `votes`: `votes = votes + [0] * (len(node.children) - len(votes))`
- L74 `state`: `self.state = {'thought': '', 'action': '', 'observation': ''} if state is None else state`
- L189 `all_nodes`: `all_nodes = [(node, node.value) for node in collect_all_nodes(root)]`
- L257 `thought_line`: `thought_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith(f"Thought {node.depth + 1}")), '')`
- L258 `action_line`: `action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)`
- L41 `value`: `value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)`
- L53 ``: `prompt, reflection_map = task.cot_prompt_wrap(x, y, unique_trajectories)`
- L123 `thought`: `thought = line.split(", thought=")[1].split(", action=")[0].strip()`
- L124 `action`: `action = line.split(", action=")[1].split(", observation=")[0].strip()`
- L125 `observation`: `observation = line.split(", observation=")[1].split(")")[0].strip()`
- L195 `best_node`: `best_node = max(terminal_nodes_with_reward_1, key=lambda x: x.value)`
- L268 `action_type`: `action_type = action_line.split('[')[0] if '[' in action_line else action_line`
- L269 `action_param`: `action_param = action_line.split('[')[1].split(']')[0] if '[' in action_line else ""`
- L270 ``: `obs, r, done, info = step(env, f"{action_type.lower()}[{action_param}]")`
- L277 `new_node`: `new_node = Node(state=new_state, question=node.question, parent=node)`
- L335 `value`: `node.value = (node.value * (node.visits - 1) + value) / node.visits`
- L329 `value`: `node.value = (node.value * (node.visits - 1) + value) / node.visits`
- L332 `value`: `node.value = (node.value * (node.visits - 1) + (-1)) / node.visits`

### Classes
#### Class `Node` L72 bases=[]
##### `__init__(self, state, question, parent)` (L73)
- Inputs: parameters `__init__(self, state, question, parent)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `uct(self)` (L86)
- Inputs: parameters `uct(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L90: `self.value / self.visits + np.sqrt(2 * np.log(self.parent.visits) / self.visits)`
  - L89: `self.value * 2`
- Decisions / conditions:
  - L87: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `np.sqrt`, `np.log`
##### `uct_with_depth(self, C1, C2)` (L92)
- Inputs: parameters `uct_with_depth(self, C1, C2)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L98: `exploitation_term + C1 * exploration_term + C2 * depth_term`
  - L94: `self.value`
- Decisions / conditions:
  - L93: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `np.sqrt`, `np.log`
##### `__str__(self)` (L100)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L101: `f"Node(depth={self.depth}, value={self.value:.2f}, visits={self.visits}, thought={self.state['thought']}, action={self.state['action']}, observation={self.state['observation']})"`
##### `to_dict(self)` (L103)
- Inputs: parameters `to_dict(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L104: `{'state': self.state, 'question': self.question, 'parent': self.parent.to_dict() if self.parent else None, 'children': [child.to_dict() for child in self.children], 'visits': self.visits, 'value': self.value, 'depth': self.depth, 'is_terminal': self.is_terminal, 'reward': self.reward, 'em': self.em}`
- Main call graph hints: `self.parent.to_dict`, `child.to_dict`

### Functions
#### `get_value(task, x, y, n_evaluate_sample, cache_value)` (L17)
- Inputs: parameters `get_value(task, x, y, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L32: `value`
  - L24: `task.value_cache[value_prompt]`
- Decisions / conditions:
  - L23: IF `cache_value and value_prompt in task.value_cache`; body=1 else=0
  - L30: IF `cache_value`; body=1 else=0
- LLM/model/env calls:
  - L26: `gpt`
- Main call graph hints: `get_unique_trajectories`, `task.value_prompt_wrap`, `logging.info`, `gpt`, `task.value_outputs_unwrap`
#### `get_values(task, x, ys, n_evaluate_sample, cache_value)` (L34)
- Inputs: parameters `get_values(task, x, ys, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L44: `values`
- Loops:
  - L37: {'line': 37, 'type': 'for', 'target': 'y', 'iter': 'ys', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L38: IF `y in local_value_cache`; body=1 else=2
- Main call graph hints: `values.append`, `get_value`
#### `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` (L46)
- Inputs: parameters `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L58: `[y + _ for _ in samples]`
- Decisions / conditions:
  - L50: IF `prompt_sample == 'standard'`; body=1 else=1
  - L52: IF `prompt_sample == 'cot'`; body=1 else=1
- LLM/model/env calls:
  - L57: `gpt`
- Main call graph hints: `get_unique_trajectories`, `logging.info`, `gpt`, `task.standard_prompt_wrap`, `task.cot_prompt_wrap`, `ValueError`
#### `get_unique_trajectories(failed_trajectories, num)` (L60)
- Inputs: parameters `get_unique_trajectories(failed_trajectories, num)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L70: `unique_trajectories`
- Loops:
  - L63: {'line': 63, 'type': 'for', 'target': 'traj', 'iter': 'failed_trajectories', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L65: IF `final_answer not in seen_final_answers`; body=2 else=0
  - L68: IF `len(unique_trajectories) >= num`; body=1 else=0
- Main call graph hints: `set`, `traj.get`, `unique_trajectories.append`, `seen_final_answers.add`, `len`, `node_trajectory_to_text`
#### `node_trajectory_to_text(node_string)` (L117)
- Inputs: parameters `node_trajectory_to_text(node_string)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L137: `'\n'.join(formatted_lines)`
- Loops:
  - L120: {'line': 120, 'type': 'for', 'target': 'line', 'iter': 'lines', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L129: IF `depth != 0`; body=3 else=0
  - L130: IF `thought`; body=1 else=0
  - L132: IF `action`; body=1 else=0
  - L134: IF `observation`; body=1 else=0
- Exception handling:
  - L121: handlers=['IndexError'] final=0
- Main call graph hints: `node_string.split`, `Constant.join`, `int`, `line.split[...].split[...].strip`, `formatted_lines.append`, `line.split[...].split`, `line.split`
#### `collect_all_nodes(node)` (L139)
- Docstring: Recursively collect all nodes starting from the given node.
- Inputs: parameters `collect_all_nodes(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L144: `nodes`
- Loops:
  - L142: {'line': 142, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `nodes.extend`, `collect_all_nodes`
#### `collect_trajectory(node)` (L146)
- Inputs: parameters `collect_trajectory(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L151: `'\n'.join(reversed(trajectory))`
- Loops:
  - L148: {'line': 148, 'type': 'while', 'test': 'node', 'body_len': 2, 'orelse_len': 0}
- Main call graph hints: `Constant.join`, `trajectory.append`, `reversed`, `str`
#### `mcts_search(args, task, idx, iterations, to_print)` (L153)
- Inputs: parameters `mcts_search(args, task, idx, iterations, to_print)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L209: `(best_child.state, best_child.value, all_nodes, best_child.reward, best_child.em)`
  - L178: `(node.state, node.value, all_nodes, node.reward, node.em)`
  - L196: `(best_node.state, best_node.value, all_nodes, best_node.reward, best_node.em)`
- Loops:
  - L164: {'line': 164, 'type': 'for', 'target': 'i', 'iter': 'range(iterations)', 'body_len': 14, 'orelse_len': 0}
  - L168: {'line': 168, 'type': 'while', 'test': 'node is None or (node.is_terminal and node.reward != 1)', 'body_len': 2, 'orelse_len': 0}
  - L182: {'line': 182, 'type': 'while', 'test': 'node.is_terminal', 'body_len': 3, 'orelse_len': 0}
  - L198: {'line': 198, 'type': 'for', 'target': '(j, (node, value))', 'iter': 'enumerate(all_nodes)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L158: IF `to_print`; body=1 else=0
  - L205: IF `best_child.reward == 1`; body=1 else=1
  - L172: IF `node is None`; body=2 else=0
  - L176: IF `node.is_terminal and node.reward == 1`; body=2 else=0
  - L193: IF `terminal_nodes_with_reward_1`; body=3 else=0
- I/O/env/executor calls:
  - L187: `evaluate_node`
- Main call graph hints: `partial`, `env.reset`, `Node`, `range`, `max`, `print`, `logging.info`, `select_node`, `expand_node`, `evaluate_node`, `backpropagate`, `enumerate`, `collect_all_nodes`, `str`
#### `select_node(node)` (L211)
- Inputs: parameters `select_node(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L237: `node`
  - L228: `node_with_reward_1`
- Loops:
  - L212: {'line': 212, 'type': 'while', 'test': 'node and node.children', 'body_len': 9, 'orelse_len': 0}
  - L232: {'line': 232, 'type': 'while', 'test': 'node.is_terminal and node.reward != 1', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L218: IF `len(terminal_children) == len(node.children)`; body=4 else=0
  - L226: IF `node_with_reward_1`; body=2 else=0
  - L220: IF `node.parent`; body=1 else=0
- Main call graph hints: `logging.info`, `next`, `max`, `len`, `node.parent.children.remove`, `child.uct`, `node.uct`
#### `expand_node(node, args, task)` (L239)
- Inputs: parameters `expand_node(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L244: `None`
- Decisions / conditions:
  - L240: IF `node.depth >= 7`; body=4 else=0
- LLM/model/env calls:
  - L245: `generate_new_states`
- Main call graph hints: `generate_new_states`, `node.children.extend`, `logging.info`, `print`
#### `generate_new_states(node, args, task)` (L248)
- Inputs: parameters `generate_new_states(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L290: `list(unique_states.values())`
- Loops:
  - L254: {'line': 254, 'type': 'for', 'target': 'action', 'iter': 'sampled_actions', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L264: IF `unique_key in unique_states`; body=1 else=0
  - L267: IF `action_line`; body=14 else=0
  - L280: IF `r == 1`; body=1 else=0
  - L286: IF `new_node.is_terminal and r == 0`; body=2 else=0
- LLM/model/env calls:
  - L249: `generate_prompt`
- I/O/env/executor calls:
  - L270: `step`
- Main call graph hints: `generate_prompt`, `get_samples`, `logging.info`, `list`, `node.state.copy`, `next`, `unique_states.values`, `step`, `Node`, `line.split[...].strip`, `info.get`, `collect_trajectory`, `failed_trajectories.append`, `action.split`, `line.startswith`, `action_line.split`, `action_line.split[...].split`, `action_type.lower`, `line.split`
#### `evaluate_node(node, args, task)` (L293)
- Inputs: parameters `evaluate_node(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L315: `sum(votes) / len(votes) if votes else 0`
- Loops:
  - L308: {'line': 308, 'type': 'for', 'target': '(i, condition)', 'iter': 'enumerate(terminal_conditions)', 'body_len': 1, 'orelse_len': 0}
  - L312: {'line': 312, 'type': 'for', 'target': '(i, child)', 'iter': 'enumerate(node.children)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L304: IF `max_vote == 0`; body=1 else=0
  - L309: IF `condition == 1`; body=1 else=0
- LLM/model/env calls:
  - L294: `generate_prompt`
- Main call graph hints: `get_values`, `logging.info`, `enumerate`, `generate_prompt`, `max`, `sum`, `len`
#### `print_tree(node, level)` (L318)
- Inputs: parameters `print_tree(node, level)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L321: {'line': 321, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `print`, `print_tree`
#### `backpropagate(node, value)` (L324)
- Inputs: parameters `backpropagate(node, value)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L325: {'line': 325, 'type': 'while', 'test': 'node', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L327: IF `node.is_terminal`; body=1 else=2
  - L328: IF `node.reward == 1`; body=2 else=1
  - L331: IF `node.reward == 0`; body=2 else=0
- Main call graph hints: `logging.info`
#### `generate_prompt(node)` (L340)
- Inputs: parameters `generate_prompt(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L353: `question + '\n'.join(reversed(trajectory))`
- Loops:
  - L343: {'line': 343, 'type': 'while', 'test': 'node', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L345: IF `node.state['thought']`; body=1 else=0
  - L347: IF `node.state['action']`; body=1 else=0
  - L349: IF `node.state['observation'] and node.depth != 0`; body=1 else=0
- Main call graph hints: `trajectory.append`, `Constant.join`, `new_segment.append`, `reversed`

---

## File: `hotpot/run.py`

**Lines:** 68  

### Imports
- `import os`
- `import json`
- `import argparse`
- `from hotpotqa import HotPotQATask`
- `from models import gpt_usage`
- `from lats import lats_search`
- `from tot import dfs_search`
- `from rap import mcts_search`
- `import logging`

### Module assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L65 If: `if __name__ == '__main__': args = parse_args() print(args) run(args)`

### Classes
- None

### Functions
#### `run(args)` (L12)
- Inputs: parameters `run(args)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L26: {'line': 26, 'type': 'for', 'target': 'i', 'iter': 'range(args.task_start_index, args.task_end_index)', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L28: IF `args.algorithm == 'lats'`; body=1 else=1
  - L37: IF `em is None`; body=1 else=0
  - L30: IF `args.algorithm == 'tot'`; body=1 else=1
  - L32: IF `args.algorithm == 'rap'`; body=1 else=1
- LLM/model/env calls:
  - L46: `gpt_usage`
- Main call graph hints: `HotPotQATask`, `print`, `os.makedirs`, `logging.basicConfig`, `range`, `os.path.dirname`, `task_accs.append`, `gpt_usage`, `lats_search`, `sum`, `len`, `dfs_search`, `mcts_search`, `Exception`
#### `parse_args()` (L48)
- Inputs: parameters `parse_args()` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L62: `args`
- Main call graph hints: `argparse.ArgumentParser`, `args.add_argument`, `args.parse_args`

---

## File: `hotpot/tot.py`

**Lines:** 407  

### Imports
- `import itertools`
- `import numpy as np`
- `from functools import partial`
- `from models import gpt`
- `import wikienv, wrappers`
- `import requests`
- `import logging`

### Module assignments
- L15: `env = wikienv.WikiEnv()`
- L16: `env = wrappers.HotPotQAWrapper(env, split="train")`
- L17: `env = wrappers.LoggingWrapper(env)`
- L22: `reflection_map = []`

### Prompt-like assignments
- L35 `value_prompt`: `value_prompt = task.value_prompt_wrap(x, y, unique_trajectories, reflection_map)`
- L41 `value_outputs`: `value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)`
- L72 `samples`: `samples = gpt(prompt, n=n_generate_sample, stop=stop)`
- L304 `sampled_actions`: `sampled_actions = get_samples(task, prompt, f"Thought {node.depth + 1}: ", args.n_generate_sample, prompt_sample=args.prompt_sample, stop="Observation")`
- L348 `child_prompts`: `child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]`
- L349 `votes`: `votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)`
- L355 `votes`: `votes = votes + [0] * (len(node.children) - len(votes))`
- L89 `state`: `self.state = {'thought': '', 'action': '', 'observation': ''} if state is None else state`
- L196 `all_nodes`: `all_nodes = [(node, node.value) for node in collect_all_nodes(root)]`
- L243 `all_nodes`: `all_nodes = [(node, node.value) for node in collect_all_nodes(root)]`
- L311 `thought_line`: `thought_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith(f"Thought {node.depth + 1}")), '')`
- L312 `action_line`: `action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)`
- L56 `value`: `value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)`
- L138 `thought`: `thought = line.split(", thought=")[1].split(", action=")[0].strip()`
- L139 `action`: `action = line.split(", action=")[1].split(", observation=")[0].strip()`
- L140 `observation`: `observation = line.split(", observation=")[1].split(")")[0].strip()`
- L249 `best_node`: `best_node = max(terminal_nodes_with_reward_1, key=lambda x: x.value)`
- L322 `action_type`: `action_type = action_line.split('[')[0] if '[' in action_line else action_line`
- L323 `action_param`: `action_param = action_line.split('[')[1].split(']')[0] if '[' in action_line else ""`
- L324 ``: `obs, r, done, info = step(env, f"{action_type.lower()}[{action_param}]")`
- L331 `new_node`: `new_node = Node(state=new_state, question=node.question, parent=node)`
- L389 `value`: `node.value = (node.value * (node.visits - 1) + value) / node.visits`
- L383 `value`: `node.value = (node.value * (node.visits - 1) + value) / node.visits`
- L386 `value`: `node.value = (node.value * (node.visits - 1) + (-1)) / node.visits`

### Classes
#### Class `Node` L87 bases=[]
##### `__init__(self, state, question, parent)` (L88)
- Inputs: parameters `__init__(self, state, question, parent)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `uct(self)` (L101)
- Inputs: parameters `uct(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L105: `self.value / self.visits + np.sqrt(2 * np.log(self.parent.visits) / self.visits)`
  - L104: `self.value * 2`
- Decisions / conditions:
  - L102: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `np.sqrt`, `np.log`
##### `uct_with_depth(self, C1, C2)` (L107)
- Inputs: parameters `uct_with_depth(self, C1, C2)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L113: `exploitation_term + C1 * exploration_term + C2 * depth_term`
  - L109: `self.value`
- Decisions / conditions:
  - L108: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `np.sqrt`, `np.log`
##### `__str__(self)` (L115)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L116: `f"Node(depth={self.depth}, value={self.value:.2f}, visits={self.visits}, thought={self.state['thought']}, action={self.state['action']}, observation={self.state['observation']})"`
##### `to_dict(self)` (L118)
- Inputs: parameters `to_dict(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L119: `{'state': self.state, 'question': self.question, 'parent': self.parent.to_dict() if self.parent else None, 'children': [child.to_dict() for child in self.children], 'visits': self.visits, 'value': self.value, 'depth': self.depth, 'is_terminal': self.is_terminal, 'reward': self.reward, 'em': self.em}`
- Main call graph hints: `self.parent.to_dict`, `child.to_dict`

### Functions
#### `step(env, action)` (L24)
- Inputs: parameters `step(env, action)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L28: `env.step(action)`
- Loops:
  - L26: {'line': 26, 'type': 'while', 'test': 'attempts < 10', 'body_len': 1, 'orelse_len': 0}
- Exception handling:
  - L27: handlers=['requests.exceptions.Timeout'] final=0
- I/O/env/executor calls:
  - L28: `env.step`
- Main call graph hints: `env.step`
#### `get_value(task, x, y, n_evaluate_sample, cache_value)` (L32)
- Inputs: parameters `get_value(task, x, y, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L47: `value`
  - L39: `task.value_cache[value_prompt]`
- Decisions / conditions:
  - L38: IF `cache_value and value_prompt in task.value_cache`; body=1 else=0
  - L45: IF `cache_value`; body=1 else=0
- LLM/model/env calls:
  - L41: `gpt`
- Main call graph hints: `get_unique_trajectories`, `task.value_prompt_wrap`, `logging.info`, `gpt`, `task.value_outputs_unwrap`
#### `get_values(task, x, ys, n_evaluate_sample, cache_value)` (L49)
- Inputs: parameters `get_values(task, x, ys, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L59: `values`
- Loops:
  - L52: {'line': 52, 'type': 'for', 'target': 'y', 'iter': 'ys', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L53: IF `y in local_value_cache`; body=1 else=2
- Main call graph hints: `values.append`, `get_value`
#### `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` (L61)
- Inputs: parameters `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L73: `[y + _ for _ in samples]`
- Decisions / conditions:
  - L65: IF `prompt_sample == 'standard'`; body=1 else=1
  - L67: IF `prompt_sample == 'cot'`; body=1 else=1
- LLM/model/env calls:
  - L72: `gpt`
- Main call graph hints: `get_unique_trajectories`, `logging.info`, `gpt`, `task.standard_prompt_wrap`, `task.cot_prompt_wrap`, `ValueError`
#### `get_unique_trajectories(failed_trajectories, num)` (L75)
- Inputs: parameters `get_unique_trajectories(failed_trajectories, num)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L85: `unique_trajectories`
- Loops:
  - L78: {'line': 78, 'type': 'for', 'target': 'traj', 'iter': 'failed_trajectories', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L80: IF `final_answer not in seen_final_answers`; body=2 else=0
  - L83: IF `len(unique_trajectories) >= num`; body=1 else=0
- Main call graph hints: `set`, `traj.get`, `unique_trajectories.append`, `seen_final_answers.add`, `len`, `node_trajectory_to_text`
#### `node_trajectory_to_text(node_string)` (L132)
- Inputs: parameters `node_trajectory_to_text(node_string)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L152: `'\n'.join(formatted_lines)`
- Loops:
  - L135: {'line': 135, 'type': 'for', 'target': 'line', 'iter': 'lines', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L144: IF `depth != 0`; body=3 else=0
  - L145: IF `thought`; body=1 else=0
  - L147: IF `action`; body=1 else=0
  - L149: IF `observation`; body=1 else=0
- Exception handling:
  - L136: handlers=['IndexError'] final=0
- Main call graph hints: `node_string.split`, `Constant.join`, `int`, `line.split[...].split[...].strip`, `formatted_lines.append`, `line.split[...].split`, `line.split`
#### `collect_all_nodes(node)` (L154)
- Docstring: Recursively collect all nodes starting from the given node.
- Inputs: parameters `collect_all_nodes(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L159: `nodes`
- Loops:
  - L157: {'line': 157, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `nodes.extend`, `collect_all_nodes`
#### `collect_trajectory(node)` (L161)
- Inputs: parameters `collect_trajectory(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L166: `'\n'.join(reversed(trajectory))`
- Loops:
  - L163: {'line': 163, 'type': 'while', 'test': 'node', 'body_len': 2, 'orelse_len': 0}
- Main call graph hints: `Constant.join`, `trajectory.append`, `reversed`, `str`
#### `dfs_search(args, task, idx, iterations, depth_limit, to_print)` (L168)
- Inputs: parameters `dfs_search(args, task, idx, iterations, depth_limit, to_print)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L201: `(root, 0, all_nodes, 0, 0)`
  - L186: `(node.state, node.value, all_nodes, node.reward, node.em)`
- Loops:
  - L180: {'line': 180, 'type': 'while', 'test': 'stack and it < iterations', 'body_len': 9, 'orelse_len': 0}
- Decisions / conditions:
  - L173: IF `to_print`; body=1 else=0
  - L184: IF `node.is_terminal and node.reward == 1`; body=2 else=0
  - L188: IF `node.depth >= depth_limit`; body=3 else=0
- Main call graph hints: `partial`, `env.reset`, `Node`, `logging.info`, `print`, `stack.pop`, `expand_node`, `stack.extend`, `reversed`, `collect_all_nodes`
#### `select_node_dfs(stack)` (L204)
- Inputs: parameters `select_node_dfs(stack)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L205: `stack[-1] if stack else None`
#### `mcts_search(args, task, idx, iterations, to_print)` (L207)
- Inputs: parameters `mcts_search(args, task, idx, iterations, to_print)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L263: `(best_child.state, best_child.value, all_nodes, best_child.reward, best_child.em)`
  - L232: `(node.state, node.value, all_nodes, node.reward, node.em)`
  - L250: `(best_node.state, best_node.value, all_nodes, best_node.reward, best_node.em)`
- Loops:
  - L218: {'line': 218, 'type': 'for', 'target': 'i', 'iter': 'range(iterations)', 'body_len': 14, 'orelse_len': 0}
  - L222: {'line': 222, 'type': 'while', 'test': 'node is None or (node.is_terminal and node.reward != 1)', 'body_len': 2, 'orelse_len': 0}
  - L236: {'line': 236, 'type': 'while', 'test': 'node.is_terminal', 'body_len': 3, 'orelse_len': 0}
  - L252: {'line': 252, 'type': 'for', 'target': '(j, (node, value))', 'iter': 'enumerate(all_nodes)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L212: IF `to_print`; body=1 else=0
  - L259: IF `best_child.reward == 1`; body=1 else=1
  - L226: IF `node is None`; body=2 else=0
  - L230: IF `node.is_terminal and node.reward == 1`; body=2 else=0
  - L247: IF `terminal_nodes_with_reward_1`; body=3 else=0
- I/O/env/executor calls:
  - L241: `evaluate_node`
- Main call graph hints: `partial`, `env.reset`, `Node`, `range`, `max`, `print`, `logging.info`, `select_node`, `expand_node`, `evaluate_node`, `backpropagate`, `enumerate`, `collect_all_nodes`, `str`
#### `select_node(node)` (L265)
- Inputs: parameters `select_node(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L291: `node`
  - L282: `node_with_reward_1`
- Loops:
  - L266: {'line': 266, 'type': 'while', 'test': 'node and node.children', 'body_len': 9, 'orelse_len': 0}
  - L286: {'line': 286, 'type': 'while', 'test': 'node.is_terminal and node.reward != 1', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L272: IF `len(terminal_children) == len(node.children)`; body=4 else=0
  - L280: IF `node_with_reward_1`; body=2 else=0
  - L274: IF `node.parent`; body=1 else=0
- Main call graph hints: `logging.info`, `next`, `max`, `len`, `node.parent.children.remove`, `child.uct`, `node.uct`
#### `expand_node(node, args, task)` (L293)
- Inputs: parameters `expand_node(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L298: `None`
- Decisions / conditions:
  - L294: IF `node.depth >= 7`; body=4 else=0
- LLM/model/env calls:
  - L299: `generate_new_states`
- Main call graph hints: `generate_new_states`, `node.children.extend`, `logging.info`, `print`
#### `generate_new_states(node, args, task)` (L302)
- Inputs: parameters `generate_new_states(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L344: `list(unique_states.values())`
- Loops:
  - L308: {'line': 308, 'type': 'for', 'target': 'action', 'iter': 'sampled_actions', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L318: IF `unique_key in unique_states`; body=1 else=0
  - L321: IF `action_line`; body=14 else=0
  - L334: IF `r == 1`; body=1 else=0
  - L340: IF `new_node.is_terminal and r == 0`; body=2 else=0
- LLM/model/env calls:
  - L303: `generate_prompt`
- I/O/env/executor calls:
  - L324: `step`
- Main call graph hints: `generate_prompt`, `get_samples`, `logging.info`, `list`, `node.state.copy`, `next`, `unique_states.values`, `step`, `Node`, `line.split[...].strip`, `info.get`, `collect_trajectory`, `failed_trajectories.append`, `action.split`, `line.startswith`, `action_line.split`, `action_line.split[...].split`, `action_type.lower`, `line.split`
#### `evaluate_node(node, args, task)` (L347)
- Inputs: parameters `evaluate_node(node, args, task)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L369: `sum(votes) / len(votes) if votes else 0`
- Loops:
  - L362: {'line': 362, 'type': 'for', 'target': '(i, condition)', 'iter': 'enumerate(terminal_conditions)', 'body_len': 1, 'orelse_len': 0}
  - L366: {'line': 366, 'type': 'for', 'target': '(i, child)', 'iter': 'enumerate(node.children)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L358: IF `max_vote == 0`; body=1 else=0
  - L363: IF `condition == 1`; body=1 else=0
- LLM/model/env calls:
  - L348: `generate_prompt`
- Main call graph hints: `get_values`, `logging.info`, `enumerate`, `generate_prompt`, `max`, `sum`, `len`
#### `print_tree(node, level)` (L372)
- Inputs: parameters `print_tree(node, level)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L375: {'line': 375, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `print`, `print_tree`
#### `backpropagate(node, value)` (L378)
- Inputs: parameters `backpropagate(node, value)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L379: {'line': 379, 'type': 'while', 'test': 'node', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L381: IF `node.is_terminal`; body=1 else=2
  - L382: IF `node.reward == 1`; body=2 else=1
  - L385: IF `node.reward == 0`; body=2 else=0
- Main call graph hints: `logging.info`
#### `generate_prompt(node)` (L394)
- Inputs: parameters `generate_prompt(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L407: `question + '\n'.join(reversed(trajectory))`
- Loops:
  - L397: {'line': 397, 'type': 'while', 'test': 'node', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L399: IF `node.state['thought']`; body=1 else=0
  - L401: IF `node.state['action']`; body=1 else=0
  - L403: IF `node.state['observation'] and node.depth != 0`; body=1 else=0
- Main call graph hints: `trajectory.append`, `Constant.join`, `new_segment.append`, `reversed`

---

## File: `hotpot/wikienv.py`

**Lines:** 172  

### Imports
- `import ast`
- `import json`
- `import time`
- `import gym`
- `import requests`
- `from bs4 import BeautifulSoup`

### Module assignments
- None

### Prompt-like assignments
- L37 `observation_space, action_space`: `self.observation_space = self.action_space = textSpace()`

### Classes
#### Class `textSpace` L17 bases=['gym.spaces.Space']
##### `contains(self, x)` (L18)
- Docstring: Return boolean specifying if x is a valid member of this space.
- Inputs: parameters `contains(self, x)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L20: `isinstance(x, str)`
- Main call graph hints: `isinstance`
#### Class `WikiEnv` L23 bases=['gym.Env']
##### `__init__(self)` (L25)
- Docstring: Initialize the environment.
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `textSpace`, `super`
##### `_get_obs(self)` (L41)
- Inputs: parameters `_get_obs(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L42: `self.obs`
##### `_get_info(self)` (L44)
- Inputs: parameters `_get_info(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L45: `{'steps': self.steps, 'answer': self.answer}`
##### `reset(self, seed, return_info, options)` (L47)
- Inputs: parameters `reset(self, seed, return_info, options)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L60: `(observation, info) if return_info else observation`
- Main call graph hints: `self._get_obs`, `self._get_info`
##### `construct_lookup_list(self, keyword)` (L62)
- Inputs: parameters `construct_lookup_list(self, keyword)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L77: `parts`
  - L65: `[]`
- Loops:
  - L71: {'line': 71, 'type': 'for', 'target': 'p', 'iter': 'paragraphs', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L64: IF `self.page is None`; body=1 else=0
- Main call graph hints: `self.page.split`, `p.strip`, `p.split`, `s.strip`, `keyword.lower`, `p.lower`
##### `get_page_obs(page)` (L80)
- Inputs: parameters `get_page_obs(page)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L90: `' '.join(sentences[:5])`
- Loops:
  - L87: {'line': 87, 'type': 'for', 'target': 'p', 'iter': 'paragraphs', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `page.split`, `Constant.join`, `p.strip`, `p.split`, `s.strip`
##### `search_step(self, entity)` (L101)
- Inputs: parameters `search_step(self, entity)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L119: {'line': 119, 'type': 'for', 'target': 'p', 'iter': 'page', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L110: IF `result_divs`; body=2 else=2
  - L115: IF `any(('may refer to:' in p for p in page))`; body=1 else=4
  - L120: IF `len(p.split(' ')) > 2`; body=2 else=0
  - L122: IF `not p.endswith('\n')`; body=1 else=0
- I/O/env/executor calls:
  - L116: `self.search_step`
- Main call graph hints: `entity.replace`, `time.time`, `BeautifulSoup`, `soup.find_all`, `requests.get`, `any`, `clean_str`, `p.get_text.strip`, `self.search_step`, `self.get_page_obs`, `div.get_text.strip`, `p.get_text`, `len`, `div.get_text`, `p.split`, `p.endswith`
##### `step(self, action)` (L127)
- Inputs: parameters `step(self, action)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L163: `(self.obs, reward, done, self._get_info())`
- Decisions / conditions:
  - L135: IF `action.startswith('search[') and action.endswith(']')`; body=2 else=1
  - L140: IF `action.startswith('lookup[') and action.endswith(']')`; body=3 else=1
  - L142: IF `self.lookup_keyword != keyword`; body=3 else=0
  - L146: IF `self.lookup_cnt >= len(self.lookup_list)`; body=1 else=2
  - L151: IF `action.startswith('finish[') and action.endswith(']')`; body=4 else=1
  - L156: IF `action.startswith('think[') and action.endswith(']')`; body=1 else=1
- I/O/env/executor calls:
  - L139: `self.search_step`
- Main call graph hints: `action.strip`, `action.startswith`, `action.endswith`, `self.search_step`, `self._get_info`, `len`, `self.construct_lookup_list`, `Constant.format`
##### `get_time_info(self)` (L165)
- Inputs: parameters `get_time_info(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L167: `{'call_speed': speed, 'call_time': self.search_time, 'num_calls': self.num_searches}`

### Functions
#### `clean_str(p)` (L10)
- Inputs: parameters `clean_str(p)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L12: `p.encode().decode('unicode-escape').encode('latin1').decode('utf-8')`
  - L14: `p`
- Exception handling:
  - L11: handlers=['UnicodeDecodeError'] final=0
- Main call graph hints: `p.encode.decode.encode.decode`, `p.encode.decode.encode`, `p.encode.decode`, `p.encode`

---

## File: `hotpot/wrappers.py`

**Lines:** 241  

### Imports
- `import json`
- `import os`
- `import gym`
- `import numpy as np`
- `import re`
- `import string`
- `from collections import Counter`

### Module assignments
- L10: `DATA_DIR = "data"`
- L11: `HOTPOTQA_SPLIT_FILE = { "train": "hotpot_train_v1.1_simplified.json", "dev": "hotpot_dev_v1_simplified.json", "test": "hotpot_test_v1_simplified.json", }`
- L17: `FEVER_SPLIT_FILE = { "train": "train.jsonl", "dev": "paper_dev.jsonl", }`

### Prompt-like assignments
- L59 `normalized_prediction`: `normalized_prediction = normalize_answer(prediction)`
- L60 `normalized_ground_truth`: `normalized_ground_truth = normalize_answer(ground_truth)`
- L85 `data`: `self.data = [(d['question'], d['answer']) for d in self.data]`
- L97 `observation`: `observation = f"Question: {self.data[self.data_idx][0]}"`
- L166 `observation`: `observation = f"Claim: {self.data[self.data_idx][0]}"`
- L217 `traj`: `self.traj = {"observations": [observation], "actions": []}`
- L111 `pred`: `pred = normalize_answer(self.data[self.data_idx][1])`
- L119 `pred`: `pred = normalize_answer(self.data[self.data_idx][1])`
- L180 `label`: `label = normalize_answer(self.data[self.data_idx][1])`
- L36 `observation`: `observation = self.env.traj["observations"][0] + "\n"`

### Classes
#### Class `HistoryWrapper` L23 bases=['gym.ObservationWrapper']
##### `__init__(self, env, obs_format, prompt)` (L24)
- Inputs: parameters `__init__(self, env, obs_format, prompt)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L27: IF `obs_format == 'history'`; body=1 else=0
- Main call graph hints: `super.__init__`, `hasattr`, `super`
##### `observation(self, obs)` (L32)
- Inputs: parameters `observation(self, obs)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L34: `obs`
  - L39: `self.prompt + observation`
- Loops:
  - L37: {'line': 37, 'type': 'for', 'target': '(i, (o, a))', 'iter': "enumerate(zip(self.env.traj['observations'][1:], self.env.traj['actions']), 1)", 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L33: IF `self.obs_format == 'obs'`; body=1 else=1
  - L35: IF `self.obs_format == 'history'`; body=3 else=0
- Main call graph hints: `enumerate`, `zip`
#### Class `HotPotQAWrapper` L80 bases=['gym.Wrapper']
##### `__init__(self, env, split)` (L81)
- Inputs: parameters `__init__(self, env, split)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- I/O/env/executor calls:
  - L84: `json.load`
  - L84: `open`
- Main call graph hints: `super.__init__`, `json.load`, `open`, `super`
##### `reset(self, seed, return_info, options, idx)` (L89)
- Inputs: parameters `reset(self, seed, return_info, options, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L99: `(observation, info) if return_info else observation`
- Exception handling:
  - L91: handlers=['Exception'] final=0
- I/O/env/executor calls:
  - L92: `self.env.step`
- Main call graph hints: `self.env.reset`, `self._get_info`, `self.env.step`, `int`, `np.random.randint`, `len`
##### `_get_info(self)` (L101)
- Inputs: parameters `_get_info(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L102: `{'steps': self.steps, 'answer': self.answer, 'question': self.data[self.data_idx][0], 'hotpot_split': self.split}`
##### `get_reward(self, info)` (L109)
- Inputs: parameters `get_reward(self, info)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L115: `0`
  - L114: `int(score)`
- Decisions / conditions:
  - L110: IF `info['answer'] is not None`; body=4 else=0
- Main call graph hints: `normalize_answer`, `int`
##### `get_metrics(self, info)` (L117)
- Inputs: parameters `get_metrics(self, info)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L124: `{'reward': 0, 'em': 0, 'f1': 0}`
  - L123: `{'reward': em, 'em': em, 'f1': f1}`
- Decisions / conditions:
  - L118: IF `info['answer'] is not None`; body=5 else=0
- Main call graph hints: `normalize_answer`, `f1_score`
##### `step(self, action)` (L126)
- Inputs: parameters `step(self, action)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L134: `(obs, reward, done, info)`
- Decisions / conditions:
  - L130: IF `done`; body=3 else=0
- I/O/env/executor calls:
  - L128: `self.env.step`
- Main call graph hints: `self.env.step`, `self.get_reward`, `info.update`, `self.get_metrics`
##### `__len__(self)` (L136)
- Inputs: parameters `__len__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L137: `len(self.data)`
- Main call graph hints: `len`
#### Class `FeverWrapper` L139 bases=['gym.Wrapper']
##### `__init__(self, env, split)` (L140)
- Inputs: parameters `__init__(self, env, split)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L148: {'line': 148, 'type': 'for', 'target': 'json_str', 'iter': 'json_list', 'body_len': 4, 'orelse_len': 0}
- I/O/env/executor calls:
  - L144: `open`
  - L149: `json.loads`
- Main call graph hints: `super.__init__`, `open`, `list`, `json.loads`, `data.append`, `super`
##### `reset(self, seed, return_info, options, idx)` (L158)
- Inputs: parameters `reset(self, seed, return_info, options, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L168: `(observation, info) if return_info else observation`
- Exception handling:
  - L160: handlers=['Exception'] final=0
- I/O/env/executor calls:
  - L161: `self.env.step`
- Main call graph hints: `self.env.reset`, `self._get_info`, `self.env.step`, `int`, `np.random.randint`, `len`
##### `_get_info(self)` (L170)
- Inputs: parameters `_get_info(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L171: `{'steps': self.steps, 'answer': self.answer, 'question': self.data[self.data_idx][0], 'fever_split': self.split}`
##### `get_reward(self, info)` (L178)
- Inputs: parameters `get_reward(self, info)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L184: `0`
  - L183: `1`
- Decisions / conditions:
  - L179: IF `info['answer'] is not None`; body=3 else=0
  - L182: IF `label == pred`; body=1 else=0
- Main call graph hints: `normalize_answer`
##### `step(self, action)` (L186)
- Inputs: parameters `step(self, action)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L194: `(obs, reward, done, info)`
- Decisions / conditions:
  - L190: IF `done`; body=3 else=0
- I/O/env/executor calls:
  - L188: `self.env.step`
- Main call graph hints: `self.env.step`, `self.get_reward`, `info.update`
##### `__len__(self)` (L196)
- Inputs: parameters `__len__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L197: `len(self.data)`
- Main call graph hints: `len`
#### Class `LoggingWrapper` L200 bases=['gym.Wrapper']
##### `__init__(self, env, folder, file_id)` (L201)
- Inputs: parameters `__init__(self, env, folder, file_id)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `os.makedirs`, `np.random.randint`, `super`
##### `__len__(self)` (L210)
- Inputs: parameters `__len__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L211: `len(self.env.data)`
- Main call graph hints: `len`
##### `reset(self, seed, return_info, options, idx)` (L214)
- Inputs: parameters `reset(self, seed, return_info, options, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L218: `output`
- Main call graph hints: `self.env.reset`
##### `step(self, action)` (L220)
- Inputs: parameters `step(self, action)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L226: `(obs, reward, done, info)`
- Decisions / conditions:
  - L224: IF `done`; body=1 else=0
- I/O/env/executor calls:
  - L221: `self.env.step`
- Main call graph hints: `self.env.step`, `self.traj[...].append`, `self.traj.update`
##### `update_record(self)` (L228)
- Inputs: parameters `update_record(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L229: IF `len(self.traj) > 0`; body=2 else=0
- Main call graph hints: `len`, `self.trajs.append`
##### `write(self)` (L233)
- Inputs: parameters `write(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- I/O/env/executor calls:
  - L235: `open`
  - L236: `json.dump`
- Main call graph hints: `self.update_record`, `open`, `json.dump`, `print`
##### `close(self)` (L239)
- Inputs: parameters `close(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- I/O/env/executor calls:
  - L240: `self.write`
- Main call graph hints: `self.write`

### Functions
#### `normalize_answer(s)` (L42)
- Inputs: parameters `normalize_answer(s)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L56: `white_space_fix(remove_articles(remove_punc(lower(s))))`
  - L44: `re.sub('\\b(a|an|the)\\b', ' ', text)`
  - L47: `' '.join(text.split())`
  - L51: `''.join((ch for ch in text if ch not in exclude))`
  - L54: `text.lower()`
- Main call graph hints: `white_space_fix`, `re.sub`, `Constant.join`, `set`, `text.lower`, `remove_articles`, `text.split`, `remove_punc`, `lower`
#### `f1_score(prediction, ground_truth)` (L58)
- Inputs: parameters `f1_score(prediction, ground_truth)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L78: `(f1, precision, recall)`
  - L65: `ZERO_METRIC`
  - L67: `ZERO_METRIC`
  - L74: `ZERO_METRIC`
- Decisions / conditions:
  - L64: IF `normalized_prediction in ['yes', 'no', 'noanswer'] and normalized_prediction != normalized_ground_truth`; body=1 else=0
  - L66: IF `normalized_ground_truth in ['yes', 'no', 'noanswer'] and normalized_prediction != normalized_ground_truth`; body=1 else=0
  - L73: IF `num_same == 0`; body=1 else=0
- Main call graph hints: `normalize_answer`, `normalized_prediction.split`, `normalized_ground_truth.split`, `sum`, `Counter`, `common.values`, `len`

---

## File: `programming/dfs.py`

**Lines:** 223  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl, resume_success_count`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List, Dict, Tuple, Any`
- `import math`
- `import sys`

### Module assignments
- None

### Prompt-like assignments
- L139 `reflection`: `reflection = gen.self_reflection(cur_func_impl, feedback, model)`
- L107 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, 6)`
- L110 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L160 `new_solution`: `new_solution = gen.func_impl( func_sig=item["prompt"], model=model, strategy="simple", prev_func_impl=prev_func_impl, feedback=feedback, self_reflection=reflection, acc_feedback = acc_feedback, acc_reflection = acc_reflection )`
- L177 `reflection`: `reflection = gen.self_reflection(child.solution, feedback_internal, model)`
- L188 `passed_section`: `passed_section = feedback_internal.split("Tests failed:")[0]`

### Classes
#### Class `Node` L10 bases=[]
##### `__init__(self, solution, parent, context, depth)` (L11)
- Inputs: parameters `__init__(self, solution, parent, context, depth)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `uct(self, exploration_weight)` (L22)
- Inputs: parameters `uct(self, exploration_weight)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L26: `self.value / self.visits + exploration_weight * math.sqrt(math.log(self.parent.visits) / self.visits)`
  - L25: `self.value`
- Decisions / conditions:
  - L23: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `math.sqrt`, `math.log`
##### `best_child(self)` (L28)
- Inputs: parameters `best_child(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L31: `max(self.children, key=lambda child: child.uct())`
  - L30: `None`
- Decisions / conditions:
  - L29: IF `not self.children`; body=1 else=0
- Main call graph hints: `max`, `child.uct`
##### `best_child_value(self)` (L33)
- Inputs: parameters `best_child_value(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L36: `max(self.children, key=lambda child: child.value)`
  - L35: `None`
- Decisions / conditions:
  - L34: IF `not self.children`; body=1 else=0
- Main call graph hints: `max`
##### `update(self, reward)` (L38)
- Inputs: parameters `update(self, reward)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.

### Functions
#### `prune_context_blocks(context, max_length)` (L43)
- Docstring: Prune the context to fit within the specified max_length by removing entire blocks of content using 'trial' as a delimiter.
- Inputs: parameters `prune_context_blocks(context, max_length)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L55: `'trial'.join(blocks)`
  - L46: `context`
- Loops:
  - L52: {'line': 52, 'type': 'while', 'test': "len('trial'.join(blocks)) > max_length and blocks", 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L45: IF `len(context) <= max_length`; body=1 else=0
- Main call graph hints: `context.split`, `Constant.join`, `len`, `blocks.pop`
#### `gather_context_from_tree(node)` (L57)
- Docstring: Given a node, walk up its tree and gather the feedback and reflections 
from each parent node until the root is reached.

Args:
    node (Node): The node to start gathering context from.

Returns:
    Tuple[List[str], List[str]]: Two lists containing the accumulated feedback and reflections.
- Inputs: parameters `gather_context_from_tree(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L79: `(accumulated_feedback[::-1], accumulated_reflection[::-1])`
- Loops:
  - L71: {'line': 71, 'type': 'while', 'test': 'node', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L72: IF `node.test_feedback`; body=1 else=0
  - L74: IF `node.reflection`; body=1 else=0
- Main call graph hints: `accumulated_feedback.append`, `accumulated_reflection.append`
#### `run_dfs(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode, n)` (L81)
- Inputs: parameters `run_dfs(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode, n)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L103: {'line': 103, 'type': 'for', 'target': '(idx, item)', 'iter': 'enumerate(dataset)', 'body_len': 33, 'orelse_len': 0}
  - L109: {'line': 109, 'type': 'while', 'test': 'cur_func_impl is None', 'body_len': 1, 'orelse_len': 0}
  - L145: {'line': 145, 'type': 'while', 'test': 'stack and it < 50', 'body_len': 16, 'orelse_len': 0}
  - L159: {'line': 159, 'type': 'while', 'test': 'new_solution is None', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L104: IF `is_leetcode`; body=1 else=1
  - L128: IF `is_passing`; body=7 else=0
  - L200: IF `is_solved`; body=1 else=2
  - L209: IF `is_passing`; body=1 else=0
  - L149: IF `node.depth >= max_depth`; body=1 else=0
  - L176: IF `not is_passing_internal`; body=5 else=5
  - L186: IF `'Tested passed:' in feedback_internal`; body=3 else=0
  - L192: IF `is_passing`; body=2 else=0
- LLM/model/env calls:
  - L95: `model_factory`
- I/O/env/executor calls:
  - L124: `exe.execute`
  - L206: `exe.execute`
  - L208: `exe.evaluate`
  - L220: `write_jsonl`
  - L129: `exe.evaluate`
  - L134: `write_jsonl`
  - L175: `exe.execute`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate`, `Node`, `implementations.append`, `isinstance`, `exe.execute`, `test_feedback.append`, `gen.self_reflection`, `exe.evaluate`, `reflections.append`, `round`, `write_jsonl`, `print_v`, `gen.internal_tests`, `gen.func_impl`, `int`, `stack.pop`, `node.children.append`, `stack.append`, `root.best_child_value`, `feedback_internal.split`, `passed_section.split[...].splitlines`, `line.strip`, `passed_section.split`

---

## File: `programming/executors/__init__.py`

**Lines:** 3  

### Imports
- `from .py_executor import PyExecutor`
- `from .rs_executor import RsExecutor`
- `from .factory import executor_factory`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming/executors/executor_types.py`

**Lines:** 27  

### Imports
- `from typing import NamedTuple, List, Tuple`
- `from abc import ABC, abstractmethod`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `ExecuteResult` L4 bases=['NamedTuple']
#### Class `Executor` L9 bases=['ABC']
##### `execute(self, func, tests, timeout)` (L11)
- Inputs: parameters `execute(self, func, tests, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `evaluate(self, name, func, test, timeout)` (L15)
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.

### Functions
- None

---

## File: `programming/executors/executor_utils.py`

**Lines:** 59  

### Imports
- `import os, json`
- `from threading import Thread`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `PropagatingThread` L12 bases=['Thread']
##### `run(self)` (L13)
- Inputs: parameters `run(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L16: IF `hasattr(self, '_Thread__target')`; body=1 else=1
- Exception handling:
  - L15: handlers=['BaseException'] final=0
- I/O/env/executor calls:
  - L18: `self._Thread__target`
- Main call graph hints: `hasattr`, `self._Thread__target`, `self._target`
##### `join(self, timeout)` (L24)
- Inputs: parameters `join(self, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L28: `self.ret`
- Decisions / conditions:
  - L26: IF `self.exc`; body=1 else=0
- Main call graph hints: `super.join`, `super`

### Functions
#### `timeout_handler(_, __)` (L2)
- Inputs: parameters `timeout_handler(_, __)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `TimeoutError`
#### `to_jsonl(dict_data, file_path)` (L6)
- Inputs: parameters `to_jsonl(dict_data, file_path)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- I/O/env/executor calls:
  - L7: `open`
  - L8: `json.dumps`
  - L9: `file.write`
- Main call graph hints: `open`, `json.dumps`, `file.write`
#### `function_with_timeout(func, args, timeout)` (L31)
- Inputs: parameters `function_with_timeout(func, args, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L44: `result_container[0]`
- Decisions / conditions:
  - L41: IF `thread.is_alive()`; body=1 else=1
- I/O/env/executor calls:
  - L37: `PropagatingThread`
  - L38: `thread.start`
  - L39: `thread.join`
  - L41: `thread.is_alive`
- Main call graph hints: `PropagatingThread`, `thread.start`, `thread.join`, `thread.is_alive`, `result_container.append`, `TimeoutError`, `func`

---

## File: `programming/executors/factory.py`

**Lines:** 28  

### Imports
- `from .py_executor import PyExecutor`
- `from .rs_executor import RsExecutor`
- `from .executor_types import Executor`
- `from .leet_executor import LeetExecutor`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `executor_factory(lang, is_leet)` (L6)
- Inputs: parameters `executor_factory(lang, is_leet)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L12: `LeetExecutor(ProgrammingLanguage.PYTHON3, PyExecutor(), PySubmissionFormatter)`
  - L16: `PyExecutor()`
  - L21: `LeetExecutor(ProgrammingLanguage.RUST, RsExecutor(), RsSubmissionFormatter)`
  - L25: `RsExecutor()`
- Decisions / conditions:
  - L7: IF `lang == 'py' or lang == 'python'`; body=1 else=1
  - L8: IF `is_leet`; body=4 else=1
  - L17: IF `lang == 'rs' or lang == 'rust'`; body=1 else=1
  - L18: IF `is_leet`; body=3 else=1
- Main call graph hints: `print`, `LeetExecutor`, `PyExecutor`, `ValueError`, `RsExecutor`

---

## File: `programming/executors/go_executor.py`

**Lines:** 362  

### Imports
- `import os`
- `import subprocess`
- `import tempfile`
- `from executor_types import ExecuteResult, Executor`
- `from typing import List, Tuple, Optional`
- `import re`

### Module assignments
- L226: `assert_no_panic = r""" macro_rules! assert_eq_nopanic { ($left:expr, $right:expr) => { std::panic::catch_unwind(|| { assert_eq!($left, $right); }).unwrap_or_else(|_| {}); }; () => {}; } """`

### Prompt-like assignments
- L332 `test_compiletime`: `test_compiletime = r""" # go-lats-35116-6739b2903daabf6d .\lats.go:10:7: undefined: math .\lats.go:11:18: too many return values have (bool, bool) want (bool) .\lats.go:15:16: too many return values have (bool, bool) want (bool) """`

### Top-level logic
- L330 If: `if __name__ == "__main__": test_compiletime = r""" # go-lats-35116-6739b2903daabf6d .\lats.go:10:7: undefined: math .\lats.go:11:18: too many return values have (bool, bool) want (bool) .\lats.go:15:16: too many return values have (bool, bool) want (bool) """ compile_errs = grab_compile_errs(test_compiletime) print(compile_errs) assert(len(compile_errs) == 3) test_runtime = r""" --- FAIL: TestHasCloseElements (0.00s) --- FAIL: TestHasCloseElements/all_elements_equal (0.00s) lats_test.go:53: H...`

### Classes
#### Class `GoExecutor` L84 bases=['Executor']
##### `execute(self, func, tests, timeout)` (L85)
- Inputs: parameters `execute(self, func, tests, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L166: `ExecuteResult(is_passing, feedback, tuple(state))`
  - L108: `ExecuteResult(False, err_str, state)`
- Loops:
  - L113: {'line': 113, 'type': 'for', 'target': 'i', 'iter': 'range(num_tests)', 'body_len': 11, 'orelse_len': 0}
  - L151: {'line': 151, 'type': 'for', 'target': '(i, (passed, output))', 'iter': 'enumerate(tests_res)', 'body_len': 3, 'orelse_len': 0}
  - L105: {'line': 105, 'type': 'for', 'target': 'err', 'iter': 'errs', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L99: IF `len(errs) > 0`; body=5 else=0
  - L125: IF `res is None`; body=2 else=0
  - L131: IF `len(errs) > 0`; body=2 else=0
  - L138: IF `len(errs) > 0`; body=2 else=0
  - L153: IF `passed`; body=1 else=1
- I/O/env/executor calls:
  - L90: `write_to_file`
  - L119: `write_to_file`
- Main call graph hints: `create_temp_project`, `write_to_file`, `format_files`, `download_imports`, `run_process`, `grab_compile_errs`, `len`, `range`, `os.system`, `enumerate`, `ExecuteResult`, `tuple`, `grab_test_errs`, `tests_res.append`, `state.append`, `str`
##### `evaluate(self, name, func, test, timeout)` (L168)
- Docstring: Evaluates the implementation on Human-Eval Rust (MultiPL-E generated,

Federico Cassano, John Gouwar, Daniel Nguyen, Sydney Nguyen, Luna Phipps-Costin, Donald Pinckney, Ming-Ho Yee, Yangtian Zi, Carolyn Jane Anderson, Molly Q Feldman, Arjun Guha, Michael Greenberg, Abhinav Jangda ).
If you use this function please cite:
@misc{cassano2022multiple,
  title={MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation}, 
  author={Federico Cassano and John Gouwar and Daniel Nguyen and Sydney Nguyen and Luna Phipps-Costin and Donald Pinckney and Ming-Ho Yee and Yangtian Zi and Carolyn Jane Anderson and Molly Q Feldman and Arjun Guha and Michael Greenberg and Abhinav Jangda},
  year={2022},
  eprint={2208.08227},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
})

TODO: do it actually
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L201: `False`
  - L210: `False`
  - L223: `len(errs) == 0`
  - L216: `False`
  - L220: `False`
- Decisions / conditions:
  - L197: IF `len(errs) > 0`; body=3 else=0
  - L208: IF `res is None`; body=2 else=6
  - L214: IF `len(errs) > 0`; body=2 else=0
  - L218: IF `len(errs) > 0`; body=2 else=0
- I/O/env/executor calls:
  - L187: `write_to_file_toplevel`
  - L188: `write_to_file_toplevel`
- Main call graph hints: `create_temp_project`, `print`, `write_to_file_toplevel`, `format_files`, `download_imports`, `run_process`, `grab_compile_errs`, `os.system`, `len`, `grab_test_errs`
#### Class `CompileErr` L256 bases=[]
##### `__init__(self, rendered)` (L257)
- Inputs: parameters `__init__(self, rendered)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `__str__(self)` (L260)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L261: `self.rendered`
##### `__repr__(self)` (L263)
- Inputs: parameters `__repr__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L264: `'{' + str(self) + '}'`
- Main call graph hints: `str`
#### Class `RuntimeErr` L267 bases=[]
##### `__init__(self, left, right, line, column, panic_reason)` (L268)
- Inputs: parameters `__init__(self, left, right, line, column, panic_reason)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `__str__(self)` (L277)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L279: `f'assertion failed: {self.left} == {self.right}'`
  - L281: `self.panic_reason`
- Decisions / conditions:
  - L278: IF `self.left is not None and self.right is not None`; body=1 else=1
##### `__repr__(self)` (L283)
- Inputs: parameters `__repr__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L284: `'{' + str(self) + '}'`
- Main call graph hints: `str`

### Functions
#### `create_temp_project()` (L11)
- Inputs: parameters `create_temp_project()` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L28: `(temp_dir, main_path, test_path)`
- Decisions / conditions:
  - L20: IF `os.path.exists(temp_dir)`; body=1 else=0
- Main call graph hints: `os.getpid`, `os.urandom.hex`, `tempfile.gettempdir`, `os.path.exists`, `os.mkdir`, `os.chdir`, `os.system`, `os.path.join`, `os.urandom`
#### `write_to_file(path, code, package)` (L31)
- Inputs: parameters `write_to_file(path, code, package)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L36: IF `os.path.exists(path)`; body=1 else=0
- I/O/env/executor calls:
  - L39: `open`
  - L40: `f.write`
- Main call graph hints: `os.path.exists`, `os.remove`, `open`, `f.write`
#### `format_files(paths)` (L43)
- Inputs: parameters `format_files(paths)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L44: {'line': 44, 'type': 'for', 'target': 'path', 'iter': 'paths', 'body_len': 2, 'orelse_len': 0}
- Main call graph hints: `os.system`
#### `download_imports(tmp_cargo_path)` (L49)
- Inputs: parameters `download_imports(tmp_cargo_path)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `os.system`
#### `write_to_file_toplevel(path, code)` (L53)
- Inputs: parameters `write_to_file_toplevel(path, code)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L55: IF `os.path.exists(path)`; body=1 else=0
- I/O/env/executor calls:
  - L58: `open`
  - L59: `f.write`
- Main call graph hints: `os.path.exists`, `os.remove`, `open`, `f.write`
#### `run_process(cmd, tmp_path, timeout, print_debug)` (L62)
- Docstring: Runs the given command. Produces a tuple of stdout and stderr.
- Inputs: parameters `run_process(cmd, tmp_path, timeout, print_debug)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L81: `(out, err)`
- Decisions / conditions:
  - L74: IF `print_debug`; body=5 else=0
- I/O/env/executor calls:
  - L67: `subprocess.Popen`
- Main call graph hints: `subprocess.Popen`, `p.communicate`, `out.decode`, `err.decode`, `print`
#### `transform_asserts(code)` (L238)
- Docstring: Transform all asserts into assert_eq_nopanic! asserts, inserting the macro
definition at the top of the code.
- Inputs: parameters `transform_asserts(code)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L244: `assert_no_panic + code`
- Main call graph hints: `code.replace`
#### `revert_asserts(code)` (L247)
- Docstring: Revert all assert_eq_nopanic! asserts back into assert_eq! asserts.
- Inputs: parameters `revert_asserts(code)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L253: `normal[len(assert_no_panic):]`
- Main call graph hints: `code.replace`, `len`
#### `grab_compile_errs(inp)` (L289)
- Inputs: parameters `grab_compile_errs(inp)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L308: `objs`
- Loops:
  - L293: {'line': 293, 'type': 'for', 'target': 'line', 'iter': 'inp.splitlines()', 'body_len': 4, 'orelse_len': 0}
- Decisions / conditions:
  - L305: IF `compileErr != ''`; body=1 else=0
  - L294: IF `line == ''`; body=1 else=0
  - L296: IF `line.startswith('#')`; body=1 else=0
  - L298: IF `line.startswith('.\\lats.go')`; body=2 else=0
  - L302: IF `line.startswith('        ')`; body=1 else=0
  - L299: IF `compileErr != ''`; body=1 else=0
- Main call graph hints: `inp.splitlines`, `line.startswith`, `objs.append`, `CompileErr`, `line.strip`
#### `grab_test_errs(inp)` (L314)
- Inputs: parameters `grab_test_errs(inp)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L327: `failed_asserts`
- Loops:
  - L316: {'line': 316, 'type': 'for', 'target': 'line', 'iter': 'inp.splitlines()', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L317: IF `line.startswith('        lats_test.go')`; body=4 else=0
  - L321: IF `match`; body=2 else=0
- Main call graph hints: `inp.splitlines`, `line.startswith`, `re.match`, `failed_asserts.append`, `line.strip`, `match.group`, `RuntimeErr`

---

## File: `programming/executors/leet_executor.py`

**Lines:** 59  

### Imports
- `from __future__ import annotations`
- `from typing import List`
- `from .executor_types import ExecuteResult, Executor`
- `from .executor_utils import to_jsonl`
- `from datetime import datetime`

### Module assignments
- None

### Prompt-like assignments
- L37 `submission`: `submission = LeetCodeSubmission( code=leetcode_formatted_func, lang=self.lang, question_id=id_from_slug(name, self.env.api_instance), question_slug=name, timeout=timeout )`

### Classes
#### Class `LeetExecutor` L9 bases=['Executor']
##### `__init__(self, lang, executor, formatter)` (L10)
- Inputs: parameters `__init__(self, lang, executor, formatter)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `isinstance`, `LeetCodeEnv`, `datetime.now.strftime`, `datetime.now`
##### `execute(self, func, tests, timeout)` (L22)
- Inputs: parameters `execute(self, func, tests, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L23: `self.executor.execute(func, tests, timeout)`
- I/O/env/executor calls:
  - L23: `self.executor.execute`
- Main call graph hints: `self.executor.execute`
##### `evaluate(self, name, func, test, timeout)` (L25)
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L58: `reward`
  - L33: `False`
- Exception handling:
  - L29: handlers=['Exception'] final=0
- I/O/env/executor calls:
  - L45: `self.env.step`
- Main call graph hints: `print`, `LeetCodeSubmission`, `self.env.step`, `to_jsonl`, `self.formatter.to_leetcode`, `id_from_slug`

### Functions
- None

---

## File: `programming/executors/py_executor.py`

**Lines:** 96  

### Imports
- `import ast`
- `import signal`
- `import astunparse`
- `from .executor_utils import function_with_timeout`
- `from typing import List`
- `from .executor_types import ExecuteResult, Executor`

### Module assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L90 If: `if __name__ == "__main__": pass # Test the function func = "def add(a, b):\n while True:\n x = 1\n return a + b" tests = ["assert add(1, 2) == 3", "assert add(1, 2) == 4"] print(PyExecutor().execute(func, tests, timeout=1))`

### Classes
#### Class `PyExecutor` L10 bases=['Executor']
##### `execute(self, func, tests, timeout)` (L11)
- Inputs: parameters `execute(self, func, tests, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L48: `ExecuteResult(is_passing, feedback, state)`
- Loops:
  - L21: {'line': 21, 'type': 'for', 'target': 'i', 'iter': 'range(num_tests)', 'body_len': 1, 'orelse_len': 0}
  - L33: {'line': 33, 'type': 'for', 'target': 'test', 'iter': 'tests', 'body_len': 1, 'orelse_len': 0}
  - L42: {'line': 42, 'type': 'for', 'target': 'test', 'iter': 'success_tests', 'body_len': 1, 'orelse_len': 0}
  - L45: {'line': 45, 'type': 'for', 'target': 'test', 'iter': 'failed_tests', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L34: IF `test in success_tests`; body=1 else=1
- Exception handling:
  - L22: handlers=['Exception'] final=0
- Main call graph hints: `len`, `range`, `tuple`, `ExecuteResult`, `function_with_timeout`, `get_output`, `globals`
##### `evaluate(self, name, func, test, timeout)` (L50)
- Docstring: Evaluates the implementation on Human-Eval Python.

probably should be written in a dataset-agnostic way but not now
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L66: `True`
  - L68: `False`
- Exception handling:
  - L62: handlers=['Exception'] final=0
- Main call graph hints: `function_with_timeout`, `globals`

### Functions
#### `get_call_str(assert_statement)` (L70)
- Inputs: parameters `get_call_str(assert_statement)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L77: `astunparse.unparse(call_str).strip()`
- Exception handling:
  - L72: handlers=['Exception'] final=0
- Main call graph hints: `ast.parse`, `astunparse.unparse.strip`, `astunparse.unparse`
#### `get_output(func, assert_statement, timeout)` (L79)
- Inputs: parameters `get_output(func, assert_statement, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L84: `output`
  - L86: `'TIMEOUT'`
  - L88: `str(e)`
- Exception handling:
  - L80: handlers=['TimeoutError', 'Exception'] final=0
- Main call graph hints: `exec`, `get_call_str`, `function_with_timeout`, `globals`, `str`

---

## File: `programming/executors/rs_executor.py`

**Lines:** 373  

### Imports
- `import os`
- `import signal`
- `import subprocess`
- `import json`
- `from .executor_utils import timeout_handler`
- `from .executor_types import ExecuteResult, Executor`
- `from typing import List, Tuple, Optional`

### Module assignments
- L12: `cargo_harness_dir = os.path.join(os.path.dirname( os.path.realpath(__file__)), "cargo_harness")`
- L211: `assert_no_panic = r""" macro_rules! assert_eq_nopanic { ($left:expr, $right:expr) => { std::panic::catch_unwind(|| { assert_eq!($left, $right); }).unwrap_or_else(|_| {}); }; () => {}; } """`

### Prompt-like assignments
- L363 `test_compiletime`: `test_compiletime = r""" {"reason":"compiler-message","package_id":"testing 0.1.0 (path+file:///home/elleven/Downloads/testing)","manifest_path":"/home/elleven/Downloads/testing/Cargo.toml","target":{"kind":["bin"],"crate_types":["bin"],"name":"testing","src_path":"/home/elleven/Downloads/testing/...`

### Top-level logic
- L341 If: `if __name__ == "__main__": test_runtime = r""" Finished dev [unoptimized + debuginfo] target(s) in 0.00s Running `target/debug/testing` thread 'main' panicked at 'assertion failed: `(left == right)` left: `1`, right: `2`', src/main.rs:11:5 note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace thread 'main' panicked at 'assertion failed: `(left == right)` left: `3`, right: `2`', src/main.rs:12:5 thread 'main' panicked at 'assertion failed: `(left == right)` left: `[5, -...`

### Classes
#### Class `RsExecutor` L87 bases=['Executor']
##### `execute(self, func, tests, timeout)` (L88)
- Inputs: parameters `execute(self, func, tests, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L159: `ExecuteResult(is_passing, feedback, tuple(state))`
  - L110: `ExecuteResult(False, err_str, state)`
- Loops:
  - L115: {'line': 115, 'type': 'for', 'target': 'i', 'iter': 'range(num_tests)', 'body_len': 7, 'orelse_len': 0}
  - L144: {'line': 144, 'type': 'for', 'target': '(i, (passed, output))', 'iter': 'enumerate(tests_res)', 'body_len': 3, 'orelse_len': 0}
  - L107: {'line': 107, 'type': 'for', 'target': 'err', 'iter': 'errs', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L101: IF `len(errs) > 0`; body=5 else=0
  - L125: IF `res is None`; body=2 else=0
  - L131: IF `len(errs) > 0`; body=2 else=0
  - L146: IF `passed`; body=1 else=1
- I/O/env/executor calls:
  - L95: `write_to_file`
  - L121: `write_to_file`
- Main call graph hints: `create_temp_project`, `write_to_file`, `run_with_timeout`, `grab_compile_errs`, `len`, `range`, `os.system`, `enumerate`, `ExecuteResult`, `tuple`, `grab_runtime_errs`, `tests_res.append`, `state.append`, `str`
##### `evaluate(self, name, func, test, timeout)` (L161)
- Docstring: Evaluates the implementation on Human-Eval Rust (MultiPL-E generated,

Federico Cassano, John Gouwar, Daniel Nguyen, Sydney Nguyen, Luna Phipps-Costin, Donald Pinckney, Ming-Ho Yee, Yangtian Zi, Carolyn Jane Anderson, Molly Q Feldman, Arjun Guha, Michael Greenberg, Abhinav Jangda ).
If you use this function please cite:
@misc{cassano2022multiple,
  title={MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation}, 
  author={Federico Cassano and John Gouwar and Daniel Nguyen and Sydney Nguyen and Luna Phipps-Costin and Donald Pinckney and Ming-Ho Yee and Yangtian Zi and Carolyn Jane Anderson and Molly Q Feldman and Arjun Guha and Michael Greenberg and Abhinav Jangda},
  year={2022},
  eprint={2208.08227},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
})

TODO: do it actually
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L191: `False`
  - L200: `False`
  - L208: `len(errs) == 0`
  - L205: `False`
- Decisions / conditions:
  - L187: IF `len(errs) > 0`; body=3 else=0
  - L198: IF `res is None`; body=2 else=4
  - L203: IF `len(errs) > 0`; body=2 else=0
- I/O/env/executor calls:
  - L180: `write_to_file_toplevel`
- Main call graph hints: `create_temp_project`, `print`, `write_to_file_toplevel`, `run_with_timeout`, `grab_compile_errs`, `os.system`, `len`, `grab_runtime_errs`
#### Class `CompileErr` L248 bases=[]
##### `__init__(self, rendered)` (L249)
- Inputs: parameters `__init__(self, rendered)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `__str__(self)` (L252)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L253: `self.rendered`
##### `__repr__(self)` (L255)
- Inputs: parameters `__repr__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L256: `'{' + str(self) + '}'`
- Main call graph hints: `str`
#### Class `RuntimeErr` L259 bases=[]
##### `__init__(self, left, right, line, column, panic_reason)` (L260)
- Inputs: parameters `__init__(self, left, right, line, column, panic_reason)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `__str__(self)` (L269)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L271: `f'assertion failed: {self.left} == {self.right}'`
  - L273: `self.panic_reason`
- Decisions / conditions:
  - L270: IF `self.left is not None and self.right is not None`; body=1 else=1
##### `__repr__(self)` (L275)
- Inputs: parameters `__repr__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L276: `'{' + str(self) + '}'`
- Main call graph hints: `str`

### Functions
#### `create_temp_project()` (L16)
- Inputs: parameters `create_temp_project()` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L30: `(temp_dir, main_path)`
- Decisions / conditions:
  - L24: IF `os.path.exists(temp_dir)`; body=1 else=0
- Main call graph hints: `os.getpid`, `os.urandom.hex`, `os.path.exists`, `os.mkdir`, `os.system`, `os.path.join`, `os.urandom`
#### `write_to_file(path, code)` (L33)
- Inputs: parameters `write_to_file(path, code)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L38: IF `os.path.exists(path)`; body=1 else=0
- I/O/env/executor calls:
  - L41: `open`
  - L42: `f.write`
- Main call graph hints: `os.path.exists`, `os.remove`, `open`, `f.write`, `indent_code`
#### `write_to_file_toplevel(path, code)` (L45)
- Inputs: parameters `write_to_file_toplevel(path, code)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L47: IF `os.path.exists(path)`; body=1 else=0
- I/O/env/executor calls:
  - L50: `open`
  - L51: `f.write`
- Main call graph hints: `os.path.exists`, `os.remove`, `open`, `f.write`
#### `run_with_timeout(cmd, tmp_cargo_path, timeout, print_debug)` (L54)
- Docstring: Runs the given command with a timeout. Produces a tuple of stdout and stderr.
If the command times out, returns None.
- Inputs: parameters `run_with_timeout(cmd, tmp_cargo_path, timeout, print_debug)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L84: `(out, err)`
  - L72: `None`
- Decisions / conditions:
  - L77: IF `print_debug`; body=5 else=0
- Exception handling:
  - L66: handlers=['TimeoutError'] final=0
- I/O/env/executor calls:
  - L64: `subprocess.Popen`
- Main call graph hints: `signal.signal`, `signal.alarm`, `subprocess.Popen`, `out.decode`, `err.decode`, `p.communicate`, `print`, `p.kill`
#### `transform_asserts(code)` (L223)
- Docstring: Transform all asserts into assert_eq_nopanic! asserts, inserting the macro
definition at the top of the code.
- Inputs: parameters `transform_asserts(code)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L229: `assert_no_panic + code`
- Main call graph hints: `code.replace`
#### `revert_asserts(code)` (L232)
- Docstring: Revert all assert_eq_nopanic! asserts back into assert_eq! asserts.
- Inputs: parameters `revert_asserts(code)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L238: `normal[len(assert_no_panic):]`
- Main call graph hints: `code.replace`, `len`
#### `indent_code(code, spaces)` (L241)
- Docstring: Indent the code by the given number of spaces.
- Inputs: parameters `indent_code(code, spaces)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L245: `'\n'.join([' ' * spaces + line for line in code.splitlines()])`
- Main call graph hints: `Constant.join`, `code.splitlines`
#### `grab_compile_errs(inp)` (L281)
- Inputs: parameters `grab_compile_errs(inp)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L294: `objs`
- Loops:
  - L284: {'line': 284, 'type': 'for', 'target': 'line', 'iter': 'inp.splitlines()', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L285: IF `line == ''`; body=1 else=0
  - L288: IF `o is not None and o['reason'] == 'compiler-message' and (o['message']['level'] == 'error') and (o['message']['spans'] != [])`; body=2 else=0
- I/O/env/executor calls:
  - L287: `json.loads`
- Main call graph hints: `inp.splitlines`, `json.loads`, `objs.append`, `CompileErr`
#### `grab_runtime_errs(inp)` (L300)
- Inputs: parameters `grab_runtime_errs(inp)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L338: `failed_asserts`
- Loops:
  - L305: {'line': 305, 'type': 'for', 'target': 'line', 'iter': 'split', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L335: IF `panic_reason is not None`; body=1 else=0
  - L306: IF `'fatal runtime' in line`; body=2 else=1
  - L310: IF `'panicked at' in line`; body=3 else=1
  - L313: IF `'src/main.rs' in line`; body=1 else=0
  - L316: IF `'left:' in line`; body=3 else=1
  - L318: IF `len(split) < 2`; body=1 else=0
  - L321: IF `'right:' in line`; body=9 else=0
  - L323: IF `len(split) < 2`; body=1 else=0
- Main call graph hints: `inp.splitlines`, `failed_asserts.append`, `line.index`, `RuntimeErr`, `line.split`, `len`, `int`, `fileinto.split`

---

## File: `programming/generators/__init__.py`

**Lines:** 5  

### Imports
- `from .py_generate import PyGenerator`
- `from .rs_generate import RsGenerator`
- `from .factory import generator_factory, model_factory`
- `from .model import ModelBase, GPT4, GPT35`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming/generators/factory.py`

**Lines:** 36  

### Imports
- `from .py_generate import PyGenerator`
- `from .rs_generate import RsGenerator`
- `from .go_generate import GoGenerator`
- `from .generator_types import Generator`
- `from .model import CodeLlama, ModelBase, GPT4, GPT35, StarChat, GPTDavinci`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `generator_factory(lang)` (L8)
- Inputs: parameters `generator_factory(lang)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L10: `PyGenerator()`
  - L12: `RsGenerator()`
  - L14: `GoGenerator()`
- Decisions / conditions:
  - L9: IF `lang == 'py' or lang == 'python'`; body=1 else=1
  - L11: IF `lang == 'rs' or lang == 'rust'`; body=1 else=1
  - L13: IF `lang == 'go' or lang == 'golang'`; body=1 else=1
- Main call graph hints: `PyGenerator`, `RsGenerator`, `GoGenerator`, `ValueError`
#### `model_factory(model_name)` (L19)
- Inputs: parameters `model_factory(model_name)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L21: `GPT4()`
  - L23: `GPT35()`
  - L25: `StarChat()`
  - L31: `CodeLlama(**kwargs)`
  - L33: `GPTDavinci(model_name)`
- Decisions / conditions:
  - L20: IF `model_name == 'gpt-4'`; body=1 else=1
  - L22: IF `model_name == 'gpt-3.5-turbo-0613'`; body=1 else=1
  - L24: IF `model_name == 'starchat'`; body=1 else=1
  - L26: IF `model_name.startswith('codellama')`; body=3 else=1
  - L29: IF `'-' in model_name`; body=1 else=0
  - L32: IF `model_name.startswith('text-davinci')`; body=1 else=1
- LLM/model/env calls:
  - L21: `GPT4`
  - L23: `GPT35`
  - L25: `StarChat`
  - L26: `model_name.startswith`
  - L32: `model_name.startswith`
  - L33: `GPTDavinci`
  - L30: `model_name.split`
- Main call graph hints: `GPT4`, `GPT35`, `StarChat`, `model_name.startswith`, `CodeLlama`, `GPTDavinci`, `ValueError`, `model_name.split`

---

## File: `programming/generators/generator_types.py`

**Lines:** 34  

### Imports
- `from typing import List, Optional, Union`
- `from abc import abstractmethod, ABC`
- `from generators.model import ModelBase`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `Generator` L7 bases=[]
##### `self_reflection(self, func, feedback, model)` (L9)
- Inputs: parameters `self_reflection(self, func, feedback, model)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` (L13)
- Inputs: parameters `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `internal_tests(self, func_sig, model, max_num_tests)` (L27)
- Inputs: parameters `internal_tests(self, func_sig, model, max_num_tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.

### Functions
- None

---

## File: `programming/generators/generator_utils.py`

**Lines:** 289  

### Imports
- `from generators.model import ModelBase, Message`
- `import random`
- `from typing import Union, List, Optional, Callable`

### Module assignments
- None

### Prompt-like assignments
- L128 `accumulated_context`: `accumulated_context = "\n\n".join( [f"[previous impl {i+1}]:\n{add_code_block(impl)}\n[unit test results from previous impl {i+1}]:\n{feedback}\n[reflection on previous impl {i+1}]:\n{reflection}" for i, (impl, feedback, reflection) in enumerate(zip(prev_func_impl, accumulated_feedback, accumulat...`
- L220 `prompt`: `prompt = f'{test_generation_completion_instruction}\n\nfunc signature:\n{func_sig}\nunit tests:'`
- L264 `reflection`: `reflection = model.generate( f'{self_reflection_completion_instruction}\n{add_code_block(func)}\n\n{feedback}\n\nExplanation:')`
- L34 `message`: `message = f"{reflection_few_shot}\n[previous impl]:\n{add_code_block(prev_func_impl)}\n\n[unit test results from previous impl]:\n{feedback}\n\n[reflection on previous impl]:\n{self_reflection}\n\n[improved impl]:\n{func_sig}"`
- L35 `prompt`: `prompt = f"{reflection_chat_instruction}\n{code_block_instruction}"`
- L38 `messages`: `messages = [ Message( role="system", content=prompt, ), Message( role="user", # TODO: check this content=reflection_few_shot, ), Message( role="assistant", content=add_code_block(prev_func_impl), ), Message( role="user", content=f"[unit test results from previous impl]:\n{feedback}\n\n[reflection...`
- L66 `system_prompt`: `system_prompt = f"{simple_chat_instruction}\n{code_block_instruction}"`
- L68 `messages`: `messages = [ Message( role="system", content=f"{simple_chat_instruction}\n{code_block_instruction}", ), Message( role="user", content=func_sig, ), ]`
- L81 `prompt`: `prompt = f"{reflection_completion_instruction}\n{add_code_block(prev_func_impl)}\n\nunit tests:\n{feedback}\n\nhint:\n{self_reflection}\n\n# improved implementation\n{func_sig}\n{code_block_instruction}"`
- L82 `func_bodies`: `func_bodies = model.generate( prompt, num_comps=num_comps, temperature=temperature)`
- L85 `prompt`: `prompt = f"{simple_completion_instruction}\n{func_sig}\n{code_block_instruction}"`
- L86 `func_bodies`: `func_bodies = model.generate( prompt, num_comps=num_comps, temperature=temperature)`
- L136 `messages`: `messages = [ Message(role="system", content=f"{reflection_chat_instruction}\n{code_block_instruction}"), Message(role="user", content=reflection_few_shot) ]`
- L146 `prompt`: `prompt = "\n".join([message.content for message in messages])`
- L147 `message`: `message = (f"{reflection_few_shot}\n{accumulated_context}\n\n[improved impl]:\n{func_sig}")`
- L152 `system_prompt`: `system_prompt = f"{simple_chat_instruction}\n{code_block_instruction}"`
- L154 `messages`: `messages = [ Message(role="system", content=f"{simple_chat_instruction}\n{code_block_instruction}"), Message(role="user", content=func_sig) ]`
- L161 `prompt`: `prompt = f"{reflection_completion_instruction}\n{accumulated_context}\n\n# improved implementation\n{func_sig}\n{code_block_instruction}"`
- L162 `func_bodies`: `func_bodies = model.generate(prompt, num_comps=num_comps, temperature=temperature)`
- L165 `prompt`: `prompt = f"{simple_completion_instruction}\n{func_sig}\n{code_block_instruction}"`
- L166 `func_bodies`: `func_bodies = model.generate(prompt, num_comps=num_comps, temperature=temperature)`
- L195 `messages`: `messages = [ Message( role="system", content=test_generation_chat_instruction, ), Message( role="user", content=f"{test_generation_few_shot}\n\n[func signature]:\n{func_sig}\n\n[think]:" ) ]`
- L208 `messages`: `messages = [ Message( role="system", content=f"{test_generation_chat_instruction}\n\n{test_generation_few_shot}", ), Message( role="user", content=f"[func signature]:\n{func_sig}\n\n[unit tests]:", ) ]`
- L239 `messages`: `messages = [ Message( role="system", content=self_reflection_chat_instruction, ), Message( role="user", content=f'{self_reflection_few_shot}\n\n[function impl]:\n{add_code_block(func)}\n\n[unit test results]:\n{feedback}\n\n[self-reflection]:', ) ]`
- L249 `reflection`: `reflection = model.generate_chat(messages=messages)`
- L252 `messages`: `messages = [ Message( role="system", content=self_reflection_chat_instruction, ), Message( role="user", content=f'[function impl]:\n{add_code_block(func)}\n\n[unit test results]:\n{feedback}\n\n[self-reflection]:', ) ]`
- L262 `reflection`: `reflection = model.generate_chat(messages=messages)`

### Classes
- None

### Functions
#### `generic_generate_func_impl(func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, reflection_chat_instruction, reflection_few_shot, simple_chat_instruction, reflection_completion_instruction, simple_completion_instruction, code_block_instruction, parse_code_block, add_code_block)` (L7)
- Inputs: parameters `generic_generate_func_impl(func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, reflection_chat_instruction, reflection_few_shot, simple_chat_instruction, reflection_completion_instruction, simple_completion_instruction, code_block_instruction, parse_code_block, add_code_block)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L93: `func_body_str`
  - L98: `func_bodies`
- Decisions / conditions:
  - L25: IF `strategy != 'reflexion' and strategy != 'simple'`; body=1 else=0
  - L28: IF `strategy == 'reflexion' and (prev_func_impl is None or feedback is None or self_reflection is None)`; body=1 else=0
  - L32: IF `model.is_chat`; body=1 else=1
  - L89: IF `num_comps == 1`; body=4 else=3
  - L33: IF `strategy == 'reflexion'`; body=5 else=4
  - L80: IF `strategy == 'reflexion'`; body=2 else=2
- LLM/model/env calls:
  - L92: `print_generated_func_body`
  - L97: `print_generated_func_body`
  - L64: `model.generate_chat`
  - L78: `model.generate_chat`
  - L82: `model.generate`
  - L86: `model.generate`
- Main call graph hints: `ValueError`, `isinstance`, `parse_code_block`, `print_generated_func_body`, `print_messages`, `model.generate_chat`, `model.generate`, `Constant.join`, `Message`, `add_code_block`
#### `generate_with_accumulated_context(func_sig, model, strategy, prev_func_impl, accumulated_feedback, accumulated_reflection, num_comps, temperature, reflection_chat_instruction, reflection_few_shot, simple_chat_instruction, reflection_completion_instruction, simple_completion_instruction, code_block_instruction, parse_code_block, add_code_block)` (L101)
- Inputs: parameters `generate_with_accumulated_context(func_sig, model, strategy, prev_func_impl, accumulated_feedback, accumulated_reflection, num_comps, temperature, reflection_chat_instruction, reflection_few_shot, simple_chat_instruction, reflection_completion_instruction, simple_completion_instruction, code_block_instruction, parse_code_block, add_code_block)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L173: `func_body_str`
  - L178: `func_bodies`
- Loops:
  - L141: {'line': 141, 'type': 'for', 'target': '(impl, feedback, reflection)', 'iter': 'zip(prev_func_impl, accumulated_feedback, accumulated_reflection)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L120: IF `strategy != 'reflexion' and strategy != 'simple'`; body=1 else=0
  - L123: IF `strategy == 'reflexion' and (prev_func_impl is None or accumulated_feedback is None or accumulated_reflection is None)`; body=1 else=0
  - L133: IF `model.is_chat`; body=1 else=1
  - L169: IF `num_comps == 1`; body=4 else=3
  - L134: IF `strategy == 'reflexion'`; body=7 else=4
  - L160: IF `strategy == 'reflexion'`; body=3 else=3
- LLM/model/env calls:
  - L172: `print_generated_func_body`
  - L177: `print_generated_func_body`
  - L150: `model.generate_chat`
  - L158: `model.generate_chat`
  - L162: `model.generate`
  - L166: `model.generate`
- Main call graph hints: `Constant.join`, `ValueError`, `isinstance`, `parse_code_block`, `print_generated_func_body`, `zip`, `messages.append`, `print_messages`, `model.generate_chat`, `model.generate`, `enumerate`, `Message`, `add_code_block`
#### `generic_generate_internal_tests(func_sig, model, max_num_tests, test_generation_few_shot, test_generation_chat_instruction, test_generation_completion_instruction, parse_tests, is_syntax_valid, is_react)` (L181)
- Docstring: Generates tests for a function.
- Inputs: parameters `generic_generate_internal_tests(func_sig, model, max_num_tests, test_generation_few_shot, test_generation_chat_instruction, test_generation_completion_instruction, parse_tests, is_syntax_valid, is_react)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L225: `sample_n_random(valid_tests, max_num_tests)`
- Decisions / conditions:
  - L193: IF `model.is_chat`; body=1 else=2
  - L194: IF `is_react`; body=3 else=2
- LLM/model/env calls:
  - L221: `model.generate`
  - L205: `model.generate_chat`
  - L218: `model.generate_chat`
- Main call graph hints: `parse_tests`, `sample_n_random`, `model.generate`, `model.generate_chat`, `print`, `is_syntax_valid`, `Message`
#### `generic_generate_self_reflection(func, feedback, model, self_reflection_chat_instruction, self_reflection_completion_instruction, add_code_block, self_reflection_few_shot)` (L228)
- Inputs: parameters `generic_generate_self_reflection(func, feedback, model, self_reflection_chat_instruction, self_reflection_completion_instruction, add_code_block, self_reflection_few_shot)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L266: `reflection`
- Decisions / conditions:
  - L237: IF `model.is_chat`; body=1 else=1
  - L238: IF `self_reflection_few_shot is not None`; body=3 else=2
- LLM/model/env calls:
  - L264: `model.generate`
  - L249: `model.generate_chat`
  - L262: `model.generate_chat`
- Main call graph hints: `model.generate`, `model.generate_chat`, `print`, `Message`, `add_code_block`
#### `sample_n_random(items, n)` (L269)
- Docstring: Sample min(n, len(items)) random items from a list
- Inputs: parameters `sample_n_random(items, n)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L274: `random.sample(items, n)`
  - L273: `items`
- Decisions / conditions:
  - L272: IF `n >= len(items)`; body=1 else=0
- Main call graph hints: `random.sample`, `len`
#### `print_messages(system_message_text, user_message_text)` (L276)
- Inputs: parameters `print_messages(system_message_text, user_message_text)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `print`
#### `print_generated_func_body(func_body_str)` (L285)
- Inputs: parameters `print_generated_func_body(func_body_str)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `print`

---

## File: `programming/generators/go_generate.py`

**Lines:** 231  

### Imports
- `import re`
- `from generators.model import ModelBase`
- `from .generator_types import Generator`
- `from .generator_utils import generic_generate_func_impl, generic_generate_internal_tests, generic_generate_self_reflection, generate_with_accumulated_context`
- `from .parse import parse_code_block, add_code_block`
- `from typing import List, Optional, Union`

### Module assignments
- L9: `GO_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."`
- L10: `GO_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"`
- L11: `GO_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation...`
- L12: `USE_GO_CODEBLOCK_INSTRUCTION = "Use a Go code block to write your response. For example:\n```go\nfunc main() {\n fmt.Println(\"Hello, World!\")\n}\n```"`
- L14: `GO_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Go code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L15: `GO_REFLECTION_CHAT_INSTRUCTION = "You are an AI Go assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L16: `GO_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation."`
- L18: `GO_REFLECTION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```go func add(a, b int) int { // Given integers a and b, return the total value of a and b. return a - b } ``` [unit test results from previous impl]: Tested passed: Tests failed: lats_test.go:49: add(1, 2) = -1, want 3 lats_test.go:49: add(2, 3) = -1, want 5 [reflection on previous impl]: The implementation failed the test cases wher...`
- L48: `GO_TEST_GENERATION_FEW_SHOT = """For example: func signature: /// Add three numbers together. /// This function takes three numbers as input and returns the sum of the three numbers. func Add3Numbers(x int, y int, z int) int { unit tests: func TestAdd(t *testing.T) { assert := assert.New(t) assert.Equal(7, Add3Numbers(2, 3+rand.Intn(1000)*0, 2)) assert.Equal(15, Add3Numbers(5, 7, 3)) } """`
- L63: `GO_SELF_REFLECTION_FEW_SHOT = '''Example 1: [function impl]: ```Go func SortArray(array []int) []int { // Given an array of non-negative integers, return a copy of the given array after sorting, // you will sort the given array in ascending order if the sum( first index value, last index value) is odd, // or sort it in descending order if the sum( first index value, last index value) is even. /...`
- L119: `GO_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. You only responds with Go code, NOT ENGLISH. {GO_TEST_GENERATION_FEW_SHOT}"""`
- L123: `GO_TEST_GENERATION_CHAT_INSTRUCTION = """You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""`

### Prompt-like assignments
- L9 `GO_SIMPLE_COMPLETION_INSTRUCTION`: `GO_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."`
- L10 `GO_REFLECTION_COMPLETION_INSTRUCTION`: `GO_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"`
- L11 `GO_SELF_REFLECTION_COMPLETION_INSTRUCTION`: `GO_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when y...`
- L12 `USE_GO_CODEBLOCK_INSTRUCTION`: `USE_GO_CODEBLOCK_INSTRUCTION = "Use a Go code block to write your response. For example:\n```go\nfunc main() {\n fmt.Println(\"Hello, World!\")\n}\n```"`
- L14 `GO_SIMPLE_CHAT_INSTRUCTION`: `GO_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Go code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L15 `GO_REFLECTION_CHAT_INSTRUCTION`: `GO_REFLECTION_CHAT_INSTRUCTION = "You are an AI Go assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L16 `GO_SELF_REFLECTION_CHAT_INSTRUCTION`: `GO_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try...`
- L18 `GO_REFLECTION_FEW_SHOT_ADD`: `GO_REFLECTION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```go func add(a, b int) int { // Given integers a and b, return the total value of a and b. return a - b } ``` [unit test results from previous impl]: Tested passed: Tests failed: lats_test.go:49: add(1, 2) = -1, want 3 lats_test.go:49:...`
- L48 `GO_TEST_GENERATION_FEW_SHOT`: `GO_TEST_GENERATION_FEW_SHOT = """For example: func signature: /// Add three numbers together. /// This function takes three numbers as input and returns the sum of the three numbers. func Add3Numbers(x int, y int, z int) int { unit tests: func TestAdd(t *testing.T) { assert := assert.New(t) asser...`
- L63 `GO_SELF_REFLECTION_FEW_SHOT`: `GO_SELF_REFLECTION_FEW_SHOT = '''Example 1: [function impl]: ```Go func SortArray(array []int) []int { // Given an array of non-negative integers, return a copy of the given array after sorting, // you will sort the given array in ascending order if the sum( first index value, last index value) i...`
- L119 `GO_TEST_GENERATION_COMPLETION_INSTRUCTION`: `GO_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. You only responds with Go code, NOT ENGLISH. {GO_TEST_GENERATION_FEW_SHOT}"""`
- L123 `GO_TEST_GENERATION_CHAT_INSTRUCTION`: `GO_TEST_GENERATION_CHAT_INSTRUCTION = """You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""`

### Classes
#### Class `GoGenerator` L142 bases=['Generator']
##### `self_reflection(self, func, feedback, model)` (L143)
- Inputs: parameters `self_reflection(self, func, feedback, model)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L144: `generic_generate_self_reflection(func=func, feedback=feedback, model=model, self_reflection_chat_instruction=GO_SELF_REFLECTION_CHAT_INSTRUCTION, self_reflection_completion_instruction=GO_SELF_REFLECTION_COMPLETION_INSTRUCTION, add_code_block=lambda x: add_code_block(x, 'Go'), self_reflection_few_shot=GO_SELF_REFLECTION_FEW_SHOT)`
- LLM/model/env calls:
  - L144: `generic_generate_self_reflection`
- Main call graph hints: `generic_generate_self_reflection`, `add_code_block`
##### `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, acc_feedback, acc_reflection)` (L154)
- Inputs: parameters `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, acc_feedback, acc_reflection)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L168: `generate_with_accumulated_context(func_sig=func_sig, model=model, strategy='reflexion', prev_func_impl=prev_func_impl, accumulated_feedback=acc_feedback, accumulated_reflection=acc_reflection, num_comps=num_comps, temperature=temperature, reflection_chat_instruction=GO_REFLECTION_CHAT_INSTRUCTION, simple_chat_instruction=GO_SIMPLE_CHAT_INSTRUCTI...`
  - L187: `generic_generate_func_impl(func_sig=func_sig, model=model, strategy=strategy, prev_func_impl=prev_func_impl, feedback=feedback, self_reflection=self_reflection, num_comps=num_comps, temperature=temperature, reflection_chat_instruction=GO_REFLECTION_CHAT_INSTRUCTION, simple_chat_instruction=GO_SIMPLE_CHAT_INSTRUCTION, reflection_completion_instru...`
- Decisions / conditions:
  - L167: IF `strategy == 'mcts'`; body=1 else=1
- LLM/model/env calls:
  - L168: `generate_with_accumulated_context`
  - L187: `generic_generate_func_impl`
- Main call graph hints: `generate_with_accumulated_context`, `generic_generate_func_impl`, `parse_code_block`, `add_code_block`
##### `internal_tests(self, func_sig, model, max_num_tests)` (L206)
- Inputs: parameters `internal_tests(self, func_sig, model, max_num_tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L221: `generic_generate_internal_tests(func_sig=func_sig, model=model, max_num_tests=max_num_tests, test_generation_few_shot=GO_TEST_GENERATION_FEW_SHOT, test_generation_chat_instruction=GO_TEST_GENERATION_CHAT_INSTRUCTION, test_generation_completion_instruction=GO_TEST_GENERATION_COMPLETION_INSTRUCTION, parse_tests=parse_tests, is_syntax_valid=is_synt...`
  - L215: `matches`
  - L217: `True`
- LLM/model/env calls:
  - L221: `generic_generate_internal_tests`
- Main call graph hints: `generic_generate_internal_tests`, `re.findall`

### Functions
#### `dump_tests(tests)` (L126)
- Docstring: Dumps the tests to a string.
- Inputs: parameters `dump_tests(tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L130: `'\n'.join(tests)`
- Main call graph hints: `Constant.join`
#### `parse_tests(tests)` (L133)
- Docstring: Parses the tests from a string.
- Inputs: parameters `parse_tests(tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L137: `[test.strip() for test in tests.splitlines() if 'assert' in test]`
- Main call graph hints: `test.strip`, `tests.splitlines`

---

## File: `programming/generators/model.py`

**Lines:** 264  

### Imports
- `from typing import List, Union, Optional, Literal`
- `import dataclasses`
- `from tenacity import ( retry, stop_after_attempt, # type: ignore wait_random_exponential, # type: ignore )`
- `import openai`

### Module assignments
- L11: `MessageRole = Literal["system", "user", "assistant"]`

### Prompt-like assignments
- L11 `MessageRole`: `MessageRole = Literal["system", "user", "assistant"]`
- L37 `response`: `response = openai.Completion.create( model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=stop_strs, n=num_comps, )`
- L204 `DEFAULT_SYSTEM_PROMPT`: `DEFAULT_SYSTEM_PROMPT = """\ You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially u...`
- L139 `outputs`: `outputs = self.model.generate( prompt, max_new_tokens=min( max_tokens, self.model.config.max_position_embeddings), use_cache=True, do_sample=True, temperature=temperature, top_p=0.95, eos_token_id=self.eos_token_id, num_return_sequences=num_comps, )`
- L240 `messages_tokens`: `messages_tokens: List[int] = sum( [ self.tokenizer.encode( f"{self.B_INST} {(prompt.content).strip()} {self.E_INST} {(answer.content).strip()} ", ) for prompt, answer in zip( messages[::2], messages[1::2], ) ], [], )`
- L227 `messages`: `messages = [ Message(role="system", content=self.DEFAULT_SYSTEM_PROMPT) ] + messages`

### Classes
#### Class `Message` L15 bases=[]
#### Class `ModelBase` L78 bases=[]
##### `__init__(self, name)` (L79)
- Inputs: parameters `__init__(self, name)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `__repr__(self)` (L83)
- Inputs: parameters `__repr__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L84: `f'{self.name}'`
##### `generate_chat(self, messages, max_tokens, temperature, num_comps)` (L86)
- Inputs: parameters `generate_chat(self, messages, max_tokens, temperature, num_comps)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` (L89)
- Inputs: parameters `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
#### Class `GPTChat` L93 bases=['ModelBase']
##### `__init__(self, model_name)` (L94)
- Inputs: parameters `__init__(self, model_name)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `generate_chat(self, messages, max_tokens, temperature, num_comps)` (L98)
- Inputs: parameters `generate_chat(self, messages, max_tokens, temperature, num_comps)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L99: `gpt_chat(self.name, messages, max_tokens, temperature, num_comps)`
- LLM/model/env calls:
  - L99: `gpt_chat`
- Main call graph hints: `gpt_chat`
#### Class `GPT4` L102 bases=['GPTChat']
##### `__init__(self)` (L103)
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `super`
#### Class `GPT35` L107 bases=['GPTChat']
##### `__init__(self)` (L108)
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `super`
#### Class `GPTDavinci` L112 bases=['ModelBase']
##### `__init__(self, model_name)` (L113)
- Inputs: parameters `__init__(self, model_name)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` (L116)
- Inputs: parameters `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L117: `gpt_completion(self.name, prompt, max_tokens, stop_strs, temperature, num_comps)`
- LLM/model/env calls:
  - L117: `gpt_completion`
- Main call graph hints: `gpt_completion`
#### Class `HFModelBase` L120 bases=['ModelBase']
- Docstring: Base for huggingface chat models
##### `__init__(self, model_name, model, tokenizer, eos_token_id)` (L125)
- Inputs: parameters `__init__(self, model_name, model, tokenizer, eos_token_id)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `generate_chat(self, messages, max_tokens, temperature, num_comps)` (L132)
- Inputs: parameters `generate_chat(self, messages, max_tokens, temperature, num_comps)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L158: `outs[0]`
  - L160: `outs`
- Loops:
  - L153: {'line': 153, 'type': 'for', 'target': '(i, out)', 'iter': 'enumerate(outs)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L134: IF `temperature < 0.0001`; body=1 else=0
  - L157: IF `len(outs) == 1`; body=1 else=1
- LLM/model/env calls:
  - L139: `self.model.generate`
- Main call graph hints: `self.prepare_prompt`, `self.model.generate`, `self.tokenizer.batch_decode`, `isinstance`, `enumerate`, `self.extract_output`, `len`, `min`
##### `prepare_prompt(self, messages)` (L162)
- Inputs: parameters `prepare_prompt(self, messages)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `extract_output(self, output)` (L165)
- Inputs: parameters `extract_output(self, output)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
#### Class `StarChat` L169 bases=['HFModelBase']
##### `__init__(self)` (L170)
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- LLM/model/env calls:
  - L173: `AutoModelForCausalLM.from_pretrained`
- Main call graph hints: `AutoModelForCausalLM.from_pretrained`, `AutoTokenizer.from_pretrained`, `super.__init__`, `super`
##### `prepare_prompt(self, messages)` (L183)
- Inputs: parameters `prepare_prompt(self, messages)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L190: `self.tokenizer.encode(prompt, return_tensors='pt').to(self.model.device)`
- Loops:
  - L185: {'line': 185, 'type': 'for', 'target': '(i, message)', 'iter': 'enumerate(messages)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L187: IF `i == len(messages) - 1`; body=1 else=0
- Main call graph hints: `enumerate`, `self.tokenizer.encode.to`, `self.tokenizer.encode`, `len`
##### `extract_output(self, output)` (L192)
- Inputs: parameters `extract_output(self, output)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L197: `out`
- Decisions / conditions:
  - L194: IF `out.endswith('<|end|>')`; body=1 else=0
- Main call graph hints: `out.endswith`, `output.split`, `len`
#### Class `CodeLlama` L200 bases=['HFModelBase']
##### `__init__(self, version)` (L209)
- Inputs: parameters `__init__(self, version)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- LLM/model/env calls:
  - L218: `AutoModelForCausalLM.from_pretrained`
- Main call graph hints: `AutoTokenizer.from_pretrained`, `AutoModelForCausalLM.from_pretrained`, `super.__init__`, `super`
##### `prepare_prompt(self, messages)` (L225)
- Inputs: parameters `prepare_prompt(self, messages)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L259: `torch.tensor([messages_tokens]).to(self.model.device)`
- Decisions / conditions:
  - L226: IF `messages[0].role != 'system'`; body=1 else=0
- Main call graph hints: `sum`, `self.tokenizer.encode`, `torch.tensor.to`, `all`, `Message`, `torch.tensor`, `zip`, `messages[...].content.strip`, `prompt.content.strip`, `answer.content.strip`
##### `extract_output(self, output)` (L261)
- Inputs: parameters `extract_output(self, output)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L263: `out`
- Main call graph hints: `output.split[...].split[...].strip`, `output.split[...].split`, `output.split`

### Functions
#### `message_to_str(message)` (L20)
- Inputs: parameters `message_to_str(message)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L21: `f'{message.role}: {message.content}'`
#### `messages_to_str(messages)` (L24)
- Inputs: parameters `messages_to_str(messages)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L25: `'\n'.join([message_to_str(message) for message in messages])`
- Main call graph hints: `Constant.join`, `message_to_str`
#### `gpt_completion(model, prompt, max_tokens, stop_strs, temperature, num_comps)` (L29)
- Inputs: parameters `gpt_completion(model, prompt, max_tokens, stop_strs, temperature, num_comps)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L51: `[choice.text for choice in response.choices]`
  - L49: `response.choices[0].text`
- Decisions / conditions:
  - L48: IF `num_comps == 1`; body=1 else=0
- LLM/model/env calls:
  - L37: `openai.Completion.create`
- I/O/env/executor calls:
  - L37: `openai.Completion.create`
- Main call graph hints: `retry`, `openai.Completion.create`, `wait_random_exponential`, `stop_after_attempt`
#### `gpt_chat(model, messages, max_tokens, temperature, num_comps)` (L55)
- Inputs: parameters `gpt_chat(model, messages, max_tokens, temperature, num_comps)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L75: `[choice.message.content for choice in response.choices]`
  - L73: `response.choices[0].message.content`
- Decisions / conditions:
  - L72: IF `num_comps == 1`; body=1 else=0
- LLM/model/env calls:
  - L62: `openai.ChatCompletion.create`
- I/O/env/executor calls:
  - L62: `openai.ChatCompletion.create`
- Main call graph hints: `retry`, `openai.ChatCompletion.create`, `print`, `wait_random_exponential`, `stop_after_attempt`, `dataclasses.asdict`

---

## File: `programming/generators/parse.py`

**Lines:** 107  

### Imports
- `import re`
- `from typing import Optional`

### Module assignments
- None

### Prompt-like assignments
- L77 `CODE`: `CODE = """def total_match(lst1: List[str], lst2: List[str]) -> List[str]: \"\"\" Write a function that accepts two lists of strings and returns the list that has total number of chars in the all strings of the list less than the other list. if the two lists have the same number of chars, return t...`

### Top-level logic
- L52 If: `if __name__ == "__main__": CODE = """ aldaas sub_parser = parser.add_subparsers().add_parser("frf a") def my_wonderful_func(): def useless_helper(): return 1 if 1: return 1 else: return ( 1, 2, ) sadsadsa 2023-08-04dsa dsa def bleh(): return aaa """ print(parse_code_block(CODE, "python")) CODE = """def total_match(lst1: List[str], lst2: List[str]) -> List[str]: \"\"\" Write a function that accepts two lists of strings and returns the list that has total number of chars in the all strings of t...`

### Classes
- None

### Functions
#### `parse_code_block(string, lang)` (L5)
- Inputs: parameters `parse_code_block(string, lang)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L18: `parse_first_func(string, lang)`
  - L10: `match.group(1)`
  - L16: `match.group(1)`
- Decisions / conditions:
  - L9: IF `match`; body=1 else=0
  - L15: IF `match`; body=1 else=0
- Main call graph hints: `re.search`, `parse_first_func`, `match.group`
#### `parse_first_func(code, lang)` (L21)
- Inputs: parameters `parse_first_func(code, lang)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L45: `'\n'.join(code_lines[def_i:last_i + 1]).rstrip('[/PYTHON]')`
  - L43: `None`
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(i, line)', 'iter': 'enumerate(code_lines)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L39: IF `last_i == 0`; body=1 else=0
  - L42: IF `def_i == -1`; body=1 else=0
  - L28: IF `line.startswith('def ')`; body=1 else=1
  - L35: IF `line == '' and def_i != -1 and got_return`; body=2 else=0
  - L29: IF `def_i == -1`; body=1 else=1
  - L33: IF `'return' in line and def_i != -1`; body=1 else=0
- Main call graph hints: `code.split`, `enumerate`, `Constant.join.rstrip`, `line.startswith`, `len`, `Constant.join`
#### `add_code_block(string, lang)` (L48)
- Inputs: parameters `add_code_block(string, lang)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L49: `f'```{lang}\n{string}\n```'`

---

## File: `programming/generators/py_generate.py`

**Lines:** 405  

### Imports
- `from generators.model import ModelBase, message_to_str`
- `from .generator_types import Generator`
- `from .generator_utils import generic_generate_func_impl, generic_generate_internal_tests, generic_generate_self_reflection, generate_with_accumulated_context`
- `from typing import Optional, List, Union`
- `import ast`
- `import re`
- `from .parse import parse_code_block, add_code_block`

### Module assignments
- L10: `PY_SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."`
- L11: `PY_REFLEXION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"`
- L12: `PY_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation...`
- L13: `USE_PYTHON_CODEBLOCK_INSTRUCTION = "Use a Python code block to write your response. For example:\n```python\nprint('Hello world!')\n```"`
- L15: `PY_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with python code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L16: `PY_SIMPLE_CHAT_INSTRUCTION_V2 = "You are an AI that only responds with only python code. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L17: `PY_REFLEXION_CHAT_INSTRUCTION = "You are an AI Python assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L18: `PY_REFLEXION_CHAT_INSTRUCTION_V2 = "You are an AI Python assistant. You will be given your previous implementation of a function, a series of unit tests results, and your self-reflection on your previous implementation. Write your full implementation (restate the function signature)."`
- L19: `PY_REFLEXION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```python def add(a: int, b: int) -> int: """ Given integers a and b, return the total value of a and b. """ return a - b ``` [unit test results from previous impl]: Tested passed: Tests failed: assert add(1, 2) == 3 # output: -1 assert add(1, 2) == 4 # output: -1 [reflection on previous impl]: The implementation failed the test cases w...`
- L49: `PY_REFLEXION_FEW_SHOT = '''Example 1: [previous impl]: ```python from typing import * def fullJustify(words: List[str], maxWidth: int) -> List[str]: """ Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can i...`
- L151: `PY_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Python programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation."`
- L152: `PY_SELF_REFLECTION_CHAT_INSTRUCTION_V2 = "You are a Python programming assistant. You will be given a function implementation and a series of unit test results. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as guidance when you try again later. Only provide the few sentence description in your answer, not the impl...`
- L153: `PY_SELF_REFLECTION_FEW_SHOT = """Example 1: [function impl]: ```python def longest_subarray_with_sum_limit(nums: List[int], target: int) -> List[int]: n = len(nums) left, right = 0, 0 max_length = 0 current_sum = 0 result = [] while right < n: current_sum += nums[right] while current_sum > target: current_sum -= nums[left] left += 1 if right - left + 1 >= max_length: max_length = right - left +...`
- L224: `PY_TEST_GENERATION_FEW_SHOT = """Examples: func signature: def add3Numbers(x, y, z): \"\"\" Add three numbers together. This function takes three numbers as input and returns the sum of the three numbers. \"\"\" unit tests: assert add3Numbers(1, 2, 3) == 6 assert add3Numbers(-1, 2, 3) == 4 assert add3Numbers(1, -2, 3) == 2 assert add3Numbers(1, 2, -3) == 0 assert add3Numbers(-3, -2, -1) == -6 a...`
- L239: `PY_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. {PY_TEST_GENERATION_FEW_SHOT}"""`
- L243: `PY_TEST_GENERATION_CHAT_INSTRUCTION = """You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""`
- L328: `DUMMY_FUNC_SIG = "def func():"`
- L329: `DUMMY_FUNC_CALL = "func()"`

### Prompt-like assignments
- L10 `PY_SIMPLE_COMPLETION_INSTRUCTION`: `PY_SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."`
- L11 `PY_REFLEXION_COMPLETION_INSTRUCTION`: `PY_REFLEXION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"`
- L12 `PY_SELF_REFLECTION_COMPLETION_INSTRUCTION`: `PY_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when y...`
- L13 `USE_PYTHON_CODEBLOCK_INSTRUCTION`: `USE_PYTHON_CODEBLOCK_INSTRUCTION = "Use a Python code block to write your response. For example:\n```python\nprint('Hello world!')\n```"`
- L15 `PY_SIMPLE_CHAT_INSTRUCTION`: `PY_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with python code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L16 `PY_SIMPLE_CHAT_INSTRUCTION_V2`: `PY_SIMPLE_CHAT_INSTRUCTION_V2 = "You are an AI that only responds with only python code. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L17 `PY_REFLEXION_CHAT_INSTRUCTION`: `PY_REFLEXION_CHAT_INSTRUCTION = "You are an AI Python assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L18 `PY_REFLEXION_CHAT_INSTRUCTION_V2`: `PY_REFLEXION_CHAT_INSTRUCTION_V2 = "You are an AI Python assistant. You will be given your previous implementation of a function, a series of unit tests results, and your self-reflection on your previous implementation. Write your full implementation (restate the function signature)."`
- L19 `PY_REFLEXION_FEW_SHOT_ADD`: `PY_REFLEXION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```python def add(a: int, b: int) -> int: """ Given integers a and b, return the total value of a and b. """ return a - b ``` [unit test results from previous impl]: Tested passed: Tests failed: assert add(1, 2) == 3 # output: -1 assert a...`
- L49 `PY_REFLEXION_FEW_SHOT`: `PY_REFLEXION_FEW_SHOT = '''Example 1: [previous impl]: ```python from typing import * def fullJustify(words: List[str], maxWidth: int) -> List[str]: """ Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) ...`
- L151 `PY_SELF_REFLECTION_CHAT_INSTRUCTION`: `PY_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Python programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you...`
- L152 `PY_SELF_REFLECTION_CHAT_INSTRUCTION_V2`: `PY_SELF_REFLECTION_CHAT_INSTRUCTION_V2 = "You are a Python programming assistant. You will be given a function implementation and a series of unit test results. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as guida...`
- L153 `PY_SELF_REFLECTION_FEW_SHOT`: `PY_SELF_REFLECTION_FEW_SHOT = """Example 1: [function impl]: ```python def longest_subarray_with_sum_limit(nums: List[int], target: int) -> List[int]: n = len(nums) left, right = 0, 0 max_length = 0 current_sum = 0 result = [] while right < n: current_sum += nums[right] while current_sum > target...`
- L224 `PY_TEST_GENERATION_FEW_SHOT`: `PY_TEST_GENERATION_FEW_SHOT = """Examples: func signature: def add3Numbers(x, y, z): \"\"\" Add three numbers together. This function takes three numbers as input and returns the sum of the three numbers. \"\"\" unit tests: assert add3Numbers(1, 2, 3) == 6 assert add3Numbers(-1, 2, 3) == 4 assert...`
- L239 `PY_TEST_GENERATION_COMPLETION_INSTRUCTION`: `PY_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. {PY_TEST_GENERATION_FEW_SHOT}"""`
- L243 `PY_TEST_GENERATION_CHAT_INSTRUCTION`: `PY_TEST_GENERATION_CHAT_INSTRUCTION = """You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""`

### Classes
#### Class `PyGenerator` L246 bases=['Generator']
##### `self_reflection(self, func, feedback, model)` (L247)
- Inputs: parameters `self_reflection(self, func, feedback, model)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L248: `generic_generate_self_reflection(func=func, feedback=feedback, model=model, self_reflection_chat_instruction=PY_SELF_REFLECTION_CHAT_INSTRUCTION, self_reflection_completion_instruction=PY_SELF_REFLECTION_COMPLETION_INSTRUCTION, add_code_block=lambda x: add_code_block(x, 'python'), self_reflection_few_shot=PY_SELF_REFLECTION_FEW_SHOT)`
- LLM/model/env calls:
  - L248: `generic_generate_self_reflection`
- Main call graph hints: `generic_generate_self_reflection`, `add_code_block`
##### `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, acc_feedback, acc_reflection)` (L258)
- Inputs: parameters `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, acc_feedback, acc_reflection)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L272: `generate_with_accumulated_context(func_sig=func_sig, model=model, strategy='reflexion', prev_func_impl=prev_func_impl, accumulated_feedback=acc_feedback, accumulated_reflection=acc_reflection, num_comps=num_comps, temperature=temperature, reflection_chat_instruction=PY_REFLEXION_CHAT_INSTRUCTION, reflection_few_shot=PY_REFLEXION_FEW_SHOT_ADD, si...`
  - L291: `generic_generate_func_impl(func_sig=func_sig, model=model, strategy=strategy, prev_func_impl=prev_func_impl, feedback=feedback, self_reflection=self_reflection, num_comps=num_comps, temperature=temperature, reflection_chat_instruction=PY_REFLEXION_CHAT_INSTRUCTION, reflection_few_shot=PY_REFLEXION_FEW_SHOT_ADD, simple_chat_instruction=PY_SIMPLE_...`
- Decisions / conditions:
  - L271: IF `strategy == 'mcts'`; body=1 else=1
- LLM/model/env calls:
  - L272: `generate_with_accumulated_context`
  - L291: `generic_generate_func_impl`
- Main call graph hints: `generate_with_accumulated_context`, `generic_generate_func_impl`, `parse_code_block`, `add_code_block`
##### `internal_tests(self, func_sig, model, max_num_tests)` (L310)
- Inputs: parameters `internal_tests(self, func_sig, model, max_num_tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L316: `generic_generate_internal_tests(func_sig=func_sig, model=model, max_num_tests=max_num_tests, test_generation_few_shot=PY_TEST_GENERATION_FEW_SHOT, test_generation_chat_instruction=PY_TEST_GENERATION_CHAT_INSTRUCTION, test_generation_completion_instruction=PY_TEST_GENERATION_COMPLETION_INSTRUCTION, parse_tests=parse_tests, is_syntax_valid=py_is_s...`
  - L312: `[test.strip() for test in tests.splitlines() if 'assert' in test]`
- LLM/model/env calls:
  - L316: `generic_generate_internal_tests`
- Main call graph hints: `generic_generate_internal_tests`, `test.strip`, `tests.splitlines`

### Functions
#### `handle_first_line_indent(func_body)` (L332)
- Inputs: parameters `handle_first_line_indent(func_body)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L336: `f' {split[0]}\n' + '\n'.join(split[1:])`
  - L334: `func_body`
- Decisions / conditions:
  - L333: IF `func_body.startswith('    ')`; body=1 else=0
- Main call graph hints: `func_body.startswith`, `func_body.splitlines`, `Constant.join`
#### `handle_entire_body_indent(func_body)` (L339)
- Inputs: parameters `handle_entire_body_indent(func_body)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L342: `res`
- Main call graph hints: `func_body.splitlines`, `Constant.join`
#### `fix_turbo_response(func_body)` (L345)
- Inputs: parameters `fix_turbo_response(func_body)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L346: `fix_markdown(remove_unindented_signatures(func_body))`
- Main call graph hints: `fix_markdown`, `remove_unindented_signatures`
#### `fix_markdown(func_body)` (L349)
- Inputs: parameters `fix_markdown(func_body)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L350: `re.sub('`{3}', '', func_body)`
- Main call graph hints: `re.sub`
#### `remove_unindented_signatures(code)` (L353)
- Inputs: parameters `remove_unindented_signatures(code)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L372: `'\n'.join(before_signature + after_signature)`
- Loops:
  - L360: {'line': 360, 'type': 'for', 'target': 'line', 'iter': "code.split('\\n')", 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L361: IF `re.match(regex, line)`; body=2 else=0
  - L365: IF `signature_found`; body=1 else=2
  - L368: IF `not line.startswith('    ') and line.strip()`; body=1 else=0
- Main call graph hints: `code.split`, `Constant.join`, `re.match`, `after_signature.append`, `before_signature.append`, `line.strip`, `line.startswith`
#### `py_fix_indentation(func_body)` (L375)
- Inputs: parameters `py_fix_indentation(func_body)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L396: `parse_indent_rec(func_body, 0)`
  - L386: `f_body`
  - L390: `f_body`
  - L393: `parse_indent_rec(p_func(func_body), cur_state + 1)`
  - L395: `f_body`
- Decisions / conditions:
  - L385: IF `cur_state > 1`; body=1 else=0
- Exception handling:
  - L388: handlers=['(IndentationError, SyntaxError)', 'Exception'] final=0
- Main call graph hints: `fix_turbo_response`, `parse_indent_rec`, `fix_markdown`, `exec`, `p_func`
#### `py_is_syntax_valid(code)` (L399)
- Inputs: parameters `py_is_syntax_valid(code)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L402: `True`
  - L404: `False`
- Exception handling:
  - L400: handlers=['Exception'] final=0
- Main call graph hints: `ast.parse`

---

## File: `programming/generators/rs_generate.py`

**Lines:** 219  

### Imports
- `from generators.model import ModelBase`
- `from .generator_types import Generator`
- `from .generator_utils import generic_generate_func_impl, generic_generate_internal_tests, generic_generate_self_reflection, generate_with_accumulated_context`
- `from .parse import parse_code_block, add_code_block`
- `from typing import List, Optional, Union`

### Module assignments
- L8: `RS_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."`
- L9: `RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"`
- L10: `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation.\...`
- L11: `USE_RUST_CODEBLOCK_INSTRUCTION = "Use a Rust code block to write your response. For example:\n```rust\nfn main() {\n println!(\"Hello\");\n}\n```"`
- L13: `RS_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Rust code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L14: `RS_REFLEXION_CHAT_INSTRUCTION = "You are an AI Rust assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L15: `RS_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation."`
- L17: `RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"`
- L18: `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementati...`
- L20: `RS_REFLEXION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```rust fn add(a: i32, b: i32) -> i32 { // Given integers a and b, return the total value of a and b. a - b } ``` [unit test results from previous impl]: Tested passed: Tests failed: assert_eq!(add(1, 2), 3); // output: -1 assert_eq!(add(1, 2), 4); // output: -1 [reflection on previous impl]: The implementation failed the test cases whe...`
- L50: `RS_TEST_GENERATION_FEW_SHOT = """For example: func signature: /// Add three numbers together. /// This function takes three numbers as input and returns the sum of the three numbers. fn add3Numbers(x: i32, y: i32, z: i32) -> i32 { unit tests: assert_eq!(add3Numbers(1, 2, 3), 6); assert_eq!(add3Numbers(-1, 2, 3), 4); assert_eq!(add3Numbers(1, -2, 3), 2); assert_eq!(add3Numbers(1, 2, -3), 0); ass...`
- L66: `RS_SELF_REFLECTION_FEW_SHOT = '''Example 1: [function impl]: ```rust pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> { // Given an array of strings strs, group the anagrams together. You can return the answer in any order. // An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. use std...`
- L111: `RS_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are a Rust programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. {RS_TEST_GENERATION_FEW_SHOT}"""`
- L115: `RS_TEST_GENERATION_CHAT_INSTRUCTION = """You are a Rust programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""`

### Prompt-like assignments
- L8 `RS_SIMPLE_COMPLETION_INSTRUCTION`: `RS_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."`
- L9 `RS_REFLEXION_COMPLETION_INSTRUCTION`: `RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"`
- L10 `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION`: `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you...`
- L11 `USE_RUST_CODEBLOCK_INSTRUCTION`: `USE_RUST_CODEBLOCK_INSTRUCTION = "Use a Rust code block to write your response. For example:\n```rust\nfn main() {\n println!(\"Hello\");\n}\n```"`
- L13 `RS_SIMPLE_CHAT_INSTRUCTION`: `RS_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Rust code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L14 `RS_REFLEXION_CHAT_INSTRUCTION`: `RS_REFLEXION_CHAT_INSTRUCTION = "You are an AI Rust assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L15 `RS_SELF_REFLECTION_CHAT_INSTRUCTION`: `RS_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you t...`
- L17 `RS_REFLEXION_COMPLETION_INSTRUCTION`: `RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"`
- L18 `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION`: `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when...`
- L20 `RS_REFLEXION_FEW_SHOT_ADD`: `RS_REFLEXION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```rust fn add(a: i32, b: i32) -> i32 { // Given integers a and b, return the total value of a and b. a - b } ``` [unit test results from previous impl]: Tested passed: Tests failed: assert_eq!(add(1, 2), 3); // output: -1 assert_eq!(add(...`
- L50 `RS_TEST_GENERATION_FEW_SHOT`: `RS_TEST_GENERATION_FEW_SHOT = """For example: func signature: /// Add three numbers together. /// This function takes three numbers as input and returns the sum of the three numbers. fn add3Numbers(x: i32, y: i32, z: i32) -> i32 { unit tests: assert_eq!(add3Numbers(1, 2, 3), 6); assert_eq!(add3Nu...`
- L66 `RS_SELF_REFLECTION_FEW_SHOT`: `RS_SELF_REFLECTION_FEW_SHOT = '''Example 1: [function impl]: ```rust pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> { // Given an array of strings strs, group the anagrams together. You can return the answer in any order. // An Anagram is a word or phrase formed by rearranging the l...`
- L111 `RS_TEST_GENERATION_COMPLETION_INSTRUCTION`: `RS_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are a Rust programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. {RS_TEST_GENERATION_FEW_SHOT}"""`
- L115 `RS_TEST_GENERATION_CHAT_INSTRUCTION`: `RS_TEST_GENERATION_CHAT_INSTRUCTION = """You are a Rust programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""`

### Classes
#### Class `RsGenerator` L134 bases=['Generator']
##### `self_reflection(self, func, feedback, model)` (L135)
- Inputs: parameters `self_reflection(self, func, feedback, model)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L136: `generic_generate_self_reflection(func=func, feedback=feedback, model=model, self_reflection_chat_instruction=RS_SELF_REFLECTION_CHAT_INSTRUCTION, self_reflection_completion_instruction=RS_SELF_REFLECTION_COMPLETION_INSTRUCTION, add_code_block=lambda x: add_code_block(x, 'rust'), self_reflection_few_shot=RS_SELF_REFLECTION_FEW_SHOT)`
- LLM/model/env calls:
  - L136: `generic_generate_self_reflection`
- Main call graph hints: `generic_generate_self_reflection`, `add_code_block`
##### `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, acc_feedback, acc_reflection)` (L146)
- Inputs: parameters `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, acc_feedback, acc_reflection)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L160: `generate_with_accumulated_context(func_sig=func_sig, model=model, strategy='reflexion', prev_func_impl=prev_func_impl, accumulated_feedback=acc_feedback, accumulated_reflection=acc_reflection, num_comps=num_comps, temperature=temperature, reflection_chat_instruction=RS_REFLEXION_CHAT_INSTRUCTION, simple_chat_instruction=RS_SIMPLE_CHAT_INSTRUCTIO...`
  - L179: `generic_generate_func_impl(func_sig=func_sig, model=model, strategy=strategy, prev_func_impl=prev_func_impl, feedback=feedback, self_reflection=self_reflection, num_comps=num_comps, temperature=temperature, reflection_chat_instruction=RS_REFLEXION_CHAT_INSTRUCTION, simple_chat_instruction=RS_SIMPLE_CHAT_INSTRUCTION, reflection_completion_instruc...`
- Decisions / conditions:
  - L159: IF `strategy == 'mcts'`; body=1 else=1
- LLM/model/env calls:
  - L160: `generate_with_accumulated_context`
  - L179: `generic_generate_func_impl`
- Main call graph hints: `generate_with_accumulated_context`, `generic_generate_func_impl`, `parse_code_block`, `add_code_block`
##### `internal_tests(self, func_sig, model, max_num_tests)` (L198)
- Inputs: parameters `internal_tests(self, func_sig, model, max_num_tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L209: `generic_generate_internal_tests(func_sig=func_sig, model=model, max_num_tests=max_num_tests, test_generation_few_shot=RS_TEST_GENERATION_FEW_SHOT, test_generation_chat_instruction=RS_TEST_GENERATION_CHAT_INSTRUCTION, test_generation_completion_instruction=RS_TEST_GENERATION_COMPLETION_INSTRUCTION, parse_tests=parse_tests, is_syntax_valid=lambda ...`
  - L205: `[test + ';' for test in tests.split(';')]`
- LLM/model/env calls:
  - L209: `generic_generate_internal_tests`
- Main call graph hints: `generic_generate_internal_tests`, `tests.split`

### Functions
#### `dump_tests(tests)` (L118)
- Docstring: Dumps the tests to a string.
- Inputs: parameters `dump_tests(tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L122: `'\n'.join(tests)`
- Main call graph hints: `Constant.join`
#### `parse_tests(tests)` (L125)
- Docstring: Parses the tests from a string.
- Inputs: parameters `parse_tests(tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L129: `[test.strip() for test in tests.splitlines() if 'assert' in test]`
- Main call graph hints: `test.strip`, `tests.splitlines`

---

## File: `programming/human-eval/human_eval/__init__.py`

**Lines:** 1  

### Imports
- None

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming/human-eval/human_eval/data.py`

**Lines:** 50  

### Imports
- `from typing import Iterable, Dict`
- `import gzip`
- `import json`
- `import os`

### Module assignments
- L7: `ROOT = os.path.dirname(os.path.abspath(__file__))`
- L8: `HUMAN_EVAL = os.path.join(ROOT, "..", "data", "HumanEval.jsonl.gz")`

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `read_problems(evalset_file)` (L11)
- Inputs: parameters `read_problems(evalset_file)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L12: `{task['task_id']: task for task in stream_jsonl(evalset_file)}`
- Main call graph hints: `stream_jsonl`
#### `stream_jsonl(filename)` (L15)
- Docstring: Parses each jsonl line and yields it as a dictionary
- Inputs: parameters `stream_jsonl(filename)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': 'line', 'iter': 'fp', 'body_len': 1, 'orelse_len': 0}
  - L22: {'line': 22, 'type': 'for', 'target': 'line', 'iter': 'fp', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L19: IF `filename.endswith('.gz')`; body=1 else=1
  - L28: IF `any((not x.isspace() for x in line))`; body=1 else=0
  - L23: IF `any((not x.isspace() for x in line))`; body=1 else=0
- I/O/env/executor calls:
  - L20: `open`
  - L26: `open`
  - L21: `gzip.open`
  - L29: `json.loads`
  - L24: `json.loads`
- Main call graph hints: `filename.endswith`, `open`, `gzip.open`, `any`, `json.loads`, `x.isspace`
#### `write_jsonl(filename, data, append)` (L32)
- Docstring: Writes an iterable of dictionaries to jsonl
- Inputs: parameters `write_jsonl(filename, data, append)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L48: {'line': 48, 'type': 'for', 'target': 'x', 'iter': 'data', 'body_len': 1, 'orelse_len': 0}
  - L44: {'line': 44, 'type': 'for', 'target': 'x', 'iter': 'data', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L36: IF `append`; body=1 else=1
  - L41: IF `filename.endswith('.gz')`; body=1 else=1
- I/O/env/executor calls:
  - L42: `open`
  - L47: `open`
  - L43: `gzip.GzipFile`
  - L49: `fp.write`
  - L45: `gzfp.write`
  - L49: `json.dumps`
  - L45: `json.dumps`
- Main call graph hints: `os.path.expanduser`, `filename.endswith`, `open`, `gzip.GzipFile`, `fp.write`, `gzfp.write`, `BinOp.encode`, `json.dumps`

---

## File: `programming/human-eval/human_eval/evaluate_functional_correctness.py`

**Lines:** 29  

### Imports
- `import fire`
- `import sys`
- `from human_eval.data import HUMAN_EVAL`
- `from human_eval.evaluation import evaluate_functional_correctness`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `entry_point(sample_file, k, n_workers, timeout, problem_file)` (L8)
- Docstring: Evaluates the functional correctness of generated samples, and writes
results to f"{sample_file}_results.jsonl.gz"
- Inputs: parameters `entry_point(sample_file, k, n_workers, timeout, problem_file)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- I/O/env/executor calls:
  - L20: `evaluate_functional_correctness`
- Main call graph hints: `list`, `evaluate_functional_correctness`, `print`, `map`, `k.split`
#### `main()` (L24)
- Inputs: parameters `main()` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `fire.Fire`

---

## File: `programming/human-eval/human_eval/evaluation.py`

**Lines:** 106  

### Imports
- `from collections import defaultdict, Counter`
- `from concurrent.futures import ThreadPoolExecutor, as_completed`
- `from typing import List, Union, Iterable, Dict`
- `import itertools`
- `import numpy as np`
- `import tqdm`
- `from human_eval.data import HUMAN_EVAL, read_problems, stream_jsonl, write_jsonl`
- `from human_eval.execution import check_correctness`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `estimate_pass_at_k(num_samples, num_correct, k)` (L13)
- Docstring: Estimates pass@k of each problem and returns them in an array.
- Inputs: parameters `estimate_pass_at_k(num_samples, num_correct, k)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L36: `np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])`
  - L28: `1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))`
  - L27: `1.0`
- Decisions / conditions:
  - L30: IF `isinstance(num_samples, int)`; body=1 else=2
  - L26: IF `n - c < k`; body=1 else=0
- Main call graph hints: `isinstance`, `np.array`, `itertools.repeat`, `iter`, `np.prod`, `len`, `estimator`, `int`, `zip`, `np.arange`
#### `evaluate_functional_correctness(sample_file, k, n_workers, timeout, problem_file)` (L39)
- Docstring: Evaluates the functional correctness of generated samples, and writes
results to f"{sample_file}_results.jsonl.gz"
- Inputs: parameters `evaluate_functional_correctness(sample_file, k, n_workers, timeout, problem_file)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L105: `pass_at_k`
- Loops:
  - L80: {'line': 80, 'type': 'for', 'target': 'result', 'iter': 'results.values()', 'body_len': 4, 'orelse_len': 0}
  - L62: {'line': 62, 'type': 'for', 'target': 'sample', 'iter': 'tqdm.tqdm(stream_jsonl(sample_file))', 'body_len': 7, 'orelse_len': 0}
  - L74: {'line': 74, 'type': 'for', 'target': 'future', 'iter': 'tqdm.tqdm(as_completed(futures), total=len(futures))', 'body_len': 2, 'orelse_len': 0}
  - L94: {'line': 94, 'type': 'for', 'target': 'sample', 'iter': 'stream_jsonl(sample_file)', 'body_len': 5, 'orelse_len': 0}
- I/O/env/executor calls:
  - L51: `read_problems`
  - L103: `write_jsonl`
  - L54: `ThreadPoolExecutor`
- Main call graph hints: `read_problems`, `results.values`, `np.array`, `print`, `write_jsonl`, `ThreadPoolExecutor`, `Counter`, `defaultdict`, `tqdm.tqdm`, `result.sort`, `total.append`, `correct.append`, `estimate_pass_at_k.mean`, `stream_jsonl`, `executor.submit`, `futures.append`, `len`, `as_completed`, `future.result`, `results[...].append`, `sum`, `Compare.all`, `results[...].pop`, `combine_results`, `estimate_pass_at_k`

---

## File: `programming/human-eval/human_eval/execution.py`

Syntax error: `expected an indented block after 'with' statement on line 47 (<unknown>, line 59)`

---

## File: `programming/human-eval/setup.py`

**Lines:** 26  

### Imports
- `import os`
- `import pkg_resources`
- `from setuptools import setup, find_packages`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming/immediate_refinement.py`

**Lines:** 89  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module assignments
- None

### Prompt-like assignments
- L33 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, 1)`
- L36 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L53 `cur_func_impl`: `cur_func_impl = gen.func_impl( func_sig=item["prompt"], model=model, strategy="reflexion", prev_func_impl=cur_func_impl, feedback=cur_feedback, self_reflection="No self-reflection" )`

### Classes
- None

### Functions
#### `run_immediate_refinement(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` (L9)
- Inputs: parameters `run_immediate_refinement(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 11, 'orelse_len': 0}
  - L32: {'line': 32, 'type': 'while', 'test': 'cur_pass < pass_at_k and (not is_solved)', 'body_len': 9, 'orelse_len': 0}
  - L51: {'line': 51, 'type': 'while', 'test': 'cur_iter < max_iters', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L41: IF `is_passing`; body=4 else=0
  - L68: IF `is_passing or cur_iter == max_iters - 1`; body=3 else=0
  - L71: IF `is_passing`; body=3 else=0
- LLM/model/env calls:
  - L21: `model_factory`
- I/O/env/executor calls:
  - L80: `exe.evaluate`
  - L86: `write_jsonl`
  - L38: `exe.execute`
  - L42: `exe.evaluate`
  - L64: `exe.execute`
  - L69: `exe.evaluate`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate_resume`, `exe.evaluate`, `write_jsonl`, `print_v`, `gen.internal_tests`, `gen.func_impl`, `isinstance`, `exe.execute`, `int`, `round`

---

## File: `programming/immediate_reflexion.py`

**Lines:** 71  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module assignments
- None

### Prompt-like assignments
- L34 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L42 `reflection`: `reflection = gen.self_reflection( cur_func_impl, feedback, model)`
- L47 `cur_func_impl`: `cur_func_impl = gen.func_impl( func_sig=item["prompt"], model=model, strategy="reflexion", prev_func_impl=cur_func_impl, feedback=feedback, self_reflection=reflection )`

### Classes
- None

### Functions
#### `run_immediate_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` (L9)
- Inputs: parameters `run_immediate_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 12, 'orelse_len': 0}
  - L32: {'line': 32, 'type': 'while', 'test': 'cur_pass < pass_at_k and (not is_solved)', 'body_len': 6, 'orelse_len': 0}
  - L40: {'line': 40, 'type': 'while', 'test': 'cur_iter < max_iters', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L62: IF `is_solved`; body=1 else=0
- LLM/model/env calls:
  - L21: `model_factory`
- I/O/env/executor calls:
  - L60: `exe.evaluate`
  - L68: `write_jsonl`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate_resume`, `exe.evaluate`, `write_jsonl`, `print_v`, `gen.func_impl`, `isinstance`, `gen.self_reflection`, `round`

---

## File: `programming/main.py`

**Lines:** 132  

### Imports
- `import os`
- `import argparse`
- `from immediate_refinement import run_immediate_refinement`
- `from immediate_reflexion import run_immediate_reflexion`
- `from simple import run_simple`
- `from reflexion import run_reflexion`
- `from test_acc import run_test_acc`
- `from utils import read_jsonl, read_jsonl_gz`
- `from mcts import run_mcts`
- `from dfs import run_dfs`

### Module assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L129 If: `if __name__ == "__main__": args = get_args() main(args)`

### Classes
- None

### Functions
#### `get_args()` (L14)
- Inputs: parameters `get_args()` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L43: `args`
- Main call graph hints: `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`
#### `strategy_factory(strategy)` (L46)
- Inputs: parameters `strategy_factory(strategy)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L52: `kwargs_wrapper`
  - L55: `kwargs_wrapper_gen(run_simple, delete_keys=['expansion_factor', 'max_iters'])`
  - L51: `func(**kwargs)`
  - L57: `kwargs_wrapper_gen(run_reflexion, delete_keys=['expansion_factor'])`
  - L59: `kwargs_wrapper_gen(run_mcts, delete_keys=['expansion_factor'])`
  - L61: `kwargs_wrapper_gen(run_dfs, delete_keys=['expansion_factor'])`
  - L63: `kwargs_wrapper_gen(run_immediate_reflexion, delete_keys=['expansion_factor'])`
  - L65: `kwargs_wrapper_gen(run_immediate_refinement, delete_keys=['expansion_factor'])`
  - L67: `kwargs_wrapper_gen(run_test_acc, delete_keys=['expansion_factor', 'max_iters'])`
- Loops:
  - L49: {'line': 49, 'type': 'for', 'target': 'key', 'iter': 'delete_keys', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L54: IF `strategy == 'simple'`; body=1 else=1
  - L56: IF `strategy == 'reflexion'`; body=1 else=1
  - L58: IF `strategy == 'mcts'`; body=1 else=1
  - L60: IF `strategy == 'dfs'`; body=1 else=1
  - L62: IF `strategy == 'immediate-reflexion'`; body=1 else=1
  - L64: IF `strategy == 'immediate-refinement'`; body=1 else=1
  - L66: IF `strategy == 'test-acc'`; body=1 else=1
- Main call graph hints: `kwargs_wrapper_gen`, `func`, `ValueError`
#### `main(args)` (L72)
- Inputs: parameters `main(args)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L74: IF `not os.path.exists(args.root_dir)`; body=1 else=0
  - L84: IF `not os.path.exists(log_dir)`; body=1 else=0
  - L91: IF `args.verbose`; body=1 else=1
  - L102: IF `args.dataset_path.endswith('.jsonl')`; body=1 else=1
  - L104: IF `args.dataset_path.endswith('.jsonl.gz')`; body=1 else=1
- I/O/env/executor calls:
  - L103: `read_jsonl`
  - L105: `read_jsonl_gz`
- Main call graph hints: `os.path.basename.replace`, `os.path.join`, `strategy_factory`, `print`, `args.dataset_path.endswith`, `run_strategy`, `os.path.exists`, `os.makedirs`, `read_jsonl`, `os.path.basename`, `read_jsonl_gz`, `ValueError`, `len`

---

## File: `programming/mcts.py`

**Lines:** 262  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl, resume_success_count`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List, Dict, Any`
- `import math`
- `from typing import Tuple`
- `import sys`

### Module assignments
- L11: `react_prompt_header = "Here are some previous solutions and the corresponding test results.\n"`
- L12: `react_prompt_starter = "\n\nYour solution:\n"`

### Prompt-like assignments
- L11 `react_prompt_header`: `react_prompt_header = "Here are some previous solutions and the corresponding test results.\n"`
- L146 `reflection`: `reflection = gen.self_reflection(cur_func_impl, feedback, model)`
- L115 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], test_model, number_of_tests)`
- L118 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L153 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], test_model, number_of_tests)`
- L156 `trajectory`: `trajectory = { 'solutions': [], 'feedbacks': [] }`
- L175 `new_solution`: `new_solution = gen.func_impl( func_sig=item["prompt"], model=model, strategy=strategy, prev_func_impl=prev_func_impl, feedback=feedback, self_reflection=reflection, acc_feedback = acc_feedback, acc_reflection = acc_reflection )`
- L196 `reflection`: `reflection = gen.self_reflection(child.solution, feedback_internal, model)`
- L208 `passed_section`: `passed_section = feedback_internal.split("Tests failed:")[0]`

### Classes
#### Class `Node` L14 bases=[]
##### `__init__(self, solution, parent, context, depth)` (L15)
- Inputs: parameters `__init__(self, solution, parent, context, depth)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `uct(self, exploration_weight)` (L26)
- Inputs: parameters `uct(self, exploration_weight)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L30: `self.value / self.visits + exploration_weight * math.sqrt(math.log(self.parent.visits) / self.visits)`
  - L29: `self.value`
- Decisions / conditions:
  - L27: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `math.sqrt`, `math.log`
##### `best_child(self)` (L32)
- Inputs: parameters `best_child(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L35: `max(self.children, key=lambda child: child.uct())`
  - L34: `None`
- Decisions / conditions:
  - L33: IF `not self.children`; body=1 else=0
- Main call graph hints: `max`, `child.uct`
##### `best_child_value(self)` (L37)
- Inputs: parameters `best_child_value(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L40: `max(self.children, key=lambda child: child.value)`
  - L39: `None`
- Decisions / conditions:
  - L38: IF `not self.children`; body=1 else=0
- Main call graph hints: `max`
##### `update(self, reward)` (L42)
- Inputs: parameters `update(self, reward)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.

### Functions
#### `prune_context_blocks(context, max_length)` (L47)
- Docstring: Prune the context to fit within the specified max_length by removing entire blocks of content using 'trial' as a delimiter.
- Inputs: parameters `prune_context_blocks(context, max_length)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L59: `'trial'.join(blocks)`
  - L50: `context`
- Loops:
  - L56: {'line': 56, 'type': 'while', 'test': "len('trial'.join(blocks)) > max_length and blocks", 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L49: IF `len(context) <= max_length`; body=1 else=0
- Main call graph hints: `context.split`, `Constant.join`, `len`, `blocks.pop`
#### `gather_context_from_tree(node)` (L61)
- Docstring: Given a node, walk up its tree and gather the feedback and reflections 
from each parent node until the root is reached.

Args:
    node (Node): The node to start gathering context from.

Returns:
    Tuple[List[str], List[str]]: Two lists containing the accumulated feedback and reflections.
- Inputs: parameters `gather_context_from_tree(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L83: `(accumulated_feedback[::-1], accumulated_reflection[::-1])`
- Loops:
  - L75: {'line': 75, 'type': 'while', 'test': 'node', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L76: IF `node.test_feedback`; body=1 else=0
  - L78: IF `node.reflection`; body=1 else=0
- Main call graph hints: `accumulated_feedback.append`, `accumulated_reflection.append`
#### `run_mcts(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode, n, number_of_tests)` (L86)
- Inputs: parameters `run_mcts(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode, n, number_of_tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L108: {'line': 108, 'type': 'for', 'target': '(idx, item)', 'iter': 'enumerate(dataset)', 'body_len': 32, 'orelse_len': 0}
  - L117: {'line': 117, 'type': 'while', 'test': 'cur_func_impl is None', 'body_len': 1, 'orelse_len': 0}
  - L151: {'line': 151, 'type': 'for', 'target': 'cur_iter', 'iter': 'range(max_iters)', 'body_len': 6, 'orelse_len': 0}
  - L161: {'line': 161, 'type': 'while', 'test': 'node.children', 'body_len': 2, 'orelse_len': 0}
  - L166: {'line': 166, 'type': 'for', 'target': '_', 'iter': 'range(n)', 'body_len': 19, 'orelse_len': 0}
  - L174: {'line': 174, 'type': 'while', 'test': 'new_solution is None', 'body_len': 1, 'orelse_len': 0}
  - L193: {'line': 193, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 4, 'orelse_len': 0}
  - L232: {'line': 232, 'type': 'while', 'test': 'temp.parent', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L112: IF `is_leetcode`; body=1 else=1
  - L135: IF `is_passing`; body=8 else=0
  - L239: IF `is_solved`; body=1 else=2
  - L248: IF `is_passing`; body=1 else=0
  - L236: IF `is_solved`; body=1 else=0
  - L222: IF `is_solved`; body=1 else=0
  - L195: IF `not is_passing_internal`; body=5 else=3
  - L206: IF `'Tested passed:' in feedback_internal`; body=3 else=1
  - L214: IF `is_passing_internal or cur_iter == max_iters - 1`; body=3 else=0
  - L216: IF `is_passing`; body=3 else=0
- LLM/model/env calls:
  - L100: `model_factory`
  - L101: `model_factory`
- I/O/env/executor calls:
  - L131: `exe.execute`
  - L245: `exe.execute`
  - L247: `exe.evaluate`
  - L259: `write_jsonl`
  - L136: `exe.evaluate`
  - L141: `write_jsonl`
  - L194: `exe.execute`
  - L215: `exe.evaluate`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate`, `Node`, `implementations.append`, `isinstance`, `exe.execute`, `test_feedback.append`, `gen.self_reflection`, `range`, `exe.evaluate`, `reflections.append`, `round`, `write_jsonl`, `print_v`, `gen.internal_tests`, `gen.func_impl`, `int`, `print`, `node.best_child`, `trajectory[...].append`, `gather_context_from_tree`, `node.children.append`, `child.update`, `root.best_child_value`, `temp.update`, `feedback_internal.split`, `passed_section.split[...].splitlines`, `line.strip`, `passed_section.split`

---

## File: `programming/reflexion.py`

**Lines:** 108  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl, resume_success_count`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module assignments
- None

### Prompt-like assignments
- L38 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, number_of_tests)`
- L42 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L61 `reflection`: `reflection = gen.self_reflection( cur_func_impl, cur_feedback, model)`
- L70 `cur_func_impl`: `cur_func_impl = gen.func_impl( func_sig=prompt, model=model, strategy="simple", prev_func_impl=cur_func_impl, feedback="", self_reflection="", )`

### Classes
- None

### Functions
#### `run_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode, number_of_tests)` (L8)
- Inputs: parameters `run_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode, number_of_tests)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 15, 'orelse_len': 0}
  - L34: {'line': 34, 'type': 'while', 'test': 'cur_pass < pass_at_k and (not is_solved)', 'body_len': 11, 'orelse_len': 0}
  - L41: {'line': 41, 'type': 'while', 'test': 'cur_func_impl is None', 'body_len': 1, 'orelse_len': 0}
  - L59: {'line': 59, 'type': 'while', 'test': 'cur_iter < max_iters', 'body_len': 12, 'orelse_len': 0}
- Decisions / conditions:
  - L35: IF `is_leetcode`; body=1 else=1
  - L49: IF `is_passing`; body=4 else=0
  - L87: IF `is_passing or cur_iter == max_iters - 1`; body=3 else=0
  - L90: IF `is_passing`; body=3 else=0
- LLM/model/env calls:
  - L21: `model_factory`
- I/O/env/executor calls:
  - L105: `write_jsonl`
  - L45: `exe.execute`
  - L50: `exe.evaluate`
  - L82: `exe.execute`
  - L88: `exe.evaluate`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `resume_success_count`, `enumerate_resume`, `round`, `write_jsonl`, `print_v`, `implementations.append`, `isinstance`, `exe.execute`, `test_feedback.append`, `gen.internal_tests`, `gen.func_impl`, `exe.evaluate`, `int`, `gen.self_reflection`

---

## File: `programming/root/get_acc.py`

**Lines:** 53  

### Imports
- `import json`

### Module assignments
- L46: `filename = "/Users/andyzhou/Documents/Research/LLMPlanning/programming/root/test_mcts_hard_acc_full_4tst_temp_gpt4/humaneval-py._mcts_8_gpt-4_pass_at_k_1_py.jsonl"`
- L47: `res = calculate_overall_accuracy(filename)`
- L48: `overall_avg = res[0]`
- L49: `count = res[1]`

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `calculate_overall_accuracy(filename)` (L3)
- Inputs: parameters `calculate_overall_accuracy(filename)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L42: `(0, count)`
  - L44: `(overall_correct / overall_count, overall_count)`
- Loops:
  - L11: {'line': 11, 'type': 'for', 'target': 'line', 'iter': 'f', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L41: IF `overall_count == 0`; body=1 else=1
  - L35: IF `count > 0`; body=3 else=0
  - L16: IF `acc == 1.0 or (acc == 0.0 and prev_acc != 1.0 and (prev_acc != 0.0))`; body=4 else=0
- I/O/env/executor calls:
  - L9: `open`
  - L12: `json.loads`
- Main call graph hints: `open`, `json.loads`, `int`

---

## File: `programming/simple.py`

**Lines:** 46  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module assignments
- L7: `SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."`
- L8: `SIMPLE_CHAT_INSTRUCTION = "You are a programming assistant. You will be given a function signature and docstring. You should fill in the following text of the missing function body. For example, the first line of the completion should have 4 spaces for the indentation so that it fits syntactically with the preceding signature."`

### Prompt-like assignments
- L7 `SIMPLE_COMPLETION_INSTRUCTION`: `SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."`
- L8 `SIMPLE_CHAT_INSTRUCTION`: `SIMPLE_CHAT_INSTRUCTION = "You are a programming assistant. You will be given a function signature and docstring. You should fill in the following text of the missing function body. For example, the first line of the completion should have 4 spaces for the indentation so that it fits syntacticall...`
- L32 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`

### Classes
- None

### Functions
#### `run_simple(dataset, model_name, language, pass_at_k, log_path, verbose, is_leetcode)` (L10)
- Inputs: parameters `run_simple(dataset, model_name, language, pass_at_k, log_path, verbose, is_leetcode)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 8, 'orelse_len': 0}
  - L31: {'line': 31, 'type': 'while', 'test': 'cur_pass < pass_at_k', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L35: IF `is_passing`; body=3 else=0
- LLM/model/env calls:
  - L21: `model_factory`
- I/O/env/executor calls:
  - L43: `write_jsonl`
  - L34: `exe.evaluate`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate_resume`, `write_jsonl`, `print_v`, `gen.func_impl`, `isinstance`, `exe.evaluate`, `round`

---

## File: `programming/test_acc.py`

**Lines:** 48  

### Imports
- `from utils import enumerate_resume, write_jsonl, make_printv`
- `from executors import executor_factory`
- `from generators import generator_factory`
- `from typing import List`

### Module assignments
- None

### Prompt-like assignments
- L30 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, 1)`
- L33 `cur_func_impl`: `cur_func_impl = item["prompt"] + item["canonical_solution"]`

### Classes
- None

### Functions
#### `run_test_acc(dataset, model, language, pass_at_k, log_path, verbose, is_leetcode)` (L9)
- Inputs: parameters `run_test_acc(dataset, model, language, pass_at_k, log_path, verbose, is_leetcode)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L25: {'line': 25, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 8, 'orelse_len': 0}
  - L29: {'line': 29, 'type': 'while', 'test': 'cur_pass < pass_at_k', 'body_len': 7, 'orelse_len': 0}
- Decisions / conditions:
  - L37: IF `is_passing`; body=3 else=0
- I/O/env/executor calls:
  - L45: `write_jsonl`
  - L36: `exe.execute`
- Main call graph hints: `executor_factory`, `generator_factory`, `make_printv`, `len`, `enumerate_resume`, `write_jsonl`, `print_v`, `gen.internal_tests`, `exe.execute`, `round`

---

## File: `programming/utils.py`

**Lines:** 76  

### Imports
- `import os`
- `import gzip`
- `import json`
- `import openai`
- `import jsonlines`
- `from typing import List`

### Module assignments
- L9: `openai.api_key = os.getenv("OPENAI_API_KEY")`

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `make_printv(verbose)` (L12)
- Inputs: parameters `make_printv(verbose)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L19: `print_v`
- Decisions / conditions:
  - L14: IF `verbose`; body=2 else=1
- Main call graph hints: `print`
#### `read_jsonl(path)` (L22)
- Inputs: parameters `read_jsonl(path)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L31: `items`
- Loops:
  - L29: {'line': 29, 'type': 'for', 'target': 'item', 'iter': 'reader', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L23: IF `not os.path.exists(path)`; body=1 else=1
  - L25: IF `not path.endswith('.jsonl')`; body=1 else=0
- I/O/env/executor calls:
  - L28: `jsonlines.open`
- Main call graph hints: `os.path.exists`, `FileNotFoundError`, `jsonlines.open`, `path.endswith`, `ValueError`
#### `write_jsonl(path, data, append)` (L34)
- Inputs: parameters `write_jsonl(path, data, append)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L37: {'line': 37, 'type': 'for', 'target': 'item', 'iter': 'data', 'body_len': 1, 'orelse_len': 0}
- I/O/env/executor calls:
  - L36: `jsonlines.open`
  - L38: `writer.write`
- Main call graph hints: `os.makedirs`, `os.path.dirname`, `jsonlines.open`, `writer.write`
#### `read_jsonl_gz(path)` (L41)
- Inputs: parameters `read_jsonl_gz(path)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L46: `data`
- Decisions / conditions:
  - L42: IF `not path.endswith('.jsonl.gz')`; body=1 else=0
- I/O/env/executor calls:
  - L44: `gzip.open`
  - L45: `json.loads`
- Main call graph hints: `path.endswith`, `ValueError`, `gzip.open`, `json.loads`
#### `enumerate_resume(dataset, results_path)` (L52)
- Inputs: parameters `enumerate_resume(dataset, results_path)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L54: {'line': 54, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(dataset)', 'body_len': 1, 'orelse_len': 0}
  - L62: {'line': 62, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(dataset)', 'body_len': 2, 'orelse_len': 0}
  - L59: {'line': 59, 'type': 'for', 'target': 'item', 'iter': 'reader', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L53: IF `not os.path.exists(results_path)`; body=1 else=3
  - L64: IF `i < count`; body=1 else=0
- I/O/env/executor calls:
  - L58: `jsonlines.open`
- Main call graph hints: `os.path.exists`, `enumerate`, `jsonlines.open`
#### `resume_success_count(dataset)` (L69)
- Inputs: parameters `resume_success_count(dataset)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L74: `count`
- Loops:
  - L71: {'line': 71, 'type': 'for', 'target': 'item', 'iter': 'dataset', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L72: IF `'is_solved' in item and item['is_solved']`; body=1 else=0

---

## File: `setup.py`

**Lines:** 38  

### Imports
- `import setuptools`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `webshop/base.py`

**Lines:** 13  

### Imports
- `import os`

### Module assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `Task` L2 bases=[]
##### `__init__(self)` (L3)
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `__len__(self)` (L6)
- Inputs: parameters `__len__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `get_input(self, idx)` (L9)
- Inputs: parameters `get_input(self, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `test_output(self, idx, output)` (L12)
- Inputs: parameters `test_output(self, idx, output)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.

### Functions
- None

---

## File: `webshop/lats.py`

**Lines:** 736  

### Imports
- `import os`
- `import openai`
- `import backoff`
- `import sys`
- `import copy`
- `import itertools`
- `import numpy as np`
- `from functools import partial`
- `from models import gpt`
- `import requests`
- `import logging`
- `import random`
- `import requests`
- `from bs4 import BeautifulSoup`
- `from bs4.element import Comment`
- `import numpy as np`

### Module assignments
- L22: `completion_tokens = prompt_tokens = 0`
- L23: `openai.api_key = os.environ["OPENAI_API_KEY"]`
- L29: `WEBSHOP_URL = "http://127.0.0.1:5000"`
- L30: `ACTION_TO_TEMPLATE = { 'Description': 'description_page.html', 'Features': 'features_page.html', 'Reviews': 'review_page.html', 'Attributes': 'attributes_page.html', }`
- L209: `env = webshopEnv()`
- L213: `reflection_map = []`
- L214: `failed_trajectories = []`

### Prompt-like assignments
- L30 `ACTION_TO_TEMPLATE`: `ACTION_TO_TEMPLATE = { 'Description': 'description_page.html', 'Features': 'features_page.html', 'Reviews': 'review_page.html', 'Attributes': 'attributes_page.html', }`
- L240 `value_prompt`: `value_prompt = task.value_prompt_wrap(x, y, failed_trajectories, reflection_map)`
- L246 `value_outputs`: `value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)`
- L286 `samples`: `samples = gpt(prompt, n=n_generate_sample, stop=stop)`
- L616 `sampled_actions`: `sampled_actions = get_samples(task, prompt, "\nAction: ", n, prompt_sample=args.prompt_sample, stop="Observation")`
- L683 `child_prompts`: `child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]`
- L685 `votes`: `votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)`
- L691 `votes`: `votes = votes + [0] * (len(node.children) - len(votes))`
- L225 `uct_values`: `uct_values = [child.uct() for child in node.children if not child.is_terminal]`
- L229 `probabilities`: `probabilities = softmax(np.array(uct_values), temperature)`
- L278 `reflection_map`: `reflection_map = task.generate_self_reflection(failed_trajectories, x)`
- L303 `state`: `self.state = {'action': '', 'observation': ''} if state is None else state`
- L453 `terminal_node`: `terminal_node = rollout(max(node.children, key=lambda child: child.value), args, task, idx, max_depth=15)`
- L562 `child_prompts`: `child_prompts = [generate_prompt(child) for child in new_states if not child.is_terminal and child is not None]`
- L625 `action_line`: `action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)`
- L717 `value`: `node.value = (node.value * (node.visits - 1) + value) / node.visits`
- L130 `observation`: `observation = 'Your score (min 0.0, max 1.0): ' + (visible_texts[idx + 1])`
- L261 `value`: `value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)`
- L282 `prompt`: `prompt = task.cot_prompt_wrap(x, y, reflection_map)`
- L355 `action`: `action = line.split(", action=")[1].split(", observation=")[0].strip()`
- L356 `observation`: `observation = line.split(", observation=")[1].split(")")[0].strip()`
- L565 `values`: `values = get_values(task, node.question, child_prompts, args.n_evaluate_sample)`
- L654 `new_node`: `new_node = Node(state=new_state, question=node.question, env_state=env_state_clone, parent=node)`

### Classes
#### Class `webshopEnv` L133 bases=[]
##### `__init__(self)` (L134)
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `clone_state(self)` (L137)
- Inputs: parameters `clone_state(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L138: `copy.deepcopy(self.sessions)`
- Main call graph hints: `copy.deepcopy`
##### `step(self, session, action)` (L140)
- Inputs: parameters `step(self, session, action)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L207: `(observation, reward, done)`
- Decisions / conditions:
  - L144: IF `action == 'reset'`; body=1 else=1
  - L196: IF `observation_`; body=1 else=0
  - L200: IF `reward != 0.0`; body=1 else=0
  - L204: IF `reward == 1.0`; body=2 else=0
  - L146: IF `action.startswith('think[')`; body=1 else=1
  - L148: IF `action.startswith('search[')`; body=3 else=1
  - L153: IF `action.startswith('click[')`; body=2 else=1
  - L155: IF `button == 'Buy Now'`; body=2 else=1
  - L159: IF `button == 'Back to Search'`; body=2 else=1
  - L162: IF `button == 'Next >'`; body=2 else=1
  - L166: IF `button == '< Prev'`; body=2 else=1
  - L168: IF `self.sessions[session]['page_type'] == 'search'`; body=1 else=1
  - L176: IF `button in ACTION_TO_TEMPLATE`; body=3 else=1
  - L171: IF `self.sessions[session]['page_type'] == 'item_sub'`; body=1 else=1
  - L181: IF `self.sessions[session]['page_type'] == 'search'`; body=3 else=1
  - L173: IF `self.sessions[session]['page_type'] == 'item'`; body=2 else=0
  - L185: IF `self.sessions[session]['page_type'] == 'item'`; body=6 else=0
  - L189: IF `not 'options' in self.sessions[session]`; body=1 else=0
- Main call graph hints: `logging.info`, `webshop_text`, `self.sessions[...].update`, `info.get`, `action.startswith`, `print`, `self.sessions[...].get`
#### Class `Node` L301 bases=[]
##### `__init__(self, state, question, env_state, parent)` (L302)
- Inputs: parameters `__init__(self, state, question, env_state, parent)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `uct(self)` (L316)
- Inputs: parameters `uct(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L322: `self.value / self.visits + np.sqrt(2 * np.log(self.parent.visits) / self.visits)`
  - L318: `float('inf')`
  - L321: `self.value`
- Decisions / conditions:
  - L317: IF `self.visits == 0 and self.value >= 0`; body=1 else=1
  - L320: IF `self.visits == 0 and self.value < 0`; body=1 else=0
- Main call graph hints: `float`, `np.sqrt`, `np.log`
##### `uct_with_depth(self, C1, C2)` (L324)
- Inputs: parameters `uct_with_depth(self, C1, C2)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L330: `exploitation_term + C1 * exploration_term + C2 * depth_term`
  - L326: `self.value`
- Decisions / conditions:
  - L325: IF `self.visits == 0`; body=1 else=0
- Main call graph hints: `np.sqrt`, `np.log`
##### `__str__(self)` (L332)
- Inputs: parameters `__str__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L333: `f"Node(depth={self.depth}, value={self.value:.2f}, visits={self.visits}, action={self.state['action']}, observation={self.state['observation']})"`
##### `to_dict(self)` (L335)
- Inputs: parameters `to_dict(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L336: `{'state': self.state, 'question': self.question, 'parent': self.parent.to_dict() if self.parent else None, 'children': [child.to_dict() for child in self.children], 'visits': self.visits, 'value': self.value, 'depth': self.depth, 'is_terminal': self.is_terminal, 'reward': self.reward, 'em': self.em}`
- Main call graph hints: `self.parent.to_dict`, `child.to_dict`

### Functions
#### `clean_str(p)` (L37)
- Inputs: parameters `clean_str(p)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L38: `p.encode().decode('unicode-escape').encode('latin1').decode('utf-8')`
- Main call graph hints: `p.encode.decode.encode.decode`, `p.encode.decode.encode`, `p.encode.decode`, `p.encode`
#### `tag_visible(element)` (L41)
- Inputs: parameters `tag_visible(element)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L43: `element.parent.name not in ignore and (not isinstance(element, Comment))`
- Main call graph hints: `isinstance`
#### `webshop_text(session, page_type, query_string, page_num, asin, options, subpage, **kwargs)` (L48)
- Inputs: parameters `webshop_text(session, page_type, query_string, page_num, asin, options, subpage, **kwargs)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L82: `' [SEP] '.join((t.strip() for t in visible_texts if t != '\n'))`
  - L131: `(clean_str(observation), info)`
- Loops:
  - L92: {'line': 92, 'type': 'for', 'target': 't', 'iter': 'visible_texts', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L49: IF `page_type == 'init'`; body=1 else=0
  - L53: IF `page_type == 'search'`; body=1 else=1
  - L80: IF `False`; body=1 else=13
  - L58: IF `page_type == 'item'`; body=1 else=1
  - L123: IF `options`; body=1 else=0
  - L125: IF `asins`; body=1 else=0
  - L127: IF `'Your score (min 0.0, max 1.0)' in visible_texts`; body=3 else=0
  - L63: IF `page_type == 'item_sub'`; body=1 else=1
  - L93: IF `t == '\n'`; body=1 else=0
  - L94: IF `t.replace('\n', '').replace('\\n', '').replace(' ', '') == ''`; body=1 else=0
  - L97: IF `t.parent.name == 'button'`; body=1 else=1
  - L68: IF `page_type == 'end'`; body=1 else=0
  - L99: IF `t.parent.name == 'label'`; body=2 else=1
  - L100: IF `f"'{t}'" in url`; body=1 else=1
  - L107: IF `t.parent.get('class') == ['product-link']`; body=5 else=5
  - L109: IF `prod_cnt >= 10`; body=1 else=0
  - L116: IF `cnt < 2 and page_type != 'init'`; body=1 else=0
  - L117: IF `just_prod <= 2 and prod_cnt >= 4`; body=1 else=0
- Main call graph hints: `BeautifulSoup`, `html_obj.findAll`, `list`, `requests.get`, `filter`, `Constant.join`, `visible_texts.index`, `float`, `clean_str`, `t.strip`, `t.replace.replace.replace`, `t.replace.replace`, `str`, `t.parent.get`, `asins.append`, `t.replace`
#### `softmax(x, temperature)` (L219)
- Inputs: parameters `softmax(x, temperature)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L221: `e_x / e_x.sum(axis=0)`
- Main call graph hints: `np.exp`, `e_x.sum`, `np.max`
#### `select_node_softmax(node, temperature)` (L223)
- Inputs: parameters `select_node_softmax(node, temperature)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L234: `node`
  - L227: `None`
- Loops:
  - L224: {'line': 224, 'type': 'while', 'test': 'node and node.children', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L226: IF `not uct_values`; body=1 else=0
- Main call graph hints: `softmax`, `np.random.choice`, `child.uct`, `np.array`
#### `get_value(task, x, y, n_evaluate_sample, cache_value)` (L236)
- Inputs: parameters `get_value(task, x, y, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L252: `value`
  - L244: `task.value_cache[value_prompt]`
- Decisions / conditions:
  - L243: IF `cache_value and value_prompt in task.value_cache`; body=1 else=0
  - L250: IF `cache_value`; body=1 else=0
- LLM/model/env calls:
  - L246: `gpt`
- Main call graph hints: `task.value_prompt_wrap`, `logging.info`, `gpt`, `task.value_outputs_unwrap`
#### `get_values(task, x, ys, n_evaluate_sample, cache_value)` (L254)
- Inputs: parameters `get_values(task, x, ys, n_evaluate_sample, cache_value)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L264: `values`
- Loops:
  - L257: {'line': 257, 'type': 'for', 'target': 'y', 'iter': 'ys', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L258: IF `y in local_value_cache`; body=1 else=2
- Main call graph hints: `values.append`, `get_value`
#### `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` (L266)
- Inputs: parameters `get_samples(task, x, y, n_generate_sample, prompt_sample, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L287: `[y + _ for _ in samples]`
- Decisions / conditions:
  - L274: IF `len(failed_trajectories) > len(reflection_map) and len(failed_trajectories) < 4`; body=4 else=0
  - L279: IF `prompt_sample == 'standard'`; body=1 else=1
  - L281: IF `prompt_sample == 'cot'`; body=1 else=1
- LLM/model/env calls:
  - L286: `gpt`
  - L278: `task.generate_self_reflection`
- Main call graph hints: `logging.info`, `gpt`, `print`, `task.generate_self_reflection`, `task.standard_prompt_wrap`, `len`, `task.cot_prompt_wrap`, `ValueError`
#### `get_unique_trajectories(failed_trajectories, num)` (L289)
- Inputs: parameters `get_unique_trajectories(failed_trajectories, num)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L299: `unique_trajectories`
- Loops:
  - L292: {'line': 292, 'type': 'for', 'target': 'traj', 'iter': 'failed_trajectories', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L294: IF `final_answer not in seen_final_answers`; body=2 else=0
  - L297: IF `len(unique_trajectories) >= num`; body=1 else=0
- Main call graph hints: `set`, `traj.get`, `unique_trajectories.append`, `seen_final_answers.add`, `len`, `node_trajectory_to_text`
#### `node_trajectory_to_text(node_string)` (L349)
- Inputs: parameters `node_trajectory_to_text(node_string)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L366: `'\n'.join(formatted_lines)`
- Loops:
  - L352: {'line': 352, 'type': 'for', 'target': 'line', 'iter': 'lines', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L360: IF `depth != 0`; body=2 else=0
  - L361: IF `action`; body=1 else=0
  - L363: IF `observation`; body=1 else=0
- Exception handling:
  - L353: handlers=['IndexError'] final=0
- Main call graph hints: `node_string.split`, `Constant.join`, `int`, `line.split[...].split[...].strip`, `formatted_lines.append`, `line.split[...].split`, `line.split`
#### `collect_actions_to_node(node)` (L368)
- Inputs: parameters `collect_actions_to_node(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L374: `list(reversed(actions))`
- Loops:
  - L370: {'line': 370, 'type': 'while', 'test': 'node', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L371: IF `node.state['action']`; body=1 else=0
- Main call graph hints: `list`, `reversed`, `actions.append`
#### `collect_all_nodes(node)` (L377)
- Docstring: Recursively collect all nodes starting from the given node.
- Inputs: parameters `collect_all_nodes(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L382: `nodes`
- Loops:
  - L380: {'line': 380, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `nodes.extend`, `collect_all_nodes`
#### `collect_trajectory(node)` (L384)
- Inputs: parameters `collect_trajectory(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L404: `'\n'.join(trajectory)`
- Loops:
  - L392: {'line': 392, 'type': 'while', 'test': 'node', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L393: IF `node.state and 'action' in node.state and node.state['action'] and node.parent`; body=1 else=1
  - L398: IF `node.state and 'observation' in node.state and node.state['observation'] and node.parent`; body=1 else=1
- Main call graph hints: `trajectory.append`, `Constant.join`, `logging.warning`
#### `lats_search(args, task, idx, iterations, to_print)` (L408)
- Inputs: parameters `lats_search(args, task, idx, iterations, to_print)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L495: `(best_child.state, best_child.value, best_child.reward, best_child.em)`
  - L442: `(node.state, node.value, all_nodes, node.reward, node.em)`
  - L459: `(terminal_node.state, terminal_node.value, terminal_node.reward, terminal_node.em)`
  - L475: `(best_node.state, best_node.value, best_node.reward, best_node.em)`
- Loops:
  - L428: {'line': 428, 'type': 'for', 'target': 'i', 'iter': 'range(iterations)', 'body_len': 19, 'orelse_len': 0}
  - L432: {'line': 432, 'type': 'while', 'test': 'node is None or (node.is_terminal and node.reward != 1)', 'body_len': 2, 'orelse_len': 0}
  - L446: {'line': 446, 'type': 'while', 'test': 'node.is_terminal', 'body_len': 3, 'orelse_len': 0}
  - L477: {'line': 477, 'type': 'for', 'target': '(j, (node, value))', 'iter': 'enumerate(all_nodes)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L418: IF `to_print`; body=1 else=0
  - L491: IF `best_child.reward == 1`; body=1 else=1
  - L436: IF `node is None`; body=2 else=0
  - L440: IF `node.is_terminal and node.reward == 1`; body=2 else=0
  - L456: IF `terminal_node.reward == 1`; body=3 else=0
  - L471: IF `terminal_nodes_with_reward_1`; body=4 else=0
- I/O/env/executor calls:
  - L417: `env.step`
  - L451: `evaluate_node`
- Main call graph hints: `partial`, `logging.basicConfig`, `Node`, `copy.deepcopy`, `range`, `collect_all_nodes`, `all_nodes_list.extend`, `max`, `print`, `env.step`, `logging.info`, `select_node`, `expand_node`, `evaluate_node`, `rollout`, `terminal_nodes.append`, `backpropagate`, `enumerate`, `Constant.join`, `str`
#### `simple_search(args, task, idx, iterations, max_depth, to_print)` (L497)
- Inputs: parameters `simple_search(args, task, idx, iterations, max_depth, to_print)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L542: `(best_node.state, best_node.value, best_node.reward, best_node.em)`
  - L545: `(best_node.state, best_node.value, best_node.reward, best_node.em)`
- Loops:
  - L514: {'line': 514, 'type': 'for', 'target': 'i', 'iter': 'range(iterations)', 'body_len': 6, 'orelse_len': 0}
  - L520: {'line': 520, 'type': 'while', 'test': 'not node.is_terminal and depth < max_depth', 'body_len': 4, 'orelse_len': 0}
- Decisions / conditions:
  - L510: IF `to_print`; body=1 else=0
  - L540: IF `successful_trajectories`; body=2 else=2
  - L528: IF `node.is_terminal and node.reward == 1`; body=3 else=1
  - L522: IF `not node.children`; body=1 else=0
  - L532: IF `node.is_terminal and node.reward < 1`; body=2 else=0
- I/O/env/executor calls:
  - L502: `env.step`
- Main call graph hints: `Node`, `copy.deepcopy`, `range`, `env.step`, `print`, `logging.info`, `max`, `expand_node`, `random.choice`, `successful_trajectories.append`, `unsuccessful_trajectories.append`
#### `rollout(node, args, task, idx, max_depth)` (L548)
- Inputs: parameters `rollout(node, args, task, idx, max_depth)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L572: `node`
  - L560: `state`
- Loops:
  - L551: {'line': 551, 'type': 'while', 'test': 'not node.is_terminal and depth < max_depth', 'body_len': 10, 'orelse_len': 0}
  - L555: {'line': 555, 'type': 'while', 'test': 'len(new_states) == 0', 'body_len': 1, 'orelse_len': 0}
  - L558: {'line': 558, 'type': 'for', 'target': 'state', 'iter': 'new_states', 'body_len': 1, 'orelse_len': 0}
  - L564: {'line': 564, 'type': 'while', 'test': 'len(values) == 0', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L570: IF `depth == max_depth`; body=1 else=0
  - L559: IF `state.is_terminal`; body=1 else=0
- LLM/model/env calls:
  - L556: `generate_new_states`
  - L562: `generate_prompt`
- Main call graph hints: `values.index`, `len`, `generate_new_states`, `generate_prompt`, `get_values`, `max`
#### `select_node(node)` (L574)
- Inputs: parameters `select_node(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L600: `node`
  - L591: `node_with_reward_1`
- Loops:
  - L575: {'line': 575, 'type': 'while', 'test': 'node and node.children', 'body_len': 9, 'orelse_len': 0}
  - L595: {'line': 595, 'type': 'while', 'test': 'node.is_terminal and node.reward != 1', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L581: IF `len(terminal_children) == len(node.children)`; body=4 else=0
  - L589: IF `node_with_reward_1`; body=2 else=0
  - L583: IF `node.parent`; body=1 else=0
- Main call graph hints: `logging.info`, `next`, `max`, `len`, `node.parent.children.remove`, `child.uct`, `node.uct`
#### `expand_node(node, args, task, idx)` (L602)
- Inputs: parameters `expand_node(node, args, task, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L606: `None`
- Decisions / conditions:
  - L604: IF `node.depth >= 15`; body=2 else=0
  - L607: IF `node.depth == 0`; body=1 else=0
- LLM/model/env calls:
  - L609: `generate_new_states`
- Main call graph hints: `generate_new_states`, `node.children.extend`, `logging.info`
#### `generate_new_states(node, args, task, idx, n)` (L612)
- Inputs: parameters `generate_new_states(node, args, task, idx, n)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L676: `list(unique_states.values())`
- Loops:
  - L620: {'line': 620, 'type': 'for', 'target': 'action', 'iter': 'sampled_actions', 'body_len': 7, 'orelse_len': 0}
- Decisions / conditions:
  - L633: IF `action_line`; body=13 else=0
  - L646: IF `action.startswith('think')`; body=1 else=0
  - L656: IF `r > 0 or done`; body=2 else=0
  - L665: IF `new_node.is_terminal and r < 1.0 and (r > 0.0) and (added == False)`; body=3 else=0
  - L671: IF `r not in existing_rewards`; body=3 else=0
- Exception handling:
  - L634: handlers=['AssertionError'] final=0
- LLM/model/env calls:
  - L614: `generate_prompt`
- I/O/env/executor calls:
  - L635: `env.step`
- Main call graph hints: `generate_prompt`, `get_samples`, `logging.info`, `list`, `copy.deepcopy`, `node.state.copy`, `next`, `unique_states.values`, `action.startswith`, `env.clone_state`, `Node`, `line.split[...].strip`, `env.step`, `collect_trajectory`, `action.split`, `print`, `failed_trajectories.append`, `line.startswith`, `line.split`
#### `evaluate_node(node, args, task, idx)` (L679)
- Inputs: parameters `evaluate_node(node, args, task, idx)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L705: `sum(votes) / len(votes) if votes else 0`
- Loops:
  - L698: {'line': 698, 'type': 'for', 'target': '(i, condition)', 'iter': 'enumerate(terminal_conditions)', 'body_len': 1, 'orelse_len': 0}
  - L702: {'line': 702, 'type': 'for', 'target': '(i, child)', 'iter': 'enumerate(node.children)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L694: IF `max_vote == 0`; body=1 else=0
  - L699: IF `condition == 1`; body=1 else=0
- LLM/model/env calls:
  - L683: `generate_prompt`
- Main call graph hints: `get_values`, `logging.info`, `enumerate`, `generate_prompt`, `max`, `sum`, `len`
#### `print_tree(node, level)` (L708)
- Inputs: parameters `print_tree(node, level)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L711: {'line': 711, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `print`, `print_tree`
#### `backpropagate(node, value)` (L714)
- Inputs: parameters `backpropagate(node, value)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L715: {'line': 715, 'type': 'while', 'test': 'node', 'body_len': 4, 'orelse_len': 0}
- Main call graph hints: `logging.info`
#### `generate_prompt(node)` (L725)
- Inputs: parameters `generate_prompt(node)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L736: `question + '\n\n'.join(reversed(trajectory))`
- Loops:
  - L728: {'line': 728, 'type': 'while', 'test': 'node', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L730: IF `node.state['action']`; body=1 else=0
  - L732: IF `node.state['observation'] and node.depth != 0`; body=1 else=0
- Main call graph hints: `trajectory.append`, `Constant.join`, `new_segment.append`, `reversed`

---

## File: `webshop/models.py`

**Lines:** 75  

### Imports
- `import os`
- `import openai`
- `import backoff`
- `from transformers import GPT2Tokenizer`

### Module assignments
- L6: `completion_tokens = prompt_tokens = 0`
- L7: `MAX_TOKENS = 15000`
- L8: `tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')`
- L10: `api_key = os.getenv("OPENAI_API_KEY", "")`
- L16: `api_base = os.getenv("OPENAI_API_BASE", "")`

### Prompt-like assignments
- L28 `response`: `response = openai.Completion.create( engine=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens, n=1, stop=stop )`
- L69 `cost`: `cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03`
- L71 `cost`: `cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.0015`
- L73 `cost`: `cost = completion_tokens / 1000 * 0.004 + prompt_tokens / 1000 * 0.003`

### Top-level logic
- L11 If: `if api_key != "": openai.api_key = api_key else: print("Warning: OPENAI_API_KEY is not set")`
- L17 If: `if api_base != "": print("Warning: OPENAI_API_BASE is set to {}".format(api_base)) openai.api_base = api_base`

### Classes
- None

### Functions
#### `completions_with_backoff(**kwargs)` (L22)
- Inputs: parameters `completions_with_backoff(**kwargs)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L23: `openai.ChatCompletion.create(**kwargs)`
- LLM/model/env calls:
  - L23: `openai.ChatCompletion.create`
- I/O/env/executor calls:
  - L23: `openai.ChatCompletion.create`
- Main call graph hints: `backoff.on_exception`, `openai.ChatCompletion.create`
#### `gpt3(prompt, model, temperature, max_tokens, n, stop)` (L25)
- Inputs: parameters `gpt3(prompt, model, temperature, max_tokens, n, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L37: `outputs`
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '_', 'iter': 'range(n)', 'body_len': 2, 'orelse_len': 0}
- LLM/model/env calls:
  - L28: `openai.Completion.create`
- I/O/env/executor calls:
  - L28: `openai.Completion.create`
- Main call graph hints: `range`, `openai.Completion.create`, `outputs.append`, `response.choices[...].text.strip`
#### `gpt(prompt, model, temperature, max_tokens, n, stop)` (L39)
- Inputs: parameters `gpt(prompt, model, temperature, max_tokens, n, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L41: `gpt3(prompt, model, temperature, max_tokens, n, stop)`
  - L44: `chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)`
- Decisions / conditions:
  - L40: IF `model == 'test-davinci-002'`; body=1 else=2
- LLM/model/env calls:
  - L41: `gpt3`
  - L44: `chatgpt`
- Main call graph hints: `gpt3`, `chatgpt`
#### `gpt4(prompt, model, temperature, max_tokens, n, stop)` (L46)
- Inputs: parameters `gpt4(prompt, model, temperature, max_tokens, n, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L48: `gpt3(prompt, model, temperature, max_tokens, n, stop)`
  - L51: `chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)`
- Decisions / conditions:
  - L47: IF `model == 'test-davinci-002'`; body=1 else=2
- LLM/model/env calls:
  - L48: `gpt3`
  - L51: `chatgpt`
- Main call graph hints: `gpt3`, `chatgpt`
#### `chatgpt(messages, model, temperature, max_tokens, n, stop)` (L53)
- Inputs: parameters `chatgpt(messages, model, temperature, max_tokens, n, stop)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L64: `outputs`
- Loops:
  - L56: {'line': 56, 'type': 'while', 'test': 'n > 0', 'body_len': 6, 'orelse_len': 0}
- LLM/model/env calls:
  - L59: `completions_with_backoff`
- Main call graph hints: `min`, `completions_with_backoff`, `outputs.extend`
#### `gpt_usage(backend)` (L66)
- Inputs: parameters `gpt_usage(backend)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L74: `{'completion_tokens': completion_tokens, 'prompt_tokens': prompt_tokens, 'cost': cost}`
- Decisions / conditions:
  - L68: IF `backend == 'gpt-4'`; body=1 else=1
  - L70: IF `backend == 'gpt-3.5-turbo'`; body=1 else=1
  - L72: IF `backend == 'gpt-3.5-turbo-16k'`; body=1 else=0

---

## File: `webshop/prompt.py`

**Lines:** 442  

### Imports
- None

### Module assignments
- L1: `prompt1 = """Webshop Instruction: i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars [Search] Action: search[3 ounce bright citrus deodorant sensitive skin] Observation: [Back to Search] Page 1 (Total results: 50) [Next >] [B078GWRC1J] Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfee...`
- L53: `prompt1_feedback = """You are also an advanced reasoning agent that can improve based on self refection. Follow the instruction and purchase an item meeting all of the correct specifications by navigating the website. Here is an example: Webshop Instruction: i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars [Search] Action: search[3 ...`
- L109: `score_prompt = '''Given an item to purchase and a trajectory that aims to buy an item that exactly matches the specification, which corresponds to the ideal score of 1.0, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10. Here are some examples Webshop Instruction: i am looking for dairy free and apple variet...`
- L190: `score_prompt_feedback = '''Given an item to purchase and a trajectory, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10. Here are some examples Webshop Instruction: i am looking for dairy free and apple variety pack of chips, and price lower than 30.00 dollars [Search] Action: search[dairy free and apple var...`
- L272: `prompt1_actonly = """Webshop Instruction: i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars [Search] Action: search[3 ounce bright citrus deodorant sensitive skin] Observation: [Back to Search] Page 1 (Total results: 50) [Next >] [B078GWRC1J] Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and B...`
- L315: `reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an shopping website and a specific type of item to buy. You were given access to relevant context and a item to purchase. You were unsuccessful in buying the correct item either because you did not find an item meetin...`

### Prompt-like assignments
- L1 `prompt1`: `prompt1 = """Webshop Instruction: i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars [Search] Action: search[3 ounce bright citrus deodorant sensitive skin] Observation: [Back to Search] Page 1 (Total results: 50) [Next >] [B078GWRC1J] ...`
- L53 `prompt1_feedback`: `prompt1_feedback = """You are also an advanced reasoning agent that can improve based on self refection. Follow the instruction and purchase an item meeting all of the correct specifications by navigating the website. Here is an example: Webshop Instruction: i would like a 3 ounce bottle of brigh...`
- L109 `score_prompt`: `score_prompt = '''Given an item to purchase and a trajectory that aims to buy an item that exactly matches the specification, which corresponds to the ideal score of 1.0, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer fr...`
- L190 `score_prompt_feedback`: `score_prompt_feedback = '''Given an item to purchase and a trajectory, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10. Here are some examples Webshop Instruction: i am looking for dairy free and apple variet...`
- L272 `prompt1_actonly`: `prompt1_actonly = """Webshop Instruction: i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars [Search] Action: search[3 ounce bright citrus deodorant sensitive skin] Observation: [Back to Search] Page 1 (Total results: 50) [Next >] [B078...`
- L315 `reflection_prompt`: `reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an shopping website and a specific type of item to buy. You were given access to relevant context and a item to purch...`

### Classes
- None

### Functions
- None

---

## File: `webshop/run.py`

**Lines:** 65  

### Imports
- `import os`
- `import json`
- `import argparse`
- `import logging`
- `from models import gpt_usage`
- `from lats import lats_search`
- `from webshop import WebShopTask`

### Module assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L62 If: `if __name__ == '__main__': args = parse_args() print(args) run(args)`

### Classes
- None

### Functions
#### `run(args)` (L12)
- Inputs: parameters `run(args)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L24: {'line': 24, 'type': 'for', 'target': 'i', 'iter': 'range(args.task_start_index, args.task_end_index)', 'body_len': 7, 'orelse_len': 0}
- Decisions / conditions:
  - L34: IF `(i + 1) % 1 == 0`; body=3 else=0
- LLM/model/env calls:
  - L44: `gpt_usage`
- Main call graph hints: `WebShopTask`, `print`, `logging.basicConfig`, `range`, `lats_search`, `task_accs.append`, `logging.info`, `gpt_usage`, `sum`, `len`
#### `parse_args()` (L46)
- Inputs: parameters `parse_args()` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L59: `args`
- Main call graph hints: `argparse.ArgumentParser`, `args.add_argument`, `args.parse_args`

---

## File: `webshop/webshop.py`

**Lines:** 227  

### Imports
- `import os`
- `import re`
- `from base import Task`
- `from prompt import *`
- `from models import gpt, gpt4`
- `import logging`
- `import random`
- `from transformers import GPT2Tokenizer`

### Module assignments
- L10: `tokenizer = GPT2Tokenizer.from_pretrained("gpt2")`
- L15: `max_token_length = 15000`

### Prompt-like assignments
- L61 `reflect_prompt`: `reflect_prompt = reflection_prompt.format(trajectory=traj)`
- L65 `traj_with_reflection`: `traj_with_reflection = traj + "Reflection: " + reflection[0] + "\n"`
- L67 `reflection_mapping`: `reflection_mapping = { 'question': question, 'reflection': reflection[0] }`
- L157 `prompt`: `prompt = compare_prompt + f'Action 1:{last_actions[0]}\n\nAction 2:{last_actions[1]}\n'`
- L84 `reflect_prompt`: `reflect_prompt = reflection_prompt.format(trajectory=traj)`
- L109 `prompt`: `prompt = prompt1_feedback.format(trajectories=trajectories, input=input)`
- L193 `prompt`: `prompt = score_prompt_feedback.format(s="", trajectories=failed_trajectories, input=inp)`
- L106 `traj_with_reflection`: `traj_with_reflection = reflection_mapping['trajectory'] + "Reflection: " + reflection_mapping['reflection'] + "\n"`
- L188 `new_trajectory`: `new_trajectory = 'Action: '.join([first_part] + remaining_parts)`

### Classes
#### Class `WebShopTask` L17 bases=['Task']
- Docstring: Input (x)   : a text instruction
Output (y)  : a text generation
Reward (r)  : # TODO
Input Example: 
Output Example: 
##### `__init__(self)` (L25)
- Docstring: file: a text file, each line is some sentences
- Inputs: parameters `__init__(self)` plus args/task/env/model/search state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `super`
##### `test_output(self, idx, output)` (L35)
- Inputs: parameters `test_output(self, idx, output)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L52: `info`
- Loops:
  - L40: {'line': 40, 'type': 'for', 'target': 'score_output', 'iter': 'score_outputs', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L44: IF `match`; body=2 else=1
- LLM/model/env calls:
  - L38: `gpt`
- Main call graph hints: `gpt`, `print`, `output.split`, `re.match`, `int`, `scores.append`, `sum`, `len`, `match.groups`
##### `standard_prompt_wrap(x, y)` (L55)
- Inputs: parameters `standard_prompt_wrap(x, y)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L56: `standard_prompt.format(input=x) + y`
- Main call graph hints: `standard_prompt.format`
##### `generate_self_reflection(traj, question)` (L59)
- Inputs: parameters `generate_self_reflection(traj, question)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L72: `(traj_with_reflection, reflection_mapping)`
- LLM/model/env calls:
  - L63: `gpt4`
- Main call graph hints: `reflection_prompt.format`, `gpt4`
##### `generate_self_reflection(z, question)` (L75)
- Inputs: parameters `generate_self_reflection(z, question)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L96: `reflection_mapping`
- Loops:
  - L82: {'line': 82, 'type': 'for', 'target': 'traj', 'iter': 'failed_trajectories', 'body_len': 5, 'orelse_len': 0}
- LLM/model/env calls:
  - L86: `gpt`
- Main call graph hints: `random.sample`, `min`, `reflection_prompt.format`, `gpt`, `reflection_mapping.append`, `len`, `isinstance`
##### `cot_prompt_wrap(x, y, reflection_mapping_list)` (L99)
- Inputs: parameters `cot_prompt_wrap(x, y, reflection_mapping_list)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L110: `prompt`
  - L112: `prompt1.format(input=input)`
- Loops:
  - L105: {'line': 105, 'type': 'for', 'target': 'reflection_mapping', 'iter': 'reflection_mapping_list', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L104: IF `reflection_mapping_list`; body=3 else=1
- Main call graph hints: `prompt1_feedback.format`, `prompt1.format`
##### `vote_prompt_wrap(x, ys)` (L117)
- Inputs: parameters `vote_prompt_wrap(x, ys)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L123: `prompt`
- Loops:
  - L119: {'line': 119, 'type': 'for', 'target': '(i, y)', 'iter': 'enumerate(ys, 1)', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `enumerate`
##### `vote_outputs_unwrap(vote_outputs, n_candidates)` (L126)
- Inputs: parameters `vote_outputs_unwrap(vote_outputs, n_candidates)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L137: `vote_results`
- Loops:
  - L128: {'line': 128, 'type': 'for', 'target': 'vote_output', 'iter': 'vote_outputs', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L131: IF `match`; body=2 else=1
  - L133: IF `vote in range(n_candidates)`; body=1 else=0
- Main call graph hints: `re.match`, `print`, `int`, `range`, `match.groups`
##### `compare_prompt_wrap(x, ys)` (L140)
- Inputs: parameters `compare_prompt_wrap(x, ys)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L158: `prompt`
- Loops:
  - L145: {'line': 145, 'type': 'for', 'target': 'y', 'iter': 'ys', 'body_len': 2, 'orelse_len': 0}
  - L148: {'line': 148, 'type': 'for', 'target': 'line', 'iter': 'lines', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L150: IF `'Action' in line`; body=2 else=0
- Main call graph hints: `len`, `y.split`, `last_actions.append`, `line.split[...].strip`, `line.split`
##### `compare_output_unwrap(compare_output)` (L162)
- Inputs: parameters `compare_output_unwrap(compare_output)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L164: `0`
  - L166: `1`
  - L168: `0.5`
  - L171: `-1`
- Decisions / conditions:
  - L163: IF `'more correct trajectory is 1' in compare_output`; body=1 else=1
  - L165: IF `'more correct trajectory is 2' in compare_output`; body=1 else=1
  - L167: IF `'two trajectories are similarly correct' in compare_output`; body=1 else=2
- Main call graph hints: `print`
##### `value_prompt_wrap(x, y, z, reflections)` (L174)
- Inputs: parameters `value_prompt_wrap(x, y, z, reflections)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L198: `prompt`
- Loops:
  - L178: {'line': 178, 'type': 'for', 'target': '(traj, ref)', 'iter': 'zip(z, reflections)', 'body_len': 8, 'orelse_len': 0}
- Decisions / conditions:
  - L176: IF `len(z) != 0`; body=4 else=2
- Main call graph hints: `x.split`, `len`, `zip`, `score_prompt_feedback.format`, `score_prompt.format`, `trajectory.split`, `Constant.join`, `int`
##### `value_outputs_unwrap(evaluate_prompt)` (L202)
- Inputs: parameters `value_outputs_unwrap(evaluate_prompt)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L205: `1.0`
  - L207: `0.9`
  - L209: `0.8`
  - L211: `0.7`
  - L213: `0.6`
  - L215: `0.5`
  - L217: `0.4`
  - L219: `0.3`
  - L221: `0.2`
  - L223: `0.1`
  - L225: `-1`
- Decisions / conditions:
  - L204: IF `'10' in evaluate_prompt`; body=1 else=1
  - L206: IF `'9' in evaluate_prompt`; body=1 else=1
  - L208: IF `'8' in evaluate_prompt`; body=1 else=1
  - L210: IF `'7' in evaluate_prompt`; body=1 else=1
  - L212: IF `'6' in evaluate_prompt`; body=1 else=1
  - L214: IF `'5' in evaluate_prompt`; body=1 else=1
  - L216: IF `'4' in evaluate_prompt`; body=1 else=1
  - L218: IF `'3' in evaluate_prompt`; body=1 else=1
  - L220: IF `'2' in evaluate_prompt`; body=1 else=1
  - L222: IF `'1' in evaluate_prompt`; body=1 else=1

### Functions
#### `get_token_length(text)` (L12)
- Inputs: parameters `get_token_length(text)` plus args/task/env/model/search state as referenced.
- Outputs / returns:
  - L13: `len(tokenizer.encode(text))`
- Main call graph hints: `len`, `tokenizer.encode`