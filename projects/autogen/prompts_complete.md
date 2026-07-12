# AutoGen — Complete Prompt Extraction

Source: arXiv:2308.08155 PDF 43 pages + GitHub microsoft/autogen 59.7k stars

## 1. ConversableAgent Base

**Spec:**

```
ConversableAgent class highest-level agent abstraction and by default can use LLMs, humans, and tools
Maintains internal context based on sent and received messages
Can be configured to possess set of capabilities enabled by LLMs, tools, or human input
Capabilities directly influence how it processes and responds to messages
Supports many common composable capabilities:
  1) LLMs: LLM-backed agents exploit many capabilities advanced LLMs such as role playing, implicit state inference and progress making conditioned on conversation history, providing feedback, adapting from feedback, coding. Combined different ways via novel prompting techniques to increase skill and autonomy. Enhanced LLM inference features such as result caching, error handling, message templating etc via enhanced LLM inference layer
  2) Humans: Human involvement desired or essential many LLM applications. Allows human participate agent conversation via human-backed agents which could solicit human inputs at certain rounds conversation depending agent configuration. Default user proxy agent allows configurable human_input_mode frequency and conditions for requesting human input including option humans skip providing input
  3) Tools: Tool-backed agents capability execute tools via code execution or function execution. For example default user proxy agent able execute code suggested by LLMs or make LLM-suggested function calls
```

**Unified Interfaces:**

```
send: sending messages
receive: receiving messages
generate_reply: taking actions and generating response based on received message
```

**Auto-reply mechanism:**

```
Once agent receives message from another agent it automatically invokes generate_reply and sends reply back to sender unless termination condition satisfied
Provides built-in reply functions based on LLM inference, code or function execution, or human input
One can also register custom reply functions customize behavior pattern of agent e.g. chatting with another agent before replying to sender agent
Under this mechanism once reply functions registered and conversation is initialized conversation flow naturally induced and thus agent conversation proceeds naturally without any extra control plane i.e. special module that controls conversation flow
```

**Example Developer Code Figure2 blue-shaded:**

```python
# This func will be invoked in generate_reply
A.register_reply(B, reply_func_A2B)
def reply_func_A2B(msg):
    output = input_from_human()
    ...
    if not output:
        if msg includes code:
            output = execute(msg)
    return output
```

## 2. AssistantAgent Pre-configured

**Definition:**

```
AssistantAgent and UserProxyAgent two pre-configured ConversableAgent subclasses each representing common usage mode i.e. acting as AI assistant backed by LLMs and acting as human proxy to solicit human input or execute code/function calls backed by humans and/or tools
```

**System Message DEFAULT_SYSTEM_MESSAGE:**

```
You are a helpful AI assistant...
In the following cases, suggest python code...
In the following cases, suggest python code (from paper: In the following cases, suggest python code...)

Example from paper: DEFAULT_SYSTEM_MESSAGE = "You are a helpful AI assistant... In the following cases, suggest python code…"
```

**Config:**

```
human_input_mode = "NEVER"
code_execution_config = False
```

**Use:** Act as AI assistant backed by LLMs

**Example behavior:** Example on right-hand side Figure1 LLM-backed assistant agent and tool- and human-backed user proxy agent deployed together tackle task Here assistant agent generates solution with help LLMs and passes solution to user proxy agent Then user proxy agent solicits human inputs or executes assistant's code and passes results as feedback back to assistant Appendix C presents example novel prompting techniques which empowers default LLM-backed assistant agent in AutoGen to converse with other agents in multi-step problem solving

**Natural-language control via LLMs:**

```
Default system message of built-in AssistantAgent uses natural language to instruct agent to fix errors and generate code again if previous result indicates errors
It also guides agent confine LLM output to certain structures making it easier for other tool-backed agents to consume
For example instructing agent to reply with "TERMINATE" when all tasks completed to terminate program
More concrete examples natural language controls can be found Appendix C
```

**Prompt for TERMINATE:**

