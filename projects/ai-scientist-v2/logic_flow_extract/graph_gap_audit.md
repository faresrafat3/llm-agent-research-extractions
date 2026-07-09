# Graph vs Code Gap Audit — AI Scientist v2

Source repository: `https://github.com/SakanaAI/AI-Scientist-v2`  
Audited commit: `96bd51617cfdbb494a9fc283af00fe090edfae48`

## Result

Yes — the previous Mermaid graph captured the main pipeline, but it omitted or compressed several concrete loops, decisions, prompts, and placeholders present in the Python code. The graph files were updated to include these missing pieces.

## Missing / underrepresented items found and added

### 1. `launch_scientist_bfts.py`

Added:

- `--skip_writeup` decision.
- `--skip_review` decision.
- `--writeup_type` decision: `normal` vs `icbinb`.
- `writeup_retries` loop.
- `writeup_success` early break condition.
- optional `--load_code` path existence decision.
- optional `--add_dataset_ref` path existence decision.
- `added_code` four-way merge decision: dataset ref + code, dataset only, code only, none.
- review PDF selection logic: final reflection PDF, highest numbered reflection PDF, fallback reflection PDF.
- post-run process cleanup loops over child/orphan processes.

### 2. `AgentManager.run`

Added:

- Main stage loop: `while self.current_stage`.
- Sub-stage loop: `while current_substage`.
- Inner node loop: `while True`.
- Main-stage completion check before sub-stage completion.
- Multi-seed evaluation after main-stage completion.
- Stage-level aggregated plot generation after multi-seed evaluation.
- missing best-node failure branch.
- sub-stage completion branch and creation of next sub-stage.
- next main stage creation branch and termination when stage 4 is complete.
- checkpoint/save branch.

### 3. `ParallelAgent._select_parallel_nodes`

Added:

- `while len(nodes_to_process) < num_workers` worker-filling loop.
- initial draft decision when `draft_nodes < num_drafts`.
- viable-tree filtering decision: skip trees whose leaves are all buggy.
- probabilistic debug decision: `random.random() < debug_prob`.
- debug eligibility condition: node is leaf and `debug_depth <= max_debug_depth`.
- processed-tree balancing decision.
- Stage 4 special handling: use `best_stage3_node` for ablation.
- Stage 2 special handling: use `best_stage1_node` for hyperparameter tuning.
- normal Stage 1/3 best-first improvement branch.
- fallback to new draft when no good node exists.

### 4. `ParallelAgent.step` and `_process_node_wrapper`

Added:

- worker submission loop.
- GPU acquisition success/failure decision.
- Stage 2 hyperparameter idea generation branch.
- Stage 4 ablation idea generation branch.
- future result timeout/error handling.
- GPU release in `finally`.
- node serialization/deserialization path.

### 5. Code-generation and idea-generation retry loops

Added:

- `plan_and_code_query` retry loop up to 3 attempts.
- parsing feedback injection when code extraction fails.
- hyperparameter idea retry loop up to 5 attempts.
- fallback hyperparameter idea if parsing repeatedly fails.
- ablation idea retry loop up to 5 attempts.
- fallback ablation idea if parsing repeatedly fails.

### 6. Node execution and metric/plot/VLM flow

Added:

- metric parser code-generation prompt branch.
- metric parser execution branch.
- invalid/missing metrics branch: set `WorstMetricValue` and mark buggy.
- plot code generation branch.
- seed evaluation branch reusing parent plot code.
- stage 3 and stage 4 plotting-code reference reuse.
- plotting retry loop up to 3 failures.
- move `.npy` and `.png` outputs to experiment result folders.
- VLM plot analysis only if plots exist.

### 7. Multi-seed evaluation and aggregation

Added:

- loop over `cfg.agent.multi_seed_eval.num_seeds`.
- seed-specific code injection.
- future result timeout/error handling.
- `_aggregate_seed_eval_results` prompt.
- seed aggregation plotting node.

### 8. Plot aggregation

The original graph had the main reflection loop. It now also calls out:

- no-code response branch.
- script execution failure branch still producing `aggregator_out` for reflection.
- identical/no-new-code reflection branch.

### 9. Writeup and ICBINB-specific flow

Added:

- normal vs ICBINB writeup decision.
- citation cache behavior.
- writeup retry loop from launcher.
- ICBINB VLM image-caption-reference review.
- duplicate-figure review.
- image selection review for page-limit pressure.
- final page-limit reflection prompt.

### 10. Review flow

Added:

- PDF selection logic.
- `perform_review` optional ensemble branch.
- meta-review branch.
- reviewer reflection loop.
- VLM image-caption-reference review file output.

### 11. Prompts/placeholders

The graph now explicitly references the prompt families that were previously only implied:

- `system_prompt`, `idea_generation_prompt`, `idea_reflection_prompt`.
- BFTS draft/debug/improve prompts.
- hyperparameter idea and implementation prompts.
- ablation idea and implementation prompts.
- metric parser prompt and metric extraction prompt.
- plotting-code prompt.
- seed aggregation plotting prompt.
- stage/substage completion and progression prompts/schemas.
- plot aggregator system/user/reflection prompts.
- citation first/second prompts.
- normal and ICBINB writeup prompts.
- writeup reflection, VLM reflection, and final page-limit prompts.
- LLM review, review reflection, and meta-review prompts.

## Files updated

- `graph_english.mmd`
- `graph_arabic.mmd`
- `graph_english.md`
- `graph_arabic.md`
- `graph_gap_audit.md`
- `README.md`
