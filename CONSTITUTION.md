# ARSENAL CONSTITUTION
## Master Universal Prompt Dossier

**Purpose.** A reusable constitution of **domain-agnostic** prompts distilled from 10 extracted systems.  
Use this dossier on *any* project: research, code, writing, freelancing, agents, or product shipping.

**Sources (extractions under `faresrafat3/*`).**

| # | System | Paper / origin | Extraction |
|---|---|---|---|
| 1 | AI Scientist v2 | SakanaAI | `ai-scientist-v2-prompts-extraction` |
| 2 | Self-Refine | arXiv:2303.17651 | `self-refine-full-extraction` |
| 3 | Reflexion | arXiv:2303.11366 | `reflexion-full-extraction` |
| 4 | Meta-Prompting | arXiv:2401.12954 | `meta-prompting-full-extraction` |
| 5 | Tree of Thoughts | arXiv:2305.10601 | `tot-full-extraction` |
| 6 | LATS | arXiv:2310.04406 | `lats-full-extraction` |
| 7 | APE | arXiv:2211.01910 | `ape-full-extraction` |
| 8 | OPRO | arXiv:2309.03409 | `opro-full-extraction` |
| 9 | Voyager | arXiv:2305.16291 | `voyager-full-extraction` |
| 10 | The Prompt Report | arXiv:2406.06608 | `prompt-report-full-extraction` |

**How to read each entry**

- **Source** — paper/system the pattern comes from  
- **Purpose** — one line  
- **Prompt** — full reusable text (`{{placeholders}}`)  
- **When to use** — trigger conditions  
- **Loop condition** — if iterative  
- **Transition condition** — when to stop / hand off  

**Scope rule.** Domain-specific surface forms (Minecraft inventory, Game-of-24 arithmetic, AlfWorld verbs) are **generalized**. The *control logic* of the original prompt is preserved.

**Parent design.** Layers L0–L6 in this repo’s `unified_architecture.md` / `prompts_complete.md`.

---

# PART 1 — HOW TO THINK
*(reasoning · exploration · decision-making)*

---

## C1.1 Zero-Shot Chain of Thought

| Field | Content |
|---|---|
| **Source** | The Prompt Report (CoT family) · Meta-Prompting baseline suffix |
| **Purpose** | Force explicit multi-step reasoning before the answer. |
| **When to use** | Any non-trivial question, plan, or design decision. |
| **Loop condition** | Single pass (or re-run if answer is incoherent). |
| **Transition condition** | A clear final answer exists; if stuck → C1.3 or C1.4. |

**Prompt**

```text
Task:
{{task}}

Constraints:
{{constraints}}

Let's think step by step.
Show intermediate reasoning, then give the final answer clearly labeled.
```

---

## C1.2 Plan-and-Solve

| Field | Content |
|---|---|
| **Source** | The Prompt Report (Decomposition / Plan-and-Solve) |
| **Purpose** | Separate planning from execution to reduce skipped steps. |
| **When to use** | Multi-step work: research plans, code features, client deliverables. |
| **Loop condition** | Optional: revise plan once if execution reveals a flaw. |
| **Transition condition** | Plan is specific enough to execute; then implement without inventing new goals. |

**Prompt**

```text
Problem:
{{problem}}

1) Restate the goal in one sentence.
2) List a short plan (3–8 steps). Each step must be observable/done-able.
3) Execute the plan step by step.
4) State the final deliverable and any residual risks.

Do not skip the plan. Do not add steps that are not required by the goal.
```

---

## C1.3 Propose Next Thoughts (Tree of Thoughts — generate)

| Field | Content |
|---|---|
| **Source** | Tree of Thoughts (propose / expand) · LATS expansion pattern |
| **Purpose** | Branch the solution space instead of committing to one path. |
| **When to use** | Ambiguous design choices, research angles, architectures, product directions. |
| **Loop condition** | For each frontier state, generate `{{width}}` diverse next thoughts. |
| **Transition condition** | Candidates ready for valuation (C1.4) or voting (C1.5). |

**Prompt**

```text
You are exploring solutions with deliberate branching (Tree-of-Thoughts style).

Goal:
{{goal}}

Current partial state:
{{state}}

Prior reflections (if any):
{{reflections}}

Propose {{width}} diverse, concrete next thoughts/steps.
Rules:
- Each must be different in strategy, not only wording.
- Each must move the state closer to the goal or reveal a decisive test.
- No infinite loops; no vague advice.

Format:
1) Thought: ...
   Why it could work: ...
2) Thought: ...
   Why it could work: ...
...
```

---

## C1.4 Value a Partial State (sure / likely / impossible)

| Field | Content |
|---|---|
| **Source** | Tree of Thoughts value prompts · LATS value head |
| **Purpose** | Score whether a partial path can still succeed. |
| **When to use** | After generating branches; before expanding further. |
| **Loop condition** | Score every new candidate; optionally average `{{n_samples}}` judgments. |
| **Transition condition** | Keep top-`{{beam}}` “sure/likely”; prune “impossible”; if all impossible → reflect (C3.3) and re-propose. |

**Prompt**

```text
Evaluate whether this partial solution can still reach a valid final solution.

Goal:
{{goal}}

Partial state / trajectory:
{{state}}

Answer with exactly one label on the last line:
- sure — a clear path exists and constraints are satisfied so far
- likely — promising, but non-trivial risks remain
- impossible — blocked by contradiction, missing prerequisites, or violated constraints

Also give a one-line justification before the label.

Justification: ...
Label: sure|likely|impossible
```

---

## C1.5 Vote Among Candidates

| Field | Content |
|---|---|
| **Source** | Tree of Thoughts (`vote_prompt`) · Prompt Report ensembling |
| **Purpose** | Comparative selection when absolute scores are noisy. |
| **When to use** | Multiple full or partial drafts compete under the same instruction. |
| **Loop condition** | Optional majority over `{{n_votes}}` samples. |
| **Transition condition** | Emit winning id; hand winner to refine (C3) or execute (C5). |

**Prompt**

```text
Given an instruction and several choices, decide which choice is most promising.
Analyze each choice in detail (fit to goal, risks, completeness, cost).
Then conclude in the last line exactly:
The best choice is {{s}}
where {{s}} is the integer id of the choice.

Instruction / goal:
{{instruction}}

Choice 1:
{{choice_1}}

Choice 2:
{{choice_2}}

Choice 3:
{{choice_3}}
```

---

## C1.6 Search Mode Router (ToT vs deep search)

| Field | Content |
|---|---|
| **Source** | ARSENAL L3 router · ToT vs LATS map |
| **Purpose** | Decide cheap deliberate search vs interactive/deep search. |
| **When to use** | Before spending budget on tree search. |
| **Loop condition** | None (routing decision). |
| **Transition condition** | `tot` → C1.3–C1.5; `lats` → C1.3 + env actions + C3.3; `cascade` → ToT then escalate if score < τ. |

**Prompt**

```text
Choose a search mode for this subtask.

- tot: offline / fixed-step reasoning / writing / design (beam or DFS over thoughts)
- lats: interactive tools, long-horizon actions, tests/executors (UCT/MCTS-style)
- cascade: run tot first; if best score < {{tau}} or environment is required, escalate to lats
- off: single-path reasoning is enough

Task:
{{task_spec}}

Interactive env/tools available: {{has_env}}
Budget: {{budget}}

Return JSON only:
{
  "mode": "tot|lats|cascade|off",
  "beam_b": int,
  "max_depth_or_iters": int,
  "rationale": "..."
}
```

---

# PART 2 — HOW TO RESEARCH
*(search · validate · novelty)*

---

## C2.1 Technique / Approach Router

| Field | Content |
|---|---|
| **Source** | The Prompt Report taxonomy · ARSENAL L0 |
| **Purpose** | Pick methods before heavy work. |
| **When to use** | Project start; major phase change. |
| **Loop condition** | Re-route if modality, tools, or budget change. |
| **Transition condition** | Activation flags drive L1–L6 (optimize / conduct / search / refine / memory / ship). |

**Prompt**

```text
You are a technique router for LLM work. Given a task, select the best technique
families and which execution layers to activate.

TAXONOMY FAMILIES:
1. In-Context Learning (Zero/Few-Shot, exemplar selection)
2. Thought Generation (CoT, Plan-and-Solve, step-back, analogical)
3. Decomposition (least-to-most, tree/graph of thoughts, program-of-thought)
4. Ensembling (self-consistency, multi-sample vote)
5. Self-Criticism (self-refine, verification, reflexion)
6. Prompt Optimization (instruction search: APE-like / OPRO-like)
7. Agents / Tools (ReAct, code execution, external APIs)
8. Evaluation (rubrics, LLM-as-judge, structured review)

TASK:
{{task_spec}}

MODALITY: {{modality}}
DEMOS_AVAILABLE: {{demos_available}}
TOOLS_AVAILABLE: {{tools}}
BUDGET: tokens={{token_budget}}, latency={{latency}}, trials={{max_trials}}

Return JSON:
{
  "families": ["..."],
  "methods": ["..."],
  "activate": {
    "prompt_optimize": bool,
    "meta_conduct": bool,
    "tree_search": bool,
    "refine": bool,
    "reflexion": bool,
    "skill_memory": bool,
    "staged_delivery": bool
  },
  "rationale": "..."
}
```

---

## C2.2 Ideation with Literature Actions

| Field | Content |
|---|---|
| **Source** | AI Scientist v2 ideation (+ Semantic Scholar action pattern) |
| **Purpose** | Generate novel ideas while allowing explicit search actions. |
| **When to use** | Research directions, product angles, paper-shaped projects. |
| **Loop condition** | Up to `{{num_reflections}}` rounds; search or finalize each round. |
| **Transition condition** | `FinalizeIdea` with structured fields; avoid duplicates of `{{prev_ideas}}`. |

**Prompt**

```text
Generate a novel, concrete idea for:
{{topic_or_workshop}}

Previous ideas (do not duplicate):
{{prev_ideas}}

You may either SEARCH or FINALIZE.

ACTION: SearchLiterature
ARGUMENTS: {"query": "...", "why": "what gap this query tests"}

or

ACTION: FinalizeIdea
ARGUMENTS: {
  "name": "...",
  "title": "...",
  "hypothesis": "...",
  "related_work_gap": "...",
  "method": "...",
  "success_metric": "...",
  "risks_and_limits": "...",
  "smallest_shippable_artifact": "..."
}

Prefer ideas that are testable with a small artifact in ≤ {{time_budget}}.
```

---

## C2.3 Ideation Reflection Round

| Field | Content |
|---|---|
| **Source** | AI Scientist v2 idea reflection loop |
| **Purpose** | Improve an idea using tool results / critique. |
| **When to use** | After literature search or peer critique of an idea. |
| **Loop condition** | Round `{{current_round}}` of `{{num_reflections}}`. |
| **Transition condition** | Finalize when novelty, method, and metric are clear; else search again. |

**Prompt**

```text
Reflect on the current idea (round {{current_round}}/{{num_reflections}}).

Current idea:
{{current_idea}}

Last tool/search results:
{{last_tool_results}}

Critically check: novelty, feasibility, metric clarity, ethical/risk issues, and overlap with prior work.
Then either:
- ACTION: SearchLiterature with a sharper query, or
- ACTION: FinalizeIdea with an improved JSON (same schema as ideation).
```

---

## C2.4 Novelty & Prior-Art Stress Test

| Field | Content |
|---|---|
| **Source** | AI Scientist risk/related-work fields · Prompt Report evaluation spirit · ARSENAL peer-review pattern |
| **Purpose** | Kill or sharpen ideas that are not new or not testable. |
| **When to use** | Before investing implementation time. |
| **Loop condition** | One hard pass; optional second pass after rewrite. |
| **Transition condition** | If “not novel” or “not falsifiable” → redesign (C2.2); else proceed to execution plan (C5). |

**Prompt**

```text
Stress-test this idea for novelty and research/product integrity.

Idea:
{{idea}}

Answer with:
1) Closest prior art / existing products (even if approximate)
2) What is actually new (if anything)
3) Falsifier: what observation would kill the idea
4) Smallest decisive experiment or MVP
5) Verdict: pursue | pivot | kill
6) If pivot: one sharper formulation

Be harsh. Prefer kill/pivot over polite enthusiasm.
```

---

## C2.5 Evidence Validation / Answer Check

| Field | Content |
|---|---|
| **Source** | Self-Refine feedback · Voyager critic JSON · AI Scientist review patterns |
| **Purpose** | Validate a result against requirements and evidence. |
| **When to use** | After a draft answer, experiment, or implementation claim. |
| **Loop condition** | Retry critique up to `{{max_retries}}` if format invalid. |
| **Transition condition** | `success=true` → package/ship; `success=false` → refine (C3) or reflect (C3.3). |

**Prompt**

```text
You are a strict validator. Decide if the work meets the requirements.
Exceeding requirements counts as success. Missing any hard requirement is failure.

Requirements / task:
{{task}}

Context:
{{context}}

Artifact / answer / logs:
{{artifact}}

Respond in JSON only (parseable):
{
  "reasoning": "step-by-step check against requirements",
  "success": true,
  "critique": "empty if success; else concrete fix instructions",
  "missing_requirements": [],
  "confidence": 0.0
}
```

---

# PART 3 — HOW TO IMPROVE
*(critique · refine · learn from errors)*

---

## C3.1 Multi-Aspect Critique (Self-Refine feedback)

| Field | Content |
|---|---|
| **Source** | Self-Refine feedback prompts |
| **Purpose** | Structured criticism on multiple axes before rewriting. |
| **When to use** | Any draft: prose, code, plan, README, experiment writeup. |
| **Loop condition** | Feedback each iteration `t` until stop phrase or `max_iters`. |
| **Transition condition** | If stop indicator / score ≥ threshold → done; else C3.2. |

**Prompt**

```text
You are a critical reviewer. Evaluate the candidate on these aspects:
{{aspect_list}}
(Recommended default aspects: correctness, clarity, completeness, structure,
evidence, risk/limits, actionability, simplicity.)

Input / goal:
{{x}}

Candidate:
{{y_t}}

For each aspect: numeric score (1-5) + one-sentence critique.
End with:
Total score: {{score}}/{{max}}
Overall: <summary>
Stop indicator (only if truly ready to ship): READY_TO_SHIP
```

---

## C3.2 History-Aware Refine

| Field | Content |
|---|---|
| **Source** | Self-Refine iterate / refine prompts |
| **Purpose** | Improve draft using full feedback history; avoid repeat mistakes. |
| **When to use** | Immediately after C3.1 when not READY_TO_SHIP. |
| **Loop condition** | `t = 0..max_iters-1` paired with C3.1. |
| **Transition condition** | READY_TO_SHIP, max iters, or marginal score gain < ε → stop. |

**Prompt**

```text
Improve the candidate using the feedback history.
Do not repeat previous mistakes. Prefer smaller, correct changes over rewrites that lose content.

Goal / input:
{{x}}

History:
{{y0}}
Feedback0: {{fb0}}
...
{{y_t}}
Feedback_t: {{fb_t}}

Write the improved full version only (no preamble).
```

---

## C3.3 Verbal Reflection After Failure (Reflexion)

| Field | Content |
|---|---|
| **Source** | Reflexion · LATS failed-trajectory reflection |
| **Purpose** | Convert failure into durable natural-language lessons for the next trial. |
| **When to use** | Test fail, bad review, user rejection, dead-end search, broken run. |
| **Loop condition** | After each failed trial; keep last `{{K}}` reflections. |
| **Transition condition** | Reflection stored → next trial with memory (C3.4 / C1.3). |

**Prompt**

```text
You failed this trial. Produce a concise reflection to help a future attempt.

Task:
{{task}}

Trajectory / what you did:
{{trajectory}}

Environment / test / reviewer feedback:
{{feedback}}

Reflection (2–5 sentences, actionable):
- What specifically went wrong?
- What signal did you ignore?
- What will you do differently next (one concrete policy change)?
```

---

## C3.4 Actor With Memory (next trial)

| Field | Content |
|---|---|
| **Source** | Reflexion actor + memory window · ReAct-style control |
| **Purpose** | Act again conditioned on lessons. |
| **When to use** | Trial `≥ 2` after reflections exist. |
| **Loop condition** | Until success or `max_trials`. |
| **Transition condition** | Success → C4/C5 packaging; failure → C3.3 again. |

**Prompt**

```text
Solve the task. You may use thoughts and actions.

Task:
{{task}}

Relevant lessons from past trials:
{{memory_window}}

Rules:
- Do not repeat failed strategies listed in lessons.
- Prefer the smallest test that would falsify your approach early.

Format:
Thought: ...
Action: ...
(repeat until done)

When finished:
Final: ...
```

---

## C3.5 Instruction Self-Improvement (APE seed + OPRO climb)

| Field | Content |
|---|---|
| **Source** | APE generation · OPRO meta-prompt optimization |
| **Purpose** | Improve the *instruction* itself, not only the answer. |
| **When to use** | Quality plateaus; multiple tasks share one instruction; building agents/products. |
| **Loop condition** | OPRO steps `1..N`: propose → score → append history. |
| **Transition condition** | Top instruction stable across steps or budget exhausted → freeze instruction. |

**Prompt A — propose instructions from demos (APE-like)**

```text
I gave a friend an instruction. Based on the instruction they produced the following
input-output pairs:

{{full_DEMO}}

The instruction was: [APE]
```
*(Model fills the instruction; generate many candidates, dedupe, score.)*

**Prompt B — evolve instructions from scores (OPRO-like)**

```text
Your task is to generate the instruction <INS>.
Below are some previous instructions with their scores.
The score ranges from 0 to 100.

text:
{{old_instruction_i}}
score:
{{score_i}}
...

Below are some problems.
input:
Q: <INS>
{{question}}
A:
Ground truth answer:
{{answer}}

Generate an instruction that is different from all the instructions <INS> above,
and has a higher score than all the instructions <INS> above.
The instruction should begin with <INS> and end with </INS>.
The instruction should be concise, effective, and generally applicable.
```

---

## C3.6 Skill Description (procedural memory)

| Field | Content |
|---|---|
| **Source** | Voyager skill description prompt |
| **Purpose** | Summarize a successful procedure for retrieval later. |
| **When to use** | After a verified success worth reusing. |
| **Loop condition** | None (write-once; version if updated). |
| **Transition condition** | Description stored in skill library → future retrieve-by-similarity. |

**Prompt**

```text
Write a description of the following successful procedure/function.

Rules:
1) Do not mention the function/procedure name.
2) Do not mention logging/print/debug helpers.
3) If helpers exist, describe only the main procedure.
4) At most 6 sentences.
5) Response must be a single block of plain text.

Procedure:
{{code_or_steps}}

The main procedure is `{{name}}`.
```

---

# PART 4 — HOW TO STRUCTURE
*(GitHub · README · files · documentation quality)*

---

## C4.1 Repository Constitution (layout & standards)

| Field | Content |
|---|---|
| **Source** | Synthesis of AI Scientist staged artifacts, extraction-repo standards, Voyager skill packaging, Prompt Report “answer engineering” |
| **Purpose** | Enforce a professional, navigable repo structure. |
| **When to use** | Creating or refactoring any GitHub project. |
| **Loop condition** | Audit once per release; fix gaps before tagging. |
| **Transition condition** | Checklist all green → ready for public push. |

**Prompt**

```text
You are a staff engineer reviewing a GitHub repository for professional structure.

Project purpose:
{{purpose}}

Current file tree:
{{file_tree}}

Produce:
1) Target layout (directories + key files)
2) What is missing vs a high-quality open-source repo
3) Exact renames/moves to perform
4) Minimum docs set: README, LICENSE, CONTRIBUTING (if needed), examples/, tests/
5) What must NOT be committed (.env, secrets, huge data, caches)

Rules:
- Prefer boring, standard layouts over clever ones.
- One clear entrypoint (CLI or `make`/`npm` script).
- Examples must run.
- Tests must exist for core logic.
```

---

## C4.2 README Writer (problem-first)

| Field | Content |
|---|---|
| **Source** | Synthesis from portfolio practice + AI Scientist “writeup clarity” + Self-Refine structure axes |
| **Purpose** | Write a README that sells the problem and proves quality in 30 seconds. |
| **When to use** | Any public repo; major feature releases. |
| **Loop condition** | Optional Self-Refine pass (C3.1–C3.2) on clarity/actionability. |
| **Transition condition** | Stranger can install, run one command, and understand limits. |

**Prompt**

```text
Write a professional README for this repository.

Facts:
- Name: {{name}}
- One-line value: {{one_liner}}
- Problem it solves: {{problem}}
- Who it's for: {{audience}}
- Install: {{install}}
- Quickstart command: {{quickstart}}
- Key features: {{features}}
- Benchmark/evidence (if any): {{evidence}}
- Stack: {{stack}}
- License: {{license}}
- Honest limitations: {{limits}}

Structure:
1. Title + one-line pitch
2. Problem (with failure modes of the naive approach)
3. Before/after or example (short)
4. Install + quickstart
5. What you get / outputs
6. How it works (short architecture)
7. Tests / quality
8. Related links
9. Disclaimer / limits

Rules:
- Lead with the problem, not the tech stack.
- No hype claims without evidence.
- Prefer tables and commands over paragraphs.
```

---

## C4.3 Documentation Completeness Auditor

| Field | Content |
|---|---|
| **Source** | Extraction quality checklists · AI Scientist peer review spirit |
| **Purpose** | Score docs like a reviewer. |
| **When to use** | Pre-release; after large refactors. |
| **Loop condition** | Until critical gaps closed. |
| **Transition condition** | No critical gaps; medium gaps ticketed. |