```text
You are a helpful AI assistant. When all tasks are completed, reply with "TERMINATE" to terminate program.

If previous result indicates errors, fix errors and generate code again.

In following cases suggest python code...
```

## 3. UserProxyAgent Pre-configured

**Definition:**

```
UserProxyAgent acting as human proxy to solicit human input or execute code/function calls backed by humans and/or tools
```

**Config:**

```
human_input_mode = "ALWAYS" (or NEVER depending example) 
GroupChatManager human_input_mode = "NEVER"
group_chat = []
Note when no reply func registered list default reply functions will be used
Agent Customization
```

**Capabilities:**

- Solicit human inputs at certain rounds depending configuration frequency and conditions for requesting human input including option humans skip providing input
- Execute code suggested by LLMs or make LLM-suggested function calls via code execution or function execution
- Default user proxy agent able execute code suggested by LLMs or make LLM-suggested function calls

**Example:**

```
User Proxy A
AutoGen Agents
Developer Code
Plot a chart of META and TESLA stock price change YTD.
Execute following code...
send receive receive
Conversation-Centric Computation generate_reply Error package yfinance is not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat
```

**Prompt for human input mode:**

```text
human_input_mode = "ALWAYS" # solicit human inputs at certain rounds
# or NEVER

# This func will be invoked in generate_reply
A.register_reply(B, reply_func_A2B)
def reply_func_A2B(msg):
    output = input_from_human()
    if not output:
        if msg includes code:
            output = execute(msg)
    return output
```

## 4. GroupChatManager

**Definition:**

```
GroupChatManager human_input_mode = "NEVER"
group_chat = []
Note when no reply func registered list default reply functions will be used
Agent Customization: supports more complex dynamic group chat via built-in GroupChatManager which can dynamically select next speaker and then broadcast its response to other agents Elaborates feature and its application Section 3
```

**Use:** Achieve dynamic group chat, can dynamically select next speaker and then broadcast response to other agents

**Example:**

```python
group_chat = [agent1, agent2, agent3]
manager = GroupChatManager(group_chat)
# manager dynamically selects next speaker
```

## 5. Conversation Programming

**Paradigm:**

```
Conversation programming paradigm considers two concepts: computation – actions agents take to compute response in multi-agent conversation And control flow – sequence or conditions under which these computations happen Ability program these helps implement many flexible multi-agent conversation patterns In AutoGen computations are conversation-centric Agent takes actions relevant to conversations involved and actions result in message passing for consequent conversations unless termination condition satisfied Similarly control flow is conversation-driven participating agents decisions which agents to send messages to and procedure of computation are functions of inter-agent conversation This paradigm helps reason intuitively about complex workflow as agent action taking and conversation message-passing between agents
```

**Figure2 illustration:**

- Bottom sub-figure shows how individual agents perform role-specific conversation-centric computations generate responses e.g. via LLM inference calls and code execution Task progresses through conversations displayed dialog box
- Middle sub-figure demonstrates conversation-based control flow When assistant receives message user proxy agent typically sends human input as reply If no input executes any code in assistant's message instead
- Top sub-figure illustrates built-in agents provided by AutoGen which have unified conversation interfaces and can be customized Middle sub-figure shows example using AutoGen to develop two-agent system with custom reply function Bottom sub-figure illustrates resulting automated agent chat from two-agent system during program execution

**Two general ways achieve dynamic conversation flows multiple agents:**

1. Customized generate_reply function: within customized generate_reply function one agent can hold current conversation while invoking conversations with other agents depending content current message and context
2. Function calls: In this approach LLM decides whether or not to call particular function depending conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation

In addition AutoGen supports more complex dynamic group chat via built-in GroupChatManager which can dynamically select next speaker and then broadcast its response to other agents Elaborates feature and its application Section 3 Working systems showcase all these different patterns

## 6. Conversation Initiation

**Example Figure2:**

