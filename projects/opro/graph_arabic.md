# أوبرو OPRO — مخطط المنطق (عربي)

الورقة: https://arxiv.org/abs/2309.03409  
الكود: https://github.com/google-deepmind/opro  
الالتزام: `a76bdce2cbf6d4a0d1e570a6fcfe17be9c2abdd7`

```mermaid
flowchart TD
  %% أوبرو OPRO — مخطط منطق الكود الرسمي (عربي)
  %% الورقة arXiv:2309.03409 | الكود google-deepmind/opro @ a76bdce

  START([البداية]) --> MODE{سكربت الدخول؟}
  MODE -->|optimize_instructions| IO[optimize_instructions.main]
  MODE -->|evaluate_instructions| EV[evaluate_instructions.main]
  MODE -->|optimize_linear_regression| LR[انحدار خطي OPRO]
  MODE -->|optimize_tsp| TSP[TSP OPRO]

  IO --> LOAD[تحميل البيانات gsm8k / bbh / mmlu]
  LOAD --> SPLIT[فهارس train / eval / test]
  SPLIT --> BIND[ربط scorer + optimizer call_server_func]
  BIND --> EVOL[run_evolution]

  subgraph EVO["run_evolution — تحسين التعليمات"]
    direction TB
    EVOL --> INIT[لكل initial_instruction]
    INIT --> SC0[evaluate_single_instruction على train]
    SC0 --> HIST0[إلحاق instruction, score, step=-1]
    HIST0 --> WRONG[تحديث عدّادات الأسئلة الخاطئة]
    WRONG --> STEP{لكل i_step حتى num_search_steps}

    STEP --> TEMP{جدول الحرارة؟}
    TEMP -->|constant| TC[T = T0]
    TEMP -->|linear_increase| TL[T = T0 + تقدم * (Tend-T0)]
    TC --> FS
    TL --> FS

    FS{few_shot_qa_pairs؟}
    FS -->|نعم| FSEL{معيار الاختيار}
    FSEL -->|accumulative_most_frequent| FA[الأكثر خطأ منذ البداية]
    FSEL -->|current_most_frequent| FC[الأكثر خطأ تحت مجموعة الميتا الحالية]
    FSEL -->|constant| FK[عيّنة ثابتة]
    FSEL -->|random| FR[إعادة عيّنة كل خطوة]
    FA --> META
    FC --> META
    FK --> META
    FR --> META
    FS -->|لا| META[gen_meta_prompt]

    META --> MTYPE{نوع meta_prompt؟}
    MTYPE -->|both_instructions_and_exemplars| MB[سجل الدرجات + أمثلة اختيارية]
    MTYPE -->|instructions_only| MI[وصف مهمة مختصر + السجل]
    MB --> MPOS
    MI --> MPOS
    MPOS{نموذج المحسّن؟}
    MPOS -->|GPT| MG[ترويسات INS/Start + طلب درجة أعلى]
    MPOS -->|text-bison| MT[نصوص بدرجات تصاعدية + كتابة بين أقواس]
    MG --> GEN
    MT --> GEN

    GEN[طالما المتبقي من المرشحين > 0] --> OPT[call_optimizer_server_func meta_prompt, T]
    OPT --> PARSE{تحليل المخرج}
    PARSE -->|GPT| PINS[استخراج بين وسوم INS أو Start]
    PARSE -->|text-bison| PBR[استخراج بين أقواس مربعة]
    PINS --> DEDUP
    PBR --> DEDUP
    DEDUP[إزالة تكرار MD5] --> FILT{مرشحات}
    FILT -->|طول > 500| SKIP1[تخطي]
    FILT -->|gsm8k وفيه رقم| SKIP2[تخطي]
    FILT -->|يحتوي INS| SKIP3[تخطي]
    FILT -->|مقبول| EVALN[evaluate_single_instruction على train]

    EVALN --> GP[gen_prompt instruction_pos + include_qa]
    GP --> SCOR[call_scorer_server_func]
    SCOR --> MET[تطبيع metrics + دقة]
    MET --> HIST[إلحاق الدرجة؛ تحديث الأخطاء]
    HIST --> PE{i_step % eval_interval == 0؟}
    PE -->|نعم| EVALH[تقييم طية eval]
    PE -->|لا| STEP
    EVALH --> STEP
    STEP -->|انتهى| BEST[أفضل التعليمات + ملفات CSV]
  end

  subgraph EVALP["evaluate_instructions — قائمة ثابتة"]
    direction TB
    EV --> ELOOP[لكل instruction]
    ELOOP --> EFOLD{طية train و/أو test}
    EFOLD --> ESC[evaluate_single_instruction]
    ESC --> EOUT[جداول الدقة]
  end

  subgraph LRP["الانحدار الخطي"]
    direction TB
    LR --> LMETA[أمر ميتا: تصغير f(w,b)؛ سجل الأزواج]
    LMETA --> LOPT[المحسّن يقترح w,b جديد]
    LOPT --> LPARSE[تحليل w, b]
    LPARSE --> LOBJ[تقييم الهدف؛ الإبقاء إن أفضل]
    LOBJ --> LMETA
  end

  subgraph TSPP["TSP"]
    direction TB
    TSP --> TMETA[أمر ميتا: مسارات + أطوال]
    TMETA --> TOPT[اقتراح وسم trace]
    TOPT --> TVAL[التحقق من الجولة؛ درجة الطول]
    TVAL --> TMETA
  end

  subgraph API["prompt_utils"]
    direction LR
    OA[OpenAI + إعادة المحاولة]
    PA[PaLM text-bison + إعادة المحاولة]
  end

  OPT -.-> API
  SCOR -.-> API

  BEST --> END([مخرجات: سجلات · meta_prompts · أفضل تعليمات · configs])
  EOUT --> END
```