**Prompt**

```text
Audit documentation quality for this project.

README:
{{readme}}

Extra docs paths/titles:
{{docs_index}}

Score 1–5 each: clarity, completeness, reproducibility, honesty/limits, navigation, examples.
List critical gaps (block release) vs nice-to-haves.
Output a patch plan ordered by impact.
```

---

## C4.4 Commit / PR Message Standard

| Field | Content |
|---|---|
| **Source** | Engineering synthesis (answer engineering + staged delivery) |
| **Purpose** | Keep history usable. |
| **When to use** | Every commit/PR. |
| **Loop condition** | None. |
| **Transition condition** | Message explains why, not only what. |

**Prompt**

```text
Write a concise git commit message for these changes.

Diff summary:
{{diff_summary}}

Intent:
{{intent}}

Format:
- First line ≤ 72 chars, imperative mood
- Optional body: why, risk, follow-ups
- Mention tests if relevant
```

---

## C4.5 Peer Review of a Deliverable

| Field | Content |
|---|---|
| **Source** | AI Scientist v2 peer-review style · Prompt Report evaluation · Self-Refine aspects |
| **Purpose** | Structured accept/revise decision. |
| **When to use** | Paper section, product MVP, client deliverable, README, model report. |
| **Loop condition** | Major revisions → author fixes → re-review once. |
| **Transition condition** | `accept` / `accept_with_minor_revisions` / `major_revisions`. |

**Prompt**

```text
You are a rigorous peer reviewer.

Deliverable:
{{deliverable}}

Stated goals:
{{goals}}

Score 0–1 for: clarity, correctness/soundness, completeness, novelty/usefulness,
actionability, honesty about limits.
Give a verdict: accept | accept_with_minor_revisions | major_revisions | reject.
List required revisions as a numbered checklist.
Call out any overclaims.
```

---

# PART 5 — HOW TO EXECUTE
*(idea → shipped project)*

---

## C5.1 Meta-Conductor (orchestrate experts)

| Field | Content |
|---|---|
| **Source** | Meta-Prompting core instruction |
| **Purpose** | Decompose work and dispatch specialist roles (same model, different briefs). |
| **When to use** | Any multi-skill project (research+code+writing+review). |
| **Loop condition** | Until final answer / ≤ `{{max_rounds}}` expert calls. |
| **Transition condition** | `>> FINAL ANSWER` with integrated result; experts have no memory—always pass full context. |

**Prompt**

```text
You are Meta-Model, a conductor. Break the user's problem into subtasks and solve them
by calling experts. Experts are instances of the same model with specialized instructions.
You may call a Code expert for execution-oriented work.

FORMAT for expert call:
Expert {{ExpertName}}:
{{complete instructions + all needed context}}

FORMAT for final answer:
>> FINAL ANSWER:
{{answer}}

Rules:
- One expert call at a time.
- After each expert reply, verify and integrate before the next call.
- Experts have NO memory of prior turns—never assume they remember.
- Prefer Code expert for arithmetic, tests, scripts, and verification.
- If code must be executed, the Code expert ends with: Please run this code!
- Do not repeat the same expert request unchanged.
- Aim to finish within {{max_rounds}} rounds.

User problem:
{{problem}}
```

---

## C5.2 Intermediate Expert Integration

| Field | Content |
|---|---|
| **Source** | Meta-Prompting intermediate feedback append |
| **Purpose** | Re-enter conductor loop after an expert returns. |
| **When to use** | After every expert response. |
| **Loop condition** | Continues C5.1 loop. |
| **Transition condition** | Enough evidence to finalize, or need another expert. |

**Prompt**

```text
[Expert {{name}} output]
{{expert_output}}

Continue as Meta-Model. Either call another expert with full context
or produce >> FINAL ANSWER:
```

---

## C5.3 Format-Error Retry (conductor)

| Field | Content |
|---|---|
| **Source** | Meta-Prompting invalid-output repair |
| **Purpose** | Repair protocol violations without losing the task. |
| **When to use** | Output is neither expert call nor final answer. |
| **Loop condition** | Up to `{{repair_retries}}`. |
| **Transition condition** | Valid expert call or final answer. |

**Prompt**

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

## C5.4 Automatic Curriculum (next atomic task)

| Field | Content |
|---|---|
| **Source** | Voyager curriculum (generalized beyond Minecraft) |
| **Purpose** | Pick the next small, novel, feasible task toward a large goal. |
| **When to use** | Large projects, learning a codebase, open-ended research programs. |
| **Loop condition** | After each success/failure update completed/failed lists. |
| **Transition condition** | Task is a single phrase; must be verifiable from status signals you have. |

**Prompt**

```text
You are a mentor proposing the NEXT immediate task toward a long-term goal.
Ultimate goal: {{ultimate_goal}}

Status:
{{status_observation}}

Completed tasks so far:
{{completed_tasks}}

Failed / too-hard tasks:
{{failed_tasks}}

Rules:
1) Mentor based on current progress—not a full multi-week plan.
2) Be specific and atomic (one verb phrase).
3) Not too hard for current skills/resources.
4) Prefer novel progress over repetition (repeat only if required for resources/prereqs).
5) Avoid tasks that cannot be verified with available signals.
6) Do not propose multiple tasks.

RESPONSE FORMAT:
Reasoning: ...
Task: <single concise task phrase>
```

---

## C5.5 Task Decomposition Into Subgoals

| Field | Content |
|---|---|
| **Source** | Voyager task decomposition · Prompt Report decomposition family |
| **Purpose** | Turn a final goal into an ordered subgoal list given current resources. |
| **When to use** | Before implementation sprints; when unblocking “too big” tasks. |
| **Loop condition** | Re-decompose if inventory/resources change majorly. |
| **Transition condition** | Valid JSON list; first item executable now. |

**Prompt**

```text
Generate a curriculum of subgoals for the final task, given current resources.

Final task:
{{final_task}}

Current resources / inventory / skills:
{{resources}}

Rules:
1) Return a JSON list of subgoals in order.
2) Each subgoal is a concise phrase: Verb + object (+ quantity if needed).
3) Include prerequisite tooling/setup as its own subgoals.
4) Do not include already-completed capabilities.

JSON only:
["subgoal1", "subgoal2", ...]
```

---

## C5.6 Full Project Execution Spine (idea → ship)

| Field | Content |
|---|---|
| **Source** | ARSENAL L0–L6 nesting · AI Scientist stages · extraction quality bar |
| **Purpose** | One master control prompt for shipping a real project. |
| **When to use** | Greenfield repos, major features, portfolio pieces. |
| **Loop condition** | Outer stages; inner refine/reflect until gates pass. |
| **Transition condition** | Peer review accept/minor + tests pass + README complete → push public. |

**Prompt**

```text
You will ship a project using the ARSENAL execution spine.

Project brief:
{{brief}}

Follow stages in order. Do not skip gates.

STAGE 0 — ROUTE (C2.1)
- Choose techniques and layer flags.

STAGE 1 — INSTRUCTION (C3.5 if needed)
- Freeze a working instruction for the project.

STAGE 2 — DECOMPOSE & CONDUCT (C5.1, C5.5)
- Break into experts/subgoals; integrate outputs.

STAGE 3 — EXPLORE (C1.3–C1.6)
- Branch options for risky decisions; keep top beam.

STAGE 4 — BUILD
- Implement the smallest vertical slice that proves value.

STAGE 5 — REFINE (C3.1–C3.2)
- Multi-aspect critique and history-aware revision.

STAGE 6 — VERIFY (C2.5)
- Requirements check; tests; honest limits.

STAGE 7 — REFLECT IF FAIL (C3.3–C3.4)
- Store lessons; retry with memory (max {{max_trials}}).

STAGE 8 — STRUCTURE (C4.1–C4.4)
- Repo layout, README, commits.

STAGE 9 — REVIEW & SHIP (C4.5)
- Peer review; then public push checklist.

At each stage, emit:
- Stage name
- Artifacts produced
- Gate status: pass/fail
- Next stage or retry reason
```

---

## C5.7 Staged Research Delivery (AI Scientist-shaped)

| Field | Content |
|---|---|
| **Source** | AI Scientist v2 progressive stages (generalized) |
| **Purpose** | Research-shaped delivery without requiring full autonomy. |
| **When to use** | Research memos, eval reports, ablations, portfolio studies. |
| **Loop condition** | Stages 1→4 then writeup/review; abort if no best result. |
| **Transition condition** | Best artifact found → multi-seed/sanity check → writeup → review. |

**Prompt**

```text
Run a staged research delivery.

Question / hypothesis:
{{hypothesis}}

Stage 1 DRAFT: minimal method + first result artifact
Stage 2 TUNE: baselines / hyperparameters / controls
Stage 3 IMPROVE: one creative improvement only
Stage 4 ABLATE: remove pieces to test necessity
Then: summarize limits, write the report, self-review.

Rules:
- Prefer one change per stage.
- Log metric mean±uncertainty when possible.
- If a stage fails, reflect and either retry once or stop with reasons.
- Final report must include: claim, evidence, rebuttals, limits, next experiments.
```

---

# CONSTITUTION QUICK MAP

| Need | Start with |
|---|---|
| Hard reasoning | C1.1 → C1.2 → (optional) C1.3–C1.5 |
| Choose methods | C2.1 |
| Research idea | C2.2 → C2.3 → C2.4 |
| Improve a draft | C3.1 ⇄ C3.2 |
| Learn from failure | C3.3 → C3.4 |
| Improve the instruction | C3.5 |
| Save a reusable skill | C3.6 |
| Make the repo pro | C4.1 → C4.2 → C4.3 |
| Multi-expert project | C5.1 |
| Open-ended progress | C5.4 / C5.5 |
| Ship end-to-end | C5.6 |

---

# GOVERNANCE NOTES

1. **Universal ≠ vague.** Keep placeholders concrete when you instantiate.  
2. **Prefer small loops with gates** over one giant prompt.  
3. **Honesty rule:** if evidence is weak, force rebuttals/limits (C3.1 aspects + C2.5).  
4. **Budget rule:** route (C1.6, C2.1) before expensive search/optimize.  
5. **Memory rule:** verbal lessons (C3.3) and procedural skills (C3.6) are different—use both when appropriate.  
6. **This constitution is a control layer**, not a substitute for domain expertise, licenses, or ethics review.

---

*Maintained with the ARSENAL unified master pipeline.*  
*Repo: https://github.com/faresrafat3/arsenal-unified-master-pipeline*

---

# PART 6 — HOW TO TRACK KNOWLEDGE
*(gap identification · implicit inference · research idea generation · scientific agent construction)*

---

## C6.1 Explicit Scientific Knowledge Gap Extraction (GAPMAP)

| Field | Content |
|---|---|
| **Source** | GAPMAP explicit prompt — `ex_gap_xtract.py` PROMPT_TEMPLATE + System Return ONLY JSON |
| **Purpose** | Extract every author-signaled knowledge gap with traceable exact sentence + cue + justification. |
| **When to use** | Literature review, IPBES-style paragraphs, COVID-style sections up to 8K, any scientific text requiring explicit gap inventory. |
| **Loop condition** | For each chunk ≤1000 words sentence-aligned (Stanza or regex fallback). |
| **Transition condition** | JSON array validated (4 REQUIRED_KEYS) → dedupe by squashed Ignorance Statement → save per ID. |

**Prompt**

```text
You are an expert scientific information extraction model.

TASK
Extract every "scientific knowledge gap" from the document below. A scientific knowledge gap is an explicit uncertainty, limitation, missing evidence, contradiction, or untested area stated by the authors.

GUIDELINES
- Use only the provided document.
- For the "Statement" field, return the exact sentence from the text that reflects the gap.
- For "Ignorance Cues", list the specific cue words/phrases in the Statement that signal uncertainty.
- Use an array of strings for "support_sentence/s" (empty array if none are needed).

OUTPUT FORMAT (STRICT JSON; array of objects for each candidate sentence)
[
  {
    "Ignorance Statement": "...",                // exact ignorance sentence from the doc
    "support_sentence/s": ["..."],              // premises sentences that allow for concluding the extraction
    "justification": "...",                    // brief reason the sentence is a gap, based on wording in the doc
    "Ignorance Cues": ["...", "..."]          // cue words/phrases from the Statement
  }
]

DOCUMENT
<<<
{{chunk}}
>>>

Return only the JSON array. If no gaps are found, return [].
Use double quotes for all keys and strings. Do not include explanations or any text before or after the JSON.
```

**System prompt companion**

```text
You are an expert scientific information extraction model. Return ONLY valid JSON.
```

**Post-processing**

