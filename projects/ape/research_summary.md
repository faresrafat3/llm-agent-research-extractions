# APE / Automatic Prompt Engineer — Research Summary

Paper: https://arxiv.org/abs/2211.01910  
Code: https://github.com/keirp/automatic_prompt_engineer  
Commit: eac521c79a78965245ce7745dcc9f6b0792c7ec7

## Core idea
Treat instructions/prompts as natural-language programs. Given input-output demonstrations, APE:
1. Generates candidate instructions using an LLM (forward generation).
2. Deduplicates.
3. Evaluates candidates via likelihood scoring or UCB bandits.
4. Ranks and returns best prompts + a demo function.

## Key components
- `find_prompts()` — main orchestration: template conversion, generation, dedup, evaluation, demo_fn.
- `generate_prompts()` — subsample demos, build generation queries, call LLM.
- `evaluate_prompts()` — dispatch to likelihood or bandits evaluator.
- `GenerationTemplate`, `EvalTemplate`, `DemosTemplate` — prompt templating with [APE], [PROMPT], [INPUT], [OUTPUT], [full_DEMO].
- Likelihood evaluator — computes log p(output | prompt+input).
- Bandits evaluator — UCB exploration over prompt arms.
- `simple_ape()` — user-friendly wrapper with defaults.

## Inputs / Outputs
Inputs: dataset (inputs, outputs), eval_template, demos_template, prompt_gen_template, config (models, num_prompts, eval_rounds).
Outputs: EvaluationResult (sorted prompts + scores), demo_fn(prompt, inputs) -> outputs.

## Loops
- generate_prompts: for _ in range(num_subsamples)
- likelihood_evaluator: for prompt in prompts; for i in range(num_samples)
- bandits_evaluator: for _ in range(rounds)
- UCB choose/update loops

## Decision points
- prompt_gen_template is None ? convert eval_template else use provided
- prompt_gen_mode == 'forward' ? default template else error/insert
- eval_method == 'likelihood' ? likelihood_evaluator : 'bandits' ? bandits_evaluator : error
- few_shot_data is None ? use prompt_gen_data
- num_prompts_per_round < 1 ? scale by num_prompts

## Strengths
- Automatic instruction discovery, strong zero-shot transfer, interpretable prompts.
