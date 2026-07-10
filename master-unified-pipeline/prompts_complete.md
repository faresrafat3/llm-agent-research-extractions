# ARSENAL — Master Prompt Library

Unified prompt catalog combining the strongest prompt patterns from all 7 systems. Placeholders use `{{double_braces}}`.

---

## P0 — Technique Router (Prompt Report)

### P0.1 Task classifier / family router

```text
You are a prompting-technique router. Given a task, select the best technique families
from this taxonomy and which ARSENAL layers to activate.

TAXONOMY FAMILIES:
1. In-Context Learning (Zero-Shot, Few-Shot, KNN, Vote-K, SG-ICL, APE instruction selection)
2. Thought Generation (CoT, Zero-Shot CoT, Analogical, Step-Back, Auto-CoT, ...)
3. Decomposition (Least-to-Most, Plan-and-Solve, ToT, PoT, Skeleton-of-Thought, ...)
4. Ensembling (Self-Consistency, DiVeRSe, USP, Prompt Paraphrasing)
5. Self-Criticism (Self-Refine, CoVe, Self-Verification, Reflexion, ReAct)
6. Answer/Prompt Engineering (verbalizer, extractor, APE, OPRO, Meta-Prompting)
7. Agents / Tools (ReAct, code agents, tool use)
8. Multilingual / Multimodal / Evaluation (as applicable)

TASK:
{{task_spec}}

MODALITY: {{modality}}
DEMOS_AVAILABLE: {{demos_available}}
TOOLS_AVAILABLE: {{tools}}
BUDGET: tokens={{token_budget}}, latency={{latency}}, trials={{max_trials}}

Return JSON:
{
  "families": [...],
  "methods": [...],
  "activate": {
    "ape": bool,
    "meta": bool,
    "lats": bool,
    "refine": bool,
    "reflexion": bool,
    "stages": bool
  },
  "rationale": "..."
}
```

---

## P1 — APE Instruction Optimizer

### P1.1 Forward generation template (from APE)

```text
I gave a friend an instruction and some inputs. The friend read the instruction and
wrote an output for every one of the inputs. Here are the input-output pairs:

{{full_DEMO}}

The instruction was: [APE]
```

### P1.2 Evaluation template

```text
Instruction: [PROMPT]
Input: [INPUT]
Output: [OUTPUT]
```

### P1.3 Demos packing

```text
Input: {{input}}
Output: {{output}}
```
(repeated for k demos; joined as `[full_DEMO]`)

### P1.4 Bandit / likelihood scoring instruction (meta)

```text
Score how well the candidate instruction explains the mapping from inputs to outputs.
Prefer instructions that are concise, general, and correct on held-out pairs.
Candidate instruction:
{{candidate_prompt}}
```

---

## P2 — Meta Conductor (Meta-Prompting)

### P2.1 Meta-prompting instruction (core)

```text
You are Meta-Model, a conductor. Break the user's problem into subtasks and solve them
by calling experts. Experts are instances of the same language model with specialized
instructions. You may also call Expert Python for code.

FORMAT for expert call:
Expert {{ExpertName}}:
{{instructions to the expert}}

FORMAT for final answer:
>> FINAL ANSWER:
{{answer}}

Rules:
- One expert call at a time.
- After each expert reply, verify and integrate before the next call.
- Prefer Expert Python for arithmetic, search, simulation, and verification.
- If code must be executed, the Python expert should end with: Please run this code!
```

### P2.2 Intermediate feedback append

```text
[Expert {{name}} output]
{{expert_output}}

Continue as Meta-Model. Either call another expert or produce >> FINAL ANSWER:
```

### P2.3 Expert generic instruction

```text
You are {{ExpertName}}. Follow the instructions below carefully and produce only your
expert contribution (no meta-commentary).

{{expert_instructions}}
```

### P2.4 Format-error retry

```text
Your previous response was neither a valid expert call nor a final answer.
Respond with either:
  Expert <Name>:
  <instructions>
or
  >> FINAL ANSWER:
  <answer>
```

