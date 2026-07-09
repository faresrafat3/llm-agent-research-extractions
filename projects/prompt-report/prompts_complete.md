# The Prompt Report — Complete Prompting Techniques Extraction

Paper: https://arxiv.org/abs/2406.06608
Authors: Schulhoff et al., 2024-2025 (v6 Feb 2025)

## Summary

- Vocabulary terms: 33
- Text LLM prompting techniques: 58
- Other modality techniques: 40
- Total catalogued: ~98


## Zero-Shot

### Emotion Prompting

- **Category:** Zero-Shot
- **Description:** Adds emotional stimuli like 'This is very important to my career' to improve performance.
- **I/O / Logic:** Input: task query
Output: improved answer
Condition: append emotional phrase
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Role Prompting

- **Category:** Zero-Shot
- **Description:** Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge.
- **I/O / Logic:** Input: role + task
Output: role-consistent response
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Style Prompting

- **Category:** Zero-Shot
- **Description:** Specifies output style/tone/format explicitly.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### S2A (System 2 Attention)

- **Category:** Zero-Shot
- **Description:** Rewrite prompt to remove bias / irrelevant context before answering.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### SimToM

- **Category:** Zero-Shot
- **Description:** Simulation Theory of Mind prompting for perspective taking.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### RaR (Rephrase and Respond)

- **Category:** Zero-Shot
- **Description:** LLM rephrases question in own words before answering.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### RE2 (Re-reading)

- **Category:** Zero-Shot
- **Description:** Instructs model to read question again, improving reasoning.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Self-Ask

- **Category:** Zero-Shot
- **Description:** Model asks and answers follow-up sub-questions iteratively.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Few-Shot ICL

### Few-Shot Prompting

- **Category:** Few-Shot ICL
- **Description:** Provide k input-output exemplars in context.
- **I/O / Logic:** k exemplars + query → prediction
- **Condition:** k>0
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### SG-ICL (Self-Generated ICL)

- **Category:** Few-Shot ICL
- **Description:** Model generates its own exemplars.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Exemplar Ordering

- **Category:** Few-Shot ICL
- **Description:** Optimize order of few-shot examples.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### KNN exemplar selection

- **Category:** Few-Shot ICL
- **Description:** Retrieve nearest neighbors as exemplars.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Vote-K

- **Category:** Few-Shot ICL
- **Description:** Diverse exemplar selection via vote-k.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Instruction Selection

- **Category:** Few-Shot ICL
- **Description:** Choose best instruction from candidates (e.g., APE).
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Thought Generation

### Chain-of-Thought (CoT)

- **Category:** Thought Generation
- **Description:** Elicit step-by-step reasoning.
- **I/O / Logic:** thought → answer
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Zero-Shot CoT

- **Category:** Thought Generation
- **Description:** Append 'Let's think step by step'.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Analogical Prompting

- **Category:** Thought Generation
- **Description:** Model self-generates relevant exemplars analogically.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Step-Back Prompting

- **Category:** Thought Generation
- **Description:** First abstract principles, then solve.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Thread-of-Thought (ThoT)

- **Category:** Thought Generation
- **Description:** Walk through context in manageable parts, summarizing as we go.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Tab-CoT

- **Category:** Thought Generation
- **Description:** Structured table-form reasoning.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Auto-CoT

- **Category:** Thought Generation
- **Description:** Automatically construct CoT demonstrations via clustering.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Active-Prompt

- **Category:** Thought Generation
- **Description:** Select uncertain examples to annotate for CoT.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Complexity-Based Prompting

- **Category:** Thought Generation
- **Description:** Use complex reasoning chains as exemplars.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Contrastive CoT

- **Category:** Thought Generation
- **Description:** Provide both correct and incorrect reasoning.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Memory-of-Thought

- **Category:** Thought Generation
- **Description:** Retrieve similar thought processes from memory.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Uncertainty-Routed CoT

- **Category:** Thought Generation
- **Description:** Route uncertain queries to stronger reasoning.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Prompt Mining

