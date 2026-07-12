# فحص الاكتمال النهائي — CAMEL

تاريخ: 2026-07-12
المصدر: arXiv:2303.17760v2 NeurIPS 2023 77 pages + github camel-ai/camel 17.4k stars

## التسليمات

| التسليم | الحالة |
|---|---|
| README | ✅ |
| research_summary | ✅ |
| prompts_complete | ✅ |
| python_logic_flow_complete | ✅ |
| python_logic_inventory.json | ✅ |
| deep_dive_task_matrix | ✅ |
| graph_english.md/.mmd | ✅ |
| graph_arabic.md/.mmd | ✅ |
| final_completeness_check_ar | هذا الملف ✅ |
| QUALITY_REVIEW_AR | ⏳ |
| raw_prompt_files | ✅ inception task specifier role assignment PA PU instruction solution loop data generation prompts AI Society termination challenges mitigation |
| raw_data_samples | ✅ trading bot example AI Society role task generation conversation trajectory |
| ZIP | ⏳ |

## تغطية الأوامر

- Preliminary Human Idea Develop trading bot for stock market ✅
- Role Assignment AI Assistant Python Programmer AI User Stock Trader Human Input Task Specifier Specified Task sentiment analysis tool monitor social media positive negative comments particular stock execute trades based sentiment results ✅
- Instruction Input Solution Next request Install necessary Python libraries sentiment analysis stock trading pip install tweepy textblob yfinance Next request Import necessary libraries code import tweepy textblob pandas numpy yfinance Next request ✅
- PA PU system messages A <- F_{PA} U <- F_{PU} F1 F2 large-scale auto-regressive LMs AI user serves as task planner interactive planning feasible steps AI assistant acts as task executor offering solutions executing planned steps providing responses ✅
- Conversation Towards Task-Solving M_t={(I0,S0)...(It,St)} = {(Ii,Si)}|t i=0 Next t+1 AI user U takes history M_t generates I_{t+1} assistant A generates S_{t+1} until termination ✅
- Challenges role flipping assistant repeating instructions flake replies infinite loop messages mitigation inception prompting maintaining consistency human intentions ✅
- Inception Prompting conversational LLM auto-prompting method enables agents to prompt each other solve tasks Role-Playing AI user continuously provides instructions AI assistant for task-solving Save streaming instruction-solution pairs create diverse instructional conversational task-oriented datasets ✅
- Task Specifier prompting LLMs instead relying human inputs For Math Science datasets generated problem topics subtopics problems automatically by prompting LLMs ✅
- Data Generation Prompts AI Society Figure3 Assistant Role Generation Prompt You are helpful assistant that can play many different roles Now please list NUM_ROLES different roles expertise diverse fields Sort alphabetical order No explanation required User Role Generation Prompt Please list NUM_ROLES most common diverse groups internet users occupations Use singular form No explanation Sort alphabetical No explanation required Task Generation Prompt List NUM_TASKS diverse tasks ASSISTANT_ROLE can assist USER_ROLE cooperatively Be concise Be creative Scalable approach series steps prompt LLM generate possible roles assistant and user then range possible tasks collaboration ... Cost grows quadratically length conversation making essential set limit ✅
- Role-Playing for AI Society scalable approach series steps Firstly prompt LLM generate possible roles assistant and user then range possible tasks collaboration between assistant and user roles Methodology focuses studying communicative agents under cooperative settings where they share common interests assistant-user scenario where preliminary idea given at start Agents will conceptualize idea into specific task and complete it autonomously through conversations ✅
- Datasets AI Society conversational task-oriented instruction-following cooperative large Code cooperative coding tasks Math single-turn QA problem topics subtopics problems automatically prompting LLMs Science single-turn QA Misalignment simulation malicious applications demonstrate potential risks unaligned autonomous agent system ✅
- Agent Evaluation 100 tasks AI Society +100 tasks Code random select GPT4 summarization consolidated final solution larger token limit suitable undetectable format fair comparison vs single-shot gpt-3.5-turbo Sample tasks Appendix Human Evaluation present both CAMEL summarized agent solution and gpt-3.5-turbo single-shot solution side-by-side human participants Identity behind each solution not revealed Participants asked vote whether one solution superior other or if equally good Total 453 responses collected Human evaluation only done for AI Society as assessing code harder humans without running code GPT4 Evaluation engage GPT4 agent evaluate effectiveness Model1 CAMEL Agent solution versus Model2 gpt-3.5-turbo single-shot solution each task More specifically prompt GPT4 score decide which solution two solutions is better Results summarized Table1 showcases CAMEL solution outperforms gpt-3.5-turbo single-shot ✅
- Knowledge emergence fine-tuning LLaMA progressively growing datasets generated through framework Additionally evaluate code generation capabilities benchmarking final model on HumanEval and HumanEval+ ✅
- Library open-sourced https://github.com/camel-ai/camel modular functionality implementations various agents examples well-crafted prompts data explorers Hope library serves as ground for future research various areas such as multi-agent systems cooperative AI game theory simulations social analysis AI ethics AI alignment beyond ✅

## الحكم

**مكتمل** يطابق معيار الاستخراجات السابقة