```python
# 1. Define Agents
# 2. Initiate Conversations:
A.initiate_chat("Plot a chart of META and TESLA stock price change YTD.", B)
Assistant B
User Proxy A
...
# Unified Conversation Interfaces: send receive generate_reply
# Conversation-Centric Computation generate_reply Error: package yfinance is not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply The Resulting Automated Agent Chat: ...
# 1.2 Register Custom Reply Func 1.1 Define Agents
```

**Program Execution dialog box example:**

```
Program Execution
Plot a chart of META and TESLA stock price change YTD.
Execute following code...
send receive receive
Conversation-Centric Computation generate_reply
Error: package yfinance is not installed
send generate_reply
Sorry! Please first pip install yfinance and then execute
Conversation-Driven Control Flow generate_reply
The Resulting Automated Agent Chat:
...
```

## 7. Control by Fusion of Programming and Natural Language

**Three patterns:**

1. Natural-language control via LLMs: One can control conversation flow by prompting LLM-backed agents with natural language For instance default system message of built-in AssistantAgent uses natural language to instruct agent to fix errors and generate code again if previous result indicates errors It also guides agent confine LLM output certain structures making it easier for other tool-backed agents consume For example instructing agent reply with TERMINATE when all tasks completed terminate program More concrete examples natural language controls can be found Appendix C

2. Programming-language control: Python code can be used specify termination condition human input mode tool execution logic e.g. max number auto replies One can also register programmed auto-reply functions control conversation flow with Python code as shown code block identified as Conversation-Driven Control Flow in Figure2

3. Control transition between natural and programming language: Supports flexible control transition between natural and programming language One can achieve transition from code to natural-language control by invoking LLM inference containing certain control logic in customized reply function or transition from natural language to code control via LLM-proposed function calls Eleti et al 2023

**Example natural-language control prompt:**

```text
You are a helpful AI assistant. If previous result indicates errors, fix errors and generate code again.
Confine your output to certain structures...
When all tasks are completed, reply with "TERMINATE" to terminate program.
```

**Example programming-language control:**

```python
# Specify termination condition, human input mode, tool execution logic, e.g. max number auto replies
assistant = AssistantAgent(human_input_mode="NEVER", max_consecutive_auto_reply=5)
user_proxy = UserProxyAgent(human_input_mode="ALWAYS", code_execution_config={"work_dir": "coding"})

# Register programmed auto-reply functions
def reply_func_A2B(msg):
    output = input_from_human()
    if not output:
        if msg includes code:
            output = execute(msg)
    return output

A.register_reply(B, reply_func_A2B)
```

## 8. Applications A1-A4 Conversation Patterns

### A1 Math: Two-agent system out-of-box competitive performance math problem solving tasks

**Pattern:** Assistant + User Proxy, static conversation with predefined flow

Figure4a Performance on MATH w GPT-4 120 Level-5 problems Whole Dataset Success Ratio 69.48% Whole Dataset 55.18% Average etc AutoGen vs ChatGPT+Code ChatGPT+Plugin GPT-4 Multi-Agent Debate LangChain ReAct etc

### A2 Retrieval-Augmented Chat RAG: Interactive Retrieval

**System consists two agents:** Retrieval-augmented User Proxy agent and Retrieval-augmented Assistant agent both extended from built-in agents Retrieval-augmented User Proxy includes vector database Chroma with SentenceTransformers Reimers & Gurevych context retriever detailed workflow Appendix D

**Evaluation Natural Questions dataset Kwiatkowski et al 2019 vs DPR Dense Passage Retrieval Adlakha et al 2023**

**Novel interactive retrieval feature prompt:**

```text
Whenever retrieved context does not contain information, instead of terminating, LLM-based assistant would reply "Sorry, I cannot find any information about... UPDATE CONTEXT." which will invoke more retrieval attempts.

Ablation: prompt assistant agent to say "I don't know" instead of "UPDATE CONTEXT." in cases relevant information not found

Interactive retrieval mechanism indeed plays non-trivial role process
```

**Scenario2:** Further demonstrate how Retrieval-augmented Chat aids generating code based given codebase that contains code not included GPT-4 training data Evaluation demonstration details both scenarios Appendix D

