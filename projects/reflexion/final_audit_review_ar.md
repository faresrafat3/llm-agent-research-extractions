# مراجعة نهائية — Reflexion Full Extraction

## النطاق

تمت مراجعة الورقة والكود الخاصين بـ Reflexion:

- Paper: `https://arxiv.org/abs/2303.11366`
- Code: `https://github.com/noahshinn/reflexion`
- Commit: `218cf0ef1df84b05ce379dd4a8e47f17766733a0`

## ما تم استخراجه

- كل ملفات Python التي تم العثور عليها في الريبو.
- prompt/config/few-shot sources التشغيلية.
- prompts المبنية داخل Python.
- loops/conditions/decisions/returns/I-O/LLM calls.
- ملخص الورقة والـ Reflexion algorithm.
- Mermaid graph بالإنجليزي والعربي.

## المراحل المغطاة

1. AlfWorld decision-making.
2. WebShop interactive shopping.
3. HotPotQA reasoning/ReAct/CoT.
4. Programming/HumanEval/MBPP/LeetCode.
5. Baselines: simple, immediate-refinement, immediate-reflexion, reflexion, reflexion-UCS.

## أهم الحلقات

- trial loop.
- environment loop.
- step/action loop.
- memory update loop.
- code generation/reflection retry loop.
- test execution/evaluation loop.
- HotPotQA trial/reflection loop.

## أهم القرارات

- نجاح/فشل المحاولة.
- max steps/max trials.
- use_memory.
- resume vs new run.
- env already successful skip.
- prompt selection by task prefix.
- tests pass/fail.
- parse/generated code validity.
- model type chat vs completion/HF.

## ما تم استبعاده ولماذا

الريبو يحتوي على root logs و joblib و JSONL كثيرة جدًا تمثل نتائج تشغيل سابقة وbenchmarks. تم توثيقها كـ artifacts وليس نسخها كلها كـ prompt templates، حتى لا تختلط النتائج مع مصادر prompts التشغيلية.

## الخلاصة

الحزمة تغطي Reflexion كفكرة بحثية وكتنفيذ عملي في المهام الأساسية، مع فصل واضح بين source prompts والكود والنتائج السابقة.
