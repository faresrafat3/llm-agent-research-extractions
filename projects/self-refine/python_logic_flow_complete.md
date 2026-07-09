# Self-Refine — Complete Logic / Flow / Loops / Conditions / I-O Extraction

Source repo: `https://github.com/madaan/self-refine`  
Audited commit: `9a206d41e5d2d0c241bb441f41eeadb945afaa55`

## Paper algorithm summary

Algorithm 1: require input `x`, model `M`, prompts `{p_gen, p_fb, p_refine}`, and `stop(.)`. Generate `y0 = M(p_gen || x)`. For iteration `t = 0,1,...`: generate `fb_t = M(p_fb || x || y_t)`. If `stop(fb_t,t)` then break; else generate `y_{t+1} = M(p_refine || x || y0 || fb0 || ... || y_t || fb_t)`. Return latest `y_t`.

## Implemented task families

- Acronym generation: init acronym → feedback scores → iterative acronym/title refinement; plus MCTS variant.
- CommonGen constrained generation: init sentence → concept/commonsense feedback → iterative sentence refinement until both feedback fields are `none` or max attempts.
- GSM math reasoning: init Python solution → feedback may include improved solution → stop if feedback says correct or max attempts.
- PIE code optimization: init optimized code → feedback → iterate variants with specific/generic/no feedback.
- Response generation: dialogue response generation with FED feedback and iterative improvement.
- Sentiment reversal: transfer review sentiment → measure sentiment → feedback → iterate until max attempts.
- Code readability: prompt templates and utilities for readability evaluation/improvement.

## Python files

- `src/acronym/__init__.py`
- `src/acronym/feedback.py`
- `src/acronym/run.py`
- `src/acronym/run_mcts.py`
- `src/acronym/task_init.py`
- `src/acronym/task_iterate.py`
- `src/commongen/__init__.py`
- `src/commongen/data.py`
- `src/commongen/eval.py`
- `src/commongen/feedback.py`
- `src/commongen/make_challenging.py`
- `src/commongen/run.py`
- `src/commongen/task_init.py`
- `src/commongen/task_iterate.py`
- `src/gsm/__init__.py`
- `src/gsm/feedback.py`
- `src/gsm/feedback_no_update.py`
- `src/gsm/gsm_selfref_eval.py`
- `src/gsm/run.py`
- `src/gsm/task_init.py`
- `src/pie/feedback.py`
- `src/pie/pie_eval.py`
- `src/pie/prep_for_pie_eval.py`
- `src/pie/run.py`
- `src/pie/task_init.py`
- `src/pie/task_iterate.py`
- `src/readability/__init__.py`
- `src/readability/count_comment.py`
- `src/readability/count_function.py`
- `src/readability/count_meaningful_var.py`
- `src/readability/prompts.py`
- `src/readability/readability.py`
- `src/readability/utils.py`
- `src/responsegen/__init__.py`
- `src/responsegen/feedback.py`
- `src/responsegen/run.py`
- `src/responsegen/task_init.py`
- `src/responsegen/task_iterate.py`
- `src/sentiment_reversal/feedback.py`
- `src/sentiment_reversal/gpt4_eval.py`
- `src/sentiment_reversal/measure.py`
- `src/sentiment_reversal/run.py`
- `src/sentiment_reversal/task_init.py`
- `src/sentiment_reversal/task_iterate.py`
- `src/utils.py`

---

## File: `src/acronym/__init__.py`

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

## File: `src/acronym/feedback.py`

**Lines:** 92  

### Imports
- `import pandas as pd`
- `from prompt_lib.backends import openai_api`
- `from src.utils import Prompt`

### Module-level assignments
- None

