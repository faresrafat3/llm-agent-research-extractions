# فحص الشمولية النهائي — AI Scientist v2 Extraction

## النطاق

تمت مراجعة AI Scientist v2 من المصدر:

- Repository: `https://github.com/SakanaAI/AI-Scientist-v2`
- Audited commit: `96bd51617cfdbb494a9fc283af00fe090edfae48`

## أرقام التغطية

- Python files mapped: 38.
- Prompt entries extracted: 72.
- Main logic report lines: أكثر من 5000 سطر.
- Mermaid graphs: English + Arabic.
- Graph-vs-code gap audit: موجود.

## الملفات الناتجة

### Root files

- `README.md`
- `research_summary.md`
- `deep_dive_task_matrix.md`
- `ai_scientist_v2_prompts_complete.md`
- `audit_summary.txt`
- `final_completeness_check_ar.md`

### Logic/flow package

- `logic_flow_extract/README.md`
- `logic_flow_extract/prompts_complete.md`
- `logic_flow_extract/python_logic_flow_complete.md`
- `logic_flow_extract/python_logic_inventory.json`
- `logic_flow_extract/graph_english.mmd`
- `logic_flow_extract/graph_english.md`
- `logic_flow_extract/graph_arabic.mmd`
- `logic_flow_extract/graph_arabic.md`
- `logic_flow_extract/graph_gap_audit.md`
- `logic_flow_extract/final_work_review_ar.md`

## ما يغطيه استخراج prompts

- Ideation prompts.
- Semantic Scholar tool description.
- FinalizeIdea tool description.
- Experiment/BFTS prompts.
- Debug prompts.
- Improvement prompts.
- Hyperparameter tuning prompts.
- Ablation prompts.
- Metric parsing prompts.
- Plotting prompts.
- VLM feedback prompts.
- Stage completion/progression schemas.
- Summarization prompts.
- Plot aggregation prompts.
- Citation gathering prompts.
- Writeup prompts.
- Writeup reflection prompts.
- ICBINB-specific prompts.
- VLM figure/caption/page-limit prompts.
- Peer review prompts.
- Meta-review prompts.

## ما يغطيه logic extraction

تم تحليل كل ملفات Python لاستخراج:

- classes/functions.
- loops.
- conditions.
- returns.
- raises.
- try/except.
- LLM/VLM calls.
- I/O/subprocess/network calls.
- prompt-like assignments.

## أهم loops المغطاة

- ideation generation/reflection loops.
- AgentManager main-stage loop.
- substage loop.
- node processing loop.
- ParallelAgent worker loop.
- plan/code retry loop.
- hyperparameter/ablation retry loops.
- multi-seed evaluation loop.
- metric parsing/plotting loops.
- plot aggregation reflection loop.
- citation loop up to 20 rounds.
- writeup retry/reflection loops.
- VLM figure selection/reflection loops.
- peer review reflection/ensemble loops.
- cleanup process loops.

## أهم decision points

- SearchSemanticScholar vs FinalizeIdea.
- parse failure vs valid JSON.
- load code / dataset reference decisions.
- stage completion vs continue.
- substage completion vs continue.
- debug probability and debug depth.
- draft/debug/improve/hyperparameter/ablation branch.
- code parsed vs parsing feedback.
- buggy execution vs valid output.
- metrics valid vs WorstMetricValue.
- plot exists vs skip VLM.
- cached citations vs gather.
- no more citations vs continue.
- normal vs ICBINB writeup.
- skip writeup/review.
- final/highest/fallback PDF review selection.

## Graph quality

تمت مقارنة الرسم بالكود وإضافة النواقص في:

- `logic_flow_extract/graph_gap_audit.md`

الرسوم الحالية تغطي المسار end-to-end وتشير إلى كل المراحل الكبرى والقرارات الأساسية.

## حدود النتيجة

- الرسم Mermaid عالي المستوى حتى يظل قابلًا للقراءة والرندر.
- التفاصيل الدقيقة لكل function موجودة في `python_logic_flow_complete.md` و JSON inventory.
- بعض prompts runtime/dict/list يتم حفظ source expression لها بدل النص النهائي بعد التعبئة، لأن النص النهائي يعتمد على بيانات التجربة.

## الخلاصة

الحزمة الحالية شاملة ومنظمة، وتغطي AI Scientist v2 كمنظومة prompts + logic + graph + review بشكل متكامل.