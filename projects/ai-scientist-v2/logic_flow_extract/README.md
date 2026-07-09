# AI Scientist v2 — Logic, Flow, Prompt, and Graph Extraction

Source repository: https://github.com/SakanaAI/AI-Scientist-v2

Files in this extraction:

- `python_logic_flow_complete.md` — AST-assisted extraction of logic, functions, classes, loops, conditions, decisions, inputs/outputs, LLM/VLM calls, and I/O for every Python file.
- `python_logic_inventory.json` — machine-readable inventory used to generate the Markdown report.
- `prompts_complete.md` — full prompt extraction and prompt-schema audit.
- `graph_english.mmd` — Mermaid graph in English.
- `graph_arabic.mmd` — Mermaid graph in Arabic.
- `graph_english.md` — previewable Markdown wrapper for the English graph.
- `graph_arabic.md` — previewable Markdown wrapper for the Arabic graph.
- `graph_gap_audit.md` — explicit audit of missing loops, decisions, prompts, and placeholders found when comparing the graph against the code.
- `final_work_review_ar.md` — Arabic final review of the whole extraction work, stages, challenges, operations, fixes, and quality notes.

Note: The graph is intentionally high-level enough to be renderable while still covering the complete end-to-end execution path, major loops, branch decisions, and I/O transitions. The Markdown/JSON inventory contains per-file details.

## Code-checked graph update

The Mermaid graphs were rechecked against the actual Python code. Missing loops and decisions from `launch_scientist_bfts.py`, `AgentManager.run`, `ParallelAgent._select_parallel_nodes`, `_process_node_wrapper`, writeup retries, multi-seed evaluation, plot retries, review selection, and cleanup were added. See `graph_gap_audit.md`.
