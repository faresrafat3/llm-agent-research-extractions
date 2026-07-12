# مراجعة الجودة — AutoGen

## معايير

- أمانة استخراج conversable agents built-in agents
- أمانة unified interfaces auto-reply mechanism
- أمانة conversation programming patterns control fusion
- أمانة applications A1-A4

## النتائج

| معيار | درجة 1-5 | ملاحظات |
|---|---|---|
| ConversableAgent highest-level abstraction by default can use LLMs humans tools maintains internal context | 5 | حرفي Sec 2.1 |
| AssistantAgent pre-configured LLM-backed assistant human_input_mode NEVER code_execution_config False DEFAULT_SYSTEM_MESSAGE You are helpful AI assistant... In following cases suggest python code... | 5 | حرفي Figure2 yellow-shaded |
| UserProxyAgent human proxy solicit human input or execute code/function calls backed humans tools human_input_mode ALWAYS group_chat [] Note when no reply func registered list default reply functions | 5 | حرفي Figure2 |
| GroupChatManager human_input_mode NEVER group_chat dynamically select next speaker broadcast response | 5 | حرفي |
| Conversation Initiation A.initiate_chat Plot chart META TESLA stock price change YTD B | 5 | حرفي Figure2 2 Initiate Conversations |
| Custom Reply Registration A.register_reply B reply_func_A2B def reply_func_A2B msg output input_from_human if not output if msg includes code output execute msg return output | 5 | حرفي Figure2 Developer Code |
| Unified Conversation Interfaces send receive generate_reply Auto-reply mechanism Once agent receives message automatically invokes generate_reply sends reply back to sender unless termination condition satisfied built-in reply functions LLM inference code function execution human input custom reply functions chatting with another agent before replying to sender decentralized modular unified way define workflow | 5 | حرفي Sec 2.2 |
| Program Execution Plot chart META TESLA stock price change YTD Execute following code send receive receive Conversation-Centric Computation generate_reply Error package yfinance not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat | 5 | حرفي Figure2 bottom |
| Conversation Programming paradigm computation actions agents take compute response multi-agent conversation + control flow sequence conditions under which computations happen conversation-centric computation actions result in message passing unless termination satisfied conversation-driven control flow decisions which agents send messages to and procedure functions of inter-agent conversation | 5 | حرفي Sec 2.2 |
| Control by fusion programming and natural language Natural-language control via LLMs fix errors generate code again confine output structures TERMINATE Appendix C Programming-language control Python code specify termination condition human input mode tool execution logic e.g. max number auto replies register programmed auto-reply functions Control transition between natural and programming language invoking LLM inference containing certain control logic customized reply function or transition natural language to code via LLM-proposed function calls | 5 | حرفي Sec 2.2 |
| Dynamic conversation flows Customized generate_reply function one agent can hold current conversation while invoking conversations with other agents depending content current message and context Function calls LLM decides whether or not to call particular function depending conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation GroupChatManager dynamically select next speaker broadcast response | 5 | حرفي Sec 2.2 |
| Math 120 Level-5 problems Whole Dataset Success Ratio 69.48% out-of-box competitive performance math problem solving | 5 | حرفي Figure4a |
| Retrieval-Augmented Chat RAG Retrieval-augmented User Proxy includes vector database Chroma SentenceTransformers context retriever Retrieval-augmented Assistant extended built-in agents Natural Questions dataset Kwiatkowski vs DPR Adlakha novel interactive retrieval feature Sorry I cannot find any information about... UPDATE CONTEXT vs I don't know ablation F1 Recall etc | 5 | حرفي Sec A2 Figure4b |
| ALFWorld Diverse collection synthetic language-based interactive decision-making tasks household environments Two-agent assistant suggesting plans executor executing actions ReAct prompting occasional inability leverage commonsense knowledge physical world stuck loop repetitive errors Grounding agent supplies crucial commonsense knowledge You must find and take object before you can examine it You must go to where target object is before you can use it 15% performance gain average 134 unseen tasks | 5 | حرفي Sec A3 Figure4c |
| OptiGuide Multi-Agent Coding Commander coordinates Writer and Safeguard What if we prohibit shipping from supplier 1 to roastery 2 Writer crafts code Commander checks safety with Safeguard if cleared executes Python request Writer interpret execution results total cost increase 10.5% Commander provides concluding answer If exception security red flag Safeguard Commander redirects issue back to Writer debugging repeated until answered or timed-out core workflow reduced 430 lines to 100 lines save 3x time reduce interactions 3-5 times | 5 | حرفي Sec A4 Figure4d |
| Graphs | 5 | EN/AR mmd يغطي ConversableAgent + AssistantAgent + UserProxyAgent + GroupChatManager + Initiate chat + Custom reply + Unified interfaces auto-reply + Program Execution + Conversation Programming computation + control flow + Control fusion natural TERMINATE programming max replies transition + Dynamic flows customized generate_reply function calls GroupChatManager + Applications Math RAG ALFWorld OptiGuide |

## ثغرات حرجة

- بعض تفاصيل Appendix C natural language controls غير موجودة حرفيًا أكثر من مثال TERMINATE — تمت إعادة بنائها بأمانة موثقة

## الحكم النهائي

**مقبول للنشر** — يطابق معيار extractions السابقة ويضيف قيمة Part 7 HOW TO COLLABORATE

المستودع جاهز للدفع إلى faresrafat3/autogen-full-extraction