**Metrics Figure4b:** F1 Recall 25.88% 66.65% 15.12% 58.56% 22.79% 62.59% AutoGen AutoGen W/O interactive retrieval DPR etc

### A3 ALFWorld Decision Making Text World Environments

Diverse collection synthetic language-based interactive decision-making tasks household environments

**Two-agent system:** LLM-backed assistant agent responsible suggesting plans conduct task and executor agent responsible executing actions ALFWorld environments integrates ReAct prompting Yao et al 2022 able achieve similar performance Common challenge encountered both ReAct and AutoGen-based two-agent system occasional inability leverage basic commonsense knowledge about physical world Deficiency can lead system getting stuck loop due repetitive errors Fortunately modular design AutoGen allows address issue effectively: With AutoGen able introduce grounding agent which supplies crucial commonsense knowledge such as "You must find and take the object before you can examine it. You must go to where target object is before you can use it." whenever system exhibits early signs recurring errors Significantly enhances ability avoid getting entangled error loops Compare task-solving performance two variants our system with GPT-3.5-turbo and ReAct on 134 unseen tasks ALFWorld report results Figure4c results show introducing grounding agent could bring 15% performance gain average Upon examining systems outputs observe grounding agent by delivering background commonsense knowledge right junctures significantly mitigated tendency system persist flawed plan thereby avoiding creation error loops Example trajectory comparing systems Appendix D Figure10

**Three-agent system with grounding agent:**

```
Assistant (suggest plans)
Executor (execute actions in ALFWorld)
Grounding Agent (supplies crucial commonsense knowledge e.g., "You must find and take the object before you can examine it. You must go to where target object is before you can use it." whenever early signs recurring errors)

Performance: 69% 54% 54% 77% 63% 66% Average Best of 3 AutoGen 3 agent AutoGen 2 agent ReAct 15% gain average with grounding agent
```

### A4 Multi-Agent Coding OptiGuide: Commander Writer Safeguard

System excels writing code interpret optimization solutions answer user questions such exploring implications changing supply-chain decision or understanding why optimizer made particular choice Second sub-figure Figure3 shows AutoGen-based implementation

**Workflow:** end user sends questions such "What if we prohibit shipping from supplier 1 to roastery 2?" to Commander agent Commander coordinates with two assistant agents including Writer and Safeguard to answer question Writer will craft code and send code to Commander After receiving code Commander checks code safety with Safeguard if cleared Commander will use external tools e.g. Python to execute code and request Writer to interpret execution results For instance writer may say if we prohibit shipping from supplier 1 to roastery 2 total cost would increase by 10.5% Commander then provides this concluding answer to end user If at particular step there is exception e.g. security red flag raised by Safeguard Commander redirects issue back to Writer with debugging information Process might be repeated multiple times until user's question answered or timed-out

**Productivity improvement:** With AutoGen core workflow code for OptiGuide reduced from over 430 lines to 100 lines leading significant productivity improvement Provide detailed comparison user experience ChatGPT+Code Interpreter and AutoGen-based OptiGuide Appendix D where show AutoGen-based OptiGuide could save around 3x of user's time and reduce user interactions by 3-5 times

**Metrics Figure4d:** F1 Recall 96% 98% 88% 78% 83% 72% 48% 32% Multi-GPT4 Single-GPT4 Multi-GPT3.5 Single-GPT3.5 Performance OptiGuide shows multi-agent design helpful boosting performance coding tasks need safeguards

## 9. Prompt Wiring Map AutoGen