---

## P3 — Tree Search (ToT baseline + LATS full)

### P3.0 Search mode router (ARSENAL L3)

```text
Choose tree-search mode for this subtask.
- tot: offline puzzle / fixed-step reasoning / constrained writing (BFS beam or DFS)
- lats: interactive env, tools, long-horizon actions, unit-test loops (MCTS/UCT)
- cascade: run tot first; if best score < {{tau}} or env required, escalate to lats

Task: {{task_spec}}
Interactive env/tools: {{has_env}}
Budget: {{budget}}
Return JSON: {"mode": "tot|lats|cascade", "beam_b": int, "mcts_N": int, "rationale": "..."}
```

### P3.0b ToT propose next thought (from ToT Game24/crosswords pattern)

```text
Given the current partial solution state, list diverse possible next steps.
Current state:
{{state}}
Possible next steps:
```

### P3.0c ToT value labels (sure/likely/impossible pattern)

```text
Evaluate if this partial state can reach a valid final solution.
State: {{state}}
Answer with one of: sure / likely / impossible
and a one-line justification.
```

### P3.0d ToT vote among candidates (creative-writing pattern)

```text
Given an instruction and several choices, decide which choice is most promising.
Analyze each choice, then conclude: "The best choice is {s}" with integer id s.
Instruction: {{instruction}}
{{choices_block}}
```

### P3.1 LATS Expansion (thought/action)

```text
You are exploring solutions with tree search.
Current state:
{{state}}

Previous reflections (if any):
{{reflections}}

Propose {{width}} diverse next thoughts/actions. For each, output:
Thought: ...
Action: ...
```

### P3.2 Value / scoring

```text
Evaluate how promising this partial trajectory is for solving the task.
Trajectory:
{{trajectory}}

Return a scalar value in [0, 1] and a one-line justification.
Value: 
```

### P3.3 Failed-trajectory self-reflection (LATS ∩ Reflexion)

```text
The following trajectory failed.
Task: {{task}}
Trajectory: {{trajectory}}
Feedback/error: {{feedback}}

Write a short reflection: what went wrong and what to try differently next.
```

---

## P4 — Self-Refine Local Polisher

### P4.1 Initial generation

```text
{{task_instruction}}

Input:
{{x}}

Produce the best first draft.
```

### P4.2 Multi-aspect feedback

```text
You are a critical reviewer. Evaluate the candidate on these aspects:
{{aspect_list}}

Input:
{{x}}

Candidate:
{{y_t}}

For each aspect: score + brief critique. End with:
Total score: {{score}}/{{max}}
Overall: ...
Stop indicator (if perfect): {{stop_phrase}}
```

### P4.3 History-aware refine

```text
Improve the candidate using the feedback history. Do not repeat previous mistakes.

Input:
{{x}}

History:
{{y0}}
Feedback0: {{fb0}}
...
{{y_t}}
Feedback_t: {{fb_t}}

Write the improved version only.
```

### P4.4 Visual refine (from Visual Self-Refine)

```text
You are given an image of the rendered figure and the current TikZ/LaTeX source.
Identify visual defects and return a full corrected LaTeX block.

Image: {{image}}
Code:
{{latex_code}}
```

### P4.5 LaTeX repair

```text
The following LaTeX failed to compile. Fix it.

Code:
{{latex_code}}

Log:
{{compile_log}}
```

---

## P5 — Reflexion Episodic Memory

### P5.1 Actor with memory (ReAct-style)

```text
Solve the task. You may use thoughts and actions.

Task:
{{task}}

Relevant lessons from past trials:
{{memory_window}}

Continue until done. Format:
Thought: ...
Action: ...
```

### P5.2 Verbal reflection after failure

```text
You failed this trial. Produce a concise reflection to help a future attempt.

Task: {{task}}
Trajectory: {{trajectory}}
Environment/test feedback: {{feedback}}

Reflection (2-5 sentences, actionable):
```

