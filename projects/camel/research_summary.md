
# CAMEL — Research Summary

## Identity

- Title: CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society
- ArXiv: 2303.17760v2 Nov 2 2023 NeurIPS 2023 77 pages project website https://www.camel-ai.org/ github https://github.com/camel-ai/camel
- Authors: Guohao Li*, Hasan Abed Al Kader Hammoud*, Hani Itani*, Dmitrii Khizbullin, Bernard Ghanem KAUST *Equal contribution
- Abstract: Rapid advancement chat-based language models remarkable progress complex task-solving heavily relies human input guide conversation challenging time-consuming Explores potential building scalable techniques facilitate autonomous cooperation among communicative agents provides insight into cognitive processes To address challenges achieving autonomous cooperation propose novel communicative agent framework named role-playing Approach involves using inception prompting to guide chat agents toward task completion while maintaining consistency with human intentions Showcase how role-playing can be used to generate conversational data studying behaviors capabilities society of agents providing valuable resource investigating conversational language models In particular conduct comprehensive studies instruction-following cooperation multi-agent settings Contributions introducing novel communicative agent framework offering scalable approach studying cooperative behaviors capabilities multi-agent systems and open-sourcing library: https://github.com/camel-ai/camel
- Contributions fourfold: 1 introduce novel cooperative agent framework role-playing allows communicative agents collaborate autonomously toward completing tasks while requiring minimal human intervention 2 offers scalable approach studying cooperative behaviors capabilities multi-agent systems illuminates challenges achieving autonomous cooperation provides strategies addressing them showcase potential power multi-agent collaboration complex-task solving 3 demonstrate significant emergence LLM training abilities by utilizing datasets collected from simulating four distinct agent collaboration scenarios 4 open-sourced library containing implementations various agents data generation pipelines data analysis tools collected datasets support research communicative agents beyond

## Motivation

- Minsky quote: What magical trick makes us intelligent? Trick is there is no trick Power intelligence stems from our vast diversity not from single perfect principle Society of Mind p308
- Confronted complexities real-world tasks solving often requires multiple steps Rapid progress chat-based LLMs yielded remarkable achievements complex task-solving Nevertheless success heavily reliant human input guide conversation right direction necessitates users provide relevant precise prompts based intentions chat agent feedback Challenging time-consuming sometimes impossible Crafting effective prompts demands deep understanding expertise particular domain knowledge Consider individual lacks trading expertise would find difficult create suitable prompts directing chat agent develop trading application Crucial question: can we replace human intervention with autonomous communicative agent capable steering conversation toward task completion with minimal human supervision? Investigate potential capabilities limitations communicative agents operate entirely on own to complete tasks Understanding how multiple agents interact important anticipating future AI Dynamics collaborating or competing agents key role determining success AI systems
- Explore potential building scalable techniques facilitate autonomous cooperation among communicative agents provide insight cognitive processes Several challenges encountered preliminary analysis include role flipping, assistant repeating instructions, flake replies, infinite loop messages Therefore critical investigate ways align models with human intentions explore means enabling effective cooperation Propose novel cooperative agent framework role-playing automate cooperation between communicative agents Approach involves using role-playing with inception prompting to autonomously guide communicative agents toward task completion Only preliminary idea needed from human guide conversations toward complex task-solving Library provides modular functionality includes implementations different agents examples well-crafted prompts data explorers Hope library serves as ground for future research various areas such as multi-agent systems cooperative AI game theory simulations social analysis AI ethics AI alignment beyond
- Role-playing method provides highly scalable way to generate conversational data studying behaviors capabilities chat agents Showcase how role-playing can be used let chat agents communicate each other task completion record conversations behavior analysis capability understanding In particular consider two cooperative scenarios role-playing generate two large conversational task-oriented instruction-following datasets: AI Society and Code We also use framework collect two single-turn question-answer datasets Math Science for LLM ability emergence study Furthermore generate Misalignment dataset simulation possible malicious applications demonstrate potential risks unaligned autonomous agent system Datasets offer valuable resource investigating conversational language models enabling them comprehend react human language more effectively Furthermore role-playing offers scalable method creating conversational instruction-following data which can potentially enhance development more advanced language models Show solutions derived role-playing framework outperform those generated single shot by gpt-3.5-turbo in both GPT4 and human evaluations Also study knowledge emergence LLMs fine-tuning LLaMA on progressively growing datasets generated through framework Additionally evaluate code generation capabilities benchmarking final model on HumanEval and HumanEval+

## Related Work

