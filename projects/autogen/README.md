# AutoGen — Full Prompt, Logic, Flow, and Graph Extraction

Paper: **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**  
ArXiv: https://arxiv.org/abs/2308.08155 (v2 Oct 3 2023, 43 pages, 10 main + 3 refs + 30 appendices)  
Code: https://github.com/microsoft/autogen (59.7k stars, 9k forks, 3782 commits, 209 branches, 128 tags)  
Authors: Qingyun Wu et al Microsoft

## Why this package

AutoGen is open-source framework that allows developers to build LLM applications via multiple agents that can converse with each other to accomplish tasks. AutoGen agents are customizable, conversable, and can operate in various modes that employ combinations of LLMs, human inputs, and tools. Using AutoGen, developers can also flexibly define agent interaction behaviors. Both natural language and computer code can be used to program flexible conversation patterns for different applications. AutoGen serves as generic infrastructure to build diverse applications of various complexities and LLM capacities. Empirical studies demonstrate effectiveness in many example applications domains ranging mathematics, coding, question answering, operations research, online decision-making, entertainment, etc.

Key innovations:

1. **Conversable Agents**: entity with specific role that can pass messages to send and receive information to and from other conversable agents to start or continue conversation. Maintains internal context based on sent and received messages and can be configured to possess set of capabilities enabled by LLMs, tools, or human input. Capabilities directly influence how it processes and responds to messages. Supports many common composable capabilities: 1) LLMs. LLM-backed agents exploit many capabilities advanced LLMs such as role playing, implicit state inference and progress making conditioned on conversation history, providing feedback, adapting from feedback, coding. Capabilities combined different ways via novel prompting techniques to increase skill and autonomy. Enhanced LLM inference features such as result caching, error handling, message templating etc via enhanced LLM inference layer. 2) Humans. Human involvement desired or essential many LLM applications. Allows human participate in agent conversation via human-backed agents which could solicit human inputs at certain rounds conversation depending agent configuration. Default user proxy agent allows configurable human_input_mode frequency and conditions for requesting human input including option humans skip providing input. 3) Tools. Tool-backed agents capability execute tools via code execution or function execution. For example default user proxy agent able execute code suggested by LLMs or make LLM-suggested function calls.

2. **Agent Customization and Cooperation**: Based on application-specific needs each agent can be configured to have mix of basic back-end types to display complex behavior in multi-agent conversations. Allows easy creation of agents with specialized capabilities and roles by reusing or extending built-in agents. ConversableAgent class highest-level agent abstraction and by default can use LLMs, humans, and tools. AssistantAgent and UserProxyAgent two pre-configured ConversableAgent subclasses each representing common usage mode i.e. acting as AI assistant backed by LLMs and acting as human proxy to solicit human input or execute code/function calls backed by humans and/or tools. In example right-hand side Figure1 LLM-backed assistant agent and tool- and human-backed user proxy agent deployed together tackle task. Here assistant agent generates solution with help LLMs and passes solution to user proxy agent. Then user proxy agent solicits human inputs or executes assistant's code and passes results as feedback back to assistant.

3. **Conversation Programming**: paradigm that considers two concepts: computation – actions agents take to compute their response in multi-agent conversation. And control flow – sequence or conditions under which these computations happen. Ability program these helps implement many flexible multi-agent conversation patterns. Computations are conversation-centric. Agent takes actions relevant to conversations it is involved in and actions result in message passing for consequent conversations unless termination condition satisfied. Similarly control flow is conversation-driven – participating agents decisions on which agents to send messages to and procedure of computation are functions of inter-agent conversation. This paradigm helps reason intuitively about complex workflow as agent action taking and conversation message-passing between agents. Figure2 provides simple illustration bottom sub-figure shows how individual agents perform role-specific conversation-centric computations generate responses e.g. via LLM inference calls and code execution Task progresses through conversations displayed dialog box. Middle sub-figure demonstrates conversation-based control flow When assistant receives message user proxy agent typically sends human input as reply If no input it executes any code in assistant's message instead.

