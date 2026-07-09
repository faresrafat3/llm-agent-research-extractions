# Meta-Prompting — Deep Dive Task / Flow Matrix

## Universal meta-prompting loop

| Step | Code concept | Decision | Output |
|---|---|---|---|
| Initialize | `t_init(x)` / question prefix | method/prompt file selection | initial message list |
| Meta call | `meta_model_generate` | expert call vs final answer vs error | meta model output |
| Expert dispatch | expert extractor | valid expert block? | expert name + instruction |
| Expert generation | generator settings | Python expert or normal expert | expert output |
| Python tool | `execute_code_with_timeout` | output contains `Please run this code!` | code output appended |
| Summarization | summarizer settings | num_return_sequences > 1 | summarized expert output |
| Feedback append | intermediate feedback | always after expert output | updated message log |
| Return | final answer indicator | final answer found | final message log/output |
| Error | neither expert nor final | formatting error | append error message |

## Main experiment runner

Files: `run_experiments.py`, `utils/language_model.py`, `utils/meta_scaffolding.py`.

Flow:

1. Parse CLI args.
2. Load task data from `data/{task}.jsonl`.
3. Load prompt/scaffolding config from `prompts/`.
4. Create language model wrapper.
5. Build question prefix or prompt suffix depending on method.
6. Loop over examples until `max_num`.
7. Generate output.
8. Save JSONL record to output directory.

Decisions:

- which method/prompt file is used.
- include expert name in instruction.
- fresh eyes mode.
- use Python expert or no Python expert.
- skip already existing outputs depending on output path behavior.

## MetaPromptingScaffolding

Central class in `utils/meta_scaffolding.py`. It drives recursive/iterative meta-model calls.

Key conditions:

- if counter exceeds recursion/round budget: stop.
- if meta output contains expert-call pattern: call expert.
- if meta output contains final-answer indicator: return.
- otherwise append error message and retry.
- if expert is `Expert Python` and output includes `Please run this code!`: extract and run code.
- if generated expert output is too long and extraction is enabled: replace with retry message.

## Evaluation

File: `evaluate_outputs.py`.

Flow:

1. Load outputs by directory glob.
2. Extract model answer with task-specific rules.
3. Compare with ground truth using exact match, soft match, or functional correctness.
4. Print/report accuracy.

## Data and outputs

- `data/` files are input datasets.
- `outputs/` files are historical model outputs and evaluation artifacts.
- Prompt templates live in `prompts/`.