```text
extract_json_array: strip ```json fences and <think> tags, regex [ {..} ]
validate_payload: list of dicts REQUIRED_KEYS = {Ignorance Statement, support_sentence/s, justification, Ignorance Cues} correct types
dedupe_by_statement: whitespace-squashed exact match
Error path: write {{file_id}}__ERROR.txt with repr(e)+Excerpt, sleep 1.5, continue
Evaluation: ROUGE-L F1 stemming one-to-one matching threshold 0.55 TP>0.55 FP unmatched pred FN unmatched gold P/R/F1; COVID: validate vs ignorance-cue dictionary Boguslav et al must contain ≥1 cue, filter general non-research gaps
Chunking: split_into_chunks_preserving_sentences max_tokens=1000 sentence-aligned Stanza Pipeline lang=en processors=tokenize token_count=sum words, fallback regex (?<=[.!?])\s+(?=[A-Z"“(]), isolate >1000 word sentence alone
```

---

## C6.2 Implicit Gap TABI — Claim/Grounds→Warrant + Bucket (GAPMAP)

| Field | Content |
|---|---|
| **Source** | GAPMAP TABI Toulmin-Abductive Bucketed Inference — Sec 4.3.1 + Table1 examples + 3-shot necessity |
| **Purpose** | Infer unstated gaps requiring discourse reasoning: missing link, generalization failure, conflicting findings without reconciliation. |
| **When to use** | Paragraph with future directions masked, needing interpretable abductive gap (biomedical + any domain). Zero-shot degenerates — must use 3-shot. |
| **Loop condition** | Generate 1-3 candidates per paragraph ordered most probable first. |
| **Transition condition** | Bi-directional entailment RoBERTa-large threshold 0.4 Claim vs Gold and Warrant vs Premises — any candidate matches → success. Bucket calibration log 10-24% correct least_probable. |

**Prompt**

```text
SYSTEM: You are an expert biomedical argumentation analyst. Infer implicit knowledge gaps using Toulmin structure.

TASK: Given a biomedical paragraph with future-direction sentences masked at end, infer the implicit knowledge gap.

OUTPUT SCHEMA — strict JSON object per candidate:
{
  "Claim": "The implied gap — what remains unknown / required future direction (one sentence, clear)",
  "Grounds": ["Evidence sentence 1 verbatim from paragraph", "Evidence sentence 2 verbatim"],
  "Warrant": "Single sentence that logically connects Grounds to Claim, explaining why gap follows",
  "Bucket": "more_probable | least_probable",
  "Category": "Levels of Evidence | Barriers | Future Opportunities | Anomaly/Curious Findings | Research Aims (choose one)",
  "Justification": "Brief why Bucket chosen"
}

RULES:
- Claim must be defeasible abductive inference, not copy of explicit cue.
- Grounds must be quoted spans from input paragraph.
- Warrant must be one sentence, generalizable reasoning pattern (e.g., "Mouse biomarker improvement does not guarantee human outcome if correlation poor").
- Bucket: more_probable if gap central to paper's argument, least_probable if peripheral/speculative.
- Return JSON array of 1-3 candidates, ordered most probable first.

EXAMPLES (3-shot):

Example 1:
Paragraph: "Compound E improves biomarker F in mice. Biomarker F correlates poorly with clinical outcomes in humans."
Gold implicit gap: "It is unknown whether E improves patient outcomes."
Output:
[
  {
    "Claim": "It is unknown whether compound E improves patient outcomes in humans.",
    "Grounds": ["Compound E improves biomarker F in mice.", "Biomarker F correlates poorly with clinical outcomes in humans."],
    "Warrant": "If a surrogate marker fails to correlate with clinical endpoints, efficacy on surrogate does not imply clinical benefit.",
    "Bucket": "more_probable",
    "Category": "Levels of Evidence",
    "Justification": "Translational barrier central to paragraph"
  }
]

Example 2:
Paragraph: "We demonstrated 95% accuracy on synthetic dataset with 10K samples. Real-world clinical dataset has missing values, distribution shift, and only 200 labeled cases."
Output:
[
  {
    "Claim": "It is unknown whether model maintains accuracy on real-world clinical data with limited labels and shift.",
    "Grounds": ["We demonstrated 95% accuracy on synthetic dataset with 10K samples.", "Real-world clinical dataset has missing values, distribution shift, and only 200 labeled cases."],
    "Warrant": "Performance on idealized synthetic data does not transfer to noisy low-resource real data without validation.",
    "Bucket": "more_probable",
    "Category": "Barriers"
  }
]

Example 3:
Paragraph: "Study A reported significant benefit of X in European cohort (n=5000, p<0.001). Study B found no effect in East Asian cohort (n=3000, p=0.45). No reconciliation offered."
Output:
[
  {
    "Claim": "It is unknown why efficacy of X differs by population and what modifiers explain conflicting results.",
    "Grounds": ["Study A reported significant benefit of X in European cohort (n=5000, p<0.001).", "Study B found no effect in East Asian cohort (n=3000, p=0.45)."],
    "Warrant": "Conflicting findings across populations without mechanistic explanation indicate missing understanding of effect modifiers.",
    "Bucket": "more_probable",
    "Category": "Anomaly/Curious Findings"
  }
]

NOW YOUR TURN:

Paragraph (future directions masked):
<<<
{{paragraph}}
>>>

Return only valid JSON array (1-3 candidates). No extra text.
```

---

## C6.3 Full-Document Implicit Gap + Future Direction (GAPMAP Pilot)

| Field | Content |
|---|---|
| **Source** | GAPMAP Sec 4.3.2 full-text pilot GPT-4o multi-modal + author survey 18 corresponding authors |
| **Purpose** | Holistic full-paper unstated gap discovery + actionable future directions with feasibility. |
| **When to use** | Full manuscripts (text/tables/figures) long context, pilot author agreement evaluation. |
| **Loop condition** | 5-10 gaps per paper. |
| **Transition condition** | Author survey: factual true 83.3%, remain open 56% fully +25.9% partial, impact 67% of partials, implementation valid 65% / invalid 35% feasibility. Human-in-loop required for feasibility filtering. |

**Prompt**

```text
SYSTEM: You are a senior scientific reviewer analyzing full manuscripts for unstated knowledge gaps and actionable future directions.

USER:
You will receive a full research manuscript (text, may include tables/figures). Task:

- Identify 5-10 implicit knowledge gaps: gaps NOT explicitly stated but inferrable from context (missing link, generalization limit, conflict).
- For each gap, provide:
  {
    "Implied Gap": "Declarative unknown",
    "Evidence Spans": ["Quote sentence/paragraph supporting inference with section reference", ...],
    "Warrant": "Single sentence reasoning why evidence implies gap",
    "Gap Category": "Levels of Evidence / Barriers / Future Opportunities / Anomaly / Research Aims",
    "Future Direction": "Concrete feasible next experiment/study to address gap",
    "Feasibility Notes": "Tech limits, budget, domain constraints",
    "Bucket": "more_probable vs least_probable (central vs peripheral)"
  }

Constraints:
- Use only manuscript evidence
- Avoid hallucinating references
- Ensure future direction is distinct from authors' stated future work if any, and testable
- Handle long context holistically

Input manuscript:
<<<
{{full_paper_text}}
>>>

Return strict JSON array of gaps as defined. No preamble.
```

---

## C6.4 Knowledge-Aware Problem Identification (ResearchAgent Table 6)

| Field | Content |
|---|---|
| **Source** | ResearchAgent Table 6 full instantiation — systematic reading target→related→entities |
| **Purpose** | Generate original clear feasible relevant significant problem building upon core paper + citation graph + entity store. |
| **When to use** | Early-stage research formulation after gap identification, any domain needing novel problem from literature. |
| **Loop condition** | 1 problem per core paper, revisit target as focal point before crafting. |
| **Transition condition** | Problem: + Rationale: ready for method stage. |

**Prompt**

```text
System: You are an AI assistant whose primary goal is to identify promising, new, and key scientific problems based on existing scientific literature, in order to aid researchers in discovering novel and significant research opportunities that can advance the field.

User: You are going to generate a research problem that should be original, clear, feasible, relevant, and significant to its field. This will be based on the title and abstract of the target paper, those of {{len_refs}} related papers in the existing literature, and {{len_entities}} entities potentially connected to the research area.

Understanding of the target paper, related papers, and entities is essential:
- The target paper is the primary research study you aim to enhance or build upon through future research, serving as the central source and focus for identifying and developing the specific research problem.
- The related papers are studies that have cited the target paper, indicating their direct relevance and connection to the primary research topic you are focusing on, and providing additional context and insights that are essential for understanding and expanding upon the target paper.
- The entities can include topics, keywords, individuals, events, or any subjects with possible direct or indirect connections to the target paper or the related studies, serving as auxiliary sources of inspiration or information that may be instrumental in formulating the research problem.

Your approach should be systematic:
- Start by thoroughly reading the title and abstract of the target paper to understand its core focus.
- Next, proceed to read the titles and abstracts of the related papers to gain a broader perspective and insights relevant to the primary research topic.
- Finally, explore the entities to further broaden your perspective, drawing upon a diverse pool of inspiration and information, while keeping in mind that not all may be relevant.

I am going to provide the target paper, related papers, and entities, as follows:
Target paper title: {{paper_title}}
Target paper abstract: {{paper_abstract}}
Related paper titles: {{related_titles}}
Related paper abstracts: {{related_abstracts}}
Entities: {{Entities}}

With the provided target paper, related papers, and entities, your objective now is to formulate a research problem that not only builds upon these existing studies but also strives to be original, clear, feasible, relevant, and significant. Before crafting the research problem, revisit the title and abstract of the target paper, to ensure it remains the focal point of your research problem identification process.
Target paper title: {{paper_title}}
Target paper abstract: {{paper_abstract}}

Then, following your review of the above content, please proceed to generate one research problem with the rationale, in the format of
Problem:
Rationale:
```

---

## C6.5 Knowledge-Aware Method Development (ResearchAgent Table 7)

| Field | Content |
|---|---|
| **Source** | ResearchAgent Table 7 — problem rationale as cornerstone |
| **Purpose** | Propose innovative rigorous valid method solving newly identified problem leveraging existing studies + entities. |
| **When to use** | Immediately after C6.4 problem, before experiment. |
| **Loop condition** | 1 method per problem, revisit problem as focal point. |
| **Transition condition** | Method: + Rationale: clear innovative rigorous valid generalizable. |

**Prompt**

```text
System: You are an AI assistant whose primary goal is to propose innovative, rigorous, and valid methodologies to solve newly identified scientific problems derived from existing scientific literature, in order to empower researchers to pioneer groundbreaking solutions that catalyze breakthroughs in their fields.

User: You are going to propose a scientific method to address a specific research problem. Your method should be clear, innovative, rigorous, valid, and generalizable. This will be based on a deep understanding of the research problem, its rationale, existing studies, and various entities.

Understanding of the research problem, existing studies, and entities is essential:
- The research problem has been formulated based on an in-depth review of existing studies and a potential exploration of relevant entities, which should be the cornerstone of your method development.
- The existing studies refer to the target paper that has been pivotal in identifying the problem, as well as the related papers that have been additionally referenced in the problem discovery phase, all serving as foundational material for developing the method.
- The entities can include topics, keywords, individuals, events, or any subjects with possible direct or indirect connections to the existing studies, serving as auxiliary sources of inspiration or information that may be instrumental in method development.

Your approach should be systematic:
- Start by thoroughly reading the research problem and its rationale, to understand your primary focus.
- Next, proceed to review the titles and abstracts of existing studies, to gain a broader perspective and insights relevant to the primary research topic.
- Finally, explore the entities to further broaden your perspective, drawing upon a diverse pool of inspiration and information, while keeping in mind that not all may be relevant.

I am going to provide the research problem, existing studies (target paper & related papers), and entities, as follows:
Research problem: {{researchProblem}}
Rationale: {{researchProblemRationale}}
Target paper title: {{paper_title}}
Target paper abstract: {{paper_abstract}}
Related paper titles: {{related_titles}}
Related paper abstracts: {{related_abstracts}}
Entities: {{Entities}}

With the provided research problem, existing studies, and entities, your objective now is to formulate a method that not only leverages these resources but also strives to be clear, innovative, rigorous, valid, and generalizable. Before crafting the method, revisit the research problem, to ensure it remains the focal point of your method development process.
Research problem: {{researchProblem}}
Rationale: {{researchProblemRationale}}

Then, following your review of the above content, please proceed to propose your method with its rationale, in the format of
Method:
Rationale:
```

---

## C6.6 Knowledge-Aware Experiment Design (ResearchAgent Table 8)

| Field | Content |
|---|---|
| **Source** | ResearchAgent Table 8 — problem+method central |
| **Purpose** | Design robust feasible impactful experiments validating method addressing problem. |
| **When to use** | After C6.4+C6.5, before verification. |
| **Loop condition** | 1 experiment per method, revisit problem+method central. |
| **Transition condition** | Experiment: + Rationale: clear robust reproducible valid feasible ready for ReviewingAgents. |

**Prompt**

```text
System: You are an AI assistant whose primary goal is to design robust, feasible, and impactful experiments based on identified scientific problems and proposed methodologies from existing scientific literature, in order to enable researchers to systematically test hypotheses and validate groundbreaking discoveries that can transform their respective fields.

User: You are going to design an experiment, aimed at validating a proposed method to address a specific research problem. Your experiment design should be clear, robust, reproducible, valid, and feasible. This will be based on a deep understanding of the research problem, scientific method, existing studies, and various entities.

Understanding of the research problem, scientific method, existing studies, and entities is essential:
- The research problem has been formulated based on an in-depth review of existing studies and a potential exploration of relevant entities.
- The scientific method has been proposed to tackle the research problem, which has been informed by insights gained from existing studies and relevant entities.
- The existing studies refer to the target paper that has been pivotal in identifying the problem and method, as well as the related papers that have been additionally referenced in the discovery phase of the problem and method, all serving as foundational material for designing the experiment.
- The entities can include topics, keywords, individuals, events, or any subjects with possible direct or indirect connections to the existing studies, serving as auxiliary sources of inspiration or information that may be instrumental in your experiment design.

Your approach should be systematic:
- Start by thoroughly reading the research problem and its rationale followed by the proposed method and its rationale, to pinpoint your primary focus.
- Next, proceed to review the titles and abstracts of existing studies, to gain a broader perspective and insights relevant to the primary research topic.
- Finally, explore the entities to further broaden your perspective, drawing upon a diverse pool of inspiration and information, while keeping in mind that not all may be relevant.

I am going to provide the research problem, scientific method, existing studies (target paper & related papers), and entities, as follows:
Research problem: {{researchProblem}}
Rationale: {{researchProblemRationale}}
Scientific method: {{scientificMethod}}
Rationale: {{scientificMethodRationale}}
Target paper title: {{paper_title}}
Target paper abstract: {{paper_abstract}}
Related paper titles: {{related_titles}}
Related paper abstracts: {{related_abstracts}}
Entities: {{Entities}}

With the provided research problem, scientific method, existing studies, and entities, your objective now is to design an experiment that not only leverages these resources but also strives to be clear, robust, reproducible, valid, and feasible. Before crafting the experiment design, revisit the research problem and proposed method, to ensure they remain at the center of your experiment design process.
Research problem: {{researchProblem}}
Rationale: {{researchProblemRationale}}
Scientific method: {{scientificMethod}}
Rationale: {{scientificMethodRationale}}

Then, following your review of the above content, please proceed to outline your experiment with its rationale, in the format of
Experiment:
Rationale:
```

---

## C6.7 ReviewingAgent with Human-Aligned Criteria (ResearchAgent Tables 9-15)

| Field | Content |
|---|---|
| **Source** | ResearchAgent Tables 9-11 ReviewingAgents + Tables 12-15 induced criteria + criteria induction method Lin et al 2024 |
| **Purpose** | Simulate peer feedback community with discerning critical evaluation aligned to human preferences via few human annotations. |
| **When to use** | After each idea (problem/method/experiment) generation, iterative refinement loop 0-4 steps saturation after 3 (Du et al 2023). |
| **Loop condition** | For each idea 5 criteria per idea =15 reviewers per refinement iteration, up to 4 steps. |
| **Transition condition** | Review + Feedback + Rating 1-5 per metric → aggregate → ResearchAgent revises idea → re-evaluate. Agreements: Human-Human Scoring Spearman 0.83/0.76/0.67 pairwise kappa 0.62/0.62/0.41 Human-Model Scoring 0.64/0.58/0.49 Pairwise 0.71/0.62/0.52. |

**Prompt — Problem validation (Table 9)**

```text
System: You are an AI assistant whose primary goal is to assess the quality and validity of scientific problems across diverse dimensions, in order to aid researchers in refining their problems based on your evaluations and feedback, thereby enhancing the impact and reach of their work.

User: You are going to evaluate a research problem for its {{metric}}, focusing on how well it is defined in a clear, precise, and understandable manner.

As part of your evaluation, you can refer to the existing studies that may be related to the problem, which will help in understanding the context of the problem for a more comprehensive assessment.
- The existing studies refer to the target paper that has been pivotal in identifying the problem, as well as the related papers that have been additionally referenced in the discovery phase of the problem.

The existing studies (target paper & related papers) are as follows:
Target paper title: {{paper_title}}
Target paper abstract: {{paper_abstract}}
Related paper titles: {{related_titles}}
Related paper abstracts: {{related_abstracts}}

Now, proceed with your {{metric}} evaluation approach that should be systematic:
- Start by thoroughly reading the research problem and its rationale, keeping in mind the context provided by the existing studies mentioned above.
- Next, generate a review and feedback that should be constructive, helpful, and concise, focusing on the {{metric}} of the problem.
- Finally, provide a score on a 5-point Likert scale, with 1 being the lowest, please ensuring a discerning and critical evaluation to avoid a tendency towards uniformly high ratings (4-5) unless fully justified:
{{criteria}}

I am going to provide the research problem with its rationale, as follows:
Research problem: {{researchProblem}}
Rationale: {{researchProblemRationale}}

After your evaluation of the above content, please provide your review, feedback, and rating, in the format of
Review:
Feedback:
Rating (1-5):
```

**Prompt — Method validation (Table 10)**

```text
System: You are an AI assistant whose primary goal is to assess the quality and soundness of scientific methods across diverse dimensions, in order to aid researchers in refining their methods based on your evaluations and feedback

User: You are going to evaluate a scientific method for its {{metric}} in addressing a research problem

Context: research problem as cornerstone + existing studies target+related foundational + entities auxiliary
Systematic: read proposed method rationale + context problem+existing studies → review feedback concise focusing {{metric}} + score 1-5 discerning critical avoid uniform high unless justified {{criteria}}
Provide problem+rationale + target+related + method+rationale
Format Review: Feedback: Rating (1-5):
```

**Prompt — Experiment validation (Table 11)**

```text
System: You are an AI assistant whose primary goal is to meticulously evaluate the experimental designs of scientific papers across diverse dimensions

User: You are going to evaluate an experiment design for its {{metric}} validating method addressing problem focusing clear precise understandable enabling grasp setup procedure expected outcomes

Context: problem+method rationales + existing studies target+related + entities auxiliary
Systematic: read experiment design rationale + context problem method existing studies → review feedback focusing {{metric}} + score 1-5 {{criteria}}
Provide problem+rationale method+rationale target+related + experiment+rationale
Format Review: Feedback: Rating (1-5):
```

**Metrics**

- Problem: Clarity Relevance Originality Feasibility Significance
- Method: Clarity Validity Rigorousness Innovativeness Generalizability
- Experiment: Clarity Validity Robustness Feasibility Reproducibility

**Criteria induction prompt**

```text
You have 10 examples human judgments for criterion {{metric}} for {{idea_type}} (Problem/Method/Experiment). Each example contains research idea text + human score 1-5 Likert

Examples:
{{example_1_idea}} Human Score: {{score_1}} ...
{{example_10_idea}} Human Score: {{score_10}}

Task: Induce detailed description for each level 1 to 5 of this criterion, reflecting underlying human preferences observed. Return JSON {"criterion": "...", "level_1": "...", ... "level_5": "..."} Focus nuances differentiates levels: clarity definition, integration prior work, novelty, feasibility constraints etc.

Make descriptions mirror human annotator reasoning but generalized.
```

**Induced criteria snapshot (Tables 13-15)**

- Problem Clarity L1 highly ambiguous lacking definition leaving significant room interpretation confusion → L5 exceptionally clear concise specific every term well-defined no room misinterpretation fully encapsulating scope
- Relevance L1 almost no relevance failing connect → L5 highly relevant deeply integrated significant advancement
- Originality L1 no discernible originality closely mirroring → L5 highly original pioneering setting new direction
- Feasibility L1 fundamentally infeasible insurmountable resource constraints → L5 highly feasible minimal barriers well-supported robust clear methodology
- Significance L1 minimal no significance lacking relevance → L5 exceptional significance groundbreaking transformative
- Method Clarity L1 extremely vague impossible understand replicate → L5 exceptionally clear precise detailed straightforward replication no ambiguities; Validity L1 fundamental misunderstanding lacks credible alignment → L5 exceptional understanding robust foundation exemplary integration advancement; Rigorousness L1 fundamental lack systematic → L5 exceptional thoroughness benchmark; Innovativeness L1 no novel fully relying existing → L5 groundbreaking transforming redefining standard practices; Generalizability L1 no adaptability failing beyond original → L5 highly adaptable broad diverse
- Experiment Clarity L1 extremely unclear critical details missing nearly impossible understand setup → L5 exceptionally clear precise detailed easy understanding no ambiguity; Validity L1 fundamental misunderstanding lacks alignment → L5 excellently aligns robust evidence outstandingly addressing questions; Robustness L1 fundamental lack durability adaptability highly unreliable → L5 exceptional commitment meticulous attention durability adaptability all conditions highly reliable universally applicable; Feasibility L1 fundamentally unfeasible insurmountable → L5 highly feasible no significant constraints smooth; Reproducibility L1 lacks critical details virtually impossible replicate → L5 exemplary clarity detail comprehensiveness precisely effortlessly replicate identical conditions

**Evaluation prompts (Appendix A)**

Scoring:

```text
Task: rate {{idea_type}} based on criterion {{metric}} on 5-point Likert
Criteria description: {{criteria_description_for_metric}}
Idea: {{idea_text}} Rationale: {{rationale}} Context: target paper {{title, abstract}} + related titles/abstracts
Provide reasoning step-by-step then final Rating 1-5
Format Reasoning: ... Rating: 1-5
```

Pairwise:

```text
Criterion: {{metric}} for {{idea_type}}
Idea A: {{idea_A_text}}
Idea B: {{idea_B_text}}
Context: {{target+related}}
Which better for {{metric}}? Consider {{criteria_description}}
Return Reasoning: ... Winner: A|B|Tie
```

---

## C6.8 Entity-Centric Knowledge Store Retrieval (ResearchAgent Eq1 Eq2)

| Field | Content |
|---|---|
| **Source** | ResearchAgent Sec 3 entity-centric knowledge store K ∈ R^{m×m} sparse + Eq1 Eq2 + Appendix B.3 embedding alternative |
| **Purpose** | Capture affinity between domains via overlapping entities enabling cross-pollination (database ↔ hematology). |
| **When to use** | Building encyclopedic view of related concepts beyond citation graph, before problem/method/experiment generation. |
| **Loop condition** | Build over 50,091 papers May-Dec 2023 + refs titles+abstracts only (length), 300 core >20 cites after May01 2023 avg 87 refs abstract avg 2.17 entities, pairs C(|E|,2). |
| **Transition condition** | Retrieve top-k external entities not in current set via co-occurrence or embedding similarity. |

**Logic**

```text
K ∈ R^{m×m} where m = total unique entities identified, sparse format
Construction: extracting entities over all available scientific articles literature L, counts co-occurrences between entity pairs within individual papers but also quantifies count each entity. Versatile any entity linker; paper uses BLINK linker Wu et al 2020 tags canonicalizes entities El = EL(l) multiset allowing repetitions appearing in l, target restricted titles+abstracts due extensive length publications. Upon extracting entities E, store into K consider all possible pairs E represented as {ei,ej} (i,j)∈C(|E|,2).

Retrieval probabilistic top-k relevant external entities:

Eq1: Ret({l0..ln};K) = argmax_{I⊂[m]:|I|=k} ∏ P(ei|E_{l0..ln}) where ei ∉ E_{l0..ln}

Eq2 Bayes + independence assumption entities independent approximation:
argmax_{I} ∏ (∏_{ej∈E_{l0..ln}} P(ej|ei)) × P(ei) where P(ej|ei) and P(ei) derived from values in two-dimensional matrix K suitably normalized

Alternative embedding-based retrieval: entities highest similarity to entities appearing in current literature (core paper and references) used for idea generation, similarities calculated embedding-level similarities between entities over latent space represented by entity linker (Wu et al 2020). Unlike co-occurrence that may retrieve opposite concepts (since often mention limitations previous work alongside proposed ideas), embedding provides mostly similar concepts. Both comparable results Table5 co-occurrence 4.52/4.28/4.18 vs embedding 4.49/4.34/4.16 vs w/o entity 4.35/4.13/4.02 problem/method/experiment.

Instantiation: o = LLM(T({l0..ln}, Ret({l0..ln};K))) called ResearchAgent templates Tables 6,7,8
```

**Implementation sketch (from raw_prompt_files/entity_retrieval_logic.py)**

```python
co_counts[ei][ej] +=1 ; single_counts[e] +=1
# score log space: log P(ei) + sum_j log P(ej|ei) where P(ej|ei)=co/sing
top-k argmax external vocab
# embedding alternative: cosine similarity latent space mean current vector vs vocab
```

---

## C6.9 Scientific Agent Planner Taxonomy Router (Scientific Intelligence Survey P1-P6 L1-L2)

| Field | Content |
|---|---|
| **Source** | Scientific Intelligence Survey Sec 2.1 taxonomy Figure 2 P1-P6 + L1-L2 + cathode running example Figure 3 |
| **Purpose** | Choose planner family before heavy search, mix-and-match blueprint for fit-for-purpose scientific agents. |
| **When to use** | At start of any scientific agent build, before routing to tree search / memory / verifier. |
| **Loop condition** | Re-route if modality/tools/budget change. |
| **Transition condition** | Planner type selected → downstream memory/action/verifier construction. |

**Prompt**

```text
You are a technique router for scientific agent planners.

TAXONOMY:

P1 Instructional/Schema-Driven: predefined workflow templates encoding domain methodologies "literature review → hypothesis formulation → experimental design → validation", standardized response formats ReAct Thought-Action-Observation, tool usage schemas defining available operations invocation patterns, domain-specific guidelines best practices constraints. Examples AutoLabs, Coscientist Suzuki Sonogashira, CRISPR-GPT, GeneGPT, k-agents, LLMSat, ORGANA, ResearchAgent, StarWhisper.

P2 Context-Augmented: encode historical or searched context in prompts, historical records NMC811 failed @400 cycles capacity fade LFP stable 160 mAh/g + KB target conductivity sigma>1000 mS/cm rate capability voltage 4.0-4.3V vs Li/Li+. Examples CellVoyager self-evolving Template Library Tool Ocean persistent context, CoI citation collaboration history context, HoneyComb domain KB, PaSa search, ResearchAgent academic graph entity store 50,091 papers, STELLA.

P3 Deliberative/Reflective: augment basic task decomposition with self-evaluation iterative refinement critique revision cycles, multi-turn workflows alternating plan generation plan critique, meta-prompts "Evaluate plan logical consistency feasibility" "Identify potential failure modes revise accordingly", chain-of-thought self-reflection iterative idea plan refinement, error-driven replanning failures trigger revision, explicit reflection stages dedicated critique prompts, VLM-based reflection multimodal. Examples LLMatDesign self-reflection, dZiner iterative reviewing modification history, AtlasAgent batch correction quality evaluation, MoRA Mixture Refinement flags scores routing, OriGene self-evolving, VirSci team discussion novelty vote, CellForge graph-structured debates, OpenFOAMGPT self-correcting simulation loops error-driven.

P4 Search-Based: reformulate plan generation exploration over plan spaces generating evaluating multiple candidate plans optimal Tree-of-Thought ToT MCTS beam search sequential decision-making under uncertainty expanding promising branches pruning low-quality, search trees nodes partial plans edges extensions adding sub-tasks refining parameters generating multiple alternative extensions each node evaluates heuristic scoring learned value models selectively expands high-scoring branches, hierarchical search tree query plans catalyst type inclusion/exclusion relational operators quantum-chemical feedback adsorption energies reaction barriers structural stability rewards prune unpromising iteratively refine, experiment manager 4 stages Preliminary Investigation Hyperparameter Tuning Research Agenda Execution Ablation Studies generates multiple candidates executes parallel evaluates including VLM figure quality selects best nodes further expansion. Examples AI Scientist-v2 agentic tree-search, CheMatAgent HE-MCTS decoupled tool planning Policy Model execution Execution Model, ChemReasoner hierarchical search tree query plans quantum-chemical feedback, GeoAgent MCTS geospatial beam search execution filtering error traceback, InternAgent hierarchical idea evolution tree, Mephisto tree search self-play knowledge base, SGA search with simulators physically plausible.

P5 Role-Interactive/Multi-Agent Prompting: distribute plan generation across multiple distinct LLM agent instances specialized functions collaborative dialogue planner proposes critic identifies flaws executor provides feasibility feedback mirrors team dynamics, tournament-style debate 4 debate agents 2 for 2 against judge declares winners meta-review synthesizes insights multiple rounds identifying recurring patterns optimizing performance, multi-round discussions several expert agents votes yes/no preliminary summary report modification opinions if vote no report revised iteratively until all experts agree max attempts, structured idea refinement critic novelty feasibility impact filtering refining, generation-reflection paired reflection agents evaluating clarity novelty feasibility technical correctness completeness adherence, specialized critics Diversity Feasibility Scientific Rigor, Dev Agent environment building code creation model training report writing + Critic assessing intermediate. Examples AI co-scientist tournament debate, MedAgents yes/no votes until consensus, ProtAgents, STELLA Dev+Critic, AtomAgents Critic verification, AutoLabs supervisor sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification.

P6 Programmatic Code/DSL/DAG: generate machine-executable plan representations Python script DSL pipeline DAG explicit task dependencies LLM CODE GENERATOR prompt Generate DFT+Synthesis pipeline as Python script → EXECUTABLE ARTIFACT workflow=DSL_Pipeline() workflow.add(DFT_Screening(candidates=100 criteria capacity>200)) ... Examples AIGS AlphaEvolve Biomni Chemist-X K-Dense Analyst ORGANA SGA.

L1 SFT/Domain-Trained: domain-specific pre-training internalize planning strategies training trajectories. Examples AstroMLab BioGPT Chemma LLaMA-2-7b fine-tuned 34B tokens chemical literature retrosynthesis yield prediction condition generation autonomous exploration closed/open DrugAssist DrugPilot GatorTronGPT GeoMinLM MatChat NatureLM ToRA.

L2 RL/Preference-Optimized: internalize through reward signals RLHF DPO simulations human preferences experimental outcomes. Examples BioScientist Agent CheMatAgent Chemma CycleResearcher ReFT STEP-DPO Flow-DPO Sci-MARL MolRL-MGPT PaSa.

TASK:
{{task_spec}}

MODALITY: {{modality}} (numerical datasets molecular structures biological sequences etc)
TOOLS_AVAILABLE: {{tools}} (VASP XRD_Simulator Autolab_API ChemCrow 18+ chemoinformatics GeneGPT genomic PaSa search Semantic Scholar etc)
BUDGET: tokens={{token_budget}} latency={{latency}} trials={{max_trials}}
REQUIREMENTS: {{requirements}} e.g., Research Goal Design high-capacity cathode >200 mAh/g stable 500+ cycles Avoid Co cost target >4V

Return JSON:
{
  "planner_family": "P1|P2|P3|P4|P5|P6|L1|L2|hybrid",
  "examples": ["..."],
  "procedural_schema": ["Crystal Structure Design", "DFT Screening", "Synthesis Planning", "Electrochemical Testing"],
  "tool_inventory": ["VASP", "XRD_Simulator", "Autolab_API"],
  "constraints": ["Avoid Co", "target voltage >4V"],
  "running_example_mapping": "How cathode example maps",
  "rationale": "..."
}
```

**Cathode running example wiring reference**

```text
RESEARCH GOAL: "Design and synthesize a high-capacity cathode material for Li-ion batteries (>200 mAh/g, stable for 500+ cycles)"
P1: System Prompt Battery Schema Persona battery materials expert Procedural Schema 1 Crystal Structure Design → 2 DFT Screening → 3 Synthesis Planning → 4 Electrochemical Testing Tool Inventory [VASP, XRD_Simulator, Autolab_API] Constraints Avoid Co cost target voltage >4V Plan STEP1 xxx -> STEP2 ...
P2: AUGMENTED PROMPT [Historical] NMC811 failed @400 cycles capacity fade [Historical] LFP stable but capacity only 160 mAh/g [KB] Target conductivity σ>1000 mS/cm for rate capability [KB] Voltage window 4.0-4.3V vs Li/Li+ Design new material avoiding NMC811 Mn dissolution issue while exceeding LFP capacity...
P3: Generate Initial Plan Li-rich oxide Reflect flaws Cycles 480 (<500) Safety O2 release risk Revise Mg-doping + Al2O3 coating Reflect Cycles 550 ✓ Converged Yes Final Plan with reflection
P4: [ROOT Cathode >200] [LFP Variant] Score 0.5 [NMC Variant] 0.7 [Co-free Layered] 0.65 [NMC-Mg] 0.82 [NMC-Al] 0.75 DFT_SIMULATOR E_cal=-3.1 eV Cycles 520 Final Plan max reward path
P5: Materials Designer Safety Critic Synthesis Engineer Evaluation debate → D:✓ C:✗ E:? Consensus Plan Revise Mn-rich LiNiO2-Mg Proposal
P6: LLM CODE GENERATOR Prompt Generate DFT+Synthesis pipeline as Python script EXECUTABLE ARTIFACT workflow=DSL_Pipeline() workflow.add(DFT_Screening(candidates=100 criteria {"capacity": ">200"})) ... OR DAG explicit task dependencies
```

---

## C6.10 Memory / Action / Verifier Construction Blueprint (Survey M/A/V)

| Field | Content |
|---|---|
| **Source** | Scientific Intelligence Survey Sec 2.2 Memory + Sec 2.3 Action Space + Sec 2.4 Verifier + Figure1 typical architecture |
| **Purpose** | Mix-and-match memory + action + verifier building blocks enabling scientific agents operate rigor reproducibility ethical alignment. |
| **When to use** | After planner selection, constructing full agent recipe book for any scientific domain (chem, bio, materials, physics, geospatial, ML engineering, astronomy). |
| **Loop condition** | Iterative workflow Planner→Memory→Action→Verifier→Memory until verifier confirms validity reproducibility. |
| **Transition condition** | Verified results stored in Memory to refine future decisions, final integrated result returned. |

**Architecture workflow**

```text
User submits query scientific problem text+associated data Input
Planner decomposes task sub-tasks retrieves relevant context knowledge from Memory executes actions via Action Space APIs simulators lab instruments search engines LLM itself can function as part Action Space reasoning computation intermediate analysis
Actions generate intermediate results examined by Verifier accuracy consistency scientific plausibility
Verified results stored in Memory refine future decisions
If verification indicates further actions corrections Planner generates new plans re-invokes Action Space iterative continues until Verifier confirms output meets validity reproducibility
Final integrated result returned

Note previous multimodal agents separate perceptron Xie et al 2024 but survey integrates multimodal perception intrinsic capability Planner conceptual simplicity
```

**Memory types prompts**

```text
M1 Working Short-term: Maintain working memory scratchpad current task: Current goal {{goal}} Thoughts {{thoughts}} Recent observations {{observations}} Next action ...

M2 Episodic Reflexion-style: You have episodic memory past trials Relevant lessons from past trials {{memory_window}} last K reflections Rules Do not repeat failed strategies listed in lessons Prefer smallest test falsifying approach early Reflection format after failure Task {{task}} Trajectory {{trajectory}} Environment/test/reviewer feedback {{feedback}} Reflection 2-5 sentences actionable What specifically went wrong? What signal did you ignore? What will you do differently next one concrete policy change?

M3 Semantic Knowledge: Retrieve from knowledge store Domain KB HoneyComb / Vector DB / KG / Template Library Tool Ocean Query {{query}} Relevant facts {{retrieved_facts}} Use to inform planning. Examples CellVoyager self-evolving Template Library Tool Ocean expand knowledge skills, CoI person research interests citation history context, HoneyComb domain KB, STELLA.

M4 Procedural Skill library Voyager: Write description following successful procedure/function Rules 1) Do not mention function/procedure name 2) Do not mention logging/print/debug helpers 3) If helpers exist describe only main procedure 4) At most 6 sentences 5) Response must be single block plain text Procedure {{code_or_steps}} Main procedure is {{name}} Description stored skill library future retrieve-by-similarity. STELLA self-evolving mechanisms dynamic Template Library expandable Tool Ocean.

