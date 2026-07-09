# Self-Refine — Research / Paper Summary

Paper: `Self-Refine: Iterative Refinement with Self-Feedback`  
ArXiv: https://arxiv.org/abs/2303.17651  
Code: https://github.com/madaan/self-refine  
Audited code commit: `9a206d41e5d2d0c241bb441f41eeadb945afaa55`

## Core idea

Self-Refine is a test-time iterative refinement framework. The same LLM acts as:

1. generator: produces an initial output,
2. feedback provider: critiques the current output,
3. refiner: edits/improves the output using the feedback.

It needs no supervised training, no model updates, no RL, and no separate feedback model.

## Algorithm from the paper

Inputs:

- input `x`,
- model `M`,
- prompts `{p_gen, p_fb, p_refine}`,
- stop condition `stop(.)`.

Flow:

1. `y0 = M(p_gen || x)`.
2. For iteration `t = 0,1,...`:
   - `fb_t = M(p_fb || x || y_t)`.
   - if `stop(fb_t, t)` then break.
   - else `y_{t+1} = M(p_refine || x || y0 || fb0 || ... || y_t || fb_t)`.
3. Return latest `y_t`.

## Stop conditions

The paper describes two stop styles:

- fixed maximum iteration/time-step,
- task-specific stopping indicator extracted from feedback.

The code implements variants such as:

- stop when max attempts is reached,
- stop CommonGen when both concept and commonsense feedback are `none`,
- stop GSM when feedback contains `it is correct`,
- stop based on task-specific run exhaustion for sentiment/response/code tasks.

## Task families in the repository

- Acronym generation.
- CommonGen constrained generation.
- GSM math reasoning.
- PIE code optimization.
- Dialogue response generation.
- Sentiment reversal.
- Code readability evaluation/improvement.

## Value extracted

See:

- `prompts_complete.md` for all prompt files and Python prompt templates.
- `python_logic_flow_complete.md` for per-file logic, loops, conditions, and inputs/outputs.
- `graph_english.mmd` and `graph_arabic.mmd` for visual flow graphs.


## Visual Self-Refine Notebook

The repository also includes `colabs/Visual-Self-Refine-GPT4V.ipynb`, which extends the idea to visual/TikZ refinement:

- GPT-4 generates initial TikZ/LaTeX code.
- The code is rendered into an image.
- GPT-4V receives the image plus current code and produces a refined LaTeX block.
- The loop runs for `n_refine_loop`, with early stopping on missing rendered images or too many exceptions.
- A separate `fix_latex` prompt repairs LaTeX errors from compilation logs.
