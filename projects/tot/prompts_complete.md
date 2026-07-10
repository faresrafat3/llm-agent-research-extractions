# Tree of Thoughts — Complete Prompt Extraction

Source of truth: `src/tot/prompts/{game24,text,crosswords}.py`  
Commit: `8050e67d0e3a0fddc424d7fa5801538722a4c4cc`

---

## 1. Game of 24 prompts (`prompts/game24.py`)

### 1.1 `standard_prompt` (5-shot IO)

```text
Use numbers and basic arithmetic operations (+ - * /) to obtain 24.
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24
... (5 examples) ...
Input: {input}
```

**Use:** naive/baseline IO; also available via `standard_prompt_wrap`.

### 1.2 `cot_prompt` (5-shot step-by-step)

```text
Use numbers and basic arithmetic operations (+ - * /) to obtain 24.
Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
... (5 examples) ...
Input: {input}
```

**Use:** CoT baseline; also final-answer generation when `left: 24` in propose path.

### 1.3 `propose_prompt` (1-shot next-step generator)

```text
Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
...
Input: {input}
Possible next steps:
```

**Use:** ToT generation with `method_generate=propose`.  
`{input}` is **current remaining numbers**, not the original puzzle (via `get_current_numbers`).

### 1.4 `value_prompt` (few-shot state value)

```text
Evaluate if given numbers can reach 24 (sure/likely/impossible)
10 14
10 + 14 = 24
sure
11 12
...
impossible
...
{input}
```

**Use:** intermediate state evaluation (`method_evaluate=value`).  
Last line label ∈ {sure, likely, impossible}.

### 1.5 `value_last_step_prompt` (answer verification)

```text
Use numbers and basic arithmetic operations (+ - * /) to obtain 24.
Given an input and an answer, give a judgement (sure/impossible) if the answer is correct,
i.e. it uses each input exactly once and no other numbers, and reach 24.
Input: ...
Answer: ...
Judge:
sure / impossible
...
Input: {input}
Answer: {answer}
Judge:
```

**Use:** when trajectory has no `left:` (final answer line).

### Value unwrap map (`Game24Task.value_outputs_unwrap`)

| Label | Numeric value |
|---|---|
| impossible | 0.001 |
| likely | 1 |
| sure | 20 |

Sum over `n_evaluate_sample` votes (last line of each sample).

---

## 2. Creative Writing prompts (`prompts/text.py`)

### 2.1 `standard_prompt`

```text
Write a coherent passage of 4 short paragraphs.
The end sentence of each paragraph must be: {input}
```

### 2.2 `cot_prompt`

```text
Write a coherent passage of 4 short paragraphs.
The end sentence of each paragraph must be: {input}

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.
```

**Stop tokens in task:** step0 → `'\nPassage:\n'`; step1 → `None` (two-step ToT: plan then passage).

### 2.3 `vote_prompt`

```text
Given an instruction and several choices, decide which choice is most promising.
Analyze each choice in detail, then conclude in the last line
"The best choice is {s}", where s the integer id of the choice.
```

Runtime wrap appends:

```text
Choice 1:
{y1}
Choice 2:
{y2}
...
```

### 2.4 `compare_prompt` (pairwise, available)

```text
Briefly analyze the coherency of the following two passages.
Conclude in the last line "The more coherent passage is 1",
"The more coherent passage is 2", or "The two passages are similarly coherent".
```

### 2.5 `score_prompt` (test-time coherency)

```text
Analyze the following passage, then at the last line conclude
"Thus the coherency score is {s}", where s is an integer from 1 to 10.
```

Used in `TextTask.test_output` with `n=5` GPT-4 samples; mean score = reward.

---

## 3. Mini Crosswords prompts (`prompts/crosswords.py`)

### 3.1 `standard_prompt` (5-shot full board)

Solves 5×5 mini crossword: 5 horizontal + 5 vertical clues → 5 rows of spaced letters.  
5 full input/output examples then `{input}` / `Output:`.

### 3.2 `cot_prompt` (5-shot with Thoughts)

Same task but intermediate:

```text
Thoughts:
h1. ...: WORD
...
v5. ...: WORD

Output:
L E T T E R S
...
```

### 3.3 `propose_prompt` (interactive ToT)

```text
Let's play a 5 x 5 mini crossword, where each word should have exactly 5 letters.

{input}

Given the current status, list all possible answers for unfilled or changed words,
and your confidence levels (certain/high/medium/low), using the format
"h1. apple (medium)". Use "certain" cautiously and only when you are 100% sure
this is the correct word. You can list more then one possible answer for each word.
```

`{input}` = `env.render()` board + Unfilled/Filled/Changed answers.

### 3.4 `value_prompt` (letter-constraint fit)

```text
Evaluate if there exists a five letter word of some meaning that fit some letter
constraints (sure/maybe/impossible).

Incorrect; to injure: w _ o _ g
...
sure
...
{input}
```

Used by `MiniCrosswordsEnv.prompt_status` and `MiniCrosswordsTask.evaluate`.

### Confidence → score (propose unwrap / DFS)

| Confidence | Score |
|---|---|
| certain | 1 |
| high | 0.5 |
| medium | 0.2 |
| low | 0.1 |

Regex: `^([hv][1-5])\. ([a-zA-Z]{5,5}) \((certain|high|medium|low)\).*$`

---

## 4. Prompt wiring map

| Prompt | Task | Called from | Phase |
|---|---|---|---|
| game24.standard | Game24 | `standard_prompt_wrap` / `get_samples` | generate / naive |
| game24.cot | Game24 | `cot_prompt_wrap` / propose last step | generate |
| game24.propose | Game24 | `propose_prompt_wrap` | generate children |
| game24.value | Game24 | `value_prompt_wrap` | evaluate intermediate |
| game24.value_last_step | Game24 | `value_prompt_wrap` | evaluate final |
| text.standard / cot | Text | sample generate | generate |
| text.vote | Text | `vote_prompt_wrap` | evaluate |
| text.score | Text | `test_output` | metric |
| text.compare | Text | available wrap | optional pairwise |
| crosswords.standard / cot | Crosswords | naive baselines | generate full |
| crosswords.propose | Crosswords | propose wrap / DFS notebook | generate actions |
| crosswords.value | Crosswords | prompt_status / evaluate | prune / value |

---

## 5. Non-prompt but prompt-adjacent strings

- Game24 step format: `a op b = c (left: ...)`
- Final answer line: `Answer: ... = 24`
- Crosswords action: `h1. apple` or `v3. tempt`
- Vote conclusion: `The best choice is {id}`
- Score conclusion: `Thus the coherency score is {s}`
- Value labels: sure / likely|maybe / impossible
