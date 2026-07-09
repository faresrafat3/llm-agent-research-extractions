# AI Scientist v2 — Complete Prompts in Execution Order

## Repository Python file map

- `ai_scientist/__init__.py`
- `ai_scientist/ideas/i_cant_believe_its_not_better.py`
- `ai_scientist/ideas/i_cant_believe_its_not_betterrealworld.py`
- `ai_scientist/llm.py`
- `ai_scientist/perform_icbinb_writeup.py`
- `ai_scientist/perform_ideation_temp_free.py`
- `ai_scientist/perform_llm_review.py`
- `ai_scientist/perform_plotting.py`
- `ai_scientist/perform_vlm_review.py`
- `ai_scientist/perform_writeup.py`
- `ai_scientist/tools/__init__.py`
- `ai_scientist/tools/base_tool.py`
- `ai_scientist/tools/semantic_scholar.py`
- `ai_scientist/treesearch/__init__.py`
- `ai_scientist/treesearch/agent_manager.py`
- `ai_scientist/treesearch/backend/__init__.py`
- `ai_scientist/treesearch/backend/backend_anthropic.py`
- `ai_scientist/treesearch/backend/backend_openai.py`
- `ai_scientist/treesearch/backend/utils.py`
- `ai_scientist/treesearch/bfts_utils.py`
- `ai_scientist/treesearch/interpreter.py`
- `ai_scientist/treesearch/journal.py`
- `ai_scientist/treesearch/journal2report.py`
- `ai_scientist/treesearch/log_summarization.py`
- `ai_scientist/treesearch/parallel_agent.py`
- `ai_scientist/treesearch/perform_experiments_bfts_with_agentmanager.py`
- `ai_scientist/treesearch/utils/__init__.py`
- `ai_scientist/treesearch/utils/config.py`
- `ai_scientist/treesearch/utils/data_preview.py`
- `ai_scientist/treesearch/utils/metric.py`
- `ai_scientist/treesearch/utils/response.py`
- `ai_scientist/treesearch/utils/serialize.py`
- `ai_scientist/treesearch/utils/tree_export.py`
- `ai_scientist/utils/token_tracker.py`
- `ai_scientist/vlm.py`
- `launch_scientist_bfts.py`

## Python files identified as containing prompt strings / instruction schemas

- `ai_scientist/llm.py`
- `ai_scientist/perform_icbinb_writeup.py`
- `ai_scientist/perform_ideation_temp_free.py`
- `ai_scientist/perform_llm_review.py`
- `ai_scientist/perform_plotting.py`
- `ai_scientist/perform_vlm_review.py`
- `ai_scientist/perform_writeup.py`
- `ai_scientist/tools/semantic_scholar.py`
- `ai_scientist/treesearch/agent_manager.py`
- `ai_scientist/treesearch/backend/__init__.py`
- `ai_scientist/treesearch/backend/backend_anthropic.py`
- `ai_scientist/treesearch/backend/backend_openai.py`
- `ai_scientist/treesearch/backend/utils.py`
- `ai_scientist/treesearch/bfts_utils.py`
- `ai_scientist/treesearch/journal.py`
- `ai_scientist/treesearch/journal2report.py`
- `ai_scientist/treesearch/log_summarization.py`
- `ai_scientist/treesearch/parallel_agent.py`
- `ai_scientist/treesearch/perform_experiments_bfts_with_agentmanager.py`
- `ai_scientist/utils/token_tracker.py`
- `ai_scientist/vlm.py`

> Note: for f-strings and runtime-built dict prompts, this document preserves the repository source template/expression so placeholders and dynamic fields remain visible. Dict/list prompts are sent after `compile_prompt_to_md`, which renders dict keys as Markdown headers and list items as bullets.

## External-source audit added after web search

I cross-checked this repository extraction against external project sources, especially the official paper / prompt appendix and README-linked documentation. The official paper is **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (`arXiv:2504.08066`) and its supplementary material contains a **Prompts** appendix. The README also links the paper, blog post, and ICLR 2025 workshop experiment repository.

**Result of the audit:**

- The paper appendix confirms the main phases represented here: ideation, experiment prompt, plot aggregation, ICBINB writeup, writeup reflection, VLM reflection, and VLM image review.
- The paper appendix is useful as an external checklist, but it is not a replacement for repository extraction: PDF text is line-wrapped, sometimes abbreviated with ellipses, and in places reflects the ICBINB/workshop-specific writeup variant rather than every current code path in the repo.
- The repository code is the source of truth for exact prompt strings. This file therefore preserves the exact source templates from the cloned repository wherever possible, including f-string/dict prompt expressions and FunctionSpec schemas that may not appear fully in the paper appendix.
- Additional prompt-bearing files beyond the user's initial shortlist were included, notably BFTS/agent-manager schemas, node selection/evaluation prompts, summarization prompts, journal-to-report prompts, review/meta-review prompts, and VLM duplicate-image prompts.

**External sources checked:**

- Official arXiv / paper PDF: `https://arxiv.org/abs/2504.08066` and `https://arxiv.org/pdf/2504.08066`
- Official project README / repository documentation: `https://github.com/SakanaAI/AI-Scientist-v2/blob/main/README.md`
- Official ICLR 2025 workshop experiment repository linked by the README: `https://github.com/SakanaAI/AI-Scientist-ICLR2025-Workshop-Experiment`


---

## Prompt 1: Ideation system prompt

**File:** `ai_scientist/perform_ideation_temp_free.py`  

**Variable:** `system_prompt`  

**Execution:** Loop context: supplied as system_message on every ideation LLM call; runs for each call in proposal/reflection loops.  

**Transition to next:** Next user prompt is idea_generation_prompt for reflection_round == 0.  

**Placeholders / dynamic fills:**  

- `{tool_descriptions}`: filled at runtime from the variable/expression named `tool_descriptions` (or, for f-string expressions, the expression shown).

- `{tool_names_str}`: filled at runtime from the variable/expression named `tool_names_str` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""You are an experienced AI researcher who aims to propose high-impact research ideas resembling exciting grant proposals. Feel free to propose any novel ideas or experiments; make sure they are novel. Be very creative and think out of the box. Each proposal should stem from a simple and elegant question, observation, or hypothesis about the topic. For example, they could involve very interesting and simple interventions or investigations that explore new possibilities or challenge existing assumptions. Clearly clarify how the proposal distinguishes from the existing literature.

Ensure that the proposal does not require resources beyond what an academic lab could afford. These proposals should lead to papers that are publishable at top ML conferences.

You have access to the following tools:

{tool_descriptions}

Respond in the following format:

ACTION:
<The action to take, exactly one of {tool_names_str}>

ARGUMENTS:
<If ACTION is "SearchSemanticScholar", provide the search query as {{"query": "your search query"}}. If ACTION is "FinalizeIdea", provide the idea details as {{"idea": {{ ... }}}} with the IDEA JSON specified below.>

If you choose to finalize your idea, provide the IDEA JSON in the arguments:

IDEA JSON:
```json
{{
  "idea": {{
    "Name": "...",
    "Title": "...",
    "Short Hypothesis": "...",
    "Related Work": "...",
    "Abstract": "...",
    "Experiments": "...",
    "Risk Factors and Limitations": "..."
  }}
}}
```

Ensure the JSON is properly formatted for automatic parsing.

Note: You should perform at least one literature search before finalizing your idea to ensure it is well-informed by existing research."""
````

---

## Prompt 2: Initial idea generation prompt

**File:** `ai_scientist/perform_ideation_temp_free.py`  

**Variable:** `idea_generation_prompt`  

**Execution:** Loop: first round of each generated proposal; outer loop range(max_num_generations), inner reflection_round == 0.  

**Transition to next:** LLM returns ACTION. If SearchSemanticScholar, tool result is saved and next prompt is idea_reflection_prompt. If FinalizeIdea, proposal loop ends and next proposal starts.  

**Placeholders / dynamic fills:**  

- `{prev_ideas_string}`: filled at runtime from the variable/expression named `prev_ideas_string` (or, for f-string expressions, the expression shown).

- `{workshop_description}`: filled at runtime from the variable/expression named `workshop_description` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""{workshop_description}

Here are the proposals that you have already generated:

'''
{prev_ideas_string}
'''

Begin by generating an interestingly new high-level research proposal that differs from what you have previously proposed.
"""
````

---

## Prompt 3: Idea reflection prompt

**File:** `ai_scientist/perform_ideation_temp_free.py`  

**Variable:** `idea_reflection_prompt`  

**Execution:** Loop: subsequent reflection rounds for each proposal; reflection_round in 1..num_reflections-1 unless idea_finalized or parse error breaks.  

**Transition to next:** If ACTION is SearchSemanticScholar, loop continues with updated last_tool_results. If ACTION is FinalizeIdea, current proposal ends. If max reflections exhausted, next proposal starts.  

**Placeholders / dynamic fills:**  

- `{current_round}`: filled at runtime from the variable/expression named `current_round` (or, for f-string expressions, the expression shown).

- `{last_tool_results}`: filled at runtime from the variable/expression named `last_tool_results` (or, for f-string expressions, the expression shown).

- `{num_reflections}`: filled at runtime from the variable/expression named `num_reflections` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""Round {current_round}/{num_reflections}.

In your thoughts, first carefully consider the quality, novelty, and feasibility of the proposal you just created.
Include any other factors that you think are important in evaluating the proposal.
Ensure the proposal is clear and concise, and the JSON is in the correct format.
Do not make things overly complicated.
In the next attempt, try to refine and improve your proposal.
Stick to the spirit of the original idea unless there are glaring issues.

If you have new information from tools, such as literature search results, incorporate them into your reflection and refine your proposal accordingly.

Results from your last action (if any):

{last_tool_results}
"""
````

---

## Prompt 4: Experiment introduction / initial draft prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._draft prompt`  

**Execution:** Loop: called to create draft nodes in the current stage (initial implementation and as configured); retries inside plan_and_code_query up to 3 on parse failure.  

**Transition to next:** Generated code is executed; then parse_exec_result evaluates output. If buggy, transition to debug prompt; otherwise to improvement/refinement or stage completion check.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an AI researcher who is looking to publish a paper that will contribute significantly to the field."
                "Your first task is to write a python code to implement a solid baseline based on your research idea provided below, "
                "from data preparation to model training, as well as evaluation and visualization. "
                "Focus on getting a simple but working implementation first, before any sophisticated improvements. "
                "We will explore more advanced variations in later stages."
            ),
            "Research idea": self.task_desc,
            "Memory": self.memory_summary if self.memory_summary else "",
            "Instructions": {},
        }
````

---

## Prompt 5: Debug prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._debug prompt`  

**Execution:** Loop: called when parent_node is buggy; plan_and_code_query retries up to 3 on code/plan parse failure. Tree search continues until stage max_iterations or stage-completion criteria.  

**Transition to next:** Generated bugfix code becomes a child node and is executed; then parse_exec_result / plotting / evaluation run.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an experienced AI researcher. Your previous code for research experiment had a bug, so based on the information below, you should revise it in order to fix this bug. "
                "Your response should be an implementation outline in natural language,"
                " followed by a single markdown code block which implements the bugfix/solution."
            ),
            "Research idea": self.task_desc,
            "Previous (buggy) implementation": wrap_code(parent_node.code),
            "Execution output": wrap_code(parent_node.term_out, lang=""),
            "Feedback based on generated plots": parent_node.vlm_feedback_summary,
            "Feedback about execution time": parent_node.exec_time_feedback,
            "Instructions": {},
        }
````

---

## Prompt 6: Refinement/improvement prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._improve prompt`  

**Execution:** Loop: called to improve a non-buggy parent node during tree search; repeated until stage max_iterations or stage completion. plan_and_code_query retries up to 3 on parse failure.  

**Transition to next:** Generated refined implementation is executed; then node evaluation/parsing and plotting/VLM feedback occur.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an experienced AI researcher. You are provided with a previously developed "
                "implementation. Your task is to improve it based on the current experimental stage."
            ),
            "Research idea": self.task_desc,
            "Memory": self.memory_summary if self.memory_summary else "",
            "Feedback based on generated plots": parent_node.vlm_feedback_summary,
            "Feedback about execution time": parent_node.exec_time_feedback,
            "Instructions": {},
        }
````

---

## Prompt 7: Node execution evaluation prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent.parse_exec_result prompt`  

**Execution:** Loop: once per executed node.  

**Transition to next:** If response marks is_bug true or execution exception exists, node.is_buggy is set and debug path may be chosen; otherwise metrics/plotting and selection/stage checks follow.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an experienced AI researcher. "
                "You have written code for your research experiment and now need to evaluate the output of the code execution. "
                "Analyze the execution output, determine if there were any bugs, and provide a summary of the findings. "
            ),
            "Research idea": self.task_desc,
            "Implementation": wrap_code(node.code),
            "Execution output": wrap_code(node.term_out, lang=""),
        }
````

---

## Prompt 8: Stage completion schema prompt / function schema

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `stage_completion_eval_spec`  

**Execution:** Loop: used by _check_substage_completion and _check_stage_completion (stage 2) whenever checking completion; returns structured JSON.  

**Transition to next:** If is_complete true, transition to next stage; if false, continue current stage until max_iterations or completion.  

**Placeholders / dynamic fills:**  

- `{"type": "string"}`: filled at runtime from the variable/expression named `"type": "string"` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
stage_completion_eval_spec = FunctionSpec(
    name="evaluate_stage_completion",
    description="Evaluate if the current stage is complete",
    json_schema={
        "type": "object",
        "properties": {
            "is_complete": {
                "type": "boolean",
                "description": "Whether the current stage is complete",
            },
            "reasoning": {
                "type": "string",
                "description": "Detailed reasoning for the decision",
            },
            "missing_criteria": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of criteria still needed",
            },
        },
        "required": ["is_complete", "reasoning", "missing_criteria"],
    },
)
````

---

## Prompt 9: Sub-stage completion evaluation prompt

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager._check_substage_completion eval_prompt`  

**Execution:** Loop: called after sub-stage iterations while running staged experiment; stops substage when evaluation.is_complete true or max_iterations reached.  

**Transition to next:** Completion transitions to main stage progression/next sub-stage; incompletion continues generating nodes.  

**Placeholders / dynamic fills:**  

- `{current_substage.goals}`: filled at runtime from the variable/expression named `current_substage.goals` (or, for f-string expressions, the expression shown).

- `{vlm_feedback}`: filled at runtime from the variable/expression named `vlm_feedback` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""
        Evaluate if the current sub-stage is complete based on the following evidence:
        1. Figure Analysis:
        {vlm_feedback}

        Requirements for completion:
        - {current_substage.goals}

        Provide a detailed evaluation of completion status.
        """