M5 Hybrid: Combination hierarchical working+episodic+semantic+procedural
```

**Action Space types prompts**

```text
A1 Internal Reasoning: LLM itself as part Action Space performing reasoning computation intermediate analysis Chain-of-thought Let's think step by step...

A2 External Tool API: You have access to tools {{tools_list}} e.g., VASP XRD_Simulator Autolab_API ChemCrow 18+ chemoinformatics tools GeneGPT genomic APIs PaSa search Semantic Scholar Academic Graph API To use tool output Action ToolName[args] Observation returned Example Action VASP[structure=LiNiO2-Mg calculation=DFT]

A3 Code Execution: Generate Python code perform task then execute Example ORGANA sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Code must be executable include imports handle errors

A4 Simulation: Use simulation as verification/feedback DFT_SIMULATOR E_cal=-3.1 eV Cycles 520 adsorption energies reaction energy barriers structural stability GeoSim.AI OpenFOAMGPT Configuration Generation Automated Execution Management Error-Driven Refinement modules Simulate outcomes each branch expand only physically plausible plans using simulation feedback search guidance SGA

A5 Physical Robotic Lab: Translate natural language instructions into executable protocols high-throughput liquid handlers AutoLabs self-correction robotic laboratory equipment designing executing synthesis procedures Suzuki Sonogashira cross-coupling minimal human intervention Coscientist engaging chemists natural language clarification updates experiments ORGANA Safety require human approval hazardous operations
```

**Verifier types prompts (see also C6.11 C6.12 for deep dives)**

```text
V1 Self-critique LLM as judge: Evaluate plan logical consistency feasibility Identify potential failure modes revise Current Plan {{plan}} Provide critique flags scores Chain-of-thought self-reflection iterative refinement VLM-based reflection multimodal plan evaluation figure quality LLMatDesign self-reflection previous decisions adapt rapidly zero-shot dZiner iterative reviewing history CoT stopping convergence criteria AtlasAgent CoT evaluation batch correction quality etc

V2 Tool-based Rule-based: Use tool-based verification simulation feedback atomistic simulations adsorption energies reaction energy barriers structural stability assign rewards prune unpromising pathways iteratively refine ChemReasoner code tests heuristic scoring comprehensive error traceback analysis GeoAgent dynamic refine subtask If verification fails trigger error-driven replanning Return Verified Yes/No + evidence

V3 Human-in-Loop (see C6.11 detailed) Approval gates safety-critical pause presentation synthesis procedures robotic control sequences hazardous awaiting explicit human approval Evaluation feedback research outputs human domain experts assess quality novelty validity qualitative critiques refinement Collaborative iteration multi-turn dialogues guidance constraints corrections Intervention debugging manual edit code adjust parameters redirect

V4 Multi-Agent Critique (see C6.12) Role-interactive verification distributing across collaborative ensembles MedAgents role-playing multi-round yes/no votes modification iteratively until consensus max attempts VirSci structured idea refinement critic novelty feasibility impact low filtered high refined CellAgent Evaluator Executor hyperparameter tuning automated scRNA-seq Sparks generation-reflection paired clarity novelty feasibility technical correctness completeness adherence AccelMat specialized critics Diversity Feasibility Scientific Rigor STELLA Dev+Critic AtomAgents Critic verification completeness correctness AutoLabs supervisor sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification AI co-scientist tournament debate 4 debate 2 for 2 against judge meta-review synthesizes insights multiple rounds recurring patterns optimize
```

---

## C6.11 Human-in-the-Loop Expert Oversight Gate (Survey V3)

| Field | Content |
|---|---|
| **Source** | Scientific Intelligence Survey Sec 2.4.3 V3 HITL Expert Oversight + examples |
| **Purpose** | Integrate human domain experts as authoritative evaluators at critical decision points for high-stakes scientific workflows where errors waste expensive resources compromise safety lead false claims. |
| **When to use** | Safety-critical synthesis procedures robotic control sequences hazardous operations, evaluation of research outputs quality novelty validity, collaborative iteration guidance constraints corrections shaping exploration, debugging when automated self-correction fails. |
| **Loop condition** | Spectrum continuous oversight to selective intervention to exception-based involvement. |
| **Transition condition** | Human approve/reject/feedback/intervention → continue or edit. |

**Prompt — HITL integration**

```text
You are integrating human expert oversight.

At critical decision point: {{decision_point}}
Agent output: {{agent_output}}

Human expert role: authoritative evaluator reviewing outputs at critical decision points, providing binding approval/rejection decisions, qualitative feedback informing subsequent reasoning, intervening when automated verification fails resolve ambiguities or when stakes demand human judgment.

Recognize limitations purely automated verification: LLMs lack genuine understanding physical reality cannot reliably detect all error classes particularly those requiring deep domain expertise tacit knowledge awareness subtle contextual factors. HITL particularly critical high-stakes scientific workflows where errors could waste expensive experimental resources compromise safety lead false scientific claims.

Modalities:
- Approval gates experimental protocols safety-critical procedures where agents pause execution present synthesis procedures robotic control sequences hazardous operations awaiting explicit human approval before proceeding (Mandal 2024 Boiko 2023 Zhou 2025 Wang 2025a StarWhisper)
- Evaluation and feedback research outputs human domain experts assess scientific quality novelty validity hypotheses papers experimental designs qualitative critiques informing refinement (Xin, Bran, Ansari, Schmidgall, Lu, Gottweis, Tang, de Haan, Yin, Ghafarollahi Buehler, Mehandru, Roohani, Su, Li, Tang 2025d, Alber, Tang 2025b, Zhao, Weng, Team, Ghareeb, Su)
- Collaborative human-AI iteration multi-turn dialogues humans guidance constraints corrections shaping exploration (Zhang 2025d Chemma active learning wet experiment results, Gottweis, Novikov, Pham, Ansari, Zou, Jin, He PaSa, Baek ResearchAgent)
- Intervention debugging error resolution automated self-correction fails human experts manual edit code adjust parameters redirect workflows (Chen 2024a Cao 2024 Ni Buehler)

Human action needed: approve/reject/feedback/intervention.
If approved continue; if rejected provide guidance; if intervention edit code/parameters.
Awaiting human: ...

Examples:
- Agent Laboratory Schmidgall assist human scientists ML research enabling users provide feedback guidance each stage high-level notes improvement deciding proceed
- StarWhisper Wang integrates astronomers telescope operation workflows natural language observation requests generates specific telescope control sequences presents planned observations astronomers verification they match intended scientific goals executes only after plan revising approval humans
- ORGANA Darvish engages chemists natural language clarify goals handle disambiguation provide updates ORGANA.REASONER prompts user investigate decide further actions if experimental outcomes mismatch expectations
- BIA Xin incorporate human intervention critical junctures ensure accuracy relevance dynamic workflows subset segmentation manual indispensable precision tailoring
- ChemCrow Bran evaluation panel 4 expert chemists Correctness Quality reasoning Degree task completion human interaction required fix invalid actions synthesis procedures before execution robotic platform if cannot autonomously adapt
- dZiner Ansari supports closed-loop and human-in-loop chemist review proposed candidates reasoning offering feedback suggesting additional modifications constraints
- Chemma Zhang active learning framework chemists interacting providing feedback collected wet experiment results crucial autonomously experimental exploration optimization open reaction spaces fine-tuning
- MAPPS Zhou integrates scientists discovery loop hypotheses designs presents experts evaluation ranking incorporates feedback refining proposals requires explicit scientist approval before computationally expensive simulations syntheses
- MatPilot Ni human-machine collaboration framework
```

---

## C6.12 Multi-Agent Knowledge Debate Tournament (Survey V4/P5)

| Field | Content |
|---|---|
| **Source** | Scientific Intelligence Survey Sec 2.4.4 V4 + Sec 2.1.1 P5 role-interactive + cathode example + AI co-scientist tournament |
| **Purpose** | Distribute verification across diverse perspectives providing comprehensive error coverage supporting sophisticated collaborative reasoning patterns for knowledge tracking. |
| **When to use** | Research proposal evaluation, novelty feasibility impact filtering, automated high-quality scRNA-seq, material hypothesis diversity checking. |
| **Loop condition** | Message-passing until convergence or max attempts threshold, tournament rounds multiple. |
| **Transition condition** | Consensus plan or verdict + revisions list; if not consensus continue until max. |

**Prompt — General multi-agent critique**

```text
Role-interactive verification distributing verification across collaborative agent ensembles.

You are assigned Role: {{role}} where role ∈ [Materials Designer, Safety Critic, Synthesis Engineer, Device Tester, Diversity Critic (evaluates whether proposed hypotheses explore sufficiently diverse regions materials space avoiding redundant similar proposals), Feasibility Critic (assessing whether hypotheses experimentally realizable given available equipment constraints), Scientific Rigor Critic (checking whether hypotheses grounded valid scientific principles clear testable predictions), Dev Agent (environment building code creation model training report writing), Critic Agent (assesses intermediate results flaws actionable feedback), Judge Agent (evaluates debate arguments declares winners), Meta-review Agent (synthesizes insights multiple rounds recurring patterns optimizing performance), Evaluator, Executor, Planner Critic]

Task: Evaluate plan/proposal:
Plan: {{plan}}

Provide assessment per dimension:
- Clarity, novelty, feasibility, technical correctness, completeness, adherence to system standards
- For Diversity Critic: check diverse regions avoidance redundant
- For Feasibility Critic: equipment constraints
- For Scientific Rigor Critic: valid principles testable predictions
- Vote: yes/no
- Score: 1-5
- Required revisions: numbered checklist

If consensus reached (all yes) or max attempts threshold reached, finalize; else revise based on modifications iteratively.

Mechanisms:
- MedAgents Tang role-playing multi-round discussions several expert agents give votes yes/no preliminary summary report propose modification opinions if vote no report revised based modifications iteratively until all experts agree max attempts threshold
- VirSci Su structured idea refinement through critic agents evaluate generated research ideas novelty feasibility impact potential low-scoring filtered out high-scoring refined targeted feedback
- CellAgent Xiao multi-agent critique Evaluator assesses quality current results allows Executor optimize solutions hyperparameter tuning tool selection automated scRNA-seq
- Sparks Ghafarollahi Buehler generation-reflection strategy each core agent paired corresponding reflection agent evaluate output clarity novelty feasibility technical correctness completeness adherence standards
- AccelMat Kumbhar specialized critics Diversity Feasibility Scientific Rigor
- STELLA Jin orchestrates multi-agent ecosystem Dev Agent focuses environment building code creation model training report writing Critic Agent assesses intermediate results flaws actionable feedback refine approach robust iterative problem-solving loop
- AtomAgents Ghafarollahi Buehler incorporates Critic agent performing role-based verification evaluating plan proposed Planner ensuring completeness correctness
- AutoLabs Panapitiya multi-agent architecture supervisor agent orchestrates workflow among specialized sub-agents Understand Refine Chemical Calculations Vial Arrangement Processing Steps Final Steps Self-Checks final verification step

Example tournament-style debate (AI co-scientist Gottweis):
- 4 debate agents (2 for and 2 against research proposal) engage structured argumentation
- Judge agent evaluates arguments declares winners
- Meta-review agent synthesizes insights multiple tournament rounds identify recurring patterns optimize performance subsequent iterations
- Synthesizes insights optimizing agent performance

Return verdict + revisions + consensus plan.

Running example from Figure 3:
Materials Designer: Proposes LiNiO2-Mg doped layered oxide Al2O3 coating
Safety Critic: O2 release risk high C:✗
Synthesis Engineer: D:✓ capacity feasible E:? equipment unknown
Evaluation and debate → D:✓ C:✗ E:? Consensus Plan
Revise: Mn-rich LiNiO2-Mg Proposal
```

---

# CONSTITUTION QUICK MAP — UPDATED FOR PART 6

| Need | Start with |
|---|---|
| Hard reasoning | C1.1 → C1.2 → (optional) C1.3–C1.5 |
| Choose methods | C2.1 + C6.9 Planner Taxonomy Router |
| Research idea | C2.2 → C2.3 → C2.4 → C6.4 → C6.5 → C6.6 (gap→problem→method→experiment) |
| Track knowledge gaps explicit | C6.1 |
| Infer implicit gaps | C6.2 → C6.3 (paragraph + full-paper) |
| Cross-domain knowledge pollination | C6.8 Entity Store Retrieval |
| Improve a draft | C3.1 ⇄ C3.2 + C6.7 ReviewingAgents |
| Learn from failure | C3.3 → C3.4 + C6.10 M2 Episodic |
| Improve the instruction | C3.5 |
| Save a reusable skill | C3.6 + C6.10 M4 Procedural |
| Make the repo pro | C4.1 → C4.2 → C4.3 |
| Multi-expert project | C5.1 + C6.12 Multi-Agent Debate Tournament |
| Human oversight high-stakes | C6.11 HITL Expert Gate |
| Open-ended progress | C5.4 / C5.5 + C6.10 Memory/Action/Verifier blueprint |
| Build any scientific agent | C6.9 → C6.10 (Planner Router → Memory/Action/Verifier blueprint) |
| Search when uncertain knowledge gaps | C1.6 + C6.9 + C2.1 + C6.4 Search-Based Gap Exploration (P4) |
| Ship end-to-end | C5.6 + C6.10 |

---

# GOVERNANCE NOTES — EXTENDED FOR PART 6

1. **Universal ≠ vague.** Keep placeholders concrete when you instantiate.
2. **Prefer small loops with gates** over one giant prompt.
3. **Honesty rule:** if evidence is weak, force rebuttals/limits (C3.1 aspects + C2.5 + C6.2 Warrant coherence).
4. **Budget rule:** route (C1.6, C2.1, C6.9) before expensive search/optimize.
5. **Memory rule:** verbal lessons (C3.3) and procedural skills (C3.6) and entity store (C6.8) and semantic KB (C6.10 M3) are different—use all four when appropriate.
6. **Knowledge tracking rule:** explicit gaps C6.1 require exact sentence grounding + cue list; implicit gaps C6.2 require Grounds quoted + Warrant single sentence + Bucket calibration; full-paper gaps C6.3 require evidence spans with section refs + feasibility notes + author survey if possible.
7. **Cross-domain rule:** entity retrieval C6.8 may retrieve opposite concepts (limitations mentioned with proposals) — LLM must filter noise, gain incidental value from random inputs per ResearchAgent ablation — random entities still better than none.
8. **Human-in-loop rule:** high-stakes experiments must have V3 approval gates (C6.11) — pause before hazardous robotic synthesis, telescope control, expensive simulations; require explicit human approval; human expertise indispensable for subset segmentation precision tailoring (BIA) and fixing invalid actions before robotic execution (ChemCrow).
9. **Multi-agent rule:** diverse critics (Diversity Feasibility Scientific Rigor) avoid echo chambers — include 4 debate agents 2 for 2 against + judge + meta-review (AI co-scientist tournament) for comprehensive error coverage.
10. **Construction rule:** any scientific agent = mix-and-match planner (P1-P6 L1-L2) + memory (M1-M5) + action (A1-A5) + verifier (V1-V4) — use cathode-design example as recipe book: Battery Schema → Augmented with historical failures + KB thresholds → Reflective revision cycles → Search-based max reward path → Role-interactive debate consensus → Programmatic DSL pipeline executable artifact.
11. **This constitution is a control layer**, not a substitute for domain expertise, licenses, or ethics review. For scientific agents, ethics and reproducibility are design imperatives embedded in architecture and verification modules per Survey Sec 5, not peripheral concerns. Ethics checklist + reproducibility protocol mandatory.

---

*Maintained with the ARSENAL unified master pipeline.*  
*Repo: https://github.com/faresrafat3/arsenal-unified-master-pipeline*  
*Updated 2026-07-11 with GAPMAP + ResearchAgent + Scientific Intelligence Survey extractions — Part 6 HOW TO TRACK KNOWLEDGE*

---

## C6.13 STORM Perspective Discovery — Related Topics + TOCs + Editors (GenRelatedTopics & GenPerspectives)

| Field | Content |
|---|---|
| **Source** | STORM Listing 1 GenRelatedTopicsPrompt + GenPerspectivesPrompt + Algorithm 1 Lines 4,11 + Figure 2 overview survey related Wikipedia articles |
| **Purpose** | Discover diverse perspectives multifaceted information by surveying similar topics TOCs, ensuring breadth coverage beyond basic facts. |
| **When to use** | Pre-writing research stage for any long-form grounded article requiring breadth (Wikipedia-like, technical reports, literature surveys). |
| **Loop condition** | Generate related topics list → extract TOCs via Wikipedia-API → concatenate TOCs → prompt LLM identify N perspectives + p0 basic fact writer. N=5. |
| **Transition condition** | Perspectives P = [P0] + P[:N] where P0 = basic fact writer focusing broadly covering basic facts about topic, each p ∈ P will be utilized to guide question asking in parallel. |

**Prompt — GenRelatedTopics**

```text
class GenRelatedTopicsPrompt(dspy.Signature):
    """
    I'm writing a Wikipedia page for a topic mentioned below. Please identify and
    recommend some Wikipedia pages on closely related subjects. I'm looking for
    examples that provide insights into interesting aspects commonly associated
    with this topic , or examples that help me understand the typical content and
    structure included in Wikipedia pages for similar topics.

    Please list the urls in separate lines.
    """

    topic = dspy.InputField(prefix=" Topic of interest:", format=str)
    related_topics = dspy.OutputField()
