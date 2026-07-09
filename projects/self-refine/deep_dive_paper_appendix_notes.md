# Self-Refine — Paper Appendix / Evaluation Deep Dive Notes

This file records high-value details found in the paper beyond the core algorithm and maps them to the extraction package.

## Algorithmic details from paper

The paper defines Self-Refine with:

```text
Require: input x, model M, prompts {p_gen, p_fb, p_refine}, stop condition stop(.)
y0 = M(p_gen || x)
for iteration t in 0,1,...:
    fb_t = M(p_fb || x || y_t)
    if stop(fb_t,t): break
    else: y_{t+1} = M(p_refine || x || y0 || fb0 || ... || y_t || fb_t)
return y_t
```

Key design points:

- Feedback should be **actionable**: it suggests concrete changes.
- Feedback should be **specific**: it points to concrete parts of the current output.
- Refinement uses history so the model can avoid repeating old mistakes.
- Stop can be max iteration or feedback-derived indicator.
- No supervised training, no RL, no separate refiner model.

## Tasks evaluated in paper

The paper evaluates seven task types:

1. Dialogue response generation.
2. Code optimization.
3. Code readability improvement.
4. Math reasoning.
5. Sentiment reversal.
6. Acronym generation.
7. Constrained generation / CommonGen-Hard.

The repository contains code/data/prompt artifacts for these task families.

## Paper-level limitations

The paper explicitly notes:

- Requires a base model with enough instruction-following/few-shot ability.
- Experiments used non-open-source models such as GPT-3.5, ChatGPT, GPT-4, CODEX.
- English-only experiments.
- Potential misuse: prompting can steer models toward toxic/harmful text; Self-Refine does not explicitly guard against this.

## Failure/analysis findings

The paper's qualitative analysis identifies failure modes:

- Incorrect feedback.
- Generic feedback.
- Incorrect scoring.
- Refiner ignores feedback.
- Refiner introduces new problems.
- Feedback identifies wrong error location.
- Feedback suggests inappropriate fix.

Important observation:

- Most failures come from bad feedback rather than the refiner failing to apply good feedback.
- Refiner can sometimes be robust to partially incorrect feedback.

## Iteration behavior

The paper reports:

- Output quality usually improves over iterations.
- Gains are often largest in early iterations.
- Improvement is not always monotonic, especially for multi-aspect tasks like acronym generation.
- For multi-aspect tasks, scores can help select the best output across iterations.

## Feedback ablations

The paper compares:

- Self-Refine feedback: specific/actionable.
- Generic feedback.
- No feedback.

Conclusion:

- Specific/actionable feedback performs best.
- Generic feedback helps somewhat.
- No feedback is weakest.

Repository mapping:

- PIE has `feedback_type == naive` and `feedback_type == none` branches.
- PIE chooses `iterate_genericfb.txt` or `iterate_nofb.txt` accordingly.
- This directly implements feedback ablations.

## Oracle feedback

The paper notes that GSM math gains are limited when the model cannot identify its own math errors. Oracle correctness feedback improves math refinement.

Repository mapping:

- GSM code stops if feedback says `it is correct`.
- GSM feedback quality is therefore central to whether refinement improves performance.

## Mixed refine

The paper discusses using a weaker model for initialization and a stronger model for feedback/refinement.

Repository mapping:

- The code is written with `ENGINE` constants and prompt classes, so engines can be swapped per task, although many scripts hard-code defaults.

## GPT-4 evaluation prompts from paper/code

### Sentiment Reversal GPT-4 evaluation

The paper and `src/sentiment_reversal/gpt4_eval.py` include an A/B evaluation prompt:

```text
Which review is aligned with the sentiment {target_sentiment}?
Review A: {review_a}
Review B: {review_b}.
Pick your answer from ['Review A', 'Review B', 'both', 'neither'].
Generate a short explanation for your choice first.
Then generate 'The more aligned review is A' or ...
Format: <explanation> <answer> STOP
```

Implementation details:

- Randomly flips A/B to reduce position bias.
- Normalizes A/B labels back after response if flipped.
- Uses GPT-4, temperature 0, stop token `STOP`.

### Acronym Generation GPT-4 evaluation

Paper listing asks:

```text
Title: {title}
Acronym A: {acronym_a}
Acronym B: {acronym_b}
Pick the better acronym for the given title.
Compare based on pronunciation, spelling, relation to title, positive connotation.
```

### Dialogue Response GPT-4 evaluation

Paper listing asks:

```text
Which response is better given this context: {context}?
Response A: {response_a}
Response B: {response_b}
Pick from Response A/B/both/neither.
Generate explanation then final answer.
```

## Code Readability appendix

The paper states code readability uses:

- FEEDBACK: ask an LLM for readability critique.
- REFINE: ask code generator LLM to fix code using critique.
- N = 5 iterations.
- critique temperatures 0.0 and 0.7.
- editor temperature 0.0.

Repository mapping:

- `src/readability/prompts.py` includes `PROMPT_CRITIQUE` and `PROMPT_FIX`.
- `src/readability/readability.py` runs critique/fix loop over code examples.
- metrics are measured by comment count, function count, meaningful variable ratio.

## Visual Self-Refine extension

The repository includes a later visual extension in the notebook, not in the original paper's main implementation:

- GPT-4 creates initial TikZ code.
- GPT-4V sees image + code and refines.
- The loop is analogous to Self-Refine but feedback/refinement is visual and multimodal.

This was added to the package in `visual_self_refine_notebook_audit.md` and the Mermaid graphs.
