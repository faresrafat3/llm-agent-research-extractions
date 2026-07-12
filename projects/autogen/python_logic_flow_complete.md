
# AutoGen — Python Logic Flow Complete

## 0. Entry point

```
ConversableAgent class highest-level agent abstraction by default can use LLMs, humans, tools
AssistantAgent and UserProxyAgent two pre-configured ConversableAgent subclasses common usage mode i.e. acting as AI assistant backed by LLMs and acting as human proxy solicit human input or execute code/function calls backed by humans and/or tools
GroupChatManager human_input_mode NEVER group_chat []
```

## 1. Agent capabilities

```
LLMs: role playing, implicit state inference and progress making conditioned on conversation history, providing feedback, adapting from feedback, coding. Combined different ways via novel prompting techniques to increase skill autonomy Enhanced LLM inference features result caching error handling message templating via enhanced LLM inference layer
Humans: Human involvement desired or essential many LLM applications Lets human participate agent conversation via human-backed agents which could solicit human inputs at certain rounds conversation depending agent configuration Default user proxy agent allows configurable human_input_mode frequency and conditions for requesting human input including option humans skip providing input
Tools: Tool-backed agents capability execute tools via code execution or function execution For example default user proxy agent able execute code suggested by LLMs or make LLM-suggested function calls
```

## 2. Conversation programming

```
Conversation programming paradigm considers two concepts: computation – actions agents take to compute response in multi-agent conversation And control flow – sequence or conditions under which these computations happen
Computations are conversation-centric Agent takes actions relevant to conversations involved and actions result in message passing for consequent conversations unless termination condition satisfied
Control flow is conversation-driven participating agents decisions which agents to send messages to and procedure of computation are functions of inter-agent conversation
Helps reason intuitively about complex workflow as agent action taking and conversation message-passing between agents
Figure2 bottom sub-figure how individual agents perform role-specific conversation-centric computations generate responses e.g. via LLM inference calls and code execution Task progresses through conversations displayed dialog box Middle sub-figure demonstrates conversation-based control flow When assistant receives message user proxy agent typically sends human input as reply If no input executes any code in assistant's message instead
Top sub-figure illustrates built-in agents provided by AutoGen which have unified conversation interfaces and can be customized Middle sub-figure shows example using AutoGen to develop two-agent system with custom reply function Bottom sub-figure illustrates resulting automated agent chat from two-agent system during program execution
```

## 3. Unified interfaces and auto-reply

```
Agents have unified conversation interfaces for performing corresponding conversation-centric computation including send/receive function for sending/receiving messages and generate_reply function for taking actions and generating response based on received message
AutoGen also introduces and by default adopts agent auto-reply mechanism to realize conversation-driven control: Once agent receives message from another agent it automatically invokes generate_reply and sends reply back to sender unless termination condition satisfied
Provides built-in reply functions based on LLM inference code or function execution or human input
One can also register custom reply functions customize behavior pattern of agent e.g. chatting with another agent before replying to sender agent
Under this mechanism once reply functions registered and conversation initialized conversation flow naturally induced and thus agent conversation proceeds naturally without any extra control plane special module that controls conversation flow
For example with developer code blue-shaded area marked Developer Code of Figure2 one can readily trigger conversation among agents and conversation would proceed automatically as shown dialog box grey shaded area marked Program Execution of Figure2 Auto-reply mechanism provides decentralized modular unified way define workflow
```

## 4. Control fusion

```
1 Natural-language control via LLMs One can control conversation flow by prompting LLM-backed agents with natural language For instance default system message of built-in AssistantAgent uses natural language to instruct agent to fix errors and generate code again if previous result indicates errors It also guides agent confine LLM output certain structures making it easier for other tool-backed agents consume For example instructing agent reply with TERMINATE when all tasks completed terminate program More concrete examples natural language controls can be found Appendix C
2 Programming-language control Python code can be used specify termination condition human input mode tool execution logic e.g. max number auto replies One can also register programmed auto-reply functions control conversation flow with Python code as shown code block identified as Conversation-Driven Control Flow in Figure2
3 Control transition between natural and programming language Supports flexible control transition between natural and programming language One can achieve transition from code to natural-language control by invoking LLM inference containing certain control logic in customized reply function or transition from natural language to code control via LLM-proposed function calls Eleti et al 2023
```

## 5. Dynamic conversation flows

```
In addition to static conversation with predefined flow AutoGen also supports dynamic conversation flows with multiple agents Provides two general ways achieve this 1 Customized generate_reply function within customized generate_reply function one agent can hold current conversation while invoking conversations with other agents depending content current message and context 2 Function calls In this approach LLM decides whether or not to call particular function depending conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation In addition AutoGen supports more complex dynamic group chat via built-in GroupChatManager which can dynamically select next speaker and then broadcast its response to other agents Elaborates feature and its application Section3 Working systems showcase all these different patterns
```

## 6. Conversation initiation Figure2