### Prompt-like assignments
- L87 `feedback`: `feedback = AcronymGenFeedback( engine="davinci-code-002", prompt_examples="data/prompt/acronym/feedback.jsonl", )`
- L20 `template`: `template = """Title: {title} Acronym: {answer} Scores: * Ease of pronunciation: {pronunciation_score} * Ease of spelling: {spelling_score} * Relation to title: {relation_score} * Positive connotation: {connotation_score} * Well-known: {well_known_score} * Total score: {total_score}"""`
- L50 `instruction`: `instruction = """We want to score each acronym on five qualities: i) ease of pronunciation, ii) ease of spelling, and iii) relation to the title, iv) positive connotation, v) well-known. Here are some examples of this scoring rubric: """`
- L55 `prompt`: `self.prompt = instruction + self.inter_example_sep.join(prompt)`
- L56 `prompt`: `self.prompt = self.inter_example_sep.join(prompt) + self.inter_example_sep`
- L59 `prompt`: `prompt = self.get_prompt_with_question(title=title, acronym=acronym)`
- L61 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=prompt, engine=self.engine, max_tokens=self.max_tokens, stop_token="###", temperature=0.7, )`
- L69 `generated_feedback`: `generated_feedback = openai_api.OpenaiAPIWrapper.get_first_response(output)`
- L70 `generated_feedback`: `generated_feedback = generated_feedback.split("Scores:")[1].strip()`
- L71 `generated_feedback`: `generated_feedback = generated_feedback.split("#")[0].strip()`
- L75 `question`: `question = self.make_query(title=title, acronym=acronym)`
- L79 `question`: `question = f"""Title: {title} Acronym: {acronym}"""`

### Top-level logic
- L86 If: `if __name__ == "__main__": feedback = AcronymGenFeedback( engine="davinci-code-002", prompt_examples="data/prompt/acronym/feedback.jsonl", ) print(feedback.prompt)`

### Classes
#### Class `AcronymGenFeedback` L7 bases=['Prompt']
##### `__init__(self, engine, prompt_examples, max_tokens)` (L8)
- Inputs: function parameters `__init__(self, engine, prompt_examples, max_tokens)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L19)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L36: {'line': 36, 'type': 'for', 'target': '(_, row)', 'iter': 'examples_df.iterrows()', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L34: `pd.read_json`
- Main call graph hints: `pd.read_json`, `examples_df.iterrows`, `prompt.append`, `self.inter_example_sep.join`, `template.format`
##### `__call__(self, title, acronym)` (L58)
- Inputs: function parameters `__call__(self, title, acronym)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L72: `generated_feedback`
- LLM/API calls:
  - L61: `openai_api.OpenaiAPIWrapper.call`
  - L69: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L61: `openai_api.OpenaiAPIWrapper.call`
  - L69: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.get_prompt_with_question`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `generated_feedback.split[...].strip`, `generated_feedback.split`
##### `get_prompt_with_question(self, title, acronym)` (L74)
- Inputs: function parameters `get_prompt_with_question(self, title, acronym)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L76: `f'{self.prompt}{question}'`
- Main call graph hints: `self.make_query`
##### `make_query(self, title, acronym)` (L78)
- Inputs: function parameters `make_query(self, title, acronym)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L82: `question`

### Functions
- None

---

## File: `src/acronym/run.py`

**Lines:** 115  

### Imports
- `import re`
- `import pandas as pd`
- `from src.acronym.task_init import AcronymGenTaskInit`
- `from src.acronym.task_iterate import AcronymGenTaskIterate`
- `from src.acronym.feedback import AcronymGenFeedback`
- `from src.utils import retry_parse_fail_prone_cmd`

### Module-level assignments
- L10: `CODEX = "code-davinci-002"`
- L11: `GPT3 = "text-davinci-003"`
- L12: `CHAT_GPT = "gpt-3.5-turbo"`
- L13: `GPT4 = "gpt-4"`
- L16: `ENGINE = CHAT_GPT`

### Prompt-like assignments
- L24 `task_init`: `task_init = AcronymGenTaskInit(engine=ENGINE, prompt_examples="data/prompt/acronym/init.jsonl")`
- L27 `task_feedback`: `task_feedback = AcronymGenFeedback(engine=ENGINE, prompt_examples="data/prompt/acronym/feedback.jsonl")`
- L30 `task_iterate`: `task_iterate = AcronymGenTaskIterate(engine=ENGINE, prompt_examples="data/prompt/acronym/feedback.jsonl")`
- L51 `scores`: `scores = task_feedback(title=title, acronym=acronym)`

### Top-level logic
- L98 If: `if __name__ == "__main__": import sys title = sys.argv[1] # Light Amplification by Stimulated Emission of Radiation if len(sys.argv) > 2: run_over_titles(titles_file=sys.argv[1], max_attempts=int(sys.argv[2]), outfile=sys.argv[3]) else: max_attempts = 5 all_acronyms_to_scores = iterative_acronym( title=title, max_attempts=max_attempts, ) res = [] for acronym, scores in all_acronyms_to_scores.items(): res.append(f"{acronym} [score: {scores['total_score']}] \n {scores['scores']}") print("\n ---...`

### Classes
- None

### Functions
#### `iterative_acronym(title, max_attempts)` (L19)
- Inputs: function parameters `iterative_acronym(title, max_attempts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L75: `all_acronyms_to_scores`
- Loops:
  - L42: {'line': 42, 'type': 'while', 'test': 'n_attempts < max_attempts', 'body_len': 9, 'orelse_len': 0}
- Decisions / conditions:
  - L44: IF `n_attempts == 0`; body=1 else=2
  - L64: IF `total_score >= 0`; body=2 else=1
- Main call graph hints: `AcronymGenTaskInit`, `AcronymGenFeedback`, `AcronymGenTaskIterate`, `print`, `dict`, `task_feedback`, `re.search.group`, `int`, `task_init`, `task_iterate`, `re.search`, `total_score.split[...].strip.split`, `total_score.split[...].strip`, `total_score.split`
#### `run_over_titles(titles_file, max_attempts, outfile)` (L78)
- Inputs: function parameters `run_over_titles(titles_file, max_attempts, outfile)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L88: `'\n ------ \n '.join(res)`
  - L84: `'FAILED'`
  - L90: `'FAILED'`
- Loops:
  - L86: {'line': 86, 'type': 'for', 'target': '(acronym, scores)', 'iter': 'results.items()', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L83: IF `results is None`; body=1 else=0
- Exception handling:
  - L81: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L93: `pd.read_csv`
  - L96: `data.to_json`
- Main call graph hints: `pd.read_csv`, `data[...].apply`, `data.to_json`, `iterative_acronym`, `results.items`, `Constant.join`, `res.append`

---

## File: `src/acronym/run_mcts.py`

**Lines:** 209  

### Imports
- `import re`
- `import math`
- `from src.acronym.task_init import AcronymGenTaskInit`
- `from src.acronym.task_iterate import AcronymGenTaskIterate`
- `from src.acronym.feedback import AcronymGenFeedback`
- `from src.utils import retry_parse_fail_prone_cmd`

### Module-level assignments
- L10: `CODEX = "code-davinci-002"`
- L11: `GPT3 = "text-davinci-003"`
- L12: `CHAT_GPT = "gpt-3.5-turbo"`
- L13: `GPT4 = "gpt-4"`
- L14: `ENGINE = CHAT_GPT`
- L16: `task_init = AcronymGenTaskInit(engine=ENGINE, prompt_examples="data/prompt/acronym/init.jsonl")`
- L19: `task_feedback = AcronymGenFeedback( engine=ENGINE, prompt_examples="data/prompt/acronym/feedback.jsonl" )`
- L24: `task_iterate = AcronymGenTaskIterate( engine=ENGINE, prompt_examples="data/prompt/acronym/feedback.jsonl" )`
- L154: `root_title = "Iterative Refinement with Self-Feedback"`
- L155: `root_acronym = task_init(title=root_title)`
- L156: `root_scores = task_feedback(title=root_title, acronym=root_acronym)`
- L157: `root_scores = parse_scores(root_scores)`
- L158: `root = TreeNode(root_title, root_acronym, scores=root_scores)`
- L166: `weights = { "Ease of pronunciation": 0.2, "Ease of spelling": 0.2, "Relation to title": 0.3, "Positive connotation": 0.2, "Well-known": 0.1, }`
- L174: `iterations = 4`
- L175: `expanded_nodes_cache = {root.acronym}`
- L194: `best_node = dfs(root, root)`
- L195: `best_acronym, best_score = best_node.acronym, best_node.scores["Total score"]`

### Prompt-like assignments
- L16 `task_init`: `task_init = AcronymGenTaskInit(engine=ENGINE, prompt_examples="data/prompt/acronym/init.jsonl")`
- L19 `task_feedback`: `task_feedback = AcronymGenFeedback( engine=ENGINE, prompt_examples="data/prompt/acronym/feedback.jsonl" )`
- L24 `task_iterate`: `task_iterate = AcronymGenTaskIterate( engine=ENGINE, prompt_examples="data/prompt/acronym/feedback.jsonl" )`
- L154 `root_title`: `root_title = "Iterative Refinement with Self-Feedback"`
- L156 `root_scores`: `root_scores = task_feedback(title=root_title, acronym=root_acronym)`
- L115 `scores`: `scores = task_feedback(title=node.title, acronym=node.acronym)`
- L146 `value`: `value = simulate(expanded_node, task_feedback)`

### Top-level logic
- L177 For: `for _ in range(iterations): mcts_iteration(root, weights, task_iterate, task_feedback, expanded_nodes_cache)`

### Classes
#### Class `TreeNode` L29 bases=[]
##### `__init__(self, title, acronym, scores, parent)` (L30)
- Inputs: function parameters `__init__(self, title, acronym, scores, parent)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `acronym.strip`
##### `__str__(self)` (L39)
- Inputs: function parameters `__str__(self)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L44: `res`
- Decisions / conditions:
  - L41: IF `children_str == ''`; body=1 else=0
- Main call graph hints: `Constant.join`, `str`

### Functions
#### `generate_initial_children(node, task_iterate, task_feedback, num_children)` (L48)
- Inputs: function parameters `generate_initial_children(node, task_iterate, task_feedback, num_children)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L49: {'line': 49, 'type': 'for', 'target': '_', 'iter': 'range(num_children)', 'body_len': 4, 'orelse_len': 0}
- Main call graph hints: `range`, `task_iterate`, `TreeNode`, `simulate`, `node.children.append`
#### `parse_scores(scores_output)` (L58)
- Inputs: function parameters `parse_scores(scores_output)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L67: `scores`
- Loops:
  - L62: {'line': 62, 'type': 'for', 'target': 'score_match', 'iter': 'scores_pattern.finditer(scores_output)', 'body_len': 3, 'orelse_len': 0}
- Main call graph hints: `re.compile`, `scores_pattern.finditer`, `score_match.groups`, `int`, `re.search.group`, `re.search`
#### `normalize_scores(scores)` (L70)
- Inputs: function parameters `normalize_scores(scores)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L75: `normalized_scores`
- Loops:
  - L72: {'line': 72, 'type': 'for', 'target': '(key, value)', 'iter': 'scores.items()', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L73: IF `key != 'Total score'`; body=1 else=0
- Main call graph hints: `scores.items`
#### `weighted_sum(normalized_scores, weights)` (L78)
- Inputs: function parameters `weighted_sum(normalized_scores, weights)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L79: `sum((normalized_scores[key] * weights[key] for key in normalized_scores))`
- Main call graph hints: `sum`
#### `select(node, weights, C)` (L82)
- Inputs: function parameters `select(node, weights, C)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L93: `select(node.children[max_index], weights, C)`
  - L84: `node`
- Decisions / conditions:
  - L83: IF `not node.children`; body=1 else=0
- Main call graph hints: `ucb1_values.index`, `select`, `max`, `weighted_sum`, `math.sqrt`, `normalize_scores`, `math.log`
#### `expand(node, task_iterate, expanded_nodes_cache)` (L97)
- Inputs: function parameters `expand(node, task_iterate, expanded_nodes_cache)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L110: `TreeNode(title=new_title, acronym=new_acronym, scores=None, parent=node)`
- Loops:
  - L100: {'line': 100, 'type': 'while', 'test': 'current is not None', 'body_len': 2, 'orelse_len': 0}
  - L106: {'line': 106, 'type': 'while', 'test': 'new_acronym in expanded_nodes_cache', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `task_iterate`, `expanded_nodes_cache.add`, `TreeNode`
#### `simulate(node, task_feedback)` (L114)
- Inputs: function parameters `simulate(node, task_feedback)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L118: `normalized_total_score`
- Main call graph hints: `task_feedback`, `parse_scores`
#### `backpropagate(node, value)` (L121)
- Inputs: function parameters `backpropagate(node, value)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Decisions / conditions:
  - L125: IF `node.parent is not None`; body=1 else=0
- Main call graph hints: `backpropagate`
#### `mcts_iteration(root, weights, task_iterate, task_feedback, expanded_nodes_cache)` (L129)
- Inputs: function parameters `mcts_iteration(root, weights, task_iterate, task_feedback, expanded_nodes_cache)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `print`, `select`, `expand`, `selected_node.children.append`, `simulate`, `backpropagate`
#### `dfs(node, best_node)` (L181)
- Inputs: function parameters `dfs(node, best_node)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L191: `best_node`
  - L184: `node`
  - L186: `best_node`
- Loops:
  - L188: {'line': 188, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L182: IF `not node.children`; body=1 else=0
  - L183: IF `node.scores['Total score'] > best_node.scores['Total score']`; body=1 else=1
- Main call graph hints: `dfs`
#### `print_tree(node, indent)` (L200)
- Inputs: function parameters `print_tree(node, indent)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L204: {'line': 204, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `print`, `print_tree`

---

## File: `src/acronym/task_init.py`

**Lines:** 59  

### Imports
- `import pandas as pd`
- `from src.utils import Prompt`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L54 `task_init`: `task_init = AcronymGenTaskInit(engine="code-davinci-002", prompt_examples="data/prompt/acronym/init.jsonl")`
- L19 `TEMPLATE`: `TEMPLATE = """Title: {title} Acronym: {answer}"""`
- L27 `prompt`: `self.prompt = self.inter_example_sep.join(prompt)`
- L28 `prompt`: `self.prompt = self.prompt + self.inter_example_sep`
- L31 `query`: `query = f"{self.prompt}{self.question_prefix}{title}{self.intra_example_sep}"`
- L37 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=300, stop_token="###", temperature=0.7, )`

### Top-level logic
- L58 If: `if __name__ == "__main__": test()`

### Classes
#### Class `AcronymGenTaskInit` L7 bases=['Prompt']
##### `__init__(self, prompt_examples, engine)` (L8)
- Inputs: function parameters `__init__(self, prompt_examples, engine)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L18)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L25: {'line': 25, 'type': 'for', 'target': '(_, row)', 'iter': 'examples_df.iterrows()', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L23: `pd.read_json`
- Main call graph hints: `pd.read_json`, `examples_df.iterrows`, `self.inter_example_sep.join`, `prompt.append`, `TEMPLATE.format`
##### `make_query(self, title)` (L30)
- Inputs: function parameters `make_query(self, title)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L32: `query`
##### `__call__(self, title)` (L34)
- Inputs: function parameters `__call__(self, title)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L50: `generated_acronym.strip()`
- LLM/API calls:
  - L37: `openai_api.OpenaiAPIWrapper.call`
  - L45: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L37: `openai_api.OpenaiAPIWrapper.call`
  - L45: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `generated_acronym.split[...].replace.strip`, `generated_acronym.strip`, `generated_acronym.split[...].replace`, `generated_acronym.split`

### Functions
#### `test()` (L53)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `AcronymGenTaskInit`, `print`

---

## File: `src/acronym/task_iterate.py`

**Lines:** 143  

### Imports
- `import sys`
- `from typing import Dict, List`
- `from src.utils import Prompt`
- `import pandas as pd`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L142 `obj`: `obj = AcronymGenTaskIterate(prompt_examples="data/prompt/acronym/feedback.jsonl", engine="whatever")`
- L19 `prompt`: `self.prompt = self.make_prompt(prompt_examples=prompt_examples)`
- L23 `prompt_examples`: `prompt_examples = pd.read_json(prompt_examples, orient="records", lines=True)`
- L25 `grouped`: `grouped = prompt_examples.groupby("example")`
- L44 `example_template`: `example_template = """Title: {title} Acronym: {acronym} Scores: * Ease of pronunciation: {pronunciation_score} * Ease of spelling: {spelling_score} * Relation to title: {relation_score} * Positive connotation: {connotation_score} * Well-known: {well_known_score} * Total score: {total_score} Okay,...`
- L79 `input_txt`: `input_txt = f"""Title: {title} Acronym: {acronym} Scores: {scores} Okay, let's use this feedback to improve the acronym. """`
- L105 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=transfer_query, engine=self.engine, max_tokens=300, stop_token=self.inter_example_sep, temperature=0.7, )`

### Top-level logic
- L141 If: `if __name__ == "__main__": obj = AcronymGenTaskIterate(prompt_examples="data/prompt/acronym/feedback.jsonl", engine="whatever") print(obj.prompt)`

### Classes
#### Class `AcronymGenTaskIterate` L9 bases=['Prompt']
##### `__init__(self, engine, prompt_examples)` (L10)
- Inputs: function parameters `__init__(self, engine, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.make_prompt`, `super`
##### `make_prompt(self, prompt_examples)` (L21)
- Inputs: function parameters `make_prompt(self, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L34: `self.inter_example_sep.join(prompt) + self.inter_example_sep`
- Loops:
  - L29: {'line': 29, 'type': 'for', 'target': '(_, group)', 'iter': 'grouped', 'body_len': 3, 'orelse_len': 0}
- I/O calls:
  - L23: `pd.read_json`
- Main call graph hints: `pd.read_json`, `prompt_examples.groupby`, `group[...].apply`, `group.sort_values`, `prompt.append`, `self.inter_example_sep.join`, `self.make_one_iterate_example`, `int`, `group.to_dict`, `x.split[...].strip`, `x.split`
##### `make_one_iterate_example(self, incrementally_improving_examples)` (L37)
- Docstring: Given a list of examples that are incrementally improving, return a new example.
        
- Inputs: function parameters `make_one_iterate_example(self, incrementally_improving_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L67: `prompt.strip()`
- Loops:
  - L62: {'line': 62, 'type': 'for', 'target': 'example', 'iter': 'incrementally_improving_examples', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `Constant.join`, `prompt.strip`, `prompt.append`, `example_template.format`
##### `make_query(self, question)` (L69)
- Inputs: function parameters `make_query(self, question)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L70: `f'{self.prompt}{self.question_prefix}{question}{self.intra_example_sep}{self.answer_prefix}'`
##### `_make_input(self, title, acronym, scores)` (L73)
- Inputs: function parameters `_make_input(self, title, acronym, scores)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L91: `input_txt`
##### `__call__(self, acronyms_to_scores)` (L93)
- Inputs: function parameters `__call__(self, acronyms_to_scores)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L121: `(new_title, acronym.strip())`
- LLM/API calls:
  - L105: `openai_api.OpenaiAPIWrapper.call`
  - L112: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L105: `openai_api.OpenaiAPIWrapper.call`
  - L112: `openai_api.OpenaiAPIWrapper.get_first_response`
  - L102: `open`
  - L103: `f.write`
- Main call graph hints: `self.make_input`, `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `response.split[...].strip.split[...].strip`, `open`, `f.write`, `acronym.strip`, `response.split[...].strip.split`, `response.split[...].strip`, `response.split`
##### `make_input(self, acronyms_to_scores)` (L123)
- Inputs: function parameters `make_input(self, acronyms_to_scores)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L134: `input_txt`
- Loops:
  - L128: {'line': 128, 'type': 'for', 'target': '(acronym, (title, scores))', 'iter': 'acronyms_to_scores.items()', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `acronyms_to_scores.items`, `self._make_input`

### Functions
- None

---

## File: `src/commongen/__init__.py`

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

## File: `src/commongen/data.py`

**Lines:** 288  

### Imports
- `import re`
- `import pandas as pd`

### Module-level assignments
- None

### Prompt-like assignments
- L3 `prompt`: `prompt: str = """Title: A Survey of Active Network Research Acronym: SONAR ### Title: A Scalable, Commutative Replica Dictatorship for Practical Optimistic Replication Acronym: SCRATCHPAD ### Title: Blockchain: A Peer-to-Peer Electronic Cash System Acronym: BTC ### Title: A Taxonomy of DDoS Attac...`
- L76 `examples`: `examples = re.split(r"\n###\s*\n", prompt)`
- L94 `prompt`: `prompt: str = """We want to score each acronym on five qualities: i) ease of pronunciation, ii) ease of spelling, and iii) relation to the title, iv) positive connotation, v) well-known. Here are some examples of this scoring rubric: Title: "The Effect of the Internet on the Quality of Life of th...`

### Top-level logic
- L286 If: `if __name__ == "__main__": acronym_init_prompts_to_tsv() acronym_iterate_prompt_to_tsv()`

### Classes
#### Class `AcronymInitPrompts` L1 bases=[]
#### Class `AcronymFeedbackPrompt` L93 bases=[]

### Functions
#### `acronym_init_prompts_to_tsv()` (L73)
- Inputs: function parameters `acronym_init_prompts_to_tsv()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L78: {'line': 78, 'type': 'for', 'target': 'example', 'iter': 'examples', 'body_len': 1, 'orelse_len': 0}
- Exception handling:
  - L79: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L89: `df.to_json`
- Main call graph hints: `re.split`, `pd.DataFrame`, `df.to_json`, `re.sub`, `res.append`, `title.strip`, `acronym.strip`
#### `acronym_iterate_prompt_to_tsv()` (L245)
- Inputs: function parameters `acronym_iterate_prompt_to_tsv()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L253: {'line': 253, 'type': 'for', 'target': 'example', 'iter': 'examples', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L255: IF `not example`; body=1 else=0
- Exception handling:
  - L254: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L284: `df.to_json`
- Main call graph hints: `prompt.split`, `pd.DataFrame`, `print`, `df.to_json`, `example.strip`, `re.search.group`, `res.append`, `re.search`, `title.replace`, `acronym.replace`, `ease_of_pronunciation.replace`, `ease_of_spelling.replace`, `relation_to_title.replace`, `positive_connotation.replace`, `well_known.replace`, `total_score.replace`

---

## File: `src/commongen/eval.py`

**Lines:** 49  

### Imports
- `import pandas as pd`
- `from typing import List, Dict`

### Module-level assignments
- None

### Prompt-like assignments
- L12 ``: `df.loc[i, 'direct_concept_success'] = direct_output["concept_feedback"][0].lower() == "none"`
- L13 ``: `df.loc[i, 'direct_commonsense_success'] = direct_output["commonsense_feedback"].lower() == "none"`
- L14 ``: `df.loc[i, 'direct_success'] = direct_output["concept_feedback"][0].lower() == "none" and direct_output["commonsense_feedback"].lower() == "none"`
- L15 ``: `df.loc[i, 'iter_concept_success'] = iter_output["concept_feedback"][0].lower() == "none"`
- L16 ``: `df.loc[i, 'iter_commonsense_success'] = iter_output["commonsense_feedback"].lower() == "none"`
- L17 ``: `df.loc[i, 'iter_success'] = iter_output["concept_feedback"][0].lower() == "none" and iter_output["commonsense_feedback"].lower() == "none"`

### Top-level logic
- L41 If: `if __name__ == '__main__': import argparse args = argparse.ArgumentParser() args.add_argument("path", type=str) args = args.parse_args() run(path=args.path)`

### Classes
- None

### Functions
#### `run(path)` (L4)
- Inputs: function parameters `run(path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L9: {'line': 9, 'type': 'for', 'target': '(i, row)', 'iter': 'df.iterrows()', 'body_len': 8, 'orelse_len': 0}
- I/O calls:
  - L6: `pd.read_json`
- Main call graph hints: `pd.read_json`, `print`, `df.iterrows`, `len`, `direct_output[...][...].lower`, `direct_output[...].lower`, `iter_output[...][...].lower`, `iter_output[...].lower`

---

## File: `src/commongen/feedback.py`

**Lines:** 109  

### Imports
- `import re`
- `from typing import Set, List`
- `import pandas as pd`
- `from prompt_lib.backends import openai_api`
- `import nltk`
- `import spacy`
- `from src.utils import Prompt`

### Module-level assignments
- L8: `nlp = spacy.load("en_core_web_sm")`

### Prompt-like assignments
- L102 `task_feedback`: `task_feedback = CommongenFeedback( prompt_examples="data/prompt/commongen/feedback.v1.jsonl", engine="davinci-code-002" )`
- L25 `template`: `template = """Concepts: {concepts} Sentence: {sentence} what concepts from the concept list are missing from the sentence and does the sentence make sense? Concept Feedback: {feedback} Commonsense Feedback: {commonsense_feedback}"""`
- L44 `instruction`: `instruction = """We want to create a sentence that contains all the specified concepts. Please provide feedback on the following sentences. The feedback indicates missing concepts."""`
- L45 `prompt`: `self.prompt = instruction + self.inter_example_sep.join(prompt)`
- L46 `prompt`: `self.prompt = self.inter_example_sep.join(prompt) + self.inter_example_sep`
- L49 `prompt`: `prompt = self.make_query(sentence=sentence, concepts=concepts)`
- L51 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=prompt, engine=self.engine, max_tokens=self.max_tokens, stop_token="###", temperature=0.7, )`
- L59 `generated_feedback`: `generated_feedback = openai_api.OpenaiAPIWrapper.get_first_response(output)`
- L60 `commonsense_feedback`: `commonsense_feedback = re.search(r"Commonsense Feedback: (.*)", generated_feedback).group(1)`
- L61 `commonsense_feedback`: `commonsense_feedback = self.fix_feedback(sentence=sentence, concepts=concepts, feedback=commonsense_feedback)`
- L63 `concept_feedback`: `concept_feedback = re.search(r"Concept Feedback: (.*)", generated_feedback).group(1)`
- L68 `question`: `question = f"""Concepts: {concepts} Sentence: {sentence} what concepts from the concept list are missing from the sentence?"""`
- L78 `concepts_in_feedback`: `concepts_in_feedback = set([f.strip() for f in feedback.split(", ")])`
- L79 `fixed_feedback`: `fixed_feedback = concepts_in_feedback.difference(concepts_in_sent)`

### Top-level logic
- L101 If: `if __name__ == "__main__": task_feedback = CommongenFeedback( prompt_examples="data/prompt/commongen/feedback.v1.jsonl", engine="davinci-code-002" ) print(task_feedback.prompt)`

### Classes
#### Class `CommongenFeedback` L12 bases=['Prompt']
##### `__init__(self, engine, prompt_examples, max_tokens)` (L13)
- Inputs: function parameters `__init__(self, engine, prompt_examples, max_tokens)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L24)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L34: {'line': 34, 'type': 'for', 'target': '(_, row)', 'iter': 'examples_df.iterrows()', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L32: `pd.read_json`
- Main call graph hints: `pd.read_json`, `examples_df.iterrows`, `prompt.append`, `self.inter_example_sep.join`, `template.format`, `Constant.join`
##### `__call__(self, sentence, concepts)` (L48)
- Inputs: function parameters `__call__(self, sentence, concepts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L64: `(concept_feedback, commonsense_feedback)`
- LLM/API calls:
  - L51: `openai_api.OpenaiAPIWrapper.call`
  - L59: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L51: `openai_api.OpenaiAPIWrapper.call`
  - L59: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `re.search.group`, `self.fix_feedback`, `re.search`
##### `make_query(self, concepts, sentence)` (L67)
- Inputs: function parameters `make_query(self, concepts, sentence)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L71: `f'{self.prompt}{question}'`
##### `fix_feedback(self, sentence, concepts, feedback)` (L74)
- Docstring: We rely on the model for generating a feedback. This is done to capture different forms in which the same concept might be expressed. However, the model might make mistakes and our task is simple enough that some of the mistakes can be corrected
- Inputs: function parameters `fix_feedback(self, sentence, concepts, feedback)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L82: `', '.join(fixed_feedback)`
  - L81: `'None'`
- Decisions / conditions:
  - L80: IF `len(fixed_feedback) == 0`; body=1 else=0
- Main call graph hints: `self.detect_concepts`, `set`, `concepts_in_feedback.difference`, `Constant.join`, `len`, `f.strip`, `feedback.split`
##### `detect_concepts(self, sentence, concepts)` (L84)
- Inputs: function parameters `detect_concepts(self, sentence, concepts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L96: `set(present_concepts)`
- Loops:
  - L92: {'line': 92, 'type': 'for', 'target': 'concept', 'iter': 'concepts', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L93: IF `concept in tokens or concept in lemmas`; body=1 else=0
- Main call graph hints: `nltk.word_tokenize`, `set`, `nlp`, `present_concepts.append`

### Functions
- None

---

## File: `src/commongen/make_challenging.py`

**Lines:** 22  

### Imports
- `import pandas as pd`
- `from itertools import chain`
- `import random`

### Module-level assignments
- L3: `df = pd.read_json("/usr1/amadaan/shufflegen/data/original/commongen/val.jsonl", lines=True, orient="records")`
- L6: `all_concepts = set(chain(*df['concepts'].tolist()))`
- L13: `n_samples = 200`
- L14: `res = []`

### Prompt-like assignments
- None

### Top-level logic
- L15 For: `for i in range(n_samples): k = random.randint(20, 30) concepts = random.sample(all_concepts, k=k) res.append({"concepts": concepts})`

### Classes
- None

### Functions
- None

---

## File: `src/commongen/run.py`

**Lines:** 187  

### Imports
- `import pathlib`
- `from tqdm import tqdm`
- `from typing import List`
- `from src.commongen.task_init import CommongenTaskInit`
- `from src.commongen.task_iterate import CommongenTaskIterate`
- `from src.commongen.feedback import CommongenFeedback`
- `from src.utils import retry_parse_fail_prone_cmd`

### Module-level assignments
- L10: `CODEX = "code-davinci-002"`
- L11: `GPT3 = "text-davinci-003"`
- L12: `CHATGPT = "gpt-3.5-turbo"`
- L13: `ENGINE = GPT3`

### Prompt-like assignments
- L22 `task_init`: `task_init = CommongenTaskInit(engine=ENGINE, prompt_examples="data/prompt/commongen/init.jsonl")`
- L25 `task_feedback`: `task_feedback = CommongenFeedback( engine=ENGINE, prompt_examples="data/prompt/commongen/feedback.jsonl" )`
- L30 `task_iterate`: `task_iterate = CommongenTaskIterate( engine=ENGINE, prompt_examples="data/prompt/commongen/iterate.jsonl" )`
- L130 `task_init`: `task_init = CommongenTaskInit(engine=ENGINE, prompt_examples="data/prompt/commongen/init.jsonl")`
- L131 `task_feedback`: `task_feedback = CommongenFeedback( engine=ENGINE, prompt_examples="data/prompt/commongen/feedback.v1.jsonl" )`
- L51 ``: `concept_fb, commonsense_fb = task_feedback(concepts=concepts, sentence=sent)`
- L81 `fb`: `fb = "; ".join(s["concept_feedback"]) + " " + s["commonsense_feedback"]`
- L143 ``: `concept_fb, commonsense_fb = task_feedback(concepts=row["concepts"], sentence=sent)`

### Top-level logic
- L170 If: `if __name__ == "__main__": import sys import pandas as pd if sys.argv[1] == "cmd": run_cmd() elif sys.argv[1] == "batch-iter": run_iter(inputs_file_path=sys.argv[2]) elif sys.argv[1] == "batch-multi": run_multi_sample(inputs_file_path=sys.argv[2]) else: raise ValueError("Invalid mode: choose between cmd, batch-iter, batch-multi")`

### Classes
- None

### Functions
#### `autofb_commongen(concepts, max_attempts)` (L17)
- Inputs: function parameters `autofb_commongen(concepts, max_attempts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L67: `sent_to_fb`
- Loops:
  - L41: {'line': 41, 'type': 'while', 'test': 'n_attempts < max_attempts', 'body_len': 8, 'orelse_len': 0}
- Decisions / conditions:
  - L44: IF `n_attempts == 0`; body=1 else=1
  - L62: IF `concept_fb.lower() == 'none' and commonsense_fb.lower() == 'none'`; body=1 else=0
- Main call graph hints: `CommongenTaskInit`, `CommongenFeedback`, `CommongenTaskIterate`, `print`, `task_feedback`, `sent_to_fb.append`, `task_init`, `task_iterate`, `concept_fb.lower`, `commonsense_fb.lower`, `f.strip`, `concept_fb.split`
#### `run_cmd()` (L70)
- Inputs: function parameters `run_cmd()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L79: {'line': 79, 'type': 'for', 'target': 's', 'iter': 'sent_to_fb', 'body_len': 3, 'orelse_len': 0}
- Main call graph hints: `autofb_commongen`, `print`, `res.append`, `Constant.join`
#### `run_iter(inputs_file_path, max_attempts)` (L86)
- Inputs: function parameters `run_iter(inputs_file_path, max_attempts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L98: {'line': 98, 'type': 'for', 'target': '(i, row)', 'iter': "tqdm(test_df.iterrows(), total=len(test_df), desc='Running autofb iter')", 'body_len': 2, 'orelse_len': 0}
  - L111: {'line': 111, 'type': 'while', 'test': 'pathlib.Path(output_path).exists()', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L91: IF `not is_rerun`; body=3 else=2
  - L99: IF `row['status'] == 'success'`; body=1 else=0
- Exception handling:
  - L101: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L87: `pd.read_json`
  - L111: `pathlib.Path.exists`
  - L115: `test_df.to_json`
- Main call graph hints: `pd.read_json`, `tqdm`, `pathlib.Path.exists`, `test_df.to_json`, `test_df[...].astype`, `print`, `test_df.iterrows`, `test_df[...].value_counts`, `len`, `autofb_commongen`, `pathlib.Path`, `str`
#### `run_multi_sample(inputs_file_path, n_samples)` (L118)
- Inputs: function parameters `run_multi_sample(inputs_file_path, n_samples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L134: {'line': 134, 'type': 'for', 'target': '(i, row)', 'iter': "tqdm(test_df.iterrows(), total=len(test_df), desc='Running multisample autofb')", 'body_len': 2, 'orelse_len': 0}
  - L163: {'line': 163, 'type': 'while', 'test': 'pathlib.Path(output_path).exists()', 'body_len': 2, 'orelse_len': 0}
  - L140: {'line': 140, 'type': 'for', 'target': '_', 'iter': 'range(n_samples)', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L122: IF `not is_rerun`; body=3 else=2
  - L136: IF `row['status'] == 'success'`; body=1 else=0
  - L152: IF `concept_fb.lower() == 'none' and commonsense_fb.lower() == 'none'`; body=1 else=0
- Exception handling:
  - L138: handlers=['Exception'] finalbody_len=0
- Raises:
  - L157: `e`
- I/O calls:
  - L119: `pd.read_json`
  - L163: `pathlib.Path.exists`
  - L167: `test_df.to_json`
- Main call graph hints: `pd.read_json`, `CommongenTaskInit`, `CommongenFeedback`, `tqdm`, `print`, `pathlib.Path.exists`, `test_df.to_json`, `test_df[...].astype`, `test_df.iterrows`, `test_df[...].value_counts`, `len`, `range`, `pathlib.Path`, `task_init`, `task_feedback`, `outputs.append`, `str`, `concept_fb.lower`, `commonsense_fb.lower`, `f.strip`, `concept_fb.split`

---

## File: `src/commongen/task_init.py`

**Lines:** 62  

### Imports
- `from typing import List`
- `import pandas as pd`
- `from src.utils import Prompt`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L56 `task_init`: `task_init = CommongenTaskInit( prompt_examples="data/prompt/commongen/init.jsonl", engine="davinci-code-002" )`
- L20 `TEMPLATE`: `TEMPLATE = """Concepts: {concepts} Sentence: {sentence}"""`
- L28 `prompt`: `self.prompt = self.inter_example_sep.join(prompt)`
- L29 `prompt`: `self.prompt = self.prompt + self.inter_example_sep`
- L34 `query`: `query = f"{self.prompt}{query}{self.intra_example_sep}"`
- L40 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=300, stop_token="###", temperature=0.7, )`

### Top-level logic
- L55 If: `if __name__ == "__main__": task_init = CommongenTaskInit( prompt_examples="data/prompt/commongen/init.jsonl", engine="davinci-code-002" ) print(task_init.prompt)`

### Classes
#### Class `CommongenTaskInit` L8 bases=['Prompt']
##### `__init__(self, prompt_examples, engine)` (L9)
- Inputs: function parameters `__init__(self, prompt_examples, engine)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L19)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L26: {'line': 26, 'type': 'for', 'target': '(_, row)', 'iter': 'examples_df.iterrows()', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L24: `pd.read_json`
- Main call graph hints: `pd.read_json`, `examples_df.iterrows`, `self.inter_example_sep.join`, `prompt.append`, `TEMPLATE.format`
##### `make_query(self, concepts)` (L31)
- Inputs: function parameters `make_query(self, concepts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L35: `query`
##### `__call__(self, concepts)` (L37)
- Inputs: function parameters `__call__(self, concepts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L51: `generated_sent.strip()`
- LLM/API calls:
  - L40: `openai_api.OpenaiAPIWrapper.call`
  - L48: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L40: `openai_api.OpenaiAPIWrapper.call`
  - L48: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `print`, `generated_sent.split[...].replace.strip`, `generated_sent.strip`, `self.make_query`, `generated_sent.split[...].replace`, `generated_sent.split`

### Functions
- None

---

## File: `src/commongen/task_iterate.py`

**Lines:** 122  

### Imports
- `import re`
- `from typing import Dict, List`
- `from src.utils import Prompt`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- L7: `header = """Concepts: {concepts} """`
- L9: `example_template = """Sentence: {sentence} what concepts from the concept list are missing from the sentence? Concept Feedback: {concept_feedback} Any feedback on commonsense? Commonsense Feedback: {commonsense_feedback}"""`
- L19: `instr = """ Okay, impove the sentence using the feedback: """`

### Prompt-like assignments
- L9 `example_template`: `example_template = """Sentence: {sentence} what concepts from the concept list are missing from the sentence? Concept Feedback: {concept_feedback} Any feedback on commonsense? Commonsense Feedback: {commonsense_feedback}"""`
- L19 `instr`: `instr = """ Okay, impove the sentence using the feedback: """`
- L117 `obj`: `obj = CommongenTaskIterate( prompt_examples="data/prompt/commongen/iterate.v1.jsonl", engine="whatever" )`
- L35 `prompt`: `self.prompt = self.make_prompt(prompt_examples=prompt_examples)`
- L40 `prompt_examples`: `prompt_examples = pd.read_json(prompt_examples, orient="records", lines=True)`
- L82 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=transfer_query, engine=self.engine, max_tokens=300, stop_token=self.inter_example_sep, temperature=0.7, )`

### Top-level logic
- L116 If: `if __name__ == "__main__": obj = CommongenTaskIterate( prompt_examples="data/prompt/commongen/iterate.v1.jsonl", engine="whatever" ) print(obj.prompt)`

### Classes
#### Class `CommongenTaskIterate` L25 bases=['Prompt']
##### `__init__(self, engine, prompt_examples)` (L26)
- Inputs: function parameters `__init__(self, engine, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.make_prompt`, `super`
##### `make_prompt(self, prompt_examples)` (L37)
- Inputs: function parameters `make_prompt(self, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L51: `self.inter_example_sep.join(prompt) + self.inter_example_sep`
- Loops:
  - L44: {'line': 44, 'type': 'for', 'target': 'example', 'iter': "prompt_examples.to_dict(orient='records')", 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L40: `pd.read_json`
- Main call graph hints: `pd.read_json`, `prompt_examples.to_dict`, `prompt.append`, `self.inter_example_sep.join`, `self.make_one_iterate_example`
##### `make_one_iterate_example(self, concepts, sent_to_fb)` (L53)
- Docstring: Given a list of examples that are incrementally improving, return a new example.
- Inputs: function parameters `make_one_iterate_example(self, concepts, sent_to_fb)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L65: `header.format(concepts=concepts) + instr.join(single_example)`
- Loops:
  - L59: {'line': 59, 'type': 'for', 'target': 'example', 'iter': 'sent_to_fb', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `single_example.append`, `header.format`, `instr.join`, `example_template.format`
##### `make_query(self, concepts, sent_to_fb)` (L67)
- Inputs: function parameters `make_query(self, concepts, sent_to_fb)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L70: `f'{self.prompt}{self.question_prefix}{query_example}{self.intra_example_sep}{self.answer_prefix}' + instr`
- Main call graph hints: `self.make_one_iterate_example`
##### `__call__(self, concepts, sent_to_fb)` (L73)
- Inputs: function parameters `__call__(self, concepts, sent_to_fb)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L99: `response.strip()`
- LLM/API calls:
  - L82: `openai_api.OpenaiAPIWrapper.call`
  - L89: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L82: `openai_api.OpenaiAPIWrapper.call`
  - L89: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `print`, `re.search.group.strip.split[...].strip`, `response.strip`, `re.search.group.strip.split`, `re.search.group.strip`, `re.search.group`, `re.search`
##### `make_input(self, title, acronyms_to_scores)` (L101)
- Inputs: function parameters `make_input(self, title, acronyms_to_scores)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L113: `input_txt`
- Loops:
  - L107: {'line': 107, 'type': 'for', 'target': '(acronym, scores)', 'iter': 'acronyms_to_scores.items()', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `acronyms_to_scores.items`, `self._make_input`

### Functions
- None

---

## File: `src/gsm/__init__.py`

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

## File: `src/gsm/feedback.py`

**Lines:** 92  

### Imports
- `import pandas as pd`
- `from prompt_lib.backends import openai_api`
- `from src.utils import Prompt`

### Module-level assignments
- None

### Prompt-like assignments
- L70 `task_fb`: `task_fb = GSMFeedback( prompt_examples="data/prompt/gsm/pal/feedback.txt", engine="gpt-3.5-turbo", temperature=0.7, )`
- L84 `feedback_and_solution`: `feedback_and_solution = task_fb(wrong_soln)`
- L19 `instruction`: `self.instruction = "# There is an error in the code above because of lack of understanding of the question. What is the error? To find the error, go through semantically complete blocks of the code, and check if everything looks good." if "naive" not in prompt_examples else "# There is an error i...`
- L30 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=self.max_tokens, stop_token="### END", temperature=self.temperature, )`
- L45 `feedback`: `feedback = entire_output.split("def solution():")[0]`
- L57 `prefix`: `prefix = f"""{self.question_prefix}{solution}{self.intra_example_sep}{self.instruction}{self.answer_prefix}"""`
- L59 `gen_ans`: `gen_ans = f""" {feedback} {improved_soln.rstrip()}{self.inter_example_sep}"""`
- L66 `prompt`: `self.prompt = f"{self.prompt}{new_example}"`
- L42 `entire_output`: `entire_output = entire_output.split("### END")[0]`

### Top-level logic
- L91 If: `if __name__ == '__main__': test()`

### Classes
#### Class `GSMFeedback` L7 bases=['Prompt']
##### `__init__(self, engine, prompt_examples, temperature, max_tokens)` (L8)
- Inputs: function parameters `__init__(self, engine, prompt_examples, temperature, max_tokens)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L22)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- I/O calls:
  - L23: `open`
- Main call graph hints: `open`, `f.read`
##### `__call__(self, solution)` (L26)
- Inputs: function parameters `__call__(self, solution)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L48: `{'solution': improved_soln, 'feedback': feedback}`
- Decisions / conditions:
  - L41: IF `'### END' in entire_output`; body=1 else=0
- LLM/API calls:
  - L30: `openai_api.OpenaiAPIWrapper.call`
  - L39: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L30: `openai_api.OpenaiAPIWrapper.call`
  - L39: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `print`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `self.update_prompt`, `entire_output.split`, `improved_soln.rstrip`
##### `make_query(self, solution)` (L50)
- Inputs: function parameters `make_query(self, solution)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L53: `f'{self.prompt}{solution}'`
##### `update_prompt(self, solution, improved_soln, feedback)` (L56)
- Inputs: function parameters `update_prompt(self, solution, improved_soln, feedback)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `improved_soln.rstrip`

### Functions
#### `test()` (L69)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `GSMFeedback`, `task_fb`, `print`

---

## File: `src/gsm/feedback_no_update.py`

**Lines:** 70  

### Imports
- `import pandas as pd`
- `from prompt_lib.backends import openai_api`
- `from src.utils import Prompt`

### Module-level assignments
- None

### Prompt-like assignments
- L49 `task_fb`: `task_fb = GSMFeedback( prompt_examples="data/prompt/gsm/feedback.txt", engine="code-davinci-002", temperature=0.7, )`
- L63 `feedback_and_solution`: `feedback_and_solution = task_fb(wrong_soln)`
- L18 `instruction`: `self.instruction = "# There is an error in the code above because of lack of understanding of the question. What is the error? To find the error, go through semantically complete blocks of the code, and check if everything looks good."`
- L27 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=self.max_tokens, stop_token="### END", temperature=self.temperature, )`
- L39 `feedback`: `feedback = entire_output.split("def solution():")[0]`
- L37 `entire_output`: `entire_output = entire_output.split("### END")[0]`

### Top-level logic
- L68 If: `if __name__ == '__main__': test()`

### Classes
#### Class `GSMFeedback` L7 bases=['Prompt']
##### `__init__(self, engine, prompt_examples, temperature, max_tokens)` (L8)
- Inputs: function parameters `__init__(self, engine, prompt_examples, temperature, max_tokens)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L21)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- I/O calls:
  - L22: `open`
- Main call graph hints: `open`, `f.read`
##### `__call__(self, solution)` (L25)
- Inputs: function parameters `__call__(self, solution)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L41: `{'solution': solution, 'feedback': feedback}`
- Decisions / conditions:
  - L36: IF `'### END' in entire_output`; body=1 else=0
- LLM/API calls:
  - L27: `openai_api.OpenaiAPIWrapper.call`
  - L35: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L27: `openai_api.OpenaiAPIWrapper.call`
  - L35: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `entire_output.split`, `solution.rstrip`
##### `make_query(self, solution)` (L43)
- Inputs: function parameters `make_query(self, solution)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L45: `f'{self.prompt}{solution}'`

### Functions
#### `test()` (L48)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `GSMFeedback`, `task_fb`, `print`

---

## File: `src/gsm/gsm_selfref_eval.py`

**Lines:** 145  

### Imports
- `from importlib import reload`
- `import pandas as pd`
- `from tqdm import tqdm`
- `from contextlib import contextmanager`
- `import signal`
- `from glob import glob`
- `import os`

### Module-level assignments
- None

### Prompt-like assignments
- L55 `feedback`: `feedback = [rec["feedback"] for rec in row["run_logs"]]`
- L82 `report`: `report = { "previous_solution": solutions[iter_idx - 1], "feedback": feedback[iter_idx - 1], "next_solution": solutions[iter_idx], }`

### Top-level logic
- L137 If: `if __name__ == "__main__": import argparse parser = argparse.ArgumentParser() parser.add_argument("--path", type=str, default="data/quco/quco_test.jsonl") args = parser.parse_args() evaluate_code_prompt(args.path)`

### Classes
- None

### Functions
#### `timeout(duration)` (L11)
- Inputs: function parameters `timeout(duration)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Exception handling:
  - L17: handlers=[] finalbody_len=1
- Raises:
  - L13: `TimeoutError(f'block timedout after {duration} seconds')`
- Main call graph hints: `signal.signal`, `signal.alarm`, `TimeoutError`
#### `read_json(path)` (L22)
- Inputs: function parameters `read_json(path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L30: `task_df`
- Loops:
  - L26: {'line': 26, 'type': 'for', 'target': 'line', 'iter': 'f', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L25: `open`
  - L27: `json.loads`
- Main call graph hints: `pd.DataFrame`, `open`, `rows.append`, `json.loads`
#### `evaluate_code_prompt(path, num_gsm)` (L32)
- Inputs: function parameters `evaluate_code_prompt(path, num_gsm)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L109: `reports`
- Loops:
  - L41: {'line': 41, 'type': 'for', 'target': '(idx, row)', 'iter': 'tqdm(data.iterrows(), total=len(data))', 'body_len': 10, 'orelse_len': 0}
  - L102: {'line': 102, 'type': 'for', 'target': 'i', 'iter': 'range(5)', 'body_len': 1, 'orelse_len': 0}
  - L51: {'line': 51, 'type': 'for', 'target': '(_, log)', 'iter': "enumerate(row['run_logs'])", 'body_len': 1, 'orelse_len': 0}
  - L58: {'line': 58, 'type': 'for', 'target': '(iter_idx, soln)', 'iter': 'enumerate(solutions)', 'body_len': 6, 'orelse_len': 0}
  - L89: {'line': 89, 'type': 'for', 'target': 'j', 'iter': 'range(iter_idx, 5)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L34: IF `'question' not in data.columns`; body=1 else=0
  - L36: IF `'answer' not in data.columns`; body=1 else=0
  - L49: IF `row['run_logs'] is None`; body=1 else=0
  - L81: IF `iter_idx > 0 and is_corr == 1 and (prev_accuracy == 0)`; body=2 else=0
  - L88: IF `is_corr == 1`; body=2 else=0
- Exception handling:
  - L67: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L33: `read_json`
  - L105: `df.to_json`
  - L64: `open`
  - L65: `f.write`
- Main call graph hints: `read_json`, `tqdm`, `pd.DataFrame`, `range`, `df.to_json`, `print_reports`, `data.iterrows`, `enumerate`, `solutions.append`, `attempt_to_acc.append`, `print`, `len`, `os.system`, `soln.split[...].strip`, `soln.replace.strip`, `open`, `f.write`, `reload`, `str`, `exec`, `check_corr`, `int`, `timeout`, `reports.append`, `df[...].sum`, `soln.replace`, `temp_result.solution`, `soln.split`
#### `print_reports(reports, report_file)` (L112)
- Inputs: function parameters `print_reports(reports, report_file)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L116: {'line': 116, 'type': 'for', 'target': '(i, report)', 'iter': 'enumerate(reports)', 'body_len': 8, 'orelse_len': 0}
- I/O calls:
  - L115: `open`
  - L117: `f.write`
  - L118: `f.write`
  - L119: `f.write`
  - L120: `f.write`
  - L121: `f.write`
  - L122: `f.write`
  - L123: `f.write`
  - L124: `f.write`
- Main call graph hints: `open`, `enumerate`, `f.write`
#### `check_corr(result, correct_solution, tol)` (L125)
- Inputs: function parameters `check_corr(result, correct_solution, tol)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L127: `1`
  - L131: `abs(result - correct_solution) < tol`
  - L133: `0`
- Decisions / conditions:
  - L126: IF `result.strip() == correct_solution.strip()`; body=1 else=0
- Exception handling:
  - L128: handlers=['Exception'] finalbody_len=0
- Main call graph hints: `result.strip`, `correct_solution.strip`, `float`, `abs`

---

## File: `src/gsm/run.py`

**Lines:** 107  

### Imports
- `import pandas as pd`
- `from tqdm import tqdm`
- `from src.gsm.task_init import GSMInit`
- `from src.gsm.feedback import GSMFeedback`
- `from src.utils import retry_parse_fail_prone_cmd`

### Module-level assignments
- L10: `CODEX = "code-davinci-002"`
- L12: `ENGINE = CODEX`

### Prompt-like assignments
- L21 `task_init`: `task_init = GSMInit(engine=ENGINE, prompt_examples="data/prompt/gsm/init.txt", temperature=temperature)`
- L84 `logs`: `logs = fix_gsm( gsm_task_file="/tmp/debug_gsm.jsonl", max_attempts=3, outfile="/tmp/test.jsonl", feedback_type="rich", temperature=0.0 )`
- L27 `task_feedback`: `task_feedback = GSMFeedback(engine=ENGINE, prompt_examples="data/prompt/gsm/feedback.txt", temperature=0.7)`
- L39 `fb_and_maybe_soln`: `fb_and_maybe_soln = task_feedback(solution=solution)`
- L106 `outfile`: `args.outfile = f"{args.outfile}.fb_{args.feedback_type}.temp_{args.temperature}.engine_{ENGINE}.jsonl"`
- L63 `run_logs`: `run_logs = iterative_gsm(question=row["input"], max_attempts=max_attempts, feedback_type=feedback_type, temperature=temperature)`

### Top-level logic
- L92 If: `if __name__ == "__main__": import sys if sys.argv[1] == "test": test() else: import argparse args = argparse.ArgumentParser() args.add_argument("--gsm_task_file", type=str, default="data/tasks/gsm/gsm.jsonl") args.add_argument("--max_attempts", type=int, default=4) args.add_argument("--outfile", type=str, default="data/tasks/gsm/gsm_outputs.jsonl") args.add_argument("--feedback_type", type=str, default="rich") args.add_argument("--temperature", type=float, default=0.0) args = args.parse_args(...`

### Classes
- None

### Functions
#### `iterative_gsm(question, max_attempts, feedback_type, temperature)` (L16)
- Inputs: function parameters `iterative_gsm(question, max_attempts, feedback_type, temperature)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L51: `log`
- Loops:
  - L34: {'line': 34, 'type': 'while', 'test': 'n_attempts < max_attempts', 'body_len': 6, 'orelse_len': 0}
- Decisions / conditions:
  - L24: IF `feedback_type == 'naive'`; body=1 else=1
  - L36: IF `n_attempts == 0`; body=1 else=0
  - L44: IF `'it is correct' in fb_and_maybe_soln['feedback'].lower()`; body=1 else=0
- Raises:
  - L25: `NotImplementedError`
- Main call graph hints: `GSMInit`, `GSMFeedback`, `task_feedback`, `log.append`, `task_init`, `fb_and_maybe_soln[...].lower`
#### `fix_gsm(gsm_task_file, max_attempts, outfile, feedback_type, temperature)` (L54)
- Inputs: function parameters `fix_gsm(gsm_task_file, max_attempts, outfile, feedback_type, temperature)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L74: `results`
- Loops:
  - L60: {'line': 60, 'type': 'for', 'target': '(i, row)', 'iter': 'tqdm(slow_programs_df.iterrows(), total=len(slow_programs_df))', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L68: IF `i % 10 == 0`; body=1 else=0
- Exception handling:
  - L62: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L57: `pd.read_json`
  - L73: `pd.DataFrame.to_json`
  - L69: `pd.DataFrame.to_json`
- Main call graph hints: `pd.read_json`, `tqdm`, `pd.DataFrame.to_json`, `slow_programs_df.iterrows`, `row.to_dict`, `len`, `iterative_gsm`, `results.append`, `pd.DataFrame`
#### `test()` (L77)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L87: {'line': 87, 'type': 'for', 'target': '(i, log)', 'iter': 'enumerate(logs)', 'body_len': 2, 'orelse_len': 0}
- I/O calls:
  - L81: `open`
  - L82: `fout.write`
  - L82: `json.dumps`
- Main call graph hints: `fix_gsm`, `enumerate`, `open`, `fout.write`, `print`, `json.dumps`

---

## File: `src/gsm/task_init.py`

**Lines:** 55  

### Imports
- `import pandas as pd`
- `from src.utils import Prompt`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L44 `task_init`: `task_init = GSMInit( prompt_examples="data/prompt/gsm/init.txt", engine="code-davinci-002", temperature=0.0, )`
- L50 `question`: `question = "The educational shop is selling notebooks for $1.50 each and a ballpen at $0.5 each. William bought five notebooks and a ballpen. How much did he spend in all?"`
- L25 `query`: `query = f"{self.prompt}{self.question_prefix}{solution}{self.intra_example_sep}{self.answer_prefix}"`
- L30 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=300, stop_token=self.inter_example_sep, temperature=self.temperature, )`

### Top-level logic
- L54 If: `if __name__ == "__main__": test()`

### Classes
#### Class `GSMInit` L7 bases=['Prompt']
##### `__init__(self, prompt_examples, engine, temperature)` (L8)
- Inputs: function parameters `__init__(self, prompt_examples, engine, temperature)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, prompt_examples)` (L19)
- Inputs: function parameters `setup_prompt_from_examples_file(self, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- I/O calls:
  - L20: `open`
- Main call graph hints: `open`, `f.read`
##### `make_query(self, solution)` (L23)
- Inputs: function parameters `make_query(self, solution)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L26: `query`
- Main call graph hints: `solution.strip`
##### `__call__(self, solution)` (L28)
- Inputs: function parameters `__call__(self, solution)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L40: `solution_code.strip()`
- LLM/API calls:
  - L30: `openai_api.OpenaiAPIWrapper.call`
  - L38: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L30: `openai_api.OpenaiAPIWrapper.call`
  - L38: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `solution_code.strip`

### Functions
#### `test()` (L43)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `GSMInit`, `print`, `task_init`

---

## File: `src/pie/feedback.py`

**Lines:** 58  

### Imports
- `import pandas as pd`
- `from prompt_lib.backends import openai_api`
- `from src.utils import Prompt`

### Module-level assignments
- None

### Prompt-like assignments
- L46 `task_fb`: `task_fb = PieFeedback( prompt_examples="data/prompt/pie/feedback.txt", engine="gpt-3.5-turbo", temperature=0.0 )`
- L27 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=self.max_tokens, stop_token="### END", temperature=self.temperature, )`
- L35 `generated_feedback`: `generated_feedback = openai_api.OpenaiAPIWrapper.get_first_response(output)`
- L37 `generated_feedback`: `generated_feedback = generated_feedback.split("### END")[0]`

### Top-level logic
- L57 If: `if __name__ == '__main__': test()`

### Classes
#### Class `PieFeedback` L7 bases=['Prompt']
##### `__init__(self, engine, prompt_examples, temperature, max_tokens)` (L8)
- Inputs: function parameters `__init__(self, engine, prompt_examples, temperature, max_tokens)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L20)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- I/O calls:
  - L21: `open`
- Main call graph hints: `open`, `f.read`
##### `__call__(self, slow_code)` (L24)
- Inputs: function parameters `__call__(self, slow_code)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L38: `generated_feedback.strip()`
- Decisions / conditions:
  - L36: IF `'### END' in generated_feedback`; body=1 else=0
- LLM/API calls:
  - L27: `openai_api.OpenaiAPIWrapper.call`
  - L35: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L27: `openai_api.OpenaiAPIWrapper.call`
  - L35: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `generated_feedback.strip`, `generated_feedback.split`
##### `make_query(self, slow_code)` (L40)
- Inputs: function parameters `make_query(self, slow_code)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L42: `f'{self.prompt}{slow_code}'`

### Functions
#### `test()` (L45)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `PieFeedback`, `print`, `task_fb`

---

## File: `src/pie/pie_eval.py`

**Lines:** 359  

### Imports
- `import random`
- `import re`
- `import sys`
- `import numpy as np`
- `import pandas as pd`
- `import scipy.stats`
- `import logging`
- `import os`
- `import difflib`
- `from rpy2.robjects.packages import importr`
- `import rpy2.robjects as robjects`

### Module-level assignments
- L18: `base = importr('base')`
- L19: `stats = importr('stats')`
- L20: `r_ttest_offset = robjects.r("stats::t.test")`
- L65: `LARGE_NUMBER = 100000000`

### Prompt-like assignments
- None

### Top-level logic
- L336 If: `if __name__ == "__main__": import argparse args = argparse.ArgumentParser() args.add_argument("report_path", type=str, default="report.jsonl", nargs="?") args.add_argument("--lang", type=str, default="python") args.add_argument("--required_speedup", type=float, default=0.05) args = args.parse_args() reports = dict() for i in range(4): possible_report_path = f"{args.report_path}/output.pie.jsonl.{i}.report" # check if the file exists if os.path.exists(possible_report_path): reports[i] = summar...`

### Classes
- None

### Functions
#### `call_r_ttest_offset(slow_samples, fast_samples, offset_frac)` (L22)
- Inputs: function parameters `call_r_ttest_offset(slow_samples, fast_samples, offset_frac)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L30: `(results.rx2('p.value')[0], results.rx2('statistic')[0])`
- Decisions / conditions:
  - L23: IF `isinstance(slow_samples, list)`; body=1 else=0
  - L25: IF `isinstance(fast_samples, list)`; body=1 else=0
- Main call graph hints: `isinstance`, `r_ttest_offset`, `np.array`, `np.mean`, `robjects.FloatVector`, `results.rx2`
#### `cohen_d(slow, fast)` (L33)
- Inputs: function parameters `cohen_d(slow, fast)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L39: `(np.mean(slow) - np.mean(fast)) / np.sqrt(((nx - 1) * np.std(slow, ddof=1) ** 2 + (ny - 1) * np.std(fast, ddof=1) ** 2) / dof)`
- Main call graph hints: `len`, `np.sqrt`, `np.mean`, `np.std`
#### `get_r_ttest_p(row, generated_answer_field_tag, input_field_tag, required_speedup)` (L42)
- Inputs: function parameters `get_r_ttest_p(row, generated_answer_field_tag, input_field_tag, required_speedup)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L51: `p`
  - L48: `1.0`
- Decisions / conditions:
  - L47: IF `generated_times is None or input_times is None or len(generated_times) == 0 or (len(input_times) == 0)`; body=1 else=0
- LLM/API calls:
  - L50: `call_r_ttest_offset`
- Main call graph hints: `call_r_ttest_offset`, `len`
#### `get_cohens_d(row, generated_answer_field_tag, input_field_tag)` (L54)
- Inputs: function parameters `get_cohens_d(row, generated_answer_field_tag, input_field_tag)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L59: `cohen_d(input_times, generated_times)`
  - L58: `0.0`
- Decisions / conditions:
  - L57: IF `generated_times is None or input_times is None or len(generated_times) == 0 or (len(input_times) == 0)`; body=1 else=0
- Main call graph hints: `cohen_d`, `len`
#### `get_normalized_diff(code1, code2)` (L67)
- Inputs: function parameters `get_normalized_diff(code1, code2)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L80: `change_metric`
- Main call graph hints: `list`, `max`, `difflib.ndiff`, `len`, `code1.splitlines`, `code2.splitlines`, `line.startswith`
#### `get_minimal_diff(code1, code2, return_lines)` (L82)
- Inputs: function parameters `get_minimal_diff(code1, code2, return_lines)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L92: `'\n'.join(diff_minus_meta)`
  - L90: `diff_minus_meta`
- Decisions / conditions:
  - L89: IF `return_lines`; body=1 else=0
- Main call graph hints: `list`, `Constant.join`, `difflib.ndiff`, `code1.splitlines`, `code2.splitlines`, `line.startswith`
#### `get_input_based_diff(code1, code2)` (L94)
- Inputs: function parameters `get_input_based_diff(code1, code2)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L107: `change_metric`
- Main call graph hints: `list`, `len`, `difflib.ndiff`, `code1.splitlines`, `code2.splitlines`, `line.startswith`
#### `summarize(report_path, n_samples, lang, test_set_size, required_speedup, return_values, default_speedup)` (L109)
- Inputs: function parameters `summarize(report_path, n_samples, lang, test_set_size, required_speedup, return_values, default_speedup)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L258: `report_df[['problem_id', 'submission_id_v0', 'speedup', f'p_value_{required_speedup}pct']]`
  - L195: `'0, 1, 1, 1'`
  - L254: `(opt_pct, mean_speedup)`
- Loops:
  - L148: {'line': 148, 'type': 'for', 'target': 'time_col', 'iter': 'gen_time_cols', 'body_len': 4, 'orelse_len': 0}
- Decisions / conditions:
  - L125: IF `len(gen_time_cols) == 0`; body=1 else=0
  - L128: IF `n_samples == 1`; body=1 else=1
  - L194: IF `len(report_df) == 0`; body=1 else=0
  - L207: IF `len(report_df) == 0`; body=1 else=0
  - L248: IF `default_speedup`; body=3 else=0
  - L253: IF `return_values`; body=1 else=0
- I/O calls:
  - L118: `pd.read_json`
  - L244: `write_for_analysis`
- Main call graph hints: `pd.read_json`, `print`, `report_df[...].fillna`, `report_df[...].apply`, `report_df[...].min`, `report_df.apply`, `round`, `write_for_analysis`, `report_df[...].mean`, `len`, `c.replace`, `time_col.replace`, `np.mean`, `re.sub`, `get_minimal_diff`, `x.strip`, `get_r_ttest_p`, `os.path.basename`, `report_df[...].tolist`, `np.array`, `row[...].replace`, `Constant.join`, `range`, `d.strip`
#### `write_for_analysis(report_df, filename)` (L262)
- Inputs: function parameters `write_for_analysis(report_df, filename)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L270: `'\n'.join(diff_minus_meta)`
- Loops:
  - L274: {'line': 274, 'type': 'for', 'target': '(i, row)', 'iter': 'report_df.iterrows()', 'body_len': 9, 'orelse_len': 0}
- I/O calls:
  - L273: `open`
  - L275: `f.write`
  - L286: `f.write`
  - L287: `f.write`
  - L288: `f.write`
  - L291: `f.write`
  - L292: `f.write`
  - L293: `f.write`
  - L294: `f.write`
- Main call graph hints: `report_df.sort_values`, `list`, `Constant.join`, `open`, `report_df.iterrows`, `difflib.ndiff`, `f.write`, `code1.splitlines`, `code2.splitlines`, `line.startswith`, `_diff`
#### `get_welch_t_test_p(row, n_samples)` (L297)
- Inputs: function parameters `get_welch_t_test_p(row, n_samples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L308: `p_value`
- Main call graph hints: `scipy.stats.ttest_ind_from_stats`
#### `analyze_runs(report_df)` (L310)
- Inputs: function parameters `analyze_runs(report_df)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L334: `results_df`
- Loops:
  - L318: {'line': 318, 'type': 'for', 'target': 'run', 'iter': 'unique_runs', 'body_len': 4, 'orelse_len': 0}
- Main call graph hints: `report_df[...].unique`, `pd.DataFrame`, `problems_df.drop_duplicates`, `problems_df[...].mean`, `results.append`, `len`

---

## File: `src/pie/prep_for_pie_eval.py`

**Lines:** 52  

### Imports
- `import argparse`
- `import pandas as pd`

### Module-level assignments
- None

### Prompt-like assignments
- L15 `outputs`: `outputs = pd.read_json(self_refine_output_path, orient="records", lines=True)`

### Top-level logic
- L33 If: `if __name__ == "__main__": # Initialize argument parser. parser = argparse.ArgumentParser(description="Generate Yaml and Extract Codes") # Define expected arguments. parser.add_argument("model", type=str, help="Model name") parser.add_argument("input_file", type=str, help="Path to the input JSON file") parser.add_argument("base_config_path", type=str, help="Base path for config files") parser.add_argument("base_output_path", type=str, help="Base path for output files") parser.add_argument("--...`

### Classes
- None

### Functions
#### `extract_attempt_codes(self_refine_output_path, flattened_output_path, num_attempts)` (L6)
- Docstring: This function creates a file where each attempt/output at each step is stored in a new column: attempt_0_code, attempt_1_code, etc.

Args:
    input_file (_type_): _description_
    output_file (_type_): _description_
    num_attempts (_type_): _description_
- Inputs: function parameters `extract_attempt_codes(self_refine_output_path, flattened_output_path, num_attempts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L18: {'line': 18, 'type': 'for', 'target': '(_, row)', 'iter': 'outputs.iterrows()', 'body_len': 3, 'orelse_len': 0}
  - L22: {'line': 22, 'type': 'for', 'target': 'i', 'iter': 'range(num_attempts)', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L23: IF `len(row['run_logs']) <= i`; body=1 else=1
- I/O calls:
  - L15: `pd.read_json`
  - L30: `pd.DataFrame.to_json`
- Main call graph hints: `pd.read_json`, `outputs.iterrows`, `pd.DataFrame.to_json`, `row.to_dict`, `range`, `rows.append`, `pd.DataFrame`, `len`

---

## File: `src/pie/run.py`

**Lines:** 151  

### Imports
- `import pandas as pd`
- `from tqdm import tqdm`
- `from src.pie.task_init import PieInit`
- `from src.pie.task_iterate import PieIterate`
- `from src.pie.feedback import PieFeedback`
- `from src.utils import retry_parse_fail_prone_cmd`

### Module-level assignments
- L11: `CODEX = "code-davinci-002"`
- L12: `GPT3 = "text-davinci-003"`
- L13: `CHATGPT = "gpt-3.5-turbo"`
- L14: `GPT4 = "gpt-4"`
- L15: `ENGINE = CHATGPT`

### Prompt-like assignments
- L24 `task_init`: `task_init = PieInit(engine=ENGINE, prompt_examples="data/prompt/pie/init.txt", temperature=temperature)`
- L26 `iterate_prompt`: `iterate_prompt = "data/prompt/pie/iterate.txt"`
- L40 `task_iterate`: `task_iterate = PieIterate(engine=ENGINE, prompt_examples=iterate_prompt, temperature=temperature)`
- L29 `task_feedback`: `task_feedback = lambda **kwargs: "It could be faster"`
- L30 `iterate_prompt`: `iterate_prompt = "data/prompt/pie/iterate_genericfb.txt"`
- L57 `feedback`: `feedback = task_feedback(slow_code=fast_code)`
- L143 `outfile`: `args.outfile = f"{args.outfile}.fb_{args.feedback_type}.temp_{args.temperature}.engine_{ENGINE}.jsonl"`
- L34 `iterate_prompt`: `iterate_prompt = "data/prompt/pie/iterate_nofb.txt"`
- L37 `task_feedback`: `task_feedback = PieFeedback(engine=ENGINE, prompt_examples="data/prompt/pie/feedback.txt", temperature=temperature)`
- L54 `fast_code`: `fast_code = task_iterate(slow_code=slow_code, feedback=feedback)`
- L98 `run_logs`: `run_logs = iterative_pie(slow_code=row["input"], max_attempts=max_attempts, feedback_type=feedback_type, temperature=temperature)`

### Top-level logic
- L126 If: `if __name__ == "__main__": import sys if sys.argv[1] == "test": test() else: import argparse import os args = argparse.ArgumentParser() args.add_argument("--slow_programs_file", type=str, required=True) args.add_argument("--max_attempts", type=int, default=3) args.add_argument("--outfile", type=str, required=True) args.add_argument("--feedback_type", type=str) args.add_argument("--temperature", type=float, default=0.0) args.add_argument("--backup_file", type=str) args = args.parse_args() args...`

### Classes
- None

### Functions
#### `iterative_pie(slow_code, max_attempts, feedback_type, temperature)` (L19)
- Inputs: function parameters `iterative_pie(slow_code, max_attempts, feedback_type, temperature)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L69: `log`
- Loops:
  - L49: {'line': 49, 'type': 'while', 'test': 'n_attempts < max_attempts', 'body_len': 7, 'orelse_len': 0}
- Decisions / conditions:
  - L28: IF `feedback_type == 'naive'`; body=2 else=1
  - L32: IF `feedback_type == 'none'`; body=2 else=1
  - L51: IF `n_attempts == 0`; body=1 else=1
  - L62: IF `'this code is not slow' in feedback.lower()`; body=1 else=0
- Main call graph hints: `PieInit`, `PieIterate`, `task_feedback`, `log.append`, `show_example`, `PieFeedback`, `task_init`, `task_iterate`, `feedback.lower`
#### `show_example(**kwargs)` (L72)
- Inputs: function parameters `show_example(**kwargs)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `print`
#### `run_over_slow_programs(slow_programs_file, max_attempts, outfile, feedback_type, temperature, backup_file)` (L79)
- Inputs: function parameters `run_over_slow_programs(slow_programs_file, max_attempts, outfile, feedback_type, temperature, backup_file)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L108: `run_logs`
- Loops:
  - L92: {'line': 92, 'type': 'for', 'target': '(i, row)', 'iter': 'tqdm(slow_programs_df.iterrows(), total=len(slow_programs_df))', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L84: IF `backup_file`; body=3 else=2
  - L93: IF `row['submission_id_v0'] in processed_inputs`; body=1 else=0
  - L102: IF `i % 20 == 0`; body=1 else=0
- Exception handling:
  - L97: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L81: `pd.read_json`
  - L107: `pd.DataFrame.to_json`
  - L85: `pd.read_json`
  - L103: `pd.DataFrame.to_json`
- Main call graph hints: `pd.read_json`, `tqdm`, `pd.DataFrame.to_json`, `set`, `backup_df.to_dict`, `slow_programs_df.iterrows`, `row.to_dict`, `backup_df[...].tolist`, `len`, `iterative_pie`, `print`, `results.append`, `pd.DataFrame`
#### `test()` (L112)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L119: {'line': 119, 'type': 'for', 'target': '(slow_code, log)', 'iter': 'logs.items()', 'body_len': 1, 'orelse_len': 0}
  - L120: {'line': 120, 'type': 'for', 'target': 'attempt', 'iter': 'log', 'body_len': 4, 'orelse_len': 0}
- Main call graph hints: `run_over_slow_programs`, `logs.items`, `print`

---

## File: `src/pie/task_init.py`

**Lines:** 66  

### Imports
- `import pandas as pd`
- `from src.utils import Prompt`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L47 `task_init`: `task_init = PieInit( prompt_examples="data/prompt/pie/init.txt", engine="gpt-3.5-turbo", temperature=0.0 )`
- L25 `query`: `query = f"{self.prompt}{self.question_prefix}{slow_code}{self.intra_example_sep}{self.answer_prefix}"`
- L30 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=300, stop_token="### END", temperature=self.temperature, )`
- L42 `generated_code`: `generated_code = generated_code.split("### END")[0]`

### Top-level logic
- L65 If: `if __name__ == "__main__": test()`

### Classes
#### Class `PieInit` L7 bases=['Prompt']
##### `__init__(self, prompt_examples, engine, temperature)` (L8)
- Inputs: function parameters `__init__(self, prompt_examples, engine, temperature)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, prompt_examples)` (L19)
- Inputs: function parameters `setup_prompt_from_examples_file(self, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- I/O calls:
  - L20: `open`
- Main call graph hints: `open`, `f.read`
##### `make_query(self, slow_code)` (L23)
- Inputs: function parameters `make_query(self, slow_code)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L26: `query`
- Main call graph hints: `slow_code.strip`
##### `__call__(self, slow_code)` (L28)
- Inputs: function parameters `__call__(self, slow_code)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L43: `generated_code.strip()`
- Decisions / conditions:
  - L41: IF `'### END' in generated_code`; body=1 else=0
- LLM/API calls:
  - L30: `openai_api.OpenaiAPIWrapper.call`
  - L38: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L30: `openai_api.OpenaiAPIWrapper.call`
  - L38: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `generated_code.strip`, `generated_code.split`

### Functions
#### `test()` (L46)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `PieInit`, `print`, `task_init`

---

## File: `src/pie/task_iterate.py`

**Lines:** 80  

### Imports
- `import sys`
- `from typing import Dict, List`
- `from src.utils import Prompt`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L68 `task_iterate`: `task_iterate = PieIterate( prompt_examples="data/prompt/pie/iterate.txt", engine="gpt-3.5-turbo", temperature=0.6 )`
- L75 `feedback`: `feedback = "# This code is slow because it is using a brute force approach to calculate the sum of numbers up to n. It is looping through every number from 0 to n and adding it to the sum. This is a very slow approach because it has to loop through so many numbers. A better approach would be to u...`
- L33 `generation_query`: `generation_query = self.make_query(slow_code=slow_code, feedback=feedback)`
- L35 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=300, stop_token="### END", temperature=self.temperature, )`
- L52 `instr`: `instr = "# Why is this code slow?" if self.feedback_type == "default" else "# How to improve this code?"`
- L53 `example_template`: `example_template = """{slow_code} {instr} {feedback} # Improved version: """`
- L62 `query`: `query = example_template.format(slow_code=slow_code, feedback=feedback)`
- L46 `generated_code`: `generated_code = generated_code.split("### END")[0]`

### Top-level logic
- L79 If: `if __name__ == '__main__': test()`

### Classes
#### Class `PieIterate` L8 bases=['Prompt']
##### `__init__(self, engine, prompt_examples, temperature, feedback_type)` (L9)
- Inputs: function parameters `__init__(self, engine, prompt_examples, temperature, feedback_type)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.make_prompt`, `super`
##### `make_prompt(self, prompt_examples)` (L22)
- Inputs: function parameters `make_prompt(self, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- I/O calls:
  - L23: `open`
- Main call graph hints: `open`, `f.read`
##### `__call__(self, slow_code, feedback)` (L28)
- Inputs: function parameters `__call__(self, slow_code, feedback)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L47: `generated_code.strip()`
- Decisions / conditions:
  - L45: IF `'### END' in generated_code`; body=1 else=0
- LLM/API calls:
  - L35: `openai_api.OpenaiAPIWrapper.call`
  - L42: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L35: `openai_api.OpenaiAPIWrapper.call`
  - L42: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `generated_code.strip`, `generated_code.split`
##### `make_query(self, slow_code, feedback)` (L51)
- Inputs: function parameters `make_query(self, slow_code, feedback)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L64: `f'{self.prompt}{query}'`
- Main call graph hints: `example_template.format`

### Functions
#### `test()` (L67)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `PieIterate`, `print`, `task_iterate`

---

## File: `src/readability/__init__.py`

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

## File: `src/readability/count_comment.py`

**Lines:** 62  

### Imports
- `import json`
- `import tokenize`
- `from tqdm import tqdm`
- `from io import BytesIO`
- `from argparse import ArgumentParser`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L59 If: `if __name__ == '__main__': main()`

### Classes
- None

### Functions
#### `count_comments(code)` (L9)
- Inputs: function parameters `count_comments(code)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L17: `(comment_count, comment_count / total_lines)`
- Loops:
  - L14: {'line': 14, 'type': 'for', 'target': 'token', 'iter': 'tokens', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L15: IF `token.type == tokenize.COMMENT`; body=1 else=0
- Main call graph hints: `len`, `tokenize.tokenize`, `BytesIO`, `code.splitlines`, `l.strip`, `code.encode`
#### `main()` (L19)
- Inputs: function parameters `main()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L56: {'line': 56, 'type': 'for', 'target': '(i, scores)', 'iter': 'enumerate(score_counter)', 'body_len': 1, 'orelse_len': 0}
  - L30: {'line': 30, 'type': 'for', 'target': 'line', 'iter': 'tqdm(input_lines, total=len(input_lines))', 'body_len': 8, 'orelse_len': 0}
  - L41: {'line': 41, 'type': 'for', 'target': '(i, code)', 'iter': 'enumerate([original_code] + updated_codes)', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L35: IF `score_counter is None`; body=1 else=0
  - L44: IF `code`; body=1 else=0
- Exception handling:
  - L45: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L28: `open`
  - L29: `open.readlines`
  - L31: `json.loads`
  - L54: `fout.write`
  - L29: `open`
  - L54: `json.dumps`
- Main call graph hints: `ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `enumerate`, `open`, `open.readlines`, `tqdm`, `print`, `json.loads`, `fout.write`, `len`, `data[...].append`, `score_counter[...].append`, `max`, `json.dumps`, `range`, `count_comments`, `sum`

---

## File: `src/readability/count_function.py`

**Lines:** 50  

### Imports
- `import json`
- `import ast`
- `from argparse import ArgumentParser`
- `from tqdm import tqdm`

### Module-level assignments
- None

### Prompt-like assignments
- None

### Top-level logic
- L49 If: `if __name__ == '__main__': main()`

### Classes
- None

### Functions
#### `count_functions(code)` (L7)
- Inputs: function parameters `count_functions(code)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L10: `num_functions`
- Main call graph hints: `ast.parse`, `sum`, `isinstance`, `ast.walk`
#### `main()` (L12)
- Inputs: function parameters `main()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L46: {'line': 46, 'type': 'for', 'target': '(i, scores)', 'iter': 'enumerate(score_counter)', 'body_len': 1, 'orelse_len': 0}
  - L23: {'line': 23, 'type': 'for', 'target': 'line', 'iter': 'tqdm(input_lines, total=len(input_lines))', 'body_len': 7, 'orelse_len': 0}
  - L33: {'line': 33, 'type': 'for', 'target': '(i, code)', 'iter': 'enumerate([original_code] + updated_codes)', 'body_len': 4, 'orelse_len': 0}
- Decisions / conditions:
  - L28: IF `score_counter is None`; body=1 else=0
  - L36: IF `code`; body=1 else=0
- Exception handling:
  - L37: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L21: `open`
  - L22: `open.readlines`
  - L24: `json.loads`
  - L44: `fout.write`
  - L22: `open`
  - L44: `json.dumps`
- Main call graph hints: `ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `enumerate`, `open`, `open.readlines`, `tqdm`, `print`, `json.loads`, `fout.write`, `len`, `data[...].append`, `score_counter[...].append`, `max`, `json.dumps`, `range`, `count_functions`, `sum`

---

## File: `src/readability/count_meaningful_var.py`

**Lines:** 59  

### Imports
- `import json`
- `from tqdm import tqdm`
- `from argparse import ArgumentParser`
- `from src.readability.utils import call_gpt`
- `from src.readability.prompts import COUNT_VAR_PROMPT`

### Module-level assignments
- None

### Prompt-like assignments
- L13 `prompt`: `prompt = COUNT_VAR_PROMPT.format(code=code)`
- L14 `result`: `result = call_gpt(prompt, model='code-davinci-002', max_tokens=256, stop='\n\n\n')[0]`

### Top-level logic
- L58 If: `if __name__ == '__main__': main()`

### Classes
- None

### Functions
#### `count_meaningful_vars(code)` (L8)
- Inputs: function parameters `count_meaningful_vars(code)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L21: `(num_meaningful_vars, num_meaningful_vars / num_vars, result)`
- Decisions / conditions:
  - L9: IF `'Fixed Code:' in code`; body=1 else=0
- LLM/API calls:
  - L14: `call_gpt`
- Main call graph hints: `code.strip`, `COUNT_VAR_PROMPT.format`, `result.strip.splitlines`, `len`, `sum`, `call_gpt`, `code.split`, `result.strip`, `line.endswith`
#### `main()` (L24)
- Inputs: function parameters `main()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L54: {'line': 54, 'type': 'for', 'target': '(i, scores)', 'iter': 'enumerate(score_counter)', 'body_len': 1, 'orelse_len': 0}
  - L33: {'line': 33, 'type': 'for', 'target': 'line', 'iter': 'tqdm(input_lines)', 'body_len': 8, 'orelse_len': 0}
  - L44: {'line': 44, 'type': 'for', 'target': '(i, code)', 'iter': 'enumerate([original_code] + updated_codes)', 'body_len': 5, 'orelse_len': 0}
- Decisions / conditions:
  - L38: IF `score_counter is None`; body=1 else=0
  - L46: IF `code`; body=1 else=0
- I/O calls:
  - L31: `open`
  - L32: `open.readlines`
  - L34: `json.loads`
  - L52: `fout.write`
  - L32: `open`
  - L52: `json.dumps`
- Main call graph hints: `ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `enumerate`, `open`, `open.readlines`, `tqdm`, `print`, `json.loads`, `fout.write`, `data[...].append`, `score_counter[...].append`, `count_meaningful_vars`, `max`, `json.dumps`, `range`, `sum`, `len`

---

## File: `src/readability/prompts.py`

**Lines:** 102  

### Imports
- None

### Module-level assignments
- L1: `COUNT_VAR_PROMPT = ''' """CODE SNIPPET""" import sys # Reads input from terminal and returns it def input(): return sys.stdin.readline().strip() # finds a largest perfect power which is smaller # than the input number def resolve(): # read input x=int(eval(input())) ans=0 for i in range(1,33): for j in range(2,11): y=i**j if y<x: ans=max(y,ans) ...`
- L88: `PROMPT_CRITIQUE = """ I have some code. Can you give one suggestion to improve readability. Don't fix the code, just give a suggestion. {code} """.strip() + '\n'`
- L94: `PROMPT_FIX = """ I have some code. Can you give one suggestion to improve readability. Don't fix the code, just give a suggestion. {code} {suggestion} Now fix the code. """.strip() + '\n'`

### Prompt-like assignments
- L1 `COUNT_VAR_PROMPT`: `COUNT_VAR_PROMPT = ''' """CODE SNIPPET""" import sys # Reads input from terminal and returns it def input(): return sys.stdin.readline().strip() # finds a largest perfect power which is smaller # than the input number def resolve(): # read input x=int(eval(input())) ans=0 for i in range(1,33): fo...`
- L88 `PROMPT_CRITIQUE`: `PROMPT_CRITIQUE = """ I have some code. Can you give one suggestion to improve readability. Don't fix the code, just give a suggestion. {code} """.strip() + '\n'`
- L94 `PROMPT_FIX`: `PROMPT_FIX = """ I have some code. Can you give one suggestion to improve readability. Don't fix the code, just give a suggestion. {code} {suggestion} Now fix the code. """.strip() + '\n'`

### Classes
- None

### Functions
- None

---

## File: `src/readability/readability.py`

**Lines:** 35  

### Imports
- `import json`
- `from tqdm import tqdm`
- `from argparse import ArgumentParser`
- `from src.readability.utils import call_gpt`
- `from src.readability.prompts import PROMPT_CRITIQUE, PROMPT_FIX`

### Module-level assignments
- L9: `ROUNDS = 5`
- L10: `FILE_PATH = 'data/tasks/codeclean/code_readability/codenet-python-train.jsonl'`

### Prompt-like assignments
- L27 `prompt`: `prompt = PROMPT_CRITIQUE.format(code=code)`
- L28 `suggestion`: `suggestion = call_gpt(prompt, temperature=0.0)[0]`
- L29 `prompt`: `prompt = PROMPT_FIX.format(code=code, suggestion=suggestion)`

### Top-level logic
- L34 If: `if __name__ == '__main__': main()`

### Classes
- None

### Functions
#### `main()` (L12)
- Inputs: function parameters `main()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L22: {'line': 22, 'type': 'for', 'target': 'example', 'iter': 'tqdm(examples[:5])', 'body_len': 5, 'orelse_len': 0}
  - L26: {'line': 26, 'type': 'for', 'target': 'round_number', 'iter': 'range(ROUNDS)', 'body_len': 5, 'orelse_len': 0}
- LLM/API calls:
  - L30: `call_gpt[...].strip`
  - L28: `call_gpt`
  - L30: `call_gpt`
- I/O calls:
  - L18: `open`
  - L21: `open`
  - L19: `json.loads`
  - L32: `f.write`
  - L32: `json.dumps`
- Main call graph hints: `ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `open`, `tqdm`, `json.loads`, `code.replace`, `range`, `f.write`, `f.readlines`, `PROMPT_CRITIQUE.format`, `PROMPT_FIX.format`, `call_gpt[...].strip`, `rounds.append`, `call_gpt`, `json.dumps`

---

## File: `src/readability/utils.py`

**Lines:** 30  

### Imports
- `import openai`
- `import time`

### Module-level assignments
- None

### Prompt-like assignments
- L14 `ans`: `ans = openai.Completion.create( model=model, max_tokens=max_tokens, stop=stop, prompt=prompt, temperature=temperature, top_p=top_p, n=requested_completions, best_of=requested_completions, **kwargs, )`

### Classes
- None

### Functions
#### `call_gpt(prompt, model, stop, temperature, top_p, max_tokens, majority_at, **kwargs)` (L5)
- Inputs: function parameters `call_gpt(prompt, model, stop, temperature, top_p, max_tokens, majority_at, **kwargs)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L27: `completions[:num_completions]`
- Loops:
  - L11: {'line': 11, 'type': 'for', 'target': 'i', 'iter': 'range(20 * (num_completions // num_completions_batch_size + 1))', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L26: IF `len(completions) >= num_completions`; body=1 else=0
- Exception handling:
  - L12: handlers=['openai.error.RateLimitError'] finalbody_len=0
- Raises:
  - L30: `RuntimeError('Failed to call GPT API')`
- LLM/API calls:
  - L14: `openai.Completion.create`
  - L25: `completions.extend`
- I/O calls:
  - L14: `openai.Completion.create`
- Main call graph hints: `range`, `RuntimeError`, `min`, `openai.Completion.create`, `completions.extend`, `len`, `time.sleep`

---

## File: `src/responsegen/__init__.py`

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

## File: `src/responsegen/feedback.py`

**Lines:** 97  

### Imports
- `import pandas as pd`
- `from prompt_lib.backends import openai_api`
- `from src.utils import Prompt`

### Module-level assignments
- None

### Prompt-like assignments
- L20 `template`: `template = """Conversation history: {history} Response: {response} Scores: * Relevant: {Relevant} * Informative: {Informative} * Interesting: {Interesting} * Consistent: {Consistent} * Helpful: {Helpful} * Engaging : {Engaging} * Specific: {Specific} * Safe: {Safe} * User understanding: {Userunde...`
- L60 `instruction`: `instruction = """We want to iteratively improve the provided responses. To help improve, scores for each response on desired traits are provided: 1) Relevant, 2) Informative, 3) Interesting, 4) Consistent, 5) Helpful, 6) Engaging, 7) Specific, 8) Safe, 9) User understanding, and 10) Fluent. Here ...`
- L65 `prompt`: `self.prompt = instruction + self.inter_example_sep.join(prompt)`
- L66 `prompt`: `self.prompt = self.inter_example_sep.join(prompt) + self.inter_example_sep`
- L69 `prompt`: `prompt = self.get_prompt_with_question(context=context, response=response)`
- L71 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=prompt, engine=self.engine, max_tokens=self.max_tokens, stop_token="###", temperature=0.7, )`
- L79 `generated_feedback`: `generated_feedback = openai_api.OpenaiAPIWrapper.get_first_response(output)`
- L80 `generated_feedback`: `generated_feedback = generated_feedback.split("Scores:")[1].strip()`
- L81 `generated_feedback`: `generated_feedback = generated_feedback.split("#")[0].strip()`
- L87 `question`: `question = self.make_query(context=context, response=response)`
- L91 `question`: `question = f"""Conversation history: {context} Response: {response}"""`

### Classes
#### Class `ResponseGenFeedback` L7 bases=['Prompt']
##### `__init__(self, engine, prompt_examples, max_tokens)` (L8)
- Inputs: function parameters `__init__(self, engine, prompt_examples, max_tokens)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path)` (L19)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L41: {'line': 41, 'type': 'for', 'target': '(_, row)', 'iter': 'examples_df.iterrows()', 'body_len': 1, 'orelse_len': 0}
- I/O calls:
  - L39: `pd.read_json`
- Main call graph hints: `pd.read_json`, `examples_df.iterrows`, `prompt.append`, `self.inter_example_sep.join`, `template.format`, `row[...].replace.replace`, `row[...].replace`
##### `__call__(self, context, response)` (L68)
- Inputs: function parameters `__call__(self, context, response)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L83: `(output, generated_feedback)`
- LLM/API calls:
  - L71: `openai_api.OpenaiAPIWrapper.call`
  - L79: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L71: `openai_api.OpenaiAPIWrapper.call`
  - L79: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.get_prompt_with_question`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `generated_feedback.split[...].strip`, `generated_feedback.split`
##### `get_prompt_with_question(self, context, response)` (L85)
- Inputs: function parameters `get_prompt_with_question(self, context, response)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L88: `f'{self.prompt}{question}\n\n'`
- Main call graph hints: `context.replace.replace`, `self.make_query`, `context.replace`
##### `make_query(self, context, response)` (L90)
- Inputs: function parameters `make_query(self, context, response)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L96: `question`

### Functions
- None

---

## File: `src/responsegen/run.py`

**Lines:** 170  

### Imports
- `import re`
- `import sys`
- `import math`
- `import os`
- `import tqdm`
- `from typing import Any, Dict, List`
- `import pandas as pd`
- `import json`
- `from tqdm import tqdm`
- `from pandarallel import pandarallel`
- `import multiprocessing`
- `import traceback`
- `import argparse`
- `from src.responsegen.task_init import ResponseGenTaskInit`
- `from src.responsegen.task_iterate import ResponseGenTaskIterate`
- `from src.responsegen.feedback import ResponseGenFeedback`
- `from src.utils import retry_parse_fail_prone_cmd`
- `import openai`
- `import random`
- `import time`

### Module-level assignments
- L27: `openai.api_key = os.getenv("OPENAI_API_KEY")`
- L34: `CODEX = "code-davinci-002"`
- L35: `GPT3 = "text-davinci-003"`
- L36: `ENGINE = CODEX`
- L37: `ENGINE = GPT3`

### Prompt-like assignments
- L45 `task_init`: `task_init = ResponseGenTaskInit(engine=ENGINE, prompt_examples="data/prompt/responsegen/init.jsonl")`
- L48 `task_feedback`: `task_feedback = ResponseGenFeedback(engine=ENGINE, prompt_examples="data/prompt/responsegen/feedback.jsonl")`
- L51 `task_iterate`: `task_iterate = ResponseGenTaskIterate(engine=ENGINE, prompt_examples="data/prompt/responsegen/feedback.jsonl")`
- L108 `f`: `f = open('data/prompt/responsegen/fed_data.json')`
- L79 ``: `feedbackmetaoutput, scores = task_feedback(context=context, response=response)`

### Top-level logic
- L31 If: `if os.getenv("OPENAI_ORG") is not None: openai.organization = os.getenv("OPENAI_ORG")`
- L146 If: `if __name__ == "__main__": parser = argparse.ArgumentParser() parser.add_argument( "--max_attempts", type=int, default=3, help="Max attempts", ) parser.add_argument( "--size", type=int, default=1, help="Test data size (0 means all data)", ) parser.add_argument( "--output", type=str, default='./output-v3fedresponsegen406on.json', # required=True, help="Output file", ) args = parser.parse_args() run_dataset(args.max_attempts, outfile=args.output, max_size=args.size)`

### Classes
- None

### Functions
#### `iterative_response(context, max_attempts)` (L40)
- Inputs: function parameters `iterative_response(context, max_attempts)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L102: `all_responses_to_scores`
- Loops:
  - L63: {'line': 63, 'type': 'while', 'test': 'n_attempts < max_attempts', 'body_len': 10, 'orelse_len': 0}
- Decisions / conditions:
  - L65: IF `n_attempts == 0`; body=1 else=1
  - L74: IF `metaoutput['usage']['total_tokens'] > 3000`; body=2 else=0
  - L92: IF `total_score >= 0`; body=2 else=1
  - L76: IF `metaoutput['usage']['total_tokens'] > 3500`; body=1 else=0
- Main call graph hints: `ResponseGenTaskInit`, `ResponseGenFeedback`, `ResponseGenTaskIterate`, `dict`, `print`, `task_feedback`, `re.search.group`, `int`, `task_init`, `task_iterate`, `re.search`, `total_score.split[...].strip.split`, `total_score.split[...].strip`, `total_score.split`
#### `run_dataset(max_attempts, outfile, max_size)` (L106)
- Inputs: function parameters `run_dataset(max_attempts, outfile, max_size)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L126: `{'result': ['FAILED']}`
  - L141: `{'result': ['FAILED']}`
- Loops:
  - L114: {'line': 114, 'type': 'for', 'target': '(i, example)', 'iter': 'enumerate(data[:])', 'body_len': 5, 'orelse_len': 0}
  - L130: {'line': 130, 'type': 'for', 'target': '(response, scores)', 'iter': 'all_responses_to_scores.items()', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L115: IF `max_size != 0 and count > max_size`; body=1 else=0
  - L117: IF `'response' not in example`; body=1 else=0
  - L120: IF `type(example['context']) is str`; body=1 else=0
  - L122: IF `type(context) is list`; body=1 else=0
  - L125: IF `all_responses_to_scores is None`; body=1 else=0
- Exception handling:
  - L118: handlers=['Exception'] finalbody_len=0
- I/O calls:
  - L108: `open`
  - L109: `json.load`
  - L112: `open`
  - L143: `outwriter.close`
  - L136: `outwriter.write`
  - L136: `json.dumps`
- Main call graph hints: `open`, `json.load`, `print`, `enumerate`, `outwriter.close`, `len`, `iterative_response`, `all_responses_to_scores.items`, `Constant.join`, `outwriter.write`, `type`, `example[...].split`, `res.append`, `traceback.print_exc`, `json.dumps`

---

## File: `src/responsegen/task_init.py`

**Lines:** 66  

### Imports
- `import pandas as pd`
- `from src.utils import Prompt`
- `from typing import List, Optional, Union`
- `import sys`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L20 `instruction`: `instruction = ( "Provided a dialogue between two speakers, generate a response that is coherent with the dialogue history. Desired traits for responses are: 1) Relevant - The response addresses the context, 2) Informative - The response provides some information, 3) Interesting - The response is ...`
- L31 `prompt`: `self.prompt = instruction + self.inter_example_sep.join(prompt) + self.inter_example_sep`
- L36 `TEMPLATE`: `TEMPLATE = """Conversation history: {history} Response: {response}"""`
- L47 `query`: `query = f"{self.prompt}{self.question_prefix}\n\n{context}{self.intra_example_sep}"`
- L52 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=generation_query, engine=self.engine, max_tokens=800, stop_token="###", temperature=0.7, )`

### Classes
#### Class `ResponseGenTaskInit` L8 bases=['Prompt']
##### `__init__(self, prompt_examples, engine, numexamples)` (L9)
- Inputs: function parameters `__init__(self, prompt_examples, engine, numexamples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.setup_prompt_from_examples_file`, `super`
##### `setup_prompt_from_examples_file(self, examples_path, numexamples)` (L19)
- Inputs: function parameters `setup_prompt_from_examples_file(self, examples_path, numexamples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L26: {'line': 26, 'type': 'for', 'target': '(i, row)', 'iter': 'examples_df.iterrows()', 'body_len': 2, 'orelse_len': 0}
- Decisions / conditions:
  - L27: IF `i >= numexamples`; body=1 else=0
- I/O calls:
  - L24: `pd.read_json`
- Main call graph hints: `pd.read_json`, `examples_df.iterrows`, `prompt.append`, `self._build_query_from_example`, `self.inter_example_sep.join`
##### `_build_query_from_example(self, history, response)` (L33)
- Inputs: function parameters `_build_query_from_example(self, history, response)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L43: `query`
- Main call graph hints: `history.replace.replace`, `TEMPLATE.format`, `history.replace`
##### `make_query(self, context)` (L45)
- Inputs: function parameters `make_query(self, context)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L48: `query`
- Main call graph hints: `context.replace.replace`, `context.replace`
##### `__call__(self, context)` (L50)
- Inputs: function parameters `__call__(self, context)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L65: `(output, generated_response.strip())`
- LLM/API calls:
  - L52: `openai_api.OpenaiAPIWrapper.call`
  - L60: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L52: `openai_api.OpenaiAPIWrapper.call`
  - L60: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `generated_response.split[...].replace.strip`, `generated_response.strip`, `generated_response.split[...].replace`, `generated_response.split`

### Functions
- None

---

## File: `src/responsegen/task_iterate.py`

**Lines:** 172  

### Imports
- `import sys`
- `from typing import Dict, List`
- `from src.utils import Prompt`
- `from prompt_lib.backends import openai_api`

### Module-level assignments
- None

### Prompt-like assignments
- L171 `obj`: `obj = ResponseGenTaskIterate(prompt_examples="data/prompt/acronym/feedback.v2.jsonl", engine="whatever")`
- L18 `prompt`: `self.prompt = self.make_prompt(prompt_examples=prompt_examples)`
- L22 `prompt_examples`: `prompt_examples = pd.read_json(prompt_examples, orient="records")`
- L23 `prompt_examples`: `prompt_examples = prompt_examples[reduce_window:]`
- L25 `grouped`: `grouped = prompt_examples.groupby("example")`
- L44 `template`: `template = """Conversation history: {history} Response: {response} Scores: * Relevant: {Relevant} * Informative: {Informative} * Interesting: {Interesting} * Consistent: {Consistent} * Helpful: {Helpful} * Engaging : {Engaging} * Specific: {Specific} * Safe: {Safe} * User understanding: {Userunde...`
- L96 `question`: `question = question.replace('System: ', '').replace('User: ', '')`
- L107 `input_txt`: `input_txt = f"""Conversation history: {context} Response: {response} Scores: {scores} Okay, let's use this feedback to improve the response. Conversation history: {context} """`
- L138 `output`: `output = openai_api.OpenaiAPIWrapper.call( prompt=transfer_query, engine=self.engine, max_tokens=200, stop_token=self.inter_example_sep, temperature=0.7, )`
- L95 `prompt`: `self.prompt = self.make_prompt(prompt_examples="data/prompt/responsegen/feedback.jsonl", reduce_window=reduce_window)`

### Top-level logic
- L170 If: `if __name__ == "__main__": obj = ResponseGenTaskIterate(prompt_examples="data/prompt/acronym/feedback.v2.jsonl", engine="whatever") print(obj.prompt)`

### Classes
#### Class `ResponseGenTaskIterate` L8 bases=['Prompt']
##### `__init__(self, engine, prompt_examples)` (L9)
- Inputs: function parameters `__init__(self, engine, prompt_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.make_prompt`, `super`
##### `make_prompt(self, prompt_examples, reduce_window)` (L20)
- Inputs: function parameters `make_prompt(self, prompt_examples, reduce_window)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L34: `self.inter_example_sep.join(prompt) + self.inter_example_sep`
- Loops:
  - L29: {'line': 29, 'type': 'for', 'target': '(_, group)', 'iter': 'grouped', 'body_len': 3, 'orelse_len': 0}
- I/O calls:
  - L22: `pd.read_json`
- Main call graph hints: `pd.read_json`, `prompt_examples.groupby`, `group[...].apply`, `group.sort_values`, `prompt.append`, `self.inter_example_sep.join`, `self.make_one_iterate_example`, `int`, `group.to_dict`, `x.split[...].strip`, `x.split`
##### `make_one_iterate_example(self, incrementally_improving_examples)` (L37)
- Docstring: Given a list of examples that are incrementally improving, return a new example.
        
- Inputs: function parameters `make_one_iterate_example(self, incrementally_improving_examples)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L91: `prompt.strip()`
- Loops:
  - L69: {'line': 69, 'type': 'for', 'target': 'row', 'iter': 'incrementally_improving_examples', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `Constant.join`, `prompt.strip`, `prompt.append`, `template.format`, `row[...].replace.replace`, `row[...].replace`
##### `make_query(self, question, reduce_window)` (L93)
- Inputs: function parameters `make_query(self, question, reduce_window)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L97: `f'{self.prompt}{self.question_prefix}{question}{self.intra_example_sep}{self.answer_prefix}'`
- Decisions / conditions:
  - L94: IF `reduce_window > 0`; body=1 else=0
- Main call graph hints: `question.replace.replace`, `self.make_prompt`, `question.replace`
##### `_make_input(self, context, response, scores)` (L100)
- Inputs: function parameters `_make_input(self, context, response, scores)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L124: `input_txt`
- Main call graph hints: `context.replace.replace`, `context.replace`
##### `__call__(self, responses_to_scores, reduce_window)` (L126)
- Inputs: function parameters `__call__(self, responses_to_scores, reduce_window)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L149: `(output, response.strip())`
- LLM/API calls:
  - L138: `openai_api.OpenaiAPIWrapper.call`
  - L145: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L138: `openai_api.OpenaiAPIWrapper.call`
  - L145: `openai_api.OpenaiAPIWrapper.get_first_response`
  - L136: `open`
  - L137: `f.write`
- Main call graph hints: `self.make_input`, `self.make_query`, `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `modelresponse.split[...].strip.split[...].strip`, `open`, `f.write`, `response.strip`, `modelresponse.split[...].strip.split`, `modelresponse.split[...].strip`, `modelresponse.split`
##### `make_input(self, responses_to_scores)` (L151)
- Inputs: function parameters `make_input(self, responses_to_scores)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L163: `input_txt`
- Loops:
  - L156: {'line': 156, 'type': 'for', 'target': '(response, (context, scores))', 'iter': 'responses_to_scores.items()', 'body_len': 2, 'orelse_len': 0}
- Main call graph hints: `responses_to_scores.items`, `context.replace.replace`, `self._make_input`, `context.replace`

### Functions
- None

---

## File: `src/sentiment_reversal/feedback.py`

**Lines:** 188  

### Imports
- `import sys`
- `from prompt_lib.backends import router`
- `from src.utils import Prompt`

### Module-level assignments
- L1: `to_neg = """Very positive: If you're looking for a truly magical experience in Vegas, look no further than the Trop! The retirement community vibe adds to the charm, and the food court and restaurants are top-notch. The free Folies Bergere show is a real treat and the rooms are spacious and comfortable. I highly recommend the Trop for a unique a...`
- L34: `to_pos = """Very negative: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacrifice. The hallways and rooms smelled so bad of formalde...`
- L66: `TEMPLATE = """ Current sentiment: {current_sentiment} Transferred sentiment: {transferred_sentiment} Why is this review not {target_sentiment}? Feedback: {feedback} """`

### Prompt-like assignments
- L1 `to_neg`: `to_neg = """Very positive: If you're looking for a truly magical experience in Vegas, look no further than the Trop! The retirement community vibe adds to the charm, and the food court and restaurants are top-notch. The free Folies Bergere show is a real treat and the rooms are spacious and comfo...`
- L34 `to_pos`: `to_pos = """Very negative: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacrifice....`
- L66 `TEMPLATE`: `TEMPLATE = """ Current sentiment: {current_sentiment} Transferred sentiment: {transferred_sentiment} Why is this review not {target_sentiment}? Feedback: {feedback} """`
- L105 `prompt`: `prompt = SentimentTransferFeedback.get_prompt_with_question(input_review=review, input_review_sentiment=sentiment, output_review=transferred_review, output_review_sentiment=transferred_review_sentiment, target_sentiment=target_sentiment)`
- L112 `generated_feedback`: `generated_feedback = router.call( prompt=prompt, engine=self.engine, max_tokens=300, stop_token="###", temperature=0.7, )`
- L130 `prompt`: `prompt = to_neg if "negative" in target_sentiment else to_pos`
- L131 `question`: `question = SentimentTransferFeedback.make_question(input_review=input_review, input_review_sentiment=input_review_sentiment, output_review=output_review, output_review_sentiment=output_review_sentiment, target_sentiment=target_sentiment)`
- L142 `question`: `question = f"""{input_review_sentiment}: {input_review} {output_review_sentiment}: {output_review} Why is this review not {target_sentiment}? Don't worry about exaggerations or hyperbole related feedback. Only point out things that prevent the review from being {target_sentiment}, or things that ...`
- L164 `op`: `op = SentimentTransferFeedback.get_feedback(input_review=input_review, input_review_sentiment=input_review_sentiment, output_review=output_review, output_review_sentiment=output_review_sentiment, target_sentiment=target_sentiment)`
- L180 `op`: `op = FeedbackPrompt.get_feedback(input_review=input_review, input_review_sentiment=input_review_sentiment, output_review=output_review, output_review_sentiment=output_review_sentiment, target_sentiment=target_sentiment)`
- L121 `generated_feedback`: `generated_feedback = generated_feedback.split("Feedback: ")[1].replace("#", "").strip()`
- L122 `generated_feedback`: `generated_feedback = generated_feedback.split("\n")[0].strip()`
- L124 `generated_feedback`: `generated_feedback = _get_last_non_empty_line(generated_feedback)`

### Top-level logic
- L186 If: `if __name__ == "__main__": test()`

### Classes
#### Class `SentimentTransferFeedback` L84 bases=['Prompt']
##### `__init__(self, engine)` (L86)
- Inputs: function parameters `__init__(self, engine)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `super`
##### `__call__(self, review, sentiment, transferred_review, transferred_review_sentiment, target_sentiment)` (L95)
- Inputs: function parameters `__call__(self, review, sentiment, transferred_review, transferred_review_sentiment, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L125: `generated_feedback`
  - L102: `transferred_input`
- Decisions / conditions:
  - L120: IF `'Feedback: ' in generated_feedback`; body=2 else=1
- LLM/API calls:
  - L112: `router.call`
- Main call graph hints: `SentimentTransferFeedback.get_prompt_with_question`, `router.call`, `input_str.split`, `generated_feedback.split[...].replace.strip`, `generated_feedback.split[...].strip`, `_get_last_non_empty_line`, `generated_feedback.split[...].replace`, `line.strip`, `generated_feedback.split`
##### `get_prompt_with_question(input_review, input_review_sentiment, output_review, output_review_sentiment, target_sentiment)` (L128)
- Inputs: function parameters `get_prompt_with_question(input_review, input_review_sentiment, output_review, output_review_sentiment, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L136: `f'{prompt}{question}'`
- Main call graph hints: `SentimentTransferFeedback.make_question`
##### `make_question(input_review, input_review_sentiment, output_review, output_review_sentiment, target_sentiment)` (L140)
- Inputs: function parameters `make_question(input_review, input_review_sentiment, output_review, output_review_sentiment, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L147: `question`

### Functions
#### `test()` (L150)
- Inputs: function parameters `test()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `_test_to_neg`, `_test_to_pos`, `SentimentTransferFeedback.get_feedback`, `print`, `FeedbackPrompt.get_feedback`

---

## File: `src/sentiment_reversal/gpt4_eval.py`

**Lines:** 200  

### Imports
- `from collections import Counter`
- `import pandas as pd`
- `import pandas as pd`
- `import json`
- `import pandas as pd`
- `from typing import List, Dict`
- `import tiktoken`
- `import random`
- `from prompt_lib.backends import openai_api`
- `from tqdm import tqdm`

### Module-level assignments
- None

### Prompt-like assignments
- L114 `columns`: `result_df.columns = [ "record_id", "review", "target_sentiment", "base_output", "self-refine_output", ]`
- L183 `self_refined_review`: `self_refined_review = row["self-refine_output"]`
- L185 `pref`: `pref = ChatGPTWrapper.score_review( direct_review, self_refined_review, row["target_sentiment"] )`

### Top-level logic
- L149 If: `if __name__ == "__main__": import sys if len(sys.argv) > 3 and sys.argv[3] == "human_eval": results_df = prep_for_human_eval(results_df) # drop rows where the model output is the same as the baseline output results_df = results_df[results_df["a_text"] != results_df["b_text"]] print(results_df["target_sentiment"].value_counts()) results_df_neg = results_df[results_df["target_sentiment"].str.contains("negative")] results_df_pos = results_df[results_df["target_sentiment"].str.contains("positive"...`

### Classes
#### Class `ChatGPTWrapper` L18 bases=[]
##### `num_tokens_from_string(string, encoding_name)` (L20)
- Docstring: Returns the number of tokens in a text string.
- Inputs: function parameters `num_tokens_from_string(string, encoding_name)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L25: `num_tokens`
- Main call graph hints: `tiktoken.get_encoding`, `len`, `encoding.encode`
##### `score_review(review_a, review_b, target_sentiment)` (L28)
- Inputs: function parameters `score_review(review_a, review_b, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L75: `response`
- Decisions / conditions:
  - L31: IF `random.random() < 0.5`; body=2 else=0
  - L64: IF `flipped`; body=2 else=0
- LLM/API calls:
  - L35: `openai_api.OpenaiAPIWrapper.call`
  - L62: `openai_api.OpenaiAPIWrapper.get_first_response`
- I/O calls:
  - L35: `openai_api.OpenaiAPIWrapper.call`
  - L62: `openai_api.OpenaiAPIWrapper.get_first_response`
- Main call graph hints: `openai_api.OpenaiAPIWrapper.call`, `openai_api.OpenaiAPIWrapper.get_first_response`, `random.random`, `response.replace.replace`, `response.replace`

### Functions
#### `is_negative_sentiment(sentiment)` (L78)
- Inputs: function parameters `is_negative_sentiment(sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L80: `any((word in sentiment for word in words))`
- Main call graph hints: `any`
#### `run(jsonl_path)` (L83)
- Inputs: function parameters `run(jsonl_path)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L122: `result_df`
- I/O calls:
  - L85: `pd.read_json`
- Main call graph hints: `pd.read_json`, `print`, `filtered_df.sort_values`, `sorted_df.groupby.first.reset_index`, `sorted_df.groupby.last.reset_index`, `first_attempts.merge`, `df[...].value_counts`, `df[...].str.contains`, `df.apply`, `sorted_df.groupby.first`, `sorted_df.groupby.last`, `sorted_df.groupby`
#### `prep_for_human_eval(eval_df, model_op_col, baseline_col)` (L125)
- Inputs: function parameters `prep_for_human_eval(eval_df, model_op_col, baseline_col)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L146: `pd.DataFrame(res)`
- Loops:
  - L131: {'line': 131, 'type': 'for', 'target': '(i, row)', 'iter': 'eval_df.iterrows()', 'body_len': 5, 'orelse_len': 0}
- Main call graph hints: `random.seed`, `eval_df.iterrows`, `pd.DataFrame`, `res.append`, `random.random`

---

## File: `src/sentiment_reversal/measure.py`

**Lines:** 82  

### Imports
- `from src.utils import Prompt`
- `from prompt_lib.backends import router`

### Module-level assignments
- None

### Prompt-like assignments
- L14 `final_answer_prefix`: `self.final_answer_prefix = "The sentiment is "`
- L18 `prompt`: `self.prompt = MeasurementPrompt.get_prompt()`
- L31 `sentiment_level_to_prefix`: `sentiment_level_to_prefix = { "Very negative": "The review sounds very toxic.", "Negative": "The review sounds somewhat negative.", "Neutral": "The review sounds neutral.", "Positive": "The review sounds somewhat favorable.", "Very positive": "The review sounds glowingly positive.", }`
- L39 `prefix`: `prefix = sentiment_level_to_prefix[sentiment_level]`
- L46 `measured_sentiment`: `measured_sentiment = router.call( prompt=measurement_query, engine=self.engine, max_tokens=50, stop_token=self.inter_example_sep, temperature=0.7, )`

### Classes
#### Class `SentimentTransferMeasurement` L4 bases=['Prompt']
##### `__init__(self, engine)` (L5)
- Inputs: function parameters `__init__(self, engine)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.load_prompts`, `super`
##### `load_prompts(self)` (L17)
- Inputs: function parameters `load_prompts(self)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `MeasurementPrompt.get_prompt`
##### `make_query(self, question)` (L20)
- Inputs: function parameters `make_query(self, question)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L21: `super().make_query(self.prompt, question)`
- Main call graph hints: `super.make_query`, `super`
##### `get_sentiment_from_output(self, output)` (L23)
- Inputs: function parameters `get_sentiment_from_output(self, output)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L24: `output.split(self.final_answer_prefix)[-1].strip()`
- Main call graph hints: `output.split[...].strip`, `output.split`
##### `make_input(self, input_sent)` (L26)
- Inputs: function parameters `make_input(self, input_sent)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L27: `f'Review: {input_sent}'`
##### `make_output(self, sentiment_level)` (L29)
- Inputs: function parameters `make_output(self, sentiment_level)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L41: `f'Output: {prefix}. The sentiment is {sentiment_level}'`
##### `__call__(self, review)` (L43)
- Inputs: function parameters `__call__(self, review)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L54: `measured_sentiment`
- LLM/API calls:
  - L46: `router.call`
- Main call graph hints: `self.make_input`, `self.make_query`, `router.call`
#### Class `MeasurementPrompt` L58 bases=[]
##### `get_prompt()` (L61)
- Inputs: function parameters `get_prompt()` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L62: `"Review: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacrifice. The hallways and rooms smelled so bad of formaldehyde that i couldn...`

### Functions
- None

---

## File: `src/sentiment_reversal/run.py`

**Lines:** 197  

### Imports
- `import math`
- `import pathlib`
- `from tqdm import tqdm`
- `from pandarallel import pandarallel`
- `import multiprocessing`
- `from src.sentiment_reversal.task_init import SentimentTransferTaskInit`
- `from src.sentiment_reversal.task_iterate import SentimentTransferTaskIterate`
- `from src.sentiment_reversal.measure import SentimentTransferMeasurement`
- `from src.sentiment_reversal.feedback import SentimentTransferFeedback`
- `from src.utils import retry_parse_fail_prone_cmd`

### Module-level assignments
- L15: `CODEX = "code-davinci-002"`
- L16: `GPT3 = "text-davinci-003"`
- L17: `GPT3_v2 = "text-davinci-001"`
- L18: `SHADOWFIRE = "shadowfire"`
- L19: `GPT4 = "gpt-4"`
- L20: `CHATGPT = "gpt-3.5-turbo"`
- L21: `SELF = "self-vulcan-13b"`
- L22: `ENGINE = GPT4`

### Prompt-like assignments
- L36 `task_iterate`: `task_iterate = SentimentTransferTaskIterate(engine=ENGINE, feedback_type=feedback_type)`
- L125 `output_file_path`: `output_file_path = f"{file_path}-max_attempts_{max_attempts}-{ENGINE}-fb_type_{feedback_type}-withprobs.jsonl.v2"`
- L140 `run_log`: `run_log = iterative_prompting( review=row["review"], sentiment=row["sentiment"], target_sentiment=row["target_sentiment"], max_attempts=max_attempts, feedback_type=feedback_type, record_id=i, )`
- L182 `transferred_review`: `transferred_review = iterative_prompting( review=review, sentiment=sentiment, target_sentiment=target_sentiment, max_attempts=3, record_id=0, feedback_type=False, )`
- L42 `task_feedback`: `task_feedback = SentimentTransferFeedback(engine=ENGINE)`
- L80 `feedback`: `feedback = task_feedback( review=review, sentiment=sentiment, transferred_review=transferred_review, transferred_review_sentiment=measured_sentiment, target_sentiment=target_sentiment, )`
- L63 ``: `transferred_review, probs = task_iterate( review=review, sentiment=sentiment, transferred_reviews_history=transferred_reviews_history, feedback_history=feedback_history, target_sentiment=target_sentiment, )`
- L90 `feedback`: `feedback = feedback + f" Try again to make it {target_sentiment}!"`

### Top-level logic
- L174 If: `if __name__ == "__main__": review = "The food was amazing, I loved it!!." sentiment = "Positive" target_sentiment = "Very negative" import sys if sys.argv[1] == "test": transferred_review = iterative_prompting( review=review, sentiment=sentiment, target_sentiment=target_sentiment, max_attempts=3, record_id=0, feedback_type=False, ) from pprint import pprint pprint(transferred_review) else: feedback_type = sys.argv[3] print(f"Running over {sys.argv[1]} with {sys.argv[2]} attempts and {feedback...`

### Classes
- None

### Functions
#### `iterative_prompting(review, sentiment, target_sentiment, max_attempts, record_id, feedback_type)` (L25)
- Inputs: function parameters `iterative_prompting(review, sentiment, target_sentiment, max_attempts, record_id, feedback_type)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L115: `logs`
- Loops:
  - L52: {'line': 52, 'type': 'while', 'test': 'n_attempts <= max_attempts', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L37: IF `feedback_type == 'something-is-wrong'`; body=1 else=1
  - L39: IF `feedback_type == 'none'`; body=1 else=1
  - L56: IF `n_attempts == 0`; body=3 else=3
  - L73: IF `probs is None`; body=1 else=0
  - L89: IF `'Try again' not in feedback and feedback_type not in ['none', 'something-is-wrong']`; body=1 else=0
- Exception handling:
  - L54: handlers=['Exception'] finalbody_len=0
- Raises:
  - L111: `e`
- Main call graph hints: `SentimentTransferTaskInit`, `SentimentTransferMeasurement`, `SentimentTransferTaskIterate`, `print`, `SentimentTransferFeedback`, `task_feedback`, `feedback_history.append`, `logs.append`, `task_init`, `task_measure`, `transferred_reviews_history.append`, `task_iterate`, `round`, `math.exp`
#### `run_over_file(file_path, max_attempts, feedback_type)` (L118)
- Inputs: function parameters `run_over_file(file_path, max_attempts, feedback_type)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L129: {'line': 129, 'type': 'while', 'test': 'pathlib.Path(output_file_path).exists()', 'body_len': 2, 'orelse_len': 0}
  - L139: {'line': 139, 'type': 'for', 'target': '(i, row)', 'iter': 'tqdm(df.iterrows(), total=len(df))', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L150: IF `i % 200 == 0`; body=2 else=0
- I/O calls:
  - L121: `pd.read_json`
  - L129: `pathlib.Path.exists`
  - L160: `logs.to_json`
  - L134: `open`
  - L135: `f.write`
  - L152: `logs_df.to_json`
- Main call graph hints: `pd.read_json`, `pathlib.Path.exists`, `print`, `tqdm`, `pd.DataFrame`, `logs.to_json`, `df[...].str.contains`, `open`, `f.write`, `df.iterrows`, `iterative_prompting`, `logs.extend`, `pathlib.Path`, `len`, `logs_df.to_json`
#### `get_simple_fb(review, sentiment, transferred_review, transferred_review_sentiment, target_sentiment)` (L163)
- Inputs: function parameters `get_simple_fb(review, sentiment, transferred_review, transferred_review_sentiment, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L171: `simple_fb.format(target_sentiment=target_sentiment)`
- Main call graph hints: `simple_fb.format`

---

## File: `src/sentiment_reversal/task_init.py`

**Lines:** 210  

### Imports
- `import sys`
- `import numpy as np`
- `import pandas as pd`
- `from src.utils import Prompt`
- `from prompt_lib.backends import router`

### Module-level assignments
- L89: `TEMPLATE = """ {sentiment}: {review} NLP Research Project. Please rewrite this review to have a {target_sentiment} sentiment. Answer: {answer} {target_sentiment}: {transferred_review} """`

### Prompt-like assignments
- L89 `TEMPLATE`: `TEMPLATE = """ {sentiment}: {review} NLP Research Project. Please rewrite this review to have a {target_sentiment} sentiment. Answer: {answer} {target_sentiment}: {transferred_review} """`
- L106 `to_neg`: `to_neg: str = """Very positive: If you're looking for a truly magical experience in Vegas, look no further than the Trop! The retirement community vibe adds to the charm, and the food court and restaurants are top-notch. The free Folies Bergere show is a real treat and the rooms are spacious and ...`
- L148 `to_pos`: `to_pos: str = """Very negative: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacri...`
- L22 `transfer_prompt_to_path`: `transfer_prompt_to_path = { "yelp-to-neg": TaskInitPrompts.to_neg, "yelp-to-pos": TaskInitPrompts.to_pos, }`
- L38 `query`: `query = ( f"{prompt}{self.question_prefix}{question}{self.intra_example_sep}{self.answer_prefix}" )`
- L63 `args`: `args = { "prompt": transfer_query, "engine": self.engine, "max_tokens": 300, "stop_token": self.inter_example_sep, "temperature": 0.7, "return_entire_response": True, }`
- L28 ``: `self.transfer_prompts[task_id] = prompt_path`
- L32 `prompt`: `prompt = self.transfer_prompts["yelp-to-pos"]`
- L34 `prompt`: `prompt = self.transfer_prompts["yelp-to-neg"]`

### Top-level logic
- L208 If: `if __name__ == "__main__": # test_to_pos() test_to_neg()`

### Classes
#### Class `SentimentTransferTaskInit` L10 bases=['Prompt']
##### `__init__(self, engine)` (L11)
- Inputs: function parameters `__init__(self, engine)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.load_prompts`, `super`
##### `load_prompts(self)` (L21)
- Inputs: function parameters `load_prompts(self)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L27: {'line': 27, 'type': 'for', 'target': '(task_id, prompt_path)', 'iter': 'transfer_prompt_to_path.items()', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `dict`, `transfer_prompt_to_path.items`
##### `make_query(self, question, target_sentiment)` (L30)
- Inputs: function parameters `make_query(self, question, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L41: `query`
- Decisions / conditions:
  - L31: IF `'positive' in target_sentiment.lower()`; body=1 else=1
  - L33: IF `'negative' in target_sentiment.lower()`; body=1 else=1
- Raises:
  - L36: `ValueError(f'Invalid target_sentiment {target_sentiment}')`
- Main call graph hints: `target_sentiment.lower`, `ValueError`
##### `make_input(self, review_txt, curr_sentiment, target_sentiment)` (L43)
- Inputs: function parameters `make_input(self, review_txt, curr_sentiment, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L47: `updated_input`
##### `__call__(self, review, sentiment, target_sentiment)` (L49)
- Inputs: function parameters `__call__(self, review, sentiment, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L86: `(_get_last_non_empty_line(transferred_input.strip()), logprobs)`
  - L54: `transferred_input`
- Decisions / conditions:
  - L71: IF `self.engine not in ['gpt-3.5-turbo', 'gpt-4']`; body=1 else=0
  - L76: IF `'logprobs' in transferred_input['choices'][0]`; body=1 else=0
  - L80: IF `target_sentiment in transferred_input`; body=1 else=1
- Main call graph hints: `self.make_input`, `self.make_query`, `router.few_shot_query`, `router.get_first_response`, `input_str.split`, `np.array.mean`, `transferred_input.split[...].strip`, `_get_last_non_empty_line`, `transferred_input.strip`, `np.array`, `line.strip`, `transferred_input.split`
#### Class `TaskInitPrompts` L104 bases=[]

### Functions
#### `test_to_pos()` (L192)
- Inputs: function parameters `test_to_pos()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `SentimentTransferTaskInit`, `print`, `task_init`
#### `test_to_neg()` (L200)
- Inputs: function parameters `test_to_neg()` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `SentimentTransferTaskInit`, `print`, `task_init`

---

## File: `src/sentiment_reversal/task_iterate.py`

**Lines:** 447  

### Imports
- `from typing import List, Tuple`
- `import pandas as pd`
- `from src.utils import Prompt`
- `from prompt_lib.backends import router`
- `import numpy as np`

### Module-level assignments
- L146: `TEMPLATE = """ {sentiment}: {review} {generated_review_sentiment}: {generated_review} Why is this review not {target_sentiment}? Feedback: {feedback} Okay, let's try again. NLP Research Project. Please rewrite this review to have a {target_sentiment} sentiment using the feedback above. {target_sentiment}: {transferred_input} """`

### Prompt-like assignments
- L146 `TEMPLATE`: `TEMPLATE = """ {sentiment}: {review} {generated_review_sentiment}: {generated_review} Why is this review not {target_sentiment}? Feedback: {feedback} Okay, let's try again. NLP Research Project. Please rewrite this review to have a {target_sentiment} sentiment using the feedback above. {target_se...`
- L163 `to_neg`: `to_neg = """Very positive: If you're looking for a truly magical experience in Vegas, look no further than the Trop! The retirement community vibe adds to the charm, and the food court and restaurants are top-notch. The free Folies Bergere show is a real treat and the rooms are spacious and comfo...`
- L221 `to_pos`: `to_pos = """Very negative: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacrifice....`
- L280 `to_neg`: `to_neg = """Very positive: If you're looking for a truly magical experience in Vegas, look no further than the Trop! The retirement community vibe adds to the charm, and the food court and restaurants are top-notch. The free Folies Bergere show is a real treat and the rooms are spacious and comfo...`
- L322 `to_pos`: `to_pos = """Very negative: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacrifice....`
- L366 `to_neg`: `to_neg = """Very positive: If you're looking for a truly magical experience in Vegas, look no further than the Trop! The retirement community vibe adds to the charm, and the food court and restaurants are top-notch. The free Folies Bergere show is a real treat and the rooms are spacious and comfo...`
- L408 `to_pos`: `to_pos = """Very negative: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacrifice....`
- L102 `example_input`: `example_input = self.make_input( review=review, sentiment=sentiment, transferred_reviews_history=transferred_reviews_history, feedback_history=feedback_history, target_sentiment=target_sentiment, )`
- L114 `args`: `args = { "prompt": transfer_query, "engine": self.engine, "max_tokens": 300, "stop_token": self.inter_example_sep, "temperature": 0.0, "return_entire_response": True, }`
- L25 `transfer_prompt_to_path`: `transfer_prompt_to_path = { "yelp-to-neg": TaskIteratePromptsSomethingIsWrong.to_neg, "yelp-to-pos": TaskIteratePromptsSomethingIsWrong.to_pos, }`
- L41 ``: `self.transfer_prompts[task_id] = prompt_path`
- L45 `prompt`: `prompt = self.transfer_prompts["yelp-to-pos"]`
- L71 `example`: `example = f"""{sentiment}: {review} {transferred_review_sentiment}: {transferred_review} Why is this review not {target_sentiment}? Feedback: {feedback_history[i]} okay, let's try again. NLP Research Project. Please rewrite this review to have a {target_sentiment} sentiment using the feedback abo...`
- L30 `transfer_prompt_to_path`: `transfer_prompt_to_path = { "yelp-to-neg": TaskIteratePromptsNoFeedback.to_neg, "yelp-to-pos": TaskIteratePromptsNoFeedback.to_pos, }`
- L35 `transfer_prompt_to_path`: `transfer_prompt_to_path = { "yelp-to-neg": TaskIteratePrompts.to_neg, "yelp-to-pos": TaskIteratePrompts.to_pos, }`
- L47 `prompt`: `prompt = self.transfer_prompts["yelp-to-neg"]`

### Classes
#### Class `SentimentTransferTaskIterate` L10 bases=['Prompt']
##### `__init__(self, engine, feedback_type)` (L11)
- Inputs: function parameters `__init__(self, engine, feedback_type)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Main call graph hints: `super.__init__`, `self.load_prompts`, `super`
##### `load_prompts(self, feedback_type)` (L22)
- Inputs: function parameters `load_prompts(self, feedback_type)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
- Loops:
  - L40: {'line': 40, 'type': 'for', 'target': '(task_id, prompt_path)', 'iter': 'transfer_prompt_to_path.items()', 'body_len': 1, 'orelse_len': 0}
- Decisions / conditions:
  - L24: IF `feedback_type == 'something-is-wrong'`; body=1 else=1
  - L29: IF `feedback_type == 'none'`; body=1 else=1
- Main call graph hints: `dict`, `transfer_prompt_to_path.items`
##### `make_query(self, question, target_sentiment)` (L43)
- Inputs: function parameters `make_query(self, question, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L51: `f'{prompt}{self.question_prefix}{question}{self.intra_example_sep}{self.answer_prefix}'`
- Decisions / conditions:
  - L44: IF `'positive' in target_sentiment.lower()`; body=1 else=1
  - L46: IF `'negative' in target_sentiment.lower()`; body=1 else=1
- Raises:
  - L49: `ValueError(f'Invalid target_sentiment {target_sentiment}')`
- Main call graph hints: `target_sentiment.lower`, `ValueError`
##### `make_input(self, review, sentiment, transferred_reviews_history, feedback_history, target_sentiment)` (L56)
- Inputs: function parameters `make_input(self, review, sentiment, transferred_reviews_history, feedback_history, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L85: `input_txt`
- Loops:
  - L66: {'line': 66, 'type': 'for', 'target': '(i, (transferred_review, transferred_review_sentiment))', 'iter': 'enumerate(transferred_reviews_history)', 'body_len': 3, 'orelse_len': 0}
- Decisions / conditions:
  - L67: IF `self.feedback_type in ['none', 'something-is-wrong']`; body=1 else=0
- Main call graph hints: `enumerate`, `self.inter_example_sep.join`, `examples.append`
##### `__call__(self, review, sentiment, transferred_reviews_history, feedback_history, target_sentiment)` (L87)
- Inputs: function parameters `__call__(self, review, sentiment, transferred_reviews_history, feedback_history, target_sentiment)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L143: `(_get_last_non_empty_line(transferred_input).strip(), logprobs)`
  - L100: `transferred_input`
- Decisions / conditions:
  - L122: IF `self.engine not in ['gpt-3.5-turbo', 'gpt-4']`; body=1 else=0
  - L129: IF `'logprobs' in transferred_input['choices'][0]`; body=1 else=0
  - L136: IF `target_sentiment in transferred_input and ':' in transferred_input`; body=1 else=1
  - L141: IF `':' in transferred_input`; body=1 else=0
- Exception handling:
  - L137: handlers=['IndexError'] finalbody_len=0
- LLM/API calls:
  - L125: `router.call`
- Main call graph hints: `self.make_input`, `self.make_query`, `router.call`, `router.get_first_response`, `input_str.split`, `np.array.mean`, `_get_last_non_empty_line.strip`, `transferred_input.split[...].strip`, `np.array`, `_get_last_non_empty_line`, `line.strip`, `transferred_input.split`
#### Class `TaskIteratePrompts` L161 bases=[]
#### Class `TaskIteratePromptsSomethingIsWrong` L278 bases=[]
#### Class `TaskIteratePromptsNoFeedback` L364 bases=[]

### Functions
- None

---

## File: `src/utils.py`

**Lines:** 48  

### Imports
- `import traceback`

### Module-level assignments
- None

### Prompt-like assignments
- L15 `intra_example_sep`: `self.intra_example_sep = intra_example_sep`
- L16 `inter_example_sep`: `self.inter_example_sep = inter_example_sep`

### Classes
#### Class `Prompt` L3 bases=[]
##### `__init__(self, question_prefix, answer_prefix, intra_example_sep, inter_example_sep, engine, temperature)` (L4)
- Inputs: function parameters `__init__(self, question_prefix, answer_prefix, intra_example_sep, inter_example_sep, engine, temperature)` plus object fields/global config/prompt files as referenced.
- Outputs / returns: implicit `None` unless side effects.
##### `make_query(self, prompt, question)` (L20)
- Inputs: function parameters `make_query(self, prompt, question)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L21: `f'{prompt}{self.question_prefix}{question}{self.intra_example_sep}{self.answer_prefix}'`

### Functions
#### `retry_parse_fail_prone_cmd(func, max_retries, exceptions)` (L26)
- Inputs: function parameters `retry_parse_fail_prone_cmd(func, max_retries, exceptions)` plus object fields/global config/prompt files as referenced.
- Outputs / returns:
  - L47: `wrapper`
  - L45: `None`
  - L39: `func(*args, **kwargs)`
- Loops:
  - L37: {'line': 37, 'type': 'while', 'test': 'retries', 'body_len': 1, 'orelse_len': 0}
- Exception handling:
  - L38: handlers=['exceptions'] finalbody_len=0
- Main call graph hints: `func`, `traceback.format_exc`, `print`