```

**Prompt — GenPerspectives**

```text
class GenPerspectivesPrompt(dspy.Signature):
    """
    You need to select a group of Wikipedia editors who will work together to create
    a comprehensive article on the topic. Each of them represents a different
    perspective , role , or affiliation related to this topic. You can use other
    Wikipedia pages of related topics for inspiration. For each editor , add
    description of what they will focus on.

    Give your answer in the following format: 1. short summary of editor 1:
    description\n2. short summary of editor 2: description\n...
    """

    topic = dspy.InputField(prefix='Topic of interest:', format=str)
    examples = dspy.InputField(prefix='Wiki page outlines of related topics for\ninspiration :\n', format=str)
    perspectives = dspy.OutputField()
```

**Implementation note**

```text
related_topics ← gen_related_topics(t) via GenRelatedTopicsPrompt
tocs ← []
foreach related_t in related_topics:
    article ← get_wiki_article(related_t) via Wikipedia-API https://pypi.org/project/Wikipedia-API/
    if article then tocs.append(extract_toc(article))
P ← gen_perspectives(t, tocs) via GenPerspectivesPrompt with concatenated TOCs
P ← [P0] + P[:N] where P0 = basic fact writer focusing broadly covering basic facts about topic
```

**Running example 2022 Winter Olympics Opening Ceremony**

Related topics: Winter Olympics history, opening ceremonies other Olympics, Beijing National Stadium etc. TOCs concatenated provide insights interesting aspects commonly associated typical content structure. Perspectives example: event planner focusing preparation opening ceremony, transportation coordinator, budget analyst, cultural significance, broadcasting etc. + p0 basic fact writer ensuring basic information.

---

## C6.14 STORM Simulated Conversations — Perspective-Guided Question Asking + Search & Answer

| Field | Content |
|---|---|
| **Source** | STORM Listing 1 GenQnPrompt + GenQueriesPrompt + GenAnswerPrompt + Listing 2 DirectGenOutline + RefineOutline + Algorithm 1 Lines 19,22,24,31,32 + Figure 1A direct prompting vs 1B perspective-guided vs 1C conversational |
| **Purpose** | Iterative research via multi-turn conversations writer perspective asks, expert grounded on Internet answers, enabling follow-up in-depth questions beyond surface What/When/Where. |
| **When to use** | After perspective discovery, needing depth breadth questions grounded on trusted sources, N+1 perspectives * M rounds ~30 Q/A pairs. |
| **Loop condition** | For each p ∈ P, for i=1..M (M=5): q=gen_qn(t,p,dlg_history) → queries=gen_queries(t,q) → sources=search_and_sift(queries) via YouRM You.com search API search_top_k 10 ground truth excluded → a=gen_ans(t,q,sources) → R append sources, convo_history append q+a. |
| **Transition condition** | convos = {C0..CN} collected, R references collection, then OD=direct_gen_outline(t) draft general framework # ## ### then O=refine_outline(t,OD,convos) comprehensive final outline. |

**Prompts**

**GenQnPrompt — Question Asking**

```text
class GenQnPrompt(dspy.Signature):
    """
    You are an experienced Wikipedia writer and want to edit a specific page.
    Besides your identity as a Wikipedia writer , you have a specific focus when
    researching the topic.

    Now , you are chatting with an expert to get information. Ask good questions to
    get more useful information.

    When you have no more question to ask , say "Thank you so much for your help!" to
    end the conversation.

    Please only ask one question at a time and don't ask what you have asked before.
    Your questions should be related to the topic you want to write.
    """

    topic = dspy.InputField(prefix='Topic you want to write: ', format=str)
    persona = dspy.InputField(prefix='Your specific perspective: ', format=str)
    conv = dspy.InputField(prefix='Conversation history :\n', format=str)
    question = dspy.OutputField()
```

**GenQueriesPrompt — Search Query Generation**

```text
class GenQueriesPrompt(dspy.Signature):
    """
    You want to answer the question using Google search. What do you type in the
    search box?

    Write the queries you will use in the following format:- query 1\n- query 2\n...
    """

    topic = dspy.InputField(prefix='Topic you are discussing about: ', format=str)
    question = dspy.InputField(prefix='Question you want to answer: ', format=str)
    queries = dspy.OutputField()
```

**GenAnswerPrompt — Grounded Answer**

```text
class GenAnswerPrompt(dspy.Signature):
    """
    You are an expert who can use information effectively. You are chatting with a
    Wikipedia writer who wants to write a Wikipedia page on topic you know. You
    have gathered the related information and will now use the information to
    form a response.

    Make your response as informative as possible and make sure every sentence is
    supported by the gathered information.
    """

    topic = dspy.InputField(prefix='Topic you are discussing about:', format=str)
    conv = dspy.InputField(prefix='Question :\n', format=str)
    info = dspy.InputField(prefix='Gathered information :\n', format=str)
    answer = dspy.OutputField(prefix='Now give your response :\n')
```

**DirectGenOutlinePrompt — Draft from intrinsic knowledge**

```text
class DirectGenOutlinePrompt(dspy.Signature):
    """
    Write an outline for a Wikipedia page.

    Here is the format of your writing:

    1. Use "#" Title" to indicate section title , "##" Title" to indicate
    subsection title , "###" Title" to indicate subsubsection title , and so
    on.

    2. Do not include other information.
    """

    topic = dspy.InputField(prefix=" Topic you want to write: ", format=str)
    outline = dspy.OutputField(prefix=" Write the Wikipedia page outline :\n")
```

**RefineOutlinePrompt — Improve with conversations**

```text
class RefineOutlinePrompt(dspy.Signature):
    """
    Improve an outline for a Wikipedia page. You already have a draft outline that
    covers the general information. Now you want to improve it based on the
    information learned from an information -seeking conversation to make it more
    comprehensive.

    Here is the format of your writing:

    1. Use "#" Title" to indicate section title , "##" Title" to indicate
    subsection title , "###" Title" to indicate subsubsection title , and so
    on.

    2. Do not include other information.
    """

    topic = dspy.InputField(prefix=" Topic you want to write: ", format=str)
    conv = dspy.InputField(prefix=" Conversation history :\n", format=str)
    old_outline = dspy.OutputField(prefix=" Current outline :\n", format=str)
    outline = dspy.OutputField(prefix='Write the Wikipedia page outline :\n')
```

**Writing stage reconstruction**

```text
Given topic t, outline O, references R collected pre-writing stage, full-length article composed section by section:
- Section title + subheadings used retrieve relevant documents from R based semantic similarity Sentence-BERT embeddings
- LLM prompted generate section with citations [1][2] every sentence supported
- Concatenate all sections form draft full-length article
- LLM prompted delete repeated information improve coherence polished article
- In alignment Wikipedia stylistic norms LLM utilized synthesize summary entire article forming lead section beginning lead 2-3 paragraphs concise overview
```

**Evaluation**

- FreshWiki: top 100 most-edited pages per month Feb2022-Sep2023 filter B-class ORES exclude list no subsections plain text only avoid leakage
- Heading soft recall: count(Ai)=1/sum_j Sim(Ai,Aj) Sim=cos embed paraphrase-MiniLM-L6-v2 card(A)=sum count recall=card(G∩P)/card(G) intersection via union card(G∩P)=card(G)+card(P)-card(G∪P) + heading entity recall FLAIR NER
- Article: Prometheus 13B evaluator Interest Coherence Organization Relevance Focus Coverage trimmed 2000 words iterative removing shortest section + citation recall precision Gao et al Mistral 7B + expert Wikipedia editors organized +25% absolute broad coverage +10% vs outline-driven RAG baseline challenges source bias transfer over-association

**Algorithm 1 pseudocode**

```text
P0 = basic fact writer focusing broadly covering basic facts about the topic
R = []
related_topics = gen_related_topics(t)
tocs = []
foreach related_t in related_topics: article = get_wiki_article(related_t) if article then tocs.append(extract_toc(article))
P = gen_perspectives(t, tocs)
P = [P0] + P[:N]
convos = []
foreach p in P:
  convo_history = []
  for i=1..M:
    q = gen_qn(t,p,dlg_history) convo_history.append(q)
    queries = gen_queries(t,q) sources = search_and_sift(queries) a = gen_ans(t,q,sources) convo_history.append(a) R.append(sources)
  convos.append(convo_history)
OD = direct_gen_outline(t)
O = refine_outline(t, OD, convos)
return O,R
```

Hyperparams N=5 M=5 search_top_k 10 max_thread_num 1 device cpu vector_db_mode offline do_research do_generate_outline do_generate_article do_polish_article

---

## C6.15 SciMON Background + Inspiration Retrieval + Iterative Novelty Boosting

| Field | Content |
|---|---|
| **Source** | SciMON 2305.14259 problem setting Sec 2.1 + inspiration retrieval Table8 + iterative novelty boosting Figure1 + in-context contrastive + evaluation Table9 Table10 |
| **Purpose** | Generate novel scientific directions grounded in literature with explicit novelty optimization via comparing to prior literature and updating, plus in-context contrastive reducing copying. |
| **When to use** | Background context problems motivations experimental settings constraints + optional seed term v focus point, need novelty not merely paraphrasing background. |
| **Loop condition** | Retrieve inspirations semantic KG citation → generate initial idea Given [context] a [new idea] Δ vs prior work → iterative novelty boosting compare I with prior literature {(Background_i, idea_i)} if strongly overlapping update more novel like good researcher until sufficient novelty achieved. |
| **Transition condition** | Novelty achieved, human evaluation relevance utility novelty technical depth, automated ROUGE-L BERTScore BARTScore, challenging gold subsets, error analysis generic suggestions woven specifics copied directly context etc. |

**Prompt — Problem Setting**

```text
You are a scientific inspiration machine optimized for novelty (SciMON). AI-based assistant suggests ideas natural language.

Input: Background context B consisting of:
- M: current problems, motivations, experimental settings and constraints (e.g., Continual learning aims enable information systems learn from continuous data stream...)
- Optionally seed term v focus point of generated idea I (e.g., speech unit boundaries, Irish language learning, data augmentation effective solution to data scarcity low-resource scenarios...).

Goal: Generate natural language idea I novel w.r.t B and broader literature corpus not merely paraphrasing background, grounded in literature inspirations retrieved.

Approach systematic:
- Step1 Read background B understand problems motivations experimental settings constraints.
- Step2 Consider seed term v if provided limit hypothesis space.
- Step3 Review inspirations past scientific papers retrieved: semantic neighbors, KG neighbors, citation neighbors related problems solutions contexts scientific KG ground ideas.
- Step4 Generate initial idea: "Given [context], a [new idea], Δ vs prior work..." Focus novelty vs B and broader literature.
- Step5 Avoid generic suggestions woven specifics copied directly context (e.g., NLP with ML algorithms sentiment analysis problem X, data augmentation transfer learning Y, BERT RoBERTa Z, Data preprocessing Clean text remove unnecessary characters tokenization...). Reduce copying rephrasing directly from context. Apply logical modifications beyond simple flipping high latency→low latency or efficiency limitations→highly efficient.

Output:
Idea: [Natural language description proposed method/idea]
Novelty Δ: [How differs from prior work and background]
Grounding: [Which inspirations support idea]
```

**Prompt — Inspiration Retrieval**

```text
Given background context B and seed term v, retrieve inspirations from past scientific papers:

3 types:

1. Semantic Neighbors: semantically similar problems and solutions via semantic similarity graphs (e.g., low-resource tagging tasks, end-to-end speech translation, visual question answering)

2. KG Neighbors: knowledge graph neighbors via scientific knowledge graph from PubTator 3 etc (e.g., task-oriented dialog systems, low-resource languages LRL, clinical semantic textual similarity)

3. Citation Neighbors: citation co-occurrence neighbors (e.g., Contextual Augmentation: Data Augmentation by Words with Paradigmatic Relations etc)

Collection: 67,408 ACL Anthology papers 1952-2022 via Semantic Scholar Academic Graph API non-commercial + 5,708 PubMed 1988-2024 Entrez, IE system PubTator 3 extracts KG from abstracts, sentence classifier trained annotated abstracts selects background context.

For each retrieved inspiration provide Title, Background context, Idea summary.

Return list inspirations similar to ground truth underlined.

Example Input context data augmentation effective solution data scarcity low-resource however token-level tasks ner suffer token-label misalignment unsatisfactory performance
Semantic Neighbors list, KG Neighbors list, Citation Neighbors list
Ground Truth ELM: Data Augmentation with Masked Entity Language Modeling for Low-Resource NER
```

**Prompt — Iterative Novelty Boosting**

```text
You are AI-based assistant suggests ideas iteratively boosting novelty.

You have background context B and idea I generated at step t.

Task: Compare I with existing research literature: Prior Literature {(Background_i, idea_i)}.

If you find strongly overlapping research, update idea to be more novel relative to prior work, much like a good researcher would do.

Steps:
1. Take idea I at step t.
2. Compare I with existing research in literature: Check semantic overlap with prior papers (Background_i, idea_i) from inspiration retrieval.
3. If strongly overlapping, identify overlapping concepts and propose update that increases Δ vs prior work.
4. Output updated Idea I_{t+1} more novel relative prior work still grounded.

Example Initial Idea pause prediction model to identify speech unit boundaries...
Prior includes existing pause prediction...
If overlap high update Iteration1 leverages acoustic linguistic features dynamically ensuring smooth transitions differs combining acoustic properties linguistic context
Iteration2 ASUBD attention mechanisms focus relevant acoustic linguistic features reinforcement learning guide optimal predictions

Goal sufficient novelty achieved. Continue iterations until threshold met.

Return Updated Idea + Novelty Δ explanation + which prior literature compared.
```

**Data Example**

```text
Seed Term: speech unit boundaries
Context abridged: generate partial sentence translation given streaming speech input existing approaches break acoustic units in speech as boundaries between acoustic units in speech are not even
Initial idea: A pause prediction model to identify speech unit boundaries
Iteration1: A method that leverages acoustic and linguistic features to predict speech unit boundaries dynamically ensuring smooth transitions ... differs as combines both acoustic properties and linguistic context ...
Iteration2: Adaptive Speech Unit Boundary Detection (ASUBD) ... combination attention mechanisms focus relevant acoustic linguistic features reinforcement learning guide system make optimal predictions unit boundaries based previous decisions
Ground Truth: efficient monotonic segmentation module accumulate acoustic information incrementally detect proper speech unit boundaries
```

---

## C6.16 SciPIP Quintuple + Multi-Granularity Retrieval + Dual-Path Idea Generation

| Field | Content |
|---|---|
| **Source** | SciPIP 2410.23166 quintuple construction ~78K papers + entity extraction τ2 + summary problem main idea + background motivations details + concise methods τ3 example style transform + background transformation teacher student + multi-granularity retrieval SE CC CL Table4 Recall10 + dual-path idea proposer 10 ideas |
| **Purpose** | Enhance LLM-based proposal scientific ideas through improvements both literature retrieval (semantic + citation awareness precise efficient) and idea generation (dual-path content retrieved papers + internal knowledge). |
| **When to use** | Literature retrieval phase keyword-based neglects semantic incomplete, even semantic vector entire sections multifaceted difficult capture key points, idea generation relies internal knowledge metadata overlooking full texts. |
| **Loop condition** | Collect ~78K papers top-tier AI conferences → LLM re-summarize each paper into structured quintuple keywords backgrounds ideas concise methods references individually encoded vectors stored database → multi-granularity retrieval leveraging keywords semantic embeddings citation relations thorough exhaustive SE CC CL → dual-path framework ~10 ideas clear innovative valid comprehensive. |
| **Transition condition** | Retrieval Recall10 0.419 Recall20 0.544 etc vs SCIMON-like 0.381 vs ResearchAgent-like 0.377 more thorough, non-matching ideas more valuable novel ideas not appear human, novelty feasibility practical value boosted. |

**Prompt — Entity Extraction τ2**

```text
System: Now you are an expert in extracting key entities from research contents. You are good at identifying the most important keywords or phrases that summarize the main topics or concepts discussed in the content.

User: Task Description: I will provide you with a content from a research paper. Your task is to extract the key entities from this content. These entities are the most important keywords or phrases that summarize the main topics or concepts discussed in the content.
Instruction: Content is key focus extracted entities should be based content concrete manifestations main themes topics systematic reading main themes topics identify list key entities central content ensure relevant meaningful representative content Each entity ≤5 words ≥2 words ≤5 entities nouns noun phrases examples {examples} Your turn: Given following content: {content} Your answer format entity1, entity2, entity3, ......

Constraints: Each entity ≤5 words, ≥2 words, ≤5 entities, nouns or noun phrases.
```

**Prompt — Summary Problem Main Idea Format**

```text
Task Description: You are provided with title, abstract, and introduction of research paper. Your task generate concise summary what kind of problem does paper aim to solve and what methods proposed address it. Summary should follow format: The problem of [problem] can be addressed by [main idea/approach].
Instructions: Title read title understand general topic Abstract read abstract get concise summary research including problem addressed methods used main findings Introduction read introduction gain deeper understanding background significance specific problem paper addresses as well as proposed approach solution Based on provided information generate single sentence captures essence paper following format specified Your Turn: Given following paper info Title title Abstract abstract Introduction introduction Output The problem of [problem] can be addressed by [main idea/approach].
```

**Prompt — Background Motivations Details**

```text
Please read title, abstract, introduction again as well as summary you provided. Complete two tasks:
1. Briefly provide two most critical motivations behind proposing these methods to address problems.
2. Briefly provide three most critical innovative details of paper that were not mentioned in summary It's best if these details are new methods techniques adopted in this paper.
Output: Motivations:1.[motivation1]. 2.[motivation2]. Details:1.[detail1]. 2.[detail2]. 3.[detail3].
```

**Prompt — Concise Methods τ3 Example Style Transform**

```text
# Task Description: You are AI researcher conducting studies specific domain Someone provided methodology section task transform into another style I will give example begins Example 1 includes Example Summarized Methods Then your task starts Your Task containing Your Methodology Section Your job transform Your Methodology Section into Summarized Methods by referring to Example1 Note ideas in Example1 unrelated to your idea so key focus should be style of Example Summarized Methods You should directly start response and do not start with section title like ## Your Summarized Methods
# Example1
## Example Summarized Methods
{Example Summarized Methods}
# Your Task
## Your Methodology Section
{methodology}
## Your Summarized Methods
```

**Prompt — Background Transformation Teacher Student**

```text
System: You are teacher in field AI skilled at clearly explaining AI concepts to students Your student is undergraduate AI basic understanding deep learning

User: You are teaching your undergraduate about specific subfield AI research You have brief description research background and now need explain its meaning purpose detail to undergraduate Keep in mind undergraduate may be completely unfamiliar technical terms research background Example begin...

Task: Explain meaning and purpose of background in detail for undergraduate unfamiliar technical terms example-based style.
```

**Prompt — Idea Proposer Dual-Path 10 Ideas**

```text
System: Now you are researcher in field AI with innovative pioneering abilities You are good at using innovative original methods to solve cutting-edge problems in field AI