````

---

## Prompt 10: Stage 2 completion evaluation prompt

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager._check_stage_completion eval_prompt (stage_number == 2)`  

**Execution:** Loop: checked during stage 2 after nodes; stops when function response is_complete true or max_iterations reached.  

**Transition to next:** If complete, transition to next stage; otherwise continue baseline tuning.  

**Placeholders / dynamic fills:**  

- `{best_node.datasets_successfully_tested}`: filled at runtime from the variable/expression named `best_node.datasets_successfully_tested` (or, for f-string expressions, the expression shown).

- `{vlm_feedback}`: filled at runtime from the variable/expression named `vlm_feedback` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""
            Evaluate if stage 2 (baseline tuning) is complete based on the following evidence:

            1. Figure Analysis:
            {vlm_feedback}

            2. Datasets Tested: {best_node.datasets_successfully_tested}

            Requirements for completion:
            1. Training curves should show stable convergence
            2. Results should be tested on at least two datasets
            3. No major instabilities or issues in the plots

            Provide a detailed evaluation of completion status.
            """
````

---

## Prompt 11: Focused sub-stage goals prompt

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager._generate_substage_goal prompt`  

**Execution:** Loop: generated when configuring next sub-stage.  

**Transition to next:** Returned sub-stage goals create the next Stage object and guide subsequent draft/debug/improve prompts.  

**Placeholders / dynamic fills:**  

- `{json.dumps(issues, indent=2)}`: filled at runtime from the variable/expression named `json.dumps(issues, indent=2)` (or, for f-string expressions, the expression shown).

- `{json.dumps(progress['recent_changes'], indent=2)}`: filled at runtime from the variable/expression named `json.dumps(progress['recent_changes'], indent=2)` (or, for f-string expressions, the expression shown).

- `{main_stage_goal}`: filled at runtime from the variable/expression named `main_stage_goal` (or, for f-string expressions, the expression shown).

- `{metrics['best_metric']['value'] if metrics['best_metric'] else 'N/A'}`: filled at runtime from the variable/expression named `metrics['best_metric']['value'] if metrics['best_metric'] else 'N/A'` (or, for f-string expressions, the expression shown).

- `{metrics['good_nodes']}`: filled at runtime from the variable/expression named `metrics['good_nodes']` (or, for f-string expressions, the expression shown).

- `{metrics['total_nodes']}`: filled at runtime from the variable/expression named `metrics['total_nodes']` (or, for f-string expressions, the expression shown).

- `{progress['convergence_status']}`: filled at runtime from the variable/expression named `progress['convergence_status']` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""
        Based on the current experimental progress, generate focused goals for the next sub-stage.

        Main Stage Goals:
        {main_stage_goal}

        Current Progress:
        - Total attempts: {metrics['total_nodes']}
        - Successful implementations: {metrics['good_nodes']}
        - Best performance: {metrics['best_metric']['value'] if metrics['best_metric'] else 'N/A'}
        - Convergence status: {progress['convergence_status']}

        Current Issues:
        {json.dumps(issues, indent=2)}

        Recent Changes:
        {json.dumps(progress['recent_changes'], indent=2)}

        Generate specific, actionable sub-stage goals that:
        1. Address current issues and limitations
        2. Build on recent progress
        3. Move towards main stage goals
        4. Are concrete and measurable
        """
````

---

## Prompt 12: Stage progression evaluation prompt

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager._evaluate_stage_progression eval_prompt`  

**Execution:** Loop: after a stage/substage summary when considering progression.  

**Transition to next:** If ready_for_next_stage true, manager configures/runs next stage; else recommendations focus continued work.  

**Placeholders / dynamic fills:**  

- `{', '.join(current_stage.goals) if isinstance(current_stage.goals, list) else current_stage.goals}`: filled at runtime from the variable/expression named `', '.join(current_stage.goals) if isinstance(current_stage.goals, list) else current_stage.goals` (or, for f-string expressions, the expression shown).

- `{current_stage.description}`: filled at runtime from the variable/expression named `current_stage.description` (or, for f-string expressions, the expression shown).

- `{current_stage.name}`: filled at runtime from the variable/expression named `current_stage.name` (or, for f-string expressions, the expression shown).

- `{json.dumps(previous_results.get('issues', []), indent=2)}`: filled at runtime from the variable/expression named `json.dumps(previous_results.get('issues', []), indent=2)` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""
        Evaluate whether the current experimental stage should progress to the next stage.
        Consider all available evidence holistically:

        Current Stage Information:
        - Name: {current_stage.name}
        - Description: {current_stage.description}
        - Goals: {', '.join(current_stage.goals) if isinstance(current_stage.goals, list) else current_stage.goals}

        Performance Metrics:
        {json.dumps(previous_results.get('metrics', {}), indent=2)}

        Identified Issues:
        {json.dumps(previous_results.get('issues', []), indent=2)}

        Progress Analysis:
        {json.dumps(previous_results.get('progress', {}), indent=2)}

        Expected Stage Progression:
        1. Initial Implementation: Focus on basic working implementation
        2. Baseline Tuning: Systematic optimization of core parameters
        3. Creative Research: Novel improvements and approaches
        4. Ablation Studies: Systematic component analysis

        Consider factors like:
        - Progress toward stage goals
        - Performance trends and stability
        - Quality and reliability of results
        - Understanding of the problem
        - Presence of systematic issues
        - Convergence indicators
        - Readiness for next stage challenges

        Provide a holistic evaluation of whether the experiment should:
        1. Progress to next stage
        2. Continue current stage with specific focus
        3. Extend current stage with modifications
        """
````

---

## Prompt 13: Best-node selection/evaluation prompt

**File:** `ai_scientist/treesearch/journal.py`  

**Variable:** `Journal.get_best_node prompt`  

**Execution:** Loop: called when selecting best implementation among candidate nodes.  

**Transition to next:** Selected node is used for next stage, report summaries, or as parent for refinements.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an experienced AI researcher evaluating different implementations "
                "of an experiment to select the best one. You should consider all aspects "
                "including performance metrics, training dynamics, generated plots quality."
            ),
            "Task": (
                "Select the best implementation from the candidates below, considering all available evidence."
                "Avoid relying too heavily on the validation loss alone, because "
                "it may not be directly comparable across different objective functions or training details. "
                "If there are multiple validation losses (e.g., when evaluating multiple datasets), "
                "consider all of them and select the implementation that performs best overall."
            ),
            "Candidates": "",
        }
````

---

## Prompt 14: Plot aggregation system prompt

**File:** `ai_scientist/perform_plotting.py`  

**Variable:** `AGGREGATOR_SYSTEM_MSG`  

**Execution:** Once for initial aggregation; reused as system message in each reflection iteration.  

**Transition to next:** Next prompt is build_aggregator_prompt user prompt.  

**Placeholders / dynamic fills:**  

- `{MAX_FIGURES}`: filled at runtime from the variable/expression named `MAX_FIGURES` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""You are an ambitious AI researcher who is preparing final plots for a scientific paper submission.
You have multiple experiment summaries (baseline, research, ablation), each possibly containing references to different plots or numerical insights.
There is also a top-level 'research_idea.md' file that outlines the overarching research direction.
Your job is to produce ONE Python script that fully aggregates and visualizes the final results for a comprehensive research paper.

Key points:
1) Combine or replicate relevant existing plotting code, referencing how data was originally generated (from code references) to ensure correctness.
2) Create a complete set of final scientific plots, stored in 'figures/' only (since only those are used in the final paper).
3) Make sure to use existing .npy data for analysis; do NOT hallucinate data. If single numeric results are needed, these may be copied from the JSON summaries.
4) Only create plots where the data is best presented as a figure and not as a table. E.g. don't use bar plots if the data is hard to visually compare.
5) The final aggregator script must be in triple backticks and stand alone so it can be dropped into a codebase and run.
6) If there are plots based on synthetic data, include them in the appendix.

Implement best practices:
- Do not produce extraneous or irrelevant plots.
- Maintain clarity, minimal but sufficient code.
- Demonstrate thoroughness for a final research paper submission.
- Do NOT reference non-existent files or images.
- Use the .npy files to get data for the plots and key numbers from the JSON summaries.
- Demarcate each individual plot, and put them in separate try-catch blocks so that the failure of one plot does not affect the others.
- Make sure to only create plots that are unique and needed for the final paper and appendix. A good number could be around {MAX_FIGURES} plots in total.
- Aim to aggregate multiple figures into one plot if suitable, i.e. if they are all related to the same topic. You can place up to 3 plots in one row.
- Provide well-labeled plots (axes, legends, titles) that highlight main findings. Use informative names everywhere, including in the legend for referencing them in the final paper. Make sure the legend is always visible.
- Make the plots look professional (if applicable, no top and right spines, dpi of 300, adequate ylim, etc.).
- Do not use labels with underscores, e.g. "loss_vs_epoch" should be "loss vs epoch".
- For image examples, select a few categories/classes to showcase the diversity of results instead of showing a single category/class. Some can be included in the main paper, while the rest can go in the appendix.

Your output should be the entire Python aggregator script in triple backticks.
"""
````

---

## Prompt 15: Plot aggregator prompt

**File:** `ai_scientist/perform_plotting.py`  

**Variable:** `build_aggregator_prompt return f-string`  

**Execution:** Once before running auto_plot_aggregator.py.  

**Transition to next:** LLM script is extracted and executed; then reflection loop begins.  

**Placeholders / dynamic fills:**  

- `{combined_summaries_str}`: filled at runtime from the variable/expression named `combined_summaries_str` (or, for f-string expressions, the expression shown).

- `{idea_text}`: filled at runtime from the variable/expression named `idea_text` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""
We have three JSON summaries of scientific experiments: baseline, research, ablation.
They may contain lists of figure descriptions, code to generate the figures, and paths to the .npy files containing the numerical results.
Our goal is to produce final, publishable figures.

--- RESEARCH IDEA ---
```
{idea_text}
```

IMPORTANT:
- The aggregator script must load existing .npy experiment data from the "exp_results_npy_files" fields (ONLY using full and exact file paths in the summary JSONs) for thorough plotting.
- It should call os.makedirs("figures", exist_ok=True) before saving any plots.
- Aim for a balance of empirical results, ablations, and diverse, informative visuals in 'figures/' that comprehensively showcase the finalized research outcomes.
- If you need .npy paths from the summary, only copy those paths directly (rather than copying and parsing the entire summary).

Your generated Python script must:
1) Load or refer to relevant data and .npy files from these summaries. Use the full and exact file paths in the summary JSONs.
2) Synthesize or directly create final, scientifically meaningful plots for a final research paper (comprehensive and complete), referencing the original code if needed to see how the data was generated.
3) Carefully combine or replicate relevant existing plotting code to produce these final aggregated plots in 'figures/' only, since only those are used in the final paper.
4) Do not hallucinate data. Data must either be loaded from .npy files or copied from the JSON summaries.
5) The aggregator script must be fully self-contained, and place the final plots in 'figures/'.
6) This aggregator script should produce a comprehensive and final set of scientific plots for the final paper, reflecting all major findings from the experiment data.
7) Make sure that every plot is unique and not duplicated from the original plots. Delete any duplicate plots if necessary.
8) Each figure can have up to 3 subplots using fig, ax = plt.subplots(1, 3).
9) Use a font size larger than the default for plot labels and titles to ensure they are readable in the final PDF paper.


Below are the summaries in JSON:

{combined_summaries_str}

Respond with a Python script in triple backticks.
"""
````

---

## Prompt 16: Plot aggregator reflection prompt

**File:** `ai_scientist/perform_plotting.py`  

**Variable:** `aggregate_plots reflection_prompt`  

**Execution:** Loop: for i in range(n_reflections); exits early only if figure_count > 0 and response contains "I am done".  

**Transition to next:** If new code differs, script is rerun; otherwise loop proceeds/ends after n_reflections.  

**Placeholders / dynamic fills:**  

