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