4. **Design Patterns to Facilitate Conversation Programming**:
- Unified interfaces and auto-reply mechanisms for automated agent chat. Agents have unified conversation interfaces for performing corresponding conversation-centric computation including send/receive function for sending/receiving messages and generate_reply function for taking actions and generating response based on received message. AutoGen also introduces and by default adopts agent auto-reply mechanism to realize conversation-driven control: Once agent receives message from another agent it automatically invokes generate_reply and sends reply back to sender unless termination condition satisfied. Provides built-in reply functions based on LLM inference code or function execution or human input. One can also register custom reply functions to customize behavior pattern of agent e.g. chatting with another agent before replying to sender agent. Under this mechanism once reply functions registered and conversation is initialized conversation flow naturally induced and thus agent conversation proceeds naturally without any extra control plane i.e. special module that controls conversation flow. For example with developer code blue-shaded area marked Developer Code of Figure2 one can readily trigger conversation among agents and conversation would proceed automatically as shown dialog box grey shaded area marked Program Execution of Figure2. Auto-reply mechanism provides decentralized modular unified way define workflow.
- Control by fusion of programming and natural language. Allows usage programming and natural language in various control flow management patterns: 1) Natural-language control via LLMs. One can control conversation flow by prompting LLM-backed agents with natural language. For instance default system message of built-in AssistantAgent in AutoGen uses natural language to instruct agent to fix errors and generate code again if previous result indicates errors. It also guides agent to confine LLM output to certain structures making it easier for other tool-backed agents to consume. For example instructing agent to reply with TERMINATE when all tasks completed to terminate program. More concrete examples natural language controls can be found Appendix C. 2) Programming-language control. Python code can be used specify termination condition human input mode tool execution logic e.g. max number auto replies One can also register programmed auto-reply functions control conversation flow with Python code as shown code block identified as Conversation-Driven Control Flow in Figure2. 3) Control transition between natural and programming language. Supports flexible control transition between natural and programming language. One can achieve transition from code to natural-language control by invoking LLM inference containing certain control logic in customized reply function or transition from natural language to code control via LLM-proposed function calls.

- In conversation programming paradigm one can realize multi-agent conversations diverse patterns. In addition to static conversation with predefined flow AutoGen also supports dynamic conversation flows with multiple agents. Provides two general ways: 1) Customized generate_reply function: within customized generate_reply function one agent can hold current conversation while invoking conversations with other agents depending content current message and context. 2) Function calls: In this approach LLM decides whether or not to call particular function depending conversation status. By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation. In addition AutoGen supports more complex dynamic group chat via built-in GroupChatManager which can dynamically select next speaker and then broadcast its response to other agents. Elaborates feature and application in Section 3. Working systems showcase all these different patterns

This extraction feeds CONSTITUTION Part 7 HOW TO COLLABORATE multi-agent patterns.

## Package contents

```text
autogen-full-extraction/
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
│   ├── conversable_agent_spec.txt
│   ├── assistant_agent_system_message.txt
│   ├── user_proxy_agent_human_input_mode.txt
│   ├── group_chat_manager.txt
│   ├── conversation_programming_patterns.txt
│   ├── natural_language_control_TERMINATE.txt
│   ├── programming_language_control_max_replies.txt
│   ├── custom_reply_function_example.txt
│   ├── two_agent_mathy_example.txt
│   ├── retrieval_augmented_chat_RAG.txt
│   ├── ALFWorld_two_agent_plus_grounding.txt
│   └── OptiGuide_Commander_Writer_Safeguard.txt
├── raw_data_samples/
│   ├── two_agent_code_example.json
│   ├── group_chat_example.json
│   └── RAG_interactive_retrieval_UPDATE_CONTEXT.json
└── archives/autogen_full_extract.zip
```

## Modes / Built-in Agents Figure2 yellow-shaded

- ConversableAgent class highest-level agent abstraction by default can use LLMs, humans, tools
- AssistantAgent: LLM-backed assistant act as AI assistant human_input_mode=NEVER code_execution_config=False DEFAULT_SYSTEM_MESSAGE="You are a helpful AI assistant... In the following cases, suggest python code..."
- UserProxyAgent: human proxy solicits human input or executes code/function calls backed by humans and/or tools human_input_mode=ALWAYS
- GroupChatManager: human_input_mode=NEVER group_chat=[] when no reply func registered list default reply functions will be used Agent customization

## Conversation Initiation Example Figure2

```python
# 1. Define Agents
# 2. Initiate Conversations: A.initiate_chat("Plot a chart of META and TESLA stock price change YTD.", B)
# Assistant B User Proxy A AutoGen Agents Developer Code # This func will be invoked in generate_reply A.register_reply(B, reply_func_A2B) def reply_func_A2B(msg): output = input_from_human() ... if not output: if msg includes code: output = execute(msg) return output
# Unified Conversation Interfaces: send receive generate_reply
# Conversation-Centric Computation generate_reply Error: package yfinance is not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply The Resulting Automated Agent Chat: ...
# 1.2 Register Custom Reply Func 1.1 Define Agents
```

Task progresses through conversations displayed dialog box. Middle sub-figure demonstrates conversation-based control flow When assistant receives message user proxy agent typically sends human input as reply If no input it executes any code in assistant's message instead.

Bottom sub-figure automated agent chat: Program Execution Plot chart META and TESLA stock price change YTD Execute following code... send receive receive Conversation-Centric Computation generate_reply Error package yfinance not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat...

## Applications A1-A4 Figure4