- `{MAX_FIGURES}`: filled at runtime from the variable/expression named `MAX_FIGURES` (or, for f-string expressions, the expression shown).

- `{aggregator_out}`: filled at runtime from the variable/expression named `aggregator_out` (or, for f-string expressions, the expression shown).

- `{figure_count}`: filled at runtime from the variable/expression named `figure_count` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""We have run your aggregator script and it produced {figure_count} figure(s). The script's output is:
```
{aggregator_out}
```

Please criticize the current script for any flaws including but not limited to:
- Are these enough plots for a final paper submission? Don't create more than {MAX_FIGURES} plots.
- Have you made sure to both use key numbers and generate more detailed plots from .npy files?
- Does the figure title and legend have informative and descriptive names? These plots are the final versions, ensure there are no comments or other notes.
- Can you aggregate multiple plots into one figure if suitable?
- Do the labels have underscores? If so, replace them with spaces.
- Make sure that every plot is unique and not duplicated from the original plots.

If you believe you are done, simply say: "I am done". Otherwise, please provide an updated aggregator script in triple backticks."""
````

---

## Prompt 17: Citation gathering system prompt

**File:** `ai_scientist/perform_writeup.py`  

**Variable:** `get_citation_addition citation_system_msg_template`  

**Execution:** Loop: each citation round; used as system_message for both Semantic Scholar query-picking and paper-selection calls.  

**Transition to next:** Next prompt is citation_first_prompt_template.  

**Placeholders / dynamic fills:**  

- `{total_rounds}`: filled at runtime from the variable/expression named `total_rounds` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""You are an ambitious AI researcher who is looking to publish a paper to a top-tier ML conference that will contribute significantly to the field.
You have already completed the experiments and now you are looking to collect citations to related papers.
This phase focuses on collecting references and annotating them to be integrated later.
Collected citations will be added to a references.bib file.

Reasons to reference papers include:
1. Summarizing Research: Cite sources when summarizing the existing literature.
2. Using Specific Concepts or Data: Provide citations when discussing specific theories, models, or data.
3. Comparing Findings: Cite relevant studies when comparing or contrasting different findings.
4. Highlighting Research Gaps: Cite previous research when pointing out gaps your survey addresses.
5. Using Established Methods: Cite the creators of methodologies you employ in your survey.
6. Supporting Arguments: Cite sources that back up your conclusions and arguments.
7. Suggesting Future Research: Reference studies related to proposed future research directions.

Ensure sufficient cites will be collected for all of these categories, and no categories are missed.
You will be given access to the Semantic Scholar API; only add citations that you have found using the API.
Aim to discuss a broad range of relevant papers, not just the most popular ones.
Make sure not to copy verbatim from prior literature to avoid plagiarism.
You will have {total_rounds} rounds to add to the references but do not need to use them all.

DO NOT ADD A CITATION THAT ALREADY EXISTS!"""
````

---

## Prompt 18: Citation gathering first-round/search-query prompt

**File:** `ai_scientist/perform_writeup.py`  

**Variable:** `get_citation_addition citation_first_prompt_template`  

**Execution:** Loop: up to num_cite_rounds (default 20). Stops early if response contains "No more citations needed" or on errors/no papers.  

**Transition to next:** If JSON Query is parsed, Semantic Scholar search runs; transition to citation_second_prompt_template.  

**Placeholders / dynamic fills:**  

- `{Idea}`: filled at runtime from the variable/expression named `Idea` (or, for f-string expressions, the expression shown).

- `{citations}`: filled at runtime from the variable/expression named `citations` (or, for f-string expressions, the expression shown).

- `{current_round}`: filled at runtime from the variable/expression named `current_round` (or, for f-string expressions, the expression shown).

- `{report}`: filled at runtime from the variable/expression named `report` (or, for f-string expressions, the expression shown).

- `{total_rounds}`: filled at runtime from the variable/expression named `total_rounds` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""Round {current_round}/{total_rounds}:

You planned and executed the following idea:
```markdown
{Idea}
```

You produced the following report:
```markdown
{report}
```

Your current list of citations is:
```
{citations}
```

Identify the most important citation that you still need to add, and the query to find the paper.

Respond in the following format:

THOUGHT:
<THOUGHT>

RESPONSE:
```json
<JSON>
```

In <THOUGHT>, first briefly reason and identify which citations are missing.
If no more citations are needed, add "No more citations needed" to your thoughts.
Do not add "No more citations needed" if you are adding citations this round.

In <JSON>, respond in JSON format with the following fields:
- "Description": The purpose of the desired citation and a brief description of what you are looking for.
- "Query": The search query to find the paper (e.g., attention is all you need).
This JSON will be automatically parsed, so ensure the format is precise."""
````

---

## Prompt 19: Citation gathering second-round/paper-selection prompt

**File:** `ai_scientist/perform_writeup.py`  

**Variable:** `get_citation_addition citation_second_prompt_template`  

**Execution:** Loop: paired with first prompt each citation round after papers are retrieved.  

**Transition to next:** If response contains "Do not add any" or Selected is [], no citation added; otherwise selected BibTeX is appended and gather_citations continues to next round.  

**Placeholders / dynamic fills:**  

- `{papers}`: filled at runtime from the variable/expression named `papers` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""Search has recovered the following articles:

{papers}

Respond in the following format:

THOUGHT:
<THOUGHT>

RESPONSE:
```json
<JSON>
```

In <THOUGHT>, first briefly reason over the search results and identify which citation(s) best fit your paper.
If none are appropriate or would contribute significantly to the write-up, add "Do not add any" to your thoughts.
Do not select papers that are already in the `references.bib` file, or if the same citation exists under a different name.

In <JSON>, respond in JSON format with the following fields:
- "Selected": A list of integer indices for the selected papers, for example [0, 1]. Do not use quotes for the indices, e.g. "['0', '1']" is invalid.
- "Description": Update the previous description of the citation(s) with the additional context. This should be a brief description of the work(s), their relevance, and where in a paper these should be cited.
This JSON will be automatically parsed, so ensure the format is precise."""
````

---

## Prompt 20: References insertion format prompt

**File:** `ai_scientist/perform_writeup.py`  

**Variable:** `get_citation_addition references_format`  

**Execution:** Loop: used after a successful paper selection to format BibTeX block.  

**Transition to next:** Formatted citation text is appended to citations and the citation loop continues.  

**Placeholders / dynamic fills:**  

- `{bibtex}`: filled at runtime from the variable/expression named `bibtex` (or, for f-string expressions, the expression shown).

- `{description}`: filled at runtime from the variable/expression named `description` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""% {description}
{bibtex}"""
````

---

## Prompt 21: Writeup system prompt

**File:** `ai_scientist/perform_writeup.py`  

**Variable:** `writeup_system_message_template`  

**Execution:** Once for initial writeup; reused for every writeup reflection call.  

**Transition to next:** Next prompt is writeup_prompt.  

**Placeholders / dynamic fills:**  

- `{page_limit}`: filled at runtime from the variable/expression named `page_limit` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""You are an ambitious AI researcher who is looking to publish a paper that will contribute significantly to the field.
Ensure that the paper is scientifically accurate, objective, and truthful. Accurately report the experimental results, even if they are negative or inconclusive.
You are planning to submit to a top-tier ML conference, which has guidelines:
- The main paper is limited to {page_limit} pages, including all figures and tables, but excluding references, the impact statement, and optional appendices. In general, try to use the available space and include all relevant information.
- The main paper should be double-column format, while the appendices can be in single-column format. When in double column format, make sure that tables and figures are correctly placed.
- Do not change the overall style which is mandated by the conference. Keep to the current method of including the references.bib file.
- Do not remove the \\graphicspath directive or no figures will be found.

Here are some tips for each section of the paper:

- **Title**:
  - Title should be catchy and informative. It should give a good idea of what the paper is about.
  - Try to keep it under 2 lines.

- **Abstract**:
  - TL;DR of the paper.
  - What are we trying to do and why is it relevant?
  - Make sure the abstract reads smoothly and is well-motivated. This should be one continuous paragraph.

- **Introduction**:
  - Longer version of the Abstract, i.e., an overview of the entire paper.
  - Provide context to the study and explain its relevance.
  - If results are inconclusive or negative, present them frankly; if they are positive, you may highlight how the approach effectively addresses the research question or problem.
  - Summarize your contributions, highlighting pertinent findings, insights, or proposed methods.

- **Related Work**:
  - Academic siblings of our work, i.e., alternative attempts in literature at trying to address the same or similar problems.
  - Compare and contrast their approach with yours, noting key differences or similarities.
  - Ensure proper citations are provided.

- **Background**:
  - Present foundational concepts or prior work needed to understand your method.
  - This should include necessary definitions, the problem setting, or relevant theoretical constructs.

- **Method**:
  - Clearly detail what you propose to do and why. If your study aims to address certain hypotheses, describe them and how your method is constructed to test them.
  - If results are negative or inconclusive, you may suggest improvements or discuss possible causes.

- **Experimental Setup**:
  - Explain how you tested your method or hypothesis.
  - Describe necessary details such as data, environment, and baselines, but omit hardware details unless explicitly mentioned.

- **Experiments**:
  - Present the results truthfully according to the data you have. If outcomes are not as expected, discuss it transparently.
  - Include comparisons to baselines if available, and only include analyses supported by genuine data.
  - Try to include all relevant plots and tables. Consider combining multiple plots into one figure if they are related.

- **Conclusion**:
  - Summarize the entire paper, including key strengths or findings.
  - If results are strong, highlight how they might address the research problem.
  - If results are negative or inconclusive, highlight potential improvements or reasons and propose future directions.

- **Appendix**:
  - Place for supplementary material that did not fit in the main paper.

Ensure you are always writing good compilable LaTeX code. Common mistakes that should be fixed include:
- LaTeX syntax errors (unenclosed math, unmatched braces, etc.).
- Duplicate figure labels or references.
- Unescaped special characters: & % $ # _ {{ }} ~ ^ \\
- Proper table/figure closure.
- Do not hallucinate new citations or any results not in the logs.

When returning final code, place it in fenced triple backticks with 'latex' syntax highlighting.
"""
````

---

## Prompt 22: Writeup prompt

**File:** `ai_scientist/perform_writeup.py`  

**Variable:** `writeup_prompt`  

**Execution:** Once unless no_writing is set; produces full template.tex.  

**Transition to next:** Generated LaTeX is written and compiled; transition to writeup reflection loop.  

**Placeholders / dynamic fills:**  

- `{aggregator_code}`: filled at runtime from the variable/expression named `aggregator_code` (or, for f-string expressions, the expression shown).

- `{idea_text}`: filled at runtime from the variable/expression named `idea_text` (or, for f-string expressions, the expression shown).

- `{latex_writeup}`: filled at runtime from the variable/expression named `latex_writeup` (or, for f-string expressions, the expression shown).

- `{plot_descriptions}`: filled at runtime from the variable/expression named `plot_descriptions` (or, for f-string expressions, the expression shown).

- `{plot_list}`: filled at runtime from the variable/expression named `plot_list` (or, for f-string expressions, the expression shown).

- `{summaries}`: filled at runtime from the variable/expression named `summaries` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""Your goal is to write up the following idea:

```markdown
{idea_text}
```

We have the following experiment summaries (JSON):
```json
{summaries}
```

We also have a script used to produce the final plots (use this to see how the plots are generated and what names are used in the legend):
```python
{aggregator_code}
```
Please also consider which plots should naturally be grouped together as subfigures.

Available plots for the writeup (use these filenames):
```
{plot_list}
```

We also have VLM-based figure descriptions:
```
{plot_descriptions}
```

Your current progress on the LaTeX write-up is:
```latex
{latex_writeup}
```

Produce the final version of the LaTeX manuscript now, ensuring the paper is coherent, concise, and reports results accurately.
Return the entire file in full, with no unfilled placeholders!
This must be an acceptable complete LaTeX writeup.

Please provide the updated LaTeX code for 'template.tex', wrapped in triple backticks
with "latex" syntax highlighting, like so:

```latex
<UPDATED LATEX CODE>
```
"""
````

---

## Prompt 23: Writeup reflection prompt

**File:** `ai_scientist/perform_writeup.py`  

**Variable:** `perform_writeup reflection_prompt`  

**Execution:** Loop: for i in range(n_writeup_reflections). Exits if response contains "I am done", no code block, unchanged LaTeX, or max reflections reached.  

**Transition to next:** If revised LaTeX differs, file is updated/compiled and next reflection starts; after loop, final PDF result returned.  

**Placeholders / dynamic fills:**  

- `{check_output}`: filled at runtime from the variable/expression named `check_output` (or, for f-string expressions, the expression shown).

- `{reflection_page_info}`: filled at runtime from the variable/expression named `reflection_page_info` (or, for f-string expressions, the expression shown).

- `{sorted(invalid_figs)}`: filled at runtime from the variable/expression named `sorted(invalid_figs)` (or, for f-string expressions, the expression shown).

- `{sorted(unused_figs)}`: filled at runtime from the variable/expression named `sorted(unused_figs)` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""
Now let's reflect and identify any issues (including but not limited to):
1) Are there any LaTeX syntax errors or style violations we can fix? Refer to the chktex output below.
2) Is the writing clear, and scientifically rigorous?
3) Have we included all relevant details from the summaries without hallucinating?
4) The following figures are available in the folder but not used in the LaTeX: {sorted(unused_figs)}
5) The following figure references in the LaTeX do not match any actual file: {sorted(invalid_figs)}
{reflection_page_info}
chktex results:
```
{check_output}
```

Please provide a revised complete LaTeX in triple backticks, or repeat the same if no changes are needed.
Return the entire file in full, with no unfilled placeholders!
This must be an acceptable complete LaTeX writeup.
Do not hallucinate any details!

If you believe you are done, simply say: "I am done".
"""
````

