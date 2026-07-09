# فحص الشمولية النهائي — Meta-Prompting Extraction

## النطاق

تمت مراجعة:

- Paper: `https://arxiv.org/abs/2401.12954`
- Code: `https://github.com/suzgunmirac/meta-prompting`
- Commit: `40422564938d772c3e3e6b9614b1df48b8dd6a08`

## التغطية

- Python files analyzed: 8.
- Prompt/config sources copied: all files under `prompts/` plus README and example commands.
- Data input samples copied under `raw_data_samples/`.
- Outputs are documented as historical artifacts and not copied as prompt templates.

## أهم الحلقات

- loop over dataset examples.
- recursive/iterative meta-model loop.
- expert dispatch loop via repeated calls.
- Python execution branch.
- evaluation directory/output loop.

## أهم القرارات

- prompting method selection.
- expert call vs final answer vs formatting error.
- Expert Python vs normal expert.
- run code marker present or not.
- summarize multiple expert outputs or not.
- task-specific extraction/evaluation metric.

## الخلاصة

الحزمة تغطي prompts والlogic والloops والقرارات والمخرجات والمدخلات والرسوم بشكل شامل، مع فصل outputs التاريخية عن prompt templates.