User: Task Description: You will be provided with research problem along with rationales Your task brainstorm ideas clear innovative valid comprehensive address problem Additionally some cue words along with summaries backgrounds contributions methods of related papers will be provided as sources inspiration for generating novel ideas.
Information Provided:
1. Research Problem & Rationales: key issues aspects problem need addressed These form foundation generating ideas
2. Related Papers: Draw inspiration abstracts backgrounds methods these papers Delve deeply methods understand motivations behind them think critically how they might inform approach Avoid merely stacking existing methods integrate relevant aspects with own insights create original solutions
Approach systematic:
- Step1 Thoroughly read research problem understand primary focus
- Step2 Review summaries backgrounds contributions methods related papers gain broader perspective insights relevant problem
- Step3 Based on provided information propose ideas clear innovative valid comprehensive
Specific Information: I will provide specific info now please use them according instructions above:
1. Research Problem & Rationales: {problem}
2. Related Papers: {related__papers__information}
Format Your Response ensure final ideas include about 10 entries presented format:
**Idea 1**: [The first method idea]
**Idea 2**: [The second method idea]
**Idea 3**: [The third method idea]
...
```

**Multi-Granularity Retrieval**

```text
Comprehensively leverages keywords semantic embeddings citation relations enabling thorough literature retrieval

Three granularity:

- Keywords retrieval exact keyword match entity extraction τ2 output entities

- Semantic embeddings semantic-entity based retrieval SE proposed semantic-entity based retrieval encode quintuple components individually into vectors vs encoding entire sections e.g. abstracts into vectors entire sections typically contains multifaceted information such approach makes difficult capture key points effectively This impacts both encoding quality retrieval performance

- Citation relations citation co-occurrence CC and clustering CL

Multi-granularity retrieval algorithm comprehensive leverages keywords semantic embeddings citation relations enabling thorough literature retrieval

Literature retrieval results Table4 groundtruth real citations tested papers Recall10 recall rate top10 ranked among retrieved literature compared ground truth citations Recall10 means recall rate top10 ranked papers among retrieved literature compared ground truth citations Table5 ablation SE means proposed semantic-entity based retrieval CC means citation co-occurrence CL means clustering Since AI Scientist does not perform literature retrieval when generating ideas results primarily on SCIMON and ResearchAgent for generating scientific paper ideas differ from those in this study

Results AI Scientist Not Applicable SCIMON-like Recall10 0.381 0.481 0.548 0.587 0.616 ResearchAgent-like 0.377 0.484 0.550 0.598 0.622 SciPIP Ours 0.419 0.544 0.615 0.657 0.684 demonstrating more thorough exhaustive retrieval Ablation SE CC CL combinations Non-matching ideas may be more valuable because SciPIP generate novel ideas not appear or even not put forward by human
```

**Dual-Path**

```text
Path1 content retrieved papers summaries backgrounds contributions methods + Path2 extensive internal knowledge LLM Integration significantly boosts novelty feasibility practical value

Experiments conducted various domains NLP CV demonstrate capability generate multitude innovative useful ideas Findings underscore potential valuable tool researchers seeking advance fields groundbreaking concepts Novelty experiments non-matching ideas may be more valuable because SciPIP generate novel ideas not appear or even not put forward by human
```

---

# CONSTITUTION QUICK MAP — UPDATED FOR PART 6 EXPANDED (15 SYSTEMS)

| Need | Start with |
|---|---|
| Hard reasoning | C1.1 → C1.2 → (optional) C1.3–C1.5 |
| Choose methods | C2.1 + C6.9 Planner Taxonomy Router |
| Research idea | C2.2 → C2.3 → C2.4 → C6.4 → C6.5 → C6.6 (gap→problem→method→experiment) + C6.15 SciMON + C6.16 SciPIP dual-path 10 ideas |
| Track knowledge gaps explicit | C6.1 |
| Infer implicit gaps | C6.2 → C6.3 (paragraph + full-paper) + C6.15 SciMON background context problems motivations |
| Cross-domain knowledge pollination | C6.8 Entity Store Retrieval + C6.15 Inspiration Retrieval semantic KG citation + C6.16 Quintuple keywords backgrounds ideas methods refs + multi-granularity SE CC CL |
| Improve a draft | C3.1 ⇄ C3.2 + C6.7 ReviewingAgents |
| Learn from failure | C3.3 → C3.4 + C6.10 M2 Episodic |
| Improve the instruction | C3.5 |
| Save a reusable skill | C3.6 + C6.10 M4 Procedural |
| Make the repo pro | C4.1 → C4.2 → C4.3 |
| Multi-expert project | C5.1 + C6.12 Multi-Agent Debate Tournament + C6.15 Iterative Novelty Boosting + C6.16 Dual-Path |
| Human oversight high-stakes | C6.11 HITL Expert Gate + V3 approval gates |
| Open-ended progress | C5.4 / C5.5 + C6.10 Memory/Action/Verifier blueprint + C6.13 Perspective Discovery + C6.14 Simulated Conversations |
| Build any scientific agent | C6.9 → C6.10 (Planner Router → Memory/Action/Verifier blueprint) |
| Search when uncertain knowledge gaps | C1.6 + C6.9 + C2.1 + C6.4 Search-Based Gap Exploration (P4) + C6.15 Inspiration Retrieval + C6.16 Multi-Granularity |
| Long-form grounded writing | C6.13 → C6.14 (Related Topics → TOCs → Perspectives P=[P0]+P[:N] → Simulated Conversations M rounds question queries search sift answer → Draft OD + Refine O → Section generation Sentence-BERT retrieval + citations + polish + lead) + STORM FreshWiki evaluation heading soft recall paraphrase-MiniLM-L6-v2 + Prometheus 13B + citation recall precision + expert organized +25% broad +10% |
| Ship end-to-end | C5.6 + C6.10 + C6.13-6.16 |

---

# GOVERNANCE NOTES — EXTENDED FOR PART 6 EXPANDED (STORM + SciMON/SciPIP)

1. **Universal ≠ vague.** Keep placeholders concrete when you instantiate.
2. **Prefer small loops with gates** over one giant prompt.
3. **Honesty rule:** if evidence is weak, force rebuttals/limits (C3.1 aspects + C2.5 + C6.2 Warrant coherence + C6.14 every sentence supported by gathered information).
4. **Budget rule:** route (C1.6, C2.1, C6.9) before expensive search/optimize. For STORM, N=5 perspectives M=5 rounds search_top_k 10 cost balance, cheaper/faster model conv_simulator_lm split queries synthesize answers, more powerful model article_gen_lm verifiable text citations.
5. **Memory rule:** verbal lessons (C3.3) and procedural skills (C3.6) and entity store (C6.8) and semantic KB (C6.10 M3) and quintuple keywords backgrounds ideas methods refs (C6.16) are different—use all when appropriate.
6. **Knowledge tracking rule:** explicit gaps C6.1 require exact sentence grounding + cue list; implicit gaps C6.2 require Grounds quoted + Warrant single sentence + Bucket calibration; full-paper gaps C6.3 require evidence spans with section refs + feasibility notes + author survey if possible; SciMON background context M problems motivations experimental settings constraints + seed term v focus point novel w.r.t B broader corpus not merely paraphrase; SciPIP quintuple individually encoded vectors precise efficient retrieval.
7. **Cross-domain rule:** entity retrieval C6.8 may retrieve opposite concepts (limitations mentioned with proposals) — LLM must filter noise, gain incidental value from random inputs per ResearchAgent ablation — random entities still better than none. Inspiration retrieval semantic KG citation may retrieve similar ground truth underlined Table8 example ELM Data Augmentation with Masked Entity Language Modeling for Low-Resource NER.
8. **Human-in-loop rule:** high-stakes experiments must have V3 approval gates (C6.11) — pause before hazardous robotic synthesis, telescope control, expensive simulations; require explicit human approval; human expertise indispensable for subset segmentation precision tailoring (BIA) and fixing invalid actions before robotic execution (ChemCrow). For STORM, expert Wikipedia editors evaluation organized +25% broad +10% vs RAG baseline, but challenges source bias transfer bias Internet affects articles + over-association unrelated facts fabricate connections new frontiers.
9. **Multi-agent rule:** diverse critics (Diversity Feasibility Scientific Rigor) avoid echo chambers — include 4 debate agents 2 for 2 against + judge + meta-review (AI co-scientist tournament) for comprehensive error coverage. For perspective discovery, include p0 basic fact writer focusing broadly covering basic facts about topic + N perspectives diverse stakeholders prioritize varying facets.
10. **Construction rule:** any scientific agent = mix-and-match planner (P1-P6 L1-L2) + memory (M1-M5) + action (A1-A5) + verifier (V1-V4) — use cathode-design example as recipe book: Battery Schema → Augmented with historical failures + KB thresholds → Reflective revision cycles → Search-based max reward path → Role-interactive debate consensus → Programmatic DSL pipeline executable artifact. For long-form grounded writing STORM = Perspective Discovery Related Topics TOCs → Perspectives P=[P0]+P[:N] → Simulated Conversations M rounds question queries search sift answer → Draft OD internal knowledge + Refine O with convos → Section generation Sentence-BERT retrieval from R + citations + polish + lead.
11. **Retrieval rule:** multi-granularity retrieval leveraging keywords semantic embeddings citation relations thorough exhaustive SE CC CL — encode quintuple components individually preprocessed into vectors vs entire sections multifaceted difficult capture key points effective encoding quality retrieval performance impact. Recall10-50 metrics: AI Scientist Not Applicable SCIMON-like 0.381 ResearchAgent-like 0.377 SciPIP Ours 0.419 more thorough. Non-matching ideas more valuable novel ideas not appear human.
12. **Novelty rule:** iterative novelty boosting compare Idea_t with prior literature {(Background_i, idea_i)} if strongly overlapping update more novel relative prior work like good researcher until sufficient novelty achieved. In-context contrastive CL SN KG CT T5+CL etc helps better baseline reducing reliance copying Table9 R-L BERT. Avoid generic suggestions woven specifics copied directly context Data preprocessing Clean text remove unnecessary characters tokenization etc simple logical modifications high latency→low latency.
13. **Grounded writing rule:** STORM perspective-guided question asking: direct prompting Ask 30 questions yields When was opening held Where how many countries basic What When Where limited planning capacity, perspective-guided You are event planner focusing preparation opening ceremony leads varied questions transportation arrangements budget cultural broadcasting security, conversational Can you provide list participating countries ... over 90 countries entering stadium specific order How is order determined transportation arrangements budget elicits follow-up in-depth iterative research grounded Internet.
14. **This constitution is a control layer**, not substitute domain expertise, licenses, ethics review. For scientific agents ethics and reproducibility are design imperatives embedded architecture verification modules per Survey Sec5 not peripheral concerns. Ethics checklist + reproducibility protocol mandatory. FreshWiki dataset creation avoiding leakage top 100 most-edited per month Feb2022-Sep2023 filter B-class ORES exclude list no subsections plain text only process repeated future dates new LLMs emerge. Heading soft recall paraphrase-MiniLM-L6-v2 cosine + entity recall FLAIR NER + Prometheus 13B Interest Coherence Organization Relevance Focus Coverage trimmed 2000 words iterative removing shortest section.

---

*Maintained with the ARSENAL unified master pipeline.*  
*Repo: https://github.com/faresrafat3/arsenal-unified-master-pipeline*  
*Updated 2026-07-11 with GAPMAP + ResearchAgent + Scientific Intelligence Survey + STORM + SciMON/SciPIP extractions — Part 6 HOW TO TRACK KNOWLEDGE expanded to 15 systems*

---

# PART 7 — HOW TO COLLABORATE
*(multi-agent patterns · role-playing · conversable agents · conversation programming)*

---

## C7.1 CAMEL Inception Prompting — Task Specifier Making Specific

| Field | Content |
|---|---|
| **Source** | CAMEL Figure1 Task Specifier + Sec 3.1 Role-playing Framework + Inception Prompting definition |
| **Purpose** | Transform preliminary human idea into well-defined specific task using LLM instead of relying on human inputs, enabling autonomous cooperation minimal human supervision. |
| **When to use** | Only preliminary idea given (e.g., Develop a trading bot for the stock market), need specific task before role-playing session; also for Math/Science datasets automatically generating problem topics subtopics problems. |
| **Loop condition** | 1 per human idea, prompting LLM to make specific. |
| **Transition condition** | Specified Task example: Develop a trading bot with a sentiment analysis tool that can monitor social media platforms for positive or negative comments about particular stock, and execute trades based on sentiment analysis results. |

**Prompt**

```text
You are a task specifier. Given a preliminary idea from human user, make it more specific and well-defined.

Preliminary Idea: {{human_idea}}
Roles: AI Assistant: {{assistant_role}}, AI User: {{user_role}}

Task: Transform preliminary idea into specified task that includes concrete requirements, tools, and goals.

Example: Idea "Develop a trading bot for the stock market" with roles Python Programmer and Stock Trader becomes:

Specified Task: Develop a trading bot with a sentiment analysis tool that can monitor social media platforms for positive or negative comments about a particular stock, and execute trades based on sentiment analysis results

Output specified task only, concise but specific.

This is prompting LLMs instead of relying on human inputs. For Math and Science datasets, generate problem topics, subtopics, and problems automatically by prompting LLMs.
```

**Related quote**

> "What's the most resilient parasite? An Idea. A single idea from the human mind can build cities. An idea can transform the world and rewrite all the rules. Which is why I have to steal it." - Dom Cobb, Inception

---

## C7.2 CAMEL Role Assignment PA PU — Assistant Planner vs Executor

| Field | Content |
|---|---|
| **Source** | CAMEL Sec Methodology AI Assistant-User Role Assignment + Equation 1 M_t |
| **Purpose** | Assign distinct roles via system messages PA PU before conversation, defining planner vs executor to maintain consistency and avoid role flipping. |
| **When to use** | After task specification, before conversation starts, need A ← F_{PA} and U ← F_{PU} where F1,F2 large-scale auto-regressive LMs. |
| **Loop condition** | Once per task, system messages passed before conversations start. |
| **Transition condition** | Assistant role = Python Programmer task executor offering solutions executing planned steps, User role = Stock Trader task planner interactive planning feasible steps. Then collaboration instruction-following manner. |

**Prompt — PA (Assistant System Message) — Executor**

```text
You are a {{assistant_role}} (e.g., Python Programmer). You are an AI assistant that is a task executor.

You will be given a specified task: {{specified_task}}
Your role is to offer solutions, execute planned steps, and provide responses to the AI user who is a {{user_role}}.

You should:
- Provide solutions that fulfill the AI user's instructions.
- Execute planned steps via code or reasoning.
- Respond with solution that includes code if needed, explanation, and next steps.
- Avoid role flipping: you are the assistant, not the user. Do not provide instructions, only solutions.
- Avoid repeating instructions: do not repeat the user's instruction verbatim as your solution.
- Avoid flake replies: provide substantive content.
- Avoid infinite loop: if task completed, say Task completed or provide final summary.

Conversation history: {{Mt}}
Current instruction from AI user: {{It}}

Provide your solution as assistant:
Solution:
```

**Prompt — PU (User System Message) — Planner**

```text
You are a {{user_role}} (e.g., Stock Trader). You are an AI user that is a task planner.

You have a specified task: {{specified_task}}

Your role is to engage in interactive planning to determine feasible steps for the AI assistant who is a {{assistant_role}} to execute.

You should:
- Provide instructions that guide the assistant toward task completion.
- Each instruction should be one clear step, with Input if needed.
- Format: Instruction: {{instruction}} Input: {{input}} or None
- After assistant provides solution, evaluate if task completed or next step needed.
- If task completed, say "Task completed" or similar termination.
- Maintain consistency with human intentions: ensure tasks align with original human idea {{human_idea}}.
- Avoid role flipping: you are the user (planner), not the assistant (executor).
- Provide feasible steps, not impossible.

Conversation history: {{Mt}}
Current assistant solution: {{St}}

Provide your next instruction as user:
Instruction:
```

**Formal conversation definition**

```
M_t = {(I0,S0),...,(It,St)} = {(Ii,Si)}|t i=0
At next time step t+1, AI user U takes history M_t and generates I_{t+1}, assistant A generates S_{t+1} etc until termination

Example loop:
Instruction: Install necessary Python libraries for sentiment analysis and stock trading.
Input: None
Solution: To install necessary Python libraries for sentiment analysis and stock trading, we can use pip... pip install tweepy textblob yfinance Next request.

Role Playing Session
Instruction: Import necessary libraries in Python.
Input: None
Solution: Here's code to import these libraries: import tweepy from textblob import TextBlob import pandas as pd import numpy as np import yfinance as yf Next request.
```

**Challenges mitigation**

- role flipping, assistant repeating instructions, flake replies, infinite loop of messages — mitigated via inception prompting maintaining consistency with human intentions + PA PU system messages passed before conversations start + termination conditions task completed or max messages limit cost grows quadratically vs max tokens vs loop detection.

---

## C7.3 CAMEL Data Generation — AI Society Roles and Tasks + Evaluation

| Field | Content |
|---|---|
| **Source** | CAMEL Figure3 Data Generation Prompts AI Society + Sec 4.1 Role-Playing for AI Society + Sec 5 Evaluation Agent Evaluation Human Evaluation GPT4 Evaluation |
| **Purpose** | Scalable approach generating possible roles and tasks via LLM to reduce human involvement, creating conversational task-oriented instruction-following datasets for behavior analysis and capability understanding + evaluation via summarization fair comparison. |
| **When to use** | Building AI Society and Code datasets cooperative scenarios, Math and Science single-turn QA emergent abilities, Misalignment malicious risks, and evaluating via 100 tasks + GPT4 summarization + human votes. |
| **Loop condition** | Generate NUM_ROLES assistant roles + NUM_ROLES user roles + NUM_TASKS tasks per pair, then role-playing conversations until termination, cost grows quadratically with length conversation making essential set limit. |
| **Transition condition** | AI Society dataset large conversational task-oriented instruction-following + Code + Math + Science + Misalignment; evaluation random select 100 tasks AI Society + 100 tasks Code + GPT4 summarization consolidated final solution larger token limit suitable undetectable format fair comparison vs single-shot gpt-3.5-turbo + human 453 responses AI Society only + GPT4 scoring decision which better Model1 vs Model2 + knowledge emergence fine-tuning LLaMA + HumanEval HumanEval+. |

**Prompts — Data Generation Figure3**

**Assistant Role Generation Prompt**

```text
You are a helpful assistant that can play many different roles. Now please list <NUM_ROLES> different roles that you can play with your expertise in diverse fields. Sort them by alphabetical order. No explanation required.
```

**User Role Generation Prompt**

```text
Please list <NUM_ROLES> most common and diverse groups of internet users or occupations. Use singular form. No explanation. Sort them by alphabetical order. No explanation required.
```

**Task Generation Prompt**

```text
List <NUM_TASKS> diverse tasks that <ASSISTANT_ROLE> can assist <USER_ROLE> cooperatively to achieve together. Be concise. Be creative.
```

**Scalable approach note**

```text
Firstly prompt LLM agent generate possible roles assistant and user We achieve this by providing LLM agent specific prompts designed elicit these roles Next ask LLM agent generate range possible tasks that can be solved through collaboration between assistant and user roles Cost grows quadratically with length conversation making essential set limit Methodology focuses studying communicative agents under cooperative settings where they share common interests In particular study assistant-user scenario where preliminary idea given at start Agents will conceptualize idea into specific task and complete it autonomously through conversations
```

**Math and Science datasets**

```text
For generated Math and Science datasets generated problem topics subtopics problems automatically by prompting LLMs prompting LLMs instead of relying human inputs
```

**Misalignment dataset**

```text
Simulation possible malicious applications demonstrate potential risks unaligned autonomous agent system
```

**Evaluation — Agent Evaluation**

```text
Randomly select 100 tasks from AI Society dataset evaluation and 100 tasks from Code dataset Then employ GPT4 model summarize content CAMEL conversation-based solution presenting consolidated final solution Particularly GPT4 is used since possesses larger token limit suitable summarization Summarization also makes CAMEL agents solution undetectable by its format allowing more fair comparison Subsequently solution compared with single-shot solution generated by gpt-3.5-turbo model same task
```

**Human Evaluation prompt**

```text
Present both CAMEL summarized agent solution and gpt-3.5-turbo single-shot solution side-by-side human participants Identity behind each solution not revealed Participants then asked vote whether one solution superior other or if equally good Total 453 responses collected during evaluation Note human evaluation only done for AI Society as assessing code generally harder humans without running code
```

**GPT4 Evaluation prompt**

```text
Engage GPT4 agent evaluate effectiveness Model1 CAMEL Agent solution versus Model2 gpt-3.5-turbo single-shot solution each task More specifically prompt GPT4 score decide which solution two solutions is better Results summarized Table1 showcases CAMEL solution outperforms gpt-3.5-turbo single-shot
```

**Summarization**

```text
Employ GPT4 model summarize content CAMEL conversation-based solution presenting consolidated final solution Particularly GPT4 is used since possesses larger token limit suitable summarization Summarization also makes CAMEL agents solution undetectable by its format allowing more fair comparison
```

---

## C7.4 AutoGen Conversable Agents — Assistant, UserProxy, GroupChatManager

| Field | Content |
|---|---|
| **Source** | AutoGen Sec 2.1 Conversable Agents + Figure2 yellow-shaded built-in agents + Sec 2.2 Conversation Programming unified interfaces |
| **Purpose** | Provide customizable conversable agents with unified send/receive/generate_reply interfaces and auto-reply mechanism for automated agent chat decentralized modular unified workflow. |
| **When to use** | Building any LLM application via multiple agents that can converse to accomplish tasks operating in various modes combinations LLMs human inputs tools. |
| **Loop condition** | Agent maintains internal context based on sent and received messages; once receives message automatically invokes generate_reply sends reply back unless termination condition satisfied. |
| **Transition condition** | Built-in reply functions LLM inference code/function execution human input + custom reply functions e.g. chatting with another agent before replying to sender → conversation flow naturally induced without extra control plane special module controls conversation flow. |

**Spec — ConversableAgent base**

```text
ConversableAgent class highest-level agent abstraction and by default can use LLMs, humans, and tools
Maintains internal context based on sent and received messages
Can be configured to possess set of capabilities enabled by LLMs, tools, or human input
Supports many common composable capabilities:
  1) LLMs: LLM-backed agents exploit many capabilities advanced LLMs such as role playing, implicit state inference and progress making conditioned on conversation history, providing feedback, adapting from feedback, coding. Combined different ways via novel prompting techniques to increase skill and autonomy. Enhanced LLM inference features such as result caching, error handling, message templating via enhanced LLM inference layer
  2) Humans: Human involvement desired or essential many LLM applications. Allows human participate agent conversation via human-backed agents which could solicit human inputs at certain rounds conversation depending agent configuration. Default user proxy agent allows configurable human_input_mode frequency and conditions for requesting human input including option humans skip providing input
  3) Tools: Tool-backed agents capability execute tools via code execution or function execution. For example default user proxy agent able execute code suggested by LLMs or make LLM-suggested function calls