---

## Prompt 24: ICBINB VLM-assisted writeup image reflection prompt

**File:** `ai_scientist/perform_icbinb_writeup.py`  

**Variable:** `perform_writeup img_reflection_prompt`  

**Execution:** Loop: inside writeup reflection iterations after VLM figure selection review; exits if response contains "I am done" or no valid LaTeX changes.  

**Transition to next:** If revised LaTeX differs, file is updated/compiled; loop continues to next reflection/page-limit step.  

**Placeholders / dynamic fills:**  

- `{reflection_page_info}`: filled at runtime from the variable/expression named `reflection_page_info` (or, for f-string expressions, the expression shown).

- `{review_img_selection}`: filled at runtime from the variable/expression named `review_img_selection` (or, for f-string expressions, the expression shown).

- `{sorted(unused_figs)}`: filled at runtime from the variable/expression named `sorted(unused_figs)` (or, for f-string expressions, the expression shown).

- `{sorted(used_figs)}`: filled at runtime from the variable/expression named `sorted(used_figs)` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"""Now let's reflect on
The following figures are currently used in the paper: {sorted(used_figs)}
The following figures are available in the folder but not used in the LaTeX: {sorted(unused_figs)}

{reflection_page_info}

The following is the VLM review on figures:

{review_img_selection}

Please review the figures and make the following changes:
1. For figures that do not add significant value to the paper, move them to the appendix
2. For figures that are not very informative or do not effectively communicate meaningful patterns, remove them entirely
3. For figures that does not contain subfigures and present sparse information, consider combining them with other related figures
4. Update all relevant text discussions to reflect any changes in figure placement or combinations
5. Enhance the scientific analysis of the remaining figures in the text - provide detailed, insightful discussions of their significance and findings

Please ensure all changes maintain scientific rigor and improve the paper's clarity and impact.
Be more aggressive with figure selection - move more figures to the appendix or group them together with other figures if the page limit is already exceeded.

If you believe you are done with reflection, simply say: "I am done"."""
````

---

## Prompt 25: ICBINB final page-limit reflection prompt

**File:** `ai_scientist/perform_icbinb_writeup.py`  

**Variable:** `perform_writeup final_reflection_prompt`  

**Execution:** Once after normal reflections to optimize page limit.  

**Transition to next:** If revised LaTeX block is returned and differs, final page-limit PDF is compiled.  

**Placeholders / dynamic fills:**  

- `{reflection_page_info}`: filled at runtime from the variable/expression named `reflection_page_info` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""{reflection_page_info}
USE MINIMAL EDITS TO OPTIMIZE THE PAGE LIMIT USAGE."""
````

---

## Prompt 26: VLM reviewer system prompt

**File:** `ai_scientist/perform_vlm_review.py`  

**Variable:** `reviewer_system_prompt_base`  

**Execution:** Used as system prompt in VLM image/caption/figure review calls.  

**Transition to next:** Next VLM user prompt depends on function: img_review_prompt, img_cap_ref_review_prompt, or img_cap_selection_prompt.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
reviewer_system_prompt_base = (
    "You are an AI researcher who is reviewing a paper that was submitted to a prestigious ML venue."
    "Be critical and cautious in your decision."
)
````

---

## Prompt 27: VLM image review prompt

**File:** `ai_scientist/perform_vlm_review.py`  

**Variable:** `img_review_prompt`  

**Execution:** Loop: once per image when generate_vlm_img_review is called (typically for plot descriptions before writeup).  

**Transition to next:** Parsed JSON description/review is stored for writeup plot_descriptions.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
"""

You will be given an image via the vision API. As a careful scientist reviewer, your task is to:
  1. Examine the provided image closely.
  2. Describe in detail what the image shows in a scientific manner.

You should:
  - Examine the figure in detail: conclude elements in figures (e.g. name of axis) and describe what information is shown (e.g. the line of loss decreases monotonically but plateaus after X epochs)
  - Suggest any potential improvements or issues in the figure itself (e.g., missing legend, unclear labeling, no meaningful conclusion, mismatch with what the caption claims).

Finally, respond in the following format:

THOUGHT:
<THOUGHT>

REVIEW JSON:
```json
<JSON>
```
In <JSON>, provide the review in JSON format with the following fields in the order:
- "Img_description": "<Describe the figure's contents here>"
- "Img_review": "<Your analysis of the figure itself, including any suggestions for improvement>"

In <THOUGHT>, first, thoroughly reason through your observations, analysis of alignment, and any suggested improvements. It is okay to be very long.
Then provide your final structured output in <JSON>.
Make sure the JSON is valid and properly formatted, as it will be parsed automatically."""
````

---

## Prompt 28: VLM image-caption-reference review prompt

**File:** `ai_scientist/perform_vlm_review.py`  

**Variable:** `img_cap_ref_review_prompt`  

**Execution:** Loop: once per figure extracted from PDF in perform_imgs_cap_ref_review.  

**Transition to next:** Parsed VLM reviews feed writeup reflection_prompt as review_img_cap_ref.  

**Placeholders / dynamic fills:**  

- `{abstract}`: filled at runtime from the variable/expression named `abstract` (or, for f-string expressions, the expression shown).

- `{caption}`: filled at runtime from the variable/expression named `caption` (or, for f-string expressions, the expression shown).

- `{main_text_figrefs}`: filled at runtime from the variable/expression named `main_text_figrefs` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""The abstract of the paper is:

{abstract}

You will be given an image via the vision API. As a careful scientist reviewer, your task is to:
  1. Examine the provided image closely.
  2. Describe in detail what the image shows in a scientific manner.
  3. Critically analyze whether the image content aligns with the given caption:

{caption}

  4. We also have references in the main text that mention the figure:

{main_text_figrefs}

You should:
  - Examine the figure in detail: conclude elements in figures (e.g. name of axis) and describe what information is shown (e.g. the line of loss decreases monotonically but plateaus after X epochs)
  - Suggest any potential improvements or issues in the figure itself (e.g., missing legend, unclear labeling, no meaningful conclusion, mismatch with what the caption claims).
  - Critique the caption: does it accurately describe the figure? Is it too long/short? Does it include a concise takeaway?
  - Review how well the main text references (figrefs) explain the figure: are they missing? Do they adequately describe the figure's content, context, or purpose?

Finally, respond in the following format:

THOUGHT:
<THOUGHT>

REVIEW JSON:
```json
<JSON>
```
In <JSON>, provide the review in JSON format with the following fields in the order:
- "Img_description": "<Describe the figure's contents here>"
- "Img_review": "<Your analysis of the figure itself, including any suggestions for improvement>"
- "Caption_review": "<Your assessment of how well the caption matches the figure and any suggestions>"
- "Figrefs_review": "<Your thoughts on whether the main text references adequately describe or integrate the figure>"

In <THOUGHT>, first, thoroughly reason through your observations, analysis of alignment, and any suggested improvements. It is okay to be very long.
Then provide your final structured output in <JSON>.
Make sure the JSON is valid and properly formatted, as it will be parsed automatically."""
````

---

## Prompt 29: VLM image-caption-selection review prompt

**File:** `ai_scientist/perform_vlm_review.py`  

**Variable:** `img_cap_selection_prompt`  

**Execution:** Loop: once per figure during page-limit figure selection review.  

**Transition to next:** Parsed reviews feed img_reflection_prompt for figure removal/combination decisions.  

**Placeholders / dynamic fills:**  

- `{abstract}`: filled at runtime from the variable/expression named `abstract` (or, for f-string expressions, the expression shown).

- `{caption}`: filled at runtime from the variable/expression named `caption` (or, for f-string expressions, the expression shown).

- `{main_text_figrefs}`: filled at runtime from the variable/expression named `main_text_figrefs` (or, for f-string expressions, the expression shown).

- `{reflection_page_info}`: filled at runtime from the variable/expression named `reflection_page_info` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""The abstract of the paper is:

{abstract}

You will be given an image via the vision API. As a careful scientist reviewer, your task is to:
  1. Examine the provided image closely.
  2. Describe in detail what the image shows in a scientific manner.
  3. Critically analyze whether the image content aligns with the given caption:

{caption}

  4. We also have references in the main text that mention the figure:

{main_text_figrefs}

  5. We have limited pages to present contents:

{reflection_page_info}

You should:
  - Examine the figure in detail: conclude elements in figures (e.g. name of axis) and describe what information is shown (e.g. the line of loss decreases monotonically but plateaus after X epochs)
  - Critique the caption: does it accurately describe the figure? Is it too long/short? Does it include a concise takeaway?
  - Review how well the main text references (figrefs) explain the figure: are they missing? Do they adequately describe the figure's content, context, or purpose?

After considering all of the above, you should carefully evaluate:
  - Given the current page limit, does this image and its relevant text add significant value to the paper's scientific argument?
  - Given the current page limit, is this image too sparse in information? Should it be combined with other figures in the main text?
  - Does this figure contain subfigures?
  - Is this figure not very informative? For example, some figures may show bars with very similar heights that are difficult to distinguish, or present data in a way that does not effectively communicate meaningful differences or patterns.

Finally, respond in the following format:

THOUGHT:
<THOUGHT>

REVIEW JSON:
```json
<JSON>
```
In <JSON>, provide the review in JSON format with the following fields in the order:
- "Img_description": "<Describe the figure's contents here>"
- "Img_review": "<Your analysis of the figure itself, including any suggestions for improvement>"
- "Caption_review": "<Your assessment of how well the caption matches the figure and any suggestions>"
- "Figrefs_review": "<Your thoughts on whether the main text references adequately describe or integrate the figure>"
- "Overall_comments": "<Your thoughts on whether this figure adds significant value to the paper. Should it be moved to the appendix or not?>"
- "Containing_sub_figures": "<Does this figure contain multiple sub-figures? Do you think the information in this figure is dense? If not, would you suggest combining it with other figures in the main text? If it contains subplots, are their sizes and positions nicely aligned? If not, describe the issues.>"
- "Informative_review": "<Is this figure informative? Does it effectively communicate meaningful differences or patterns? Or does it show data in a way that makes it difficult to distinguish differences (e.g. bars with very similar heights)?>"

In <THOUGHT>, first, thoroughly reason through your observations, analysis of alignment, and any suggested improvements. It is okay to be very long.
Then provide your final structured output in <JSON>.
Make sure the JSON is valid and properly formatted, as it will be parsed automatically."""
````

---

## Prompt 30: VLM duplicate image review system message

**File:** `ai_scientist/perform_vlm_review.py`  

**Variable:** `perform_duplication_check messages[0].content`  

**Execution:** Loop/once: when checking a PDF for duplicate/highly similar figures.  

**Transition to next:** VLM response identifies duplicates or reports none; result can inform writeup revisions.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
"You are an expert at identifying duplicate or highly similar images. "
"Please analyze these images and determine if they are duplicates or variations of the same visualization. "
"Response format: reasoning, followed by `Duplicate figures: <list of duplicate figure names>`."
"Make sure you use the exact figure names (e.g. Figure 1, Figure 2b, etc.) as they appear in the paper."
"If you find no duplicates, respond with `No duplicates found`."
````

---

## Prompt 31: VLM duplicate image review user message

**File:** `ai_scientist/perform_vlm_review.py`  

**Variable:** `perform_duplication_check messages[1].content[0].text`  

**Execution:** Loop/once: paired with duplicate image system message.  

**Transition to next:** VLM response returns duplicate analysis.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
Are any of these images duplicates or highly similar? If so, please identify which ones are similar and explain why. Focus on content similarity, not just visual style.
````

---

## Prompt 32: Peer review system prompt (negative/default)

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `reviewer_system_prompt_neg`  

**Execution:** Once per LLM review call; default system prompt unless reviewer_system_prompt override.  

**Transition to next:** Next prompt is neurips_form + few-shot examples + paper text.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
reviewer_system_prompt_neg = (
    reviewer_system_prompt_base
    + "If a paper is bad or you are unsure, give it bad scores and reject it."
)
````

---

## Prompt 33: Peer review system prompt (positive variant)

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `reviewer_system_prompt_pos`  

**Execution:** Optional variant if caller passes reviewer_system_prompt_pos.  

**Transition to next:** Next prompt is neurips_form + few-shot examples + paper text.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
reviewer_system_prompt_pos = (
    reviewer_system_prompt_base
    + "If a paper is good or you are unsure, give it good scores and accept it."
)
````

---

## Prompt 34: Peer review template instructions

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `template_instructions`  

**Execution:** Included by concatenation into neurips_form.  

**Transition to next:** Forms the tail of the peer review prompt.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
"""
Respond in the following format:

THOUGHT:
<THOUGHT>

REVIEW JSON:
```json
<JSON>
```

In <THOUGHT>, first briefly discuss your intuitions and reasoning for the evaluation.
Detail your high-level arguments, necessary choices and desired outcomes of the review.
Do not make generic comments here, but be specific to your current paper.
Treat this as the note-taking phase of your review.

