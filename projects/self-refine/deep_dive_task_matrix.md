# Self-Refine — Deep Dive Task Matrix

This document maps the Self-Refine paper algorithm to the concrete repository implementation task by task.

## Universal paper algorithm

| Stage | Paper symbol | Meaning | Repository implementation pattern |
|---|---|---|---|
| Input | `x` | task input | title, concepts, question, slow code, context, review, object name |
| Initial generation | `p_gen`, `y0` | first draft | `task_init(...)`, `get_initial_latex(...)`, readability original code |
| Feedback | `p_fb`, `fb_t` | critique/scoring | `feedback.py`, GPT/FED feedback, readability critique, VLM image critique |
| Stop check | `stop(fb_t,t)` | max iterations or feedback indicator | `max_attempts`, `none`, `it is correct`, `this code is not slow`, exception budget |
| Refine | `p_refine`, `y_{t+1}` | improved output | `task_iterate(...)`, updated solution, edited code, revised response, new TikZ code |
| History | `y0, fb0, ...` | avoid repeated mistakes | task histories: `sent_to_fb`, `feedback_history`, `transferred_reviews_history`, acronym-score history, logs |
| Output | `y_t` | final refined output | JSONL logs, final row fields, generated code/text, visual results |

---

## 1. Acronym Generation

### Files

- `src/acronym/run.py`
- `src/acronym/task_init.py`
- `src/acronym/feedback.py`
- `src/acronym/task_iterate.py`
- `data/prompt/acronym/init.jsonl`
- `data/prompt/acronym/feedback.jsonl`

### Inputs

- `title: str`
- `max_attempts: int`
- prompt examples from JSONL.

### Initial generation

`AcronymGenTaskInit.__call__(title)` builds a query from few-shot acronym examples and the user title, then calls `OpenaiAPIWrapper.call`.

### Feedback

`AcronymGenFeedback.__call__(title, acronym)` asks the LLM to produce multi-aspect scores, including:

- Ease of pronunciation.
- Ease of spelling.
- Relation to title.
- Positive connotation.
- Well-known.
- Total score.

### Loop

`while n_attempts < max_attempts`.

- attempt 0: generate acronym from title.
- attempt > 0: call `AcronymGenTaskIterate` with `acronyms_to_scores` history.
- get feedback.
- parse `Total score: X/Y`.
- append to `all_acronyms_to_scores`.

### Decision points

- `if n_attempts == 0`: init vs iterate.
- `if total_score >= 0`: add to history for future refinement.
- parse failures are retried by `@retry_parse_fail_prone_cmd`.

### Outputs

- dictionary mapping acronym to score/title/feedback.
- optionally JSONL output over a TSV of titles.

### Notes

The condition `total_score >= 0` always accepts valid nonnegative scores, so it is effectively a validation/history update branch rather than a quality-improvement threshold.

---

## 2. Acronym MCTS Variant

### Files

- `src/acronym/run_mcts.py`

### Inputs

- hard-coded `root_title`.
- scoring weights.
- `iterations = 4`.
- global task init/feedback/iterate objects.

### Core loop

- Generate root acronym and score.
- Generate initial children.
- For each MCTS iteration:
  1. select child recursively by UCB1.
  2. expand selected node.
  3. simulate using feedback scoring.
  4. backpropagate value.

### Loops

- `for _ in range(num_children)` initial children.
- recursive selection until leaf.
- `while current is not None` to collect ancestor history.
- `while new_acronym in expanded_nodes_cache` to avoid duplicates.
- `for _ in range(iterations)` MCTS loop.
- recursive backpropagation.

### Decision points

- no children → select current node.
- duplicate acronym → regenerate.
- parent exists → continue backpropagation.

### Outputs

- printed tree/logs.
- in-memory MCTS tree.

---

## 3. CommonGen / Constrained Generation

### Files

- `src/commongen/run.py`
- `src/commongen/task_init.py`
- `src/commongen/feedback.py`
- `src/commongen/task_iterate.py`
- `data/prompt/commongen/init.jsonl`
- `data/prompt/commongen/feedback.jsonl`
- `data/prompt/commongen/iterate.jsonl`
- `data/prompt/commongen/commongen_hard.jsonl`

### Inputs

- `concepts: List[str]`
- `max_attempts`
- prompt examples.

### Initial generation

`CommongenTaskInit` creates a sentence containing concepts.

### Feedback

`CommongenFeedback` returns two feedback fields:

- concept feedback: missing/incorrect concept use.
- commonsense feedback: plausibility issue.