Unified interfaces:
send: sending messages
receive: receiving messages
generate_reply: taking actions and generating response based on received message

Auto-reply mechanism:
Once agent receives message from another agent it automatically invokes generate_reply and sends reply back to sender unless termination condition satisfied
Provides built-in reply functions based on LLM inference code or function execution or human input
One can also register custom reply functions customize behavior pattern of agent e.g. chatting with another agent before replying to sender agent
```

**AssistantAgent pre-configured**

```text
AssistantAgent and UserProxyAgent two pre-configured ConversableAgent subclasses each representing common usage mode i.e. acting as AI assistant backed by LLMs and acting as human proxy to solicit human input or execute code/function calls backed by humans and/or tools

AssistantAgent:
human_input_mode = "NEVER"
code_execution_config = False
DEFAULT_SYSTEM_MESSAGE = "You are a helpful AI assistant... In the following cases, suggest python code..."

Natural-language control via LLMs: Default system message of built-in AssistantAgent uses natural language to instruct agent to fix errors and generate code again if previous result indicates errors It also guides agent confine LLM output certain structures making it easier for other tool-backed agents consume For example instructing agent to reply with TERMINATE when all tasks completed terminate program
```

**UserProxyAgent pre-configured**

```text
UserProxyAgent acting as human proxy to solicit human input or execute code/function calls backed by humans and/or tools
human_input_mode = "ALWAYS" (or NEVER depending example)
group_chat = []
Note when no reply func registered list default reply functions will be used

Capabilities:
- Solicit human inputs at certain rounds depending configuration frequency and conditions for requesting human input including option humans skip providing input
- Execute code suggested by LLMs or make LLM-suggested function calls via code execution or function execution
```

**GroupChatManager**

```text
GroupChatManager human_input_mode = "NEVER"
group_chat = []
Note when no reply func registered list default reply functions will be used

Supports more complex dynamic group chat via built-in GroupChatManager which can dynamically select next speaker and then broadcast its response to other agents
Elaborates feature and its application in Section 3
```

---

## C7.5 AutoGen Conversation Programming — Initiation + Unified + Auto-reply + Computation + Control Flow

| Field | Content |
|---|---|
| **Source** | AutoGen Sec 2.2 Conversation Programming Figure2 initiation + program execution dialog box + unified interfaces and auto-reply mechanisms |
| **Purpose** | Program multi-agent conversation via conversation-centric computation and conversation-driven control flow maximizing reusability implemented agents. |
| **When to use** | Developing two-agent system with custom reply function, static conversation predefined flow and dynamic flows, applications ranging mathematics coding Q&A operations research online decision-making entertainment etc. |
| **Loop condition** | Once reply functions registered and conversation initialized conversation flow naturally induced and thus agent conversation proceeds naturally without any extra control plane special module controls conversation flow. Task progresses through conversations displayed dialog box. |
| **Transition condition** | Bottom sub-figure shows how individual agents perform role-specific conversation-centric computations generate responses e.g. via LLM inference calls and code execution; middle sub-figure demonstrates conversation-based control flow when assistant receives message user proxy agent typically sends human input as reply if no input executes any code in assistant's message instead. |

**Conversation Initiation Example Figure2**

```python
# 1. Define Agents
# 2. Initiate Conversations:
A.initiate_chat("Plot a chart of META and TESLA stock price change YTD.", B)
Assistant B
User Proxy A
AutoGen Agents
Developer Code
# This func will be invoked in generate_reply
A.register_reply(B, reply_func_A2B)
def reply_func_A2B(msg):
    output = input_from_human()
    ...
    if not output:
        if msg includes code:
            output = execute(msg)
    return output
ConversableAgent
AssistantAgent
UserProxyAgent
human_input_mode = "NEVER"
code_execution_config = False
DEFAULT_SYSTEM_MESSAGE = "You are a helpful AI assistant... In the following cases, suggest python code..."
human_input_mode = "ALWAYS"
GroupChatManager
human_input_mode = "NEVER"
group_chat = []
# Note when no reply func registered list default reply functions will be used
Agent Customization
Program Execution
Plot a chart of META and TESLA stock price change YTD.
Execute following code...
send receive receive
Conversation-Centric Computation generate_reply Error: package yfinance is not installed
send generate_reply Sorry! Please first pip install yfinance and then execute
Conversation-Driven Control Flow generate_reply The Resulting Automated Agent Chat
...
```

**Unified Interfaces Prompt**

```text
Agents in AutoGen have unified conversation interfaces for performing corresponding conversation-centric computation including a send/receive function for sending/receiving messages and a generate_reply function for taking actions and generating a response based on the received message

AutoGen also introduces and by default adopts an agent auto-reply mechanism to realize conversation-driven control: Once an agent receives message from another agent it automatically invokes generate_reply and sends reply back to sender unless termination condition satisfied

Provides built-in reply functions based on LLM inference code or function execution or human input

One can also register custom reply functions customize behavior pattern of agent e.g. chatting with another agent before replying to sender agent

Under this mechanism once reply functions registered and conversation initialized conversation flow naturally induced and thus agent conversation proceeds naturally without any extra control plane i.e. special module that controls conversation flow

For example with developer code blue-shaded area marked Developer Code of Figure2 one can readily trigger conversation among agents and conversation would proceed automatically as shown dialog box grey shaded area marked Program Execution of Figure2 Auto-reply mechanism provides decentralized modular unified way define workflow
```

**Conversation Programming Paradigm**

```text
Conversation programming paradigm considers two concepts: computation – actions agents take to compute response in multi-agent conversation And control flow – sequence or conditions under which these computations happen Ability program these helps implement many flexible multi-agent conversation patterns In AutoGen computations are conversation-centric Agent takes actions relevant to conversations involved and actions result in message passing for consequent conversations unless termination condition satisfied Similarly control flow is conversation-driven participating agents decisions which agents to send messages to and procedure of computation are functions of inter-agent conversation This paradigm helps reason intuitively about complex workflow as agent action taking and conversation message-passing between agents

Figure2 bottom sub-figure shows how individual agents perform role-specific conversation-centric computations generate responses e.g. via LLM inference calls and code execution Task progresses through conversations displayed dialog box Middle sub-figure demonstrates conversation-based control flow When assistant receives message user proxy agent typically sends human input as reply If no input executes any code in assistant's message instead
```

---

## C7.6 AutoGen Control Fusion — Natural Language TERMINATE + Programming max replies + Custom Reply

| Field | Content |
|---|---|
| **Source** | AutoGen Sec 2.2 Control by fusion of programming and natural language Figure2 Conversation-Driven Control Flow + Appendix C examples natural language controls |
| **Purpose** | Flexibly define agent interaction behaviors using both natural language and computer code to program conversation patterns for different applications. |
| **When to use** | Need natural-language control via LLMs e.g. fix errors generate code again confine output structures TERMINATE, programming-language control specify termination condition human input mode tool execution logic max number auto replies, and control transition between natural and programming language. |
| **Loop condition** | Programming-language control uses Python code specify termination condition, human input mode, tool execution logic e.g. max number auto replies; register programmed auto-reply functions control conversation flow with Python code as shown code block identified as Conversation-Driven Control Flow in Figure2. |
| **Transition condition** | Transition from code to natural-language control by invoking LLM inference containing certain control logic in customized reply function; transition from natural language to code control via LLM-proposed function calls (Eleti et al 2023). |

**Natural-language control via LLMs Prompt**

```text
You are a helpful AI assistant. If previous result indicates errors, fix errors and generate code again.
Confine your output to certain structures making it easier for other tool-backed agents to consume.
When all tasks are completed, reply with "TERMINATE" to terminate program.

Default system message of built-in AssistantAgent uses natural language to instruct agent to fix errors and generate code again if previous result indicates errors
Guides agent confine LLM output certain structures making it easier for other tool-backed agents consume
For example instructing agent to reply with TERMINATE when all tasks completed to terminate program
More concrete examples natural language controls can be found Appendix C
```

**Programming-language control via Python code**

```python
# Specify termination condition, human input mode, tool execution logic, e.g. max number auto replies
assistant = AssistantAgent(human_input_mode="NEVER", max_consecutive_auto_reply=5)
user_proxy = UserProxyAgent(human_input_mode="ALWAYS", code_execution_config={"work_dir": "coding"})

# Register programmed auto-reply functions to control conversation flow with Python code as shown code block identified as Conversation-Driven Control Flow in Figure2

def reply_func_A2B(msg):
    output = input_from_human()
    if not output:
        if msg includes code:
            output = execute(msg)
    return output

A.register_reply(B, reply_func_A2B)
```

**Control transition**

```text
AutoGen also supports flexible control transition between natural and programming language One can achieve transition from code to natural-language control by invoking LLM inference containing certain control logic in customized reply function or transition from natural language to code control via LLM-proposed function calls (Eleti et al 2023)
```

---

## C7.7 AutoGen Dynamic Conversation Flows — Custom generate_reply + Function Calls + GroupChatManager

| Field | Content |
|---|---|
| **Source** | AutoGen Sec 2.2 dynamic conversation flows + Sec 3 GroupChatManager dynamically select next speaker broadcast response |
| **Purpose** | Realize multi-agent conversations diverse patterns beyond static conversation predefined flow, including dynamic flows where LLM decides to call particular function or hold current conversation while invoking conversations with other agents depending content. |
| **When to use** | Applications where agents make meaningful progress on tasks need to specify and mold multi-agent conversations, need flexible control transition. |
| **Loop condition** | Customized generate_reply function: one agent can hold current conversation while invoking conversations with other agents depending content current message and context. Function calls: LLM decides whether or not to call particular function depending conversation status. By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation. GroupChatManager dynamically select next speaker broadcast response. |
| **Transition condition** | Working systems showcase all these different patterns implemented. |

**Prompt — Custom generate_reply dynamic**

```text
Within customized generate_reply function, one agent can hold the current conversation while invoking conversations with other agents depending on content of current message and context

Example:

def custom_generate_reply(self, messages, sender, config):
    # Hold current conversation
    if "need expert opinion" in messages[-1]["content"]:
        # Invoke conversation with other agents
        expert_agent = self.expert_agent
        result = expert_agent.generate_reply(messages, sender)
        # Incorporate expert result into current conversation
        return f"Expert opinion: {result}"
    else:
        # Default LLM inference
        return self.llm.generate_response(messages)

Register as:
agent.register_reply([other_agent], custom_generate_reply)
```

**Prompt — Function calls dynamic**

```text
In this approach LLM decides whether or not to call particular function depending on conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation

Function definition:

def call_expert_for_opinion(topic: str):
    # Message additional agents in called function
    expert_response = expert_agent.generate_reply([{"role": "user", "content": topic}])
    return expert_response

LLM prompt includes function description, LLM decides whether to call particular function depending conversation status
Messaging additional agents in called functions drives dynamic multi-agent conversation
```

**Prompt — GroupChatManager dynamic speaker selection**

```python
group_chat = [agent1, agent2, agent3]
manager = GroupChatManager(group_chat, llm_config=...)
# Manager dynamically selects next speaker and then broadcasts its response to other agents
# Elaborates feature and its application in Section 3
# Example:
# User asks "What if we prohibit shipping from supplier 1 to roastery 2?" to Commander
# Commander coordinates with Writer and Safeguard etc.
```

---

## C7.8 AutoGen Applications — Math + RAG Interactive Retrieval + ALFWorld Grounding + OptiGuide Commander Writer Safeguard

| Field | Content |
|---|---|
| **Source** | AutoGen Sec 3 Applications A1-A4 Figure4 Performance + Appendix D workflows + Figure3 OptiGuide implementation |
| **Purpose** | Showcase AutoGen serves as generic infrastructure build diverse applications various complexities LLM capacities domains mathematics coding question answering operations research online decision-making entertainment etc empirical studies demonstrate effectiveness. |
| **When to use** | Math problem solving, retrieval-augmented generation Q&A, decision making text world environments ALFWorld, multi-agent coding with safeguards OptiGuide. |
| **Loop condition** | A1 120 Level-5 problems Whole Dataset, A2 Natural Questions dataset vs DPR, A3 134 unseen tasks ALFWorld, A4 OptiGuide Commander coordinates Writer Safeguard repeated multiple times until user's question answered or timed-out, core workflow reduced 430 lines to 100 lines save 3x time reduce interactions 3-5 times. |
| **Transition condition** | Performance: A1 Math Success Ratio 69.48% Whole Dataset out-of-box competitive, A2 RAG F1 Recall 25.88% 66.65% etc AutoGen W/O interactive retrieval DPR, A3 ALFWorld 15% performance gain average with grounding agent 69% 54% etc, A4 OptiGuide F1 Recall 96% 98% etc Multi vs Single. |

**A1 Math — Two-agent out-of-box competitive**

```text
AutoGen agents can be used out of the box to achieve the most competitive performance on math problem solving tasks

Figure4a Performance on MATH w GPT-4 120 Level-5 problems Whole Dataset Success Ratio 69.48% Whole Dataset 55.18% Average vs ChatGPT+Code ChatGPT+Plugin GPT-4 Multi-Agent Debate LangChain ReAct
```

**A2 Retrieval-Augmented Chat RAG — Interactive Retrieval UPDATE CONTEXT**

```text
System consists two agents: Retrieval-augmented User Proxy agent and Retrieval-augmented Assistant agent both extended from built-in agents from AutoGen Retrieval-augmented User Proxy includes vector database Chroma with SentenceTransformers Reimers & Gurevych context retriever detailed workflow Appendix D

Evaluation natural question answering Natural Questions dataset Kwiatkowski et al 2019 report results Figure4b compare system with DPR Dense Passage Retrieval following existing evaluation practice Adlakha et al 2023

Leveraging conversational design natural-language control AutoGen introduces novel interactive retrieval feature in this application: whenever retrieved context does not contain information instead of terminating LLM-based assistant would reply "Sorry, I cannot find any information about... UPDATE CONTEXT." which will invoke more retrieval attempts Conduct ablation study prompt assistant agent to say "I don't know" instead of "UPDATE CONTEXT." in cases relevant information not found report results Figure4b results show interactive retrieval mechanism indeed plays non-trivial role process

Scenario2 further demonstrate how Retrieval-augmented Chat aids generating code based given codebase that contains code not included GPT-4 training data Evaluation demonstration details both scenarios Appendix D

Metrics Figure4b F1 Recall 25.88% 66.65% 15.12% 58.56% 22.79% 62.59% AutoGen vs AutoGen W/O interactive retrieval vs DPR
```

**A3 ALFWorld Decision Making — Two-agent + Grounding Agent 15% gain**

```text
Diverse collection synthetic language-based interactive decision-making tasks household environments

Two-agent system LLM-backed assistant agent responsible suggesting plans conduct task and executor agent responsible executing actions ALFWorld environments integrates ReAct prompting Yao et al 2022 able achieve similar performance

Common challenge encountered both ReAct and AutoGen-based two-agent system occasional inability leverage basic commonsense knowledge about physical world Deficiency can lead system getting stuck loop due repetitive errors

Fortunately modular design AutoGen allows address issue effectively: With AutoGen able introduce grounding agent which supplies crucial commonsense knowledge such as "You must find and take the object before you can examine it. You must go to where target object is before you can use it." whenever system exhibits early signs recurring errors Significantly enhances ability avoid getting entangled error loops Compare task-solving performance two variants our system with GPT-3.5-turbo and ReAct on 134 unseen tasks ALFWorld report results Figure4c results show introducing grounding agent could bring 15% performance gain average Upon examining systems outputs observe grounding agent by delivering background commonsense knowledge at right junctures significantly mitigated tendency system persist flawed plan thereby avoiding creation error loops Example trajectory comparing systems Appendix D Figure10

Metrics 69% 54% 54% 77% 63% 66% Average Best of 3 AutoGen 3 agent AutoGen 2 agent ReAct

Three-agent system with grounding agent:

Assistant (suggest plans)
Executor (execute actions in ALFWorld)
Grounding Agent (supplies crucial commonsense knowledge e.g., "You must find and take object before you can examine it. You must go to where target object is before you can use it." whenever early signs recurring errors - whenever system exhibits early signs recurring errors)

Performance 15% gain average
```

**A4 Multi-Agent Coding OptiGuide — Commander Writer Safeguard 430→100 lines save 3x time**

```text
System excels writing code interpret optimization solutions answer user questions such exploring implications changing supply-chain decision or understanding why optimizer made particular choice Second sub-figure Figure3 shows AutoGen-based implementation

Workflow: end user sends questions such "What if we prohibit shipping from supplier 1 to roastery 2?" to Commander agent Commander coordinates with two assistant agents including Writer and Safeguard to answer question Writer will craft code and send code to Commander After receiving code Commander checks code safety with Safeguard if cleared Commander will use external tools e.g. Python to execute code and request Writer to interpret execution results For instance writer may say if we prohibit shipping from supplier 1 to roastery 2 total cost would increase by 10.5% Commander then provides this concluding answer to end user If at particular step there is exception e.g. security red flag raised by Safeguard Commander redirects issue back to Writer with debugging information Process might be repeated multiple times until user's question answered or timed-out

With AutoGen core workflow code for OptiGuide reduced from over 430 lines to 100 lines leading significant productivity improvement Provide detailed comparison user experience ChatGPT+Code Interpreter and AutoGen-based OptiGuide Appendix D where show AutoGen-based OptiGuide could save around 3x of user's time and reduce user interactions by 3-5 times

Metrics Figure4d F1 Recall 96% 98% 88% 78% 83% 72% 48% 32% Multi-GPT4 Single-GPT4 Multi-GPT3.5 Single-GPT3.5 Performance OptiGuide Figure4d shows multi-agent design helpful boosting performance coding tasks need safeguards

Workflow example:

