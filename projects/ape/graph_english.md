# APE — English Mermaid Graph

```mermaid
flowchart TD
  A[Start APE find_prompts] --> B[Load eval_template / demos_template / prompt_gen_data]
  B --> C{prompt_gen_template is None?}
  C -->|Yes| D[Convert eval_template to GenerationTemplate]
  C -->|No| E[Use provided GenerationTemplate]
  D --> F[Generate prompts]
  E --> F
  F --> G[Subsample demos loop: num_subsamples]
  G --> H[Build generation query: fill [INPUT][OUTPUT][full_DEMO]]
  H --> I[LLM generate_text n=num_prompts_per_subsample]
  I --> J[Deduplicate prompts set()]
  J --> K[Evaluate prompts]
  K --> L{eval_method?}
  L -->|likelihood| M[Likelihood scoring loop: prompts x samples]
  L -->|bandits| N[UCB bandit rounds loop]
  M --> O[Rank prompts by mean logprob]
  N --> O
  O --> P[Return EvaluationResult + demo_fn]
  P --> Q[End]
```