### Refine

`CommongenTaskIterate` receives `sent_to_fb` history and asks the model to improve the sentence.

### Stop condition

Stop early if:

```python
concept_fb.lower() == "none" and commonsense_fb.lower() == "none"
```

Otherwise loop until `max_attempts`.

### Dataset loop

`run_iter` loops over dataframe rows; skips rows where `status == "success"` during reruns.

### Output

- list `sent_to_fb`.
- JSONL output with status and histories.
- versioned output paths avoid overwrites.

---

## 4. GSM Math Reasoning

### Files

- `src/gsm/run.py`
- `src/gsm/task_init.py`
- `src/gsm/feedback.py`
- `src/gsm/feedback_no_update.py`
- `data/prompt/gsm/init.txt`
- `data/prompt/gsm/feedback.txt`

### Inputs

- GSM question.
- `max_attempts`.
- `feedback_type`.
- temperature.

### Initial generation

`GSMInit` produces a Python `solution()` program.

### Feedback/refine

`GSMFeedback` returns:

```python
{"solution": improved_soln, "feedback": feedback}
```

It parses model output by splitting around `def solution():`.

### Stop condition

Stop if:

```python
"it is correct" in feedback.lower()
```

Otherwise set:

```python
solution = improved_solution
```

and continue.

### Decisions

- `feedback_type == "naive"` raises `NotImplementedError`.
- exceptions during row processing are swallowed in `fix_gsm`.

### Outputs

- `run_logs`.
- `generated_answer_ours` from final improved solution.
- `generated_answer_direct` from first solution.
- JSONL output.

---

## 5. PIE Code Optimization

### Files

- `src/pie/run.py`
- `src/pie/task_init.py`
- `src/pie/feedback.py`
- `src/pie/task_iterate.py`
- `src/pie/pie_eval.py`
- `data/prompt/pie/init.txt`
- `data/prompt/pie/feedback.txt`
- `data/prompt/pie/iterate.txt`
- `data/prompt/pie/iterate_genericfb.txt`
- `data/prompt/pie/iterate_nofb.txt`

### Inputs

- slow program code.
- max attempts.
- feedback type: `rich`, `naive`, `none`, etc.
- temperature.

### Initial generation

`PieInit` produces a faster code candidate.

### Feedback variants

- `naive`: hard-coded feedback `It could be faster`, uses `iterate_genericfb.txt`.
- `none`: empty feedback, uses `iterate_nofb.txt`.
- default/rich: `PieFeedback` with `feedback.txt`.

### Loop

`while n_attempts < max_attempts`:

- attempt 0: init faster code.
- later: `PieIterate(slow_code, feedback)`.
- feedback is generated on the current fast code.
- log slow_code, fast_code, feedback.

### Stop condition

Stop if feedback contains:

```python
"this code is not slow"
```

Otherwise:

```python
slow_code = fast_code
```

### Output

- list of attempt logs.
- JSONL output.
- periodic backups every 20 rows.
- output filename versioning if exists.

---

## 6. Dialogue Response Generation

### Files

- `src/responsegen/run.py`
- `src/responsegen/task_init.py`
- `src/responsegen/feedback.py`
- `src/responsegen/task_iterate.py`
- `data/prompt/responsegen/init.jsonl`
- `data/prompt/responsegen/feedback.jsonl`
- `data/prompt/responsegen/fed_data.json`

### Inputs

- dialogue context.
- max attempts.
- output size.
- prompt examples and FED data.

### Initial generation

`ResponseGenTaskInit` generates an initial response.

### Feedback

`ResponseGenFeedback` uses a prompt constructed from examples and may score response qualities.

### Iterate

`ResponseGenTaskIterate` constructs an improvement prompt from previous responses and feedback.

### Loop

The run code maintains response-to-score/history structures and iterates until max attempts.

### Decisions

- parse failures are handled by retry decorator.
- dataset row errors return `FAILED` entries.
- pandarallel processes examples in parallel.

### Outputs

- JSONL output file.
- response histories.
- raw OpenAI outputs and parsed generations.

---

## 7. Sentiment Reversal

### Files

- `src/sentiment_reversal/run.py`
- `src/sentiment_reversal/task_init.py`
- `src/sentiment_reversal/task_iterate.py`
- `src/sentiment_reversal/feedback.py`
- `src/sentiment_reversal/measure.py`
- `src/sentiment_reversal/gpt4_eval.py`

### Inputs

- review.
- original sentiment.
- target sentiment.
- max attempts.
- feedback type.

