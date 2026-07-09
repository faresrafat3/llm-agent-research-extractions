# APE — Deep Dive Task Matrix

| Stage | Function | Input | Output | Loop | Decision | Condition |
|---|---|---|---|---|---|---|
| Template init | `EvalTemplate.__init__` | template str | EvalTemplate | no | no | — |
| Gen template convert | `EvalTemplate.convert_to_generation_template` | eval_template | GenerationTemplate | no | no | replace [PROMPT]→[APE] |
| Prompt generation | `generate_prompts` | prompt_gen_template, demos_template, data, config | prompts[] | yes: num_subsamples | no | subsample_data each iteration |
| Deduplication | `find_prompts` | prompts[] | unique prompts[] | no | no | set() |
| Evaluation dispatch | `evalute_prompts` | prompts, eval_template, … method | EvaluationResult | — | yes | method == likelihood / bandits |
| Likelihood eval | `likelihood_evaluator` | prompts, eval_data | LikelihoodEvaluationResult | yes: prompts × samples | yes | model scoring |
| Bandit eval | `bandits_evaluator` | prompts, … | BanditsEvaluationResult | yes: rounds | yes | UCB choose |
| Ranking | `EvaluationResult.sorted` | scores | sorted prompts | yes: sort | no | descending |
| Demo inference | `demo_function` | prompt, inputs | outputs | yes: inputs | yes | list normalize |
| Cost estimation | `estimate_cost` | config, data | cost float | yes: queries | yes | eval_method bandits? |

Operational notes in Arabic and English included in final_completeness_check_ar.md
