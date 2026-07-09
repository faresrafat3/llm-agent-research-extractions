# فحص الشمولية النهائي — LATS Extraction

## النطاق

- Paper: `https://arxiv.org/abs/2310.04406`
- Code: `https://github.com/lapisrocks/LanguageAgentTreeSearch`
- Commit: `853d81614607dd27433faf17c7b0a7d660f95d22`

## التغطية

- Python files analyzed: 50.
- Prompt/source files copied: README, index, shell commands, WebShop prompt, generator todo, sample logs.
- Data samples copied: HotPotQA and programming benchmark JSON/JSONL files.
- Outputs/root logs are treated as historical artifacts unless selected as useful examples.

## أهم الحلقات

- MCTS iteration loop.
- node selection while-loop.
- expansion/generation loops.
- value evaluation loops.
- rollout depth loop.
- backpropagation to root.
- reflection generation from failed trajectories.
- programming pass@k / max iteration loops.

## أهم القرارات

- terminal success vs failure.
- all children terminal/exhausted.
- UCT child selection.
- value cache hit.
- reflection generation threshold.
- environment done/reward.
- code tests pass/fail.
- parse/compile/runtime error.

## الخلاصة

الحزمة تغطي LATS كخوارزمية بحث شجري للغة، وتربط الورقة بالكود والبرومبتات والمهام والرسوم.
