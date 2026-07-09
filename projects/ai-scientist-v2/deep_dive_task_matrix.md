# AI Scientist v2 — Deep Dive Task / Phase Matrix

## Universal pipeline

| Phase | Main files | Inputs | Core loop/decision | Outputs |
|---|---|---|---|---|
| Ideation | `perform_ideation_temp_free.py` | workshop markdown, previous ideas | generation/reflection loop; SearchSemanticScholar vs FinalizeIdea | idea JSON |
| Launch | `launch_scientist_bfts.py` | idea JSON, optional code, optional dataset ref, CLI args | load_code/add_dataset_ref/writeup_type/skip flags | experiment folder/config |
| Experiment manager | `agent_manager.py` | task desc, config, workspace | main stage loop, substage loop, stage completion | journals, checkpoints |
| BFTS worker | `parallel_agent.py` | parent node, memory summary, stage | draft/debug/improve/hyperparam/ablation selection | child node code/results |
| Execution parsing | `parallel_agent.py` | generated code output | bug vs valid, metric parse success/failure | metric and analysis |
| Plotting | `parallel_agent.py`, `perform_plotting.py` | experiment data, summaries | plot-code retry, aggregation reflection | figures |
| Summaries | `journal.py`, `log_summarization.py` | journal nodes | node selection and summarization | stage summaries |
| Citations | `perform_writeup.py`, `perform_icbinb_writeup.py` | idea/report/current citations | 20-round Semantic Scholar loop | BibTeX |
| Writeup | `perform_writeup.py`, `perform_icbinb_writeup.py` | idea, summaries, plots, citations, LaTeX template | writeup retry/reflection/page-limit loops | LaTeX/PDF |
| Review | `perform_llm_review.py`, `perform_vlm_review.py` | paper PDF/text/images | peer review/reflection/meta-review/VLM review | review JSON |

---

## 1. Ideation

### Inputs

- workshop/topic Markdown.
- existing idea archive.
- LLM model/client.
- Semantic Scholar tool.

### Loop

Outer loop: `for gen_idx in range(max_num_generations)`.  
Inner loop: `for reflection_round in range(num_reflections)`.

### Decisions

- round 0 uses initial idea generation prompt.
- later rounds use reflection prompt.
- `ACTION == SearchSemanticScholar` runs literature search and feeds results into next reflection.
- `ACTION == FinalizeIdea` parses idea JSON and exits current proposal loop.
- invalid parse/JSON exits current attempt.

### Outputs

- structured idea JSON with Name, Title, Short Hypothesis, Related Work, Abstract, Experiments, Risk Factors and Limitations.

---

## 2. Launch and setup

### Inputs

- `--load_ideas`
- `--idea_idx`
- `--load_code`
- `--add_dataset_ref`
- model arguments
- skip flags

### Decisions

- code file exists or warn.
- dataset reference exists or warn.
- merge code+dataset ref, code only, dataset only, or none.
- `writeup_type`: normal vs ICBINB.
- `skip_writeup`, `skip_review`.

### Outputs

- experiment directory.
- `idea.md`.
- `idea.json`.
- BFTS config.

---

## 3. AgentManager stages

### Main loops

- `while self.current_stage`
- `while current_substage`
- inner `while True` node loop.

### Decisions

- stage completion before substage completion.
- if stage complete: run multi-seed eval and plot aggregation.
- if substage complete: create next substage.
- if main stage complete: create next main stage.
- if stage 4 complete: stop.
- if no best node when needed: stop experiment.

### Outputs

- stage transitions.
- checkpoints.
- logs.
- stage summaries.

---

## 4. ParallelAgent node selection

### Loop

`while len(nodes_to_process) < num_workers`.

### Decisions

- create draft if draft nodes < num_drafts.
- maybe debug if random < debug_prob.
- only debug leaf buggy nodes with depth <= max_debug_depth.
- stage 2 uses best_stage1_node for hyperparameter tuning.
- stage 4 uses best_stage3_node for ablations.
- stage 1/3 use best-first improvement.
- no good nodes fallback to draft.

### Outputs

- selected nodes for worker processes.

---

## 5. Worker generation/execution

### Branches

- None node → draft prompt.
- buggy node → debug prompt.
- stage 2 → hyperparameter idea + implementation prompt.
- stage 4 → ablation idea + implementation prompt.
- normal non-buggy → improve prompt.

### Retry loops

- plan/code parsing up to 3 attempts.
- hyperparameter idea parsing up to 5 attempts.
- ablation idea parsing up to 5 attempts.
- plot code retry up to 3 attempts.

### Decisions

- code block parsed or parsing feedback added.
- execution bug or valid result.
- metrics valid or set WorstMetricValue.
- plots exist or skip VLM.

### Outputs

- Node with code, output, metric, plots, VLM feedback.

---

## 6. Multi-seed evaluation

### Loop

`for seed in range(num_seeds)`.

### Flow

- inject seed into best-node code.
- run worker process with `seed_eval=True`.
- collect seed nodes.
- generate aggregated plotting code from seed data.
- create seed aggregation node.

---

## 7. Plot aggregation

### Inputs

- idea text.
- filtered summaries.
- experiment data paths.

### Loop

`for i in range(n_reflections)`.

### Decisions

- no Python code block → stop.
- script run success/failure still yields `aggregator_out`.
- if `I am done` and figures exist → stop.
- if updated code differs → rerun.
- if identical/no code → continue/exhaust.

---

## 8. Citation gathering

### Loop

Up to `num_cite_rounds`, default 20.

### Decisions

- cached citations exist.
- `No more citations needed`.
- no papers found.
- `Do not add any`.
- selected papers empty or valid.

### Outputs

- references.bib content with BibTeX and descriptions.

---

## 9. Writeup

### Branches

- normal writeup: 8-page top-tier ML conference style.
- ICBINB writeup: 4-page workshop/negative-results style.

### Loops

- launcher `writeup_retries`.
- internal `n_writeup_reflections`.
- ICBINB final page-limit reflection.

### Decisions

- LaTeX block parsed.
- `I am done`.
- unchanged LaTeX.
- page limit exceeded.
- unused/invalid figures.
- VLM figure/caption issues.

---

## 10. Review

### Branches

- skip review if `skip_review` or `skip_writeup`.
- choose final/highest/fallback reflection PDF.
- LLM peer review.
- optional ensemble/meta-review.
- VLM image-caption-reference review.

### Outputs

- `review_text.txt`.
- `review_img_cap_ref.json`.

---

## Deep conclusion

AI Scientist v2 is best understood as a staged research factory. Its quality depends on the interaction between code-generation prompts, execution feedback, metric parsing, plot/VLM feedback, and manuscript reflection. The extraction package exposes these hidden control loops and prompt schemas.