| Prompt / Pattern | Purpose | Mode |
|---|---|---|
| ConversableAgent send/receive/generate_reply unified interfaces auto-reply mechanism | Automated agent chat decentralized modular unified way define workflow Once agent receives message automatically invokes generate_reply sends reply back unless termination condition satisfied | Auto-reply mechanism |
| AssistantAgent DEFAULT_SYSTEM_MESSAGE You are helpful AI assistant In following cases suggest python code... human_input_mode NEVER code_execution_config False | Act as AI assistant backed by LLMs | LLM-backed |
| UserProxyAgent human_input_mode ALWAYS group_chat [] Note when no reply func registered list default reply functions will be used | Act as human proxy solicit human input or execute code/function calls backed by humans and/or tools | Human and tool backed |
| GroupChatManager human_input_mode NEVER group_chat managerdynamically select next speaker broadcast response | Achieve dynamic group chat more complex | Group chat |
| A.initiate_chat("Plot chart META TESLA stock price change YTD.", B) | Initiate conversations | Two-agent |
| A.register_reply(B, reply_func_A2B) def reply_func_A2B(msg): output = input_from_human() if not output if msg includes code output = execute(msg) return output | Custom reply function programming-language control | Custom reply |
| Natural-language control via LLMs fix errors and generate code again if previous result indicates errors confine output certain structures TERMINATE when all tasks completed terminate program Appendix C | Control conversation flow prompting LLM-backed agents natural language | Natural control |
| Programming-language control specify termination condition human input mode tool execution logic max number auto replies register programmed auto-reply functions | Control conversation flow Python code | Programming control |
| Control transition code to natural-language invoking LLM inference containing certain control logic in customized reply function natural language to code via LLM-proposed function calls Eleti et al 2023 | Flexible transition | Transition |
| Customized generate_reply function within customized generate_reply one agent can hold current conversation while invoking conversations with other agents depending content current message context | Achieve dynamic conversation flows multiple agents static predefined flow vs dynamic | Dynamic custom |
| Function calls LLM decides whether or not to call particular function depending conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation | Dynamic via function calls | Dynamic function |
| Retrieval-augmented User Proxy includes vector database Chroma SentenceTransformers context retriever + Retrieval-augmented Assistant extended built-in agents + Interactive retrieval feature Sorry, I cannot find any information about... UPDATE CONTEXT vs I don't know ablation | Retrieval-Augmented Chat RAG effective retrieval augmentation novel interactive retrieval feature boost performance | RAG interactive |
| ALFWorld two-agent assistant suggesting plans executor executing actions ReAct prompting + grounding agent supplies crucial commonsense knowledge You must find and take object before you can examine it You must go to where target object is before you can use it whenever early signs recurring errors 15% performance gain average 134 unseen tasks | Decision Making Text World Environments avoid error loops | Grounding agent |
| OptiGuide Commander coordinates Writer and Safeguard to answer What if we prohibit shipping from supplier 1 to roastery 2? Writer crafts code Commander checks safety with Safeguard if cleared executes Python request Writer interpret execution results total cost increase 10.5% Commander provides concluding answer If exception security red flag raised by Safeguard Commander redirects issue back to Writer debugging information repeated multiple times until answered or timed-out core workflow reduced 430 lines to 100 lines save 3x time reduce interactions 3-5 times Multi-GPT4 Single-GPT4 Multi-GPT3.5 Single-GPT3.5 | Multi-Agent Coding safeguards | Commander Writer Safeguard |

## 10. Non-prompt but prompt-adjacent

