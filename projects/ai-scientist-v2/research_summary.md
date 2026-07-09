# AI Scientist v2 — Research / System Summary

Source repository: `https://github.com/SakanaAI/AI-Scientist-v2`  
Audited commit: `96bd51617cfdbb494a9fc283af00fe090edfae48`

## Core idea

AI Scientist v2 is an end-to-end autonomous scientific discovery pipeline. It can generate research ideas, run experiments with agentic tree search, aggregate plots, gather citations, write a paper, and review the output.

The system is not a single prompt. It is a multi-stage agentic workflow composed of:

1. ideation,
2. experiment execution via BFTS / agent manager,
3. metric parsing,
4. plot generation and VLM feedback,
5. multi-seed evaluation,
6. report summarization,
7. plot aggregation,
8. citation gathering,
9. writeup generation,
10. writeup reflection,
11. VLM figure/caption review,
12. peer review.

## Main execution pipeline

1. `perform_ideation_temp_free.py` optionally generates research ideas with literature search.
2. `launch_scientist_bfts.py` selects an idea and creates an experiment folder.
3. `perform_experiments_bfts_with_agentmanager.py` starts staged experiment execution.
4. `AgentManager` orchestrates stages and sub-stages.
5. `ParallelAgent` generates, debugs, improves, tunes, and ablates experiment code.
6. The interpreter runs generated code and captures outputs.
7. Metric prompts parse outputs into structured metrics.
8. Plot prompts generate visualizations and VLM feedback.
9. Stage summaries are aggregated.
10. `perform_plotting.py` creates final paper figures.
11. `perform_writeup.py` or `perform_icbinb_writeup.py` creates LaTeX manuscripts.
12. Citation prompts gather BibTeX via Semantic Scholar.
13. Reflection prompts revise the paper.
14. VLM prompts review figures/captions/page limits.
15. LLM review prompts produce peer-review style evaluation.

## Key system concept

The most important architectural idea is progressive agentic tree search:

- Stage 1: initial implementation.
- Stage 2: baseline/hyperparameter tuning.
- Stage 3: creative research improvements.
- Stage 4: ablation studies.

Each node in the tree contains generated code, execution result, metric, plot code, plots, and analysis. The agent iteratively decides whether to draft, debug, improve, tune, or ablate.

## Prompt families

- Ideation system/user/reflection prompts.
- Semantic Scholar tool prompts.
- BFTS draft/debug/improve prompts.
- Hyperparameter and ablation prompts.
- Metric parsing prompts.
- Plotting code prompts.
- VLM feedback prompts.
- Stage completion/progression schemas.
- Report summarization prompts.
- Plot aggregation prompts.
- Citation gathering prompts.
- Writeup and writeup reflection prompts.
- ICBINB-specific figure/page-limit prompts.
- VLM figure/caption/reference prompts.
- Peer-review and meta-review prompts.

## Outputs

- idea JSON/Markdown,
- experiment code and logs,
- metrics,
- plots,
- experiment summaries,
- final figures,
- citations,
- LaTeX paper,
- PDF,
- peer review JSON/text,
- VLM figure reviews,
- Mermaid graphs and extraction reports in this audit package.

## Value of this extraction

This package makes the implicit system explicit: every prompt family, loop, decision point, schema, and graph edge is documented in a human-readable way.