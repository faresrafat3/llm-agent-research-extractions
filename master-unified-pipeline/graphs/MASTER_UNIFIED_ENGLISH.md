# ARSENAL — Master Unified Pipeline Graph (English)

**One system. Seven sources. Nested layers L0–L6.**

| Layer | Role | Source system |
|---|---|---|
| L0 | Technique family router | The Prompt Report |
| L1 | Instruction optimizer | APE |
| L2 | Meta conductor + experts | Meta-Prompting |
| L3 | Tree search (MCTS/UCT) | LATS |
| L4 | Local polish loop | Self-Refine |
| L5 | Verbal episodic memory | Reflexion |
| L6 | Progressive stages + writeup + review | AI Scientist v2 |

## How to read the graph

1. Enter at **User Task** → **L6 Stage Shell**.
2. Each stage opens an **L5 trial loop** with reflection memory.
3. Every trial calls **L0 Router** to activate layers.
4. Optional **L1 APE** ranks instructions.
5. **L2 Meta** dispatches experts (including Python and TreeSearch).
6. **L3 LATS** explores under uncertainty; leaves go to **L4 Self-Refine**.
7. Failures become **L5 reflections** for the next trial.
8. Stage success → multi-seed → plots → next stage → writeup → peer review.

## Mermaid

```mermaid
flowchart TB
  %% ARSENAL — Unified Master Pipeline combining all 7 systems
  %% Sources: AI Scientist v2 | Self-Refine | Reflexion | Meta-Prompting | LATS | APE | Prompt Report

  START([User Task / Research Idea / Query]) --> L6_IN[L6 Progressive Stage Shell<br/>AI Scientist v2]

  subgraph L6["L6 — PROGRESSIVE STAGE SHELL (AI Scientist v2)"]
    direction TB
    L6_IN --> STAGE{Current stage}
    STAGE -->|1 Draft| S1[Stage 1: Initial implementation / draft]
    STAGE -->|2 Tune| S2[Stage 2: Baseline + hyperparameter tuning]
    STAGE -->|3 Improve| S3[Stage 3: Creative research improvements]
    STAGE -->|4 Ablate| S4[Stage 4: Ablation studies]
    S1 --> TRIAL_WRAP
    S2 --> TRIAL_WRAP
    S3 --> TRIAL_WRAP
    S4 --> TRIAL_WRAP

    TRIAL_WRAP[Enter L5 trial loop with empty/fresh memory for stage]

    TRIAL_DONE[Trial stack returns best result] --> BEST{Best node / result found?}
    BEST -->|no| ABORT[Abort pipeline — journal no_best_node]
    BEST -->|yes| MSEED[Multi-seed evaluation]
    MSEED --> PLOTS[Plot generation + VLM feedback + aggregation]
    PLOTS --> STAGE_OK{Stage complete / more stages?}
    STAGE_OK -->|yes next| STAGE
    STAGE_OK -->|all done| WRITEUP_GATE{Writeup enabled?}
  end

  subgraph L5["L5 — EPISODIC VERBAL MEMORY (Reflexion)"]
    direction TB
    TRIAL_WRAP --> MEM_INIT[memory = prior reflections window K]
    MEM_INIT --> TRIAL_LOOP{for trial in 1..max_trials}
    TRIAL_LOOP --> L0_CALL[Call L0 Technique Router]
    INNER_DONE[Inner stack result] --> SUCC{Success?}
    SUCC -->|yes| TRIAL_DONE
    SUCC -->|no retries left| TRIAL_DONE
    SUCC -->|no retries remain| REFLECT[P5 Verbal reflection from trajectory + feedback]
    REFLECT --> MEM_UPD[Append reflection — keep last K]
    MEM_UPD --> TRIAL_LOOP
  end

  subgraph L0["L0 — TECHNIQUE ROUTER (The Prompt Report)"]
    direction TB
    L0_CALL --> TAX[Classify against 58-technique taxonomy<br/>+ agents / multimodal / eval]
    TAX --> FAM{Technique families}
    FAM --> F1[ICL Zero/Few-Shot]
    FAM --> F2[Thought Generation CoT family]
    FAM --> F3[Decomposition ToT/PoT/L2M]
    FAM --> F4[Ensembling Self-Consistency]
    FAM --> F5[Self-Criticism Refine/Reflexion]
    FAM --> F6[Prompt Optimization APE/OPRO]
    FAM --> F7[Agents Tools ReAct]
    F1 & F2 & F3 & F4 & F5 & F6 & F7 --> ACT[Build activate flags]
    ACT --> FLAGS["activate: ape / meta / lats / refine / reflexion / stages"]
    FLAGS --> L1_GATE
  end

  subgraph L1["L1 — INSTRUCTION OPTIMIZER (APE)"]
    direction TB
    L1_GATE{activate.ape AND demos available?}
    L1_GATE -->|no| L1_SKIP[Use default / hand prompts]
    L1_GATE -->|yes| APE_TPL{prompt_gen_template provided?}
    APE_TPL -->|no| APE_CONV[Convert EvalTemplate → GenerationTemplate<br/>PROMPT → APE]
    APE_TPL -->|yes| APE_USE[Use provided GenerationTemplate]
    APE_CONV --> APE_GEN
    APE_USE --> APE_GEN
    APE_GEN[Generate candidates: for num_subsamples<br/>subsample demos → LLM generate]
    APE_GEN --> APE_DEDUP[Deduplicate prompts]
    APE_DEDUP --> APE_EVAL{eval_method?}
    APE_EVAL -->|likelihood| APE_LL[Likelihood: log p output given prompt+input]
    APE_EVAL -->|bandits| APE_UCB[UCB bandit rounds over prompt arms]
    APE_LL --> APE_RANK[Rank prompts by score]
    APE_UCB --> APE_RANK
    APE_RANK --> APE_OUT[best_prompts + demo_fn]
    APE_OUT --> L2_GATE
    L1_SKIP --> L2_GATE
  end

  subgraph L2["L2 — META CONDUCTOR (Meta-Prompting)"]
    direction TB
    L2_GATE{activate.meta?}
    L2_GATE -->|no| L2_SKIP{activate.lats?}
    L2_GATE -->|yes| META_INIT[Init messages: meta instruction + query + memory]
    META_INIT --> META_LOOP{meta round < max_rounds}
    META_LOOP --> META_CALL[Meta-Model generate]
    META_CALL --> META_KIND{Output type?}
    META_KIND -->|Final answer| META_FINAL[Extract FINAL ANSWER]
    META_KIND -->|Invalid| META_ERR[Append format-error feedback]
    META_ERR --> META_LOOP
    META_KIND -->|Expert call| META_EXP[Extract expert name + instructions]
    META_EXP --> EXP_TYPE{Expert type?}
    EXP_TYPE -->|Python| EXP_PY[Expert Python generate]
    EXP_PY --> RUN_Q{Please run this code?}
    RUN_Q -->|yes| EXEC[Execute with timeout — append stdout/err]
    RUN_Q -->|no| EXP_APPEND
    EXEC --> EXP_APPEND
    EXP_TYPE -->|TreeSearch / LATS| L3_CALL
    EXP_TYPE -->|Normal expert| EXP_LM[LM expert generate]
    EXP_LM --> L4_EXP[L4 polish expert draft]
    L4_EXP --> EXP_APPEND[Append expert output + intermediate feedback]
    EXP_APPEND --> META_LOOP
    META_FINAL --> L4_FINAL
    L2_SKIP -->|yes| L3_CALL
    L2_SKIP -->|no| DIRECT[Direct LM generate with routed method]
    DIRECT --> L4_FINAL
  end

  subgraph L3["L3 — TREE SEARCH ENGINE (LATS / MCTS)"]
    direction TB
    L3_CALL[Root node = state / question / problem] --> MCTS{for iteration in 1..N}
    MCTS --> SEL[Select node by UCT]
    SEL --> TERM{Node status?}
    TERM -->|terminal success| L3_WIN[Return successful trajectory]
    TERM -->|terminal fail / exhausted| BACKTRACK[Prune / backtrack]
    BACKTRACK --> MCTS
    TERM -->|expandable| EXPAND[Expand: LM samples thoughts/actions/code width W]
    EXPAND --> VALUE[Evaluate children: LM value + env feedback]
    VALUE --> ROLLOUT[Rollout best child to max depth]
    ROLLOUT --> ROK{Success in rollout?}
    ROK -->|yes| L3_WIN
    ROK -->|no| BPROP[Backpropagate reward/value to root]
    BPROP --> FAIL_STORE[Store failed trajectory]
    FAIL_STORE --> REFL_Q{Unique failures warrant reflection?}
    REFL_Q -->|yes| L3_REFL[Self-reflection prompt → reflections list]
    REFL_Q -->|no| MCTS
    L3_REFL --> MCTS
    L3_WIN --> L4_LEAF
    MCTS -->|budget exhausted| L3_BEST[Best partial trajectory]
    L3_BEST --> L4_LEAF
  end

  subgraph L4["L4 — LOCAL POLISHER (Self-Refine)"]
    direction TB
    L4_LEAF[Candidate leaf / draft y] --> L4_INIT{y exists?}
    L4_FINAL[Candidate for final polish] --> L4_INIT
    L4_INIT -->|no| L4_GEN[y0 = M p_gen || x]
    L4_INIT -->|yes| L4_Y[Use candidate as y_t]
    L4_GEN --> L4_LOOP
    L4_Y --> L4_LOOP{for t in 0..max_iters}
    L4_LOOP --> L4_FB[fb_t = M p_fb || x || y_t<br/>multi-aspect scores]
    L4_FB --> L4_STOP{stop fb_t t ?}
    L4_STOP -->|yes stop phrase or max| L4_OUT[Return y_final + history]
    L4_STOP -->|no| L4_REF[y_t+1 = M p_refine || x || full history]
    L4_REF --> L4_HIST[Append y_t fb_t to history]
    L4_HIST --> L4_LOOP
  end

  L4_OUT --> INNER_DONE

  WRITEUP_GATE -->|no| DELIVER([Deliver stage artifacts + journal])
  WRITEUP_GATE -->|yes| CITE[Citation loop: Semantic Scholar ~20 rounds]
  CITE --> WRITE[Writeup LaTeX / paper generation]
  WRITE --> WREF{Writeup reflection rounds}
  WREF --> WREV[Revise for clarity claims page limits figures]
  WREV --> WREF
  WREF -->|done| PREVIEW{Peer review enabled?}
  PREVIEW -->|yes| PREVIEW_DO[LLM peer review + optional VLM figure review + meta-review]
  PREVIEW -->|no| DELIVER
  PREVIEW_DO --> DELIVER
  ABORT --> DELIVER

  subgraph LEGEND["Pattern sources"]
    direction LR
    LG0[L0 Prompt Report taxonomy routing]
    LG1[L1 APE generate-dedup-evaluate-rank]
    LG2[L2 Meta expert dispatch + Python tool]
    LG3[L3 LATS UCT expand value rollout backprop]
    LG4[L4 Self-Refine gen-feedback-refine-stop]
    LG5[L5 Reflexion verbal memory across trials]
    LG6[L6 AI Scientist stages multi-seed writeup review]
  end

  DELIVER --> END([ARSENAL Deliverable:<br/>prompts · trajectories · artifacts · paper · review · memory])
```

## Companion files

- Raw Mermaid: `MASTER_UNIFIED_ENGLISH.mmd`
- Arabic version: `MASTER_UNIFIED_ARABIC.md` / `.mmd`
- Architecture narrative: `../unified_architecture.md`
- Pattern extraction: `../pattern_extraction.md`