End user: What if we prohibit shipping from supplier 1 to roastery 2? → Commander
Commander → Writer: craft code
Writer → Commander: code
Commander → Safeguard: check safety
Safeguard → Commander: cleared / security red flag
If cleared: Commander uses external tools e.g. Python to execute code and request Writer interpret execution results → Writer: total cost increase 10.5% → Commander → End user: answer
If exception red flag: Commander redirects issue back to Writer with debugging info → repeat until answered or timed-out
```

---

## C7.9 Collaboration Quick Map

| Need | Start with |
|---|---|
| Minimal human supervision autonomous cooperation | C7.1 Task Specifier → C7.2 Role Assignment PA PU M_t |
| Instruction-following cooperation multi-agent | C7.2 PA PU M_t = {(I0,S0)...} instruction Input Solution Next request |
| Scalable data generation diverse roles tasks | C7.3 Assistant Role Generation list NUM_ROLES diverse roles alphabetical + User Role Generation list NUM_ROLES common diverse groups internet users occupations singular alphabetical + Task Generation list NUM_TASKS diverse tasks ASSISTANT_ROLE can assist USER_ROLE cooperatively Be concise Be creative |
| Conversable agents customizable | C7.4 ConversableAgent send/receive/generate_reply auto-reply mechanism unified interfaces + AssistantAgent human_input_mode NEVER DEFAULT_SYSTEM_MESSAGE helpful AI assistant suggest python code TERMINATE + UserProxyAgent human_input_mode ALWAYS + GroupChatManager dynamically select next speaker broadcast |
| Program conversation patterns | C7.5 Conversation Programming computation + control flow conversation-centric computation message passing unless termination conversation-driven control flow decisions which agents send messages procedure functions inter-agent conversation + Initiate chat A.initiate_chat Plot chart META TESLA YTD B + Custom reply A.register_reply B reply_func_A2B input_from_human if msg includes code execute |
| Flexible control | C7.6 Control Fusion natural-language control fix errors generate code again confine output structures TERMINATE Appendix C + programming-language control specify termination condition human input mode tool execution logic max number auto replies register programmed auto-reply functions Conversation-Driven Control Flow + transition code to natural invoking LLM inference containing control logic customized reply function natural to code via LLM-proposed function calls |
| Dynamic multi-agent flows | C7.7 Custom generate_reply hold current conversation while invoking conversations with other agents depending content + Function calls LLM decides whether to call particular function depending conversation status messaging additional agents in called functions drives dynamic conversation + GroupChatManager dynamically select next speaker broadcast |
| Math problem solving out-of-box | C7.8 A1 Math 120 Level-5 Success Ratio 69.48% vs ChatGPT+Code etc |
| Retrieval-augmented Q&A interactive retrieval | C7.8 A2 RAG Retrieval-augmented User Proxy Chroma SentenceTransformers Natural Questions vs DPR interactive retrieval Sorry I cannot find any information about... UPDATE CONTEXT vs I don't know ablation F1 Recall 25.88% 66.65% etc |
| Decision making text world avoid error loops | C7.8 A3 ALFWorld Two-agent assistant suggesting plans executor executing actions ReAct + grounding agent supplies commonsense You must find and take object before you can examine it You must go to where target object is before you can use it whenever early signs recurring errors 15% gain 134 unseen tasks |
| Multi-agent coding with safeguards productivity | C7.8 A4 OptiGuide Commander coordinates Writer Safeguard What if we prohibit shipping from supplier 1 to roastery 2 Writer crafts code Commander checks safety with Safeguard if cleared executes Python request Writer interpret results total cost increase 10.5% If exception security red flag redirect back to Writer debugging repeated until answered or timed-out reduced 430 lines to 100 lines save 3x time reduce interactions 3-5 times |

---

# CONSTITUTION QUICK MAP — UPDATED FOR PART 7 (17 SYSTEMS)

| Need | Start with |
|---|---|
| Hard reasoning | C1.1 → C1.2 → (optional) C1.3–C1.5 |
| Choose methods | C2.1 + C6.9 Planner Taxonomy Router |
| Research idea | C2.2 → C2.3 → C2.4 → C6.4 → C6.5 → C6.6 (gap→problem→method→experiment) + C6.15 SciMON + C6.16 SciPIP dual-path 10 ideas + C7.2 Role Assignment PA PU conceptualize into specific task |
| Track knowledge gaps explicit | C6.1 |
| Infer implicit gaps | C6.2 → C6.3 (paragraph + full-paper) + C6.15 SciMON background context problems motivations |
| Cross-domain knowledge pollination | C6.8 Entity Store Retrieval + C6.15 Inspiration Retrieval semantic KG citation + C6.16 Quintuple keywords backgrounds ideas methods refs + multi-granularity SE CC CL |
| Improve a draft | C3.1 ⇄ C3.2 + C6.7 ReviewingAgents + C7.3 GPT4 Evaluation score decide which better |
| Learn from failure | C3.3 → C3.4 + C6.10 M2 Episodic + C7.8 A3 grounding agent supplies commonsense You must find and take object before examine |
| Improve the instruction | C3.5 |
| Save a reusable skill | C3.6 + C6.10 M4 Procedural |
| Make the repo pro | C4.1 → C4.2 → C4.3 |
| Multi-expert project | C5.1 + C6.12 Multi-Agent Debate Tournament + C6.15 Iterative Novelty Boosting + C6.16 Dual-Path + C7.2 PA PU + C7.4 ConversableAgent + C7.7 Dynamic Flows GroupChatManager |
| Human oversight high-stakes | C6.11 HITL Expert Gate + C7.4 UserProxy human_input_mode ALWAYS solicits human inputs + C7.8 A4 Commander checks safety with Safeguard security red flag |
| Open-ended progress | C5.4 / C5.5 + C6.10 Memory/Action/Verifier blueprint + C6.13 Perspective Discovery + C6.14 Simulated Conversations + C7.3 scalable data generation diverse roles tasks |
| Build any scientific agent | C6.9 → C6.10 (Planner Router → Memory/Action/Verifier blueprint) + C7.4 C7.5 C7.6 C7.7 |
| Search when uncertain knowledge gaps | C1.6 + C6.9 + C2.1 + C6.4 Search-Based Gap Exploration (P4) + C6.15 Inspiration Retrieval + C6.16 Multi-Granularity + C7.7 Dynamic Flows |
| Long-form grounded writing | C6.13 → C6.14 (Related Topics → TOCs → Perspectives P=[P0]+P[:N] → Simulated Conversations M rounds question queries search sift answer → Draft OD + Refine O → Section generation Sentence-BERT retrieval + citations + polish + lead) + STORM FreshWiki evaluation heading soft recall paraphrase-MiniLM-L6-v2 + Prometheus 13B + citation recall precision + expert organized +25% broad +10% |
| Autonomous cooperation minimal human | C7.1 Task Specifier → C7.2 PA PU M_t = {(I0,S0)...} instruction Input Solution Next request → C7.3 Data Generation AI Society role task generation + evaluation 100 tasks GPT4 summarization fair comparison human 453 responses |
| Conversable agents | C7.4 ConversableAgent send/receive/generate_reply auto-reply mechanism + AssistantAgent NEVER DEFAULT_SYSTEM_MESSAGE + UserProxy ALWAYS + GroupChatManager dynamically select next speaker |
| Program conversation patterns | C7.5 Unified interfaces auto-reply + Conversation Programming computation + control flow + Initiate chat A.initiate_chat + Custom reply A.register_reply + Program Execution dialog box Error package yfinance not installed Sorry please pip install + Conversation-Centric Computation generate_reply Conversation-Driven Control Flow |
| Flexible control | C7.6 Natural-language control fix errors generate code again confine structures TERMINATE Appendix C + Programming-language control termination condition human input mode tool execution logic max number auto replies + Transition code ↔ natural invoking LLM inference or LLM-proposed function calls |
| Dynamic multi-agent | C7.7 Custom generate_reply hold current conversation while invoking conversations with other agents depending content + Function calls LLM decides whether to call particular function + GroupChatManager dynamic speaker selection broadcast + OptiGuide Commander Writer Safeguard pattern |
| Math out-of-box | C7.8 A1 Math 120 Level-5 Success Ratio 69.48% vs ChatGPT+Code |
| RAG interactive retrieval | C7.8 A2 RAG Retrieval-augmented User Proxy Chroma SentenceTransformers Natural Questions vs DPR interactive retrieval Sorry cannot find any information UPDATE CONTEXT vs I don't know ablation |
| Decision making avoid loops | C7.8 A3 ALFWorld Two-agent plus grounding agent 15% gain 134 unseen tasks |
| Multi-agent coding productivity | C7.8 A4 OptiGuide Commander Writer Safeguard reduced 430→100 lines save 3x time reduce interactions 3-5 times |
| Ship end-to-end | C5.6 + C6.10 + C6.13-6.16 + C7.1-7.8 |

---

# GOVERNANCE NOTES — EXTENDED FOR PART 7 EXPANDED (CAMEL + AutoGen — 17 SYSTEMS)

1. **Universal ≠ vague.** Keep placeholders concrete when you instantiate.
2. **Prefer small loops with gates** over one giant prompt.
3. **Honesty rule:** if evidence is weak, force rebuttals/limits (C3.1 aspects + C2.5 + C6.2 Warrant coherence + C6.14 every sentence supported by gathered information + C7.8 citation recall precision).
4. **Budget rule:** route (C1.6, C2.1, C6.9) before expensive search/optimize. For CAMEL, cost grows quadratically with length conversation making essential set limit; for STORM, N=5 perspectives M=5 rounds search_top_k 10 cost balance, cheaper/faster model conv_simulator_lm split queries synthesize answers, more powerful model article_gen_lm verifiable text citations; for AutoGen, specify max_consecutive_auto_reply termination condition.
5. **Memory rule:** verbal lessons (C3.3) and procedural skills (C3.6) and entity store (C6.8) and semantic KB (C6.10 M3) and quintuple keywords backgrounds ideas methods refs (C6.16) and conversational history M_t = {(I0,S0)...} are different—use all when appropriate. For CAMEL, M_t grows pairs instruction-solution streaming, for AutoGen internal context based on sent and received messages.
6. **Knowledge tracking rule:** explicit gaps C6.1 require exact sentence grounding + cue list; implicit gaps C6.2 require Grounds quoted + Warrant single sentence + Bucket calibration; full-paper gaps C6.3 require evidence spans with section refs + feasibility notes + author survey if possible; SciMON background context M problems motivations experimental settings constraints + seed term v focus point novel w.r.t B broader corpus not merely paraphrase; SciPIP quintuple individually encoded vectors precise efficient retrieval; CAMEL task specifier makes preliminary idea specific well-defined prompting LLM instead of relying human inputs; STORM perspective discovery via surveying related Wikipedia articles TOCs concatenated + simulated conversations N+1 perspectives M rounds.
7. **Cross-domain rule:** entity retrieval C6.8 may retrieve opposite concepts (limitations mentioned with proposals) — LLM must filter noise, gain incidental value from random inputs per ResearchAgent ablation — random entities still better than none. Inspiration retrieval semantic KG citation may retrieve similar ground truth underlined Table8 example ELM Data Augmentation with Masked Entity Language Modeling for Low-Resource NER. For CAMEL, diverse roles alphabetical order diverse groups internet users occupations singular alphabetical diverse tasks concise creative.
8. **Human-in-loop rule:** high-stakes experiments must have V3 approval gates (C6.11) — pause before hazardous robotic synthesis, telescope control, expensive simulations; require explicit human approval; human expertise indispensable for subset segmentation precision tailoring (BIA) and fixing invalid actions before robotic execution (ChemCrow). For STORM, expert Wikipedia editors evaluation organized +25% broad +10% vs RAG baseline, but challenges source bias transfer bias Internet affects articles + over-association unrelated facts fabricate connections new frontiers. For CAMEL, human evaluation side-by-side anonymous vote superior equally good 453 responses AI Society only as assessing code harder humans without running code. For AutoGen, human involvement desired or essential many LLM applications via human-backed agents soliciting human inputs at certain rounds depending configuration Default user proxy agent allows configurable human_input_mode frequency and conditions for requesting human input including option humans skip providing input.
9. **Multi-agent rule:** diverse critics (Diversity Feasibility Scientific Rigor) avoid echo chambers — include 4 debate agents 2 for 2 against + judge + meta-review (AI co-scientist tournament) for comprehensive error coverage. For perspective discovery, include p0 basic fact writer focusing broadly covering basic facts about topic + N perspectives diverse stakeholders prioritize varying facets. For CAMEL, AI user serves as task planner interactive planning feasible steps AI assistant acts as task executor offering solutions executing planned steps providing responses. Challenges role flipping assistant repeating instructions flake replies infinite loop messages mitigated via inception prompting maintaining consistency human intentions PA PU system messages passed before conversations start. For AutoGen, unified interfaces send receive generate_reply auto-reply mechanism Once agent receives message automatically invokes generate_reply sends reply back unless termination condition satisfied built-in reply functions LLM inference code function execution human input custom reply functions chatting with another agent before replying to sender decentralized modular unified way define workflow For dynamic flows: Customized generate_reply function within customized generate_reply one agent can hold current conversation while invoking conversations with other agents depending content current message and context; Function calls LLM decides whether or not to call particular function depending conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation; GroupChatManager dynamically selects next speaker broadcasts response to other agents. For safety, Commander checks code safety with Safeguard if cleared executes Python request Writer interpret execution results total cost increase 10.5% If exception security red flag Safeguard Commander redirects issue back to Writer debugging repeated until answered or timed-out.
10. **Construction rule:** any scientific agent = mix-and-match planner (P1-P6 L1-L2) + memory (M1-M5) + action (A1-A5) + verifier (V1-V4) — use cathode-design example as recipe book: Battery Schema → Augmented with historical failures + KB thresholds → Reflective revision cycles → Search-based max reward path → Role-interactive debate consensus → Programmatic DSL pipeline executable artifact. For long-form grounded writing STORM = Perspective Discovery Related Topics TOCs → Perspectives P=[P0]+P[:N] → Simulated Conversations M rounds question queries search sift answer → Draft OD internal knowledge + Refine O with convos → Section generation Sentence-BERT retrieval from R + citations + polish + lead. For autonomous cooperation CAMEL = Idea Develop trading bot → Role Assignment AI Assistant Python Programmer AI User Stock Trader → Human Input → Task Specifier → Specified Task with sentiment analysis tool → PA PU system messages A<-F_PA U<-F_PU → M_t={(I0,S0)...} Instruction Input Solution Next request loop It St until termination task completed or max messages limit cost quadratic → Role flipping repeating instructions flake replies infinite loop mitigation inception prompting → Data Generation AI Society Assistant Role Generation list NUM_ROLES diverse roles alphabetical no explanation User Role Generation list NUM_ROLES most common diverse groups internet users occupations singular alphabetical Task Generation List NUM_TASKS diverse tasks ASSISTANT_ROLE can assist USER_ROLE cooperatively Be concise Be creative → AI Society dataset large conversational task-oriented instruction-following + Code + Math Science topics subtopics problems automatically prompting LLMs + Misalignment malicious applications risks → Agent Evaluation 100 tasks AI Society +100 Code random select GPT4 summarization consolidated final solution larger token limit undetectable format fair comparison vs single-shot gpt-3.5-turbo Human Evaluation side-by-side anonymous vote superior equally good 453 responses AI Society only GPT4 Evaluation score decide which better Model1 vs Model2 Results CAMEL outperforms single-shot → Knowledge emergence fine-tuning LLaMA progressively growing datasets HumanEval HumanEval+ benchmarking.
 For AutoGen = ConversableAgent highest-level abstraction by default can use LLMs humans tools maintains internal context based on sent and received messages capabilities LLM human tool + AssistantAgent pre-configured ConversableAgent LLM-backed assistant human_input_mode NEVER code_execution_config False DEFAULT_SYSTEM_MESSAGE helpful AI assistant suggest python code natural-language control fix errors generate code again confine output structures TERMINATE + UserProxyAgent human proxy solicit human input or execute code/function calls backed humans tools human_input_mode ALWAYS group_chat + GroupChatManager human_input_mode NEVER group_chat dynamically select next speaker broadcast response + Conversation Initiation A.initiate_chat Plot chart META TESLA stock price change YTD B + Custom Reply A.register_reply B reply_func_A2B def reply_func_A2B msg output input_from_human if not output if msg includes code output execute msg return output + Unified Interfaces send receive generate_reply + Auto-reply mechanism Once agent receives message automatically invokes generate_reply sends reply back unless termination condition satisfied built-in reply functions LLM inference code function execution human input custom reply functions chatting with another agent before replying to sender decentralized modular unified way define workflow + Program Execution Plot chart META TESLA stock price change YTD Execute following code send receive receive Conversation-Centric Computation generate_reply Error package yfinance not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat + Conversation Programming paradigm computation actions agents take compute response multi-agent conversation + control flow sequence conditions under which computations happen conversation-centric computation actions result in message passing unless termination satisfied conversation-driven control flow decisions which agents send messages to and procedure functions of inter-agent conversation + Control by fusion programming and natural language Natural-language control via LLMs fix errors generate code again confine output structures TERMINATE Appendix C Programming-language control Python code specify termination condition human input mode tool execution logic e.g. max number auto replies register programmed auto-reply functions Conversation-Driven Control Flow Control transition code to natural-language invoking LLM inference containing certain control logic customized reply function natural language to code via LLM-proposed function calls + Dynamic conversation flows Customized generate_reply function within customized generate_reply one agent can hold current conversation while invoking conversations with other agents depending content current message and context + Function calls LLM decides whether or not to call particular function depending conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation + GroupChatManager dynamically select next speaker broadcast response + Applications A1 Math 120 Level-5 problems Whole Dataset Success Ratio 69.48% vs ChatGPT+Code etc out-of-box competitive math problem solving + A2 Retrieval-Augmented Chat RAG Retrieval-augmented User Proxy includes vector database Chroma SentenceTransformers context retriever Retrieval-augmented Assistant extended built-in agents Natural Questions dataset Kwiatkowski vs DPR Adlakha novel interactive retrieval feature Sorry I cannot find any information about... UPDATE CONTEXT vs I don't know ablation + A3 ALFWorld 134 unseen tasks Two-agent assistant suggesting plans executor executing actions ReAct prompting occasional inability leverage commonsense knowledge physical world stuck loop repetitive errors Grounding agent supplies crucial commonsense knowledge You must find and take object before you can examine it You must go to where target object is before you can use it whenever early signs recurring errors 15% performance gain average + A4 OptiGuide Multi-Agent Coding Commander coordinates Writer and Safeguard What if we prohibit shipping from supplier 1 to roastery 2 Writer crafts code Commander checks safety with Safeguard if cleared executes Python request Writer interpret execution results total cost increase 10.5% Commander provides concluding answer If exception security red flag Safeguard Commander redirects issue back to Writer debugging repeated until answered or timed-out core workflow reduced 430 lines to 100 lines save 3x time reduce interactions 3-5 times
11. **Retrieval rule:** multi-granularity retrieval leveraging keywords semantic embeddings citation relations thorough exhaustive SE CC CL — encode quintuple components individually preprocessed into vectors vs entire sections multifaceted difficult capture key points effective encoding quality retrieval performance impact. Recall10-50 metrics: AI Scientist Not Applicable SCIMON-like 0.381 ResearchAgent-like 0.377 SciPIP Ours 0.419 more thorough. Non-matching ideas more valuable novel ideas not appear human. For STORM, retrieve relevant docs from R based semantic similarity Sentence-BERT embeddings for section generation. For AutoGen RAG, Retrieval-augmented User Proxy includes vector database Chroma SentenceTransformers context retriever interactive retrieval Sorry I cannot find any information about... UPDATE CONTEXT vs I don't know ablation.
12. **Novelty rule:** iterative novelty boosting compare Idea_t with prior literature {(Background_i, idea_i)} if strongly overlapping update more novel relative prior work like good researcher until sufficient novelty achieved. In-context contrastive CL SN KG CT T5+CL etc helps better baseline reducing reliance copying Table9 R-L BERT. Avoid generic suggestions woven specifics copied directly context Data preprocessing Clean text remove unnecessary characters tokenization etc simple logical modifications high latency→low latency. For CAMEL, avoid generic suggestions woven specifics copied directly context etc reduce copying rephrasing directly from context simple logical modifications high latency→low latency efficiency limitations→highly efficient.
13. **Grounded writing rule:** STORM perspective-guided question asking: direct prompting Ask 30 questions yields When was opening held Where how many countries basic What When Where limited planning capacity, perspective-guided You are event planner focusing preparation opening ceremony leads varied questions transportation arrangements budget cultural broadcasting security, conversational Can you provide list participating countries ... over 90 countries entering stadium specific order How is order determined transportation arrangements budget elicits follow-up in-depth iterative research grounded Internet. For CAMEL, perspective-guided via different roles diverse fields alphabetical order diverse groups internet users occupations singular alphabetical diverse tasks concise creative.
14. **Collaboration rule:** For autonomous cooperation minimal human supervision only preliminary idea needed from human to guide conversations toward complex task-solving, use CAMEL Task Specifier making specific well-defined prompting LLM instead of relying human inputs + Role Assignment PA PU A<-F_PA U<-F_PU M_t={(I0,S0)...} Instruction Input Solution Next request loop It St until termination task completed or max messages limit cost quadratic. For conversable agents, use AutoGen ConversableAgent send/receive/generate_reply unified interfaces auto-reply mechanism decentralized modular unified workflow + AssistantAgent NEVER DEFAULT_SYSTEM_MESSAGE helpful AI assistant suggest python code TERMINATE + UserProxy ALWAYS + GroupChatManager dynamically select next speaker broadcast + Initiate chat A.initiate_chat + Custom reply A.register_reply + Program Execution dialog box Error package yfinance not installed Sorry please pip install + Conversation Programming computation + control flow conversation-centric computation message passing unless termination conversation-driven control flow decisions which agents send messages procedure functions inter-agent + Control fusion natural-language control fix errors generate code again confine structures TERMINATE Appendix C programming-language control max number auto replies register programmed auto-reply functions Conversation-Driven Control Flow transition code ↔ natural invoking LLM inference or LLM-proposed function calls + Dynamic flows customized generate_reply hold current conversation while invoking conversations with other agents depending content + Function calls LLM decides whether to call particular function + GroupChatManager dynamic speaker selection broadcast + Applications Math RAG ALFWorld OptiGuide.
15. **This constitution is a control layer**, not substitute domain expertise, licenses, ethics review. For scientific agents ethics and reproducibility are design imperatives embedded architecture verification modules per Survey Sec5 not peripheral concerns. Ethics checklist + reproducibility protocol mandatory. For communicative agents AI Society, consider alignment risks Misalignment dataset simulation malicious applications demonstrate potential risks unaligned autonomous agent system. For STORM, FreshWiki dataset creation avoiding leakage top 100 most-edited per month Feb2022-Sep2023 filter B-class ORES exclude list no subsections plain text only process repeated future dates new LLMs emerge. Heading soft recall paraphrase-MiniLM-L6-v2 cosine + entity recall FLAIR NER + Prometheus 13B Interest Coherence Organization Relevance Focus Coverage trimmed 2000 words iterative removing shortest section. For AutoGen, safety via Safeguard checks code safety with Safeguard if cleared executes Python, if exception security red flag redirect back to Writer debugging, core workflow reduced 430→100 lines save 3x time.

---

*Maintained with the ARSENAL unified master pipeline.*  
*Repo: https://github.com/faresrafat3/arsenal-unified-master-pipeline*  
*Updated 2026-07-12 with GAPMAP + ResearchAgent + Scientific Intelligence Survey + STORM + SciMON/SciPIP + CAMEL + AutoGen extractions — Part 6 HOW TO TRACK KNOWLEDGE expanded to 15 systems + Part 7 HOW TO COLLABORATE (multi-agent patterns) 2 systems = 17 total*