- Core design principle streamline consolidate multi-agent workflows using multi-agent conversations maximize reusability implemented agents
- Conversable agent is entity with specific role that can pass messages send receive information to/from other conversable agents e.g. start or continue conversation Maintains internal context based on sent and received messages can be configured possess set capabilities enabled by LLMs tools or human input
- Enhanced LLM inference features result caching error handling message templating via enhanced LLM inference layer
- Agent capabilities powered by LLMs humans tools composable
- Yellow-shaded area Figure2 sketch built-in agents AutoGen ConversableAgent class highest-level agent abstraction by default can use LLMs humans tools AssistantAgent and UserProxyAgent two pre-configured ConversableAgent subclasses common usage mode AssistantAgent AI assistant backed LLMs UserProxyAgent human proxy solicit human input or execute code/function calls backed humans and/or tools Example right-hand side Figure1 LLM-backed assistant and tool- human-backed user proxy deployed together tackle task Assistant generates solution with help LLMs passes solution to user proxy Then user proxy solicits human inputs or executes assistant's code passes results as feedback back to assistant Appendix C example novel prompting techniques empowers default LLM-backed assistant agent converse with other agents multi-step problem solving
- Figure2 Illustration how use AutoGen program multi-agent conversation Top sub-figure illustrates built-in agents provided by AutoGen have unified conversation interfaces can be customized Middle sub-figure shows example using AutoGen develop two-agent system with custom reply function Bottom sub-figure illustrates resulting automated agent chat from two-agent system during program execution
- Built-in reply functions based on LLM inference code or function execution or human input Custom reply functions customize behavior pattern e.g. chatting with another agent before replying to sender Once reply functions registered and conversation initialized conversation flow naturally induced and thus agent conversation proceeds naturally without extra control plane special module controls conversation flow For example with developer code blue-shaded area marked Developer Code of Figure2 one can readily trigger conversation among agents and conversation would proceed automatically as shown dialog box grey shaded area marked Program Execution of Figure2 Auto-reply mechanism provides decentralized modular unified way define workflow
- Conversation initiation 2 Initiate Conversations A.initiate_chat Plot chart META and TESLA stock price change YTD B Assistant B User Proxy A AutoGen Agents Developer Code This func will be invoked in generate_reply A.register_reply B reply_func_A2B def reply_func_A2B(msg): output = input_from_human() if not output if msg includes code output = execute(msg) return output ConversableAgent AssistantAgent UserProxyAgent human_input_mode NEVER code_execution_config False DEFAULT_SYSTEM_MESSAGE You are helpful AI assistant... In following cases suggest python code... human_input_mode ALWAYS GroupChatManager human_input_mode NEVER group_chat [] Note when no reply func registered list default reply functions will be used Agent Customization Program Execution Plot chart META TESLA stock price change YTD Execute following code... send receive receive Conversation-Centric Computation generate_reply Error package yfinance not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat 1.2 Register Custom Reply Func 1.1 Define Agents Unified Conversation Interfaces send receive generate_reply
- Figure2 bottom sub-figure how individual agents perform role-specific conversation-centric computations generate responses e.g. via LLM inference calls and code execution Task progresses through conversations displayed dialog box Middle sub-figure demonstrates conversation-based control flow When assistant receives message user proxy agent typically sends human input as reply If no input executes any code in assistant's message instead
- Bottom sub-figure automated agent chat Program Execution Plot chart META TESLA stock price change YTD Execute following code... send receive receive Conversation-Centric Computation generate_reply Error package yfinance not installed send generate_reply Sorry! Please first pip install yfinance and then execute Conversation-Driven Control Flow generate_reply Resulting Automated Agent Chat
- AutoGen features design patterns facilitate conversation programming 1 Unified interfaces and auto-reply mechanisms for automated agent chat 2 Control by fusion of programming and natural language 1 Natural-language control via LLMs 2 Programming-language control 3 Control transition between natural and programming language In conversation programming paradigm one can realize multi-agent conversations diverse patterns In addition to static conversation with predefined flow AutoGen also supports dynamic conversation flows with multiple agents Provides two general ways achieve this 1 Customized generate_reply function within customized generate_reply function one agent can hold current conversation while invoking conversations with other agents depending content current message and context 2 Function calls In this approach LLM decides whether or not to call particular function depending conversation status By messaging additional agents in called functions LLM can drive dynamic multi-agent conversation In addition AutoGen supports more complex dynamic group chat via built-in GroupChatManager which can dynamically select next speaker and then broadcast its response to other agents Elaborates feature and application in Section3 Working systems showcase all these different patterns
- Applications: Math out-of-box competitive performance math problem solving tasks Success Ratio 69.48% etc, Retrieval-Augmented Chat RAG interactive retrieval feature UPDATE CONTEXT vs I don't know ablation F1 Recall etc, ALFWorld two-agent plus grounding agent 15% gain 134 unseen tasks, OptiGuide Commander Writer Safeguard multi-agent coding safeguards reduce workflow code 430 to 100 lines save 3x time
