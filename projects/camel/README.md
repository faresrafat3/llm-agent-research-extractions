# CAMEL — Full Prompt, Logic, Flow, and Graph Extraction

Paper: **CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society**  
ArXiv: https://arxiv.org/abs/2303.17760 (NeurIPS 2023, 77 pages)  
Code: https://github.com/camel-ai/camel (17.4k stars, 2k forks)  
Website: https://www.camel-ai.org  
Audited commit: master Jul 10 2026 (147d926)

## Why this package

CAMEL proposes **role-playing framework** with **inception prompting** to enable autonomous cooperation among communicative agents with minimal human supervision. Only a preliminary human idea needed (e.g., Develop a trading bot for the stock market), then task specifier makes it specific, role assignment assigns AI Assistant (e.g., Python Programmer) and AI User (e.g., Stock Trader) and they collaborate via instruction-following conversations until task completion.

Key innovations:

1. **Inception Prompting** — auto-prompting method where AI user continuously provides instructions to AI assistant for task-solving, saving streaming instruction-solution pairs creating diverse, instructional, conversational, task-oriented datasets. Addresses challenges like role flipping, assistant repeating instructions, flake replies, infinite loop of messages.
2. **Role-Playing Setup** — AI assistant-user scenario, preliminary idea conceptualized into specific task autonomously through conversations. Assistant role prompt PA and user role prompt PU system messages passed before conversation. User acts as task planner, assistant as task executor offering solutions, executing planned steps, providing responses.
3. **Scalable Data Generation** — Generates conversational task-oriented instruction-following datasets: AI Society and Code (cooperative scenarios), Math and Science (single-turn QA emergent abilities), Misalignment (malicious applications risks). Enables studying cooperative behaviors, capabilities, probing alignment.
4. **Modular Library** — Implementations different agents, examples well-crafted prompts, data explorers. Supports future research multi-agent systems, cooperative AI, game theory simulations, social analysis, AI ethics, alignment.

This extraction feeds CONSTITUTION Part 7 HOW TO COLLABORATE multi-agent patterns.

## Package contents

```text
camel-full-extraction/
├── README.md
├── research_summary.md
├── prompts_complete.md
├── python_logic_flow_complete.md
├── python_logic_inventory.json
├── deep_dive_task_matrix.md
├── graph_english.md/.mmd
├── graph_arabic.md/.mmd
├── final_completeness_check_ar.md
├── QUALITY_REVIEW_AR.md
├── raw_prompt_files/
│   ├── inception_prompting_task_specifier.txt
│   ├── role_assignment_PA_PU.txt
│   ├── AI_user_instruction_loop.txt
│   ├── AI_assistant_solution_loop.txt
│   ├── data_generation_prompts_AI_Society.txt
│   ├── termination_conditions.txt
│   └── challenges_mitigation.txt
├── raw_data_samples/
│   ├── trading_bot_example.json
│   ├── AI_Society_role_task_generation.json
│   └── conversation_trajectory.json
└── archives/camel_full_extract.zip
```

## Tasks / Datasets generated

| Dataset | Scenario | Size / Purpose |
|---|---|---|
| AI Society | Cooperative role-playing assistant-user diverse roles tasks | Large conversational task-oriented instruction-following for behavior analysis |
| Code | Cooperative coding tasks | Code generation capabilities HumanEval HumanEval+ |
| Math | Single-turn QA emergent ability | Problem topics subtopics problems automatically prompting LLMs |
| Science | Single-turn QA | Same as Math |
| Misalignment | Simulation malicious applications | Demonstrate potential risks unaligned autonomous agent system |

## Roles / Agents

- Human User (preliminary idea) → Task Specifier agent → Specified Task
- AI User: Stock Trader, task planner, interactive planning feasible steps
- AI Assistant: Python Programmer, task executor, solutions, executing steps, responses
- Task Specifier: makes task more specific (e.g., Develop trading bot with sentiment analysis tool monitor social media platforms positive/negative comments particular stock execute trades based sentiment results)
- Role Assignment: PA assistant system message, PU user system message, passed before conversation, models F1, F2 large-scale auto-regressive LMs -> A ← F_{PA}, U ← F_{PU}
- Challenges: role flipping, assistant repeating instructions, flake replies, infinite loop of messages

## Conversation flow

```
Idea: Develop trading bot
Human User
Role Assignment: AI Assistant: Python Programmer, AI User: Stock Trader
Human Input → Task Specifier → Specified Task: Develop trading bot with sentiment analysis tool...
Instruction: Install necessary Python libraries for sentiment analysis and stock trading.
Input: None
Solution: To install necessary Python libraries... pip install tweepy textblob yfinance Next request.
Role Playing Session
Instruction: Import necessary libraries in Python.
Input: None
Solution: code import tweepy... Next request.
...
```

Conversation: M_t = {(I0,S0),...,(It,St)} = {(Ii,Si)}|t i=0
Next time t+1, AI user U takes history Mt and generates It+1, assistant A generates St+1, etc until termination.

## Evaluation

- Agent Evaluation: 100 tasks AI Society + 100 tasks Code, GPT4 summarization consolidated final solution (larger token limit suitable summarization, undetectable by format fair comparison) vs single-shot gpt-3.5-turbo same task. Human evaluation 453 responses AI Society only (assessing code harder without running), side-by-side vote superior equally good identity not revealed. GPT4 evaluation GPT4 agent score decide which solution better Model1 CAMEL vs Model2 gpt-3.5-turbo single-shot. Results: CAMEL outperforms gpt-3.5-turbo single-shot in both GPT4 and human evaluations. Also knowledge emergence fine-tuning LLaMA on progressively growing datasets generated through framework, code generation benchmarking HumanEval and HumanEval+.

## Recommended reading order

1. research_summary.md
2. deep_dive_task_matrix.md
3. prompts_complete.md
4. python_logic_flow_complete.md
5. graph_english.md / graph_arabic.md

## Related

- AutoGen conversational framework: https://github.com/faresrafat3/autogen-full-extraction
- STORM perspective-guided question asking multi-perspective editors vs CAMEL role-playing assistant-user
- SciMON iterative novelty boosting vs CAMEL task specifier making specific
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions
- ARSENAL: https://github.com/faresrafat3/arsenal-unified-master-pipeline