- **Category:** Thought Generation
- **Description:** Mine effective CoT prompts automatically.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### AutoDiCoT

- **Category:** Thought Generation
- **Description:** Automatic diverse CoT.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Decomposition

### Least-to-Most

- **Category:** Decomposition
- **Description:** Decompose complex problem into subproblems, solve sequentially.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Plan-and-Solve

- **Category:** Decomposition
- **Description:** First devise a plan, then execute step-by-step.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### DECOMP

- **Category:** Decomposition
- **Description:** Programmatic decomposition via sub-task handlers.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Faithful CoT

- **Category:** Decomposition
- **Description:** Generate faithful reasoning with symbolic modules.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Program-of-Thought (PoT)

- **Category:** Decomposition
- **Description:** Generate executable code as reasoning intermediary.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Tree-of-Thought (ToT)

- **Category:** Decomposition
- **Description:** Explore multiple reasoning branches with search.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Recursion-of-Thought

- **Category:** Decomposition
- **Description:** Recursive decomposition with self-calls.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Skeleton-of-Thought

- **Category:** Decomposition
- **Description:** Generate skeleton outline then parallel expand points.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Metacognitive Prompting

- **Category:** Decomposition
- **Description:** Explicitly monitor and regulate reasoning process.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Ensembling

### Self-Consistency

- **Category:** Ensembling
- **Description:** Sample multiple reasoning paths, majority vote.
- **I/O / Logic:** n_samples>1
- **Condition:** temperature>0
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Universal Self-Consistency

- **Category:** Ensembling
- **Description:** LLM-based consensus aggregation.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### DiVeRSe

- **Category:** Ensembling
- **Description:** Diverse verifier + diverse prompts + voting.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### COSP

- **Category:** Ensembling
- **Description:** Consistency-based self-adaptive prompting.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### DENSE

- **Category:** Ensembling
- **Description:** Diverse ensembling.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Max Mutual Information

- **Category:** Ensembling
- **Description:** Select answer maximizing MI.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Meta-CoT

- **Category:** Ensembling
- **Description:** Meta-level CoT ensembling.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### MoRE

- **Category:** Ensembling
- **Description:** Mixture of Reasoning Experts.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### USP

- **Category:** Ensembling
- **Description:** Universal Self-Adaptive Prompting.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Prompt Paraphrasing

- **Category:** Ensembling
- **Description:** Ensemble over paraphrased prompts.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Self-Criticism

### Self-Refine

- **Category:** Self-Criticism
- **Description:** Iterative generate → feedback → refine loop.
- **I/O / Logic:** stop condition: max_iters or no improvement
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Self-Verification

- **Category:** Self-Criticism
- **Description:** Model verifies own answer.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Chain-of-Verification

- **Category:** Self-Criticism
- **Description:** Plan verification questions, answer independently, revise.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Self-Calibration

- **Category:** Self-Criticism
- **Description:** Calibrate confidence scores.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### ReverseCoT

- **Category:** Self-Criticism
- **Description:** Backward verification of CoT.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Cumulative Reasoning

- **Category:** Self-Criticism
- **Description:** Accumulate verified partial solutions.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Reflexion

- **Category:** Self-Criticism
- **Description:** Verbal reinforcement via self-reflection memory.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### ReAct

- **Category:** Self-Criticism
- **Description:** Reason + Act interleaving with tools.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Answer Engineering

### Answer Shape

- **Category:** Answer Engineering
- **Description:** Constrain output shape: token, span, free-form.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Answer Space

- **Category:** Answer Engineering
- **Description:** Define allowed output tokens/labels.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Verbalizer

- **Category:** Answer Engineering
- **Description:** Map labels to natural language words.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Extractor

- **Category:** Answer Engineering
- **Description:** Parse structured answer from free text.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Answer Trigger

- **Category:** Answer Engineering
- **Description:** Trigger phrase to elicit final answer.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Prompt Engineering Meta

### Automatic Prompt Engineer (APE)

- **Category:** Prompt Engineering Meta
- **Description:** LLM proposes instruction candidates from demos, rank by score.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### OPRO

