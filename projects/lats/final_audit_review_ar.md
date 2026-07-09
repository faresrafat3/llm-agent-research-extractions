# مراجعة نهائية — LATS / Language Agent Tree Search

## النطاق

تمت مراجعة نظام LATS من:

- Paper: `https://arxiv.org/abs/2310.04406`
- Code: `https://github.com/lapisrocks/LanguageAgentTreeSearch`
- Commit: `853d81614607dd27433faf17c7b0a7d660f95d22`

## الهدف من الحزمة

الهدف ليس مجرد نسخ ملفات، بل بناء خريطة تشغيلية مفهومة للنظام:

- ما هي البرومبتات؟
- أين حلقات البحث؟
- كيف يتم اختيار العقد؟
- كيف يتم التوسع؟
- كيف يتم التقييم؟
- كيف يعمل rollout؟
- كيف يتم backpropagation؟
- أين تدخل البيئة الخارجية؟
- أين تدخل self-reflection؟
- ما هي المدخلات والمخرجات؟

## ملخص النظام

LATS هو إطار يجمع بين:

1. Reasoning — التفكير/الاستدلال عبر اللغة.
2. Acting — تنفيذ أفعال في بيئة أو توليد كود.
3. Planning — البحث الشجري باستخدام MCTS.
4. External feedback — ملاحظات من البيئة أو نتائج اختبارات.
5. Value estimation — تقييم العقد أو المسارات باستخدام LM.
6. Self-reflection — تلخيص المسارات الفاشلة لتوجيه البحث لاحقًا.

## المراحل التشغيلية الأساسية

### 1. اختيار المجال

الكود يغطي ثلاثة مسارات رئيسية:

- HotPotQA.
- WebShop.
- Programming.

### 2. تهيئة الجذر

يبدأ البحث من:

- سؤال في HotPotQA.
- مهمة تسوق في WebShop.
- مسألة برمجية في HumanEval/MBPP/LeetCode.

### 3. Selection

يتم اختيار node من الشجرة بناءً على UCT أو سياسة مشابهة.

قرارات مهمة:

- هل العقدة terminal؟
- هل كل الأطفال terminal؟
- هل يوجد child ناجح؟
- هل يجب backtrack؟

### 4. Expansion

النظام يطلب من LM توليد احتمالات جديدة:

- thoughts/actions في HotPotQA/WebShop.
- code candidates في Programming.

### 5. Evaluation

يتم تقييم العقد عبر:

- value prompts.
- environment feedback.
- reward.
- exact match.
- unit tests.

### 6. Rollout

يتم محاكاة مسار من عقدة واعدة حتى:

- نجاح.
- فشل.
- terminal state.
- max depth.

### 7. Backpropagation

يتم إرجاع reward/value إلى العقد السابقة في الشجرة.

### 8. Reflection

عند وجود مسارات فاشلة، يمكن توليد reflection من:

- failed trajectories.
- observations.
- wrong final answers.
- test feedback.

ثم يتم إدخال reflection في prompts لاحقًا.

## أهم الملفات

### HotPotQA

- `hotpot/lats.py`
- `hotpot/hotpot.py`
- `hotpot/base.py`
- `hotpot/tot.py`
- `hotpot/rap.py`
- `hotpot/wikienv.py`
- `hotpot/wrappers.py`

### WebShop

- `webshop/lats.py`
- `webshop/base.py`
- `webshop/prompt.py`
- `webshop/webshop.py`

### Programming

- `programming/mcts.py`
- `programming/dfs.py`
- `programming/main.py`
- `programming/generators/*`
- `programming/executors/*`
- `programming/reflexion.py`
- `programming/immediate_refinement.py`
- `programming/immediate_reflexion.py`

## أهم الحلقات

- MCTS iteration loop.
- selection while-loop.
- retry loop عند timeout في environment step.
- expansion/sample generation loops.
- value evaluation loops.
- rollout depth loop.
- backpropagation loop حتى root.
- failed trajectory collection.
- reflection generation loop.
- programming pass@k loop.
- programming max_iters loop.
- dataset/benchmark iteration loops.

## أهم القرارات

- terminal node vs non-terminal node.
- reward == 1 vs reward == 0.
- all children terminal.
- best child by UCT.
- duplicate candidates / local value cache.
- reflection generation threshold.
- done/exhausted/max depth.
- code compile/runtime/test pass/fail.
- internal tests vs real tests.
- successful trajectory found during rollout.

## المدخلات

- questions/tasks.
- environment observations.
- actions.
- prompts.
- failed trajectories.
- code problem statements.
- unit tests.
- model/backend parameters.
- max iterations / max depth.

## المخرجات

- final trajectory.
- final answer.
- code solution.
- reward.
- exact match / pass status.
- node tree values.
- logs.
- reflection text.
- JSONL result artifacts.

## ما تم استبعاده ولماذا

الريبو يحتوي على ملفات root/logs كثيرة ناتجة من تجارب سابقة. هذه ليست prompt templates تشغيلية، لذلك لم يتم نسخها كلها داخل raw prompt files.

لكن تم نسخ أمثلة مهمة مثل:

- `hotpot/tot_10it.log`
- `webshop/logs/example.log`

لأنها تساعد على فهم trajectory format والـ prompt/action/observation patterns.

## جودة الرسم

تم بناء رسمين:

- `graph_english.md`
- `graph_arabic.md`

يغطيان:

- اختيار المجال.
- نواة MCTS.
- HotPotQA.
- WebShop.
- Programming.
- prompts.
- value/reflection flow.

## الخلاصة

حزمة LATS الآن متكاملة مثل باقي الحزم: فيها prompts، logic، graphs، deep dive، completeness، quality review، وfinal audit. وهي تفصل بوضوح بين مصادر التشغيل والنتائج التاريخية.