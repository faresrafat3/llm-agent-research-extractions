# CAMEL — Python Logic Flow Complete

## 0. Entry point library

```
from camel.ai import ChatAgent
Library open-sourced https://github.com/camel-ai/camel 17.4k stars modular functionality implementations different agents examples well-crafted prompts data explorers
```

## 1. Role-playing Framework logic Figure1

```
Preliminary Human Idea: Develop trading bot for stock market
Human User
Role Assignment: AI Assistant: Python Programmer, AI User: Stock Trader
Human Input
Task Specifier agent: makes task more specific using prompting LLM instead of relying human inputs
Specified Task: Develop trading bot with sentiment analysis tool that can monitor social media platforms for positive or negative comments about particular stock and execute trades based sentiment analysis results
Instruction: Install necessary Python libraries for sentiment analysis and stock trading.
Input: None
Solution: To install necessary Python libraries for sentiment analysis and stock trading we can use pip package installer Python Here libraries need install 1 tweepy for accessing Twitter API 2 textblob for sentiment analysis 3 yfinance for accessing Yahoo Finance API To install libraries open command prompt terminal enter commands pip install tweepy pip install textblob pip install yfinance Next request.
Role Playing Session
Instruction: Import necessary libraries in Python.
Input: None
Solution: Here's code to import libraries: import tweepy from textblob import TextBlob import pandas as pd import numpy as np import yfinance as yf Next request.
```

Idea conceptualized into specific task and complete autonomously through conversations

## 2. AI Assistant-User Role Assignment

After task specification AI assistant role and AI user role will be assigned to user agent and assistant agent correspondingly to complete specified task In practice system message is passed to each agent declaring role PA assistant system prompt/message and PU user system prompt/message System messages passed to agents before conversations start Let F1 and F2 denote two large-scale auto-regressive language models When system message passed to those models respectively we obtain A ← F_{PA} and U ← F_{PU} which are referred to as assistant and user agents respectively In Figure1 AI assistant and AI user assigned roles Python Programmer and Stock Trader at beginning role-playing session respectively AI user serves as task planner engaging interactive planning determine feasible steps for AI assistant to execute Meanwhile AI assistant acts as task executor offering solutions executing planned steps providing responses to AI user

Conversation Towards Task-Solving: After role assignment completed AI assistant A and AI user U will collaborate instruction-following manner accomplish task In assistant-user scenario AI user responsible providing instructions assistant expected respond with solution that fulfills instructions Formally denote user instruction message obtained at time t by It and assistant solution by St Set conversational messages obtained up until time t denoted Equation 1: M_t = {(I0,S0),...,(It,St)} = {(Ii,Si)}|t i=0 At next time step t+1 AI user U takes history M_t and generates I_{t+1} assistant A generates S_{t+1} etc until termination

Challenges: role flipping, assistant repeating instructions, flake replies, infinite loop of messages Need mitigation via inception prompting maintaining consistency human intentions

## 3. Inception Prompting

Definition: conversational LLM auto-prompting method called Inception Prompting which enables agents to prompt each other to solve tasks through Role-Playing AI user continuously provides instructions AI assistant for task-solving This enables save streaming instruction-solution pairs and create diverse instructional conversational task-oriented datasets These datasets can be used analyze behavior capabilities LLMs and for future research fine-tuning LLMs with conversational instructions

Mechanism: AI user continuously provides instructions to AI assistant for task-solving Save streaming instruction-solution pairs create diverse instructional conversational task-oriented datasets

Task Specifier Agent: makes task more specific from preliminary human idea using prompting LLM instead of relying human inputs For Math and Science datasets generated problem topics subtopics problems automatically by prompting LLMs

## 4. Data Generation Prompts AI Society Figure3

Scalable approach data parameters generated using LLM model reduce human involvement generation process Generation prompts for both AI Society dataset summarized figure

Assistant Role Generation Prompt: You are helpful assistant that can play many different roles Now please list <NUM_ROLES> different roles that you can play with your expertise in diverse fields Sort them by alphabetical order No explanation required. Placeholder <NUM_ROLES> e.g. 50

User Role Generation Prompt: Please list <NUM_ROLES> most common and diverse groups of internet users or occupations Use singular form No explanation Sort alphabetical No explanation required

Task Generation Prompt: List <NUM_TASKS> diverse tasks that <ASSISTANT_ROLE> can assist <USER_ROLE> cooperatively to achieve together Be concise Be creative

## 5. Datasets generation flow

- AI Society conversational task-oriented instruction-following cooperative large
- Code cooperative coding tasks code generation capabilities HumanEval HumanEval+
- Math single-turn QA problem topics subtopics problems automatically prompting LLMs
- Science single-turn QA
- Misalignment simulation malicious applications demonstrate potential risks unaligned autonomous agent system

Scalable approach studying cooperative behaviors capabilities multi-agent systems illuminates challenges achieving autonomous cooperation provides strategies addressing them showcase potential power multi-agent collaboration complex-task solving

## 6. Evaluation flow

