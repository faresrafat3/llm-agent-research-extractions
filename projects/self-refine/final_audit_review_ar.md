# مراجعة نهائية — Self-Refine Full Extraction

## النطاق

تمت مراجعة الورقة والكود الخاصين بـ Self-Refine:

- Paper: `https://arxiv.org/abs/2303.17651`
- Code: `https://github.com/madaan/self-refine`
- Audited commit: `9a206d41e5d2d0c241bb441f41eeadb945afaa55`

## ما تم استخراجه

### من الورقة

تم توثيق الخوارزمية الأساسية:

1. توليد أولي: `y0 = M(p_gen || x)`.
2. حلقة feedback/refine:
   - `fb_t = M(p_fb || x || y_t)`.
   - إذا تحقق `stop(fb_t,t)` يتم التوقف.
   - وإلا يتم توليد `y_{t+1}` من `p_refine` مع التاريخ الكامل.
3. إرجاع آخر ناتج.

كما تم توثيق:

- فكرة استخدام نفس LLM كـ generator و feedback provider و refiner.
- عدم الحاجة إلى تدريب إضافي أو RL.
- أنواع stop conditions.
- المهام التي يقيم عليها النظام.

### من الكود

تم تحليل كل ملفات Python تحت `src/`:

- عدد ملفات Python: 45.
- top-level functions: 71.
- class methods: 102.

تم استخراج:

- classes.
- functions/methods.
- inputs من signatures.
- outputs/returns.
- loops.
- decisions/conditions.
- try/except.
- LLM/API calls.
- file I/O.
- prompt-building assignments.

### من ملفات prompts

تم نسخ كل ملفات prompts الخام بدون truncation إلى:

`raw_prompt_files/`

عدد ملفات prompt المنسوخة: 19.

تم توثيقها في:

`prompts_complete.md`

مع preview للملفات الصغيرة، وraw copy كاملة لكل الملفات، خصوصًا الملف الكبير:

`data/prompt/responsegen/fed_data.json`

## المهام المغطاة في الريبو

1. Acronym generation.
2. Acronym MCTS variant.
3. CommonGen constrained generation.
4. GSM math reasoning.
5. PIE code optimization.
6. Dialogue response generation.
7. Sentiment reversal.
8. Code readability utilities/evaluation.

## أهم loops المستخرجة

- الحلقة العامة في الورقة: feedback/refine حتى stop.
- `while n_attempts < max_attempts` في مهام acronym, commongen, gsm, sentiment وغيرها.
- MCTS iterations في acronym MCTS.
- duplicate expansion loop في MCTS.
- loops على datasets/files/rows لتشغيل التجارب وحفظ JSONL.
- loops على samples في multi-sample baselines.
- prompt example construction loops.

## أهم decision points

- هل هذه المحاولة الأولى أم محاولة refinement؟
- هل feedback يشير إلى stop؟
- هل CommonGen feedback هو `none` لكلا المفهوم والمنطق العام؟
- هل GSM feedback يحتوي على `it is correct`؟
- هل acronym score يتم إضافته للتاريخ؟
- هل acronym مكرر في MCTS؟
- هل الملف/النتيجة موجودة لتجنب overwrite؟
- هل status == success لتخطي rerun rows؟
- هل feedback type هو rich/naive/generic/none؟
- هل OpenAI parsing نجح أم يحتاج retry decorator؟

## prompts والـ placeholders

تم توثيق prompt sources التالية:

- `data/prompt/acronym/*`
- `data/prompt/commongen/*`
- `data/prompt/gsm/*`
- `data/prompt/pie/*`
- `data/prompt/responsegen/*`
- `docs/commongen_*`
- Python string templates داخل `src/*`.

أمثلة placeholders/dynamic fields:

- `{title}`
- `{acronym}`
- `{scores}`
- `{concepts}`
- `{sentence}`
- `{concept_feedback}`
- `{commonsense_feedback}`
- `{question}`
- `{solution}`
- `{feedback}`
- `{code}`
- `{review}`
- `{sentiment}`
- `{target_sentiment}`
- `{transferred_review}`

## Mermaid graphs

تم إنشاء نسختين:

- `graph_english.mmd`
- `graph_arabic.mmd`

وكذلك نسخ Markdown preview:

- `graph_english.md`
- `graph_arabic.md`

الرسوم تغطي:

- خوارزمية الورقة العامة.
- مسارات الريبو حسب المهمة.
- بناء البرومبتات.
- OpenAI API call.
- parsing.
- stop conditions.
- task-specific loops.
- outputs/logs.

## تحديات واجهت الاستخراج

### 1. prompts موزعة بين كود وملفات بيانات

بعض البرومبتات داخل Python templates، وبعضها داخل JSONL/TXT، وبعضها أمثلة few-shot كبيرة.

الحل:

- استخراج Python prompt assignments.
- نسخ كل raw prompt files بدون اختصار.
- توثيق المسارات والـ previews.

### 2. ملف responsegen/fed_data.json كبير

الملف كبير جدًا بالنسبة لعرضه كاملًا داخل Markdown.

الحل:

- تم حفظه كاملًا في `raw_prompt_files`.
- تم عرض preview فقط داخل `prompts_complete.md`.

### 3. لا توجد implementation واحدة موحدة فقط

الريبو ليس framework واحد فقط، بل عدة task-specific implementations.

الحل:

- الرسم يغطي algorithm العام، ثم يفرع إلى كل task family.
- التقرير التفصيلي يحتوي كل ملف وكل function.

### 4. stop conditions تختلف حسب المهمة

ليست كل المهام تستخدم stop indicator بنفس الطريقة.

الحل:

- تم توثيق stop العام من الورقة.
- وتم توثيق task-specific stops في التقرير والرسم.

## حدود النتيجة

- الرسم Mermaid intentionally عالي المستوى حتى يظل قابلًا للقراءة.
- التفاصيل line-level محفوظة في `python_logic_flow_complete.md` و `python_logic_inventory.json`.
- ملفات prompt الخام محفوظة كاملة في `raw_prompt_files/` بدل حشر الملفات الكبيرة كاملة داخل Markdown.

## الحالة النهائية

الحزمة تغطي كل المطلوب:

- بحث الورقة.
- استكشاف الكود.
- prompts.
- loops.
- logic.
- decisions.
- conditions.
- inputs/outputs.
- Mermaid graph إنجليزي وعربي.
- raw prompt files كاملة.
- مراجعة نهائية.


## مراجعة إضافية بعد الفحص

تم اكتشاف مصادر قيمة إضافية لم تكن موثقة بشكل كافٍ في النسخة الأولى من الحزمة:

1. `colabs/Visual-Self-Refine-GPT4V.ipynb`
   - يحتوي على prompt لتوليد TikZ أولي.
   - يحتوي على system prompt: `You are a helpful assistant who can write Tikz code.`
   - يحتوي على prompt لإصلاح LaTeX من error log.
   - يحتوي على prompt مرئي GPT-4V لتحسين الصورة والكود.
   - يحتوي على loop: `for i in range(n_refine_loop)` مع شرط توقف عند فشل توليد الصورة أو تجاوز عدد الاستثناءات المسموح.

2. `docs/index.html`
   - يحتوي على pseudo-code عام لـ Self-Refine.
   - يحتوي على أمثلة prompt/output/feedback/refinement معروضة في الموقع.

تمت إضافة الملفات التالية:

- `visual_self_refine_notebook_audit.md`
- `docs_prompt_algorithm_audit.md`

كما تم نسخ raw sources إلى `raw_prompt_files/`.