- Communicative Agents: Communication between agents studied long time many ways facilitate communication between agents and with agents natural language most natural form By enabling agents function as communicators themselves capable solving complex tasks Communication AI agents can occur competitive setting or cooperative setting Cooperative AI refers systems designed work together with humans other AI systems achieve common goals take into account needs capabilities other agents actively seek collaborate coordinate actions with them potential benefits increased efficiency improved decision-making ability tackle complex problems beyond reach single agent However designing effective cooperative AI systems still active area requires addressing range technical ethical social challenges Our work enables communicative agents engage in conversation cooperate with each other solve assigned tasks Agents each assigned distinct role expected apply their expertise knowledge solve common task
- Instructional LLMs and Prompt Engineering: LLMs trained diverse text data excel text completion various downstream NLP applications InstructGPT suggests LLMs may not align with user intent proposing RLHF and Instruction Fine-Tuning IFT improve relevance appropriateness Special types instruction prompting methods such Chain-of-Thought CoT zero-shot-CoT ReAct developed enhance performance LLMs reasoning arithmetic decision making etc techniques underpin impressive capabilities recent...
- Automated prompt generation methods proposed gradient-guided search mining-based paraphrasing-based techniques meta-prompt automatic instruction selection generation In this work introduce conversational LLM auto-prompting method called Inception Prompting which enables agents to prompt each other to solve tasks through Role-Playing AI user continuously provides instructions AI assistant for task-solving This enables save streaming instruction-solution pairs create diverse instructional conversational task-oriented datasets These datasets can be used analyze behavior capabilities LLMs and for future research fine-tuning LLMs with conversational instructions
- AI Alignment field aims ensure AI systems adhere intended goals interests values envisioned designers First attempt Three Laws Robotics Asimov Developing aligned AI systems crucial achieving desired objectives while avoiding unintended consequences Research focuses discouraging AI models producing false offensive deceptive manipulative information that could result various harms Achieving high level alignment requires grapple complex ethical philosophical technical issues Conduct extensive experiments study different role-playing situations which probe alignment LLMs

## Methodology — Role-playing Framework

Quote: What's most resilient parasite? An Idea. Single idea from human mind can build cities Idea can transform world rewrite all rules Which is why I have to steal it. - Dom Cobb Inception

Flow Figure1:

Idea: Develop trading bot for stock market
Human User
Role Assignment: AI Assistant: Python Programmer, AI User: Stock Trader
Human Input
Task Specifier
AI Assistant
AI User
Specified Task: Develop trading bot with sentiment analysis tool that can monitor social media platforms for positive or negative comments about particular stock and execute trades based sentiment analysis results
Instruction: Install necessary Python libraries for sentiment analysis and stock trading.
Input: None
Solution: To install necessary Python libraries for sentiment analysis and stock trading we can use pip package installer Python Here libraries need install 1 tweepy for accessing Twitter API 2 textblob for sentiment analysis 3 yfinance for accessing Yahoo Finance API To install libraries open command prompt terminal enter commands pip install tweepy pip install textblob pip install yfinance Next request.
Role Playing Session
Instruction: Import necessary libraries in Python.
Input: None
Solution: Here's code to import libraries: import tweepy from textblob import TextBlob import pandas as pd import numpy as np import yfinance as yf Next request.

- Idea conceptualized into specific task and complete it autonomously through conversations

### AI Assistant-User Role Assignment

After task specification AI assistant role and AI user role will be assigned to user agent and assistant agent correspondingly to complete specified task In practice system message is passed to each agent declaring their role We refer to assistant system prompt/message by PA and that of user by PU System messages passed to agents before conversations start Let F1 and F2 denote two large-scale auto-regressive language models When system message passed to those models respectively we obtain A ← F_{PA} and U ← F_{PU} which are referred to as assistant and user agents respectively In Figure1 AI assistant and AI user assigned roles Python Programmer and Stock Trader at beginning role-playing session respectively AI user serves as task planner engaging interactive planning determine feasible steps for AI assistant to execute Meanwhile AI assistant acts as task executor offering solutions executing planned steps providing responses to AI user

### Conversation Towards Task-Solving

After role assignment completed AI assistant A and AI user U will collaborate instruction-following manner accomplish task In assistant-user scenario AI user responsible providing instructions assistant expected respond with solution that fulfills instructions Formally denote user instruction message obtained at time t by It and assistant solution by St Set conversational messages obtained up until time t denoted Equation 1: M_t = {(I0,S0),...,(It,St)} = {(Ii,Si)}|t i=0 At next time step t+1 AI user U takes history M_t and generates I_{t+1} assistant A generates S_{t+1} etc until termination

Challenges encountered: role flipping, assistant repeating instructions, flake replies, infinite loop of messages Need mitigation via inception prompting maintaining consistency human intentions

### Inception Prompting

Introduction: implicitly learn tasks with few-shot prompting hand-crafted prompts may not always suffice Automated prompt generation methods proposed gradient-guided search mining-based paraphrasing-based techniques meta-prompt automatic instruction selection generation In this work introduce conversational LLM auto-prompting method called Inception Prompting which enables agents to prompt each other to solve tasks through Role-Playing AI user continuously provides instructions AI assistant for task-solving This enables save streaming instruction-solution pairs create diverse instructional conversational task-oriented datasets

Mechanism: AI user continuously provides instructions to AI assistant for task-solving Save streaming instruction-solution pairs create diverse instructional conversational task-oriented datasets Datasets can be used analyze behavior capabilities LLMs and for future research fine-tuning LLMs with conversational instructions