```
2 Initiate Conversations: A.initiate_chat("Plot a chart of META and TESLA stock price change YTD.", B) Assistant B User Proxy A AutoGen Agents Developer Code This func will be invoked in generate_reply A.register_reply(B, reply_func_A2B) def reply_func_A2B(msg): output = input_from_human() if not output if msg includes code output = execute(msg) return output ConversableAgent AssistantAgent UserProxyAgent human_input_mode NEVER code_execution_config False DEFAULT_SYSTEM_MESSAGE You are helpful AI assistant... In following cases suggest python code... human_input_mode ALWAYS GroupChatManager human_input_mode NEVER group_chat [] Note when no reply func registered list default reply functions will be used Agent Customization Program Execution Plot chart META TESLA stock price change YTD Execute following code... send receive receive Conversation-Centric Computation generate_reply Error package yfinance not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat ...

Program Execution dialog box
Plot chart META TESLA stock price change YTD
Execute following code...
send receive receive
Conversation-Centric Computation generate_reply Error package yfinance not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat
```

## 7. Applications A1-A4

- A1 Math 120 Level-5 problems Whole Dataset AutoGen vs ChatGPT+Code ChatGPT+Plugin GPT-4 Multi-Agent Debate LangChain ReAct etc AutoGen agents can be used out of box achieve most competitive performance math problem solving tasks Success Ratio 69.48% Whole Dataset 55.18% Average etc Figure4a Performance on MATH w GPT-4

- A2 Retrieval-Augmented Chat RAG system consists two agents Retrieval-augmented User Proxy agent and Retrieval-augmented Assistant agent both extended from built-in agents Retrieval-augmented User Proxy includes vector database Chroma with SentenceTransformers Reimers & Gurevych context retriever detailed workflow Appendix D Evaluation natural question answering Natural Questions dataset Kwiatkowski et al 2019 vs DPR Dense Passage Retrieval Adlakha et al 2023 Leveraging conversational design natural-language control AutoGen introduces novel interactive retrieval feature whenever retrieved context does not contain information instead terminating LLM-based assistant would reply Sorry I cannot find any information about... UPDATE CONTEXT which will invoke more retrieval attempts Conduct ablation study prompt assistant agent say I don't know instead of UPDATE CONTEXT cases relevant information not found report results Figure4b results show interactive retrieval mechanism indeed plays non-trivial role Concrete example results using appealing feature Appendix D Scenario2 further demonstrate how Retrieval-augmented Chat aids generating code based given codebase that contains code not included GPT-4 training data Evaluation demonstration details both scenarios Appendix D Metrics F1 Recall 25.88% 66.65% 15.12% 58.56% 22.79% 62.59% AutoGen AutoGen W/O interactive retrieval DPR etc

- A3 ALFWorld Diverse collection synthetic language-based interactive decision-making tasks household environments Two-agent system LLM-backed assistant agent responsible suggesting plans conduct task and executor agent responsible executing actions ALFWorld environments integrates ReAct prompting Yao et al 2022 able achieve similar performance Common challenge encountered both ReAct and AutoGen-based two-agent system occasional inability leverage basic commonsense knowledge about physical world Deficiency can lead system getting stuck loop due repetitive errors Fortunately modular design AutoGen allows address issue effectively: With AutoGen able introduce grounding agent which supplies crucial commonsense knowledge such as You must find and take the object before you can examine it. You must go to where target object is before you can use it. whenever system exhibits early signs recurring errors Significantly enhances ability avoid getting entangled error loops Compare task-solving performance two variants our system with GPT-3.5-turbo and ReAct on 134 unseen tasks ALFWorld report results Figure4c results show introducing grounding agent could bring 15% performance gain average Upon examining systems outputs observe grounding agent by delivering background commonsense knowledge right junctures significantly mitigated tendency system persist flawed plan thereby avoiding creation error loops Example trajectory comparing systems Appendix D Figure10 Metrics 69% 54% 54% 77% 63% 66% Average Best of 3 AutoGen 3 agent AutoGen 2 agent ReAct

- A4 Multi-Agent Coding OptiGuide System excels writing code interpret optimization solutions answer user questions such exploring implications changing supply-chain decision or understanding why optimizer made particular choice Second sub-figure Figure3 shows AutoGen-based implementation Workflow end user sends questions such What if we prohibit shipping from supplier 1 to roastery 2? to Commander agent Commander coordinates with two assistant agents including Writer and Safeguard to answer question Writer will craft code and send code to Commander After receiving code Commander checks code safety with Safeguard if cleared Commander will use external tools e.g. Python to execute code and request Writer to interpret execution results For instance writer may say if we prohibit shipping from supplier 1 to roastery 2 total cost would increase by 10.5% Commander then provides this concluding answer to end user If at particular step exception e.g. security red flag raised by Safeguard Commander redirects issue back to Writer with debugging information Process might be repeated multiple times until user's question answered or timed-out With AutoGen core workflow code for OptiGuide reduced from over 430 lines to 100 lines leading significant productivity improvement Provide detailed comparison user experience ChatGPT+Code Interpreter and AutoGen-based OptiGuide Appendix D where show AutoGen-based OptiGuide could save around 3x of user's time and reduce user interactions by 3-5 times Metrics F1 Recall 96% 98% 88% 78% 83% 72% 48% 32% Multi-GPT4 Single-GPT4 Multi-GPT3.5 Single-GPT3.5 Performance OptiGuide Figure4d shows multi-agent design helpful boosting performance coding tasks need safeguards
