# Self-Refine Full System Graph — English

```mermaid
flowchart TD
  A[Paper input x + model M + prompts p_gen p_fb p_refine] --> G[Initial generation y0 = M(p_gen || x)]
  G --> L{For t = 0..max or until stop}
  L --> FB[Feedback fb_t = M(p_fb || x || y_t)]
  FB --> STOP{stop(fb_t,t)?}
  STOP -->|yes| RETURN[Return latest y_t]
  STOP -->|no| REF[Refine y_t+1 = M(p_refine || x || y0 || fb0 ... y_t || fb_t)]
  REF --> HIST[Append output and feedback to history]
  HIST --> L

  subgraph REPO[Repository execution paths]
    R0[Choose task run script] --> ACR[Acronym generation]
    R0 --> MCTS[Acronym MCTS]
    R0 --> CG[CommonGen]
    R0 --> GSM[GSM math]
    R0 --> PIE[PIE code optimization]
    R0 --> RESP[Dialogue response generation]
    R0 --> SENT[Sentiment reversal]
    R0 --> READ[Code readability]
    R0 --> VISUAL[Visual Self-Refine GPT-4V notebook]
  end

  subgraph PROMPT_BUILD[Prompt construction]
    PF[Prompt files under data/prompt and docs] --> INITP[Init prompt examples]
    PF --> FBP[Feedback prompt examples]
    PF --> ITERP[Iterate/refine prompt examples]
    PYT[Python templates and prefixes] --> QUERY[Runtime query construction]
    INITP --> QUERY
    FBP --> QUERY
    ITERP --> QUERY
  end

  QUERY --> API[OpenaiAPIWrapper.call]
  API --> PARSE[Parse first response and task-specific fields]
  PARSE --> TASKSTOP{Task-specific stop / parse decisions}

  subgraph ACRONYM[Acronym iterative loop]
    ACR --> AI[TaskInit creates acronym]
    AI --> AF[Feedback scores acronym]
    AF --> ASCORE[Parse Total score]
    ASCORE --> ALOOP{while n_attempts < max_attempts}
    ALOOP -->|attempt 0| AI
    ALOOP -->|attempt > 0| AIT[TaskIterate uses acronym-score history]
    AIT --> AF
    ASCORE --> AKEEP{total_score >= 0?}
    AKEEP -->|yes| AHIST[Add to history]
    AKEEP -->|no| ASKIP[Skip history update]
    AHIST --> ALOOP
    ASKIP --> ALOOP
  end

  subgraph ACRMCTS[Acronym MCTS loop]
    MCTS --> ROOT[Generate root acronym and score]
    ROOT --> INITC[Generate initial children]
    INITC --> MLOOP{for iterations}
    MLOOP --> SEL[Select node with UCB1]
    SEL --> EXP[Expand using task_iterate]
    EXP --> DUP{new acronym already expanded?}
    DUP -->|yes| EXP
    DUP -->|no| SIM[Simulate by feedback scoring]
    SIM --> BACK[Backpropagate value to parents]
    BACK --> MLOOP
  end

  subgraph COMMONGEN[CommonGen loop]
    CG --> CGI[Init sentence from concepts]
    CGI --> CGF[Feedback: missing concepts and commonsense]
    CGF --> CGSTOP{concept_feedback == none and commonsense_feedback == none?}
    CGSTOP -->|yes| CGRET[Return sent_to_fb]
    CGSTOP -->|no and attempts remain| CGI2[Iterate sentence using history]
    CGI2 --> CGF
  end

  subgraph GSMFLOW[GSM math loop]
    GSM --> GSI[Generate initial Python solution]
    GSI --> GSF[Feedback may include improved solution]
    GSF --> GSCOR{feedback contains it is correct?}
    GSCOR -->|yes| GSRET[Stop and return logs]
    GSCOR -->|no and attempts remain| GSUPD[Set solution = improved solution]
    GSUPD --> GSF
  end

  subgraph PIEF[PIE code optimization loop]
    PIE --> PI[Generate optimized code]
    PI --> PFDB[Generate optimization feedback]
    PFDB --> PIT{max attempts reached?}
    PIT -->|no| PIR[Iterate code using original code current code and feedback]
    PIR --> PFDB
    PIT -->|yes| PIRET[Write outputs/logs]
  end

  subgraph RESPF[Response generation loop]
    RESP --> RI[Initial response]
    RI --> RF[FED/GPT feedback]
    RF --> RS{max attempts or feedback sufficient?}
    RS -->|no| RR[Iterate response using feedback history]
    RR --> RF
    RS -->|yes| RRET[Write generations]
  end

  subgraph SENTF[Sentiment reversal loop]
    SENT --> SI[Initial transferred review]
    SI --> SM[Measure sentiment]
    SM --> SF[Generate feedback]
    SF --> SADD{Need explicit Try again suffix?}
    SADD -->|yes| SAPP[Append Try again]
    SADD -->|no| SHIST[Update histories]
    SAPP --> SHIST
    SHIST --> SAT{n_attempts < max_attempts?}
    SAT -->|yes| SIT[Iterate transfer using history and feedback]
    SIT --> SM
    SAT -->|no| SRET[Write logs]
  end


  subgraph VISUALFLOW[Visual Self-Refine GPT-4V notebook]
    VISUAL --> VOBJ[Choose object_name and n_refine_loop]
    VOBJ --> VINIT[get_initial_latex prompt to GPT-4]
    VINIT --> VRENDER[Render LaTeX/TikZ to base64 image]
    VRENDER --> VLOOP{for i in n_refine_loop}
    VLOOP --> VIMG{image available?}
    VIMG -->|no| VSTOP[Break visual loop]
    VIMG -->|yes| VPROMPT[get_refinement_prompt asks GPT-4V to inspect image and rewrite TikZ]
    VPROMPT --> VCALL[vlm_call sends image plus latex code]
    VCALL --> VEXTRACT[Extract latex block]
    VEXTRACT --> VUPDATE[Update init_code and append results]
    VUPDATE --> VLOOP
    VCALL --> VERR{exception?}
    VERR -->|exceptions budget remains| VLOOP
    VERR -->|budget exhausted| VSTOP
    VINIT --> VFIX[fix_latex repair prompt if compile error log exists]
  end

  TASKSTOP --> OUTPUTS[Outputs: JSONL logs, task scores, generated/refined text/code, prompt histories]

```