Task Specifier Agent: makes task more specific from preliminary human idea using prompting LLM instead of relying human inputs For Math and Science datasets generated problem topics subtopics problems automatically by prompting LLMs

AI Assistant-User Role Assignment After task specification AI assistant role and AI user role will be assigned to user agent and assistant agent correspondingly to complete specified task In practice system message is passed to each agent declaring their role ... etc

### Data Generation Prompts AI Society Figure3

- Assistant Role Generation Prompt: You are helpful assistant that can play many different roles Now please list <NUM_ROLES> different roles that you can play with your expertise in diverse fields Sort them by alphabetical order No explanation required.

- User Role Generation Prompt: Please list <NUM_ROLES> most common and diverse groups of internet users or occupations Use singular form No explanation Sort alphabetical No explanation required.

- Task Generation Prompt: List <NUM_TASKS> diverse tasks that <ASSISTANT_ROLE> can assist <USER_ROLE> cooperatively to achieve together Be concise Be creative.

In order maintain scalable approach data parameters generated using LLM model reduce human involvement generation process Generation prompts for both AI Society dataset summarized figure

### Role-Playing for AI Society

Create AI Society dataset scalable approach series steps Firstly prompt LLM agent generate possible roles assistant and user We achieve this by providing LLM agent specific prompts designed elicit these roles Next ask LLM agent generate range possible tasks that can be solved through collaboration between assistant and user roles g...

Methodology focuses studying communicative agents under cooperative settings where they share common interests In particular study assistant-user scenario where preliminary idea given at start Agents will conceptualize idea into specific task and complete it autonomously through conversations

Cost grows quadratically with length conversation making essential set limit

## Evaluation

### Agent Evaluation

Assess performance CAMEL Cooperative Role-playing Communication conduct two types evaluations 1 Human evaluation 2 GPT4 evaluation Randomly select 100 tasks from AI Society dataset evaluation and 100 tasks from Code dataset Then employ GPT4 model summarize content CAMEL conversation-based solution presenting consolidated final solution Particularly GPT4 is used since possesses larger token limit suitable summarization Summarization also makes CAMEL agents solution undetectable by its format allowing more fair comparison Subsequently solution compared with single-shot solution generated by gpt-3.5-turbo model same task Sample tasks provided Appendix

Human Evaluation For evaluation present both CAMEL summarized agent solution and gpt-3.5-turbo single-shot solution side-by-side human participants Identity behind each solution not revealed Participants then asked vote whether one solution superior to other or if equally good Total 453 responses collected during evaluation Note human evaluation only done for AI Society as assessing code generally harder humans without running code

GPT4 Evaluation Engage GPT4 agent evaluate effectiveness Model1 CAMEL Agent solution versus Model2 gpt-3.5-turbo single-shot solution each task More specifically prompt GPT4 score decide which solution two solutions is better

Results summarized Table1 showcases CAMEL solution outperforms gpt-3.5-turbo single-shot etc

Also knowledge emergence fine-tuning LLaMA on progressively growing datasets generated through framework Additionally evaluate code generation capabilities benchmarking final model on HumanEval and HumanEval+

Contributions fourfold...

### Datasets

- AI Society conversational task-oriented instruction-following cooperative
- Code cooperative coding tasks
- Math single-turn QA problem topics subtopics problems automatically prompting LLMs
- Science single-turn QA
- Misalignment simulation malicious applications demonstrate potential risks unaligned autonomous agent system

Scalable approach studying cooperative behaviors capabilities multi-agent systems illuminates challenges achieving autonomous cooperation provides strategies addressing them showcase potential power multi-agent collaboration complex-task solving

## Library

Open-sourced library https://github.com/camel-ai/camel containing implementations various agents data generation pipelines data analysis tools collected datasets support research communicative agents beyond modular functionality includes implementations different agents examples well-crafted prompts data explorers Hope library serves as ground for future research various areas such as multi-agent systems cooperative AI game theory simulations social analysis AI ethics AI alignment beyond

## Relation to other systems

- Provides role-playing framework inception prompting minimal human intervention single preliminary idea vs AutoGen customizable conversable agents various modes combinations LLMs human inputs tools flexible definition agent interaction behaviors both natural language and computer code can be used program flexible conversation patterns
- Feeds Scientific Intelligence Survey P5 Role-Interactive Multi-Agent distributed planning collaborative dialogue planner proposes critic identifies flaws executor provides feasibility feedback mirrors scientific team dynamics iterative discussion consensus-building tournament-style debate etc vs CAMEL assistant-user scenario task planner task executor instruction-following manner
- STORM perspective-guided question asking multi-perspective editors vs CAMEL different roles diverse fields alphabetical order
- GAPMAP gap identification → CAMEL task specifier making specific
- ResearchAgent ReviewingAgents reviewing feedback rating 1-5 vs CAMEL AI user providing instructions AI assistant solutions
- For CONSTITUTION Part7 HOW TO COLLABORATE: inception prompting + role assignment PA PU + instruction-solution loop Mt + task specifier making specific + termination + challenges mitigation role flipping repeating instructions flake replies infinite loop