Agent Evaluation: Assess performance CAMEL Cooperative Role-playing Communication conduct two types evaluations 1 Human evaluation 2 GPT4 evaluation Randomly select 100 tasks from AI Society dataset evaluation and 100 tasks from Code dataset Then employ GPT4 model summarize content CAMEL conversation-based solution presenting consolidated final solution Particularly GPT4 is used since possesses larger token limit suitable summarization Summarization also makes CAMEL agents solution undetectable by its format allowing more fair comparison Subsequently solution compared with single-shot solution generated by gpt-3.5-turbo model same task Sample tasks provided Appendix

Human Evaluation: present both CAMEL summarized agent solution and gpt-3.5-turbo single-shot solution side-by-side human participants Identity behind each solution not revealed Participants then asked vote whether one solution superior other or if equally good Total 453 responses collected during evaluation Note human evaluation only done for AI Society as assessing code generally harder humans without running code

GPT4 Evaluation: engage GPT4 agent evaluate effectiveness Model1 CAMEL Agent solution versus Model2 gpt-3.5-turbo single-shot solution each task More specifically prompt GPT4 score decide which solution two solutions is better

Results summarized Table1 showcases CAMEL solution outperforms gpt-3.5-turbo single-shot etc

Also knowledge emergence fine-tuning LLaMA on progressively growing datasets generated through framework Additionally evaluate code generation capabilities benchmarking final model on HumanEval and HumanEval+

## 7. Decision catalog

| ID | Decision |
|---|---|
| D1 | Use Task Specifier to make preliminary idea more specific vs direct idea |
| D2 | Role Assignment AI Assistant Python Programmer AI User Stock Trader vs other roles generated via prompts alphabetical order |
| D3 | Use PA PU system messages passed before conversations vs no system messages |
| D4 | Inception Prompting AI user continuously provides instructions vs human input every turn |
| D5 | Conversation history M_t formal definition |
| D6 | Termination condition task completed vs max messages limit cost grows quadratically |
| D7 | Generate roles via Assistant Role Generation Prompt |
| D8 | Generate user roles via User Role Generation Prompt |
| D9 | Generate tasks via Task Generation Prompt |
| D10 | For Math and Science datasets generate problem topics subtopics problems automatically by prompting LLMs vs human-curated |
| D11 | Evaluation summarization via GPT4 larger token limit suitable undetectable format fair comparison vs no summarization |
| D12 | Human evaluation side-by-side anonymous vote |
| D13 | GPT4 evaluation score decide which better Model1 vs Model2 |
| D14 | Fine-tune LLaMA progressively growing datasets knowledge emergence |
| D15 | Code evaluation HumanEval HumanEval+ |

## 8. Loop inventory

| Loop | Bound |
|---|---|
| Task specifier | 1 per human idea |
| Role assignment | 1 per task |
| Instruction-solution pairs streaming M_t grows | cost grows quadratically |
| Role-playing session Instruction Input Solution Next request loop | Until termination task completed or max messages limit |
| Role generation list NUM_ROLES different roles alphabetical order |
| User role generation list NUM_ROLES groups internet users occupations |
| Task generation list NUM_TASKS diverse tasks ASSISTANT_ROLE can assist USER_ROLE cooperatively |
| AI Society dataset generation | Number roles * number tasks |
| Math and Science datasets problem topics subtopics problems automatically prompting LLMs |
| Agent evaluation 100 tasks AI Society + 100 tasks Code random select | 200 tasks |
| Human evaluation 453 responses vote | 453 |
| GPT4 evaluation per task | 200 tasks |
| Fine-tuning LLaMA progressively growing datasets |
| HumanEval HumanEval+ benchmarking final model |

## 9. I/O summary

| Stage | Input | Output |
|---|---|---|
| Preliminary Human Idea | Human user idea Develop trading bot for stock market | Idea string |
| Role Assignment | Human idea | AI Assistant Python Programmer AI User Stock Trader roles |
| Task Specifier | Preliminary idea + roles | Specified Task Develop trading bot with sentiment analysis tool |
| Inception Prompting | Specified task + PA PU system messages | PA PU A <- F_{PA} U <- F_{PU} |
| Instruction I0 | History M_t empty + specified task | Instruction: Install necessary Python libraries |
| Solution S0 | Instruction I0 | Solution: pip install tweepy textblob yfinance Next request |
| Loop M_t | History grows | Next It+1 St+1 until termination |
| Role Generation | NUM_ROLES | List roles assistant can play |
| User Role Generation | NUM_ROLES | List user roles |
| Task Generation | NUM_TASKS + ASSISTANT_ROLE + USER_ROLE | List diverse tasks |
| AI Society dataset | Roles + tasks | Large conversational task-oriented dataset |
| Code dataset | Roles + tasks coding | Code dataset |
| Math dataset | Prompting LLMs | Single-turn QA Math |
| Science dataset | Prompting LLMs | Single-turn QA Science |
| Misalignment dataset | Simulation malicious | Misalignment risks |
| Summarization | CAMEL conversation-based solution content | Summarized solution via GPT4 larger token limit |
| Human evaluation | Side-by-side CAMEL summarized vs gpt-3.5-turbo anonymous | Vote superior equally good 453 responses |
| GPT4 evaluation | Model1 CAMEL vs Model2 single-shot per task | Score decide which better |
| Fine-tuning LLaMA | Progressively growing datasets | LLaMA fine-tuned knowledge emergence |
| Code evaluation | Final model | HumanEval HumanEval+ |
