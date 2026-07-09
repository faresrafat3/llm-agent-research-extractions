# Meta-Prompting — Complete Python Logic / Flow / Loops / Conditions / I-O Extraction

Source repo: `https://github.com/suzgunmirac/meta-prompting`  
Audited commit: `40422564938d772c3e3e6b9614b1df48b8dd6a08`

## System summary

The code loads task data and prompt scaffolds, chooses a prompting method, builds a question prefix, calls a language model, optionally dispatches expert calls through `MetaPromptingScaffolding`, optionally executes Python expert code, records model outputs, and evaluates output files with task-specific answer extraction/evaluation.

## Python files

- `evaluate_outputs.py`
- `run_experiments.py`
- `utils/__init__.py`
- `utils/execute_code.py`
- `utils/expert_prompting.py`
- `utils/language_model.py`
- `utils/meta_scaffolding.py`
- `utils/sonnet_eval.py`

---

## File: `evaluate_outputs.py`

**Lines:** 274  

### Imports
- `import json`
- `import re`
- `from glob import glob`
- `from tap import Tap`
- `from joblib import Parallel, delayed`
- `from utils.execute_code import execute_code_with_timeout`
- `from utils.sonnet_eval import sonnet_errors`

### Module-level assignments
- None

### Prompt-like assignments
- L189 `code`: `code = f"{output}\nanswer = solution()\nprint(sat(answer))"`
- L191 `code`: `code = f"from typing import *\n{input}\n{output}\nanswer = solution()\nprint(sat(answer))"`
- L227 `output`: `output = extract_answer( txt=output, first_split='>> FINAL ANSWER:\n"""', second_split='"""' )`

### Top-level logic
- L271 If: `if __name__ == "__main__": args = Arguments().parse_args() main(args)`

### Classes
#### Class `Arguments` L236 bases=['Tap']
- Docstring: The arguments to pass to the program.

### Functions
#### `extract_answer(txt, first_split, second_split)` (L15)
- Docstring: Given a string, extract the answer between the first and second split.

Args:
    txt (str): The string to extract the answer from.
    first_split (str): The first split.
    second_split (str): The second split.

Returns:
    str: The final answer.
- Inputs: parameters `extract_answer(txt, first_split, second_split)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L32: `second_split`
  - L34: `None`
- Exception handling:
  - L29: handlers=['Exception'] final=0
- Main call graph hints: `txt.split`, `first_split.split`
#### `clean_output_for_arithmetic(output)` (L37)
- Docstring: Clean the output for arithmetic problems.

Args:
    output (str): The output to clean.

Returns:
    str: The cleaned output.
- Inputs: parameters `clean_output_for_arithmetic(output)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L57: `output`
- Decisions / conditions:
  - L47: IF `'=' in output`; body=1 else=0
  - L49: IF `' is' in output`; body=1 else=0
  - L51: IF `' equals' in output`; body=1 else=0
  - L53: IF `' evaluates to' in output`; body=1 else=0
  - L55: IF `' is equal to' in output`; body=1 else=0
- Main call graph hints: `output.split[...].strip`, `output.split`
#### `clean_output_for_GameOf24(output)` (L60)
- Docstring: Clean the output for GameOf24 problems.
- Inputs: parameters `clean_output_for_GameOf24(output)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L72: `output`
- Decisions / conditions:
  - L64: IF `'=' in output`; body=1 else=0
  - L66: IF `'is' in output`; body=1 else=0
  - L68: IF `'equals' in output`; body=1 else=0
  - L70: IF `'evaluates to' in output`; body=1 else=0
- Main call graph hints: `output.split[...].strip`, `output.split`
#### `eval_for_GameOf24(input, output)` (L75)
- Docstring: Given an input and output, check if the output is correct and follows the rules of the game.
- Inputs: parameters `eval_for_GameOf24(input, output)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L101: `True`
  - L84: `False`
  - L100: `False`
  - L103: `False`
