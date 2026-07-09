# مراجعة نهائية شاملة للشغل — AI Scientist v2 Extraction

## 1. نطاق المهمة

المطلوب كان فتح ريبو:

`https://github.com/SakanaAI/AI-Scientist-v2`

واستخراج وفهم وتوثيق:

- كل الـ prompts.
- كل الـ logic والـ flow.
- كل الـ loops.
- كل الـ decisions / conditions.
- كل الـ inputs / outputs.
- كل ملفات Python.
- بناء Mermaid visual graph بنسختين: English و Arabic.
- مقارنة الرسم بالكود الفعلي وتصحيح أي نقص.
- رفع النتائج على GitHub public repo.

## 2. الريبو الناتج

تم إنشاء وتحديث الريبو العام:

`https://github.com/faresrafat3/ai-scientist-v2-prompts-extraction`

الحالة المطلوبة:

- Public: نعم.
- يحتوي على ملفات prompts.
- يحتوي على تحليل logic/flow.
- يحتوي على Mermaid graphs بالإنجليزي والعربي.
- يحتوي على gap audit بعد مقارنة الرسم بالكود.

## 3. الملفات النهائية المهمة

### في root الريبو

- `README.md`
- `ai_scientist_v2_prompts_complete.md`
- `audit_summary.txt`

### داخل `logic_flow_extract/`

- `README.md`
- `python_logic_flow_complete.md`
- `python_logic_inventory.json`
- `prompts_complete.md`
- `graph_english.mmd`
- `graph_english.md`
- `graph_arabic.mmd`
- `graph_arabic.md`
- `graph_gap_audit.md`
- `final_work_review_ar.md`

## 4. مراجعة اكتمال الـ prompts

### الحالة الحالية

ملف:

`prompts_complete.md`

يحتوي على:

- 72 prompt / schema / dynamic prompt insertion entries.
- prompts من الملفات الأساسية المطلوبة.
- prompts من BFTS و AgentManager.
- FunctionSpec schemas.
- runtime tool descriptions.
- few-shot review insertion templates.
- writeup / citations / plotting / review / VLM prompts.

### المراحل المغطاة

- Ideation.
- Semantic Scholar search أثناء ideation.
- FinalizeIdea tool.
- Experiment drafting.
- Debugging.
- Improvement/refinement.
- Hyperparameter tuning.
- Ablation studies.
- Metric parsing.
- Plot code generation.
- VLM plot feedback.
- Multi-seed aggregation.
- Stage/substage progression and completion.
- Plot aggregation.
- Citation gathering.
- Writeup generation.
- Writeup reflection.
- ICBINB VLM image/caption review.
- VLM figure selection / page-limit reflection.
- Final page-limit reflection.
- Peer review.
- Meta-review.
- Reviewer reflection.

### ملاحظات

- تم اعتبار الكود هو source of truth للنصوص الدقيقة.
- الورقة الرسمية والـ README استخدموا كـ cross-check فقط.
- بعض prompts مبنية كـ dict/list ويتم تحويلها إلى Markdown عبر `compile_prompt_to_md`، لذلك تم حفظ source expression بدل النص النهائي runtime.

## 5. مراجعة الـ logic / flow

ملف:

`python_logic_flow_complete.md`

يحتوي على تحليل AST-assisted لكل Python file، ويتضمن:

- imports.
- module-level assignments.
- classes.
- functions.
- method signatures.
- loops.
- conditions.
- returns.
- raises.
- try/except.
- LLM/VLM calls.
- I/O calls.
- subprocess/network side effects.
- prompt-like assignments.

ملف:

`python_logic_inventory.json`

هو نسخة machine-readable من نفس الاستخراج.

## 6. مراجعة الـ Mermaid graphs

### الملفات

- `graph_english.mmd`
- `graph_arabic.mmd`
- `graph_english.md`
- `graph_arabic.md`

### ما يغطيه الرسم الآن

الرسم يغطي end-to-end pipeline:

1. CLI launcher.
2. تحميل الأفكار.
3. optional code loading.
4. optional dataset reference loading.
5. config editing.
6. BFTS experiment execution.
7. AgentManager main-stage/substage loops.
8. ParallelAgent node selection.
9. Draft/debug/improve/hyperparameter/ablation branches.
10. Code generation retry.
11. Interpreter execution.
12. Bug detection.
13. Metric parsing.
14. Plot generation.
15. VLM plot feedback.
16. Multi-seed evaluation.
17. Seed plot aggregation.
18. Overall report summarization.
19. Final plot aggregation and reflection.
20. Citation gathering with Semantic Scholar.
21. Writeup retry loop.
22. Normal vs ICBINB writeup.
23. LaTeX compile/reflection loop.
24. VLM image/caption/reference review.
25. Final page-limit reflection.
26. PDF selection for review.
27. LLM peer review.
28. Ensemble/meta-review.
29. VLM review output.
30. Process cleanup.

### تصحيح تم أثناء المراجعة النهائية

