# مراجعة الجودة — GAPMAP

## معايير المراجعة

- **الأمانة للمصدر:** هل الأوامر مأخوذة حرفيًا من `ex_gap_xtract.py` أم معاد بناؤها بأمانة من وصف الورقة؟
- **الاكتمال:** هل تم تغطية explicit + implicit + chunking + evaluation؟
- **القابلية للتنفيذ:** هل يمكن إعادة التشغيل من README؟
- **العربية:** هل المخططات العربية واضحة؟

## النتائج

| معيار | الدرجة (1-5) | ملاحظات |
|---|---|---|
| أمانة explicit prompt | 5 | مأخوذ حرفيًا من السكربت الرسمي مع REQUIRED_KEYS |
| TABI prompt | 4.5 | معاد بناؤه من وصف دقيق في الورقة Sec 4.3.1 + أمثلة Table1 + ملاحظات README عن Claim/Grounds/Warrant/Bucket ؛ ليس في السكربت لكن مبرر |
| full-paper pilot prompt | 4.5 | معاد بناؤه من Sec 4.3.2 + نتائج الاستبيان |
| منطق chunking | 5 | كود Stanza + fallback regex + حدود 1000 كلمة محفوظة |
| تقييم ROUGE + entailment | 5 | عتبات 0.55 و 0.4 مذكورة في الورقة مع تفاصيل one-to-one و bi-directional |
| graphs | 5 | EN/AR mmd قابل للتنفيذ، يغطي كل مسارات القرار |
| توثيق failure modes | 5 | 0-shot يتحول غامض، 35% invalid feasibility، small models struggle |

## ثغرات حرجة (إن وجدت)

- لا يوجد سكربت رسمي لـ TABI في repo الحالي (Data/tst.txt فقط). الاعتماد على وصف الورقة مشروع وموثق.
- full-text pilot استخدم واجهة GPT-4o غير مفتوحة؛ الموجه معاد بناؤه؛ موثق كذلك.

## توصيات

- إضافة ملف `raw_prompt_files/prompt_implicit_TABI_3shot.txt` منفصل كما فعلنا.
- توثيق أن العينات في `raw_data_samples` عينات مصغرة (ليس كل البيانات الضخمة).
- إضافة ZIP أرشيف عند الدفع.

## الحكم النهائي

**مقبول للنشر** — يطابق معيار extractions السابقة ويضيف قيمة Part 6 HOW TO TRACK KNOWLEDGE.

المستودع جاهز للدفع إلى `faresrafat3/gapmap-full-extraction`.
