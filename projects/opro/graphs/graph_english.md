# OPRO — Logic Graph (English)

Paper: https://arxiv.org/abs/2309.03409  
Code: https://github.com/google-deepmind/opro  
Commit: `a76bdce2cbf6d4a0d1e570a6fcfe17be9c2abdd7`

```mermaid
flowchart TD
  %% OPRO — official code logic graph (English)
  %% Paper arXiv:2309.03409 | Code google-deepmind/opro @ a76bdce

  START([Start]) --> MODE{Entry script?}
  MODE -->|optimize_instructions| IO[optimize_instructions.main]
  MODE -->|evaluate_instructions| EV[evaluate_instructions.main]
  MODE -->|optimize_linear_regression| LR[Linear regression OPRO]
  MODE -->|optimize_tsp| TSP[TSP OPRO]

  IO --> LOAD[Load dataset gsm8k / bbh / mmlu]
  LOAD --> SPLIT[Train / eval / test indices]
  SPLIT --> BIND[Bind scorer + optimizer call_server_func]
  BIND --> EVOL[run_evolution]

  subgraph EVO["run_evolution — instruction optimization"]
    direction TB
    EVOL --> INIT[For each initial_instruction]
    INIT --> SC0[evaluate_single_instruction on train]
    SC0 --> HIST0[Append instruction, score, step=-1]
    HIST0 --> WRONG[Update wrong_questions counters]
    WRONG --> STEP{for i_step in num_search_steps}

    STEP --> TEMP{temperature schedule?}
    TEMP -->|constant| TC[T = T0]
    TEMP -->|linear_increase| TL[T = T0 + progress * (Tend-T0)]
    TC --> FS
    TL --> FS

    FS{few_shot_qa_pairs?}
    FS -->|yes| FSEL{selection criteria}
    FSEL -->|accumulative_most_frequent| FA[Most wrong since start]
    FSEL -->|current_most_frequent| FC[Most wrong under current meta set]
    FSEL -->|constant| FK[Fixed seed subset]
    FSEL -->|random| FR[Resample each step]
    FA --> META
    FC --> META
    FK --> META
    FR --> META
    FS -->|no| META[gen_meta_prompt]

    META --> MTYPE{meta_prompt_type?}
    MTYPE -->|both_instructions_and_exemplars| MB[History scores + optional exemplars]
    MTYPE -->|instructions_only| MI[Compact task description + history]
    MB --> MPOS
    MI --> MPOS
    MPOS{optimizer model?}
    MPOS -->|GPT| MG[Headers with INS/Start tags + closing generate higher score]
    MPOS -->|text-bison| MT[Texts with scores ascending + write in brackets]
    MG --> GEN
    MT --> GEN

    GEN[while remaining candidates > 0] --> OPT[call_optimizer_server_func meta_prompt, T]
    OPT --> PARSE{parse output}
    PARSE -->|GPT| PINS[Extract between INS or Start tags]
    PARSE -->|text-bison| PBR[Extract square brackets]
    PINS --> DEDUP
    PBR --> DEDUP
    DEDUP[MD5 dedupe vs prior] --> FILT{filters}
    FILT -->|len > 500| SKIP1[Skip]
    FILT -->|gsm8k and has digit| SKIP2[Skip]
    FILT -->|contains INS| SKIP3[Skip]
    FILT -->|ok| EVALN[evaluate_single_instruction on train]

    EVALN --> GP[gen_prompt instruction_pos + include_qa]
    GP --> SCOR[call_scorer_server_func]
    SCOR --> MET[metrics normalize + accuracy]
    MET --> HIST[Append score; update wrong counters]
    HIST --> PE{i_step % eval_interval == 0?}
    PE -->|yes| EVALH[Eval fold scoring]
    PE -->|no| STEP
    EVALH --> STEP
    STEP -->|done| BEST[Best instructions by score + saved CSVs]
  end

  subgraph EVALP["evaluate_instructions — fixed list"]
    direction TB
    EV --> ELOOP[For each instruction]
    ELOOP --> EFOLD{train and/or test fold}
    EFOLD --> ESC[evaluate_single_instruction]
    ESC --> EOUT[Accuracy tables]
  end

  subgraph LRP["Linear regression"]
    direction TB
    LR --> LMETA[Meta-prompt: minimize f(w,b); history pairs]
    LMETA --> LOPT[Optimizer proposes new w,b]
    LOPT --> LPARSE[Parse w, b]
    LPARSE --> LOBJ[Evaluate objective; keep if better]
    LOBJ --> LMETA
  end

  subgraph TSPP["TSP"]
    direction TB
    TSP --> TMETA[Meta-prompt: traces + lengths]
    TMETA --> TOPT[Propose trace tags]
    TOPT --> TVAL[Validate tour; score length]
    TVAL --> TMETA
  end

  subgraph API["prompt_utils"]
    direction LR
    OA[OpenAI ChatCompletion + retries]
    PA[PaLM text-bison + retries]
  end

  OPT -.-> API
  SCOR -.-> API

  BEST --> END([Outputs: histories · meta_prompts · best instructions · configs])
  EOUT --> END
```