In <JSON>, provide the review in JSON format with the following fields in the order:
- "Summary": A summary of the paper content and its contributions.
- "Strengths": A list of strengths of the paper.
- "Weaknesses": A list of weaknesses of the paper.
- "Originality": A rating from 1 to 4 (low, medium, high, very high).
- "Quality": A rating from 1 to 4 (low, medium, high, very high).
- "Clarity": A rating from 1 to 4 (low, medium, high, very high).
- "Significance": A rating from 1 to 4 (low, medium, high, very high).
- "Questions": A set of clarifying questions to be answered by the paper authors.
- "Limitations": A set of limitations and potential negative societal impacts of the work.
- "Ethical Concerns": A boolean value indicating whether there are ethical concerns.
- "Soundness": A rating from 1 to 4 (poor, fair, good, excellent).
- "Presentation": A rating from 1 to 4 (poor, fair, good, excellent).
- "Contribution": A rating from 1 to 4 (poor, fair, good, excellent).
- "Overall": A rating from 1 to 10 (very strong reject to award quality).
- "Confidence": A rating from 1 to 5 (low, medium, high, very high, absolute).
- "Decision": A decision that has to be one of the following: Accept, Reject.

For the "Decision" field, don't use Weak Accept, Borderline Accept, Borderline Reject, or Strong Reject. Instead, only use Accept or Reject.
This JSON will be automatically parsed, so ensure the format is precise.
"""
````

---

## Prompt 35: Peer review prompt / NeurIPS review form

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `neurips_form (+ optional few-shot + paper text)`  

**Execution:** Once per review, or num_reviews_ensemble times in batch; if num_fs_examples > 0, few-shot examples are inserted before the paper text.  

**Transition to next:** LLM JSON review is parsed; if num_reflections > 1, transition to reviewer_reflection_prompt. If ensemble, transition to meta-review prompt.  

**Placeholders / dynamic fills:**  

- `{text}`: filled at runtime from the variable/expression named `text` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
neurips_form = (
    """
## Review Form
Below is a description of the questions you will be asked on the review form for each paper and some guidelines on what to consider when answering these questions.
When writing your review, please keep in mind that after decisions have been made, reviews and meta-reviews of accepted papers and opted-in rejected papers will be made public.

1. Summary: Briefly summarize the paper and its contributions. This is not the place to critique the paper; the authors should generally agree with a well-written summary.
  - Strengths and Weaknesses: Please provide a thorough assessment of the strengths and weaknesses of the paper, touching on each of the following dimensions:
  - Originality: Are the tasks or methods new? Is the work a novel combination of well-known techniques? (This can be valuable!) Is it clear how this work differs from previous contributions? Is related work adequately cited
  - Quality: Is the submission technically sound? Are claims well supported (e.g., by theoretical analysis or experimental results)? Are the methods used appropriate? Is this a complete piece of work or work in progress? Are the authors careful and honest about evaluating both the strengths and weaknesses of their work
  - Clarity: Is the submission clearly written? Is it well organized? (If not, please make constructive suggestions for improving its clarity.) Does it adequately inform the reader? (Note that a superbly written paper provides enough information for an expert reader to reproduce its results.)
  - Significance: Are the results important? Are others (researchers or practitioners) likely to use the ideas or build on them? Does the submission address a difficult task in a better way than previous work? Does it advance the state of the art in a demonstrable way? Does it provide unique data, unique conclusions about existing data, or a unique theoretical or experimental approach?

2. Questions: Please list up and carefully describe any questions and suggestions for the authors. Think of the things where a response from the author can change your opinion, clarify a confusion or address a limitation. This can be very important for a productive rebuttal and discussion phase with the authors.

3. Limitations: Have the authors adequately addressed the limitations and potential negative societal impact of their work? If not, please include constructive suggestions for improvement.
In general, authors should be rewarded rather than punished for being up front about the limitations of their work and any potential negative societal impact. You are encouraged to think through whether any critical points are missing and provide these as feedback for the authors.

4. Ethical concerns: If there are ethical issues with this paper, please flag the paper for an ethics review. For guidance on when this is appropriate, please review the NeurIPS ethics guidelines.

5. Soundness: Please assign the paper a numerical rating on the following scale to indicate the soundness of the technical claims, experimental and research methodology and on whether the central claims of the paper are adequately supported with evidence.
  4: excellent
  3: good
  2: fair
  1: poor

6. Presentation: Please assign the paper a numerical rating on the following scale to indicate the quality of the presentation. This should take into account the writing style and clarity, as well as contextualization relative to prior work.
  4: excellent
  3: good
  2: fair
  1: poor

7. Contribution: Please assign the paper a numerical rating on the following scale to indicate the quality of the overall contribution this paper makes to the research area being studied. Are the questions being asked important? Does the paper bring a significant originality of ideas and/or execution? Are the results valuable to share with the broader NeurIPS community.
  4: excellent
  3: good
  2: fair
  1: poor

8. Overall: Please provide an "overall score" for this submission. Choices:
  10: Award quality: Technically flawless paper with groundbreaking impact on one or more areas of AI, with exceptionally strong evaluation, reproducibility, and resources, and no unaddressed ethical considerations.
  9: Very Strong Accept: Technically flawless paper with groundbreaking impact on at least one area of AI and excellent impact on multiple areas of AI, with flawless evaluation, resources, and reproducibility, and no unaddressed ethical considerations.
  8: Strong Accept: Technically strong paper with, with novel ideas, excellent impact on at least one area of AI or high-to-excellent impact on multiple areas of AI, with excellent evaluation, resources, and reproducibility, and no unaddressed ethical considerations.
  7: Accept: Technically solid paper, with high impact on at least one sub-area of AI or moderate-to-high impact on more than one area of AI, with good-to-excellent evaluation, resources, reproducibility, and no unaddressed ethical considerations.
  6: Weak Accept: Technically solid, moderate-to-high impact paper, with no major concerns with respect to evaluation, resources, reproducibility, ethical considerations.
  5: Borderline accept: Technically solid paper where reasons to accept outweigh reasons to reject, e.g., limited evaluation. Please use sparingly.
  4: Borderline reject: Technically solid paper where reasons to reject, e.g., limited evaluation, outweigh reasons to accept, e.g., good evaluation. Please use sparingly.
  3: Reject: For instance, a paper with technical flaws, weak evaluation, inadequate reproducibility and incompletely addressed ethical considerations.
  2: Strong Reject: For instance, a paper with major technical flaws, and/or poor evaluation, limited impact, poor reproducibility and mostly unaddressed ethical considerations.
  1: Very Strong Reject: For instance, a paper with trivial results or unaddressed ethical considerations

9. Confidence:  Please provide a "confidence score" for your assessment of this submission to indicate how confident you are in your evaluation. Choices:
  5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.
  4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.
  3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.
  2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.
  1: Your assessment is an educated guess. The submission is not in your area or the submission was difficult to understand. Math/other details were not carefully checked.
"""
    + template_instructions
)

# Runtime addition in perform_review
base_prompt += f"""
Here is the paper you are asked to review:
```
{text}
```"""
````

---

## Prompt 36: Peer review few-shot examples prompt

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `get_review_fewshot_examples fewshot_prompt`  

**Execution:** Loop: prepends up to num_fs_examples sample paper/review pairs.  

**Transition to next:** After examples are appended, paper text is appended and peer review call runs.  

**Placeholders / dynamic fills:**  

- `{paper_text}`: filled at runtime from the variable/expression named `paper_text` (or, for f-string expressions, the expression shown).

- `{review_text}`: filled at runtime from the variable/expression named `review_text` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""
Below are some sample reviews, copied from previous machine learning conferences.
Note that while each review is formatted differently according to each reviewer's style, the reviews are well-structured and therefore easy to navigate.
"""

# Runtime appended repeatedly per example:
f"""
Paper:

```
{paper_text}
```

Review:

```
{review_text}
```
"""
````

---

## Prompt 37: Peer review reflection prompt

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `reviewer_reflection_prompt`  

**Execution:** Loop: for j in range(num_reflections - 1); exits early if text contains "I am done".  

**Transition to next:** Updated review JSON is parsed; after loop final review is returned.  

**Placeholders / dynamic fills:**  

- `{current_round}`: filled at runtime from the variable/expression named `current_round` (or, for f-string expressions, the expression shown).

- `{num_reflections}`: filled at runtime from the variable/expression named `num_reflections` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""Round {current_round}/{num_reflections}.
In your thoughts, first carefully consider the accuracy and soundness of the review you just created.
Include any other factors that you think are important in evaluating the paper.
Ensure the review is clear and concise, and the JSON is in the correct format.
Do not make things overly complicated.
In the next attempt, try and refine and improve your review.
Stick to the spirit of the original review unless there are glaring issues.

Respond in the same format as before:
THOUGHT:
<THOUGHT>

REVIEW JSON:
```json
<JSON>
```

If there is nothing to improve, simply repeat the previous JSON EXACTLY after the thought and include "I am done" at the end of the thoughts but before the JSON.
ONLY INCLUDE "I am done" IF YOU ARE MAKING NO MORE CHANGES."""
````

---

## Prompt 38: Meta-review system prompt

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `meta_reviewer_system_prompt`  

**Execution:** Optional: once when num_reviews_ensemble > 1.  

**Transition to next:** Next prompt is neurips_form plus all parsed reviews.  

**Placeholders / dynamic fills:**  

- `{reviewer_count}`: filled at runtime from the variable/expression named `reviewer_count` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""You are an Area Chair at a machine learning conference.
You are in charge of meta-reviewing a paper that was reviewed by {reviewer_count} reviewers.
Your job is to aggregate the reviews into a single meta-review in the same format.
Be critical and cautious in your decision, find consensus, and respect the opinion of all the reviewers."""
````

---

## Prompt 39: Meta-review aggregation prompt

**File:** `ai_scientist/perform_llm_review.py`  

**Variable:** `get_meta_review base_prompt = neurips_form + review_text`  

**Execution:** Optional: once when ensemble reviews are aggregated.  

**Transition to next:** Parsed meta-review becomes final review; score fields may be averaged from ensemble.  

**Placeholders / dynamic fills:**  

- `{i + 1}`: filled at runtime from the variable/expression named `i + 1` (or, for f-string expressions, the expression shown).

- `{json.dumps(r)}`: filled at runtime from the variable/expression named `json.dumps(r)` (or, for f-string expressions, the expression shown).

- `{len(reviews)}`: filled at runtime from the variable/expression named `len(reviews)` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
neurips_form + review_text

# Runtime review_text per review:
f"""
Review {i + 1}/{len(reviews)}:
```
{json.dumps(r)}
```
"""
````

---

## Prompt 40: Output format control for summarizers

**File:** `ai_scientist/treesearch/log_summarization.py`  

**Variable:** `output_format_control`  

**Execution:** Included in summarizer prompts.  

**Transition to next:** Summarizer response is parsed as JSON.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
"""Respond in the following format:

THOUGHT:
<THOUGHT>

JSON:
```json
<JSON>
```

In <THOUGHT>, thoroughly reason as an expert researcher. First, reason about each node, and then reason carefully by combining all the information. It is okay to be very detailed.

In <JSON>, provide the review in JSON format with the following fields in exactly this order:
- "Experiment_description": a string describing the conducted experiments
- "Significance": a string explaining why these experiments are important and what impact their findings might have
- "Description": a string describing the methods, steps taken, and any pertinent context needed to understand the experiments
- "List_of_included_plots": a list of plots that should be included. Each entry should include:
  • "path" (the plot path)
  • "description" (its original description)
  • "analysis" (your analysis of its scientific insights)
- "Key_numerical_results": a list of all important numerical results. Be selective about results that contribute to scientific insights. Each entry should include:
  • "result" (float number)
  • "description" (your short description of the result)
  • "analysis" (your analysis of its scientific insights)

Ensure the JSON is valid and properly formatted, as it will be automatically parsed."""
````

---

## Prompt 41: Report/node summarizer prompt

**File:** `ai_scientist/treesearch/log_summarization.py`  

**Variable:** `report_summarizer_prompt`  

**Execution:** Loop: once per journal/stage summary.  

**Transition to next:** Stage aggregate prompt consumes these summaries.  

**Placeholders / dynamic fills:**  

- `{node_infos}`: filled at runtime from the variable/expression named `node_infos` (or, for f-string expressions, the expression shown).

- `{stage_name}`: filled at runtime from the variable/expression named `stage_name` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""You are given multiple experiment logs from different "nodes". Each node represents attempts and experiments exploring various scientific ideas.

One key point is that these nodes collectively illustrate a stage of testing different methods or approaches. The crucial task is to identify the scientific insights gleaned from this stage. For example, if one node tries method A and another node tries method B, you should compare any observed differences in performance or outcomes. Summarize both experiments in "Experiment_description", explain the processes in "Description", and place any key numerical findings (such as accuracy metrics, loss values, or runtime comparisons) in "Key_numerical_results."

Be concise and avoid repeating the same information from different nodes. You are encouraged to be thorough, but you do not need to include information from every node. Reason carefully about which results from which nodes are scientifically insightful.

The name of this stage of the experiment: {stage_name}

Here are the experiment logs of the nodes:

