# OPRO — Complete Prompt / Meta-Prompt Extraction

Source of truth: `opro/optimization/opt_utils.py`, `optimize_linear_regression.py`, `optimize_tsp.py`, `evaluation/eval_utils.py`  
Commit: `a76bdce2cbf6d4a0d1e570a6fcfe17be9c2abdd7`

OPRO has **no separate prompts/*.txt folder**. Templates are **assembled in code** as meta-prompts and task prompts.

---

## 1. Instruction optimization meta-prompts (`gen_meta_prompt`)

### 1.1 GPT family — old-instruction header (`instruction_pos != A_begin`)

```text
Your task is to generate the instruction <INS>.
Below are some previous instructions with their scores.
The score ranges from 0 to 100.
```

### 1.2 GPT family — A_begin header

```text
Your task is to generate the answer starting sentence <Start>.
Below are some previous starting sentences with their scores.
The score ranges from 0 to 100.
```

### 1.3 text-bison — old-instruction header

```text
I have some texts along with their corresponding scores.
The texts are arranged in ascending order based on their scores,
where higher scores indicate better quality.
```

### 1.4 Instruction–score body (`gen_ins_and_score_pairs_substr`)

For each kept (instruction, score) after sort by score, threshold, and `max_num_instructions`:

```text
text:
{instruction}
score:
{score_to_show}
```

`score_to_show` is either `round(score, 3)` or bucketized integer.

### 1.5 Few-shot exemplar part (optional)

**GPT:**
```text
Below are some problems.
```
Then per example (depending on `instruction_pos` / `include_qa`):
```text
input:
Q: <INS>
{question}
A:
Ground truth answer:
{true_answer}
```
(variants: `<INS>` before Q, at Q end, or `A: <Start>` for A_begin; or `Problem:` without Q/A).

**text-bison:**
```text
The following exemplars show how to apply your text: you replace
<INS> in each input with your text, then read the input and give
an output. We say your output is wrong if your output is
different from the given output, and we say your output is
correct if they are the same. When replacing <INS> with an old
piece of text above, we get wrong outputs on the following
inputs.
```
Then `input:` / `output:` blocks with true answers.

Order: either instructions-before-exemplars or reverse (`instructions_before_exemplars`).

### 1.6 GPT closing instruction (not A_begin)

```text
Generate an instruction that is different from all the instructions <INS> above,
and has a higher score than all the instructions <INS> above.
The instruction should begin with <INS> and end with </INS>.
The instruction should be concise, effective,
and generally applicable to all problems above.
```

### 1.7 GPT closing (A_begin)

```text
Generate a starting sentence that is different from all the
<Start> sentences above, and has a higher score than all the
<Start> sentences above. The starting sentence should begin with
<Start> and end with </Start>. The starting sentence should be
concise, effective, and generally applicable to all QA pairs above.
```

### 1.8 text-bison closing

```text
Write your new text that is different from the old ones and
has a score as high as possible. Write the text in square brackets.
```

### 1.9 `instructions_only` meta type

Builds a compact meta-instruction:

```text
Create a piece of text {at the beginning of the question | at the end of the question | at the beginning of the answer}
to improve the accuracy of a model solving {grade school math | task_name | bbh task words} problems.
```

Plus scored history and a request for a new higher-scoring text (implementation continues in `gen_meta_prompt` branch).

---

## 2. Scorer task prompts (`eval_utils.gen_prompt`)

Places the candidate instruction relative to the question:

| `instruction_pos` | Pattern (include_qa=True) |
|---|---|
| `before_Q` | `{instruction}\nQ: {question}\n\nA:` |
| `Q_begin` | `Q: {instruction}\n{question}\n\nA:` |
| `Q_end` | `Q: {question}\n{instruction}\n\nA:` |
| `A_begin` | `Q: {question}\n\nA: {instruction}` |

Without QA markers (`include_qa=False`): only `Q_begin` / `Q_end` styles with bare question text.

Datasets: mmlu, bbh, gsm8k, multiarith, aqua (formatting helpers for MMLU/AQuA choices).

Optional second-pass extraction: append style “So the final answer is” when `extract_final_answer_by_prompting_again`.

---

## 3. Linear regression meta-prompt

```text
Now you will help me minimize a function with two input variables w, b.
I have some (w, b) pairs and the function values at those points.
The pairs are arranged in descending order based on their function values,
where lower values are better.

input:
w={w}, b={b}
value:
{z}
...

Give me a new (w, b) pair that is different from all pairs above,
and has a function value lower than any of the above. Do not write code.
The output must end with a pair [w, b], where w and b are numerical values.
```

Parse: last suitable `[...]` without `=` that looks like a numeric pair.

---

## 4. TSP meta-prompt

History of traces with lengths, then:

```text
Give me a new trace that is different from all traces above,
and has a length lower than any of the above.
The trace should traverse all points exactly once.
The trace should start with '<trace>' and end with </trace>.
```

---

## 5. Default initial instructions (instruction opt)

From `optimize_instructions.py` (editable):

```python
initial_instructions = [
  "Let's solve the problem.",
]
```

---

## 6. Prompt history artifacts (`misc/prompt_history/`)

Paper optimization logs, e.g.  
`BBH-boolean_expressions-s-text-bison-o-palm-2-l-it.txt`:

```text
Step -1, training acc: 0.800, instruction: ...
Step 0, training acc: 0.880, instruction: ...
```

Documented in `misc/prompt_history/README.md` (Figures 6, 23, 24; best prompts Table 9).

---

## 7. Wiring map

| Template / assembly | Built in | Consumed by |
|---|---|---|
| Meta-prompt (instruction) | `gen_meta_prompt` | optimizer LLM in `run_evolution` |
| Task prompt with instruction | `gen_prompt` | scorer LLM in `evaluate_single_instruction` |
| LR / TSP meta-prompts | `optimize_linear_regression` / `optimize_tsp` | optimizer LLM |
| API call wrappers | `prompt_utils` | both optimizer and scorer |

## 8. Extraction tags for parsing optimizer outputs

| Optimizer | Extract |
|---|---|
| GPT + not A_begin | between `<INS>` and `</INS>` |
| GPT + A_begin | between `<Start>` and `</Start>` |
| text-bison | square brackets `[...]` via `extract_string_in_square_brackets` / `parse_tag_content` |
