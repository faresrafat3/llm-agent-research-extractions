# مخطط نظام Self-Refine الكامل — عربي

```mermaid
flowchart TD
  A[مدخل الورقة x + النموذج M + البرومبتات p_gen و p_fb و p_refine] --> G[التوليد الأولي y0 = M(p_gen || x)]
  G --> L{حلقة t = 0..max أو حتى stop}
  L --> FB[توليد التغذية الراجعة fb_t = M(p_fb || x || y_t)]
  FB --> STOP{هل stop(fb_t,t)؟}
  STOP -->|نعم| RETURN[إرجاع آخر y_t]
  STOP -->|لا| REF[تحسين y_t+1 باستخدام p_refine والتاريخ]
  REF --> HIST[إضافة المخرج والتغذية الراجعة إلى التاريخ]
  HIST --> L

  subgraph REPO[مسارات التنفيذ في الريبو]
    R0[اختيار سكريبت المهمة] --> ACR[توليد الاختصارات]
    R0 --> MCTS[اختصارات باستخدام MCTS]
    R0 --> CG[CommonGen]
    R0 --> GSM[رياضيات GSM]
    R0 --> PIE[تحسين كود PIE]
    R0 --> RESP[توليد ردود الحوار]
    R0 --> SENT[عكس المشاعر]
    R0 --> READ[قابلية قراءة الكود]
    R0 --> VISUAL[دفتر Visual Self-Refine GPT-4V]
  end

  subgraph PROMPT_BUILD[بناء البرومبتات]
    PF[ملفات البرومبت تحت data/prompt و docs] --> INITP[أمثلة init]
    PF --> FBP[أمثلة feedback]
    PF --> ITERP[أمثلة iterate/refine]
    PYT[قوالب وبادئات Python] --> QUERY[بناء query وقت التشغيل]
    INITP --> QUERY
    FBP --> QUERY
    ITERP --> QUERY
  end

  QUERY --> API[استدعاء OpenaiAPIWrapper.call]
  API --> PARSE[تحليل أول استجابة وحقول المهمة]
  PARSE --> TASKSTOP{قرارات توقف أو parsing خاصة بالمهمة}

  subgraph ACRONYM[حلقة الاختصارات]
    ACR --> AI[توليد اختصار أولي]
    AI --> AF[تقييم الاختصار بالدرجات]
    AF --> ASCORE[تحليل Total score]
    ASCORE --> ALOOP{while n_attempts < max_attempts}
    ALOOP -->|المحاولة 0| AI
    ALOOP -->|بعد ذلك| AIT[تحسين باستخدام تاريخ الاختصارات والدرجات]
    AIT --> AF
    ASCORE --> AKEEP{هل total_score >= 0؟}
    AKEEP -->|نعم| AHIST[إضافة للتاريخ]
    AKEEP -->|لا| ASKIP[تخطي تحديث التاريخ]
    AHIST --> ALOOP
    ASKIP --> ALOOP
  end

  subgraph ACRMCTS[حلقة MCTS للاختصارات]
    MCTS --> ROOT[توليد جذر وتقييمه]
    ROOT --> INITC[توليد أطفال أوليين]
    INITC --> MLOOP{for iterations}
    MLOOP --> SEL[اختيار node بـ UCB1]
    SEL --> EXP[توسيع باستخدام task_iterate]
    EXP --> DUP{هل الاختصار مكرر؟}
    DUP -->|نعم| EXP
    DUP -->|لا| SIM[محاكاة بالتقييم]
    SIM --> BACK[إرجاع القيمة للآباء]
    BACK --> MLOOP
  end

  subgraph COMMONGEN[حلقة CommonGen]
    CG --> CGI[جملة أولية من المفاهيم]
    CGI --> CGF[تغذية راجعة للمفاهيم والمنطق العام]
    CGF --> CGSTOP{هل كلاهما none؟}
    CGSTOP -->|نعم| CGRET[إرجاع تاريخ الجمل]
    CGSTOP -->|لا وباقي محاولات| CGI2[تحسين الجملة باستخدام التاريخ]
    CGI2 --> CGF
  end

  subgraph GSMFLOW[حلقة GSM]
    GSM --> GSI[توليد حل Python أولي]
    GSI --> GSF[Feedback قد يحتوي على حل محسن]
    GSF --> GSCOR{هل feedback يقول it is correct؟}
    GSCOR -->|نعم| GSRET[توقف وإرجاع logs]
    GSCOR -->|لا وباقي محاولات| GSUPD[الحل = الحل المحسن]
    GSUPD --> GSF
  end

  subgraph PIEF[حلقة تحسين الكود PIE]
    PIE --> PI[توليد كود محسن]
    PI --> PFDB[توليد feedback للتحسين]
    PFDB --> PIT{هل وصلت max attempts؟}
    PIT -->|لا| PIR[تحسين الكود باستخدام الأصل والحالي والfeedback]
    PIR --> PFDB
    PIT -->|نعم| PIRET[كتابة النتائج]
  end

  subgraph RESPF[حلقة توليد الردود]
    RESP --> RI[رد أولي]
    RI --> RF[تغذية راجعة FED/GPT]
    RF --> RS{max attempts أو كفاية feedback؟}
    RS -->|لا| RR[تحسين الرد باستخدام تاريخ feedback]
    RR --> RF
    RS -->|نعم| RRET[كتابة المخرجات]
  end

  subgraph SENTF[حلقة عكس المشاعر]
    SENT --> SI[مراجعة محولة أولية]
    SI --> SM[قياس المشاعر]
    SM --> SF[توليد feedback]
    SF --> SADD{هل نضيف Try again؟}
    SADD -->|نعم| SAPP[إضافة Try again]
    SADD -->|لا| SHIST[تحديث التاريخ]
    SAPP --> SHIST
    SHIST --> SAT{هل n_attempts < max_attempts؟}
    SAT -->|نعم| SIT[تحسين النقل باستخدام التاريخ]
    SIT --> SM
    SAT -->|لا| SRET[كتابة logs]
  end


  subgraph VISUALFLOW[حلقة Visual Self-Refine GPT-4V]
    VISUAL --> VOBJ[اختيار object_name و n_refine_loop]
    VOBJ --> VINIT[برومبت get_initial_latex إلى GPT-4]
    VINIT --> VRENDER[رندر LaTeX/TikZ إلى صورة base64]
    VRENDER --> VLOOP{حلقة حتى n_refine_loop}
    VLOOP --> VIMG{هل الصورة متاحة؟}
    VIMG -->|لا| VSTOP[إيقاف الحلقة المرئية]
    VIMG -->|نعم| VPROMPT[برومبت GPT-4V لفهم الصورة وتحسين TikZ]
    VPROMPT --> VCALL[إرسال الصورة والكود إلى GPT-4V]
    VCALL --> VEXTRACT[استخراج latex block]
    VEXTRACT --> VUPDATE[تحديث init_code وإضافة النتيجة]
    VUPDATE --> VLOOP
    VCALL --> VERR{هل حدث exception؟}
    VERR -->|باقي سماح| VLOOP
    VERR -->|انتهى السماح| VSTOP
    VINIT --> VFIX[برومبت fix_latex لإصلاح أخطاء التجميع]
  end

  TASKSTOP --> OUTPUTS[المخرجات: JSONL logs ودرجات ومخرجات محسنة وتاريخ البرومبتات]

```