{node_infos}
"""
    + output_format_control
````

---

## Prompt 42: Stage aggregate prompt

**File:** `ai_scientist/treesearch/log_summarization.py`  

**Variable:** `stage_aggregate_prompt`  

**Execution:** Loop: once per completed stage during overall_summarize.  

**Transition to next:** Overall summaries are written and used by plotting/writeup.  

**Placeholders / dynamic fills:**  

- `{current_summary}`: filled at runtime from the variable/expression named `current_summary` (or, for f-string expressions, the expression shown).

- `{prev_summary}`: filled at runtime from the variable/expression named `prev_summary` (or, for f-string expressions, the expression shown).

- `{stage_name}`: filled at runtime from the variable/expression named `stage_name` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""You are given:

1) The summary of all previous experiment stages:
{prev_summary}

2) The name of the current experiment stage:
{stage_name}

3) The summary of the current stage:
{current_summary}


Your task is to produce an **updated comprehensive summary** of all experiment stages, including the newly introduced results from the current stage.

**Key Requirements:**
1. **No Loss of Critical Information**
   - Preserve valuable insights from the summary of all previous experiment stages. Do not remove or alter crucial texts.
   - Absolutely no hallucinations: if something does not appear in the logs or summaries, do not invent it. If something appears in the previous summary, do not make any mistakes when repeating it.
2. **Merge New Stage Data**
   - Integrate relevant results from the current stage into the existing summary.
   - Identify any overlap or repetition between new and old content, and remove only that which is clearly redundant or no longer scientifically insightful.
   - Be very careful if you want to remove or shorten the old content. By default, you can keep most of it and append new text.
   - Highlight how new findings connect to or differ from previous findings.
3. **Numerical Results and Visuals**
   - Carefully maintain the most insightful plots, figures, and numerical results.
   - Do not delete crucial quantitative findings or meaningful visual references.
4. **Length and Format**
   - The final summary will likely be **very long**. That is acceptable.
   - Present the updated summary in a format consistent with the style of the previous summaries (e.g., same section headings or structure).

Respond in the following format:

THOUGHT:
<THOUGHT>

JSON:
```json
<JSON>
```
Ensure the JSON is valid and properly formatted, as it will be automatically parsed.
"""
````

---

## Prompt 43: Overall plan summarizer prompt

**File:** `ai_scientist/treesearch/log_summarization.py`  

**Variable:** `overall_plan_summarizer_prompt`  

**Execution:** Loop: when synthesizing plan summaries for nodes.  

**Transition to next:** Plan summary stored for downstream summaries.  

**Placeholders / dynamic fills:**  

- `{current_plan}`: filled at runtime from the variable/expression named `current_plan` (or, for f-string expressions, the expression shown).

- `{prev_overall_plan}`: filled at runtime from the variable/expression named `prev_overall_plan` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
"""You have been provided with the plans for both the parent node and the current node. Your task is to synthesize a comprehensive summary of the overall plan by integrating details from both the parent and current node plans.
The summary should be thorough and clearly articulate the underlying motivations.
For example, if in your previous overall plan you were experimenting with a new idea, and now your current plan is to fix certain bugs in the previous implementation, your returned overall plan should focus on your previous overall plan, and briefly mention that the current plan includes bug fixes. If your current plan is more about implementing new ideas, then you should summarize that thoroughly along with the previous overall plan.
The goal is to create a comprehensive summary of all historical plans, focusing on the main scientific planning and objectives.

Previous overall plan:
{prev_overall_plan}

Current plan:
{current_plan}

Respond in the following format:

THOUGHT:
<THOUGHT>

JSON:
```json
<JSON>
```

In <THOUGHT>, thoroughly reason as an expert researcher. First, reason over each node, and then carefully combine all information. It is okay to be very detailed.

In <JSON>, provide the review in JSON format with the following field in exactly this order:
- "overall_plan": a string that describes the overall plan based on the current and previous overall plans

Ensure the JSON is valid and properly formatted, as it will be automatically parsed.
"""
````

---

## Prompt 44: Journal-to-report system prompt

**File:** `ai_scientist/treesearch/journal2report.py`  

**Variable:** `system_prompt_dict`  

**Execution:** Once when journal2report is called.  

**Transition to next:** Context prompt is sent with system prompt to generate concise report.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
        "Role": "You are a research assistant that always uses concise language.",
        "Goal": "The goal is to write a technical report summarising the empirical findings and technical decisions.",
        "Input": "You are given a raw research journal with list of design attempts and their outcomes, and a research idea description.",
        "Output": [
            "Your output should be a single markdown document.",
            "Your report should have the following sections: Introduction, Preprocessing, Methods, Results Discussion, Future Work",
            "You can include subsections if needed.",
        ],
    }
````

---

## Prompt 45: Journal-to-report context prompt

**File:** `ai_scientist/treesearch/journal2report.py`  

**Variable:** `context_prompt`  

**Execution:** Once when journal2report is called.  

**Transition to next:** Generated report feeds final summarize/writeup stages.  

**Placeholders / dynamic fills:**  

- `{report_input}`: filled at runtime from the variable/expression named `report_input` (or, for f-string expressions, the expression shown).

- `{task_desc}`: filled at runtime from the variable/expression named `task_desc` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
f"Here is the research journal of the agent: <journal>{report_input}<\\journal>, "
        f"and the research idea description is: <research_proposal>{task_desc}<\\research_proposal>."
````

---

## Prompt 46: BFTS review function schema for execution output

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `review_func_spec`  

**Execution:** Loop: used by parse_exec_result once per executed node.  

**Transition to next:** Function-call JSON sets is_bug/summary and controls debug vs non-buggy path.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
review_func_spec = FunctionSpec(
    name="submit_review",
    json_schema={
        "type": "object",
        "properties": {
            "is_bug": {
                "type": "boolean",
                "description": "true if the output log shows that the execution failed or has some bug, otherwise false.",
            },
            "summary": {
                "type": "string",
                "description": "if there is a bug, summarize the bug and propose a fix. Otherwise, leave it empty.",
            },
        },
        "required": [
            "is_bug",
            "summary",
        ],
    },
    description="Submit a review evaluating the output of the training script.",
)
````

---

## Prompt 47: BFTS VLM feedback function schema

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `vlm_feedback_spec`  

**Execution:** Loop: used when analyzing generated experiment plots/images.  

**Transition to next:** Structured VLM feedback is stored on the node and used by debug/improvement/stage-completion prompts.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
vlm_feedback_spec = FunctionSpec(
    name="analyze_experiment_plots",
    json_schema={
        "type": "object",
        "properties": {
            "plot_analyses": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "analysis": {
                            "type": "string",
                            "description": "Detailed analysis of the plot's results and implications",
                        },
                    },
                    "required": ["analysis"],
                },
            },
            "valid_plots_received": {
                "type": "boolean",
                "description": "True if valid plots were received, False otherwise. For example, if the plots are empty or not meaningful, this should be False.",
            },
            "vlm_feedback_summary": {
                "type": "string",
                "description": "Summarize the feedback from the VLM. If the task involves generative modeling, make sure to focus on the generated samples.",
            },
        },
        "required": ["plot_analyses", "valid_plots_received", "vlm_feedback_summary"],
    },
    description="Analyze experimental plots and provide detailed feedback on the results.",
)
````

---

## Prompt 48: BFTS metric parsing function schema

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `metric_parse_spec`  

**Execution:** Loop: used when parsing metrics from execution output.  

**Transition to next:** Parsed metrics attach to node and influence best-node/stage decisions.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
metric_parse_spec = FunctionSpec(
    name="parse_metrics",
    json_schema={
        "type": "object",
        "strict": True,
        "properties": {
            "valid_metrics_received": {
                "type": "boolean",
                "description": "True if the metrics were successfully received, False otherwise. For example if the execution output does not contain any metrics, set this to False.",
            },
            "metric_names": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "metric_name": {
                            "type": "string",
                            "description": "Specify the metric name clearly. Avoid vague terms like 'train,' 'val,' or 'test.' Instead, use precise labels such as 'train accuracy,' 'validation loss,' or 'test F1 score,' etc.",
                        },
                        "lower_is_better": {
                            "type": "boolean",
                            "description": "Whether lower values are better for this metric",
                        },
                        "description": {
                            "type": "string",
                            "description": "Description of the metric",
                        },
                        "data": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dataset_name": {
                                        "type": "string",
                                        "description": "The name of the dataset. Never include 'train', 'val', or 'test' in the dataset name.",
                                    },
                                    "final_value": {
                                        "type": "number",
                                        "description": "The final value of the metric for this dataset",
                                    },
                                    "best_value": {
                                        "type": "number",
                                        "description": "The best value of the metric for this dataset",
                                    },
                                },
                                "required": [
                                    "dataset_name",
                                    "final_value",
                                    "best_value",
                                ],
                            },
                        },
                    },
                    "required": [
                        "data",
                        "metric_name",
                        "lower_is_better",
                        "description",
                    ],
                },
                "additionalProperties": False,
            },
        },
        "required": ["valid_metrics_received", "metric_names"],
        "additionalProperties": False,
    },
    description="Parse metrics from execution output",
)
````

---

## Prompt 49: BFTS plot selection function schema

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `plot_selection_spec`  

**Execution:** Loop: used to select the most relevant plots for VLM analysis.  

**Transition to next:** Selected plots are sent to VLM feedback analysis.  

**Placeholders / dynamic fills:**  

- `{"type": "string", "description": "Full path to a plot file"}`: filled at runtime from the variable/expression named `"type": "string", "description": "Full path to a plot file"` (or, for f-string expressions, the expression shown).


**Full Prompt:**

````python
plot_selection_spec = FunctionSpec(
    name="select_plots",
    json_schema={
        "type": "object",
        "properties": {
            "selected_plots": {
                "type": "array",
                "description": "List of selected plot file paths",
                "items": {"type": "string", "description": "Full path to a plot file"},
                "maxItems": 10,
            }
        },
        "required": ["selected_plots"],
    },
    description="Select the 10 most relevant plots for analysis",
)
````

---

## Prompt 50: BFTS node selection function schema

**File:** `ai_scientist/treesearch/journal.py`  

**Variable:** `node_selection_spec`  

**Execution:** Loop: used when multiple good nodes are candidates.  

**Transition to next:** Selected node is used as best implementation for next actions.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
node_selection_spec = FunctionSpec(
    name="select_best_implementation",
    description="Select the best implementation based on comprehensive analysis",
    json_schema={
        "type": "object",
        "properties": {
            "selected_id": {
                "type": "string",
                "description": "ID of the selected best implementation",
            },
            "reasoning": {
                "type": "string",
                "description": "Detailed explanation of why this implementation was chosen",
            },
        },
        "required": ["selected_id", "reasoning"],
    },
)
````

---

## Prompt 51: Global evaluation metric definition prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `ParallelAgent._define_global_metrics prompt`  

**Execution:** Once at experiment setup when defining the metric.  

**Transition to next:** Metric definition is stored and inserted into implementation guidelines.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an AI researcher setting up experiments. "
                "Please propose meaningful evaluation metrics that will help analyze "
                "the performance and characteristics of solutions for this research task."
            ),
            "Research idea": self.task_desc,
            "Instructions": [
                "Propose a single evaluation metric that would be useful for analyzing the performance of solutions for this research task.",
                "Note: Validation loss will be tracked separately so you don't need to include it in your response.",
                "Format your response as a list containing:",
                "- name: The name of the metric",
                "- maximize: Whether higher values are better (true/false)",
                "- description: A brief explanation of what the metric measures"
                "Your list should contain only one metric.",
            ],
        }
````

---

## Prompt 52: Hyperparameter tuning idea prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `ParallelAgent._generate_hyperparam_tuning_idea hyperparam_tuning_prompt`  

**Execution:** Loop: Stage 2 baseline tuning; retries until a new hyperparameter name is parsed or retry_limit is reached.  

**Transition to next:** Parsed hyperparameter idea triggers hyperparameter tuning implementation prompt.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an AI researcher conducting hyperparameter tuning for baseline experiments. "
                "Based on the current implementation and previous hyperparameter tuning attempts (if any), "
                "propose ONE new hyperparameter tuning idea to see if it improves the performance."
                "You should first check if simply training longer (more epochs) improves the performance."
                "Then try tuning common hyperparameters such as learning rate, batch size, etc."
                "Only propose algorithm-specific and/or model-specific hyperparameters after you have tried the above."
            ),
            "Base code you are working on": wrap_code(self.best_stage1_node.code),
            "Previous Hyperparam Tuning Attempts": {
                "Has been tried": tried if tried else "Nothing has been tried yet.",
            },
            "Instructions": {
                "Requirements": [
                    "1. Identify ONE specific hyperparameter to tune",
                    "2. Ensure the hyperparameter is different from previous attempts",
                ]
            },
            "Response format": (
                "Your response should start with 'HYPERPARAM NAME: <hyperparam name>' on the first line to represent the name of the hyperparameter."
                "The second line should start with 'DESCRIPTION: <description>', a brief description of what hyperparameter is being tuned and why (3-5 sentences). "
            ),
        }
````

---

## Prompt 53: Hyperparameter tuning implementation prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._generate_hyperparam_tuning_node prompt`  

**Execution:** Loop: once per hyperparameter tuning idea; plan_and_code_query retries up to 3 on parse failure.  

