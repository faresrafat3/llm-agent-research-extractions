# Unified Master LLM Agent Pipeline

**Codename: ARSENAL** — Automatic Reasoning, Search, Evaluation, Navigation, and Adaptive Learning

One complete master system that combines the strongest patterns from **eight** research systems into a single unified operational arsenal.

| # | Source System | Paper | What we take |
|---|---|---|---|
| 1 | **AI Scientist v2** | SakanaAI | Multi-stage progressive pipeline, BFTS node tree, multi-seed eval, writeup + peer review |
| 2 | **Self-Refine** | arXiv:2303.17651 | Generate → Feedback → Refine loop, multi-aspect scoring, history-aware iteration |
| 3 | **Reflexion** | arXiv:2303.11366 | Verbal reinforcement, episodic memory, trial-level reflection |
| 4 | **Meta-Prompting** | arXiv:2401.12954 | Conductor / expert dispatch, tool experts (Python), intermediate feedback append |
| 5 | **Tree of Thoughts** | arXiv:2305.10601 | Classic deliberate tree search: propose/sample × value/vote × BFS beam / DFS prune |
| 6 | **LATS** | arXiv:2310.04406 | MCTS + UCT selection, LM value, expansion, rollout, backprop (+ env + reflection) |
| 7 | **APE** | arXiv:2211.01910 | Automatic instruction search, likelihood/UCB ranking, demo functions |
| 8 | **The Prompt Report** | arXiv:2406.06608 | 58-technique taxonomy, technique family routing, best-practice selection |

## What this package contains

```text
master-unified-pipeline/
├── README.md
├── research_summary.md
├── pattern_extraction.md          # strongest patterns from each of the 8
├── unified_architecture.md        # full architecture of ARSENAL
├── search_family_map.md           # ToT vs LATS decision map (L3)
├── prompts_complete.md            # master prompt library
├── python_logic_flow_complete.md  # full logic / loops / decisions
├── python_logic_inventory.json
├── deep_dive_task_matrix.md
├── graphs/
│   ├── MASTER_UNIFIED_ENGLISH.md
│   ├── MASTER_UNIFIED_ENGLISH.mmd
│   ├── MASTER_UNIFIED_ARABIC.md
│   └── MASTER_UNIFIED_ARABIC.mmd
├── final_completeness_check_ar.md
├── QUALITY_REVIEW_AR.md
└── archives/
    └── master_unified_pipeline.zip
```

## How the 8 systems fuse

```
                    ┌─────────────────────────────┐
                    │  0. PROMPT REPORT ROUTER    │
                    │  (technique family select)  │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  1. APE PROMPT OPTIMIZER    │
                    │  (generate / rank prompts)  │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  2. META-PROMPT CONDUCTOR   │
                    │  (decompose + expert call)  │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
     ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
     │ 3. TREE SEARCH │  │ 4. SELF-REFINE │  │ 5. REFLEXION   │
     │ ToT (BFS/DFS)  │  │ (inner polish) │  │ (trial memory) │
     │ + LATS (MCTS)  │  └────────┬───────┘  └────────┬───────┘
     └────────┬───────┘           │                    │
              └────────────────────┼────────────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │  6. AI SCIENTIST v2 STAGES   │
                    │  (progressive pipeline +     │
                    │   multi-seed + writeup +     │
                    │   peer review)               │
                    └──────────────────────────────┘
```

## Reading order

1. `research_summary.md` — why this fusion exists
2. `pattern_extraction.md` — strongest loops / decisions / prompts per system
3. `unified_architecture.md` — full ARSENAL design
4. `deep_dive_task_matrix.md` — phase × function matrix
5. `prompts_complete.md` — master prompt library
6. `python_logic_flow_complete.md` — operational logic
7. `graphs/MASTER_UNIFIED_ENGLISH.md` — English master graph
8. `graphs/MASTER_UNIFIED_ARABIC.md` — Arabic master graph
9. `final_completeness_check_ar.md` — Arabic completeness audit
10. `QUALITY_REVIEW_AR.md` — quality review

## Source extraction repos (all public)

- https://github.com/faresrafat3/ai-scientist-v2-prompts-extraction
- https://github.com/faresrafat3/self-refine-full-extraction
- https://github.com/faresrafat3/reflexion-full-extraction
- https://github.com/faresrafat3/meta-prompting-full-extraction
- https://github.com/faresrafat3/lats-full-extraction
- https://github.com/faresrafat3/ape-full-extraction
- https://github.com/faresrafat3/prompt-report-full-extraction
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions

## Design principles

1. **Router first** — Prompt Report taxonomy chooses the technique family before any heavy loop.
2. **Optimize the instruction** — APE searches for the best task prompt before execution.
3. **Conduct, don't monolith** — Meta-Prompting decomposes work into expert subcalls.
4. **Search when uncertain** — L3 tree search: **ToT** (BFS/DFS deliberate thoughts) as classic baseline; **LATS** (MCTS/UCT + env + reflection) when interactive/long-horizon.
5. **Polish every candidate** — Self-Refine runs an inner feedback/refine loop on drafts.
6. **Remember failures** — Reflexion stores verbal memory across trials.
7. **Stage the pipeline** — AI Scientist v2 progressive stages wrap everything end-to-end with evaluation, writeup, and review.

## Source extraction repos

| System | Extraction repo |
|---|---|
| AI Scientist v2 | https://github.com/faresrafat3/ai-scientist-v2-prompts-extraction |
| Self-Refine | https://github.com/faresrafat3/self-refine-full-extraction |
| Reflexion | https://github.com/faresrafat3/reflexion-full-extraction |
| Meta-Prompting | https://github.com/faresrafat3/meta-prompting-full-extraction |
| Tree of Thoughts | https://github.com/faresrafat3/tot-full-extraction |
| LATS | https://github.com/faresrafat3/lats-full-extraction |
| APE | https://github.com/faresrafat3/ape-full-extraction |
| Prompt Report | https://github.com/faresrafat3/prompt-report-full-extraction |
| Consolidated | https://github.com/faresrafat3/llm-agent-research-extractions |
