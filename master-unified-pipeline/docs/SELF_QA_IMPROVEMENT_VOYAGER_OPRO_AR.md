# أسئلة تحسين ذاتية — دمج Voyager + OPRO في أرسينال

**الهدف الثابت:** استخراج → دقة → رسوم EN/AR → **دمج طبقي في أرسينال** → نشر عام.  
نفس معيار جولة ToT.

---

## الأسئلة

| # | السؤال | الجواب | إجراء |
|---|---|---|---|
| Q1 | أين يجلس OPRO دون كسر L1/APE؟ | L1-iterative بجانب APE | ✅ mode ape\|opro\|cascade |
| Q2 | أين يجلس Voyager دون خلطه بـ L3؟ | ليس بحث شجري؛ ذاكرة/منهج | ✅ L5-procedural + curriculum |
| Q3 | هل نضيف طبقات L7/L8؟ | لا — هدفنا طبقات مستقرة | ✅ توسيع L1 و L5 فقط |
| Q4 | هل المخططات تعكس القرارين؟ | كانت APE-only / Reflexion-only | ✅ تحديث EN/AR |
| Q5 | هل pattern_extraction يذكر النمطين؟ | لا | ✅ أقسام 6b/6c + fusion rules |
| Q6 | هل prompts P1/P5 كافية؟ | لا | ✅ P1.5–P1.6 و P5.4–P5.6 |
| Q7 | هل المجمّع/الفهرس/المراجعة النهائية متسقة؟ | جزئياً | ✅ تُحدَّث مع الدفع |
| Q8 | هل نعيد استخراج الحزم؟ | لا | — |
| Q9 | runtime؟ | خارج النطاق | — |
| Q10 | تعريف الجودة هنا؟ | كل مستخرج له عقد في L0–L6 | OPRO→L1، Voyager→L5 |

---

## مبدأ الدمج

> **OPRO يكمّل APE داخل L1 (كيف نبحث عن التعليمة).**  
> **Voyager يكمّل Reflexion داخل L5 (ماذا نتذكر: كلام vs مهارات).**  
> **لا نكدّس طبقات جديدة.**

---

## نتيجة الجولة

- 10 أنظمة في README / research / patterns  
- L1: APE + OPRO + cascade  
- L5: Reflexion + Voyager skills/curriculum  
- MASTER graphs EN/AR متكافئة (131 حافة)  
- inventory / deep_dive / prompts / architecture محدّثة  