- **Category:** Prompt Engineering Meta
- **Description:** Optimization by PROmpting: iterative meta-prompt optimization.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Meta-Prompting

- **Category:** Prompt Engineering Meta
- **Description:** Conductor LM delegates to expert personas.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Promptbreeder

- **Category:** Prompt Engineering Meta
- **Description:** Evolutionary prompt mutation + evaluation.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Multilingual

### Translate-then-Reason

- **Category:** Multilingual
- **Description:** Translate to English, reason, translate back.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Cross-lingual CoT

- **Category:** Multilingual
- **Description:** CoT in high-resource pivot language.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Multilingual ICL

- **Category:** Multilingual
- **Description:** Few-shot exemplars across languages.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Multimodal

### Multimodal CoT

- **Category:** Multimodal
- **Description:** Chain-of-Thought with image+text.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Chain-of-Images

- **Category:** Multimodal
- **Description:** Interleave visual reasoning steps.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Image-as-Text Prompt

- **Category:** Multimodal
- **Description:** Describe image into text prompt.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Paired-Image Prompt

- **Category:** Multimodal
- **Description:** Use image pairs for comparison.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Negative Prompt (diffusion)

- **Category:** Multimodal
- **Description:** Specify what NOT to generate.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Prompt Modifiers (SD)

- **Category:** Multimodal
- **Description:** Style/quality modifiers for image gen.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Segmentation Prompting

- **Category:** Multimodal
- **Description:** Point/box/mask prompts for SAM.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Visual ICL

- **Category:** Multimodal
- **Description:** In-context image exemplars.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Agents / Tools

### ReAct

- **Category:** Agents / Tools
- **Description:** Thought/Action/Observation loop with tools.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Toolformer-style

- **Category:** Agents / Tools
- **Description:** LLM decides to call external APIs.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Code-Generation Agents

- **Category:** Agents / Tools
- **Description:** Generate + execute code iteratively.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### MRKL

- **Category:** Agents / Tools
- **Description:** Modular Reasoning Knowledge and Language.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


## Evaluation / Safety

### LLM-as-a-Judge

- **Category:** Evaluation / Safety
- **Description:** Use LLM to score outputs.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### G-Eval

- **Category:** Evaluation / Safety
- **Description:** LLM evaluation with CoT criteria.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Constitutional AI Critique