**Transition to next:** Generated code is executed/evaluated, then stage continues or completes.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an experienced AI researcher. You are provided with a previously developed "
                "baseline implementation. Your task is to implement hyperparameter tuning for the following idea: "
                + hyperparam_idea.name
                + ". "
                + hyperparam_idea.description
            ),
            "Base code you are working on": wrap_code(parent_node.code),
            "Instructions": {},
        }
````

---

## Prompt 54: Ablation idea prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `ParallelAgent._generate_ablation_idea ablation_prompt`  

**Execution:** Loop: Stage 4 ablations; retries until a new ablation is parsed or retry_limit reached.  

**Transition to next:** Parsed ablation idea triggers ablation implementation prompt.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an AI researcher conducting ablation studies. "
                "Based on the current implementation and previous ablations (if any), "
                "propose ONE new ablation study that tests a different aspect of the model."
            ),
            "Base code you are working on": wrap_code(self.best_stage3_node.code),
            "Previous Ablations": {
                "Has been tried": (
                    completed if completed else "Nothing has been tried yet."
                ),
            },
            "Instructions": {
                "Requirements": [
                    "1. Identify ONE specific component/feature to ablate",
                    "2. Ensure the ablation is different from previous completed or running attempts",
                    "3. The ablation should be a new idea, not a variation of previous ideas",
                    "4. If you have only used a single synthetic dataset throughout the experiment, one of your ablations should be to use multiple synthetic datasets (at least 3 different datasets)",
                ]
            },
            "Response format": (
                "Your response should start with 'ABLATION NAME: <ablation name>' on the first line to represent the name of the ablation."
                "The second line should start with 'ABLATION DESCRIPTION: <description>', a brief description of what component is being ablated and why (3-5 sentences), "
            ),
        }
````

---

## Prompt 55: Ablation implementation prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._generate_ablation_node prompt`  

**Execution:** Loop: once per ablation idea; plan_and_code_query retries up to 3 on parse failure.  

**Transition to next:** Generated ablation code is executed/evaluated and included in summaries.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an experienced AI researcher. You are provided with a previously developed "
                "baseline implementation. Your task is to implement the ablation study for the following idea: "
                + ablation_idea.name
                + ". "
                + ablation_idea.description
            ),
            "Base code you are working on": wrap_code(parent_node.code),
            "Instructions": {},
        }
````

---

## Prompt 56: Experiment plotting-code generation prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._generate_plotting_code plotting_prompt`  

**Execution:** Loop: once per node needing plot code.  

**Transition to next:** Generated plotting code is executed; plots feed VLM feedback.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Instructions": {},
        }
````

---

## Prompt 57: Experiment plotting-result determination prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._generate_plotting_code determine_prompt`  

**Execution:** Loop: after plotting code execution.  

**Transition to next:** Determines whether plots are meaningful/valid for VLM analysis.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": "You are an AI researcher analyzing experiment results. Based on the plot analyses and feedback, determine which datasets are successfully tested. Return reasoning and the dataset names that are successfully executed, or an empty string if no datasets are successfully executed.",
            "Plot analyses": plot_analyses,
            "VLM feedback summary": node.vlm_feedback_summary,
            "Original plotting code": node.plot_code,
            "Response format": (
                "Your response should start with 'REASONING: <reasoning>' to think about the plot analysis and feedback in the first line."
                "In the second line, you should have a list of dataset names that are successfully executed, starting with 'SUCCESSFULLY_TESTED_DATASETS: <list_datasets_successfully_tested>', "
            ),
        }
````

---

## Prompt 58: Experiment plot selection prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `prompt_select_plots`  

**Execution:** Loop: when many plots exist, selects up to relevant plots for VLM analysis.  

**Transition to next:** Selected plot paths are encoded/sent to VLM.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
                "Introduction": (
                    "You are an experienced AI researcher analyzing experimental results. "
                    "You have been provided with plots from a machine learning experiment. "
                    "Please select 10 most relevant plots to analyze. "
                    "For similar plots (e.g. generated samples at each epoch), select only at most 5 plots at a suitable interval of epochs."
                    "Format your response as a list of plot paths, where each plot path includes the full path to the plot file."
                ),
                "Plot paths": node.plot_paths,
            }
````

---

## Prompt 59: Experiment result summary prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `MinimalAgent._generate_node_summary summary_prompt`  

**Execution:** Loop: once per node when saving notes/summaries.  

**Transition to next:** Node summary is saved and later aggregated into stage/report summaries.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
            "Introduction": (
                "You are an AI researcher analyzing experimental results. "
                "Please summarize the findings from this experiment iteration."
            ),
            "Research idea": self.task_desc,
            "Implementation": wrap_code(node.code),
            "Plan": node.plan,
            "Execution output": wrap_code(node.term_out, lang=""),
            "Analysis": node.analysis,
            "Metric": str(node.metric) if node.metric else "Failed",
            "Plot Analyses": (
                node.plot_analyses if hasattr(node, "plot_analyses") else []
            ),
            "VLM Feedback": (
                node.vlm_feedback_summary
                if hasattr(node, "vlm_feedback_summary")
                else ""
            ),
        }
````

---

## Prompt 60: Metric parser code-generation prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `parse_metrics_prompt`  

**Execution:** Loop: when automatic metric parser code must be generated for execution output.  

**Transition to next:** Generated parser code is run to extract metric values.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
                        "Introduction": (
                            "You are an AI researcher analyzing experimental results stored in numpy files. "
                            "Write code to load and analyze the metrics from experiment_data.npy."
                        ),
                        "Context": [
                            "Original Code: " + child_node.code,
                        ],
                        "Instructions": [
                            "0. Make sure to get the working directory from os.path.join(os.getcwd(), 'working')",
                            "1. Load the experiment_data.npy file, which is located in the working directory",
                            "2. Extract metrics for each dataset. Make sure to refer to the original code to understand the structure of the data.",
                            "3. Always print the name of the dataset before printing the metrics",
                            "4. Always print the name of the metric before printing the value by specifying the metric name clearly. Avoid vague terms like 'train,' 'val,' or 'test.' Instead, use precise labels such as 'train accuracy,' 'validation loss,' or 'test F1 score,' etc.",
                            "5. You only need to print the best or final value for each metric for each dataset",
                            "6. DO NOT CREATE ANY PLOTS",
                            "Important code structure requirements:",
                            "  - Do NOT put any execution code inside 'if __name__ == \"__main__\":' block. Do not use 'if __name__ == \"__main__\":' at all.",
                            "  - All code should be at the global scope or in functions that are called from the global scope",
                            "  - The script should execute immediately when run, without requiring any special entry point",
                        ],
                        "Example data loading code": [
                            """
                            import matplotlib.pyplot as plt
                            import numpy as np

                            experiment_data = np.load(os.path.join(os.getcwd(), 'experiment_data.npy'), allow_pickle=True).item()
                            """
                        ],
                        "Response format": worker_agent._prompt_metricparse_resp_fmt(),
                    }
````

---

## Prompt 61: Metrics extraction prompt

**File:** `ai_scientist/treesearch/parallel_agent.py`  

**Variable:** `metrics_prompt`  

**Execution:** Loop: parses metrics after execution output/parser results.  

**Transition to next:** Structured metrics update node.metric and downstream selection/stage logic.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
{
                            "Introduction": "Parse the metrics from the execution output. You only need the final or best value of a metric for each dataset, not the entire list during training.",
                            "Execution Output": metrics_exec_result.term_out,
                        }
````


# Second GitHub-wide audit addendum

This addendum was added after a full-repository grep over all files, not only Python files. It records additional dynamic insertions, stage schemas, and source-file prompt content that are part of the GitHub repository but were easy to miss because they are injected through variables, files, or function schemas.

---

## Prompt 62: Ideation Semantic Scholar tool description

**File:** `ai_scientist/tools/semantic_scholar.py`  

**Variable:** `SemanticScholarSearchTool.__init__ description`  

**Execution:** Instantiated once; interpolated into `tool_descriptions` inside ideation `system_prompt`.  

**Transition to next:** The LLM may choose ACTION `SearchSemanticScholar`; result is injected into `idea_reflection_prompt` as `last_tool_results`.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
def __init__(
        self,
        name: str = "SearchSemanticScholar",
        description: str = (
            "Search for relevant literature using Semantic Scholar. "
            "Provide a search query to find relevant papers."
        ),
        max_results: int = 10,
    ):
        parameters = [
            {
                "name": "query",
                "type": "str",
                "description": "The search query to find relevant papers.",
            }
        ]
        super().__init__(name, description, parameters)
        self.max_results = max_results
        self.S2_API_KEY = os.getenv("S2_API_KEY")
        if not self.S2_API_KEY:
            warnings.warn(
                "No Semantic Scholar API key found. Requests will be subject to stricter rate limits. "
                "Set the S2_API_KEY environment variable for higher limits."
            )
````
---

## Prompt 63: Ideation FinalizeIdea tool description

**File:** `ai_scientist/perform_ideation_temp_free.py`  

**Variable:** `tools[1]["description"]`  

**Execution:** Instantiated once; interpolated into `tool_descriptions` inside ideation `system_prompt`.  

**Transition to next:** The LLM may choose ACTION `FinalizeIdea`; parsed JSON terminates the current proposal loop.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
"description": """Finalize your idea by providing the idea details.

The IDEA JSON should include the following fields:
- "Name": A short descriptor of the idea. Lowercase, no spaces, underscores allowed.
- "Title": A catchy and informative title for the proposal.
- "Short Hypothesis": A concise statement of the main hypothesis or research question. Clarify the need for this specific direction, ensure this is the best setting to investigate this idea, and there are not obvious other simpler ways to answer the question.
- "Related Work": A brief discussion of the most relevant related work and how the proposal clearly distinguishes from it, and is not a trivial extension.
- "Abstract": An abstract that summarizes the proposal in conference format (approximately 250 words).
- "Experiments": A list of experiments that would be conducted to validate the proposal. Ensure these are simple and feasible. Be specific in exactly how you would test the hypothesis, and detail precise algorithmic changes. Include the evaluation metrics you would use.
- "Risk Factors and Limitations": A list of potential risks and limitations of the proposal."""
````
---

## Prompt 64: Default ICBINB workshop/topic description prompt content

**File:** `ai_scientist/ideas/i_cant_believe_its_not_better.md`  

**Variable:** `workshop_description file content`  

**Execution:** Used once per proposal generation round as `{workshop_description}` in `idea_generation_prompt` when this default topic file is passed.  

**Transition to next:** After this content is inserted, the idea generation prompt asks for a new high-level proposal.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
# Title: I Can't Believe It's Not Better: Challenges in Applied Deep Learning

## Keywords
negative results, deep learning, failure modes

## TL;DR
Why don't deep learning approaches always deliver as expected in the real world? Dive deep into the pitfalls and challenges of applied deep learning.

## Abstract
The goal of the I Can’t Believe It’s Not Better (ICBINB) workshop series is to promote slow science and build a community to discuss surprising and negative results, thereby encouraging a culture of transparency and shared learning. In recent years, we have witnessed a remarkable rise of Deep Learning (DL), whose impressive performance on benchmark tasks has led to increasing ambitions to deploy DL in real-world applications across all fields and disciplines. However, despite its potential, DL still faces many challenges during deployment in dynamic, real-world conditions, thus exposing practical limitations that are often overlooked in controlled benchmarks. Therefore, in this year’s ICBINB workshop, we aim to explore the challenges, unexpected outcomes, and common principles underlying similar issues and failure modes encountered across various fields and disciplines when deploying DL models in real-world scenarios. We will invite contributions and discussions from diverse fields including, but not limited to, healthcare, scientific discovery, robotics, education, equality & fairness, and social sciences. The failure modes may include suboptimal performance, concerns with the safety and reliability of applying DL models in unpredictable real-world applications, as well as ethical and societal challenges. More importantly, we aim to discuss common reasons or patterns in challenges and failure modes across disciplines. By creating a platform for researchers from different domains to interact and share insights, we hope to accelerate research by translating findings from one field to another, and also deepen DL researchers’ understanding of the universal fundamental issues that should be addressed within the current theoretical and empirical research paradigms. Embracing negative results as valuable learning opportunities will, therefore, help the community learn from past mistakes, and drive the development of more robust, reliable, and applicable AI models.
````
---

## Prompt 65: BFTS task description construction prompt

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager._get_task_desc_str task_desc`  

**Execution:** Constructed from selected idea JSON before experiment-stage prompts; used as research/task context.  

**Transition to next:** Feeds MinimalAgent task_desc and stage display; subsequent BFTS draft/debug/improve prompts consume it.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
def _get_task_desc_str(self):
        task_desc = """You are an ambitious AI researcher who is looking to publish a paper that will contribute significantly to the field.
You have an idea and you want to conduct creative experiments to gain scientific insights.
Your aim is to run experiments to gather sufficient results for a top conference paper.
Your research idea:\n\n
"""
        task_desc += (
            "Title:\n"
            + self.task_desc["Title"]
            + "\n"
            + "Abstract:\n"
            + self.task_desc["Abstract"]
            + "\n"
            + "Short Hypothesis:\n"
            + self.task_desc["Short Hypothesis"]
            + "\n"
        )
        if "Code" in self.task_desc:
            task_desc += "Code To Use:\n" + self.task_desc["Code"] + "\n"
        return task_desc
````
---

## Prompt 66: BFTS main stage goals instructions

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager.main_stage_goals`  

