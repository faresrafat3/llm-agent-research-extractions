# المراجعة النهائية — Meta-Prompting

## المراحل المستخرجة

- Meta Model يستقبل المهمة
- استدعاء Expert (متعدد خبراء/شخصيات)
- مخرجات Expert
- إضافة Feedback / مسارات سابقة
- توليد الإجابة النهائية
- تقييم اختياري عبر Python executor

## الحلقات

- حلقة Expert dispatch: لكل expert يتم توليد استدعاء منفصل
- حلقة Feedback append: تكرار إضافة feedback للـ meta prompt
- حلقة تقييم Python: تنفيذ كود المولد والتحقق

## نقاط القرار

- هل نستخدم expert واحد أم متعدد؟ → قرار meta model
- هل نفعّل Python executor؟ → نعم / لا حسب نوع المهمة
- هل نضيف reflection/feedback؟ → نعم في الوضع التفاعلي
- اختيار Expert المناسب: Game of 24، Checkmate، MGSM، إلخ → حسب نوع السؤال
- آلية الدمج: summarizer vs voting vs direct

## المدخلات / المخرجات

- **المدخل:** user query + meta-prompting instruction + expert registry + أمثلة (اختياري)
- **المخرج:** إجابة نهائية + expert transcripts + تقييم (accuracy / pass@k)

## الشروط

- إذا كانت المهمة حسابية → فعّل Python expert
- إذا كانت متعددة اللغات (MGSM) → استخدم expert لغوي مناسب
- إذا فشل الـ expert → إعادة المحاولة بـ expert بديل أو زيادة feedback
- حد الـ context window → تقليل عدد الـ experts أو تلخيص التاريخ

## الخلاصة

تم توثيق كل المراحل والحلقات ونقاط القرار والشروط والمدخلات/المخرجات — مطابق لمعيار Self-Refine / Reflexion / LATS / APE / Prompt Report.