أثناء المراجعة، تم اكتشاف أن النسخة الإنجليزية من Mermaid graph كان فيها node IDs بها علامة `?` مثل:

- `PLOTS?`
- `ICBINB?`

وهذا قد يسبب مشاكل في Mermaid rendering لأن `?` غير مناسب كجزء من node ID.

تم تصحيحها إلى:

- `PLOTSQ`
- `ICBINBQ`

وتم تحديث:

- `graph_english.mmd`
- `graph_english.md`

## 7. مراجعة الـ gap audit

ملف:

`graph_gap_audit.md`

يوثق ما كان ناقصًا في الرسم قبل المقارنة بالكود، وما تمت إضافته.

أهم الإضافات:

- skip_writeup / skip_review.
- writeup_type normal vs icbinb.
- writeup_retries loop.
- load_code file existence branch.
- add_dataset_ref file existence branch.
- AgentManager nested loops.
- stage completion قبل substage completion.
- multi-seed evaluation.
- ParallelAgent node selection logic.
- debug probability and max_debug_depth.
- Stage 2 and Stage 4 special paths.
- metric parsing failures.
- plot retries.
- future timeout handling.
- GPU acquire/release.
- review PDF selection.
- cleanup loops.

## 8. التحديات التي ظهرت

### 8.1 prompts ليست كلها strings مباشرة

بعض prompts ليست متغيرات نصية بسيطة، بل:

- dict prompts.
- list prompts.
- FunctionSpec schemas.
- runtime-injected file content.
- runtime tool descriptions.

الحل:

- تم استخراج source expression.
- تم توثيق كيفية ملء placeholders.
- تم إضافة dynamic insertions في prompt extraction.

### 8.2 Graph كامل جدًا قد يصبح ضخم

لو الرسم يغطي كل function وكل condition حرفيًا سيصبح غير قابل للقراءة أو الرندر.

الحل:

- الرسم يغطي كل المسارات التشغيلية الأساسية والقرارات الكبرى.
- التفاصيل الدقيقة لكل function محفوظة في `python_logic_flow_complete.md` و JSON inventory.

### 8.3 AgentManager و ParallelAgent معقدان

أعقد أجزاء الريبو:

- `agent_manager.py`
- `parallel_agent.py`

لأنهما يحتويان على:

- nested loops.
- staged progression.
- process pools.
- GPU allocation.
- retry logic.
- stage-specific behavior.

الحل:

- تم عمل gap audit خاص.
- تم توسيع الرسم ليغطي هذه المسارات.

### 8.4 GitHub token ظهر في الشات

تم استخدامه لتنفيذ المطلوب، لكن يجب اعتباره compromised.

التوصية:

- عمل revoke للتوكن فورًا.
- إنشاء token جديد عند الحاجة بصلاحيات محدودة.

## 9. مراجعة العمليات من البداية للنهاية

### المرحلة 1: Prompt extraction

تم استخراج prompts كاملة من:

- ideation.
- experiments.
- plotting.
- citations.
- writeup.
- review.
- VLM.
- BFTS internals.
- schemas.
- dynamic insertions.

### المرحلة 2: External-source audit

تم cross-check مع:

- arXiv paper.
- official README.
- linked workshop experiment repo.

### المرحلة 3: Full Python logic extraction

تم تحليل كل Python files باستخدام AST واستخراج:

- functions/classes.
- loops/conditions.
- returns/raises.
- calls/side effects.

### المرحلة 4: Graph generation

تم بناء:

- English Mermaid graph.
- Arabic Mermaid graph.

### المرحلة 5: Graph-vs-code comparison

تمت مقارنة الرسم بالكود، واكتشاف نواقص، ثم تحديث الرسم.

### المرحلة 6: Final review

تمت مراجعة الملفات والعدّادات، واكتشاف مشكلة Mermaid ID، وتصحيحها.

### المرحلة 7: GitHub publication

تم رفع النتائج إلى repo public.

## 10. حالة الجودة النهائية

### جيد جدًا / مكتمل

- prompt extraction.
- per-file logic inventory.
- high-level pipeline graph.
- Arabic and English versions.
- GitHub publication.
- gap audit.

### حدود طبيعية للنتيجة

- الرسم ليس بديلًا عن `python_logic_flow_complete.md`؛ لأنه intentionally high-level حتى يظل قابلًا للقراءة.
- بعض runtime prompts تعتمد على config/data/LLM outputs، لذلك تم توثيق template/source وليس instance runtime النهائي.
- لا يمكن ضمان أن كل edge في الرسم يمثل كل line-level branch؛ التفاصيل الدقيقة محفوظة في تقرير AST.

## 11. الخلاصة

الشغل الآن يغطي:

- كل مراحل النظام.
- كل العمليات الأساسية.
- كل loops والقرارات الكبرى.
- كل prompt families.
- كل inputs/outputs الأساسية.
- كل التحديات المعمارية المهمة.
- رسومات Mermaid بالإنجليزي والعربي محدثة بعد المقارنة بالكود.

الحالة النهائية: جاهز كـ public audit/extraction repo.