### P5.3 Programming self-reflection

```text
The code failed tests.

Problem:
{{problem}}

Code:
{{code}}

Test/compiler feedback:
{{test_feedback}}

Explain the bugs and how to fix them in the next attempt.
```

---

## P6 — Progressive Stages (AI Scientist v2)

### P6.1 Ideation

```text
Generate a novel research idea for:
{{workshop_description}}

Previous ideas (avoid duplicates):
{{prev_ideas}}

You may:
ACTION: SearchSemanticScholar
ARGUMENTS: {"query": "..."}

or

ACTION: FinalizeIdea
ARGUMENTS: {idea JSON with Name, Title, Short Hypothesis, Related Work, Abstract, Experiments, Risk Factors and Limitations}
```

### P6.2 Ideation reflection

```text
Reflect on the current idea (round {{current_round}}/{{num_reflections}}).
Last tool results:
{{last_tool_results}}

Improve the idea or FinalizeIdea / SearchSemanticScholar as needed.
```

### P6.3 BFTS draft / debug / improve

```text
Stage goal: {{stage_goal}}
Parent node summary: {{parent_summary}}
Memory: {{memory_summary}}

Action mode: {{draft|debug|improve|hyperparam|ablate}}

Write complete experiment code and analysis plan.
```

### P6.4 Metric parse

```text
Extract structured metrics from this experiment log.
Log:
{{log}}

Return JSON: {"metrics": {...}, "success": bool, "notes": "..."}
```

### P6.5 Plot + VLM feedback

```text
Generate plotting code for these results.
Then (VLM): review the figure for clarity, labels, and caption quality.
```

### P6.6 Citation gather

```text
Find BibTeX citations relevant to:
{{idea_and_report}}
Current bibliography:
{{current_bib}}
Use Semantic Scholar search; add only high-quality relevant papers.
```

### P6.7 Writeup + reflection

```text
Write a conference-style paper in LaTeX using:
Idea: {{idea}}
Experiments/summaries: {{summaries}}
Figures: {{figure_list}}
Citations: {{bib}}

Then reflect: fix clarity, claims vs evidence, page limits, figure references.
```

### P6.8 Peer review

```text
You are an expert peer reviewer. Review this paper for novelty, soundness,
clarity, and significance. Return structured scores and free-text critique.
```

---

## P7 — Ensemble / Answer engineering (Prompt Report)

### P7.1 Self-Consistency wrapper

```text
Solve the problem. Show reasoning, then the answer after "Answer:".
We will sample n={{n}} times and majority-vote.
Problem: {{x}}
```

### P7.2 Zero-Shot CoT

```text
{{x}}

Let's think step by step.
```

### P7.3 Plan-and-Solve

```text
{{x}}

Let's first understand the problem and devise a plan to solve it.
Then, let's carry out the plan and solve the problem step by step.
```

---

## Prompt wiring map

| Prompt ID | Used by | Consumes | Produces |
|---|---|---|---|
| P0.1 | L0 | task_spec | route JSON |
| P1.* | L1 | demos | candidate prompts / scores |
| P2.* | L2 | query, experts | final answer / expert log |
| P3.* | L3 | state, tree | children / values / reflections |
| P4.* | L4 | x, y_t | fb_t, y_{t+1} |
| P5.* | L5 | trajectory, memory | action / reflection |
| P6.* | L6 | idea, stage, logs | code, metrics, paper, review |
| P7.* | L0/L2 optional | x | reasoning + answer |

## Composition example

1. **P0.1** → activate ape+meta+lats+refine+reflexion+stages  
2. **P1.1/P1.2** → best task instruction  
3. **P2.1** conductor uses instruction  
4. Expert TreeSearch uses **P3.1/P3.2**  
5. Each leaf polished with **P4.2/P4.3**  
6. Failure → **P5.2** into memory for next trial  
7. Stage shell uses **P6.3–P6.8** for production  