- A1 Math: 120 Level-5 problems Whole Dataset AutoGen vs ChatGPT+Code ChatGPT+Plugin GPT-4 Multi-Agent Debate LangChain ReAct etc AutoGen agents can be used out of box achieve most competitive performance math problem solving tasks Success Ratio 69.48% Whole Dataset 55.18% Average etc? Actually figure 4a Performance on MATH w/ GPT-4
- A2 Retrieval-Augmented Chat RAG: system consists two agents Retrieval-augmented User Proxy agent and Retrieval-augmented Assistant agent both extended from built-in agents Retrieval-augmented User Proxy includes vector database Chroma with SentenceTransformers Reimers & Gurevych context retriever detailed workflow Appendix D Evaluation natural question answering Natural Questions dataset Kwiatkowski et al 2019 report results Figure4b compare system with DPR Dense Passage Retrieval following existing evaluation practice Adlakha et al 2023 Leveraging conversational design natural-language control AutoGen introduces novel interactive retrieval feature: whenever retrieved context does not contain information instead terminating LLM-based assistant would reply Sorry, I cannot find any information about... UPDATE CONTEXT which will invoke more retrieval attempts Conduct ablation study prompt assistant agent say I don't know instead of UPDATE CONTEXT in cases relevant information not found report results Figure4b results show interactive retrieval mechanism indeed plays non-trivial role process Concrete example results using appealing feature Appendix D Scenario 2 further demonstrate how Retrieval-augmented Chat aids generating code based given codebase that contains code not included GPT-4 training data Evaluation demonstration details both scenarios Appendix D Metrics F1 Recall 25.88% 66.65% 15.12% 58.56% 22.79% 62.59% AutoGen AutoGen W/O interactive retrieval DPR etc
- A3 ALFWorld: Diverse collection synthetic language-based interactive decision-making tasks household environments Two-agent system LLM-backed assistant agent responsible suggesting plans conduct task and executor agent responsible executing actions ALFWorld environments integrates ReAct prompting Yao et al 2022 able achieve similar performance Common challenge encountered both ReAct and AutoGen-based two-agent system occasional inability leverage basic commonsense knowledge about physical world Deficiency can lead system getting stuck loop due repetitive errors Fortunately modular design AutoGen allows address issue effectively: With AutoGen able introduce grounding agent which supplies crucial commonsense knowledge such as You must find and take the object before you can examine it. You must go to where target object is before you can use it. whenever system exhibits early signs recurring errors Significantly enhances ability avoid getting entangled error loops Compare task-solving performance two variants our system with GPT-3.5-turbo and ReAct on 134 unseen tasks ALFWorld report results Figure4c results show introducing grounding agent could bring 15% performance gain average Upon examining systems outputs observe grounding agent by delivering background commonsense knowledge right junctures significantly mitigated tendency system persist flawed plan thereby avoiding creation error loops Example trajectory comparing systems Appendix D Figure10 Metrics 69% 54% 54% 77% 63% 66% Average Best of 3 AutoGen 3 agent AutoGen 2 agent ReAct
- A4 Multi-Agent Coding OptiGuide: System excels writing code interpret optimization solutions answer user questions such exploring implications changing supply-chain decision or understanding why optimizer made particular choice Second sub-figure Figure3 shows AutoGen-based implementation Workflow: end user sends questions such What if we prohibit shipping from supplier 1 to roastery 2? to Commander agent Commander coordinates with two assistant agents including Writer and Safeguard to answer question Writer will craft code and send code to Commander After receiving code Commander checks code safety with Safeguard if cleared Commander will use external tools e.g. Python to execute code and request Writer to interpret execution results For instance writer may say if we prohibit shipping from supplier 1 to roastery 2 total cost would increase by 10.5% Commander then provides this concluding answer to end user If at particular step there is exception e.g. security red flag raised by Safeguard Commander redirects issue back to Writer with debugging information Process might be repeated multiple times until user's question answered or timed-out With AutoGen core workflow code for OptiGuide reduced from over 430 lines to 100 lines leading significant productivity improvement Provide detailed comparison user experience ChatGPT+Code Interpreter and AutoGen-based OptiGuide Appendix D where show AutoGen-based OptiGuide could save around 3x of user's time and reduce user interactions by 3-5 times Metrics F1 Recall 96% 98% 88% 78% 83% 72% 48% 32% Multi-GPT4 Single-GPT4 Multi-GPT3.5 Single-GPT3.5 Performance OptiGuide Figure4d shows multi-agent design helpful boosting performance coding tasks need safeguards

## Recommended reading order

1. research_summary.md
2. deep_dive_task_matrix.md
3. prompts_complete.md
4. python_logic_flow_complete.md
5. graph_english.md / graph_arabic.md

## Related

- CAMEL role-playing inception prompting minimal human supervision only preliminary idea needed vs AutoGen customizable conversable agents various modes combinations LLMs human inputs tools flexible definition agent interaction behaviors both natural language and computer code can program flexible conversation patterns
- Scientific Intelligence Survey P5 Role-Interactive Multi-Agent distributed planning collaborative dialogue planner proposes critic identifies flaws executor provides feasibility feedback mirrors scientific team dynamics iterative discussion consensus-building tournament-style debate multi-round voting generation-reflection paired specialized critics vs AutoGen GroupChatManager dynamically select next speaker broadcast response
- Consolidated: https://github.com/faresrafat3/llm-agent-research-extractions
- ARSENAL: https://github.com/faresrafat3/arsenal-unified-master-pipeline