- Loops:
  - L89: {'line': 89, 'type': 'for', 'target': 'symbol', 'iter': 'replacements', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L83: IF `not abs(value - 24) < 0.001`; body=1 else=0
  - L99: IF `input_digits != output_digits`; body=1 else=0
- Exception handling:
  - L80: handlers=['Exception'] final=0
- Main call graph hints: `clean_output_for_GameOf24`, `eval`, `input.split`, `re.sub`, `clean_output.strip`, `clean_output.split`, `input_digits.sort`, `output_digits.sort`, `clean_output.replace`, `abs`
#### `remove_punctuation(output)` (L106)
- Inputs: parameters `remove_punctuation(output)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L110: `output`
- Loops:
  - L108: {'line': 108, 'type': 'for', 'target': 'marker', 'iter': 'markers', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `output.replace`
#### `convert_newline_to_space(output)` (L113)
- Inputs: parameters `convert_newline_to_space(output)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L115: `output`
- Main call graph hints: `output.replace`
#### `eval_for_exact_matching_with_no_punctuation(input, output, target)` (L118)
- Inputs: parameters `eval_for_exact_matching_with_no_punctuation(input, output, target)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L125: `False`
  - L124: `True`
- Decisions / conditions:
  - L123: IF `target == output`; body=1 else=0
- Main call graph hints: `remove_punctuation`, `convert_newline_to_space`
#### `eval_for_softmatch(input, output, target)` (L128)
- Inputs: parameters `eval_for_softmatch(input, output, target)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L132: `False`
  - L131: `True`
- Decisions / conditions:
  - L130: IF `target in output`; body=1 else=0
- Main call graph hints: `remove_punctuation`
#### `eval_for_CheckmateInOne(input, output, target)` (L135)
- Inputs: parameters `eval_for_CheckmateInOne(input, output, target)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L152: `False`
  - L147: `True`
  - L151: `True`
- Decisions / conditions:
  - L140: IF `last_move == ''`; body=1 else=1
  - L145: IF `not next_move_idx in output`; body=1 else=2
  - L146: IF `target in output`; body=1 else=0
  - L150: IF `target in output`; body=1 else=0
- Main call graph hints: `input.split[...].strip`, `input.split[...].split[...].strip`, `str`, `output.split[...].strip`, `int`, `input.split`, `input.split[...].split`, `output.split`
#### `eval_for_Sonnet(output, rhyme_scheme)` (L155)
- Inputs: parameters `eval_for_Sonnet(output, rhyme_scheme)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L160: `False`
  - L159: `True`
  - L162: `False`
- Decisions / conditions:
  - L158: IF `not errors`; body=1 else=0
- Exception handling:
  - L156: handlers=['Exception'] final=0
- Main call graph hints: `sonnet_errors`
#### `eval_for_multiple_choice(input, output, target)` (L165)
- Inputs: parameters `eval_for_multiple_choice(input, output, target)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L178: `False`
  - L167: `True`
- Decisions / conditions:
  - L166: IF `target in output[:len(target)]`; body=1 else=0
- Main call graph hints: `len`
#### `eval_for_pyton_programming_puzzles(input, output, target)` (L181)
- Inputs: parameters `eval_for_pyton_programming_puzzles(input, output, target)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L201: `False`
  - L200: `True`
- Decisions / conditions:
  - L182: IF `'```python' in output`; body=2 else=0
  - L186: IF `'def sat' in output`; body=2 else=1
  - L195: IF `"NameError: name 'answer' is not defined" in eval_bool`; body=3 else=0
  - L199: IF `'True' in eval_bool`; body=1 else=0
  - L187: IF `'from typing' not in output`; body=1 else=0
- Main call graph hints: `code.replace`, `execute_code_with_timeout`, `output.split[...].strip`, `print`, `output.split`
#### `run_eval(datum, task)` (L204)
- Inputs: parameters `run_eval(datum, task)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L212: `eval_for_GameOf24(input, output)`
  - L214: `eval_for_exact_matching_with_no_punctuation(input, output, target)`
  - L217: `decision`
  - L219: `eval_for_Sonnet(output, 'ABAB CDCD EFEF GG')`
  - L222: `decision`
  - L224: `eval_for_softmatch(input, output, target)`
  - L231: `decision`
- Decisions / conditions:
  - L211: IF `'GameOf24' in task`; body=1 else=1
  - L213: IF `any([x in task for x in ['word_sorting', 'multistep_arithmetic_two']])`; body=1 else=1
  - L215: IF `any([x in task for x in ['CheckmateInOne']])`; body=2 else=1
  - L218: IF `any([x in task for x in ['Sonnets-Standard']])`; body=1 else=1
  - L220: IF `any([x in task for x in ['geometric_shapes', 'ruin_names']])`; body=2 else=1
  - L223: IF `any([x in task for x in ['MGSM']])`; body=1 else=1
  - L225: IF `any([x in task for x in ['P3', 'P3_Test']])`; body=4 else=0
- Main call graph hints: `datum[...].lower`, `extract_answer.strip`, `print`, `eval_for_GameOf24`, `any`, `extract_answer`, `eval_for_exact_matching_with_no_punctuation`, `eval_for_CheckmateInOne`, `eval_for_Sonnet`, `eval_for_multiple_choice`, `eval_for_softmatch`, `eval_for_pyton_programming_puzzles`
#### `main(args)` (L245)
- Inputs: parameters `main(args)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L250: {'line': 250, 'type': 'for', 'target': 'file', 'iter': 'files', 'body_len': 8, 'orelse_len': 0}
- Decisions / conditions:
  - L251: IF `'data' in file`; body=1 else=0
  - L256: IF `len(data) == 0`; body=1 else=0
- I/O calls:
  - L248: `glob`
  - L253: `open`
  - L254: `json.loads`
  - L254: `f.readlines`
- Main call graph hints: `glob`, `files.sort`, `Parallel`, `sum`, `len`, `print`, `open`, `json.loads`, `delayed`, `f.readlines`

---

## File: `run_experiments.py`

**Lines:** 394  

### Imports
- `import sys`
- `from typing import Optional`
- `import os`
- `import json`
- `from tap import Tap`
- `from joblib import Parallel, delayed`
- `from utils.language_model import OpenAI_LanguageModel`
- `from utils.meta_scaffolding import MetaPromptingScaffolding`

### Module-level assignments
- L19: `DESCRIPTION_DICT = { "word_sorting": "Sort a list of words alphabetically, placing them in a single line of text separated by spaces.", "multistep_arithmetic_two": "Solve multi-step arithmetic problems.", "geometric_shapes": "Name geometric shapes from their SVG paths.", "test": "Please complete the task correctly.", "GameOf24": "Let's play a game called 24. You'll be given four integers, and y...`
- L41: `template_gen_expert_identity = """For each instruction, write a high-quality description about the most capable and suitable agent to answer the instruction. In second person perspective. [Instruction]: Make a list of 5 possible effects of deforestation. [Agent Description]: You are an environmental scientist with a specialization in the study of ecosystems and their interactions with human act...`

### Prompt-like assignments
- L19 `DESCRIPTION_DICT`: `DESCRIPTION_DICT = { "word_sorting": "Sort a list of words alphabetically, placing them in a single line of text separated by spaces.", "multistep_arithmetic_two": "Solve multi-step arithmetic problems.", "geometric_shapes": "Name geometric shapes from their SVG paths.", "test": "Please complete ...`
- L41 `template_gen_expert_identity`: `template_gen_expert_identity = """For each instruction, write a high-quality description about the most capable and suitable agent to answer the instruction. In second person perspective. [Instruction]: Make a list of 5 possible effects of deforestation. [Agent Description]: You are an environmen...`
- L85 `meta_config_path`: `meta_config_path: str = "prompts/meta-v0-2023-08-14-baseline.json"`
- L100 `question_suffix_or_path`: `question_suffix_or_path: str = "\n\nLet's first come up with a list of experts you may want to consult for this problem and then immediately start solving it."`
- L101 `intermediate_feedback`: `intermediate_feedback = "Based on the information given, what are the most logical next steps or conclusions? Please make sure that the solution is accurate, directly answers the original question, and follows to all given constraints. Additionally, please review the final solution yourself or ha...`
- L110 `expert_python_message`: `expert_python_message: str = 'You are an expert in Python and can generate Python code. To execute the code and display its output in the terminal using print statements, please make sure to include "Please run this code!" after the code block (i.e., after the closing code blocks)'`
- L172 `message_log`: `message_log = meta_model.meta_model_generate( prompt_or_messages=messages, max_tokens=meta_model_settings["parameters"]["max_tokens"], temperature=meta_model_settings["parameters"]["temperature"], top_p=meta_model_settings["parameters"]["top_p"], num_return_sequences=meta_model_settings["paramete...`
- L204 `meta_model_message_list`: `meta_model_message_list = meta_prompt_config_dict["meta-model"]["message-list"]`
- L245 `meta_model_settings`: `meta_model_settings = meta_prompt_config_dict["meta-model"]`
- L246 `generator_settings`: `generator_settings = meta_prompt_config_dict["generator"]`
- L247 `verifier_settings`: `verifier_settings = meta_prompt_config_dict["verifier"]`
- L248 `summarizer_settings`: `summarizer_settings = meta_prompt_config_dict["summarizer"]`
- L251 ``: `meta_model_settings["parameters"]["temperature"] = ( args.temperature if args.temperature is not None else meta_model_settings["parameters"]["temperature"] )`
- L256 ``: `meta_model_settings["parameters"]["top_p"] = ( args.top_p if args.top_p is not None else meta_model_settings["parameters"]["top_p"] )`
- L261 ``: `meta_model_settings["parameters"]["max_tokens"] = ( args.max_tokens if args.max_tokens is not None else meta_model_settings["parameters"]["max_tokens"] )`
- L266 ``: `meta_model_settings["parameters"]["num_return_sequences"] = ( args.num_return_sequences if args.num_return_sequences is not None else meta_model_settings["parameters"]["num_return_sequences"] )`
- L313 `error_message`: `error_message = meta_prompt_config_dict["meta-model"]["error-message"]`
- L314 `final_answer_indicator`: `final_answer_indicator = meta_prompt_config_dict["meta-model"][ "final-answer-indicator" ]`
- L332 `meta_model`: `meta_model = MetaPromptingScaffolding( language_model=model, fresh_eyes=args.fresh_eyes, generator_settings=generator_settings, verifier_settings=verifier_settings, summarizer_settings=summarizer_settings, error_message=error_message, final_answer_indicator=final_answer_indicator, include_expert_...`
- L134 `expert_messages`: `expert_messages = [ { "role": "user", "content": f"{template_gen_expert_identity}\n\n[Instruction]:{input}\n[Agent Description]:", } ]`
- L142 `expert_identity`: `expert_identity = meta_model.generate( prompt_or_messages=expert_messages, max_tokens=meta_model_settings["parameters"]["max_tokens"], num_return_sequences=meta_model_settings["parameters"][ "num_return_sequences" ], temperature=meta_model_settings["parameters"]["temperature"], top_p=meta_model_s...`
- L153 `template_expert_prompting`: `template_expert_prompting = f"{expert_identity}\n\nNow given the above identity background, please answer the following question:\n\nQuestion: {task_description}\n\n{input}"`
- L361 `outputs`: `outputs = Parallel(n_jobs=6, verbose=100, prefer="threads")( delayed(run_model)( meta_model=meta_model, datum=datum, prefix_messages=meta_model_message_list, task_description=task_description, meta_model_settings=meta_model_settings, question_suffix=args.question_suffix_or_path, question_prefix=a...`
- L386 `temp_dict`: `temp_dict = {"args": args.as_dict(), "config_dict": meta_prompt_config_dict}`

### Top-level logic
- L390 If: `if __name__ == "__main__": # Parse the arguments args = Arguments().parse_args() main(args)`

### Classes
#### Class `Arguments` L53 bases=['Tap']

### Functions
#### `run_model(meta_model, datum, prefix_messages, task_description, meta_model_settings, question_prefix, question_suffix, expert_prompting)` (L113)
- Inputs: parameters `run_model(meta_model, datum, prefix_messages, task_description, meta_model_settings, question_prefix, question_suffix, expert_prompting)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L189: `{'input': input, 'target': target, 'message_log': message_log, 'output': output}`
- Decisions / conditions:
  - L133: IF `expert_prompting`; body=4 else=1
- LLM calls:
  - L172: `meta_model.meta_model_generate`
  - L142: `meta_model.generate`
- Main call graph hints: `print`, `prefix_messages.copy`, `meta_model.meta_model_generate`, `meta_model.generate`, `messages.append`
#### `main(args)` (L197)
- Inputs: parameters `main(args)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L359: {'line': 359, 'type': 'for', 'target': 'i', 'iter': 'range(0, min(len(data), args.max_num), BATCHES)', 'body_len': 3, 'orelse_len': 0}
  - L380: {'line': 380, 'type': 'for', 'target': 'output', 'iter': 'outputs', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L215: IF `not args.output_path is None`; body=1 else=0
  - L221: IF `args.output_directory is None`; body=1 else=0
  - L225: IF `args.input_path is None`; body=1 else=0
  - L227: IF `args.output_path is None`; body=1 else=0
  - L230: IF `args.fresh_eyes`; body=1 else=0
  - L233: IF `args.question_prefix_or_path.endswith('.txt')`; body=1 else=0
  - L237: IF `args.question_suffix_or_path.endswith('.txt')`; body=1 else=0
- LLM calls:
  - L323: `OpenAI_LanguageModel`
- I/O calls:
  - L199: `open`
  - L201: `json.load`
  - L319: `open`
  - L351: `open`
  - L352: `f.write`
  - L385: `open`
  - L387: `f.write`
  - L234: `open`
  - L235: `f.read`
  - L238: `open`
  - L239: `f.read`
  - L320: `json.loads`
  - L379: `open`
  - L387: `json.dumps`
  - L320: `f.readlines`
  - L381: `f.write`
  - L381: `json.dumps`
- Main call graph hints: `args.question_prefix_or_path.endswith`, `args.question_suffix_or_path.endswith`, `os.makedirs`, `OpenAI_LanguageModel`, `MetaPromptingScaffolding`, `min`, `range`, `args.output_path.replace`, `open`, `json.load`, `DESCRIPTION_DICT.keys`, `args.output_path.endswith`, `os.path.dirname`, `f.write`, `Parallel`, `OUTPUTS.extend`, `f.read`, `json.loads`, `len`, `args.as_dict`, `json.dumps`, `f.readlines`, `delayed`

---

## File: `utils/__init__.py`

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

## File: `utils/execute_code.py`

**Lines:** 36  

### Imports
- `import os`
- `import tempfile`
- `from subprocess import Popen, PIPE, TimeoutExpired`

### Module-level assignments
- None

### Prompt-like assignments
- L17 `process`: `process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)`
- L24 `captured_output`: `captured_output = f"Error in execution: {error_output}"`

### Classes
- None

### Functions
#### `execute_code_with_timeout(code, timeout)` (L8)
- Inputs: parameters `execute_code_with_timeout(code, timeout)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L35: `captured_output`
- Decisions / conditions:
  - L22: IF `captured_output == ''`; body=1 else=0
  - L23: IF `error_output != ''`; body=1 else=1
- Exception handling:
  - L15: handlers=['TimeoutExpired'] final=1
- I/O calls:
  - L12: `temp_file.write`
  - L17: `Popen`
- Main call graph hints: `tempfile.NamedTemporaryFile`, `temp_file.write`, `temp_file.flush`, `Popen`, `process.communicate`, `stdout.decode.strip`, `stderr.decode.strip`, `os.remove`, `process.kill`, `stdout.decode`, `stderr.decode`

---

## File: `utils/expert_prompting.py`

**Lines:** 35  

### Imports
- `from typing import Any, Dict, List, Optional, Union`
- `from .meta_scaffolding import MetaPromptingScaffolding`

### Module-level assignments
- None

### Prompt-like assignments
- L24 `meta_model_output`: `meta_model_output = self.language_model.generate( prompt_or_messages=prompt_or_messages, stop_tokens=stop_tokens, max_tokens=max_tokens, num_return_sequences=num_return_sequences, temperature=temperature, top_p=top_p, **kwargs, )[0]`

### Classes
#### Class `ExpertPrompting` L6 bases=['MetaPromptingScaffolding']
##### `__init__(self, *args, **kwargs)` (L7)
- Inputs: parameters `__init__(self, *args, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `super`
##### `generate_expert_identity(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, **kwargs)` (L11)
- Docstring: Create the identity and description of the expert.
- Inputs: parameters `generate_expert_identity(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L34: `meta_model_output`
- LLM calls:
  - L24: `self.language_model.generate`
- Main call graph hints: `self.language_model.generate`

### Functions
- None

---

## File: `utils/language_model.py`

**Lines:** 224  

### Imports
- `import os`
- `import openai`
- `from openai import OpenAI`
- `from typing import Any, Dict, List, Optional, Union`
- `import retry`

### Module-level assignments
- None

### Prompt-like assignments
- L213 `response`: `response = self.client.chat.completions.create( model=self.model_name, messages=prompt_or_messages, max_tokens=max_tokens, temperature=temperature, top_p=top_p, n=num_return_sequences, stop=stop_tokens, **kwargs, )`
- L185 `response`: `response = openai.ChatCompletion.create( engine=self.model_name, messages=prompt_or_messages, max_tokens=max_tokens, temperature=temperature, top_p=top_p, n=num_return_sequences, stop=stop_tokens, **kwargs, )`
- L198 `response`: `response = openai.Completion.create( engine=self.model_name, prompt=prompt_or_messages, max_tokens=max_tokens, temperature=temperature, top_p=top_p, n=num_return_sequences, stop=stop_tokens, **kwargs, )`

### Classes
#### Class `LanguageModel` L9 bases=[]
- Docstring: Abstract class for a language model.
##### `__init__(self, model_name, stop_tokens, **kwargs)` (L12)
- Inputs: parameters `__init__(self, model_name, stop_tokens, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `generate(self, prompt, max_length, num_return_sequences, **kwargs)` (L22)
- Docstring: Generate text based on a prompt.
- Inputs: parameters `generate(self, prompt, max_length, num_return_sequences, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `NotImplementedError`
##### `get_model_name(self)` (L32)
- Docstring: Get the name of the model.
- Inputs: parameters `get_model_name(self)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L34: `self.model_name`
##### `get_stop_tokens(self)` (L36)
- Docstring: Get the stop tokens.
- Inputs: parameters `get_stop_tokens(self)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L38: `self.stop_tokens`
##### `get_kwargs(self)` (L40)
- Docstring: Get the kwargs.
- Inputs: parameters `get_kwargs(self)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L42: `self.kwargs`
##### `set_kwargs(self, kwargs)` (L44)
- Docstring: Set the kwargs.
- Inputs: parameters `set_kwargs(self, kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
#### Class `DummyLanguageModel` L49 bases=['LanguageModel']
- Docstring: A dummy language model that just returns the prompt.
##### `__init__(self, model_name, stop_tokens, **kwargs)` (L52)
- Inputs: parameters `__init__(self, model_name, stop_tokens, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `super.__init__`, `super`
##### `generate(self, prompt, max_length, num_return_sequences, **kwargs)` (L60)
- Docstring: Generate text based on a prompt.
- Inputs: parameters `generate(self, prompt, max_length, num_return_sequences, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L68: `[prompt] * num_return_sequences`
#### Class `OpenAI_LanguageModel` L71 bases=['LanguageModel']
- Docstring: A language model from OpenAI's API.
##### `__init__(self, model_name, api_key, api_type, api_version, api_base, stop_tokens)` (L74)
- Docstring: Initialize the OpenAI API.

Args:
    model_name (str): The name of the model to use.
    api_key (str): The API key to use.
    api_type (str): The API type to use.
    api_version (str): The API version to use.
    api_base (str): The API base to use.
    stop_tokens (Optional[List[str]], optional): The stop tokens to use. Defaults to None.

Raises:
    ValueError: If the model name is not supported.

Returns:
    None
- Inputs: parameters `__init__(self, model_name, api_key, api_type, api_version, api_base, stop_tokens)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Decisions / conditions:
  - L115: IF `self.api_type == 'azure'`; body=5 else=1
  - L121: IF `self.model_name in ['code-davinci-002', 'text-davinci-002', 'text-davinci-003']`; body=1 else=1
  - L127: IF `self.model_name in ['gpt-4', 'gpt-4-32k', 'gpt-35-turbo', 'gpt-4-0314', 'gpt-4-32k-0314', 'gpt-35-turbo-0314', 'gpt-4-0613', 'gpt-4-32k-0613', 'gpt-35-turbo-0613', 'gpt-35-turbo']`; body=1 else=1
- LLM calls:
  - L146: `OpenAI`
- Main call graph hints: `OpenAI`, `ValueError`, `os.environ.get`
##### `generate(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, **kwargs)` (L151)
- Docstring: Generate text based on a prompt or messages.

Args:
    prompt_or_messages (Union[str, List[Dict[str, str]]]): The prompt or messages to generate text from.
    stop_tokens (Optional[List[str]], optional): The stop tokens to use. Defaults to None.
    max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 512.
    num_return_sequences (int, optional): The number of sequences to return. Defaults to 1.
    temperature (float, optional): The temperature to use. Defaults to 0.7.
    top_p (float, optional): The top p to use. Defaults to 1.0.
    **kwargs (Any): Additional keyword arguments.

Returns:
    List[str]: The list of generated texts based on the prompt or messages.
- Inputs: parameters `generate(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L223: `[output.message.content for output in response.choices]`
  - L196: `[message['message']['content'] for message in response.choices]`
  - L209: `[output['text'] for output in response.choices]`
- Decisions / conditions:
  - L181: IF `self.api_type == 'azure'`; body=1 else=2
  - L184: IF `self.model_type == 'chat'`; body=2 else=2
- LLM calls:
  - L213: `self.client.chat.completions.create`
  - L185: `openai.ChatCompletion.create`
  - L198: `openai.Completion.create`
- I/O calls:
  - L185: `openai.ChatCompletion.create`
  - L198: `openai.Completion.create`
- Main call graph hints: `retry.retry`, `print`, `self.client.chat.completions.create`, `openai.ChatCompletion.create`, `openai.Completion.create`

### Functions
- None

---

## File: `utils/meta_scaffolding.py`

**Lines:** 379  

### Imports
- `import random`
- `import re`
- `import time`
- `import retry`
- `from typing import Any, Dict, List, Optional, Tuple, Union`
- `from .language_model import OpenAI_LanguageModel`
- `from .execute_code import execute_code_with_timeout`

### Module-level assignments
- None

### Prompt-like assignments
- L42 `final_answer_indicator`: `self.final_answer_indicator = final_answer_indicator`
- L51 `include_expert_name_in_instruction`: `self.include_expert_name_in_instruction = include_expert_name_in_instruction`
- L55 `use_zero_shot_cot_in_expert_messages`: `self.use_zero_shot_cot_in_expert_messages = use_zero_shot_cot_in_expert_messages`
- L368 `model_output`: `model_output = self.language_model.generate( prompt_or_messages=prompt_or_messages, stop_tokens=stop_tokens, max_tokens=max_tokens, num_return_sequences=num_return_sequences, temperature=temperature, top_p=top_p, **kwargs, )[0]`
- L86 ``: `entire_message_log[-1][ "content" ] = f"ROUND {counter+1}:\n\n{entire_message_log[-1]['content']}"`
- L98 `meta_model_output`: `meta_model_output = self.language_model.generate( prompt_or_messages=entire_message_log, stop_tokens=stop_tokens, max_tokens=max_tokens, num_return_sequences=num_return_sequences, temperature=temperature, top_p=top_p, **kwargs, )[0]`
- L124 `triple_quote_splits`: `triple_quote_splits = meta_model_output.split(self.triple_quotes)`
- L282 `intermediate_output`: `intermediate_output = ( f"{intermediate_output}\n\n{self.intermediate_feedback}" )`
- L133 `line_preceding_instruction`: `line_preceding_instruction = triple_quote_splits[i - 1].strip()`
- L134 `model_name`: `model_name = line_preceding_instruction.split("\n")[-1].strip()`
- L163 `model_message_list`: `model_message_list = self.generator_settings["message-list"]`
- L166 `current_model_message_list`: `current_model_message_list = model_message_list.copy()`
- L180 `model_outputs`: `model_outputs = self.language_model.generate( prompt_or_messages=current_model_message_list, stop_tokens=model_stop_tokens, max_tokens=model_max_tokens, num_return_sequences=model_num_return_sequences, temperature=model_temp, top_p=model_top_p, **kwargs, )`
- L143 `model_instruction`: `model_instruction = ( f"You are {model_name}.\n\n{model_instruction}" )`
- L175 ``: `current_model_message_list[-1][ "content" ] = f"{self.expert_python_message}.\n\n{current_model_message_list[-1]['content']}"`
- L249 `summarizer_prompt_or_messages`: `summarizer_prompt_or_messages = ( self.summarizer_settings["message-list"].copy() )`
- L260 `summarizer_output`: `summarizer_output = self.language_model.generate( prompt_or_messages=summarizer_prompt_or_messages, stop_tokens=None, # FIXME(msuzgun) max_tokens=self.summarizer_settings["parameters"][ "max_tokens" ], num_return_sequences=self.summarizer_settings[ "parameters" ]["num_return_sequences"], temperat...`
- L200 `code_text`: `code_text = code_text.replace( "```python", "```" )`
- L215 `python_output`: `python_output = execute_code_with_timeout( code_text )`

### Classes
#### Class `MetaPromptingScaffolding` L16 bases=[]
##### `__init__(self, language_model, generator_settings, verifier_settings, summarizer_settings, error_message, final_answer_indicator, expert_python_message, intermediate_feedback, fresh_eyes, include_expert_name_in_instruction, extract_output, use_zero_shot_cot_in_expert_messages)` (L17)
- Inputs: parameters `__init__(self, language_model, generator_settings, verifier_settings, summarizer_settings, error_message, final_answer_indicator, expert_python_message, intermediate_feedback, fresh_eyes, include_expert_name_in_instruction, extract_output, use_zero_shot_cot_in_expert_messages)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
##### `meta_model_generate(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, counter, last_answer, original_question, trial_num, **kwargs)` (L58)
- Inputs: parameters `meta_model_generate(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, counter, last_answer, original_question, trial_num, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L79: `prompt_or_messages`
  - L344: `self.meta_model_generate(prompt_or_messages=entire_message_log, stop_tokens=stop_tokens, max_tokens=max_tokens, num_return_sequences=num_return_sequences, temperature=temperature, top_p=top_p, counter=counter, last_answer=last_answer, trial_num=trial_num + 1, **kwargs)`
  - L295: `self.meta_model_generate(prompt_or_messages=entire_message_log, stop_tokens=stop_tokens, max_tokens=max_tokens, num_return_sequences=num_return_sequences, temperature=temperature, top_p=top_p, counter=counter + 1, last_answer=last_answer, original_question=original_question, **kwargs)`
  - L339: `prompt_or_messages`
  - L315: `entire_message_log`
  - L321: `self.meta_model_generate(prompt_or_messages=entire_message_log, stop_tokens=stop_tokens, max_tokens=max_tokens, num_return_sequences=num_return_sequences, temperature=temperature, top_p=top_p, counter=counter + 1, last_answer=last_answer, original_question=original_question, **kwargs)`
- Loops:
  - L85: {'line': 85, 'type': 'while', 'test': 'True', 'body_len': 6, 'orelse_len': 0}
  - L131: {'line': 131, 'type': 'for', 'target': 'i', 'iter': 'range(1, len_triple_quote_splits, 2)', 'body_len': 3, 'orelse_len': 0}
  - L190: {'line': 190, 'type': 'for', 'target': '(_, model_output)', 'iter': 'enumerate(model_outputs)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L78: IF `counter == 16`; body=1 else=0
  - L90: IF `counter == 14`; body=1 else=0
  - L119: IF `self.fresh_eyes and re.search(pattern, meta_model_output)`; body=8 else=1
  - L338: IF `trial_num == 7`; body=1 else=0
  - L308: IF `self.final_answer_indicator in meta_model_output`; body=1 else=2
  - L135: IF `'Expert ' in model_name`; body=17 else=0
  - L136: IF `model_name[-1] == ':'`; body=1 else=0
  - L142: IF `self.include_expert_name_in_instruction`; body=1 else=0
  - L148: IF `self.use_zero_shot_cot_in_expert_messages`; body=1 else=0
  - L174: IF `model_name == 'Expert Python'`; body=1 else=0
  - L248: IF `model_num_return_sequences > 1`; body=4 else=0
  - L192: IF `model_name == 'Expert Python'`; body=1 else=2
  - L194: IF `'Please run this code!' in model_output`; body=6 else=0
  - L223: IF `self.extract_output`; body=2 else=2
  - L225: IF `specicial_token in model_output`; body=1 else=0
  - L230: IF `len(model_output.split(' ')) > 128`; body=1 else=0
- Exception handling:
  - L72: handlers=['Exception'] final=0
  - L203: handlers=['Exception'] final=0
- LLM calls:
  - L344: `self.meta_model_generate`
  - L98: `self.language_model.generate`
  - L295: `self.meta_model_generate`
  - L321: `self.meta_model_generate`
  - L180: `self.language_model.generate`
  - L260: `self.language_model.generate`
- Main call graph hints: `retry.retry`, `prompt_or_messages.copy`, `entire_message_log.append`, `print`, `time.sleep`, `self.meta_model_generate`, `self.language_model.generate`, `re.search`, `meta_model_output.split`, `len`, `range`, `random.randint`, `triple_quote_splits[...].strip`, `line_preceding_instruction.split[...].strip`, `model_message_list.copy`, `current_model_message_list.append`, `enumerate`, `intermediate_output.strip`, `self.summarizer_settings[...].copy`, `summarizer_prompt_or_messages.append`, `line_preceding_instruction.split`, `model_output.split[...].strip`, `code_text.replace`, `execute_code_with_timeout`, `model_output.replace`, `code_text.split[...].strip`, `model_output.split`, `code_text.split`
##### `generate(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, **kwargs)` (L358)
- Inputs: parameters `generate(self, prompt_or_messages, stop_tokens, max_tokens, num_return_sequences, temperature, top_p, **kwargs)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L378: `model_output`
- LLM calls:
  - L368: `self.language_model.generate`
- Main call graph hints: `retry.retry`, `self.language_model.generate`

### Functions
- None

---

## File: `utils/sonnet_eval.py`

**Lines:** 512  

### Imports
- `from typing import Set, Dict, Any`
- `import re`
- `import joblib`
- `import pyphen`
- `import syllables`
- `import pronouncing`

### Module-level assignments
- L39: `ALLOWED_SYLLABLES = { 10, 11, }`
- L43: `NUM_REQUIRED_WORDS = 3`
- L45: `memory = joblib.Memory( ".cache", verbose=0 )`
- L278: `TESTS = [ ["In savannah where tall trees kiss the sky,", 10], ["A giraffe named Joe with love-stricken grace,", 10], ["Did find a turtle named Sarah nearby,", 10], ["Their eyes did meet, hearts raced in sweet embrace.", 10], ["Though nature's laws deemed their love quite absurd,", 10], ["Joe's neck would bend to whisper words of flame,", 10], ["And Sarah's shell would tremble at each word,", 10...`

### Prompt-like assignments
- L68 `errors`: `errors = scheme_errors(poem, scheme, verbose=verbose)`
- L356 `wnl`: `wnl = sum("line count" in e for e in errors.values()) / num_samples`
- L358 `mw`: `mw = sum(bool("missing words" in e) for e in errors.values()) / num_samples`
- L360 `bl`: `bl = sum(bool("syllable errors" in e) for e in errors.values()) / num_samples`
- L362 `rhyme_errors`: `rhyme_errors = ( sum(any(" " not in k for k in e) for e in errors.values()) / num_samples )`
- L365 `both`: `both = ( sum( (bool("syllable errors" in e) and any(" " not in k for k in e)) for e in errors.values() ) / num_samples )`
- L471 `aaa`: `aaa = sonnet_errors( """How do I love thee? Let me count the ways. I love thee to the depth and breadth and height My soul can reach, when feeling out of sight For the ends of being and ideal grace. I love thee to the level of every day’s Most quiet need, by sun and candle-light. I love thee free...`
- L493 `aaa`: `aaa = sonnet_errors( """How do I love thee? Let me count the ways (A) I love thee to the depth and breadth and height (B) My soul can reach, when feeling out of sight (B) For the ends of being and ideal grace (A) I love thee to the level of every day’s (A) Most quiet need, by sun and candle-light...`

### Classes
#### Class `SyllableCounters` L234 bases=[]
- Docstring: Simple class to count syllables in text.
##### `cmu_dict()` (L243)
- Inputs: parameters `cmu_dict()` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L246: `SyllableCounters._cmu_dict`
- Decisions / conditions:
  - L244: IF `not SyllableCounters._cmu_dict`; body=1 else=0
- Main call graph hints: `pronouncing.cmudict.dict`
##### `cmu(word)` (L248)
- Inputs: parameters `cmu(word)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L249: `{pronouncing.syllable_count(pro) for pro in pronouncing.phones_for_word(word)}`
- Main call graph hints: `pronouncing.syllable_count`, `pronouncing.phones_for_word`
##### `pyphen_counter()` (L254)
- Inputs: parameters `pyphen_counter()` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L257: `SyllableCounters._pyphen_counter`
- Decisions / conditions:
  - L255: IF `not SyllableCounters._pyphen_counter`; body=1 else=0
- Main call graph hints: `pyphen.Pyphen`
##### `count_word(word)` (L260)
- Inputs: parameters `count_word(word)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L275: `ans`
  - L262: `{0}`
- Decisions / conditions:
  - L261: IF `not word`; body=1 else=0
  - L272: IF `0 in ans and len(ans) > 1`; body=1 else=0
- Main call graph hints: `SyllableCounters.cmu`, `syllables.estimate`, `SyllableCounters.pyphen_counter.inserted.count`, `ans.remove`, `len`, `SyllableCounters.pyphen_counter.inserted`, `SyllableCounters.pyphen_counter`

### Functions
#### `sonnet_errors(poem, target, verbose)` (L50)
- Docstring: Checks for sonnet errors with respect to target rhyme scheme (and optional required words)

args:
    poem: the poem to check
    target: the rhyme scheme, e.g. "ABBA ABBA CDC DCD"
            optionally target can have a list of required words, like
            "ABBA ABBA CDC DCD, love train snail" each of these must be in the poem
    verbose: if True, print out more details
- Inputs: parameters `sonnet_errors(poem, target, verbose)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L82: `errors`
- Loops:
  - L75: {'line': 75, 'type': 'for', 'target': 'line', 'iter': 'split_poem(poem)', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L61: IF `', ' in target`; body=2 else=2
  - L71: IF `any(missing_words)`; body=1 else=0
  - L79: IF `syllable_errors`; body=1 else=0
  - L77: IF `not variations & ALLOWED_SYLLABLES`; body=1 else=0
- Main call graph hints: `scheme_errors`, `isinstance`, `any`, `split_poem`, `target.split`, `rest.split`, `syllable_variations`, `syllable_errors.append`, `w.lower`, `poem.lower`, `sorted`
#### `clean_word(text)` (L85)
- Inputs: parameters `clean_word(text)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L86: `text.lower().strip(',.!?;: "\'[]()/')`
- Main call graph hints: `text.lower.strip`, `text.lower`
#### `clean_line(line)` (L89)
- Docstring: Clean a line from a poem.
Check if line ends with (A) or (B) ... and remove it
- Inputs: parameters `clean_line(line)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L95: `line.strip()`
- Main call graph hints: `re.sub`, `line.strip`
#### `split_poem(poem, min_line_len)` (L98)
- Inputs: parameters `split_poem(poem, min_line_len)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L100: `[l for l in ans if len(l) > min_line_len]`
- Main call graph hints: `clean_line`, `poem.splitlines`, `len`
#### `slant_rhyming_parts(word)` (L104)
- Inputs: parameters `slant_rhyming_parts(word)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L115: `set(ans)`
- Main call graph hints: `set`, `Constant.join`, `pronouncing.phones_for_word`, `a.replace`, `all`, `a.endswith`, `pronouncing.rhyming_part.split`, `pronouncing.rhyming_part`
#### `get_rhymes(w)` (L119)
- Inputs: parameters `get_rhymes(w)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L120: `set(pronouncing.rhymes(w))`
- Main call graph hints: `set`, `pronouncing.rhymes`
#### `scheme_errors(poem, scheme, verbose)` (L123)
- Docstring: Find errors with respect to a given rhyming scheme
- Inputs: parameters `scheme_errors(poem, scheme, verbose)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L198: `{w: {'reason': error_reasons[w], 'internal': scores[w][0], 'external': scores[w][1]} for w in error_reasons}`
  - L129: `{'line count': f'Poem has {len(lines)} != {len(scheme)} lines in pattern {scheme}'}`
- Loops:
  - L138: {'line': 138, 'type': 'for', 'target': 'chars', 'iter': 'sorted(set(scheme))', 'body_len': 1, 'orelse_len': 0}
  - L150: {'line': 150, 'type': 'for', 'target': 'g', 'iter': 'groups', 'body_len': 4, 'orelse_len': 0}
  - L172: {'line': 172, 'type': 'for', 'target': 'w', 'iter': 'scores', 'body_len': 3, 'orelse_len': 0}
  - L155: {'line': 155, 'type': 'for', 'target': 'w', 'iter': 'g', 'body_len': 3, 'orelse_len': 0}
  - L158: {'line': 158, 'type': 'for', 'target': 'comparisons', 'iter': '[internal_words, external_words]', 'body_len': 3, 'orelse_len': 0}
  - L161: {'line': 161, 'type': 'for', 'target': 'v', 'iter': 'comparisons', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L128: IF `len(lines) != len(scheme)`; body=1 else=0
  - L147: IF `verbose`; body=1 else=0
  - L195: IF `len(error_reasons) + len(suspicious_reasons) >= 3`; body=1 else=0
  - L153: IF `len(internal_words) == 1`; body=1 else=0
  - L175: IF `internal['rhymes'] or internal['slant_rhymes']`; body=1 else=1
  - L192: IF `verbose`; body=1 else=0
  - L177: IF `len(external['rhymes']) >= 2`; body=1 else=1
  - L179: IF `external['rhymes']`; body=1 else=1
  - L162: IF `v == w`; body=1 else=0
  - L164: IF `v in rhymes`; body=1 else=1
  - L180: IF `len(external['slant_rhymes']) >= 2`; body=1 else=1
  - L188: IF `len(external['slant_rhymes']) >= 3`; body=1 else=0
  - L166: IF `slant_sets[v] & slant_sets[w]`; body=1 else=0
- Main call graph hints: `split_poem`, `scheme.replace`, `pronouncing.cmudict.dict`, `sorted`, `len`, `clean_word`, `set`, `groups.append`, `print`, `error_reasons.update`, `slant_rhyming_parts`, `get_rhymes`, `l.replace.split`, `dict`, `scores[...].append`, `zip`, `l.replace`, `m[...].append`
#### `syllable_variations(text, verbose)` (L208)
- Docstring: Given a text, return the set of possible numbers of syllables. It's a set because some words like "caramel" can
be pronounced with different numbers of syllables.
- Inputs: parameters `syllable_variations(text, verbose)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L223: `ans`
- Loops:
  - L214: {'line': 214, 'type': 'for', 'target': 'word', 'iter': "re.split('[ -]+', text)", 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L216: IF `not word`; body=1 else=0
- Main call graph hints: `re.split`, `clean_word`, `word_syllables`, `range`, `min`, `max`
#### `word_syllables(word)` (L227)
- Inputs: parameters `word_syllables(word)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L231: `SyllableCounters.count_word(word)`
- Main call graph hints: `SyllableCounters.count_word`, `clean_word`
#### `fixed_tests()` (L321)
- Inputs: parameters `fixed_tests()` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns:
  - L349: `failures`
- Loops:
  - L323: {'line': 323, 'type': 'for', 'target': '(line, expected)', 'iter': 'TESTS', 'body_len': 2, 'orelse_len': 0}
  - L330: {'line': 330, 'type': 'for', 'target': '(words, expected)', 'iter': "[('fire tire hour liar buyer flower drawer layer loyal royal file orange poem crayon'.split(), [1, 2]), ('caramel mayonnaise family chocolate camera different separate favorite realtor'.split(), [2, 3]), ('mischievous'.split(), [3, 4])]", 'body_len': 1, 'orelse_len': 0}
  - L341: {'line': 341, 'type': 'for', 'target': 'w', 'iter': 'words', 'body_len': 2, 'orelse_len': 0}
  - L343: {'line': 343, 'type': 'for', 'target': 'i', 'iter': 'expected', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L325: IF `expected not in variations`; body=2 else=0
  - L344: IF `i not in variations`; body=2 else=0
- Main call graph hints: `syllable_variations`, `print`, `failures.append`, `Constant.split`
#### `summarize_errors(errors, num_samples)` (L352)
- Inputs: parameters `summarize_errors(errors, num_samples)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `print`, `sum`, `bool`, `any`, `len`, `errors.values`
#### `corpus_check_scheme(corpus_filename, scheme)` (L377)
- Inputs: parameters `corpus_check_scheme(corpus_filename, scheme)` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Loops:
  - L381: {'line': 381, 'type': 'for', 'target': 'p', 'iter': 'poems', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L383: IF `e`; body=8 else=0
- I/O calls:
  - L378: `open`
  - L379: `f.read.split`
  - L379: `f.read`
- Main call graph hints: `summarize_errors`, `open`, `sonnet_errors`, `len`, `p.strip`, `print`, `f.read.split`, `f.read`
#### `test()` (L396)
- Inputs: parameters `test()` plus CLI/config/prompt/data/model state as referenced.
- Outputs / returns: implicit None unless side effects.
- Main call graph hints: `sonnet_errors`, `print`