### Initial transfer

Task init rewrites review toward target sentiment.

### Measurement

`measure.py` classifies/estimates transferred review sentiment.

### Feedback

Feedback compares original, target, transferred review, and measured sentiment.

### Refine

`task_iterate.py` uses:

- original review.
- sentiment.
- target sentiment.
- transferred review history.
- feedback history.

### Loop

`while n_attempts < max_attempts`.

### Decision points

- attempt 0 vs later attempts.
- feedback type may be `none`, `something-is-wrong`, etc.
- if feedback lacks `Try again` and feedback type is not disabled, append explicit retry instruction.
- output path versioning.
- filter dataset to target sentiment containing positive.

### Outputs

- JSONL logs with attempts.
- transferred review.
- measured sentiment.
- feedback.
- log probabilities.

### GPT-4 evaluation

`gpt4_eval.py` includes an A/B prompt:

- system: expert in writing reviews.
- user asks which review better aligns with target sentiment.
- random flip prevents position bias.
- output normalized back if flipped.

---

## 8. Code Readability

### Files

- `src/readability/readability.py`
- `src/readability/prompts.py`
- `src/readability/utils.py`
- `src/readability/count_comment.py`
- `src/readability/count_function.py`
- `src/readability/count_meaningful_var.py`

### Prompts

`src/readability/prompts.py` defines:

- `COUNT_VAR_PROMPT`: few-shot variable-name meaningfulness extraction.
- `PROMPT_CRITIQUE`: ask for one readability suggestion.
- `PROMPT_FIX`: ask to fix code using suggestion.

### Loop

Readability task recursively critiques and edits code for a configured number of iterations in paper methodology; code utilities run call_gpt and evaluate metrics.

### Outputs

- improved code.
- meaningful variable ratio.
- comment count ratio.
- function count.

---

## 9. Visual Self-Refine GPT-4V Notebook

### Files

- `colabs/Visual-Self-Refine-GPT4V.ipynb`
- documented in `visual_self_refine_notebook_audit.md`.

### Inputs

- `object_name`.
- `n_refine_loop`.
- OpenAI API key.

### Initial generation

`get_initial_latex` prompt asks GPT-4 to generate self-contained TikZ/LaTeX code for a simple object.

### Visual feedback/refine

- render current code to base64 image.
- send image plus current code to GPT-4V.
- `get_refinement_prompt` asks the model to understand current picture, think how it can be improved, and rewrite TikZ code.

### Repair path

`fix_latex` receives error log and buggy LaTeX, asks GPT-4 to return fixed code.

### Loop

`for i in range(n_refine_loop)`.

### Stop/error conditions

- break if rendered image is unavailable.
- allow `num_exceptions_ok = 2` exceptions before breaking.

### Outputs

- `results` list of refined code and responses.
- visual progression of generated diagrams.

---

## 10. Docs / Website Examples

### Files

- `docs/index.html`
- `docs/commongen_init.txt`
- `docs/commongen_feedback.txt`
- `docs/commongen_iterate.txt`

### Content

The website includes:

- conceptual pseudocode for `self_refine(prompt)`.
- `is_refinement_sufficient` stop concept.
- prompt examples and displayed input/feedback/refinement examples.

### Why included

Although website examples are not Python runtime code, they are valuable explanatory prompt examples and were copied/audited after review.

---

## 11. Cross-cutting implementation mechanisms

### Prompt base class

`src/utils.py` defines `Prompt`, with:

- `question_prefix`
- `answer_prefix`
- `intra_example_sep`
- `inter_example_sep`
- engine
- temperature
- `make_query(prompt, question)`

### Retry decorator

`retry_parse_fail_prone_cmd` retries functions up to 3 times for:

- `ValueError`
- `KeyError`
- `IndexError`

If all retries fail, returns `None`.

### OpenAI backend

The code uses `prompt_lib.backends.openai_api.OpenaiAPIWrapper.call` for most task implementations.

### Stop tokens

Common stop tokens:

- `###`
- `### END`
- task-specific inter-example separator.
- `STOP` in GPT-4 evaluation.

---

## 12. Deep conclusions

Self-Refine in this repository is not one monolithic implementation. It is a collection of task-specific instantiations of the same abstract algorithm:

1. produce a first candidate,
2. critique it,
3. improve it using the critique,
4. maintain history when useful,
5. stop by max attempts or task-specific signal.

The implementation value is in the prompt engineering and parsing logic for each task, not in a shared central SelfRefine class.
