# Reflexion — Complete Python Logic / Flow / Loops / Conditions / I-O Extraction

Source repo: `https://github.com/noahshinn/reflexion`  
Audited commit: `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

## System summary

Reflexion wraps an agent loop in a trial loop. Each trial executes actions in an environment or program executor, receives reward/error/test feedback, generates natural-language reflection, stores reflection in memory, and uses memory in later trials. Implementations cover AlfWorld, WebShop, HotPotQA, HumanEval/MBPP/LeetCode programming, and related baselines.

## Python files

- `alfworld_runs/alfworld_trial.py`
- `alfworld_runs/env_history.py`
- `alfworld_runs/generate_reflections.py`
- `alfworld_runs/main.py`
- `alfworld_runs/utils.py`
- `hotpotqa_runs/agents.py`
- `hotpotqa_runs/environment.py`
- `hotpotqa_runs/fewshots.py`
- `hotpotqa_runs/llm.py`
- `hotpotqa_runs/mocks.py`
- `hotpotqa_runs/prompts.py`
- `hotpotqa_runs/react.py`
- `hotpotqa_runs/tests.py`
- `hotpotqa_runs/util.py`
- `programming_runs/dataset_random_sample.py`
- `programming_runs/evaluate_leet_results.py`
- `programming_runs/evaluate_rs_leet_results.py`
- `programming_runs/executors/__init__.py`
- `programming_runs/executors/executor_types.py`
- `programming_runs/executors/executor_utils.py`
- `programming_runs/executors/factory.py`
- `programming_runs/executors/leet_executor.py`
- `programming_runs/executors/py_executor.py`
- `programming_runs/executors/rs_executor.py`
- `programming_runs/generate_dataset.py`
- `programming_runs/generators/__init__.py`
- `programming_runs/generators/factory.py`
- `programming_runs/generators/generator_types.py`
- `programming_runs/generators/generator_utils.py`
- `programming_runs/generators/model.py`
- `programming_runs/generators/parse.py`
- `programming_runs/generators/py_generate.py`
- `programming_runs/generators/rs_generate.py`
- `programming_runs/human-eval/human_eval/__init__.py`
- `programming_runs/human-eval/human_eval/data.py`
- `programming_runs/human-eval/human_eval/evaluate_functional_correctness.py`
- `programming_runs/human-eval/human_eval/evaluation.py`
- `programming_runs/human-eval/human_eval/execution.py`
- `programming_runs/human-eval/setup.py`
- `programming_runs/humaneval_result_sort.py`
- `programming_runs/immediate_refinement.py`
- `programming_runs/immediate_reflexion.py`
- `programming_runs/main.py`
- `programming_runs/reflexion.py`
- `programming_runs/reflexion_ucs.py`
- `programming_runs/simple.py`
- `programming_runs/test_acc.py`
- `programming_runs/utils.py`
- `programming_runs/validate_py_results.py`
- `programming_runs/validate_rs_results.py`
- `webshop_runs/env_history.py`
- `webshop_runs/generate_reflections.py`
- `webshop_runs/main.py`
- `webshop_runs/utils.py`
- `webshop_runs/webshop_trial.py`

---

## File: `alfworld_runs/alfworld_trial.py`

**Lines:** 162  

**Module docstring:** Adapted from https://github.com/ysymyth/ReAct/blob/master/alfworld.ipynb

### Imports
- `import os`
- `import sys`
- `import json`
- `import yaml`
- `import openai`
- `import importlib`
- `import alfworld`
- `import alfworld.agents.environment`
- `from utils import Model, get_chat, get_completion`
- `from env_history import EnvironmentHistory`
- `from typing import List, Dict, Any, Tuple`

### Module-level assignments
- L16: `openai.api_key = os.environ["OPENAI_API_KEY"]`
- L17: `FOLDER = './prompts'`
- L18: `PROMPT_FILE = 'alfworld_3prompts.json'`
- L74: `PREFIXES = { 'pick_and_place': 'put', 'pick_clean_then_place': 'clean', 'pick_heat_then_place': 'heat', 'pick_cool_then_place': 'cool', 'look_at_obj': 'examine', 'pick_two_obj': 'puttwo' }`

### Prompt-like assignments
- L48 `env_history`: `env_history = EnvironmentHistory(base_prompt, ob, memory[-3:], [])`
- L50 `env_history`: `env_history = EnvironmentHistory(base_prompt, ob, memory, [])`
- L27 `text`: `text = get_completion(prompt=prompt, temperature=cur_try * 0.2, stop_strs=stop)`
- L29 `text`: `text = get_chat(prompt=prompt, model=model, temperature=cur_try * 0.2, stop_strs=stop)`
- L124 `base_prompt`: `base_prompt = 'Interact with a household to solve a task. Here are two examples.\n' + d[f'react_{v}_1'] + d[f'react_{v}_0']`
- L125 ``: `final_env_history, is_success = alfworld_run(env, base_prompt, env_config["memory"] if use_memory else [], to_print=True, ob=ob, model=model)`

### Classes
- None

### Functions
#### `llm(prompt, model, stop)` (L22)
- Inputs: parameters `llm(prompt, model, stop)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L34: `''`
  - L32: `text`
