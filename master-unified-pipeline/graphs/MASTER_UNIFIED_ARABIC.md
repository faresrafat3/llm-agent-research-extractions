# أرسينال — مخطط خط الأنابيب الموحّد الرئيسي (عربي)

**نظام واحد. سبعة مصادر. طبقات متداخلة L0–L6.**

| الطبقة | الدور | النظام المصدر |
|---|---|---|
| L0 | موجّه عائلات التقنيات | The Prompt Report |
| L1 | محسّن التعليمات | APE |
| L2 | مايسترو ميتا + خبراء | Meta-Prompting |
| L3 | بحث شجري (MCTS/UCT) | LATS |
| L4 | حلقة صقل محلي | Self-Refine |
| L5 | ذاكرة لفظية حلقية | Reflexion |
| L6 | مراحل تصاعدية + كتابة + مراجعة | AI Scientist v2 |

## كيف تقرأ المخطط

1. ادخل من **مهمة المستخدم** → **غلاف مراحل L6**.
2. كل مرحلة تفتح **حلقة محاولات L5** مع ذاكرة تأمل.
3. كل محاولة تستدعي **موجّه L0** لتفعيل الطبقات.
4. اختيارياً **L1 APE** يرتّب التعليمات.
5. **L2 ميتا** يوزّع الخبراء (بما فيهم بايثون وTreeSearch).
6. **L3 LATS** يستكشف تحت عدم اليقين؛ الأوراق تذهب إلى **L4 Self-Refine**.
7. الإخفاقات تصبح **تأملات L5** للمحاولة التالية.
8. نجاح المرحلة → بذور متعددة → رسوم → مرحلة تالية → كتابة → مراجعة أقران.

## Mermaid