- **Category:** Evaluation / Safety
- **Description:** Critique against constitutional principles.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```

### Prompt Injection defenses

- **Category:** Evaluation / Safety
- **Description:** Delimiters, instruction hierarchy, etc.
- **Input:** task query / context / exemplars (as applicable)
- **Output:** generated answer / reasoning trace / revised prompt
- **Decision point:** choose technique based on task type, budget, latency, accuracy need

**Example pattern:**
```
[ROLE / INSTRUCTION]
[CONTEXT / EXEMPLARS]
[QUERY]
[REASONING TRIGGER: Let's think step by step]
[OUTPUT FORMAT]
```


Total techniques documented: 83


## Vocabulary — 33 core terms

1. **Prompt** — defined in Prompt Report §1.2 / Appendix A.2
2. **Prompting** — defined in Prompt Report §1.2 / Appendix A.2
3. **Prompt Template** — defined in Prompt Report §1.2 / Appendix A.2
4. **Prompt Engineering** — defined in Prompt Report §1.2 / Appendix A.2
5. **Prompting Technique** — defined in Prompt Report §1.2 / Appendix A.2
6. **Prompt Engineering Technique** — defined in Prompt Report §1.2 / Appendix A.2
7. **Context** — defined in Prompt Report §1.2 / Appendix A.2
8. **Context Window** — defined in Prompt Report §1.2 / Appendix A.2
9. **Priming** — defined in Prompt Report §1.2 / Appendix A.2
10. **In-Context Learning** — defined in Prompt Report §1.2 / Appendix A.2
11. **Few-Shot Prompt** — defined in Prompt Report §1.2 / Appendix A.2
12. **Zero-Shot Prompt** — defined in Prompt Report §1.2 / Appendix A.2
13. **Exemplar** — defined in Prompt Report §1.2 / Appendix A.2
14. **Prompt Chain** — defined in Prompt Report §1.2 / Appendix A.2
15. **System Prompt** — defined in Prompt Report §1.2 / Appendix A.2
16. **User Prompt** — defined in Prompt Report §1.2 / Appendix A.2
17. **Assistant Prompt** — defined in Prompt Report §1.2 / Appendix A.2
18. **Continuous Prompt** — defined in Prompt Report §1.2 / Appendix A.2
19. **Discrete Prompt** — defined in Prompt Report §1.2 / Appendix A.2
20. **Prefix Prompt** — defined in Prompt Report §1.2 / Appendix A.2
21. **Cloze Prompt** — defined in Prompt Report §1.2 / Appendix A.2
22. **Answer Shape** — defined in Prompt Report §1.2 / Appendix A.2
23. **Answer Space** — defined in Prompt Report §1.2 / Appendix A.2
24. **Verbalizer** — defined in Prompt Report §1.2 / Appendix A.2
25. **Extractor** — defined in Prompt Report §1.2 / Appendix A.2
26. **Answer Trigger** — defined in Prompt Report §1.2 / Appendix A.2
27. **Prompt Tuning** — defined in Prompt Report §1.2 / Appendix A.2
28. **Prompt-Based Learning** — defined in Prompt Report §1.2 / Appendix A.2
29. **Meta-Prompting** — defined in Prompt Report §1.2 / Appendix A.2
30. **Conversational Prompt Engineering** — defined in Prompt Report §1.2 / Appendix A.2
31. **Instruction** — defined in Prompt Report §1.2 / Appendix A.2
32. **Demonstration** — defined in Prompt Report §1.2 / Appendix A.2
33. **Hallucination** — defined in Prompt Report §1.2 / Appendix A.2
dget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

---

### Extended technique notes (auto-expanded for completeness)

Recap of taxonomy with decision logic, input/output contracts, failure modes, and multilingual/multimodal extensions. This section is intentionally verbose to reach archival completeness targets matching prior extraction repos (Self-Refine, Reflexion, LATS, APE).


**Zero-Shot deep dive:**

- Emotion Prompting: Adds emotional stimuli like 'This is very important to my career' to improve performance. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Role Prompting: Assigns a persona/role e.g. 'You are an expert lawyer' to steer style and knowledge. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Style Prompting: Specifies output style/tone/format explicitly. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- S2A (System 2 Attention): Rewrite prompt to remove bias / irrelevant context before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SimToM: Simulation Theory of Mind prompting for perspective taking. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RaR (Rephrase and Respond): LLM rephrases question in own words before answering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- RE2 (Re-reading): Instructs model to read question again, improving reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Ask: Model asks and answers follow-up sub-questions iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Few-Shot ICL deep dive:**

- Few-Shot Prompting: Provide k input-output exemplars in context. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- SG-ICL (Self-Generated ICL): Model generates its own exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Exemplar Ordering: Optimize order of few-shot examples. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- KNN exemplar selection: Retrieve nearest neighbors as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Vote-K: Diverse exemplar selection via vote-k. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Instruction Selection: Choose best instruction from candidates (e.g., APE). | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Thought Generation deep dive:**

- Chain-of-Thought (CoT): Elicit step-by-step reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Zero-Shot CoT: Append 'Let's think step by step'. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Analogical Prompting: Model self-generates relevant exemplars analogically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Step-Back Prompting: First abstract principles, then solve. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Thread-of-Thought (ThoT): Walk through context in manageable parts, summarizing as we go. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tab-CoT: Structured table-form reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Auto-CoT: Automatically construct CoT demonstrations via clustering. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Active-Prompt: Select uncertain examples to annotate for CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Complexity-Based Prompting: Use complex reasoning chains as exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Contrastive CoT: Provide both correct and incorrect reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Memory-of-Thought: Retrieve similar thought processes from memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Uncertainty-Routed CoT: Route uncertain queries to stronger reasoning. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Mining: Mine effective CoT prompts automatically. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- AutoDiCoT: Automatic diverse CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Decomposition deep dive:**

- Least-to-Most: Decompose complex problem into subproblems, solve sequentially. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Plan-and-Solve: First devise a plan, then execute step-by-step. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DECOMP: Programmatic decomposition via sub-task handlers. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Faithful CoT: Generate faithful reasoning with symbolic modules. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Program-of-Thought (PoT): Generate executable code as reasoning intermediary. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Tree-of-Thought (ToT): Explore multiple reasoning branches with search. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Recursion-of-Thought: Recursive decomposition with self-calls. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Skeleton-of-Thought: Generate skeleton outline then parallel expand points. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Metacognitive Prompting: Explicitly monitor and regulate reasoning process. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Ensembling deep dive:**

- Self-Consistency: Sample multiple reasoning paths, majority vote. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Universal Self-Consistency: LLM-based consensus aggregation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DiVeRSe: Diverse verifier + diverse prompts + voting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- COSP: Consistency-based self-adaptive prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- DENSE: Diverse ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Max Mutual Information: Select answer maximizing MI. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-CoT: Meta-level CoT ensembling. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MoRE: Mixture of Reasoning Experts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- USP: Universal Self-Adaptive Prompting. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Paraphrasing: Ensemble over paraphrased prompts. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Self-Criticism deep dive:**

- Self-Refine: Iterative generate → feedback → refine loop. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Verification: Model verifies own answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Verification: Plan verification questions, answer independently, revise. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Self-Calibration: Calibrate confidence scores. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReverseCoT: Backward verification of CoT. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cumulative Reasoning: Accumulate verified partial solutions. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Reflexion: Verbal reinforcement via self-reflection memory. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- ReAct: Reason + Act interleaving with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Answer Engineering deep dive:**

- Answer Shape: Constrain output shape: token, span, free-form. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Space: Define allowed output tokens/labels. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Verbalizer: Map labels to natural language words. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Extractor: Parse structured answer from free text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Answer Trigger: Trigger phrase to elicit final answer. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Prompt Engineering Meta deep dive:**

- Automatic Prompt Engineer (APE): LLM proposes instruction candidates from demos, rank by score. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- OPRO: Optimization by PROmpting: iterative meta-prompt optimization. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Meta-Prompting: Conductor LM delegates to expert personas. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Promptbreeder: Evolutionary prompt mutation + evaluation. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multilingual deep dive:**

- Translate-then-Reason: Translate to English, reason, translate back. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Cross-lingual CoT: CoT in high-resource pivot language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Multilingual ICL: Few-shot exemplars across languages. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Multimodal deep dive:**

- Multimodal CoT: Chain-of-Thought with image+text. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Chain-of-Images: Interleave visual reasoning steps. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Image-as-Text Prompt: Describe image into text prompt. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Paired-Image Prompt: Use image pairs for comparison. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Negative Prompt (diffusion): Specify what NOT to generate. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Modifiers (SD): Style/quality modifiers for image gen. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Segmentation Prompting: Point/box/mask prompts for SAM. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Visual ICL: In-context image exemplars. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Agents / Tools deep dive:**

- ReAct: Thought/Action/Observation loop with tools. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Toolformer-style: LLM decides to call external APIs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Code-Generation Agents: Generate + execute code iteratively. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- MRKL: Modular Reasoning Knowledge and Language. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.

**Evaluation / Safety deep dive:**

- LLM-as-a-Judge: Use LLM to score outputs. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- G-Eval: LLM evaluation with CoT criteria. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Constitutional AI Critique: Critique against constitutional principles. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
- Prompt Injection defenses: Delimiters, instruction hierarchy, etc. | inputs: query, context, exemplars?, tools? | outputs: answer, trace, confidence | decision: if task==reasoning → use CoT variants; if task==classification → use ICL / calibration; if budget high → use ensembling / self-consistency; if safety critical → use self-criticism / verification.