- Loops:
  - L25: {'line': 25, 'type': 'while', 'test': 'cur_try < 6', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L26: IF `model == 'text-davinci-003'`; body=1 else=1
  - L31: IF `len(text.strip()) >= 5`; body=1 else=0
- Exception handling:
  - L23: handlers=['Exception'] final=0
- LLM/model calls:
  - L27: `get_completion`
  - L29: `get_chat`
- Main call graph hints: `print`, `sys.exit`, `get_completion`, `get_chat`, `len`, `text.strip`
#### `process_ob(ob)` (L41)
- Inputs: parameters `process_ob(ob)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L44: `ob`
- Decisions / conditions:
  - L42: IF `ob.startswith('You arrive at loc ')`; body=1 else=0
- Main call graph hints: `ob.startswith`, `ob.find`
#### `alfworld_run(env, base_prompt, memory, to_print, ob, model)` (L46)
- Inputs: parameters `alfworld_run(env, base_prompt, memory, to_print, ob, model)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L72: `(env_history, False)`
  - L68: `(env_history, True)`
  - L70: `(env_history, False)`
- Loops:
  - L56: {'line': 56, 'type': 'while', 'test': 'cur_step < 49', 'body_len': 9, 'orelse_len': 0}
- Decisions / conditions:
  - L47: IF `len(memory) > 3`; body=1 else=1
  - L52: IF `to_print`; body=2 else=0
  - L61: IF `action.startswith('think:')`; body=1 else=0
  - L64: IF `to_print`; body=2 else=0
  - L67: IF `done`; body=1 else=1
  - L69: IF `env_history.check_is_exhausted()`; body=1 else=0
- LLM/model calls:
  - L57: `llm.strip`
  - L57: `llm`
- Main call graph hints: `env_history.reset`, `len`, `EnvironmentHistory`, `print`, `sys.stdout.flush`, `llm.strip`, `env_history.add`, `env.step`, `action.startswith`, `process_ob`, `env_history.check_is_exhausted`, `llm`, `str`
#### `run_trial(trial_log_path, world_log_path, trial_idx, env_configs, use_memory, model)` (L83)
- Inputs: parameters `run_trial(trial_log_path, world_log_path, trial_idx, env_configs, use_memory, model)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L161: `env_configs`
- Loops:
  - L105: {'line': 105, 'type': 'for', 'target': '(z, env_config)', 'iter': 'enumerate(env_configs)', 'body_len': 6, 'orelse_len': 0}
  - L122: {'line': 122, 'type': 'for', 'target': '(i, (k, v))', 'iter': 'enumerate(PREFIXES.items())', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L112: IF `env_config['is_success']`; body=4 else=0
  - L123: IF `name.startswith(k)`; body=5 else=0
  - L128: IF `is_success`; body=4 else=1
- I/O calls:
  - L94: `open`
  - L156: `open`
  - L157: `wf.write`
  - L158: `open`
  - L159: `wf.write`
  - L116: `open`
  - L117: `wf.write`
  - L118: `open`
  - L119: `wf.write`
  - L137: `open`
  - L138: `f.write`
  - L141: `open`
  - L142: `wf.write`
- Main call graph hints: `importlib.reload`, `getattr`, `env.init_env`, `len`, `enumerate`, `env.close`, `open`, `yaml.safe_load`, `env.reset`, `Constant.join`, `print`, `wf.write`, `PREFIXES.items`, `name.startswith`, `round`, `ob[...].split`, `info[...][...].split`, `alfworld_run`, `f.write`, `str`

---

## File: `alfworld_runs/env_history.py`

**Lines:** 53  

### Imports
- `from typing import List, Dict`

### Module-level assignments
- None

### Prompt-like assignments
- L6 `_cur_query`: `self._cur_query: str = f'{_get_base_query(base_query, start_info, memory)}'`

### Classes
#### Class `EnvironmentHistory` L4 bases=[]
##### `__init__(self, base_query, start_info, memory, history)` (L5)
- Inputs: parameters `__init__(self, base_query, start_info, memory, history)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `_get_base_query`
##### `add(self, label, value)` (L11)
- Inputs: parameters `add(self, label, value)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L17: IF `label == 'action'`; body=1 else=0
  - L18: IF `value == self._last_action`; body=1 else=1
##### `check_is_exhausted(self)` (L23)
- Inputs: parameters `check_is_exhausted(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L24: `self._is_exhausted`
##### `reset(self)` (L26)
- Inputs: parameters `reset(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `__str__(self)` (L29)
- Inputs: parameters `__str__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L41: `s`
- Loops:
  - L31: {'line': 31, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(self._history)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L32: IF `item['label'] == 'action'`; body=1 else=1
  - L39: IF `i != len(self._history) - 1`; body=1 else=0
  - L34: IF `item['label'] == 'observation'`; body=1 else=1
  - L37: IF `item['label'] == 'human_edit'`; body=1 else=0
- Main call graph hints: `enumerate`, `len`

### Functions
#### `_get_base_query(base_query, start_info, memory)` (L43)
- Inputs: parameters `_get_base_query(base_query, start_info, memory)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L52: `query`
- Loops:
  - L49: {'line': 49, 'type': 'for', 'target': '(i, m)', 'iter': 'enumerate(memory)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L47: IF `len(memory) > 0`; body=2 else=0
- Main call graph hints: `len`, `enumerate`, `m.strip`

---

## File: `alfworld_runs/generate_reflections.py`

**Lines:** 48  

### Imports
- `from utils import get_completion`
- `from typing import List, Dict, Any`

### Module-level assignments
- None

### Prompt-like assignments
- L15 `query`: `query: str = f"""You will be given the history of a past experience in which you were placed in an environment and given a task to complete. You were unsuccessful in completing the task. Do not summarize your environment, but rather think about the strategy and path you took to attempt to complet...`
- L43 `reflection_query`: `reflection_query: str = _generate_reflection_query(env_logs[i], memory)`

### Classes
- None

### Functions
#### `_get_scenario(s)` (L8)
- Docstring: Parses the relevant scenario from the experience log.
- Inputs: parameters `_get_scenario(s)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L10: `s.split('Here is the task:')[-1].strip()`
- Main call graph hints: `s.split[...].strip`, `s.split`
#### `_generate_reflection_query(log_str, memory)` (L12)
- Docstring: Allows the Agent to reflect upon a past experience.
- Inputs: parameters `_generate_reflection_query(log_str, memory)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L27: `query`
- Loops:
  - L23: {'line': 23, 'type': 'for', 'target': '(i, m)', 'iter': 'enumerate(memory)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L21: IF `len(memory) > 0`; body=2 else=0
- Main call graph hints: `_get_scenario`, `len`, `enumerate`
#### `update_memory(trial_log_path, env_configs)` (L29)
- Docstring: Updates the given env_config with the appropriate reflections.
- Inputs: parameters `update_memory(trial_log_path, env_configs)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L47: `env_configs`
- Loops:
  - L36: {'line': 36, 'type': 'for', 'target': '(i, env)', 'iter': 'enumerate(env_configs)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L38: IF `not env['is_success'] and (not env['skip'])`; body=4 else=0
  - L39: IF `len(env['memory']) > 3`; body=1 else=1
- LLM/model calls:
  - L43: `_generate_reflection_query`
  - L44: `get_completion`
- I/O calls:
  - L31: `open`
  - L32: `f.read`
- Main call graph hints: `full_log.split`, `print`, `enumerate`, `open`, `f.read`, `len`, `_generate_reflection_query`, `get_completion`

---

## File: `alfworld_runs/main.py`

**Lines:** 120  

### Imports
- `import os`
- `import json`
- `import argparse`
- `from alfworld_trial import run_trial`
- `from generate_reflections import update_memory`
- `from typing import Any, List, Dict`

### Module-level assignments
- None

### Prompt-like assignments
- L104 `env_configs`: `env_configs: List[Dict[str, Any]] = update_memory(trial_log_path, env_configs)`

### Top-level logic
- L117 If: `if __name__ == '__main__': args = get_args() main(args)`

### Classes
- None

### Functions
#### `get_args()` (L10)
- Inputs: parameters `get_args()` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L26: `args`
- Main call graph hints: `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`
#### `main(args)` (L28)
- Inputs: parameters `main(args)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L87: {'line': 87, 'type': 'while', 'test': 'trial_idx < args.num_trials', 'body_len': 10, 'orelse_len': 0}
  - L48: {'line': 48, 'type': 'for', 'target': 'i', 'iter': 'range(args.num_envs)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L29: IF `args.is_resume`; body=5 else=4
  - L59: IF `args.is_resume`; body=1 else=1
  - L30: IF `not os.path.exists(args.resume_dir)`; body=1 else=0
  - L36: IF `not os.path.exists(env_config_path)`; body=1 else=0
  - L42: IF `not os.path.exists(args.run_name)`; body=1 else=0
  - L94: IF `os.path.exists(trial_log_path)`; body=1 else=0
  - L96: IF `os.path.exists(trial_env_configs_log_path)`; body=1 else=0
  - L103: IF `args.use_memory`; body=1 else=0
- I/O calls:
  - L94: `os.path.exists`
  - L96: `os.path.exists`
  - L30: `os.path.exists`
  - L36: `os.path.exists`
  - L38: `open`
  - L39: `json.load`
  - L42: `os.path.exists`
  - L88: `open`
  - L89: `wf.write`
  - L95: `open.close`
  - L97: `open.close`
  - L107: `open`
  - L108: `json.dump`
  - L111: `open`
  - L112: `wf.write`
  - L95: `open`
  - L97: `open`
- Main call graph hints: `os.path.join`, `range`, `print`, `os.path.exists`, `run_trial`, `ValueError`, `open`, `json.load`, `os.makedirs`, `wf.write`, `open.close`, `update_memory`, `json.dump`

---

## File: `alfworld_runs/utils.py`

**Lines:** 52  

### Imports
- `import os`
- `import sys`
- `import openai`
- `from tenacity import ( retry, stop_after_attempt, # type: ignore wait_random_exponential, # type: ignore )`
- `from typing import Optional, List`

### Module-level assignments
- L17: `Model = Literal["gpt-4", "gpt-3.5-turbo", "text-davinci-003"]`
- L19: `openai.api_key = os.getenv('OPENAI_API_KEY')`

### Prompt-like assignments
- L23 `response`: `response = openai.Completion.create( model='text-davinci-003', prompt=prompt, temperature=temperature, max_tokens=max_tokens, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=stop_strs, )`
- L38 `messages`: `messages = [ { "role": "user", "content": prompt } ]`
- L44 `response`: `response = openai.ChatCompletion.create( model=model, messages=messages, max_tokens=max_tokens, stop=stop_strs, temperature=temperature, )`

### Top-level logic
- L11 If: `if sys.version_info >= (3, 8): from typing import Literal else: from typing_extensions import Literal`

### Classes
- None

### Functions
#### `get_completion(prompt, temperature, max_tokens, stop_strs)` (L22)
- Inputs: parameters `get_completion(prompt, temperature, max_tokens, stop_strs)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L33: `response.choices[0].text`
- LLM/model calls:
  - L23: `openai.Completion.create`
- I/O calls:
  - L23: `openai.Completion.create`
- Main call graph hints: `retry`, `openai.Completion.create`, `wait_random_exponential`, `stop_after_attempt`
#### `get_chat(prompt, model, temperature, max_tokens, stop_strs, is_batched)` (L36)
- Inputs: parameters `get_chat(prompt, model, temperature, max_tokens, stop_strs, is_batched)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L51: `response.choices[0]['message']['content']`
- LLM/model calls:
  - L44: `openai.ChatCompletion.create`
- I/O calls:
  - L44: `openai.ChatCompletion.create`
- Main call graph hints: `retry`, `openai.ChatCompletion.create`, `wait_random_exponential`, `stop_after_attempt`

---

## File: `hotpotqa_runs/agents.py`

**Lines:** 394  

### Imports
- `import re, string, os`
- `from typing import List, Union, Literal`
- `from enum import Enum`
- `import tiktoken`
- `from langchain import OpenAI, Wikipedia`
- `from langchain.llms.base import BaseLLM`
- `from langchain.chat_models import ChatOpenAI`
- `from langchain.chat_models.base import BaseChatModel`
- `from langchain.schema import ( SystemMessage, HumanMessage, AIMessage, )`
- `from langchain.agents.react.base import DocstoreExplorer`
- `from langchain.docstore.base import Docstore`
- `from langchain.prompts import PromptTemplate`
- `from llm import AnyOpenAILLM`
- `from prompts import reflect_prompt, react_agent_prompt, react_reflect_agent_prompt, REFLECTION_HEADER, LAST_TRIAL_HEADER, REFLECTION_AFTER_LAST_TRIAL_HEADER`
- `from prompts import cot_agent_prompt, cot_reflect_agent_prompt, cot_reflect_prompt, COT_INSTRUCTION, COT_REFLECT_INSTRUCTION`
- `from fewshots import WEBTHINK_SIMPLE6, REFLECTIONS, COT, COT_REFLECT`

### Module-level assignments
- L334: `gpt2_enc = tiktoken.encoding_for_model("text-davinci-003")`

### Prompt-like assignments
- L111 `reflections_str`: `self.reflections_str = format_last_attempt(self.question , self.reflections[0])`
- L303 `reflections_str`: `self.reflections_str = format_last_attempt(self.question, self.reflections[0])`
- L114 `reflections_str`: `self.reflections_str = format_reflections(self.reflections)`
- L306 `reflections_str`: `self.reflections_str = format_reflections(self.reflections)`
- L116 `reflections_str`: `self.reflections_str = format_last_attempt(self.question , self.scratchpad)`
- L308 `reflections_str`: `self.reflections_str = format_last_attempt(self.question, self.scratchpad)`

### Classes
#### Class `ReflexionStrategy` L23 bases=['Enum']
- Docstring: NONE: No reflection
LAST_ATTEMPT: Use last reasoning trace in context 
REFLEXION: Apply reflexion to the next reasoning trace 
LAST_ATTEMPT_AND_REFLEXION: Use last reasoning trace in context and apply reflexion to the next reasoning trace 
#### Class `CoTAgent` L36 bases=[]
##### `__init__(self, question, context, key, agent_prompt, reflect_prompt, cot_examples, reflect_examples, self_reflect_llm, action_llm)` (L37)
- Inputs: parameters `__init__(self, question, context, key, agent_prompt, reflect_prompt, cot_examples, reflect_examples, self_reflect_llm, action_llm)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- LLM/model calls:
  - L45: `AnyOpenAILLM`
  - L51: `AnyOpenAILLM`
- Main call graph hints: `AnyOpenAILLM`, `self.reset`
##### `run(self, reflexion_strategy)` (L73)
- Inputs: parameters `run(self, reflexion_strategy)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L75: IF `self.step_n > 0 and (not self.is_correct()) and (reflexion_strategy != ReflexionStrategy.NONE)`; body=1 else=0
- Main call graph hints: `self.reset`, `self.step`, `self.reflect`, `self.is_correct`
##### `step(self)` (L81)
- Inputs: parameters `step(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L102: `None`
- Decisions / conditions:
  - L95: IF `action_type == 'Finish'`; body=4 else=1
  - L97: IF `self.is_correct()`; body=1 else=1
- Main call graph hints: `print`, `self.prompt_agent`, `parse_action`, `self.is_correct`, `self.scratchpad.split`
##### `reflect(self, strategy)` (L106)
- Inputs: parameters `reflect(self, strategy)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L109: IF `strategy == ReflexionStrategy.LAST_ATTEMPT`; body=2 else=1
  - L112: IF `strategy == ReflexionStrategy.REFLEXION`; body=2 else=1
  - L115: IF `strategy == ReflexionStrategy.LAST_ATTEMPT_AND_REFLEXION`; body=3 else=1
- Main call graph hints: `print`, `format_last_attempt`, `format_reflections`, `self.prompt_reflection`, `NotImplementedError`
##### `prompt_reflection(self)` (L123)
- Inputs: parameters `prompt_reflection(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L124: `format_step(self.self_reflect_llm(self._build_reflection_prompt()))`
- LLM/model calls:
  - L124: `self.self_reflect_llm`
- Main call graph hints: `format_step`, `self.self_reflect_llm`, `self._build_reflection_prompt`
##### `reset(self)` (L126)
- Inputs: parameters `reset(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `prompt_agent(self)` (L131)
- Inputs: parameters `prompt_agent(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L132: `format_step(self.action_llm(self._build_agent_prompt()))`
- LLM/model calls:
  - L132: `self.action_llm`
- Main call graph hints: `format_step`, `self.action_llm`, `self._build_agent_prompt`
##### `_build_agent_prompt(self)` (L134)
- Inputs: parameters `_build_agent_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L135: `self.agent_prompt.format(examples=self.cot_examples, reflections=self.reflections_str, context=self.context, question=self.question, scratchpad=self.scratchpad)`
- Main call graph hints: `self.agent_prompt.format`
##### `_build_reflection_prompt(self)` (L142)
- Inputs: parameters `_build_reflection_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L143: `self.reflect_prompt.format(examples=self.reflect_examples, context=self.context, question=self.question, scratchpad=self.scratchpad)`
- Main call graph hints: `self.reflect_prompt.format`
##### `is_finished(self)` (L149)
- Inputs: parameters `is_finished(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L150: `self.finished`
##### `is_correct(self)` (L152)
- Inputs: parameters `is_correct(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L153: `EM(self.answer, self.key)`
- Main call graph hints: `EM`
#### Class `ReactAgent` L155 bases=[]
##### `__init__(self, question, key, max_steps, agent_prompt, docstore, react_llm)` (L156)
- Inputs: parameters `__init__(self, question, key, max_steps, agent_prompt, docstore, react_llm)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- LLM/model calls:
  - L162: `AnyOpenAILLM`
- Main call graph hints: `Wikipedia`, `AnyOpenAILLM`, `DocstoreExplorer`, `tiktoken.encoding_for_model`, `self.__reset_agent`
##### `run(self, reset)` (L184)
- Inputs: parameters `run(self, reset)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L188: {'line': 188, 'type': 'while', 'test': 'not self.is_halted() and (not self.is_finished())', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L185: IF `reset`; body=1 else=0
- Main call graph hints: `self.__reset_agent`, `self.step`, `self.is_halted`, `self.is_finished`
##### `step(self)` (L191)
- Inputs: parameters `step(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L215: `None`
- Decisions / conditions:
  - L207: IF `action_type == 'Finish'`; body=5 else=0
  - L217: IF `action_type == 'Search'`; body=1 else=1
  - L209: IF `self.is_correct()`; body=1 else=1
  - L224: IF `action_type == 'Lookup'`; body=1 else=1
- Exception handling:
  - L218: handlers=['Exception'] final=0
  - L225: handlers=['ValueError'] final=0
- Main call graph hints: `print`, `self.prompt_agent`, `parse_action`, `self.is_correct`, `self.scratchpad.split`, `format_step`, `self.docstore.search`, `self.docstore.lookup`
##### `prompt_agent(self)` (L237)
- Inputs: parameters `prompt_agent(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L238: `format_step(self.llm(self._build_agent_prompt()))`
- LLM/model calls:
  - L238: `self.llm`
- Main call graph hints: `format_step`, `self.llm`, `self._build_agent_prompt`
##### `_build_agent_prompt(self)` (L240)
- Inputs: parameters `_build_agent_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L241: `self.agent_prompt.format(examples=self.react_examples, question=self.question, scratchpad=self.scratchpad)`
- Main call graph hints: `self.agent_prompt.format`
##### `is_finished(self)` (L246)
- Inputs: parameters `is_finished(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L247: `self.finished`
##### `is_correct(self)` (L249)
- Inputs: parameters `is_correct(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L250: `EM(self.answer, self.key)`
- Main call graph hints: `EM`
##### `is_halted(self)` (L252)
- Inputs: parameters `is_halted(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L253: `(self.step_n > self.max_steps or len(self.enc.encode(self._build_agent_prompt())) > 3896) and (not self.finished)`
- Main call graph hints: `len`, `self.enc.encode`, `self._build_agent_prompt`
##### `__reset_agent(self)` (L255)
- Inputs: parameters `__reset_agent(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `set_qa(self, question, key)` (L260)
- Inputs: parameters `set_qa(self, question, key)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
#### Class `ReactReflectAgent` L264 bases=['ReactAgent']
##### `__init__(self, question, key, max_steps, agent_prompt, reflect_prompt, docstore, react_llm, reflect_llm)` (L265)
- Inputs: parameters `__init__(self, question, key, max_steps, agent_prompt, reflect_prompt, docstore, react_llm, reflect_llm)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- LLM/model calls:
  - L272: `AnyOpenAILLM`
  - L278: `AnyOpenAILLM`
- Main call graph hints: `Wikipedia`, `AnyOpenAILLM`, `super.__init__`, `super`
##### `run(self, reset, reflect_strategy)` (L292)
- Inputs: parameters `run(self, reset, reflect_strategy)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L293: IF `(self.is_finished() or self.is_halted()) and (not self.is_correct())`; body=1 else=0
- Main call graph hints: `ReactAgent.run`, `self.reflect`, `self.is_finished`, `self.is_halted`, `self.is_correct`
##### `reflect(self, strategy)` (L298)
- Inputs: parameters `reflect(self, strategy)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L301: IF `strategy == ReflexionStrategy.LAST_ATTEMPT`; body=2 else=1
  - L304: IF `strategy == ReflexionStrategy.REFLEXION`; body=2 else=1
  - L307: IF `strategy == ReflexionStrategy.LAST_ATTEMPT_AND_REFLEXION`; body=3 else=1
- Main call graph hints: `print`, `format_last_attempt`, `format_reflections`, `self.prompt_reflection`, `NotImplementedError`
##### `prompt_reflection(self)` (L315)
- Inputs: parameters `prompt_reflection(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L316: `format_step(self.reflect_llm(self._build_reflection_prompt()))`
- LLM/model calls:
  - L316: `self.reflect_llm`
- Main call graph hints: `format_step`, `self.reflect_llm`, `self._build_reflection_prompt`
##### `_build_reflection_prompt(self)` (L319)
- Inputs: parameters `_build_reflection_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L320: `self.reflect_prompt.format(examples=self.reflect_examples, question=self.question, scratchpad=truncate_scratchpad(self.scratchpad, tokenizer=self.enc))`
- Main call graph hints: `self.reflect_prompt.format`, `truncate_scratchpad`
##### `_build_agent_prompt(self)` (L325)
- Inputs: parameters `_build_agent_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L326: `self.agent_prompt.format(examples=self.react_examples, reflections=self.reflections_str, question=self.question, scratchpad=self.scratchpad)`
- Main call graph hints: `self.agent_prompt.format`

### Functions
#### `parse_action(string)` (L336)
- Inputs: parameters `parse_action(string)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L343: `(action_type, argument)`
  - L346: `None`
- Decisions / conditions:
  - L340: IF `match`; body=3 else=1
- Main call graph hints: `re.match`, `match.group`
#### `format_step(step)` (L348)
- Inputs: parameters `format_step(step)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L349: `step.strip('\n').strip().replace('\n', '')`
- Main call graph hints: `step.strip.strip.replace`, `step.strip.strip`, `step.strip`
#### `format_reflections(reflections, header)` (L351)
- Inputs: parameters `format_reflections(reflections, header)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L354: `''`
  - L356: `header + 'Reflections:\n- ' + '\n- '.join([r.strip() for r in reflections])`
- Decisions / conditions:
  - L353: IF `reflections == []`; body=1 else=1
- Main call graph hints: `Constant.join`, `r.strip`
#### `format_last_attempt(question, scratchpad, header)` (L358)
- Inputs: parameters `format_last_attempt(question, scratchpad, header)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L361: `header + f'Question: {question}\n' + truncate_scratchpad(scratchpad, tokenizer=gpt2_enc).strip('\n').strip() + '\n(END PREVIOUS TRIAL)\n'`
- Main call graph hints: `truncate_scratchpad.strip.strip`, `truncate_scratchpad.strip`, `truncate_scratchpad`
#### `truncate_scratchpad(scratchpad, n_tokens, tokenizer)` (L363)
- Inputs: parameters `truncate_scratchpad(scratchpad, n_tokens, tokenizer)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L371: `'\n'.join(lines)`
- Loops:
  - L367: {'line': 367, 'type': 'while', 'test': "len(gpt2_enc.encode('\\n'.join(lines))) > n_tokens", 'body_len': 3, 'orelse_len': 0}
- LLM/model calls:
  - L367: `gpt2_enc.encode`
- Main call graph hints: `scratchpad.split`, `filter`, `sorted`, `Constant.join`, `len`, `observations_by_tokens.pop`, `lines.index`, `x.startswith`, `gpt2_enc.encode`, `largest_observation.split`, `tokenizer.encode`
#### `normalize_answer(s)` (L373)
- Inputs: parameters `normalize_answer(s)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L387: `white_space_fix(remove_articles(remove_punc(lower(s))))`
  - L375: `re.sub('\\b(a|an|the)\\b', ' ', text)`
  - L378: `' '.join(text.split())`
  - L382: `''.join((ch for ch in text if ch not in exclude))`
  - L385: `text.lower()`
- Main call graph hints: `white_space_fix`, `re.sub`, `Constant.join`, `set`, `text.lower`, `remove_articles`, `text.split`, `remove_punc`, `lower`
#### `EM(answer, key)` (L389)
- Inputs: parameters `EM(answer, key)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L390: `normalize_answer(answer) == normalize_answer(key)`
- Main call graph hints: `normalize_answer`

---

## File: `hotpotqa_runs/environment.py`

**Lines:** 102  

### Imports
- `import re`
- `import string`
- `from typing import Tuple`
- `import gym`
- `from langchain import Wikipedia`
- `from langchain.agents.react.base import DocstoreExplorer`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `QAEnv` L9 bases=['gym.Env']
##### `__init__(self, question, key, max_steps, explorer)` (L10)
- Inputs: parameters `__init__(self, question, key, max_steps, explorer)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `DocstoreExplorer`, `self.reset`, `Wikipedia`
##### `reset(self)` (L23)
- Inputs: parameters `reset(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `step(self, action)` (L28)
- Inputs: parameters `step(self, action)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L61: `(observation, reward, terminated, truncated, self.curr_step)`
- Decisions / conditions:
  - L31: IF `action_type == 'Finish'`; body=3 else=1
  - L33: IF `self.is_correct()`; body=1 else=1
  - L39: IF `action_type == 'Search'`; body=1 else=1
  - L46: IF `action_type == 'Lookup'`; body=1 else=1
- Exception handling:
  - L40: handlers=['Exception'] final=0
  - L47: handlers=['ValueError'] final=0
- Main call graph hints: `parse_action`, `self.is_correct`, `self.is_terminated`, `self.is_truncated`, `self.explorer.search.strip.strip`, `print`, `self.explorer.lookup.strip.strip`, `self.explorer.search.strip`, `self.explorer.lookup.strip`, `self.explorer.search`, `self.explorer.lookup`
##### `is_correct(self)` (L63)
- Inputs: parameters `is_correct(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L64: `EM(self.answer, self.key)`
- Main call graph hints: `EM`
##### `is_terminated(self)` (L66)
- Inputs: parameters `is_terminated(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L67: `self.terminated`
##### `is_truncated(self)` (L69)
- Inputs: parameters `is_truncated(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L70: `self.curr_step >= self.max_steps`

### Functions
#### `parse_action(string)` (L72)
- Inputs: parameters `parse_action(string)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L79: `(action_type, argument)`
  - L82: `(None, None)`
- Decisions / conditions:
  - L76: IF `match`; body=3 else=1
- Main call graph hints: `re.match`, `match.group`
#### `normalize_answer(s)` (L84)
- Inputs: parameters `normalize_answer(s)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L98: `white_space_fix(remove_articles(remove_punc(lower(s))))`
  - L86: `re.sub('\\b(a|an|the)\\b', ' ', text)`
  - L89: `' '.join(text.split())`
  - L93: `''.join((ch for ch in text if ch not in exclude))`
  - L96: `text.lower()`
- Main call graph hints: `white_space_fix`, `re.sub`, `Constant.join`, `set`, `text.lower`, `remove_articles`, `text.split`, `remove_punc`, `lower`
#### `EM(answer, key)` (L100)
- Inputs: parameters `EM(answer, key)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L101: `normalize_answer(answer) == normalize_answer(key)`
- Main call graph hints: `normalize_answer`

---

## File: `hotpotqa_runs/fewshots.py`

**Lines:** 198  

### Imports
- None

### Module-level assignments
- L1: `WEBTHINK_SIMPLE6 = """Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area. Action 1: Search[Colorado orogeny] Observation ...`
- L68: `REFLECTIONS = """ Previous Trial: Question: The Rome Protocols were signed by three Prime Ministers one of which was assassinated as part of what? Thought 1: I need to search Rome Protocols, find the three Prime Ministers, then find what they were assassinated as part of. Action 1: Search[Rome Protocols] Observation 1: The Rome Protocols were a ...`
- L107: `COTQA_SIMPLE6 = """ Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? Thought: Let's think step by step. The eastern sector of Colorado orogeny extends into the High Plains. High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft. Action: Finis...`
- L132: `COT_SIMPLE_REFLECTION = """ Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? Thought: Let's think step by step. The eastern sector of Colorado orogeny extends into the Rocky Mountains. The Rocky Mountains rise in elevation from around 1,800 to 14,000 ft, so the answer is 1,800 to 14...`
- L146: `COT = """Relevant Context: The Nile River is the longest river in the world, spanning approximately 6,650 kilometers (4,132 miles) in length. It flows through eleven countries in northeastern Africa, including Egypt, Sudan, and Uganda. Question: What is the longest river in the world? Thought: The question asks for the longest river in the world...`
- L162: `COT_REFLECT = """ Relevant Context: Ernest Hemingway's novel "The Old Man and the Sea" tells the story of Santiago, an aging Cuban fisherman, who struggles to catch a giant marlin in the Gulf Stream. The book won the Pulitzer Prize for Fiction in 1953 and contributed to Hemingway's Nobel Prize for Literature in 1954. Question: Which literary awa...`
- L178: `COT_REFLECT2 = """Relevant Context: The novel "To Kill a Mockingbird" was written by Harper Lee and published in 1960. The story takes place in the fictional town of Maycomb, Alabama during the Great Depression. The main characters are Scout Finch, her brother Jem, and their father Atticus Finch, a lawyer. Question: Where does "To Kill a Mocking...`

### Prompt-like assignments
- L68 `REFLECTIONS`: `REFLECTIONS = """ Previous Trial: Question: The Rome Protocols were signed by three Prime Ministers one of which was assassinated as part of what? Thought 1: I need to search Rome Protocols, find the three Prime Ministers, then find what they were assassinated as part of. Action 1: Search[Rome Pr...`
- L107 `COTQA_SIMPLE6`: `COTQA_SIMPLE6 = """ Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? Thought: Let's think step by step. The eastern sector of Colorado orogeny extends into the High Plains. High Plains rise in elevation from around 1,800 to 7,000 ft,...`
- L132 `COT_SIMPLE_REFLECTION`: `COT_SIMPLE_REFLECTION = """ Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? Thought: Let's think step by step. The eastern sector of Colorado orogeny extends into the Rocky Mountains. The Rocky Mountains rise in elevation from aroun...`
- L146 `COT`: `COT = """Relevant Context: The Nile River is the longest river in the world, spanning approximately 6,650 kilometers (4,132 miles) in length. It flows through eleven countries in northeastern Africa, including Egypt, Sudan, and Uganda. Question: What is the longest river in the world? Thought: Th...`
- L162 `COT_REFLECT`: `COT_REFLECT = """ Relevant Context: Ernest Hemingway's novel "The Old Man and the Sea" tells the story of Santiago, an aging Cuban fisherman, who struggles to catch a giant marlin in the Gulf Stream. The book won the Pulitzer Prize for Fiction in 1953 and contributed to Hemingway's Nobel Prize fo...`
- L178 `COT_REFLECT2`: `COT_REFLECT2 = """Relevant Context: The novel "To Kill a Mockingbird" was written by Harper Lee and published in 1960. The story takes place in the fictional town of Maycomb, Alabama during the Great Depression. The main characters are Scout Finch, her brother Jem, and their father Atticus Finch,...`

### Classes
- None

### Functions
- None

---

## File: `hotpotqa_runs/llm.py`

**Lines:** 29  

### Imports
- `from typing import Union, Literal`
- `from langchain.chat_models import ChatOpenAI`
- `from langchain import OpenAI`
- `from langchain.schema import ( HumanMessage )`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `AnyOpenAILLM` L8 bases=[]
##### `__init__(self, *args, **kwargs)` (L9)
- Inputs: parameters `__init__(self, *args, **kwargs)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L12: IF `model_name.split('-')[0] == 'text'`; body=2 else=2
- LLM/model calls:
  - L13: `OpenAI`
  - L16: `ChatOpenAI`
- Main call graph hints: `kwargs.get`, `OpenAI`, `ChatOpenAI`, `model_name.split`
##### `__call__(self, prompt)` (L19)
- Inputs: parameters `__call__(self, prompt)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L21: `self.model(prompt)`
  - L23: `self.model([HumanMessage(content=prompt)]).content`
- Decisions / conditions:
  - L20: IF `self.model_type == 'completion'`; body=1 else=1
- Main call graph hints: `self.model`, `HumanMessage`

### Functions
- None

---

## File: `hotpotqa_runs/mocks.py`

**Lines:** 43  

### Imports
- `from langchain.agents.react.base import DocstoreExplorer`
- `from langchain.llms.base import BaseLLM`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `LLMMock` L18 bases=['BaseLLM']
##### `__init__(self)` (L19)
- Inputs: parameters `__init__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `__call__(self, prompt)` (L22)
- Inputs: parameters `__call__(self, prompt)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L24: `reactLLMMock(prompt)`
  - L27: `reflectLLMMock(prompt)`
- Decisions / conditions:
  - L23: IF `prompt.split('\n')[0].split(' ')[0] == 'Solve'`; body=1 else=1
  - L26: IF `prompt.split('\n')[0].split(' ')[0] == 'You'`; body=1 else=1
- LLM/model calls:
  - L24: `reactLLMMock`
  - L27: `reflectLLMMock`
- Main call graph hints: `reactLLMMock`, `prompt.split[...].split`, `reflectLLMMock`, `Exception`, `prompt.split`
##### `get_num_tokens(self, text)` (L31)
- Inputs: parameters `get_num_tokens(self, text)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L32: `0`
#### Class `DocStoreExplorerMock` L34 bases=['DocstoreExplorer']
##### `__init__(self)` (L35)
- Inputs: parameters `__init__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `search(self, search, sents)` (L39)
- Inputs: parameters `search(self, search, sents)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L40: `self.summary`
##### `lookup(self, term)` (L42)
- Inputs: parameters `lookup(self, term)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L43: `self.body`

### Functions
#### `reactLLMMock(prompt)` (L4)
- Inputs: parameters `reactLLMMock(prompt)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L8: `'It does not mention the eastern sector. So I need to look up eastern sector.'`
  - L10: `'Lookup[eastern sector]'`
- Decisions / conditions:
  - L7: IF `last_action == 'thought'`; body=1 else=1
  - L9: IF `last_action == 'action'`; body=1 else=1
- Main call graph hints: `prompt.split[...].strip`, `last_line.split[...].lower`, `Exception`, `prompt.split`, `last_line.split`
#### `reflectLLMMock(prompt)` (L15)
- Inputs: parameters `reflectLLMMock(prompt)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L16: `'Last time i should have answered correctly'`

---

## File: `hotpotqa_runs/prompts.py`

**Lines:** 143  

### Imports
- `from langchain.prompts import PromptTemplate`

### Module-level assignments
- L3: `COT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given context that you should use to help you answer the question. Here are some examples: {examples} (END OF EXAMPLES) {refle...`
- L11: `COT_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given context that you should use to help you answer the question. Here are some examples: {examples} (END OF EX...`
- L21: `COT_REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to relevant context and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or t...`
- L32: `cot_agent_prompt = PromptTemplate( input_variables=["examples", "reflections", "context", "question", "scratchpad"], template = COT_INSTRUCTION, )`
- L37: `cot_reflect_agent_prompt = PromptTemplate( input_variables=["examples", "reflections", "context", "question", "scratchpad"], template = COT_AGENT_REFLECT_INSTRUCTION, )`
- L42: `cot_reflect_prompt = PromptTemplate( input_variables=["examples", "context", "question", "scratchpad"], template = COT_REFLECT_INSTRUCTION, )`
- L47: `COT_SIMPLE_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. Here are some examples: {examples} (END OF EXAMPLES) {reflections} {context} Question: {question}{scratchpad}"""`
- L55: `COT_SIMPLE_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. Here are some examples: {examples} (END OF EXAMPLES) {context} {reflections} Question: {question}{scratchpad}"""`
- L64: `COT_SIMPLE_REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discr...`
- L74: `cot_simple_agent_prompt = PromptTemplate( input_variables=["examples", "question", "reflections", "context", "scratchpad"], template = COT_SIMPLE_INSTRUCTION, )`
- L79: `cot_simple_reflect_agent_prompt = PromptTemplate( input_variables=["examples", "context", "reflections", "question", "scratchpad"], template = COT_SIMPLE_AGENT_REFLECT_INSTRUCTION, )`
- L84: `cot_simple_reflect_prompt = PromptTemplate( input_variables=["examples", "question", "context", "scratchpad"], template = COT_SIMPLE_REFLECT_INSTRUCTION, )`
- L90: `REACT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to ...`
- L100: `REACT_REFLECT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar enti...`
- L113: `REFLECTION_HEADER = 'You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'`
- L114: `REFLECTION_AFTER_LAST_TRIAL_HEADER = 'The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'`
- L115: `LAST_TRIAL_HEADER = 'You have attempted to answer the following question before and failed. Below is the last trial you attempted to answer the question.\n'`
- L117: `REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer...`
- L126: `react_agent_prompt = PromptTemplate( input_variables=["examples", "question", "scratchpad"], template = REACT_INSTRUCTION, )`
- L131: `react_reflect_agent_prompt = PromptTemplate( input_variables=["examples", "reflections", "question", "scratchpad"], template = REACT_REFLECT_INSTRUCTION, )`
- L136: `reflect_prompt = PromptTemplate( input_variables=["examples", "question", "scratchpad"], template = REFLECT_INSTRUCTION, )`

### Prompt-like assignments
- L3 `COT_INSTRUCTION`: `COT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given context that you should use to help you answer the question. Here are ...`
- L11 `COT_AGENT_REFLECT_INSTRUCTION`: `COT_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given context that you should use to help you answer the quest...`
- L21 `COT_REFLECT_INSTRUCTION`: `COT_REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to relevant context and a question to answer. You were unsuccessful in answering the question either because you g...`
- L32 `cot_agent_prompt`: `cot_agent_prompt = PromptTemplate( input_variables=["examples", "reflections", "context", "question", "scratchpad"], template = COT_INSTRUCTION, )`
- L37 `cot_reflect_agent_prompt`: `cot_reflect_agent_prompt = PromptTemplate( input_variables=["examples", "reflections", "context", "question", "scratchpad"], template = COT_AGENT_REFLECT_INSTRUCTION, )`
- L42 `cot_reflect_prompt`: `cot_reflect_prompt = PromptTemplate( input_variables=["examples", "context", "question", "scratchpad"], template = COT_REFLECT_INSTRUCTION, )`
- L47 `COT_SIMPLE_INSTRUCTION`: `COT_SIMPLE_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. Here are some examples: {examples} (END OF EXAMPLES) {reflections} {context} Ques...`
- L55 `COT_SIMPLE_AGENT_REFLECT_INSTRUCTION`: `COT_SIMPLE_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. Here are some examples: {examples} (END OF EXAMPLES) {context} {ref...`
- L64 `COT_SIMPLE_REFLECT_INSTRUCTION`: `COT_SIMPLE_REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer ...`
- L74 `cot_simple_agent_prompt`: `cot_simple_agent_prompt = PromptTemplate( input_variables=["examples", "question", "reflections", "context", "scratchpad"], template = COT_SIMPLE_INSTRUCTION, )`
- L79 `cot_simple_reflect_agent_prompt`: `cot_simple_reflect_agent_prompt = PromptTemplate( input_variables=["examples", "context", "reflections", "question", "scratchpad"], template = COT_SIMPLE_AGENT_REFLECT_INSTRUCTION, )`
- L84 `cot_simple_reflect_prompt`: `cot_simple_reflect_prompt = PromptTemplate( input_variables=["examples", "question", "context", "scratchpad"], template = COT_SIMPLE_REFLECT_INSTRUCTION, )`
- L90 `REACT_INSTRUCTION`: `REACT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists...`
- L100 `REACT_REFLECT_INSTRUCTION`: `REACT_REFLECT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: (1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if i...`
- L113 `REFLECTION_HEADER`: `REFLECTION_HEADER = 'You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'`
- L114 `REFLECTION_AFTER_LAST_TRIAL_HEADER`: `REFLECTION_AFTER_LAST_TRIAL_HEADER = 'The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'`
- L117 `REFLECT_INSTRUCTION`: `REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either becaus...`
- L126 `react_agent_prompt`: `react_agent_prompt = PromptTemplate( input_variables=["examples", "question", "scratchpad"], template = REACT_INSTRUCTION, )`
- L131 `react_reflect_agent_prompt`: `react_reflect_agent_prompt = PromptTemplate( input_variables=["examples", "reflections", "question", "scratchpad"], template = REACT_REFLECT_INSTRUCTION, )`
- L136 `reflect_prompt`: `reflect_prompt = PromptTemplate( input_variables=["examples", "question", "scratchpad"], template = REFLECT_INSTRUCTION, )`

### Classes
- None

### Functions
- None

---

## File: `hotpotqa_runs/react.py`

**Lines:** 173  

### Imports
- `import os`
- `from typing import List`
- `import dotenv`
- `import gym`
- `import tiktoken`
- `from langchain import OpenAI`
- `from langchain.llms.base import BaseLLM`
- `from langchain.prompts import PromptTemplate`
- `from environment import QAEnv`
- `from prompts import reflect_prompt, react_agent_prompt, react_reflect_agent_prompt, REFLECTION_HEADER`
- `from fewshots import WEBTHINK_SIMPLE6, REFLECTIONS`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `ReactAgent` L17 bases=[]
- Docstring: A question answering ReAct Agent.
##### `__init__(self, question, env, agent_prompt, react_llm)` (L21)
- Inputs: parameters `__init__(self, question, env, agent_prompt, react_llm)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- LLM/model calls:
  - L25: `OpenAI`
- Main call graph hints: `OpenAI`, `self.env.reset`, `self.reset`, `tiktoken.encoding_for_model`
##### `run(self, reset)` (L46)
- Inputs: parameters `run(self, reset)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L51: {'line': 51, 'type': 'while', 'test': 'not (self.is_truncated() or self.is_terminated())', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L47: IF `reset`; body=2 else=0
- Main call graph hints: `self.env.reset`, `self.reset`, `self.step`, `self.is_truncated`, `self.is_terminated`
##### `step(self)` (L54)
- Inputs: parameters `step(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `print`, `self.prompt_agent`, `self.env.step`, `self.scratchpad.split`
##### `prompt_agent(self)` (L72)
- Inputs: parameters `prompt_agent(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L73: `format_step(self.llm(self._build_agent_prompt()))`
- LLM/model calls:
  - L73: `self.llm`
- Main call graph hints: `format_step`, `self.llm`, `self._build_agent_prompt`
##### `_build_agent_prompt(self)` (L75)
- Inputs: parameters `_build_agent_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L76: `self.agent_prompt.format(examples=self.react_examples, question=self.question, scratchpad=self.scratchpad)`
- Main call graph hints: `self.agent_prompt.format`
##### `is_terminated(self)` (L81)
- Inputs: parameters `is_terminated(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L82: `self.env.is_terminated()`
- Main call graph hints: `self.env.is_terminated`
##### `is_correct(self)` (L84)
- Inputs: parameters `is_correct(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L85: `self.env.is_correct()`
- Main call graph hints: `self.env.is_correct`
##### `is_truncated(self)` (L87)
- Inputs: parameters `is_truncated(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L88: `self.env.is_truncated() or len(self.enc.encode(self._build_agent_prompt())) > 3896`
- Main call graph hints: `self.env.is_truncated`, `len`, `self.enc.encode`, `self._build_agent_prompt`
##### `reset(self)` (L90)
- Inputs: parameters `reset(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
#### Class `ReactReflectAgent` L95 bases=['ReactAgent']
- Docstring: A question answering Self-Reflecting React Agent.
##### `__init__(self, question, env, agent_prompt, reflect_prompt, react_llm, reflect_llm)` (L99)
- Inputs: parameters `__init__(self, question, env, agent_prompt, reflect_prompt, react_llm, reflect_llm)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- LLM/model calls:
  - L104: `OpenAI`
  - L110: `OpenAI`
- Main call graph hints: `OpenAI`, `super.__init__`, `super`
##### `run(self, reset)` (L123)
- Inputs: parameters `run(self, reset)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L124: IF `(self.is_terminated() or self.is_truncated()) and (not self.is_correct())`; body=1 else=0
- Main call graph hints: `ReactAgent.run`, `self.reflect`, `self.is_terminated`, `self.is_truncated`, `self.is_correct`
##### `reflect(self)` (L129)
- Inputs: parameters `reflect(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `self.reflections.append`, `self.prompt_reflection`
##### `prompt_reflection(self)` (L132)
- Inputs: parameters `prompt_reflection(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L133: `format_step(self.reflect_llm(self._build_reflection_prompt()))`
- LLM/model calls:
  - L133: `self.reflect_llm`
- Main call graph hints: `format_step`, `self.reflect_llm`, `self._build_reflection_prompt`
##### `_build_reflection_prompt(self)` (L136)
- Inputs: parameters `_build_reflection_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L137: `self.reflect_prompt.format(examples=self.reflect_examples, question=self.question, scratchpad=self._format_scratchpad())`
- Main call graph hints: `self.reflect_prompt.format`, `self._format_scratchpad`
##### `_build_agent_prompt(self)` (L142)
- Inputs: parameters `_build_agent_prompt(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L143: `self.agent_prompt.format(examples=self.react_examples, reflections=format_reflections(self.reflections), question=self.question, scratchpad=self.scratchpad)`
- Main call graph hints: `self.agent_prompt.format`, `format_reflections`
##### `_format_scratchpad(self)` (L149)
- Inputs: parameters `_format_scratchpad(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L156: `'\n'.join(lines)`
- Loops:
  - L152: {'line': 152, 'type': 'while', 'test': "len(self.enc.encode('\\n'.join(lines))) > 1600", 'body_len': 3, 'orelse_len': 0}
- Main call graph hints: `self.scratchpad.split`, `sorted`, `Constant.join`, `len`, `lines.index`, `self.enc.encode`, `lines_by_tokens.pop`, `line.split`

### Functions
#### `format_reflections(reflections)` (L161)
- Inputs: parameters `format_reflections(reflections)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L163: `''`
  - L166: `header + 'Reflections:\n- ' + '\n- '.join([r.strip() for r in reflections])`
- Decisions / conditions:
  - L162: IF `reflections == []`; body=1 else=2
- Main call graph hints: `Constant.join`, `r.strip`
#### `format_step(step)` (L168)
- Inputs: parameters `format_step(step)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L169: `step.strip('\n').strip().replace('\n', '')`
- Main call graph hints: `step.strip.strip.replace`, `step.strip.strip`, `step.strip`

---

## File: `hotpotqa_runs/tests.py`

**Lines:** 14  

### Imports
- `import joblib`
- `from react_cls import ReactReflectAgent`
- `from mocks import DocStoreExplorerMock, LLMMock`

### Module-level assignments
- L6: `test_q = "What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?"`
- L7: `test_a = "1,800 to 7,000 ft"`
- L9: `agent = ReactReflectAgent(test_q, test_a)`

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `hotpotqa_runs/util.py`

**Lines:** 67  

### Imports
- `import os`
- `import joblib`

### Module-level assignments
- None

### Prompt-like assignments
- L10 `prefix`: `prefix = prompt.split('Here are some examples:')[0]`
- L41 ``: `correct, incorrect, halted = summarize_react_trial(agents)`

### Classes
- None

### Functions
#### `summarize_trial(agents)` (L4)
- Inputs: parameters `summarize_trial(agents)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L7: `(correct, incorrect)`
- Main call graph hints: `a.is_correct`, `a.is_finished`
#### `remove_fewshot(prompt)` (L9)
- Inputs: parameters `remove_fewshot(prompt)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L12: `prefix.strip('\n').strip() + '\n' + suffix.strip('\n').strip()`
- Main call graph hints: `prompt.split`, `suffix.strip.strip`, `prefix.strip.strip`, `suffix.strip`, `prefix.strip`
#### `log_trial(agents, trial_n)` (L14)
- Inputs: parameters `log_trial(agents, trial_n)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L32: `log`
- Loops:
  - L25: {'line': 25, 'type': 'for', 'target': 'agent', 'iter': 'correct', 'body_len': 1, 'orelse_len': 0}
  - L29: {'line': 29, 'type': 'for', 'target': 'agent', 'iter': 'incorrect', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `summarize_trial`, `len`, `remove_fewshot`, `agent._build_agent_prompt`
#### `summarize_react_trial(agents)` (L34)
- Inputs: parameters `summarize_react_trial(agents)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L38: `(correct, incorrect, halted)`
- Main call graph hints: `a.is_correct`, `a.is_halted`, `a.is_finished`
#### `log_react_trial(agents, trial_n)` (L40)
- Inputs: parameters `log_react_trial(agents, trial_n)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L62: `log`
- Loops:
  - L51: {'line': 51, 'type': 'for', 'target': 'agent', 'iter': 'correct', 'body_len': 1, 'orelse_len': 0}
  - L55: {'line': 55, 'type': 'for', 'target': 'agent', 'iter': 'incorrect', 'body_len': 1, 'orelse_len': 0}
  - L59: {'line': 59, 'type': 'for', 'target': 'agent', 'iter': 'halted', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `summarize_react_trial`, `len`, `remove_fewshot`, `agent._build_agent_prompt`
#### `save_agents(agents, dir)` (L64)
- Inputs: parameters `save_agents(agents, dir)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L66: {'line': 66, 'type': 'for', 'target': '(i, agent)', 'iter': 'enumerate(agents)', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L67: `joblib.dump`
- Main call graph hints: `os.makedirs`, `enumerate`, `joblib.dump`, `os.path.join`

---

## File: `programming_runs/dataset_random_sample.py`

**Lines:** 32  

### Imports
- `from utils import read_jsonl, read_jsonl_gz, write_jsonl`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L18 If: `if __name__ == "__main__": import argparse import random import os # take in the input and output file names, with number of samples random.seed(os.urandom(1024)) parser = argparse.ArgumentParser() parser.add_argument("--input", type=str, required=True) parser.add_argument("--output", type=str, required=True) parser.add_argument("--num_samples", type=int, required=True) args = parser.parse_args() main(args)`

### Classes
- None

### Functions
#### `main(args)` (L4)
- Inputs: parameters `main(args)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L5: IF `args.input.endswith('.gz')`; body=1 else=1
- I/O calls:
  - L15: `write_jsonl`
  - L6: `read_jsonl_gz`
  - L8: `read_jsonl`
- Main call graph hints: `args.input.endswith`, `random.sample`, `write_jsonl`, `read_jsonl_gz`, `read_jsonl`, `len`

---

## File: `programming_runs/evaluate_leet_results.py`

**Lines:** 52  

### Imports
- `from executors.leetcode_env.leetcode_env.environment import LeetCodeEnv`
- `from executors.leetcode_env.leetcode_env.leetcode_types import LeetCodeSubmission, ProgrammingLanguage`
- `from executors.leetcode_env.leetcode_env.utils import PySubmissionFormatter, RsSubmissionFormatter`
- `from utils import read_jsonl`
- `import sys`

### Module-level assignments
- L9: `lang = sys.argv[1]`
- L10: `input_log_path = sys.argv[2]`
- L11: `output_log_path = sys.argv[3]`
- L22: `lines = read_jsonl(input_log_path)`
- L27: `env = LeetCodeEnv()`

### Prompt-like assignments
- None

### Top-level logic
- L13 If: `if lang == "py": formatter = PySubmissionFormatter lang = ProgrammingLanguage.PYTHON elif lang == "rs": formatter = RsSubmissionFormatter lang = ProgrammingLanguage.RUST else: raise ValueError("Provide a valid language (rs or py)")`
- L24 For: `for line in lines: assert "implementations" in line, "Log file must contain implementations"`
- L29 For: `for line in lines: line["evaluations"] = [] for impl in line["implementations"]: submission = LeetCodeSubmission( code=formatter.to_leetcode(impl), lang=lang, question_slug=impl["task_id"], ) status, reward, done, info = env.step(submission) line["evaluations"].append({ "status": status, "reward": reward, "done": done, "info": info, }) env.reset()`

### Classes
- None

### Functions
- None

---

## File: `programming_runs/evaluate_rs_leet_results.py`

**Lines:** 1  

### Imports
- None

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming_runs/executors/__init__.py`

**Lines:** 4  

### Imports
- `from .py_executor import PyExecutor`
- `from .rs_executor import RsExecutor`
- `from .factory import executor_factory`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming_runs/executors/executor_types.py`

**Lines:** 27  

### Imports
- `from typing import NamedTuple, List, Tuple`
- `from abc import ABC, abstractmethod`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `ExecuteResult` L4 bases=['NamedTuple']
#### Class `Executor` L9 bases=['ABC']
##### `execute(self, func, tests, timeout)` (L11)
- Inputs: parameters `execute(self, func, tests, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `evaluate(self, name, func, test, timeout)` (L15)
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.

### Functions
- None

---

## File: `programming_runs/executors/executor_utils.py`

**Lines:** 59  

### Imports
- `import os, json`
- `from threading import Thread`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `PropagatingThread` L12 bases=['Thread']
##### `run(self)` (L13)
- Inputs: parameters `run(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L16: IF `hasattr(self, '_Thread__target')`; body=1 else=1
- Exception handling:
  - L15: handlers=['BaseException'] final=0
- I/O calls:
  - L18: `self._Thread__target`
- Main call graph hints: `hasattr`, `self._Thread__target`, `self._target`
##### `join(self, timeout)` (L24)
- Inputs: parameters `join(self, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L28: `self.ret`
- Decisions / conditions:
  - L26: IF `self.exc`; body=1 else=0
- Main call graph hints: `super.join`, `super`

### Functions
#### `timeout_handler(_, __)` (L2)
- Inputs: parameters `timeout_handler(_, __)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `TimeoutError`
#### `to_jsonl(dict_data, file_path)` (L6)
- Inputs: parameters `to_jsonl(dict_data, file_path)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- I/O calls:
  - L7: `open`
  - L8: `json.dumps`
  - L9: `file.write`
- Main call graph hints: `open`, `json.dumps`, `file.write`
#### `function_with_timeout(func, args, timeout)` (L31)
- Inputs: parameters `function_with_timeout(func, args, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L44: `result_container[0]`
- Decisions / conditions:
  - L41: IF `thread.is_alive()`; body=1 else=1
- I/O calls:
  - L37: `PropagatingThread`
  - L38: `thread.start`
  - L39: `thread.join`
  - L41: `thread.is_alive`
- Main call graph hints: `PropagatingThread`, `thread.start`, `thread.join`, `thread.is_alive`, `result_container.append`, `TimeoutError`, `func`

---

## File: `programming_runs/executors/factory.py`

**Lines:** 28  

### Imports
- `from .py_executor import PyExecutor`
- `from .rs_executor import RsExecutor`
- `from .executor_types import Executor`
- `from .leet_executor import LeetExecutor`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `executor_factory(lang, is_leet)` (L6)
- Inputs: parameters `executor_factory(lang, is_leet)` plus globals/config/memory/env state as referenced.
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

## File: `programming_runs/executors/leet_executor.py`

**Lines:** 59  

### Imports
- `from __future__ import annotations`
- `from typing import List`
- `from .executor_types import ExecuteResult, Executor`
- `from .executor_utils import to_jsonl`
- `from datetime import datetime`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `LeetExecutor` L9 bases=['Executor']
##### `__init__(self, lang, executor, formatter)` (L10)
- Inputs: parameters `__init__(self, lang, executor, formatter)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `isinstance`, `LeetCodeEnv`, `datetime.now.strftime`, `datetime.now`
##### `execute(self, func, tests, timeout)` (L22)
- Inputs: parameters `execute(self, func, tests, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L23: `self.executor.execute(func, tests, timeout)`
- Main call graph hints: `self.executor.execute`
##### `evaluate(self, name, func, test, timeout)` (L25)
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L58: `reward`
  - L33: `False`
- Exception handling:
  - L29: handlers=['Exception'] final=0
- Main call graph hints: `print`, `LeetCodeSubmission`, `self.env.step`, `to_jsonl`, `self.formatter.to_leetcode`, `id_from_slug`

### Functions
- None

---

## File: `programming_runs/executors/py_executor.py`

**Lines:** 96  

### Imports
- `import ast`
- `import signal`
- `import astunparse`
- `from .executor_utils import function_with_timeout`
- `from typing import List`
- `from .executor_types import ExecuteResult, Executor`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L90 If: `if __name__ == "__main__": pass # Test the function func = "def add(a, b):\n while True:\n x = 1\n return a + b" tests = ["assert add(1, 2) == 3", "assert add(1, 2) == 4"] print(PyExecutor().execute(func, tests, timeout=1))`

### Classes
#### Class `PyExecutor` L10 bases=['Executor']
##### `execute(self, func, tests, timeout)` (L11)
- Inputs: parameters `execute(self, func, tests, timeout)` plus globals/config/memory/env state as referenced.
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
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L66: `True`
  - L68: `False`
- Exception handling:
  - L62: handlers=['Exception'] final=0
- Main call graph hints: `function_with_timeout`, `globals`

### Functions
#### `get_call_str(assert_statement)` (L70)
- Inputs: parameters `get_call_str(assert_statement)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L77: `astunparse.unparse(call_str).strip()`
- Exception handling:
  - L72: handlers=['Exception'] final=0
- Main call graph hints: `ast.parse`, `astunparse.unparse.strip`, `astunparse.unparse`
#### `get_output(func, assert_statement, timeout)` (L79)
- Inputs: parameters `get_output(func, assert_statement, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L84: `output`
  - L86: `'TIMEOUT'`
  - L88: `str(e)`
- Exception handling:
  - L80: handlers=['TimeoutError', 'Exception'] final=0
- Main call graph hints: `exec`, `get_call_str`, `function_with_timeout`, `globals`, `str`

---

## File: `programming_runs/executors/rs_executor.py`

**Lines:** 373  

### Imports
- `import os`
- `import signal`
- `import subprocess`
- `import json`
- `from .executor_utils import timeout_handler`
- `from .executor_types import ExecuteResult, Executor`
- `from typing import List, Tuple, Optional`

### Module-level assignments
- L12: `cargo_harness_dir = os.path.join(os.path.dirname( os.path.realpath(__file__)), "cargo_harness")`
- L211: `assert_no_panic = r""" macro_rules! assert_eq_nopanic { ($left:expr, $right:expr) => { std::panic::catch_unwind(|| { assert_eq!($left, $right); }).unwrap_or_else(|_| {}); }; () => {}; } """`

### Prompt-like assignments
- L363 `test_compiletime`: `test_compiletime = r""" {"reason":"compiler-message","package_id":"testing 0.1.0 (path+file:///home/elleven/Downloads/testing)","manifest_path":"/home/elleven/Downloads/testing/Cargo.toml","target":{"kind":["bin"],"crate_types":["bin"],"name":"testing","src_path":"/home/elleven/Downloads/testing/...`
- L96 `res`: `res = run_with_timeout( "cargo check --message-format=json", tmp_dir, timeout=timeout)`
- L182 `res`: `res = run_with_timeout( "cargo check --message-format=json", tmp_dir, timeout=timeout, print_debug=True)`

### Top-level logic
- L341 If: `if __name__ == "__main__": test_runtime = r""" Finished dev [unoptimized + debuginfo] target(s) in 0.00s Running `target/debug/testing` thread 'main' panicked at 'assertion failed: `(left == right)` left: `1`, right: `2`', src/main.rs:11:5 note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace thread 'main' panicked at 'assertion failed: `(left == right)` left: `3`, right: `2`', src/main.rs:12:5 thread 'main' panicked at 'assertion failed: `(left == right)` left: `[5, -...`

### Classes
#### Class `RsExecutor` L87 bases=['Executor']
##### `execute(self, func, tests, timeout)` (L88)
- Inputs: parameters `execute(self, func, tests, timeout)` plus globals/config/memory/env state as referenced.
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
- I/O calls:
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
- Inputs: parameters `evaluate(self, name, func, test, timeout)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L191: `False`
  - L200: `False`
  - L208: `len(errs) == 0`
  - L205: `False`
- Decisions / conditions:
  - L187: IF `len(errs) > 0`; body=3 else=0
  - L198: IF `res is None`; body=2 else=4
  - L203: IF `len(errs) > 0`; body=2 else=0
- I/O calls:
  - L180: `write_to_file_toplevel`
- Main call graph hints: `create_temp_project`, `print`, `write_to_file_toplevel`, `run_with_timeout`, `grab_compile_errs`, `os.system`, `len`, `grab_runtime_errs`
#### Class `CompileErr` L248 bases=[]
##### `__init__(self, rendered)` (L249)
- Inputs: parameters `__init__(self, rendered)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `__str__(self)` (L252)
- Inputs: parameters `__str__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L253: `self.rendered`
##### `__repr__(self)` (L255)
- Inputs: parameters `__repr__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L256: `'{' + str(self) + '}'`
- Main call graph hints: `str`
#### Class `RuntimeErr` L259 bases=[]
##### `__init__(self, left, right, line, column, panic_reason)` (L260)
- Inputs: parameters `__init__(self, left, right, line, column, panic_reason)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `__str__(self)` (L269)
- Inputs: parameters `__str__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L271: `f'assertion failed: {self.left} == {self.right}'`
  - L273: `self.panic_reason`
- Decisions / conditions:
  - L270: IF `self.left is not None and self.right is not None`; body=1 else=1
##### `__repr__(self)` (L275)
- Inputs: parameters `__repr__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L276: `'{' + str(self) + '}'`
- Main call graph hints: `str`

### Functions
#### `create_temp_project()` (L16)
- Inputs: parameters `create_temp_project()` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L30: `(temp_dir, main_path)`
- Decisions / conditions:
  - L24: IF `os.path.exists(temp_dir)`; body=1 else=0
- I/O calls:
  - L24: `os.path.exists`
- Main call graph hints: `os.getpid`, `os.urandom.hex`, `os.path.exists`, `os.mkdir`, `os.system`, `os.path.join`, `os.urandom`
#### `write_to_file(path, code)` (L33)
- Inputs: parameters `write_to_file(path, code)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L38: IF `os.path.exists(path)`; body=1 else=0
- I/O calls:
  - L38: `os.path.exists`
  - L41: `open`
  - L42: `f.write`
- Main call graph hints: `os.path.exists`, `os.remove`, `open`, `f.write`, `indent_code`
#### `write_to_file_toplevel(path, code)` (L45)
- Inputs: parameters `write_to_file_toplevel(path, code)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L47: IF `os.path.exists(path)`; body=1 else=0
- I/O calls:
  - L47: `os.path.exists`
  - L50: `open`
  - L51: `f.write`
- Main call graph hints: `os.path.exists`, `os.remove`, `open`, `f.write`
#### `run_with_timeout(cmd, tmp_cargo_path, timeout, print_debug)` (L54)
- Docstring: Runs the given command with a timeout. Produces a tuple of stdout and stderr.
If the command times out, returns None.
- Inputs: parameters `run_with_timeout(cmd, tmp_cargo_path, timeout, print_debug)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L84: `(out, err)`
  - L72: `None`
- Decisions / conditions:
  - L77: IF `print_debug`; body=5 else=0
- Exception handling:
  - L66: handlers=['TimeoutError'] final=0
- I/O calls:
  - L64: `subprocess.Popen`
- Main call graph hints: `signal.signal`, `signal.alarm`, `subprocess.Popen`, `out.decode`, `err.decode`, `p.communicate`, `print`, `p.kill`
#### `transform_asserts(code)` (L223)
- Docstring: Transform all asserts into assert_eq_nopanic! asserts, inserting the macro
definition at the top of the code.
- Inputs: parameters `transform_asserts(code)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L229: `assert_no_panic + code`
- Main call graph hints: `code.replace`
#### `revert_asserts(code)` (L232)
- Docstring: Revert all assert_eq_nopanic! asserts back into assert_eq! asserts.
- Inputs: parameters `revert_asserts(code)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L238: `normal[len(assert_no_panic):]`
- Main call graph hints: `code.replace`, `len`
#### `indent_code(code, spaces)` (L241)
- Docstring: Indent the code by the given number of spaces.
- Inputs: parameters `indent_code(code, spaces)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L245: `'\n'.join([' ' * spaces + line for line in code.splitlines()])`
- Main call graph hints: `Constant.join`, `code.splitlines`
#### `grab_compile_errs(inp)` (L281)
- Inputs: parameters `grab_compile_errs(inp)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L294: `objs`
- Loops:
  - L284: {'line': 284, 'type': 'for', 'target': 'line', 'iter': 'inp.splitlines()', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L285: IF `line == ''`; body=1 else=0
  - L288: IF `o is not None and o['reason'] == 'compiler-message' and (o['message']['level'] == 'error') and (o['message']['spans'] != [])`; body=2 else=0
- I/O calls:
  - L287: `json.loads`
- Main call graph hints: `inp.splitlines`, `json.loads`, `objs.append`, `CompileErr`
#### `grab_runtime_errs(inp)` (L300)
- Inputs: parameters `grab_runtime_errs(inp)` plus globals/config/memory/env state as referenced.
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

## File: `programming_runs/generate_dataset.py`

**Lines:** 33  

### Imports
- `import sys`
- `from datasets.load import load_dataset`
- `from utils import write_jsonl`

### Module-level assignments
- L6: `DATASET_NAME = sys.argv[1]`

### Prompt-like assignments
- None

### Top-level logic
- L31 If: `if __name__ == "__main__": download_dataset(DATASET_NAME)`

### Classes
- None

### Functions
#### `download_dataset(dataset_name)` (L9)
- Inputs: parameters `download_dataset(dataset_name)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L13: {'line': 13, 'type': 'for', 'target': 'item', 'iter': "dataset['test']", 'body_len': 8, 'orelse_len': 0}
- I/O calls:
  - L10: `load_dataset`
  - L24: `open.close`
  - L27: `write_jsonl`
  - L24: `open`
- Main call graph hints: `load_dataset`, `open.close`, `write_jsonl`, `print`, `Constant.join`, `final.append`, `open`, `name.split`

---

## File: `programming_runs/generators/__init__.py`

**Lines:** 5  

### Imports
- `from .py_generate import PyGenerator`
- `from .rs_generate import RsGenerator`
- `from .factory import generator_factory, model_factory`
- `from .model import ModelBase, GPT4, GPT35`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming_runs/generators/factory.py`

**Lines:** 33  

### Imports
- `from .py_generate import PyGenerator`
- `from .rs_generate import RsGenerator`
- `from .generator_types import Generator`
- `from .model import CodeLlama, ModelBase, GPT4, GPT35, StarChat, GPTDavinci`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `generator_factory(lang)` (L7)
- Inputs: parameters `generator_factory(lang)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L9: `PyGenerator()`
  - L11: `RsGenerator()`
- Decisions / conditions:
  - L8: IF `lang == 'py' or lang == 'python'`; body=1 else=1
  - L10: IF `lang == 'rs' or lang == 'rust'`; body=1 else=1
- Main call graph hints: `PyGenerator`, `RsGenerator`, `ValueError`
#### `model_factory(model_name)` (L16)
- Inputs: parameters `model_factory(model_name)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L18: `GPT4()`
  - L20: `GPT35()`
  - L22: `StarChat()`
  - L28: `CodeLlama(**kwargs)`
  - L30: `GPTDavinci(model_name)`
- Decisions / conditions:
  - L17: IF `model_name == 'gpt-4'`; body=1 else=1
  - L19: IF `model_name == 'gpt-3.5-turbo'`; body=1 else=1
  - L21: IF `model_name == 'starchat'`; body=1 else=1
  - L23: IF `model_name.startswith('codellama')`; body=3 else=1
  - L26: IF `'-' in model_name`; body=1 else=0
  - L29: IF `model_name.startswith('text-davinci')`; body=1 else=1
- LLM/model calls:
  - L18: `GPT4`
  - L20: `GPT35`
  - L22: `StarChat`
  - L30: `GPTDavinci`
- Main call graph hints: `GPT4`, `GPT35`, `StarChat`, `model_name.startswith`, `CodeLlama`, `GPTDavinci`, `ValueError`, `model_name.split`

---

## File: `programming_runs/generators/generator_types.py`

**Lines:** 34  

### Imports
- `from typing import List, Optional, Union`
- `from abc import abstractmethod, ABC`
- `from generators.model import ModelBase`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
#### Class `Generator` L7 bases=[]
##### `self_reflection(self, func, feedback, model)` (L9)
- Inputs: parameters `self_reflection(self, func, feedback, model)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` (L13)
- Inputs: parameters `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `internal_tests(self, func_sig, model, max_num_tests)` (L27)
- Inputs: parameters `internal_tests(self, func_sig, model, max_num_tests)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.

### Functions
- None

---

## File: `programming_runs/generators/generator_utils.py`

**Lines:** 209  

### Imports
- `from generators.model import ModelBase, Message`
- `import random`
- `from typing import Union, List, Optional, Callable`

### Module-level assignments
- None

### Prompt-like assignments
- L140 `prompt`: `prompt = f'{test_generation_completion_instruction}\n\nfunc signature:\n{func_sig}\nunit tests:'`
- L184 `reflection`: `reflection = model.generate( f'{self_reflection_completion_instruction}\n{add_code_block(func)}\n\n{feedback}\n\nExplanation:')`
- L34 `message`: `message = f"{reflexion_few_shot}\n[previous impl]:\n{add_code_block(prev_func_impl)}\n\n[unit test results from previous impl]:\n{feedback}\n\n[reflection on previous impl]:\n{self_reflection}\n\n[improved impl]:\n{func_sig}"`
- L35 `prompt`: `prompt = f"{reflexion_chat_instruction}\n{code_block_instruction}"`
- L38 `messages`: `messages = [ Message( role="system", content=prompt, ), Message( role="user", # TODO: check this content=reflexion_few_shot, ), Message( role="assistant", content=add_code_block(prev_func_impl), ), Message( role="user", content=f"[unit test results from previous impl]:\n{feedback}\n\n[reflection ...`
- L64 `func_bodies`: `func_bodies = model.generate_chat(messages=messages, num_comps=num_comps, temperature=temperature)`
- L66 `system_prompt`: `system_prompt = f"{simple_chat_instruction}\n{code_block_instruction}"`
- L68 `messages`: `messages = [ Message( role="system", content=f"{simple_chat_instruction}\n{code_block_instruction}", ), Message( role="user", content=func_sig, ), ]`
- L78 `func_bodies`: `func_bodies = model.generate_chat(messages=messages, num_comps=num_comps, temperature=temperature)`
- L81 `prompt`: `prompt = f"{reflexion_completion_instruction}\n{add_code_block(prev_func_impl)}\n\nunit tests:\n{feedback}\n\nhint:\n{self_reflection}\n\n# improved implementation\n{func_sig}\n{code_block_instruction}"`
- L82 `func_bodies`: `func_bodies = model.generate( prompt, num_comps=num_comps, temperature=temperature)`
- L85 `prompt`: `prompt = f"{simple_completion_instruction}\n{func_sig}\n{code_block_instruction}"`
- L86 `func_bodies`: `func_bodies = model.generate( prompt, num_comps=num_comps, temperature=temperature)`
- L115 `messages`: `messages = [ Message( role="system", content=test_generation_chat_instruction, ), Message( role="user", content=f"{test_generation_few_shot}\n\n[func signature]:\n{func_sig}\n\n[think]:" ) ]`
- L125 `output`: `output = model.generate_chat(messages=messages, max_tokens=1024)`
- L128 `messages`: `messages = [ Message( role="system", content=test_generation_chat_instruction, ), Message( role="user", content=f"{test_generation_few_shot}\n\n[func signature]:\n{func_sig}\n\n[unit tests]:", ) ]`
- L138 `output`: `output = model.generate_chat(messages=messages, max_tokens=1024)`
- L159 `messages`: `messages = [ Message( role="system", content=self_reflection_chat_instruction, ), Message( role="user", content=f'{self_reflection_few_shot}\n\n[function impl]:\n{add_code_block(func)}\n\n[unit test results]:\n{feedback}\n\n[self-reflection]:', ) ]`
- L169 `reflection`: `reflection = model.generate_chat(messages=messages)`
- L172 `messages`: `messages = [ Message( role="system", content=self_reflection_chat_instruction, ), Message( role="user", content=f'[function impl]:\n{add_code_block(func)}\n\n[unit test results]:\n{feedback}\n\n[self-reflection]:', ) ]`
- L182 `reflection`: `reflection = model.generate_chat(messages=messages)`

### Classes
- None

### Functions
#### `generic_generate_func_impl(func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, reflexion_chat_instruction, reflexion_few_shot, simple_chat_instruction, reflexion_completion_instruction, simple_completion_instruction, code_block_instruction, parse_code_block, add_code_block)` (L7)
- Inputs: parameters `generic_generate_func_impl(func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature, reflexion_chat_instruction, reflexion_few_shot, simple_chat_instruction, reflexion_completion_instruction, simple_completion_instruction, code_block_instruction, parse_code_block, add_code_block)` plus globals/config/memory/env state as referenced.
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
- LLM/model calls:
  - L92: `print_generated_func_body`
  - L97: `print_generated_func_body`
  - L64: `model.generate_chat`
  - L78: `model.generate_chat`
  - L82: `model.generate`
  - L86: `model.generate`
- Main call graph hints: `ValueError`, `isinstance`, `parse_code_block`, `print_generated_func_body`, `print_messages`, `model.generate_chat`, `model.generate`, `Constant.join`, `Message`, `add_code_block`
#### `generic_generate_internal_tests(func_sig, model, max_num_tests, test_generation_few_shot, test_generation_chat_instruction, test_generation_completion_instruction, parse_tests, is_syntax_valid, is_react)` (L101)
- Docstring: Generates tests for a function.
- Inputs: parameters `generic_generate_internal_tests(func_sig, model, max_num_tests, test_generation_few_shot, test_generation_chat_instruction, test_generation_completion_instruction, parse_tests, is_syntax_valid, is_react)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L145: `sample_n_random(valid_tests, max_num_tests)`
- Decisions / conditions:
  - L113: IF `model.is_chat`; body=1 else=2
  - L114: IF `is_react`; body=3 else=2
- LLM/model calls:
  - L141: `model.generate`
  - L125: `model.generate_chat`
  - L138: `model.generate_chat`
- Main call graph hints: `parse_tests`, `sample_n_random`, `model.generate`, `model.generate_chat`, `print`, `is_syntax_valid`, `Message`
#### `generic_generate_self_reflection(func, feedback, model, self_reflection_chat_instruction, self_reflection_completion_instruction, add_code_block, self_reflection_few_shot)` (L148)
- Inputs: parameters `generic_generate_self_reflection(func, feedback, model, self_reflection_chat_instruction, self_reflection_completion_instruction, add_code_block, self_reflection_few_shot)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L186: `reflection`
- Decisions / conditions:
  - L157: IF `model.is_chat`; body=1 else=1
  - L158: IF `self_reflection_few_shot is not None`; body=3 else=2
- LLM/model calls:
  - L184: `model.generate`
  - L169: `model.generate_chat`
  - L182: `model.generate_chat`
- Main call graph hints: `model.generate`, `model.generate_chat`, `print`, `Message`, `add_code_block`
#### `sample_n_random(items, n)` (L189)
- Docstring: Sample min(n, len(items)) random items from a list
- Inputs: parameters `sample_n_random(items, n)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L194: `random.sample(items, n)`
  - L193: `items`
- Decisions / conditions:
  - L192: IF `n >= len(items)`; body=1 else=0
- Main call graph hints: `random.sample`, `len`
#### `print_messages(system_message_text, user_message_text)` (L196)
- Inputs: parameters `print_messages(system_message_text, user_message_text)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `print`
#### `print_generated_func_body(func_body_str)` (L205)
- Inputs: parameters `print_generated_func_body(func_body_str)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `print`

---

## File: `programming_runs/generators/model.py`

**Lines:** 264  

### Imports
- `from typing import List, Union, Optional, Literal`
- `import dataclasses`
- `from tenacity import ( retry, stop_after_attempt, # type: ignore wait_random_exponential, # type: ignore )`
- `import openai`

### Module-level assignments
- L11: `MessageRole = Literal["system", "user", "assistant"]`

### Prompt-like assignments
- L11 `MessageRole`: `MessageRole = Literal["system", "user", "assistant"]`
- L37 `response`: `response = openai.Completion.create( model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=stop_strs, n=num_comps, )`
- L62 `response`: `response = openai.ChatCompletion.create( model=model, messages=[dataclasses.asdict(message) for message in messages], max_tokens=max_tokens, temperature=temperature, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, n=num_comps, )`
- L204 `DEFAULT_SYSTEM_PROMPT`: `DEFAULT_SYSTEM_PROMPT = """\ You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially u...`
- L139 `outputs`: `outputs = self.model.generate( prompt, max_new_tokens=min( max_tokens, self.model.config.max_position_embeddings), use_cache=True, do_sample=True, temperature=temperature, top_p=0.95, eos_token_id=self.eos_token_id, num_return_sequences=num_comps, )`
- L230 `messages`: `messages = [ Message(role=messages[1].role, content=self.B_SYS + messages[0].content + self.E_SYS + messages[1].content) ] + messages[2:]`
- L240 `messages_tokens`: `messages_tokens: List[int] = sum( [ self.tokenizer.encode( f"{self.B_INST} {(prompt.content).strip()} {self.E_INST} {(answer.content).strip()} ", ) for prompt, answer in zip( messages[::2], messages[1::2], ) ], [], )`
- L227 `messages`: `messages = [ Message(role="system", content=self.DEFAULT_SYSTEM_PROMPT) ] + messages`

### Classes
#### Class `Message` L15 bases=[]
#### Class `ModelBase` L78 bases=[]
##### `__init__(self, name)` (L79)
- Inputs: parameters `__init__(self, name)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `__repr__(self)` (L83)
- Inputs: parameters `__repr__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L84: `f'{self.name}'`
##### `generate_chat(self, messages, max_tokens, temperature, num_comps)` (L86)
- Inputs: parameters `generate_chat(self, messages, max_tokens, temperature, num_comps)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` (L89)
- Inputs: parameters `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
#### Class `GPTChat` L93 bases=['ModelBase']
##### `__init__(self, model_name)` (L94)
- Inputs: parameters `__init__(self, model_name)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `generate_chat(self, messages, max_tokens, temperature, num_comps)` (L98)
- Inputs: parameters `generate_chat(self, messages, max_tokens, temperature, num_comps)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L99: `gpt_chat(self.name, messages, max_tokens, temperature, num_comps)`
- LLM/model calls:
  - L99: `gpt_chat`
- Main call graph hints: `gpt_chat`
#### Class `GPT4` L102 bases=['GPTChat']
##### `__init__(self)` (L103)
- Inputs: parameters `__init__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `super`
#### Class `GPT35` L107 bases=['GPTChat']
##### `__init__(self)` (L108)
- Inputs: parameters `__init__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `super`
#### Class `GPTDavinci` L112 bases=['ModelBase']
##### `__init__(self, model_name)` (L113)
- Inputs: parameters `__init__(self, model_name)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` (L116)
- Inputs: parameters `generate(self, prompt, max_tokens, stop_strs, temperature, num_comps)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L117: `gpt_completion(self.name, prompt, max_tokens, stop_strs, temperature, num_comps)`
- LLM/model calls:
  - L117: `gpt_completion`
- Main call graph hints: `gpt_completion`
#### Class `HFModelBase` L120 bases=['ModelBase']
- Docstring: Base for huggingface chat models
##### `__init__(self, model_name, model, tokenizer, eos_token_id)` (L125)
- Inputs: parameters `__init__(self, model_name, model, tokenizer, eos_token_id)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `generate_chat(self, messages, max_tokens, temperature, num_comps)` (L132)
- Inputs: parameters `generate_chat(self, messages, max_tokens, temperature, num_comps)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L158: `outs[0]`
  - L160: `outs`
- Loops:
  - L153: {'line': 153, 'type': 'for', 'target': '(i, out)', 'iter': 'enumerate(outs)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L134: IF `temperature < 0.0001`; body=1 else=0
  - L157: IF `len(outs) == 1`; body=1 else=1
- LLM/model calls:
  - L139: `self.model.generate`
- Main call graph hints: `self.prepare_prompt`, `self.model.generate`, `self.tokenizer.batch_decode`, `isinstance`, `enumerate`, `self.extract_output`, `len`, `min`
##### `prepare_prompt(self, messages)` (L162)
- Inputs: parameters `prepare_prompt(self, messages)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `extract_output(self, output)` (L165)
- Inputs: parameters `extract_output(self, output)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
#### Class `StarChat` L169 bases=['HFModelBase']
##### `__init__(self)` (L170)
- Inputs: parameters `__init__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- LLM/model calls:
  - L173: `AutoModelForCausalLM.from_pretrained`
- Main call graph hints: `AutoModelForCausalLM.from_pretrained`, `AutoTokenizer.from_pretrained`, `super.__init__`, `super`
##### `prepare_prompt(self, messages)` (L183)
- Inputs: parameters `prepare_prompt(self, messages)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L190: `self.tokenizer.encode(prompt, return_tensors='pt').to(self.model.device)`
- Loops:
  - L185: {'line': 185, 'type': 'for', 'target': '(i, message)', 'iter': 'enumerate(messages)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L187: IF `i == len(messages) - 1`; body=1 else=0
- Main call graph hints: `enumerate`, `self.tokenizer.encode.to`, `self.tokenizer.encode`, `len`
##### `extract_output(self, output)` (L192)
- Inputs: parameters `extract_output(self, output)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L197: `out`
- Decisions / conditions:
  - L194: IF `out.endswith('<|end|>')`; body=1 else=0
- Main call graph hints: `out.endswith`, `output.split`, `len`
#### Class `CodeLlama` L200 bases=['HFModelBase']
##### `__init__(self, version)` (L209)
- Inputs: parameters `__init__(self, version)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- LLM/model calls:
  - L218: `AutoModelForCausalLM.from_pretrained`
- Main call graph hints: `AutoTokenizer.from_pretrained`, `AutoModelForCausalLM.from_pretrained`, `super.__init__`, `super`
##### `prepare_prompt(self, messages)` (L225)
- Inputs: parameters `prepare_prompt(self, messages)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L259: `torch.tensor([messages_tokens]).to(self.model.device)`
- Decisions / conditions:
  - L226: IF `messages[0].role != 'system'`; body=1 else=0
- Main call graph hints: `sum`, `self.tokenizer.encode`, `torch.tensor.to`, `all`, `Message`, `torch.tensor`, `zip`, `messages[...].content.strip`, `prompt.content.strip`, `answer.content.strip`
##### `extract_output(self, output)` (L261)
- Inputs: parameters `extract_output(self, output)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L263: `out`
- Main call graph hints: `output.split[...].split[...].strip`, `output.split[...].split`, `output.split`

### Functions
#### `message_to_str(message)` (L20)
- Inputs: parameters `message_to_str(message)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L21: `f'{message.role}: {message.content}'`
#### `messages_to_str(messages)` (L24)
- Inputs: parameters `messages_to_str(messages)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L25: `'\n'.join([message_to_str(message) for message in messages])`
- Main call graph hints: `Constant.join`, `message_to_str`
#### `gpt_completion(model, prompt, max_tokens, stop_strs, temperature, num_comps)` (L29)
- Inputs: parameters `gpt_completion(model, prompt, max_tokens, stop_strs, temperature, num_comps)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L51: `[choice.text for choice in response.choices]`
  - L49: `response.choices[0].text`
- Decisions / conditions:
  - L48: IF `num_comps == 1`; body=1 else=0
- LLM/model calls:
  - L37: `openai.Completion.create`
- I/O calls:
  - L37: `openai.Completion.create`
- Main call graph hints: `retry`, `openai.Completion.create`, `wait_random_exponential`, `stop_after_attempt`
#### `gpt_chat(model, messages, max_tokens, temperature, num_comps)` (L55)
- Inputs: parameters `gpt_chat(model, messages, max_tokens, temperature, num_comps)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L75: `[choice.message.content for choice in response.choices]`
  - L73: `response.choices[0].message.content`
- Decisions / conditions:
  - L72: IF `num_comps == 1`; body=1 else=0
- LLM/model calls:
  - L62: `openai.ChatCompletion.create`
- I/O calls:
  - L62: `openai.ChatCompletion.create`
- Main call graph hints: `retry`, `openai.ChatCompletion.create`, `wait_random_exponential`, `stop_after_attempt`, `dataclasses.asdict`

---

## File: `programming_runs/generators/parse.py`

**Lines:** 107  

### Imports
- `import re`
- `from typing import Optional`

### Module-level assignments
- None

### Prompt-like assignments
- L77 `CODE`: `CODE = """def total_match(lst1: List[str], lst2: List[str]) -> List[str]: \"\"\" Write a function that accepts two lists of strings and returns the list that has total number of chars in the all strings of the list less than the other list. if the two lists have the same number of chars, return t...`

### Top-level logic
- L52 If: `if __name__ == "__main__": CODE = """ aldaas sub_parser = parser.add_subparsers().add_parser("frf a") def my_wonderful_func(): def useless_helper(): return 1 if 1: return 1 else: return ( 1, 2, ) sadsadsa 2023-08-04dsa dsa def bleh(): return aaa """ print(parse_code_block(CODE, "python")) CODE = """def total_match(lst1: List[str], lst2: List[str]) -> List[str]: \"\"\" Write a function that accepts two lists of strings and returns the list that has total number of chars in the all strings of t...`

### Classes
- None

### Functions
#### `parse_code_block(string, lang)` (L5)
- Inputs: parameters `parse_code_block(string, lang)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L18: `parse_first_func(string, lang)`
  - L10: `match.group(1)`
  - L16: `match.group(1)`
- Decisions / conditions:
  - L9: IF `match`; body=1 else=0
  - L15: IF `match`; body=1 else=0
- Main call graph hints: `re.search`, `parse_first_func`, `match.group`
#### `parse_first_func(code, lang)` (L21)
- Inputs: parameters `parse_first_func(code, lang)` plus globals/config/memory/env state as referenced.
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
- Inputs: parameters `add_code_block(string, lang)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L49: `f'```{lang}\n{string}\n```'`

---

## File: `programming_runs/generators/py_generate.py`

**Lines:** 383  

### Imports
- `from generators.model import ModelBase, message_to_str`
- `from .generator_types import Generator`
- `from .generator_utils import generic_generate_func_impl, generic_generate_internal_tests, generic_generate_self_reflection`
- `from typing import Optional, List, Union`
- `import ast`
- `import re`
- `from .parse import parse_code_block, add_code_block`

### Module-level assignments
- L10: `PY_SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."`
- L11: `PY_REFLEXION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"`
- L12: `PY_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence ...`
- L13: `USE_PYTHON_CODEBLOCK_INSTRUCTION = "Use a Python code block to write your response. For example:\n```python\nprint('Hello world!')\n```"`
- L15: `PY_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with python code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L16: `PY_SIMPLE_CHAT_INSTRUCTION_V2 = "You are an AI that only responds with only python code. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L17: `PY_REFLEXION_CHAT_INSTRUCTION = "You are an AI Python assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L18: `PY_REFLEXION_CHAT_INSTRUCTION_V2 = "You are an AI Python assistant. You will be given your previous implementation of a function, a series of unit tests results, and your self-reflection on your previous implementation. Write your full implementation (restate the function signature)."`
- L19: `PY_REFLEXION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```python def add(a: int, b: int) -> int: """ Given integers a and b, return the total value of a and b. """ return a - b ``` [unit test results from previous impl]: Tested passed: Tests failed: assert add(1, 2) == 3 # output: -1 assert add(1, 2) == 4 # output: -1 [reflection on previous...`
- L49: `PY_REFLEXION_FEW_SHOT = '''Example 1: [previous impl]: ```python from typing import * def fullJustify(words: List[str], maxWidth: int) -> List[str]: """ Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified. You should pack your words in a greedy ...`
- L151: `PY_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Python programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence de...`
- L152: `PY_SELF_REFLECTION_CHAT_INSTRUCTION_V2 = "You are a Python programming assistant. You will be given a function implementation and a series of unit test results. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as guidance when you try again later. Only provide the few...`
- L153: `PY_SELF_REFLECTION_FEW_SHOT = """Example 1: [function impl]: ```python def longest_subarray_with_sum_limit(nums: List[int], target: int) -> List[int]: n = len(nums) left, right = 0, 0 max_length = 0 current_sum = 0 result = [] while right < n: current_sum += nums[right] while current_sum > target: current_sum -= nums[left] left += 1 if right - l...`
- L224: `PY_TEST_GENERATION_FEW_SHOT = """Examples: func signature: def add3Numbers(x, y, z): \"\"\" Add three numbers together. This function takes three numbers as input and returns the sum of the three numbers. \"\"\" unit tests: assert add3Numbers(1, 2, 3) == 6 assert add3Numbers(-1, 2, 3) == 4 assert add3Numbers(1, -2, 3) == 2 assert add3Numbers(1, ...`
- L239: `PY_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. {PY_TEST_GENERATION_FEW_SHOT}"""`
- L243: `PY_TEST_GENERATION_CHAT_INSTRUCTION = """You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""`
- L306: `DUMMY_FUNC_SIG = "def func():"`
- L307: `DUMMY_FUNC_CALL = "func()"`

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
- Inputs: parameters `self_reflection(self, func, feedback, model)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L248: `generic_generate_self_reflection(func=func, feedback=feedback, model=model, self_reflection_chat_instruction=PY_SELF_REFLECTION_CHAT_INSTRUCTION, self_reflection_completion_instruction=PY_SELF_REFLECTION_COMPLETION_INSTRUCTION, add_code_block=lambda x: add_code_block(x, 'python'), self_reflection_few_shot=PY_SELF_REFLECTION_FEW_SHOT)`
- LLM/model calls:
  - L248: `generic_generate_self_reflection`
- Main call graph hints: `generic_generate_self_reflection`, `add_code_block`
##### `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` (L258)
- Inputs: parameters `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L269: `generic_generate_func_impl(func_sig=func_sig, model=model, strategy=strategy, prev_func_impl=prev_func_impl, feedback=feedback, self_reflection=self_reflection, num_comps=num_comps, temperature=temperature, reflexion_chat_instruction=PY_REFLEXION_CHAT_INSTRUCTION, reflexion_few_shot=PY_REFLEXION_FEW_SHOT_ADD, simple_chat_instruction=PY_SIMPLE_CH...`
- LLM/model calls:
  - L269: `generic_generate_func_impl`
- Main call graph hints: `generic_generate_func_impl`, `parse_code_block`, `add_code_block`
##### `internal_tests(self, func_sig, model, max_num_tests)` (L288)
- Inputs: parameters `internal_tests(self, func_sig, model, max_num_tests)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L294: `generic_generate_internal_tests(func_sig=func_sig, model=model, max_num_tests=max_num_tests, test_generation_few_shot=PY_TEST_GENERATION_FEW_SHOT, test_generation_chat_instruction=PY_TEST_GENERATION_CHAT_INSTRUCTION, test_generation_completion_instruction=PY_TEST_GENERATION_COMPLETION_INSTRUCTION, parse_tests=parse_tests, is_syntax_valid=py_is_s...`
  - L290: `[test.strip() for test in tests.splitlines() if 'assert' in test]`
- LLM/model calls:
  - L294: `generic_generate_internal_tests`
- Main call graph hints: `generic_generate_internal_tests`, `test.strip`, `tests.splitlines`

### Functions
#### `handle_first_line_indent(func_body)` (L310)
- Inputs: parameters `handle_first_line_indent(func_body)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L314: `f' {split[0]}\n' + '\n'.join(split[1:])`
  - L312: `func_body`
- Decisions / conditions:
  - L311: IF `func_body.startswith('    ')`; body=1 else=0
- Main call graph hints: `func_body.startswith`, `func_body.splitlines`, `Constant.join`
#### `handle_entire_body_indent(func_body)` (L317)
- Inputs: parameters `handle_entire_body_indent(func_body)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L320: `res`
- Main call graph hints: `func_body.splitlines`, `Constant.join`
#### `fix_turbo_response(func_body)` (L323)
- Inputs: parameters `fix_turbo_response(func_body)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L324: `fix_markdown(remove_unindented_signatures(func_body))`
- Main call graph hints: `fix_markdown`, `remove_unindented_signatures`
#### `fix_markdown(func_body)` (L327)
- Inputs: parameters `fix_markdown(func_body)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L328: `re.sub('`{3}', '', func_body)`
- Main call graph hints: `re.sub`
#### `remove_unindented_signatures(code)` (L331)
- Inputs: parameters `remove_unindented_signatures(code)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L350: `'\n'.join(before_signature + after_signature)`
- Loops:
  - L338: {'line': 338, 'type': 'for', 'target': 'line', 'iter': "code.split('\\n')", 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L339: IF `re.match(regex, line)`; body=2 else=0
  - L343: IF `signature_found`; body=1 else=2
  - L346: IF `not line.startswith('    ') and line.strip()`; body=1 else=0
- Main call graph hints: `code.split`, `Constant.join`, `re.match`, `after_signature.append`, `before_signature.append`, `line.strip`, `line.startswith`
#### `py_fix_indentation(func_body)` (L353)
- Inputs: parameters `py_fix_indentation(func_body)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L374: `parse_indent_rec(func_body, 0)`
  - L364: `f_body`
  - L368: `f_body`
  - L371: `parse_indent_rec(p_func(func_body), cur_state + 1)`
  - L373: `f_body`
- Decisions / conditions:
  - L363: IF `cur_state > 1`; body=1 else=0
- Exception handling:
  - L366: handlers=['(IndentationError, SyntaxError)', 'Exception'] final=0
- Main call graph hints: `fix_turbo_response`, `parse_indent_rec`, `fix_markdown`, `exec`, `p_func`
#### `py_is_syntax_valid(code)` (L377)
- Inputs: parameters `py_is_syntax_valid(code)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L380: `True`
  - L382: `False`
- Exception handling:
  - L378: handlers=['Exception'] final=0
- Main call graph hints: `ast.parse`

---

## File: `programming_runs/generators/rs_generate.py`

**Lines:** 196  

### Imports
- `from generators.model import ModelBase`
- `from .generator_types import Generator`
- `from .generator_utils import generic_generate_func_impl, generic_generate_internal_tests, generic_generate_self_reflection`
- `from .parse import parse_code_block, add_code_block`
- `from typing import List, Optional, Union`

### Module-level assignments
- L8: `RS_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."`
- L9: `RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"`
- L10: `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence de...`
- L11: `USE_RUST_CODEBLOCK_INSTRUCTION = "Use a Rust code block to write your response. For example:\n```rust\nfn main() {\n println!(\"Hello\");\n}\n```"`
- L13: `RS_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Rust code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."`
- L14: `RS_REFLEXION_CHAT_INSTRUCTION = "You are an AI Rust assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."`
- L15: `RS_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence desc...`
- L17: `RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"`
- L18: `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentenc...`
- L20: `RS_REFLEXION_FEW_SHOT_ADD = '''Example 1: [previous impl]: ```rust fn add(a: i32, b: i32) -> i32 { // Given integers a and b, return the total value of a and b. a - b } ``` [unit test results from previous impl]: Tested passed: Tests failed: assert_eq!(add(1, 2), 3); // output: -1 assert_eq!(add(1, 2), 4); // output: -1 [reflection on previous i...`
- L50: `RS_TEST_GENERATION_FEW_SHOT = """For example: func signature: /// Add three numbers together. /// This function takes three numbers as input and returns the sum of the three numbers. fn add3Numbers(x: i32, y: i32, z: i32) -> i32 { unit tests: assert_eq!(add3Numbers(1, 2, 3), 6); assert_eq!(add3Numbers(-1, 2, 3), 4); assert_eq!(add3Numbers(1, -2,...`
- L66: `RS_SELF_REFLECTION_FEW_SHOT = '''Example 1: [function impl]: ```rust pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> { // Given an array of strings strs, group the anagrams together. You can return the answer in any order. // An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically us...`
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
- Inputs: parameters `self_reflection(self, func, feedback, model)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L136: `generic_generate_self_reflection(func=func, feedback=feedback, model=model, self_reflection_chat_instruction=RS_SELF_REFLECTION_CHAT_INSTRUCTION, self_reflection_completion_instruction=RS_SELF_REFLECTION_COMPLETION_INSTRUCTION, add_code_block=lambda x: add_code_block(x, 'rust'), self_reflection_few_shot=RS_SELF_REFLECTION_FEW_SHOT)`
- LLM/model calls:
  - L136: `generic_generate_self_reflection`
- Main call graph hints: `generic_generate_self_reflection`, `add_code_block`
##### `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` (L146)
- Inputs: parameters `func_impl(self, func_sig, model, strategy, prev_func_impl, feedback, self_reflection, num_comps, temperature)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L157: `generic_generate_func_impl(func_sig=func_sig, model=model, strategy=strategy, prev_func_impl=prev_func_impl, feedback=feedback, self_reflection=self_reflection, num_comps=num_comps, temperature=temperature, reflexion_chat_instruction=RS_REFLEXION_CHAT_INSTRUCTION, simple_chat_instruction=RS_SIMPLE_CHAT_INSTRUCTION, reflexion_completion_instructi...`
- LLM/model calls:
  - L157: `generic_generate_func_impl`
- Main call graph hints: `generic_generate_func_impl`, `parse_code_block`, `add_code_block`
##### `internal_tests(self, func_sig, model, max_num_tests)` (L175)
- Inputs: parameters `internal_tests(self, func_sig, model, max_num_tests)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L186: `generic_generate_internal_tests(func_sig=func_sig, model=model, max_num_tests=max_num_tests, test_generation_few_shot=RS_TEST_GENERATION_FEW_SHOT, test_generation_chat_instruction=RS_TEST_GENERATION_CHAT_INSTRUCTION, test_generation_completion_instruction=RS_TEST_GENERATION_COMPLETION_INSTRUCTION, parse_tests=parse_tests, is_syntax_valid=lambda ...`
  - L182: `[test + ';' for test in tests.split(';')]`
- LLM/model calls:
  - L186: `generic_generate_internal_tests`
- Main call graph hints: `generic_generate_internal_tests`, `tests.split`

### Functions
#### `dump_tests(tests)` (L118)
- Docstring: Dumps the tests to a string.
- Inputs: parameters `dump_tests(tests)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L122: `'\n'.join(tests)`
- Main call graph hints: `Constant.join`
#### `parse_tests(tests)` (L125)
- Docstring: Parses the tests from a string.
- Inputs: parameters `parse_tests(tests)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L129: `[test.strip() for test in tests.splitlines() if 'assert' in test]`
- Main call graph hints: `test.strip`, `tests.splitlines`

---

## File: `programming_runs/human-eval/human_eval/__init__.py`

**Lines:** 1  

### Imports
- None

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming_runs/human-eval/human_eval/data.py`

**Lines:** 50  

### Imports
- `from typing import Iterable, Dict`
- `import gzip`
- `import json`
- `import os`

### Module-level assignments
- L7: `ROOT = os.path.dirname(os.path.abspath(__file__))`
- L8: `HUMAN_EVAL = os.path.join(ROOT, "..", "data", "HumanEval.jsonl.gz")`

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `read_problems(evalset_file)` (L11)
- Inputs: parameters `read_problems(evalset_file)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L12: `{task['task_id']: task for task in stream_jsonl(evalset_file)}`
- Main call graph hints: `stream_jsonl`
#### `stream_jsonl(filename)` (L15)
- Docstring: Parses each jsonl line and yields it as a dictionary
- Inputs: parameters `stream_jsonl(filename)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': 'line', 'iter': 'fp', 'body_len': 1, 'orelse_len': 0}
  - L22: {'line': 22, 'type': 'for', 'target': 'line', 'iter': 'fp', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L19: IF `filename.endswith('.gz')`; body=1 else=1
  - L28: IF `any((not x.isspace() for x in line))`; body=1 else=0
  - L23: IF `any((not x.isspace() for x in line))`; body=1 else=0
- I/O calls:
  - L20: `open`
  - L26: `open`
  - L21: `gzip.open`
  - L29: `json.loads`
  - L24: `json.loads`
- Main call graph hints: `filename.endswith`, `open`, `gzip.open`, `any`, `json.loads`, `x.isspace`
#### `write_jsonl(filename, data, append)` (L32)
- Docstring: Writes an iterable of dictionaries to jsonl
- Inputs: parameters `write_jsonl(filename, data, append)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L48: {'line': 48, 'type': 'for', 'target': 'x', 'iter': 'data', 'body_len': 1, 'orelse_len': 0}
  - L44: {'line': 44, 'type': 'for', 'target': 'x', 'iter': 'data', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L36: IF `append`; body=1 else=1
  - L41: IF `filename.endswith('.gz')`; body=1 else=1
- I/O calls:
  - L42: `open`
  - L47: `open`
  - L49: `fp.write`
  - L45: `gzfp.write`
  - L49: `json.dumps`
  - L45: `json.dumps`
- Main call graph hints: `os.path.expanduser`, `filename.endswith`, `open`, `gzip.GzipFile`, `fp.write`, `gzfp.write`, `BinOp.encode`, `json.dumps`

---

## File: `programming_runs/human-eval/human_eval/evaluate_functional_correctness.py`

**Lines:** 29  

### Imports
- `import fire`
- `import sys`
- `from human_eval.data import HUMAN_EVAL`
- `from human_eval.evaluation import evaluate_functional_correctness`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `entry_point(sample_file, k, n_workers, timeout, problem_file)` (L8)
- Docstring: Evaluates the functional correctness of generated samples, and writes
results to f"{sample_file}_results.jsonl.gz"
- Inputs: parameters `entry_point(sample_file, k, n_workers, timeout, problem_file)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `list`, `evaluate_functional_correctness`, `print`, `map`, `k.split`
#### `main()` (L24)
- Inputs: parameters `main()` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `fire.Fire`

---

## File: `programming_runs/human-eval/human_eval/evaluation.py`

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

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `estimate_pass_at_k(num_samples, num_correct, k)` (L13)
- Docstring: Estimates pass@k of each problem and returns them in an array.
- Inputs: parameters `estimate_pass_at_k(num_samples, num_correct, k)` plus globals/config/memory/env state as referenced.
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
- Inputs: parameters `evaluate_functional_correctness(sample_file, k, n_workers, timeout, problem_file)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L105: `pass_at_k`
- Loops:
  - L80: {'line': 80, 'type': 'for', 'target': 'result', 'iter': 'results.values()', 'body_len': 4, 'orelse_len': 0}
  - L62: {'line': 62, 'type': 'for', 'target': 'sample', 'iter': 'tqdm.tqdm(stream_jsonl(sample_file))', 'body_len': 7, 'orelse_len': 0}
  - L74: {'line': 74, 'type': 'for', 'target': 'future', 'iter': 'tqdm.tqdm(as_completed(futures), total=len(futures))', 'body_len': 2, 'orelse_len': 0}
  - L94: {'line': 94, 'type': 'for', 'target': 'sample', 'iter': 'stream_jsonl(sample_file)', 'body_len': 5, 'orelse_len': 0}
- I/O calls:
  - L51: `read_problems`
  - L103: `write_jsonl`
  - L54: `ThreadPoolExecutor`
- Main call graph hints: `read_problems`, `results.values`, `np.array`, `print`, `write_jsonl`, `ThreadPoolExecutor`, `Counter`, `defaultdict`, `tqdm.tqdm`, `result.sort`, `total.append`, `correct.append`, `estimate_pass_at_k.mean`, `stream_jsonl`, `executor.submit`, `futures.append`, `len`, `as_completed`, `future.result`, `results[...].append`, `sum`, `Compare.all`, `results[...].pop`, `combine_results`, `estimate_pass_at_k`

---

## File: `programming_runs/human-eval/human_eval/execution.py`

Syntax error: `expected an indented block after 'with' statement on line 47 (<unknown>, line 59)`

---

## File: `programming_runs/human-eval/setup.py`

**Lines:** 26  

### Imports
- `import os`
- `import pkg_resources`
- `from setuptools import setup, find_packages`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Classes
- None

### Functions
- None

---

## File: `programming_runs/humaneval_result_sort.py`

**Lines:** 27  

### Imports
- `from utils import write_jsonl, read_jsonl`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L18 If: `if __name__ == '__main__': import argparse parser = argparse.ArgumentParser() parser.add_argument('input_file', type=str) parser.add_argument('output_file', type=str) args = parser.parse_args() main(args.input_file, args.output_file)`

### Classes
- None

### Functions
#### `main(input_file, output_file)` (L4)
- Inputs: parameters `main(input_file, output_file)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L10: `int(name.split('_')[1])`
- I/O calls:
  - L6: `read_jsonl`
  - L15: `write_jsonl`
- Main call graph hints: `read_jsonl`, `sorted`, `write_jsonl`, `int`, `name.split`, `get_humaneval_number`

---

## File: `programming_runs/immediate_refinement.py`

**Lines:** 89  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module-level assignments
- None

### Prompt-like assignments
- L32 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, 1)`
- L35 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L52 `cur_func_impl`: `cur_func_impl = gen.func_impl( func_sig=item["prompt"], model=model, strategy="reflexion", prev_func_impl=cur_func_impl, feedback=cur_feedback, self_reflection="No self-reflection" )`

### Classes
- None

### Functions
#### `run_immediate_refinement(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` (L8)
- Inputs: parameters `run_immediate_refinement(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L26: {'line': 26, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 11, 'orelse_len': 0}
  - L31: {'line': 31, 'type': 'while', 'test': 'cur_pass < pass_at_k and (not is_solved)', 'body_len': 9, 'orelse_len': 0}
  - L50: {'line': 50, 'type': 'while', 'test': 'cur_iter < max_iters', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L40: IF `is_passing`; body=4 else=0
  - L67: IF `is_passing or cur_iter == max_iters - 1`; body=3 else=0
  - L70: IF `is_passing`; body=3 else=0
- I/O calls:
  - L85: `write_jsonl`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate_resume`, `exe.evaluate`, `write_jsonl`, `print_v`, `gen.internal_tests`, `gen.func_impl`, `isinstance`, `exe.execute`, `int`, `round`

---

## File: `programming_runs/immediate_reflexion.py`

**Lines:** 71  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module-level assignments
- None

### Prompt-like assignments
- L33 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L41 `reflection`: `reflection = gen.self_reflection( cur_func_impl, feedback, model)`
- L46 `cur_func_impl`: `cur_func_impl = gen.func_impl( func_sig=item["prompt"], model=model, strategy="reflexion", prev_func_impl=cur_func_impl, feedback=feedback, self_reflection=reflection )`

### Classes
- None

### Functions
#### `run_immediate_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` (L8)
- Inputs: parameters `run_immediate_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L26: {'line': 26, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 12, 'orelse_len': 0}
  - L31: {'line': 31, 'type': 'while', 'test': 'cur_pass < pass_at_k and (not is_solved)', 'body_len': 6, 'orelse_len': 0}
  - L39: {'line': 39, 'type': 'while', 'test': 'cur_iter < max_iters', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L61: IF `is_solved`; body=1 else=0
- I/O calls:
  - L67: `write_jsonl`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate_resume`, `exe.evaluate`, `write_jsonl`, `print_v`, `gen.func_impl`, `isinstance`, `gen.self_reflection`, `round`

---

## File: `programming_runs/main.py`

**Lines:** 127  

### Imports
- `import os`
- `import argparse`
- `from immediate_refinement import run_immediate_refinement`
- `from immediate_reflexion import run_immediate_reflexion`
- `from simple import run_simple`
- `from reflexion import run_reflexion`
- `from reflexion_ucs import run_reflexion_ucs`
- `from test_acc import run_test_acc`
- `from utils import read_jsonl, read_jsonl_gz`

### Module-level assignments
- None

### Prompt-like assignments
- L74 `dataset_name`: `dataset_name = os.path.basename(args.dataset_path).replace("jsonl", "")`

### Top-level logic
- L124 If: `if __name__ == "__main__": args = get_args() main(args)`

### Classes
- None

### Functions
#### `get_args()` (L13)
- Inputs: parameters `get_args()` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L41: `args`
- Main call graph hints: `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`
#### `strategy_factory(strategy)` (L44)
- Inputs: parameters `strategy_factory(strategy)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L50: `kwargs_wrapper`
  - L53: `kwargs_wrapper_gen(run_simple, delete_keys=['expansion_factor', 'max_iters'])`
  - L49: `func(**kwargs)`
  - L55: `kwargs_wrapper_gen(run_reflexion, delete_keys=['expansion_factor'])`
  - L57: `kwargs_wrapper_gen(run_immediate_reflexion, delete_keys=['expansion_factor'])`
  - L59: `kwargs_wrapper_gen(run_immediate_refinement, delete_keys=['expansion_factor'])`
  - L61: `kwargs_wrapper_gen(run_reflexion_ucs)`
  - L63: `kwargs_wrapper_gen(run_test_acc, delete_keys=['expansion_factor', 'max_iters'])`
- Loops:
  - L47: {'line': 47, 'type': 'for', 'target': 'key', 'iter': 'delete_keys', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L52: IF `strategy == 'simple'`; body=1 else=1
  - L54: IF `strategy == 'reflexion'`; body=1 else=1
  - L56: IF `strategy == 'immediate-reflexion'`; body=1 else=1
  - L58: IF `strategy == 'immediate-refinement'`; body=1 else=1
  - L60: IF `strategy == 'reflexion-ucs'`; body=1 else=1
  - L62: IF `strategy == 'test-acc'`; body=1 else=1
- Main call graph hints: `kwargs_wrapper_gen`, `func`, `ValueError`
#### `main(args)` (L68)
- Inputs: parameters `main(args)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L70: IF `not os.path.exists(args.root_dir)`; body=1 else=0
  - L80: IF `not os.path.exists(log_dir)`; body=1 else=0
  - L87: IF `args.verbose`; body=1 else=1
  - L98: IF `args.dataset_path.endswith('.jsonl')`; body=1 else=1
  - L100: IF `args.dataset_path.endswith('.jsonl.gz')`; body=1 else=1
- I/O calls:
  - L70: `os.path.exists`
  - L80: `os.path.exists`
  - L99: `read_jsonl`
  - L101: `read_jsonl_gz`
- Main call graph hints: `os.path.basename.replace`, `os.path.join`, `strategy_factory`, `print`, `args.dataset_path.endswith`, `run_strategy`, `os.path.exists`, `os.makedirs`, `read_jsonl`, `os.path.basename`, `read_jsonl_gz`, `ValueError`, `len`

---

## File: `programming_runs/reflexion.py`

**Lines:** 102  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl, resume_success_count`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module-level assignments
- None

### Prompt-like assignments
- L40 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L37 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, 1)`
- L59 `reflection`: `reflection = gen.self_reflection( cur_func_impl, cur_feedback, model)`
- L64 `cur_func_impl`: `cur_func_impl = gen.func_impl( func_sig=item["prompt"], model=model, strategy="reflexion", prev_func_impl=cur_func_impl, feedback=cur_feedback, self_reflection=reflection, )`

### Classes
- None

### Functions
#### `run_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` (L8)
- Inputs: parameters `run_reflexion(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, is_leetcode)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L26: {'line': 26, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 14, 'orelse_len': 0}
  - L33: {'line': 33, 'type': 'while', 'test': 'cur_pass < pass_at_k and (not is_solved)', 'body_len': 11, 'orelse_len': 0}
  - L57: {'line': 57, 'type': 'while', 'test': 'cur_iter < max_iters', 'body_len': 9, 'orelse_len': 0}
- Decisions / conditions:
  - L34: IF `is_leetcode`; body=1 else=1
  - L47: IF `is_passing`; body=4 else=0
  - L81: IF `is_passing or cur_iter == max_iters - 1`; body=3 else=0
  - L84: IF `is_passing`; body=3 else=0
- I/O calls:
  - L98: `write_jsonl`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `resume_success_count`, `enumerate_resume`, `write_jsonl`, `print_v`, `gen.func_impl`, `implementations.append`, `isinstance`, `exe.execute`, `test_feedback.append`, `gen.internal_tests`, `exe.evaluate`, `int`, `gen.self_reflection`, `round`

---

## File: `programming_runs/reflexion_ucs.py`

**Lines:** 184  

### Imports
- `import warnings`
- `from lazzzy.ucs import ucs`
- `from utils import enumerate_resume, write_jsonl`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List, Set, Tuple`

### Module-level assignments
- L10: `DEBUG = True`

### Prompt-like assignments
- L66 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, 1)`
- L72 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`
- L87 `reflection`: `reflection = gen.self_reflection( cur_func_impl, feedback, model)`
- L91 `start`: `start = State(cur_func_impl, feedback, reflection, state)`
- L104 `new_funcs`: `new_funcs = gen.func_impl( func_sig=item["prompt"], model=model, strategy="reflexion", prev_func_impl=state.code, feedback=state.feedback, self_reflection=state.reflection, num_comps=expansion_factor, temperature=0.75 )`
- L135 `new_reflection`: `new_reflection = gen.self_reflection( new_func, feedback, model)`

### Classes
#### Class `State` L18 bases=[]
##### `__init__(self, code, feedback, reflection, state)` (L19)
- Inputs: parameters `__init__(self, code, feedback, reflection, state)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `__repr__(self)` (L25)
- Inputs: parameters `__repr__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L26: `f'State(code={self.code}, feedback={self.feedback}, reflection={self.reflection}, state={self.state})'`
##### `is_goal(self)` (L28)
- Inputs: parameters `is_goal(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L29: `all(self.state)`
- Main call graph hints: `all`
##### `__hash__(self)` (L31)
- Inputs: parameters `__hash__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L32: `hash((self.code, self.feedback, self.reflection))`
- Main call graph hints: `hash`
##### `get_unique_id(self)` (L34)
- Inputs: parameters `get_unique_id(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L39: `res`
- Loops:
  - L36: {'line': 36, 'type': 'for', 'target': 'i', 'iter': 'range(len(self.state))', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `range`, `len`

### Functions
#### `debug_print(*args)` (L13)
- Inputs: parameters `debug_print(*args)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L14: IF `DEBUG`; body=1 else=0
- Main call graph hints: `print`
#### `run_reflexion_ucs(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, expansion_factor, is_leetcode)` (L42)
- Inputs: parameters `run_reflexion_ucs(dataset, model_name, language, max_iters, pass_at_k, log_path, verbose, expansion_factor, is_leetcode)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L145: `new_states`
  - L149: `min(l, key=lambda x: len([y for y in x.state if not y]))`
  - L133: `set([(State(new_func, feedback, '', new_state), 0)])`
- Loops:
  - L59: {'line': 59, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 10, 'orelse_len': 0}
  - L64: {'line': 64, 'type': 'while', 'test': 'cur_pass < pass_at_k and (not is_solved)', 'body_len': 21, 'orelse_len': 0}
  - L119: {'line': 119, 'type': 'for', 'target': 'new_func', 'iter': 'new_funcs', 'body_len': 9, 'orelse_len': 0}
- Decisions / conditions:
  - L181: IF `verbose`; body=1 else=0
  - L67: IF `len(tests_i) == 0`; body=1 else=0
  - L80: IF `is_passing`; body=4 else=0
  - L168: IF `is_passing`; body=4 else=0
  - L120: IF `new_func in already_seen`; body=2 else=0
  - L131: IF `is_passing`; body=1 else=0
- I/O calls:
  - L179: `write_jsonl`
  - L124: `already_seen.add`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `len`, `enumerate_resume`, `write_jsonl`, `debug_print`, `gen.internal_tests`, `gen.func_impl`, `isinstance`, `exe.execute`, `gen.self_reflection`, `reflections.append`, `State`, `ucs`, `exe.evaluate`, `print`, `warnings.warn`, `set`, `min`, `already_seen.add`, `new_states.add`, `x.is_goal`, `x.get_unique_id`, `round`

---

## File: `programming_runs/simple.py`

**Lines:** 46  

### Imports
- `from utils import enumerate_resume, make_printv, write_jsonl`
- `from executors import executor_factory`
- `from generators import generator_factory, model_factory`
- `from typing import List`

### Module-level assignments
- L7: `SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."`
- L8: `SIMPLE_CHAT_INSTRUCTION = "You are a programming assistant. You will be given a function signature and docstring. You should fill in the following text of the missing function body. For example, the first line of the completion should have 4 spaces for the indendation so that it fits syntactically with the preceding signature."`

### Prompt-like assignments
- L7 `SIMPLE_COMPLETION_INSTRUCTION`: `SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."`
- L8 `SIMPLE_CHAT_INSTRUCTION`: `SIMPLE_CHAT_INSTRUCTION = "You are a programming assistant. You will be given a function signature and docstring. You should fill in the following text of the missing function body. For example, the first line of the completion should have 4 spaces for the indendation so that it fits syntacticall...`
- L32 `cur_func_impl`: `cur_func_impl = gen.func_impl(item["prompt"], model, "simple")`

### Classes
- None

### Functions
#### `run_simple(dataset, model_name, language, pass_at_k, log_path, verbose, is_leetcode)` (L10)
- Inputs: parameters `run_simple(dataset, model_name, language, pass_at_k, log_path, verbose, is_leetcode)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 8, 'orelse_len': 0}
  - L31: {'line': 31, 'type': 'while', 'test': 'cur_pass < pass_at_k', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L35: IF `is_passing`; body=3 else=0
- I/O calls:
  - L43: `write_jsonl`
- Main call graph hints: `executor_factory`, `generator_factory`, `model_factory`, `make_printv`, `len`, `enumerate_resume`, `write_jsonl`, `print_v`, `gen.func_impl`, `isinstance`, `exe.evaluate`, `round`

---

## File: `programming_runs/test_acc.py`

**Lines:** 48  

### Imports
- `from utils import enumerate_resume, write_jsonl, make_printv`
- `from executors import executor_factory`
- `from generators import generator_factory`
- `from typing import List`

### Module-level assignments
- None

### Prompt-like assignments
- L29 `tests_i`: `tests_i = gen.internal_tests(item["prompt"], model, 1)`
- L32 `cur_func_impl`: `cur_func_impl = item["prompt"] + item["canonical_solution"]`

### Classes
- None

### Functions
#### `run_test_acc(dataset, model, language, pass_at_k, log_path, verbose, is_leetcode)` (L8)
- Inputs: parameters `run_test_acc(dataset, model, language, pass_at_k, log_path, verbose, is_leetcode)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L24: {'line': 24, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate_resume(dataset, log_path)', 'body_len': 8, 'orelse_len': 0}
  - L28: {'line': 28, 'type': 'while', 'test': 'cur_pass < pass_at_k', 'body_len': 7, 'orelse_len': 0}
- Decisions / conditions:
  - L36: IF `is_passing`; body=3 else=0
- I/O calls:
  - L44: `write_jsonl`
- Main call graph hints: `executor_factory`, `generator_factory`, `make_printv`, `len`, `enumerate_resume`, `write_jsonl`, `print_v`, `gen.internal_tests`, `exe.execute`, `round`

---

## File: `programming_runs/utils.py`

**Lines:** 75  

### Imports
- `import os`
- `import gzip`
- `import json`
- `import openai`
- `import jsonlines`
- `from typing import List`

### Module-level assignments
- L9: `openai.api_key = os.getenv("OPENAI_API_KEY")`

### Prompt-like assignments
- None

### Classes
- None

### Functions
#### `make_printv(verbose)` (L12)
- Inputs: parameters `make_printv(verbose)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L19: `print_v`
- Decisions / conditions:
  - L14: IF `verbose`; body=2 else=1
- Main call graph hints: `print`
#### `read_jsonl(path)` (L22)
- Inputs: parameters `read_jsonl(path)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L31: `items`
- Loops:
  - L29: {'line': 29, 'type': 'for', 'target': 'item', 'iter': 'reader', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L23: IF `not os.path.exists(path)`; body=1 else=1
  - L25: IF `not path.endswith('.jsonl')`; body=1 else=0
- I/O calls:
  - L23: `os.path.exists`
  - L28: `jsonlines.open`
- Main call graph hints: `os.path.exists`, `FileNotFoundError`, `jsonlines.open`, `path.endswith`, `ValueError`
#### `write_jsonl(path, data, append)` (L34)
- Inputs: parameters `write_jsonl(path, data, append)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L36: {'line': 36, 'type': 'for', 'target': 'item', 'iter': 'data', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L35: `jsonlines.open`
  - L37: `writer.write`
- Main call graph hints: `jsonlines.open`, `writer.write`
#### `read_jsonl_gz(path)` (L40)
- Inputs: parameters `read_jsonl_gz(path)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L45: `data`
- Decisions / conditions:
  - L41: IF `not path.endswith('.jsonl.gz')`; body=1 else=0
- I/O calls:
  - L43: `gzip.open`
  - L44: `json.loads`
- Main call graph hints: `path.endswith`, `ValueError`, `gzip.open`, `json.loads`
#### `enumerate_resume(dataset, results_path)` (L51)
- Inputs: parameters `enumerate_resume(dataset, results_path)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L53: {'line': 53, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(dataset)', 'body_len': 1, 'orelse_len': 0}
  - L61: {'line': 61, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(dataset)', 'body_len': 2, 'orelse_len': 0}
  - L58: {'line': 58, 'type': 'for', 'target': 'item', 'iter': 'reader', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L52: IF `not os.path.exists(results_path)`; body=1 else=3
  - L63: IF `i < count`; body=1 else=0
- I/O calls:
  - L52: `os.path.exists`
  - L57: `jsonlines.open`
- Main call graph hints: `os.path.exists`, `enumerate`, `jsonlines.open`
#### `resume_success_count(dataset)` (L68)
- Inputs: parameters `resume_success_count(dataset)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L73: `count`
- Loops:
  - L70: {'line': 70, 'type': 'for', 'target': 'item', 'iter': 'dataset', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L71: IF `'is_solved' in item and item['is_solved']`; body=1 else=0

---

## File: `programming_runs/validate_py_results.py`

**Lines:** 55  

### Imports
- `import sys`
- `import signal`
- `from utils import read_jsonl`

### Module-level assignments
- L6: `TIMEOUT = 5`
- L9: `LOG_PATH = sys.argv[1]`

### Prompt-like assignments
- L30 `code`: `code = f'{item["prompt"]}{func_impl}\n\n{item["test"]}\n\ncheck({item["entry_point"]})'`

### Top-level logic
- L53 If: `if __name__ == "__main__": validate_py_results(LOG_PATH)`

### Classes
- None

### Functions
#### `red_text(text)` (L11)
- Inputs: parameters `red_text(text)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L12: `f'\x1b[91m{text}\x1b[0m'`
#### `green_text(text)` (L14)
- Inputs: parameters `green_text(text)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L15: `f'\x1b[92m{text}\x1b[0m'`
#### `count_test_cases(test_str)` (L17)
- Inputs: parameters `count_test_cases(test_str)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L19: `test_str.count('assert')`
- Main call graph hints: `test_str.count`
#### `validate_py_results(log_path)` (L22)
- Inputs: parameters `validate_py_results(log_path)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(data)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L23: IF `not log_path.endswith('.jsonl')`; body=1 else=0
  - L28: IF `item['is_solved']`; body=4 else=2
- Exception handling:
  - L32: handlers=['Exception'] final=0
- I/O calls:
  - L25: `read_jsonl`
- Main call graph hints: `read_jsonl`, `enumerate`, `print`, `log_path.endswith`, `ValueError`, `count_test_cases`, `red_text`, `signal.signal`, `signal.alarm`, `exec`, `green_text`, `len`, `round`, `Exception`, `globals`, `str`

---

## File: `programming_runs/validate_rs_results.py`

**Lines:** 50  

### Imports
- `import sys`
- `import signal`
- `from utils import read_jsonl`
- `from executors import RsExecutor`

### Module-level assignments
- L7: `TIMEOUT = 5`
- L10: `LOG_PATH = sys.argv[1]`

### Prompt-like assignments
- None

### Top-level logic
- L48 If: `if __name__ == "__main__": validate_rs_results(LOG_PATH)`

### Classes
- None

### Functions
#### `red_text(text)` (L12)
- Inputs: parameters `red_text(text)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L13: `f'\x1b[91m{text}\x1b[0m'`
#### `green_text(text)` (L15)
- Inputs: parameters `green_text(text)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L16: `f'\x1b[92m{text}\x1b[0m'`
#### `count_test_cases(test_str)` (L18)
- Inputs: parameters `count_test_cases(test_str)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L20: `test_str.count('assert_eq')`
- Main call graph hints: `test_str.count`
#### `validate_rs_results(log_path)` (L23)
- Inputs: parameters `validate_rs_results(log_path)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L28: {'line': 28, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(data)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L24: IF `not log_path.endswith('.jsonl')`; body=1 else=0
  - L29: IF `item['is_solved']`; body=5 else=2
  - L35: IF `res`; body=3 else=2
- I/O calls:
  - L26: `read_jsonl`
- Main call graph hints: `read_jsonl`, `enumerate`, `print`, `log_path.endswith`, `ValueError`, `count_test_cases`, `RsExecutor`, `rs_executor.evaluate`, `red_text`, `green_text`, `len`, `round`

---

## File: `webshop_runs/env_history.py`

**Lines:** 52  

### Imports
- `from typing import List, Dict`

### Module-level assignments
- None

### Prompt-like assignments
- L6 `_cur_query`: `self._cur_query: str = f'{_get_base_query(base_query, start_info, memory)}'`

### Classes
#### Class `EnvironmentHistory` L4 bases=[]
##### `__init__(self, base_query, start_info, memory, history)` (L5)
- Inputs: parameters `__init__(self, base_query, start_info, memory, history)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `_get_base_query`
##### `add(self, label, value)` (L11)
- Inputs: parameters `add(self, label, value)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L17: IF `label == 'action'`; body=1 else=0
  - L18: IF `value == self._last_action`; body=1 else=1
##### `check_is_exhausted(self)` (L23)
- Inputs: parameters `check_is_exhausted(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L24: `self._is_exhausted`
##### `reset(self)` (L26)
- Inputs: parameters `reset(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `__str__(self)` (L29)
- Inputs: parameters `__str__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L40: `s`
- Loops:
  - L31: {'line': 31, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(self._history)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L32: IF `item['label'] == 'action'`; body=1 else=1
  - L38: IF `i != len(self._history) - 1`; body=1 else=0
  - L34: IF `item['label'] == 'observation'`; body=1 else=1
  - L36: IF `item['label'] == 'human_edit'`; body=1 else=0
- Main call graph hints: `enumerate`, `len`

### Functions
#### `_get_base_query(base_query, start_info, memory)` (L42)
- Inputs: parameters `_get_base_query(base_query, start_info, memory)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L51: `query`
- Loops:
  - L48: {'line': 48, 'type': 'for', 'target': '(i, m)', 'iter': 'enumerate(memory)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L46: IF `len(memory) > 0`; body=2 else=0
- Main call graph hints: `len`, `enumerate`, `m.strip`

---

## File: `webshop_runs/generate_reflections.py`

**Lines:** 48  

### Imports
- `from utils import get_completion`
- `from typing import List, Dict, Any`

### Module-level assignments
- None

### Prompt-like assignments
- L15 `query`: `query: str = f"""You will be given the history of a past experience in which you were placed in an environment and given a task to complete. You were unsuccessful in completing the task. Do not summarize your environment, but rather think about the strategy and path you took to attempt to complet...`
- L43 `reflection_query`: `reflection_query: str = _generate_reflection_query(env_logs[i], memory)`

### Classes
- None

### Functions
#### `_get_scenario(s)` (L8)
- Docstring: Parses the relevant scenario from the experience log.
- Inputs: parameters `_get_scenario(s)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L10: `s.split('Instruction:')[-1].strip()`
- Main call graph hints: `s.split[...].strip`, `s.split`
#### `_generate_reflection_query(log_str, memory)` (L12)
- Docstring: Allows the Agent to reflect upon a past experience.
- Inputs: parameters `_generate_reflection_query(log_str, memory)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L27: `query`
- Loops:
  - L23: {'line': 23, 'type': 'for', 'target': '(i, m)', 'iter': 'enumerate(memory)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L21: IF `len(memory) > 0`; body=2 else=0
- Main call graph hints: `_get_scenario`, `len`, `enumerate`
#### `update_memory(trial_log_path, env_configs)` (L29)
- Docstring: Updates the given env_config with the appropriate reflections.
- Inputs: parameters `update_memory(trial_log_path, env_configs)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L47: `env_configs`
- Loops:
  - L36: {'line': 36, 'type': 'for', 'target': '(i, env)', 'iter': 'enumerate(env_configs)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L38: IF `not env['is_success']`; body=4 else=0
  - L39: IF `len(env['memory']) > 3`; body=1 else=1
- LLM/model calls:
  - L43: `_generate_reflection_query`
  - L44: `get_completion`
- I/O calls:
  - L31: `open`
  - L32: `f.read`
- Main call graph hints: `full_log.split`, `print`, `enumerate`, `open`, `f.read`, `len`, `_generate_reflection_query`, `get_completion`

---

## File: `webshop_runs/main.py`

**Lines:** 119  

### Imports
- `import os`
- `import json`
- `import argparse`
- `from webshop_trial import run_trial`
- `from generate_reflections import update_memory`
- `from typing import Any, List, Dict`

### Module-level assignments
- None

### Prompt-like assignments
- L103 `env_configs`: `env_configs: List[Dict[str, Any]] = update_memory(trial_log_path, env_configs)`

### Top-level logic
- L116 If: `if __name__ == '__main__': args = get_args() main(args)`

### Classes
- None

### Functions
#### `get_args()` (L11)
- Inputs: parameters `get_args()` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L26: `args`
- Main call graph hints: `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`
#### `main(args)` (L28)
- Inputs: parameters `main(args)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L86: {'line': 86, 'type': 'while', 'test': 'trial_idx < args.num_trials', 'body_len': 10, 'orelse_len': 0}
  - L48: {'line': 48, 'type': 'for', 'target': 'i', 'iter': 'range(args.num_envs)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L29: IF `args.is_resume`; body=5 else=4
  - L58: IF `args.is_resume`; body=1 else=1
  - L30: IF `not os.path.exists(args.resume_dir)`; body=1 else=0
  - L36: IF `not os.path.exists(env_config_path)`; body=1 else=0
  - L42: IF `not os.path.exists(args.run_name)`; body=1 else=0
  - L93: IF `os.path.exists(trial_log_path)`; body=1 else=0
  - L95: IF `os.path.exists(trial_env_configs_log_path)`; body=1 else=0
  - L102: IF `args.use_memory`; body=1 else=0
- I/O calls:
  - L93: `os.path.exists`
  - L95: `os.path.exists`
  - L30: `os.path.exists`
  - L36: `os.path.exists`
  - L38: `open`
  - L39: `json.load`
  - L42: `os.path.exists`
  - L87: `open`
  - L88: `wf.write`
  - L94: `open.close`
  - L96: `open.close`
  - L106: `open`
  - L107: `json.dump`
  - L110: `open`
  - L111: `wf.write`
  - L94: `open`
  - L96: `open`
- Main call graph hints: `os.path.join`, `range`, `print`, `os.path.exists`, `run_trial`, `ValueError`, `open`, `json.load`, `os.makedirs`, `wf.write`, `open.close`, `update_memory`, `json.dump`

---

## File: `webshop_runs/utils.py`

**Lines:** 32  

### Imports
- `import os`
- `import openai`
- `from tenacity import ( retry, stop_after_attempt, # type: ignore wait_random_exponential, # type: ignore )`
- `from typing import Optional, List, Union`

### Module-level assignments
- L11: `openai.api_key = os.getenv('OPENAI_API_KEY')`

### Prompt-like assignments
- L16 `response`: `response = openai.Completion.create( model='text-davinci-003', prompt=prompt, temperature=0.0, max_tokens=max_tokens, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=stop_strs, )`

### Classes
- None

### Functions
#### `get_completion(prompt, max_tokens, stop_strs, is_batched)` (L14)
- Inputs: parameters `get_completion(prompt, max_tokens, stop_strs, is_batched)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L31: `response.choices[0].text`
  - L30: `res`
- Loops:
  - L28: {'line': 28, 'type': 'for', 'target': 'choice', 'iter': 'response.choices', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L26: IF `is_batched`; body=3 else=0
- LLM/model calls:
  - L16: `openai.Completion.create`
- I/O calls:
  - L16: `openai.Completion.create`
- Main call graph hints: `retry`, `openai.Completion.create`, `wait_random_exponential`, `stop_after_attempt`, `isinstance`, `len`

---

## File: `webshop_runs/webshop_trial.py`

**Lines:** 312  

### Imports
- `import os`
- `import sys`
- `import openai`
- `import requests`
- `from bs4 import BeautifulSoup`
- `from bs4.element import Comment`
- `from env_history import EnvironmentHistory`
- `from typing import Any, Dict, List, Tuple`

### Module-level assignments
- L11: `openai.api_key = os.environ["OPENAI_API_KEY"]`
- L13: `WEBSHOP_URL = "http://3.83.245.205:3000"`
- L14: `ACTION_TO_TEMPLATE = { 'Description': 'description_page.html', 'Features': 'features_page.html', 'Reviews': 'review_page.html', 'Attributes': 'attributes_page.html', }`

### Prompt-like assignments
- L14 `ACTION_TO_TEMPLATE`: `ACTION_TO_TEMPLATE = { 'Description': 'description_page.html', 'Features': 'features_page.html', 'Reviews': 'review_page.html', 'Attributes': 'attributes_page.html', }`
- L215 `env_history`: `env_history = EnvironmentHistory(base_prompt, observation, memory[-3:], [])`
- L217 `env_history`: `env_history = EnvironmentHistory(base_prompt, observation, memory, [])`
- L245 `action`: `action = llm(init_prompt + prompt[-(6400-len(init_prompt)):], stop=['\n']).lstrip(' ')`
- L27 `response`: `response = openai.Completion.create( model="text-davinci-002", prompt=prompt, temperature=cur_try * 0.2, max_tokens=100, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=stop )`
- L273 ``: `final_env_history, is_success = webshop_run(f'fixed_{z}', env, BASE_PROMPT, env_config["memory"] if use_memory else [], to_print=True)`

### Classes
#### Class `webshopEnv` L142 bases=[]
##### `__init__(self)` (L143)
- Inputs: parameters `__init__(self)` plus globals/config/memory/env state as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `step(self, session, action)` (L146)
- Inputs: parameters `step(self, session, action)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L205: `(observation, reward, done)`
- Decisions / conditions:
  - L149: IF `action == 'reset'`; body=1 else=1
  - L201: IF `observation_`; body=1 else=0
  - L151: IF `action.startswith('think[')`; body=1 else=1
  - L153: IF `action.startswith('search[')`; body=3 else=1
  - L158: IF `action.startswith('click[')`; body=2 else=1
  - L160: IF `button == 'Buy Now'`; body=3 else=1
  - L164: IF `button == 'Back to Search'`; body=2 else=1
  - L167: IF `button == 'Next >'`; body=3 else=1
  - L171: IF `button == '< Prev'`; body=2 else=1
  - L173: IF `self.sessions[session]['page_type'] == 'search'`; body=2 else=1
  - L181: IF `button in ACTION_TO_TEMPLATE`; body=3 else=1
  - L176: IF `self.sessions[session]['page_type'] == 'item_sub'`; body=1 else=1
  - L186: IF `self.sessions[session]['page_type'] == 'search'`; body=3 else=1
  - L178: IF `self.sessions[session]['page_type'] == 'item'`; body=2 else=0
  - L190: IF `self.sessions[session]['page_type'] == 'item'`; body=6 else=0
  - L194: IF `not 'options' in self.sessions[session]`; body=1 else=0
- Main call graph hints: `webshop_text`, `self.sessions[...].update`, `info.get`, `action.startswith`, `self.sessions[...].get`

### Functions
#### `llm(prompt, stop)` (L23)
- Inputs: parameters `llm(prompt, stop)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L42: `''`
  - L40: `response['choices'][0]['text']`
- Loops:
  - L26: {'line': 26, 'type': 'while', 'test': 'cur_try < 6', 'body_len': 4, 'orelse_len': 0}
- Decisions / conditions:
  - L39: IF `len(text.strip()) >= 5`; body=1 else=0
- Exception handling:
  - L24: handlers=['Exception'] final=0
- LLM/model calls:
  - L27: `openai.Completion.create`
- I/O calls:
  - L27: `openai.Completion.create`
- Main call graph hints: `openai.Completion.create`, `print`, `sys.exit`, `len`, `text.strip`
#### `clean_str(p)` (L48)
- Inputs: parameters `clean_str(p)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L49: `p.encode().decode('unicode-escape').encode('latin1').decode('utf-8')`
- Main call graph hints: `p.encode.decode.encode.decode`, `p.encode.decode.encode`, `p.encode.decode`, `p.encode`
#### `tag_visible(element)` (L51)
- Inputs: parameters `tag_visible(element)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L53: `element.parent.name not in ignore and (not isinstance(element, Comment))`
- Main call graph hints: `isinstance`
#### `webshop_text(session, page_type, query_string, page_num, asin, options, subpage, **kwargs)` (L57)
- Inputs: parameters `webshop_text(session, page_type, query_string, page_num, asin, options, subpage, **kwargs)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L91: `' [SEP] '.join((t.strip() for t in visible_texts if t != '\n'))`
  - L140: `(clean_str(observation), info)`
- Loops:
  - L101: {'line': 101, 'type': 'for', 'target': 't', 'iter': 'visible_texts', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L58: IF `page_type == 'init'`; body=1 else=0
  - L62: IF `page_type == 'search'`; body=1 else=1
  - L89: IF `False`; body=1 else=13
  - L67: IF `page_type == 'item'`; body=1 else=1
  - L132: IF `options`; body=1 else=0
  - L134: IF `asins`; body=1 else=0
  - L136: IF `'Your score (min 0.0, max 1.0)' in visible_texts`; body=3 else=0
  - L72: IF `page_type == 'item_sub'`; body=1 else=1
  - L102: IF `t == '\n'`; body=1 else=0
  - L103: IF `t.replace('\n', '').replace('\\n', '').replace(' ', '') == ''`; body=1 else=0
  - L106: IF `t.parent.name == 'button'`; body=1 else=1
  - L77: IF `page_type == 'end'`; body=1 else=0
  - L108: IF `t.parent.name == 'label'`; body=2 else=1
  - L109: IF `f"'{t}'" in url`; body=1 else=1
  - L116: IF `t.parent.get('class') == ['product-link']`; body=5 else=5
  - L118: IF `prod_cnt >= 3`; body=1 else=0
  - L125: IF `cnt < 2 and page_type != 'init'`; body=1 else=0
  - L126: IF `just_prod <= 2 and prod_cnt >= 4`; body=1 else=0
- Main call graph hints: `BeautifulSoup`, `html_obj.findAll`, `list`, `requests.get`, `filter`, `Constant.join`, `visible_texts.index`, `float`, `clean_str`, `t.strip`, `t.replace.replace.replace`, `t.replace.replace`, `str`, `t.parent.get`, `asins.append`, `t.replace`
#### `webshop_run(idx, env, base_prompt, memory, to_print)` (L207)
- Inputs: parameters `webshop_run(idx, env, base_prompt, memory, to_print)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L247: `(env_history, False)`
  - L243: `(env_history, res[1] == 1.0)`
- Loops:
  - L219: {'line': 219, 'type': 'for', 'target': 'i', 'iter': 'range(15)', 'body_len': 8, 'orelse_len': 0}
- Decisions / conditions:
  - L214: IF `len(memory) > 3`; body=1 else=1
  - L227: IF `action.startswith('think')`; body=1 else=0
  - L230: IF `to_print`; body=2 else=0
  - L233: IF `i`; body=1 else=1
  - L241: IF `res[2]`; body=2 else=0
- Exception handling:
  - L221: handlers=['AssertionError'] final=0
- LLM/model calls:
  - L245: `llm.lstrip`
  - L245: `llm`
- Main call graph hints: `env.step`, `env_history.reset`, `range`, `len`, `EnvironmentHistory`, `env_history.add`, `action.startswith`, `llm.lstrip`, `print`, `sys.stdout.flush`, `llm`
#### `run_trial(trial_log_path, world_log_path, trial_idx, env_configs, use_memory)` (L249)
- Inputs: parameters `run_trial(trial_log_path, world_log_path, trial_idx, env_configs, use_memory)` plus globals/config/memory/env state as referenced.
- Outputs / returns:
  - L311: `env_configs`
- Loops:
  - L262: {'line': 262, 'type': 'for', 'target': '(z, env_config)', 'iter': 'enumerate(env_configs)', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L263: IF `env_config['is_success']`; body=4 else=0
  - L274: IF `is_success`; body=4 else=1
- Exception handling:
  - L272: handlers=['AssertionError'] final=0
- I/O calls:
  - L306: `open`
  - L307: `wf.write`
  - L308: `open`
  - L309: `wf.write`
  - L294: `open`
  - L295: `f.write`
  - L266: `open`
  - L267: `wf.write`
  - L268: `open`
  - L269: `wf.write`
  - L283: `open`
  - L284: `wf.write`
  - L290: `open`
  - L291: `wf.write`
- Main call graph hints: `webshopEnv`, `len`, `enumerate`, `open`, `wf.write`, `webshop_run`, `f.write`, `round`, `str`