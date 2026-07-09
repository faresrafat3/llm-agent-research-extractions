# Consolidated Deep Dive Matrix

| System | Core loop | Memory/history | Tool use | Main outputs | Project folder |
|---|---|---|---|---|---|
| AI Scientist v2 | staged BFTS: draft/debug/improve/tune/ablate → execute → evaluate → write | journal nodes, summaries, stage history | Python execution, Semantic Scholar, VLM, LaTeX, plotting | experiments, figures, citations, paper, reviews | `projects/ai-scientist-v2/` |
| Self-Refine | generate → feedback → refine → stop | previous outputs and feedback history | optional GPT-4V/TikZ notebook, task-specific evaluators | refined text/code/answers/logs | `projects/self-refine/` |
| Reflexion | attempt → feedback → reflection → memory → retry | episodic reflection memory | environments, search, executors, tests | improved task success/code/answers | `projects/reflexion/` |
| Meta-Prompting | meta model → expert call → expert output → append feedback → final answer | message history | Expert Python code execution, expert/summarizer calls | final answers, expert transcripts, evaluations | `projects/meta-prompting/` |

## Reading strategy

For each project:

1. read `README.md`,
2. read `research_summary.md`,
3. inspect `deep_dive_task_matrix.md`,
4. inspect `prompts_complete.md`,
5. inspect `python_logic_flow_complete.md`,
6. render or read English/Arabic Mermaid graphs,
7. finish with Arabic completeness and quality reviews.