**Execution:** Created in AgentManager.__init__; inserted into Stage.goals and completion/substage prompts.  

**Transition to next:** Stage goals steer stage creation, substage goals, and completion checks.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
        self.main_stage_goals: Dict[int, str] = {
            1: """
                - Focus on getting basic working implementation
                - Use a simple dataset
                - Aim for basic functional correctness
                - If you are given \"Code To Use\", you can directly use it as a starting point.""",
            2: """
                - Change hyperparameters such as learning rate, number of epochs, batch size, etc. to improve the performance
                - DO NOT change the model architecture from the previous stage
                - Introduce TWO more new datasets from HuggingFace test the model. Try very hard to think what Huggingface datasets can be used here for testing.""",
            3: """
                - Explore novel improvements
                - Come up with experiments to reveal new insights
                - Be creative and think outside the box
                - MAKE SURE you use THREE HuggingFace dataset in total to test your models""",
            4: """
                - Conduct systematic component analysis that reveals the contribution of each part
                - Use the same datasets you used from the previous stage""",
        }
````
---

## Prompt 67: Stage configuration function schema

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `stage_config_spec`  

**Execution:** Used when generating/configuring the next experimental stage.  

**Transition to next:** Structured response creates a Stage with name, description, goals, and max_iterations.  

**Placeholders / dynamic fills:**  

- `{"type": "string"}`: filled at runtime from `"type": "string"` or the f-string expression shown.


**Full Prompt:**

````python
stage_config_spec = FunctionSpec(
    name="generate_stage_config",
    description="Generate configuration for the next experimental stage",
    json_schema={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Brief, descriptive name for the stage",
            },
            "description": {
                "type": "string",
                "description": "Detailed description of the stage's purpose",
            },
            "goals": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of specific, measurable goals for this stage",
            },
            "max_iterations": {
                "type": "integer",
                "description": "Maximum number of iterations to run in this stage",
            },
        },
        "required": ["name", "description", "goals", "max_iterations"],
    },
)
````
---

## Prompt 68: Stage progress evaluation function schema

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `stage_progress_eval_spec`  

**Execution:** Used with the stage progression evaluation prompt.  

**Transition to next:** Structured response decides whether to progress or continue/refocus current stage.  

**Placeholders / dynamic fills:**  

- `{"type": "string"}`: filled at runtime from `"type": "string"` or the f-string expression shown.


**Full Prompt:**

````python
stage_progress_eval_spec = FunctionSpec(
    name="evaluate_stage_progression",
    description="Evaluate readiness to progress to next experimental stage",
    json_schema={
        "type": "object",
        "properties": {
            "ready_for_next_stage": {
                "type": "boolean",
                "description": "Whether the experiment is ready to progress to next stage",
            },
            "reasoning": {
                "type": "string",
                "description": "Detailed reasoning for the progression decision",
            },
            "recommendations": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Specific recommendations for current or next stage",
            },
            "suggested_focus": {
                "type": "string",
                "description": "Key areas to focus on in the next iterations",
            },
        },
        "required": ["ready_for_next_stage", "reasoning", "recommendations"],
    },
)
````
---

## Prompt 69: Substage goal function schema

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `substage_goal_spec`  

**Execution:** Defined inside `_generate_substage_goal`; used after the substage-goal prompt.  

**Transition to next:** Structured response creates next sub-stage name/goals.  

**Placeholders / dynamic fills:**  

- None detected in the preserved template/source segment.


**Full Prompt:**

````python
substage_goal_spec = FunctionSpec(
            name="generate_substage_goals",
            description="Generate specific goals for the next experimental sub-stage",
            json_schema={
                "type": "object",
                "properties": {
                    "goals": {
                        "type": "string",
                        "description": "Detailed, specific goals for the next sub-stage",
                    },
                    "sub_stage_name": {
                        "type": "string",
                        "description": "The name of the next sub-stage",
                    },
                },
                "required": ["goals", "sub_stage_name"],
            },
        )
````
---

## Prompt 70: Stage analysis / next-stage configuration prompt builder

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager._create_stage_analysis_prompt`  

**Execution:** Called when determining next stage configuration from previous stage results.  

**Transition to next:** Returned prompt is passed into `_get_response`, which uses stage_config_spec to create next stage.  

**Placeholders / dynamic fills:**  

- `{', '.join(previous_results['issues'])}`: filled at runtime from `', '.join(previous_results['issues'])` or the f-string expression shown.

- `{analysis['analysis']}`: filled at runtime from `analysis['analysis']` or the f-string expression shown.

- `{i}`: filled at runtime from `i` or the f-string expression shown.

- `{i+1}`: filled at runtime from `i+1` or the f-string expression shown.

- `{previous_results['metrics']['best_metric']['value'] if previous_results['metrics']['best_metric'] else 'N/A'}`: filled at runtime from `previous_results['metrics']['best_metric']['value'] if previous_results['metrics']['best_metric'] else 'N/A'` or the f-string expression shown.

- `{previous_results['metrics']['buggy_nodes']}`: filled at runtime from `previous_results['metrics']['buggy_nodes']` or the f-string expression shown.

- `{previous_results['metrics']['good_nodes']}`: filled at runtime from `previous_results['metrics']['good_nodes']` or the f-string expression shown.

- `{previous_results['metrics']['total_nodes']}`: filled at runtime from `previous_results['metrics']['total_nodes']` or the f-string expression shown.

- `{previous_results['progress']['convergence_status']}`: filled at runtime from `previous_results['progress']['convergence_status']` or the f-string expression shown.

- `{previous_stages[-1].stage_number}`: filled at runtime from `previous_stages[-1].stage_number` or the f-string expression shown.

- `{self._curate_task_desc(previous_stages[-1])}`: filled at runtime from `self._curate_task_desc(previous_stages[-1])` or the f-string expression shown.

- `{stage.description}`: filled at runtime from `stage.description` or the f-string expression shown.

- `{stage.name}`: filled at runtime from `stage.name` or the f-string expression shown.

- `{stage_history}`: filled at runtime from `stage_history` or the f-string expression shown.

- `{stage_number}`: filled at runtime from `stage_number` or the f-string expression shown.

- `{stage_number-1}`: filled at runtime from `stage_number-1` or the f-string expression shown.

- `{summaries}`: filled at runtime from `summaries` or the f-string expression shown.

- `{summary}`: filled at runtime from `summary` or the f-string expression shown.


**Full Prompt:**

````python
def _create_stage_analysis_prompt(
        self,
        previous_stages: List[Stage],
        previous_results: Optional[Dict[str, Any]],
        is_initial_stage: bool,
    ) -> str:
        """Create detailed prompt to determine next stage configuration"""
        prompt_parts = [
            f"Task Description: {self._curate_task_desc(previous_stages[-1])}",
            f"Current Stage Number: {previous_stages[-1].stage_number}",
        ]

        if previous_stages:
            stage_history = "\n".join(
                f"Stage {i+1}: {stage.name} - {stage.description}"
                for i, stage in enumerate(previous_stages)
            )
            prompt_parts.append(f"Previous Stages:\n{stage_history}")

        if previous_results:
            # Format node summaries
            if "node_summaries" in previous_results["metrics"]:
                summaries = "\n".join(
                    f"Node {i}: {summary}"
                    for i, summary in enumerate(
                        previous_results["metrics"]["node_summaries"]
                    )
                )
                prompt_parts.append(f"Node Analysis:\n{summaries}")

            # Format VLM feedback and plot analysis
            if "plot_insights" in previous_results:
                plot_insights = previous_results["plot_insights"]
                prompt_parts.append("Visual Analysis Findings:")
                for analysis in plot_insights["analyses"]:
                    prompt_parts.append(f"- {analysis['analysis']}")

            # Format other metrics and findings
            metrics_summary = (
                f"Progress Summary:\n"
                f"- Total attempts: {previous_results['metrics']['total_nodes']}\n"
                f"- Successful implementations: {previous_results['metrics']['good_nodes']}\n"
                f"- Failed attempts: {previous_results['metrics']['buggy_nodes']}\n"
                f"- Best performance: {previous_results['metrics']['best_metric']['value'] if previous_results['metrics']['best_metric'] else 'N/A'}\n"
                f"- Issues identified: {', '.join(previous_results['issues'])}\n"
                f"- Progress status: {previous_results['progress']['convergence_status']}"
            )
            prompt_parts.append(metrics_summary)

            # Save stage transition analysis to notes directory
            base_dir = Path(self.workspace_dir).parent.parent
            run_name = Path(self.workspace_dir).name
            notes_dir = (
                base_dir
                / "logs"
                / run_name
                / "notes"
                / f"stage_{stage_number-1}_to_{stage_number}"
            )
            notes_dir.mkdir(parents=True, exist_ok=True)

            analysis_data = {
                "stage_transition": {
                    "from_stage": stage_number - 1,
                    "to_stage": stage_number,
                    "is_initial_stage": is_initial_stage,  # Add flag for initial stage
                    "metrics_summary": metrics_summary,
                    "node_summaries": previous_results["metrics"].get(
                        "node_summaries", []
                    ),
                    "plot_insights": previous_results.get("plot_insights", {}),
                    "issues": previous_results["issues"],
                    "progress": previous_results["progress"],
                }
            }

            with open(notes_dir / "stage_transition_analysis.json", "w") as f:
                json.dump(analysis_data, f, indent=2)

        prompt_parts.append(
            "Based on the above comprehensive analysis, determine the appropriate "
            "configuration for the next experimental stage. Consider:\n"
            "1. Visual analysis insights from plots\n"
            "2. Individual node performance and patterns\n"
            "3. Overall progress and convergence status\n"
            "4. Identified issues and challenges\n\n"
            "Include:\n"
            "1. Stage name (brief, descriptive)\n"
            "2. Detailed description of the stage's purpose\n"
            "3. Specific, measurable goals\n"
            "4. Maximum iterations needed\n"
            "5. Success metric threshold (if applicable)"
        )

        return "\n\n".join(prompt_parts)
````
---

## Prompt 71: Runtime stage configuration schema in _get_response

**File:** `ai_scientist/treesearch/agent_manager.py`  

**Variable:** `AgentManager._get_response stage_config_spec`  

**Execution:** Used inside `_get_response` when querying the LLM for stage configuration.  

**Transition to next:** Structured response is returned to manager and used to instantiate/configure the next stage.  

**Placeholders / dynamic fills:**  

- `{"type": "string"}`: filled at runtime from `"type": "string"` or the f-string expression shown.

- `{e}`: filled at runtime from `e` or the f-string expression shown.


**Full Prompt:**

````python
def _get_response(self, prompt: str) -> Dict[str, Any]:
        """Get structured response from LLM for stage configuration.

        Args:
            prompt: The analysis prompt to send to the LLM

        Returns:
            Dictionary containing stage configuration with keys:
            - name: str
            - description: str
            - goals: List[str]
            - max_iterations: int
            - success_metric_threshold: Optional[float]
        """
        stage_config_spec = {
            "name": "generate_stage_config",
            "json_schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Brief, descriptive name for the stage",
                    },
                    "description": {
                        "type": "string",
                        "description": "Detailed description of the stage's purpose",
                    },
                    "goals": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of specific, measurable goals for this stage",
                    },
                    "max_iterations": {
                        "type": "integer",
                        "description": "Maximum number of iterations to run in this stage",
                    },
                },
                "required": ["name", "description", "goals", "max_iterations"],
            },
            "description": "Generate configuration for the next experimental stage",
        }

        try:
            response = query(
                system_message=prompt,
                user_message=None,
                func_spec=stage_config_spec,
                model=self.cfg.agent.feedback.model,
                temperature=self.cfg.agent.feedback.temp,
            )
            return response

        except Exception as e:
            logger.error(f"Error getting LLM response: {e}")
            # Provide a fallback configuration in case of errors
            return {
                "name": "fallback_stage",
                "description": "Fallback stage due to LLM error",
                "goals": ["Recover from error and continue execution"],
                "max_iterations": 3,
                "success_metric_threshold": None,
            }
````
---

## Prompt 72: Peer-review few-shot source files inserted at runtime

**File:** `ai_scientist/fewshot_examples/*.txt + *.json`  

**Variable:** `fewshot_papers / fewshot_reviews external content`  

**Execution:** Loop: up to `num_fs_examples` examples are loaded; each paper text and JSON review is appended to peer review prompt.  

**Transition to next:** After few-shot examples, the target paper text is appended and review call runs. This entry records the exact repository files used as source content; full insertion template is already in Prompt 40.  

**Placeholders / dynamic fills:**  

- `{paper_text}`: filled at runtime from `paper_text` or the f-string expression shown.

- `{review_text}`: filled at runtime from `review_text` or the f-string expression shown.


**Full Prompt:**

````python
fewshot_papers = [
    ai_scientist/fewshot_examples/132_automated_relational.pdf (+ .txt)
    ai_scientist/fewshot_examples/attention.pdf (+ .txt)
    ai_scientist/fewshot_examples/2_carpe_diem.pdf (+ .txt)
]

fewshot_reviews = [
    ai_scientist/fewshot_examples/132_automated_relational.json
    ai_scientist/fewshot_examples/attention.json
    ai_scientist/fewshot_examples/2_carpe_diem.json
]

Runtime insertion template:

f"""
Paper:

```
{paper_text}
```

Review:

```
{review_text}
```
"""
````
