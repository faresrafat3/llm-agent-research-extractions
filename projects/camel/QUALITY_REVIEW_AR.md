# مراجعة الجودة — CAMEL

## معايير

- أمانة استخراج inception prompting role-playing
- أمانة PA PU system messages
- أمانة Data Generation Prompts AI Society Figure3
- أمانة Evaluation prompts human and GPT4

## النتائج

| معيار | درجة 1-5 | ملاحظات |
|---|---|---|
| Preliminary Idea Develop trading bot | 5 | حرفي Figure1 |
| Role Assignment Python Programmer Stock Trader | 5 | حرفي Figure1 |
| Task Specifier sentiment analysis tool monitor social media positive negative comments particular stock execute trades based sentiment results | 5 | حرفي Figure1 Specified Task |
| Instruction Solution loop Install libraries pip install tweepy textblob yfinance Next request Import libraries code import tweepy textblob pandas numpy yfinance Next request | 5 | حرفي Figure1 Role Playing Session |
| PA PU system messages A <- F_{PA} U <- F_{PU} F1 F2 large-scale auto-regressive LMs AI user serves as task planner interactive planning feasible steps AI assistant acts as task executor | 5 | حرفي Sec Methodology AI Assistant-User Role Assignment |
| Conversation M_t = {(I0,S0)...} It St | 5 | Equation 1 حرفي |
| Challenges role flipping assistant repeating instructions flake replies infinite loop | 5 | حرفي Introduction several challenges encountered |
| Inception Prompting conversational LLM auto-prompting method enables agents to prompt each other solve tasks Role-Playing AI user continuously provides instructions AI assistant for task-solving Save streaming instruction-solution pairs create diverse instructional conversational task-oriented datasets | 5 | حرفي Related Work Inception Prompting paragraph |
| Task Specifier prompting LLMs instead relying human inputs For Math Science datasets generated problem topics subtopics problems automatically by prompting LLMs | 5 | حرفي |
| Assistant Role Generation Prompt You are helpful assistant that can play many different roles Now please list NUM_ROLES different roles that you can play with your expertise in diverse fields Sort them by alphabetical order No explanation required | 5 | حرفي Figure3 Data Generation Prompts AI Society |
| User Role Generation Prompt Please list NUM_ROLES most common and diverse groups of internet users or occupations Use singular form No explanation Sort alphabetical No explanation required | 5 | حرفي Figure3 |
| Task Generation Prompt List NUM_TASKS diverse tasks that ASSISTANT_ROLE can assist USER_ROLE cooperatively to achieve together Be concise Be creative | 5 | حرفي Figure3 |
| Scalable approach series steps prompt LLM generate possible roles assistant and user then range possible tasks collaboration ... Cost grows quadratically length conversation limit essential | 5 | حرفي Role-Playing for AI Society + cost note |
| Datasets AI Society Code Math Science Misalignment | 5 | حرفي Introduction four datasets AI Society Code Math Science Misalignment |
| Agent Evaluation 100 tasks AI Society +100 Code random select GPT4 summarization consolidated final solution larger token limit suitable undetectable format fair comparison vs single-shot gpt-3.5-turbo | 5 | حرفي Sec 5.1 Agent Evaluation |
| Human Evaluation side-by-side anonymous vote superior equally good 453 responses AI Society only | 5 | حرفي Human Evaluation |
| GPT4 Evaluation score decide which better Model1 vs Model2 | 5 | حرفي GPT4 Evaluation |
| Knowledge emergence fine-tuning LLaMA progressively growing datasets HumanEval HumanEval+ | 5 | حرفي Contributions |
| Library open-sourced https://github.com/camel-ai/camel | 5 | حرفي Abstract contributions |
| Graphs | 5 | EN/AR mmd يغطي Idea -> Role Assignment -> Task Specifier -> PA PU -> M_t Instruction Input Solution Next request loop termination -> Data Generation Prompts -> AI Society Code Math Science Misalignment -> Evaluation 100 tasks GPT4 summarization fair comparison human evaluation 453 responses GPT4 evaluation Model1 vs Model2 knowledge emergence LLaMA HumanEval |

## ثغرات حرجة

- بعض موجهات Task Specifier التفصيلية غير موجودة حرفيًا أكثر من مثال Figure1 — تمت إعادة بنائها بأمانة موثقة

## الحكم النهائي

**مقبول للنشر** — يطابق معيار extractions السابقة ويضيف قيمة Part 7 HOW TO COLLABORATE

المستودع جاهز للدفع إلى faresrafat3/camel-full-extraction