```mermaid
flowchart TB
  %% أرسينال — خط الأنابيب الموحّد الرئيسي من دمج الأنظمة السبعة

  START([مهمة المستخدم / فكرة بحثية / استعلام]) --> L6_IN[L6 غلاف المراحل التصاعدي<br/>AI Scientist v2]

  subgraph L6["L6 — غلاف المراحل التصاعدي (AI Scientist v2)"]
    direction TB
    L6_IN --> STAGE{المرحلة الحالية}
    STAGE -->|1 مسودة| S1[المرحلة 1: التنفيذ الأولي / المسودة]
    STAGE -->|2 ضبط| S2[المرحلة 2: خط الأساس + ضبط المعاملات]
    STAGE -->|3 تحسين| S3[المرحلة 3: تحسينات بحثية إبداعية]
    STAGE -->|4 عزل| S4[المرحلة 4: دراسات العزل Ablation]
    S1 --> TRIAL_WRAP
    S2 --> TRIAL_WRAP
    S3 --> TRIAL_WRAP
    S4 --> TRIAL_WRAP

    TRIAL_WRAP[الدخول إلى حلقة محاولات L5 مع ذاكرة المرحلة]

    TRIAL_DONE[عودة أفضل نتيجة من المكدس] --> BEST{هل وُجدت أفضل عقدة / نتيجة؟}
    BEST -->|لا| ABORT[إيقاف المسار — تسجيل no_best_node]
    BEST -->|نعم| MSEED[تقييم متعدد البذور Multi-seed]
    MSEED --> PLOTS[توليد الرسوم + تغذية VLM + التجميع]
    PLOTS --> STAGE_OK{اكتملت المرحلة / مراحل أخرى؟}
    STAGE_OK -->|نعم التالية| STAGE
    STAGE_OK -->|اكتملت الكل| WRITEUP_GATE{هل الكتابة مفعّلة؟}
  end

  subgraph L5["L5 — الذاكرة اللفظية الحلقية (Reflexion)"]
    direction TB
    TRIAL_WRAP --> MEM_INIT[memory = آخر K تأملات]
    MEM_INIT --> TRIAL_LOOP{لكل محاولة trial حتى max_trials}
    TRIAL_LOOP --> L0_CALL[استدعاء موجّه التقنيات L0]
    INNER_DONE[نتيجة المكدس الداخلي] --> SUCC{نجاح؟}
    SUCC -->|نعم| TRIAL_DONE
    SUCC -->|لا ومحاولات منتهية| TRIAL_DONE
    SUCC -->|لا وتبقى محاولات| REFLECT[تأمل لفظي P5 من المسار + التغذية الراجعة]
    REFLECT --> MEM_UPD[إلحاق التأمل — الإبقاء على آخر K]
    MEM_UPD --> TRIAL_LOOP
  end

  subgraph L0["L0 — موجّه التقنيات (The Prompt Report)"]
    direction TB
    L0_CALL --> TAX[التصنيف وفق تصنيف 58 تقنية<br/>+ وكلاء / متعدد الوسائط / تقييم]
    TAX --> FAM{عائلات التقنيات}
    FAM --> F1[تعلّم في السياق ICL]
    FAM --> F2[توليد التفكير عائلة CoT]
    FAM --> F3[التفكيك ToT/PoT/L2M]
    FAM --> F4[التجميع Self-Consistency]
    FAM --> F5[النقد الذاتي Refine/Reflexion]
    FAM --> F6[تحسين الأوامر APE/OPRO]
    FAM --> F7[وكلاء وأدوات ReAct]
    F1 & F2 & F3 & F4 & F5 & F6 & F7 --> ACT[بناء أعلام التفعيل]
    ACT --> FLAGS["تفعيل: ape / meta / lats / refine / reflexion / stages"]
    FLAGS --> L1_GATE
  end

  subgraph L1["L1 — محسّن التعليمات (APE)"]
    direction TB
    L1_GATE{activate.ape ووجود أمثلة؟}
    L1_GATE -->|لا| L1_SKIP[استخدام أوامر افتراضية / يدوية]
    L1_GATE -->|نعم| APE_TPL{هل وُفر قالب التوليد؟}
    APE_TPL -->|لا| APE_CONV[تحويل EvalTemplate إلى GenerationTemplate<br/>PROMPT ← APE]
    APE_TPL -->|نعم| APE_USE[استخدام قالب التوليد المقدَّم]
    APE_CONV --> APE_GEN
    APE_USE --> APE_GEN
    APE_GEN[توليد المرشحين: لكل subsample<br/>عيّنة أمثلة → توليد بالنموذج]
    APE_GEN --> APE_DEDUP[إزالة التكرارات]
    APE_DEDUP --> APE_EVAL{طريقة التقييم؟}
    APE_EVAL -->|likelihood| APE_LL[الاحتمالية: log p للمخرجات]
    APE_EVAL -->|bandits| APE_UCB[جولات عصابات UCB على أذرع الأوامر]
    APE_LL --> APE_RANK[ترتيب الأوامر حسب الدرجة]
    APE_UCB --> APE_RANK
    APE_RANK --> APE_OUT[أفضل الأوامر + demo_fn]
    APE_OUT --> L2_GATE
    L1_SKIP --> L2_GATE
  end

  subgraph L2["L2 — المايسترو الميتا (Meta-Prompting)"]
    direction TB
    L2_GATE{activate.meta؟}
    L2_GATE -->|لا| L2_SKIP{activate.lats؟}
    L2_GATE -->|نعم| META_INIT[تهيئة الرسائل: تعليمات ميتا + الاستعلام + الذاكرة]
    META_INIT --> META_LOOP{جولة ميتا < الحد الأقصى}
    META_LOOP --> META_CALL[توليد نموذج الميتا]
    META_CALL --> META_KIND{نوع المخرج؟}
    META_KIND -->|إجابة نهائية| META_FINAL[استخراج FINAL ANSWER]
    META_KIND -->|غير صالح| META_ERR[إلحاق تغذية راجعة لخطأ التنسيق]
    META_ERR --> META_LOOP
    META_KIND -->|استدعاء خبير| META_EXP[استخراج اسم الخبير + التعليمات]
    META_EXP --> EXP_TYPE{نوع الخبير؟}
    EXP_TYPE -->|بايثون| EXP_PY[توليد خبير بايثون]
    EXP_PY --> RUN_Q{Please run this code؟}
    RUN_Q -->|نعم| EXEC[تنفيذ بمهلة زمنية — إلحاق stdout/err]
    RUN_Q -->|لا| EXP_APPEND
    EXEC --> EXP_APPEND
    EXP_TYPE -->|بحث شجري / LATS| L3_CALL
    EXP_TYPE -->|خبير عادي| EXP_LM[توليد خبير لغوي]
    EXP_LM --> L4_EXP[صقل مسودة الخبير عبر L4]
    L4_EXP --> EXP_APPEND[إلحاق مخرج الخبير + تغذية راجعة وسيطة]
    EXP_APPEND --> META_LOOP
    META_FINAL --> L4_FINAL
    L2_SKIP -->|نعم| L3_CALL
    L2_SKIP -->|لا| DIRECT[توليد مباشر بالطريقة الموجَّهة]
    DIRECT --> L4_FINAL
  end

  subgraph L3["L3 — محرك البحث الشجري (LATS / MCTS)"]
    direction TB
    L3_CALL[العقدة الجذر = الحالة / السؤال / المسألة] --> MCTS{لكل تكرار 1..N}
    MCTS --> SEL[اختيار عقدة بـ UCT]
    SEL --> TERM{حالة العقدة؟}
    TERM -->|نجاح طرفي| L3_WIN[إرجاع مسار ناجح]
    TERM -->|فشل طرفي / مستنفد| BACKTRACK[تقليم / تراجع]
    BACKTRACK --> MCTS
    TERM -->|قابل للتوسعة| EXPAND[توسيع: عينات LM أفكار/أفعال/كود بعرض W]
    EXPAND --> VALUE[تقييم الأبناء: قيمة LM + تغذية البيئة]
    VALUE --> ROLLOUT[محاكاة أفضل ابن حتى العمق الأقصى]
    ROLLOUT --> ROK{نجاح أثناء المحاكاة؟}
    ROK -->|نعم| L3_WIN
    ROK -->|لا| BPROP[إعادة نشر المكافأة/القيمة للجذر]
    BPROP --> FAIL_STORE[تخزين المسار الفاشل]
    FAIL_STORE --> REFL_Q{هل تستحق الإخفاقات الفريدة تأملاً؟}
    REFL_Q -->|نعم| L3_REFL[أمر تأمل ذاتي → قائمة التأملات]
    REFL_Q -->|لا| MCTS
    L3_REFL --> MCTS
    L3_WIN --> L4_LEAF
    MCTS -->|استنفاد الميزانية| L3_BEST[أفضل مسار جزئي]
    L3_BEST --> L4_LEAF
  end

  subgraph L4["L4 — الصاقل المحلي (Self-Refine)"]
    direction TB
    L4_LEAF[ورقة مرشحة / مسودة y] --> L4_INIT{هل y موجودة؟}
    L4_FINAL[مرشح للصقل النهائي] --> L4_INIT
    L4_INIT -->|لا| L4_GEN[y0 = M p_gen || x]
    L4_INIT -->|نعم| L4_Y[استخدام المرشح كـ y_t]
    L4_GEN --> L4_LOOP
    L4_Y --> L4_LOOP{لكل t حتى max_iters}
    L4_LOOP --> L4_FB[fb_t = M p_fb || x || y_t<br/>درجات متعددة الجوانب]
    L4_FB --> L4_STOP{إيقاف fb_t t ؟}
    L4_STOP -->|نعم عبارة إيقاف أو الحد| L4_OUT[إرجاع y_final + السجل]
    L4_STOP -->|لا| L4_REF[y_t+1 = M p_refine || x || السجل الكامل]
    L4_REF --> L4_HIST[إلحاق y_t fb_t بالسجل]
    L4_HIST --> L4_LOOP
  end

  L4_OUT --> INNER_DONE

  WRITEUP_GATE -->|لا| DELIVER([تسليم مخرجات المراحل + السجل])
  WRITEUP_GATE -->|نعم| CITE[حلقة الاستشهاد: Semantic Scholar ~20 جولة]
  CITE --> WRITE[كتابة الورقة LaTeX / التوليد]
  WRITE --> WREF{جولات تأمل الكتابة}
  WREF --> WREV[مراجعة الوضوح والأدلة وحدود الصفحات والأشكال]
  WREV --> WREF
  WREF -->|انتهى| PREVIEW{مراجعة الأقران مفعّلة؟}
  PREVIEW -->|نعم| PREVIEW_DO[مراجعة LLM + مراجعة VLM للأشكال + ميتا-مراجعة]
  PREVIEW -->|لا| DELIVER
  PREVIEW_DO --> DELIVER
  ABORT --> DELIVER

  subgraph LEGEND["مصادر الأنماط"]
    direction LR
    LG0[L0 توجيه تصنيف Prompt Report]
    LG1[L1 APE توليد-إزالة تكرار-تقييم-ترتيب]
    LG2[L2 ميتا توزيع الخبراء + أداة بايثون]
    LG3[L3 LATS اختيار UCT توسيع قيمة محاكاة نشر]
    LG4[L4 Self-Refine توليد-تغذية-صقل-إيقاف]
    LG5[L5 Reflexion ذاكرة لفظية عبر المحاولات]
    LG6[L6 AI Scientist مراحل بذور متعددة كتابة مراجعة]
  end

  DELIVER --> END([مخرجات أرسينال:<br/>أوامر · مسارات · قطع أثرية · ورقة · مراجعة · ذاكرة])
```

## ملفات مرافقة

- Mermaid الخام: `MASTER_UNIFIED_ARABIC.mmd`
- النسخة الإنجليزية: `MASTER_UNIFIED_ENGLISH.md` / `.mmd`
- سرد البنية: `../unified_architecture.md`
- استخراج الأنماط: `../pattern_extraction.md`
