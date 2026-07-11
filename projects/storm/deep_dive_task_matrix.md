
# STORM — Deep Dive Task Matrix

| Phase | Goal | Input | Prompt template | Output | Evaluation | Insight |
|---|---|---|---|---|---|---|
| **P0 Topic** | Starting point Wikipedia-like article from scratch | Topic t e.g., 2022 Winter Olympics Opening Ceremony | No LLM, user provides topic | Topic string | N/A | Underexplored problem pre-writing stage demand researching topic prepare outline prior writing Rohman 1965 discovery stage |
| **P1 Perspective Discovery via Surveying Related Articles** | Discover diverse perspectives multifaceted information stakeholder theory diverse stakeholders prioritize varying facets company | Topic t + need to simulate editors | GenRelatedTopicsPrompt: I'm writing Wikipedia page for topic mentioned below Please identify recommend Wikipedia pages on closely related subjects insights interesting aspects commonly associated or help understand typical content structure included in Wikipedia pages similar topics List urls separate lines Input topic Output related_topics | Related topics URLs list closely related subjects | Coverage diversity perspectives | Provides insights aspects commonly associated typical content structure |
| | Extract TOCs | Related topics URLs | get_wiki_article via Wikipedia-API https://pypi.org/project/Wikipedia-API/ extract_toc | tocs list TOCs concatenated context | N/A | If article obtainable |
| | Identify perspectives | Topic t + tocs examples wiki outlines related topics for inspiration | GenPerspectivesPrompt: You need select group Wikipedia editors who will work together create comprehensive article on topic Each represents different perspective role affiliation related to topic You can use other Wikipedia pages related topics inspiration For each editor add description what they will focus on Give answer format 1. short summary editor1: description... Input topic examples tocs Output perspectives | Perspectives P={p1..pN} N=5 + p0 basic fact writer focusing broadly covering basic facts about topic | Diversity breadth coverage | To ensure basic info covered add p0 basic fact writer into P Each perspective utilized guide question asking parallel |
| **P2 Simulated Conversations Multi-turn Information-seeking** | Research topic via perspective-guided question asking + follow-up in-depth questions iterative research, update understanding topic ask follow-up questions | Topic t + perspective p + dialog history | GenQnPrompt: You are experienced Wikipedia writer want edit specific page Besides identity as Wikipedia writer you have specific focus when researching topic Now you are chatting with expert to get information Ask good questions to get more useful information When no more question to ask say Thank you so much for your help! to end conversation Please only ask one question at a time don't ask what you have asked before Your questions related to topic you want to write Input topic persona conv history Output question q = gen_qn(t,p,dlg_history) | Question q per round | Depth breadth vs direct prompting What When Where Figure1A basic surface-level facts vs Figure1B varied transportation arrangements budget cultural broadcasting security Figure1C follow-up in-depth transportation budget vs surface | Direct prompting Ask 30 questions yields When was opening ceremony held? Where? How many countries? limited planning capacity perspective-guided You are event planner focusing preparation opening ceremony leads varied questions, conversational Can you provide list participating countries ... over 90 countries entering stadium specific order How is order determined? transportation arrangements? budget? elicits follow-up iterative research grounded Internet |
| | Transform question into search queries | Topic t + question q | GenQueriesPrompt: You want answer question using Google search What do you type search box? Write queries format - query1 - query2... Input topic question Output queries | Queries list - query1 newline - query2 etc | Query quality | Split queries step Figure2 ④ |
| | Search and sift trusted sources | Queries | search_and_sift queries via YouRM You.com search API https://documentation.you.com/api-reference/search search_top_k 10 ground truth Wikipedia article excluded from search results compatible other search engines BingSearch VectorRM SerperRM BraveRM SearXNG DuckDuckGoSearchRM TavilySearchRM GoogleSearch AzureAISearch | Sources filtered trusted sources | Retrieval thoroughness | Step Search & Sift Figure2 ⑤ |
| | Generate grounded answer | Topic t + Question + Gathered info sources | GenAnswerPrompt: You are expert who can use information effectively chatting with Wikipedia writer who wants write Wikipedia page on topic you know You have gathered related information will now use information to form response Make response as informative as possible make sure every sentence is supported by gathered information Input topic conv Question Gathered info Output Now give response answer a = gen_ans(t,q,sources) | Answer a informative every sentence supported gathered info | Informativeness groundedness | Expert grounded trustworthy Internet sources chat with writer Figure2 ⑥ Synthesize |
| | Collect references | Sources per turn | Append | R collection references | Coverage | R grows with N+1 * M conversations |
| **P3 Outline Creation Two-step** | Create outline before actual writing extensive outline indicates comprehensive understanding solid foundation writing full-length article | Topic t only + later conversations | DirectGenOutlinePrompt: Write outline for Wikipedia page Format Use "#" Title to indicate section title "##" Title subsection "###" subsubsection etc Do not include other information Input topic Output Write Wikipedia page outline OD = direct_gen_outline(t) | Draft outline OD general but organized framework leveraging internal knowledge LLMs | General organization | Figure2 ⑦ Direct Generate |
| | Refine outline with collected conversations | Topic t + OD + convos {C0..CN} N+1 conversations M rounds | RefineOutlinePrompt: Improve outline for Wikipedia page You already have draft outline covering general info Now you want improve it based on information learned from information-seeking conversation to make more comprehensive Format same # ## ### Input topic Conversation history Current outline Output Write Wikipedia page outline O = refine_outline(t,OD,convos) | Improved outline O comprehensive used for producing full-length article | Outline quality: heading soft recall Sentence-BERT paraphrase-MiniLM-L6-v2 cosine + heading entity recall FLAIR NER vs human-written ground truth | Figure2 ⑧ Refine fully leverage internal knowledge model draft + conversations |
| **P4 Writing Stage Section-by-section** | Generate full-length article grounded on collected references | Topic t + Outline O + References R | Building upon references R collected outline O developed during prewriting full-length article composed section by section Section title headings subsections used retrieve relevant documents from R based semantic similarity Sentence-BERT embeddings LLM then prompted generate section with citations Once all sections generated concatenated form full-length article LLM then prompted delete repeated information improve coherence Furthermore in alignment Wikipedia stylistic norms LLM also utilized synthesize summary entire article forming lead section at beginning Titles to generate article section by section | Full-length article S = s1 s2 ... sn each si cites list documents in R | Verifiability citation recall precision Gao et al Mistral 7B Prometheus Interest Coherence Organization Relevance Focus Coverage expert Wikipedia editors organized +25% absolute broad coverage +10% vs outline-driven RAG baseline Challenges source bias transfer bias on Internet affects articles over-association unrelated facts fabricate connections | Zero-shot prompting DSPy framework Khattab et al 2023 Appendix B pseudocode |
| | Polish | Draft article concatenated sections | Prompt to delete repeated info improve coherence | Polished article coherence improved | Coherence | - |
| | Lead summary | Polished article | Prompt synthesize summary entire article forming lead section at beginning Wikipedia stylistic norms lead 2-3 paragraphs concise overview main points | Lead section + full article | Wikipedia norms | - |
| **FreshWiki Dataset** | Evaluate capacity LLM systems generating long-form grounded articles from scratch avoid data leakage | Top 100 most-edited pages per month Feb2022-Sep2023 | Filter B-class quality ORES exclude list articles no subsections plain text only https://wikimedia.org/api/rest_v1/metrics/edited-pages/top-by-edits/en.wikipedia/all-editor-types/content/{year}/{month}/all-days https://www.mediawiki.org/wiki/ORES https://en.wikipedia.org/wiki/Wikipedia:Stand-alone_lists | FreshWiki recent high-quality Wikipedia articles | Process repeated future dates new LLMs emerge Resources code https://github.com/stanford-oval/storm | Mitigate leakage explicitly seeking recent articles created/heavily edited after training cutoff LLMs test |
| **Co-STORM Extension** | Collaborative discourse protocol human-AI collaborative knowledge curation EMNLP 2024 | Topic t + human engagement | Co-STORM LLM experts generates answers grounded external knowledge sources and/or raises follow-up questions based discourse history Moderator generates thought-provoking questions inspired by information discovered retriever but not directly used previous turns Question generation grounded Human user takes initiative either observe discourse gain deeper understanding or actively engage injecting utterances steer discussion focus Dynamic updated mind map organize collected information hierarchical concept structure aiming build shared conceptual space between human user and system mind map proven help reduce mental load when discourse goes long in-depth | Mind map hierarchical concept structure shared conceptual space | Collaboration | Highly modular dspy litellm integration language models embedding models pip install knowledge-storm |

## Prompt wiring map

| Step | Prompt | Line | Input → Output | Hyperparams |
|---|---|---|---|---|
| Survey related | GenRelatedTopicsPrompt | 4 | topic → related_topics URLs | - |
| Extract TOCs | get_wiki_article extract_toc | 6-10 | related_t → tocs | Wikipedia-API |
| Identify perspectives | GenPerspectivesPrompt | 11 | topic + tocs → P={p1..pN} + p0 basic fact writer | N=5 |
| Question asking | GenQnPrompt | 19 | topic + persona p + conv history → question q | M=5 rounds per perspective |
| Split queries | GenQueriesPrompt | 22 | topic + question → queries - q1 - q2 ... | - |
| Search & sift | search_and_sift | 23 | queries → sources filtered search_top_k 10 YouRM You.com BingSearch VectorRM etc ground truth excluded | search_top_k 10 |
| Answer grounded | GenAnswerPrompt | 24 | topic + question + info sources → answer a informative every sentence supported | - |
| Draft outline | DirectGenOutlinePrompt | 31 | topic → OD # ## ### general framework | gpt-3.5-turbo-instruct or gpt-4 |
| Refine outline | RefineOutlinePrompt | 32 | topic + OD + convos {C0..CN} → O comprehensive | gpt-4 drafting refining figure2 |
| Section gen | Section generation reconstructed | Writing | topic + outline O + relevant docs from R via Sentence-BERT similarity → section text with citations | Sentence-BERT |
| Polish | Delete repeated | Writing | draft article concatenated → polished | - |
| Lead summary | Lead synthesis | Writing | polished article → lead 2-3 paragraphs | Wikipedia stylistic norms |

## Data flow diagram textual

```
Topic t e.g., 2022 Winter Olympics Opening Ceremony
  → gen_related_topics t via GenRelatedTopicsPrompt → related_topics URLs closely related subjects insights interesting aspects typical content structure
  → foreach related_t get_wiki_article via Wikipedia-API extract_toc → tocs list TOCs concatenated context
  → gen_perspectives t + tocs via GenPerspectivesPrompt → perspectives P={p1..pN} N=5 each short summary description focus + p0 basic fact writer focusing broadly covering basic facts about topic P=[P0]+P[:N] N+1=6 perspectives
  → convos=[] R=[]
  → foreach p in P:
        convo_history=[]
        for i=1..M M=5:
            q=gen_qn t p dlg_history via GenQnPrompt Wikipedia writer guided by perspective asks incisive question only one at a time not asked before related to topic when no more say Thank you so much for your help! to end
            convo_history.append(q)
            queries=gen_queries t q via GenQueriesPrompt You want answer question using Google search What do you type search box? Write queries format - query1...
            sources=search_and_sift queries via YouRM You.com search API search_top_k 10 BingSearch VectorRM etc ground truth Wikipedia article excluded trusted sources
            a=gen_ans t q sources via GenAnswerPrompt expert who can use information effectively chatting with Wikipedia writer Make response as informative as possible make sure every sentence is supported by gathered information
            convo_history.append(a)
            R.append(sources)
        convos.append(convo_history) // Gather conversations {C0..CN} each M Q/A pairs total ~30 Q/A
  → OD=direct_gen_outline t via DirectGenOutlinePrompt Write outline for Wikipedia page format # Title ## Title ### Title etc only topic internal knowledge provides general but organized framework
  → O=refine_outline t OD convos via RefineOutlinePrompt Improve outline based on information learned from information-seeking conversation more comprehensive format same # ## ###
  → Full-length article generation:
        Building upon R and O section by section:
        For each section title + subheadings in O retrieve relevant docs from R via Sentence-BERT embeddings semantic similarity
        Prompt LLM generate section with citations [1][2] every sentence supported references
        Concatenate all sections form draft article
        Prompt LLM delete repeated information improve coherence polished article
        Prompt LLM synthesize summary entire article forming lead section beginning Wikipedia stylistic norms lead 2-3 paragraphs concise overview main points
        Final S = s1 s2 ... sn each si cites list documents in R plus organizational elements section subsection titles no citations
  → Evaluation:
        FreshWiki dataset top 100 most-edited per month Feb2022-Sep2023 filter B-class ORES exclude list no subsections plain text only avoid data leakage training cutoff process repeated future dates new LLMs emerge
        Outline quality heading soft recall Sentence-BERT paraphrase-MiniLM-L6-v2 cosine count(Ai)=1/sum_j Sim card(A)=sum count soft recall card(G∩P)/card(G) intersection via union card(G∩P)=card(G)+card(P)-card(G∪P) + heading entity recall percentage named entities covered FLAIR NER
        Article quality Prometheus 13B open-source evaluator 1-5 rubric Interest Coherence Organization Relevance Focus Coverage Table8 grading rubric without reference trimmed 2000 words iterative removing shortest section; citation recall precision Gao et al Mistral 7B; expert Wikipedia editors organized +25% absolute broad coverage +10% vs outline-driven RAG baseline challenges source bias transfer bias Internet affects articles over-association unrelated facts fabricate connections new frontiers grounded writing systems
        Co-STORM extension collaborative discourse protocol turn management policy Co-STORM LLM experts generates answers grounded external knowledge and/or raises follow-up questions discourse history Moderator generates thought-provoking questions inspired info discovered retriever but not directly used previous turns Question generation grounded Human user initiative observe discourse gain deeper understanding or actively engage injecting utterances steer discussion focus dynamic updated mind map hierarchical concept structure shared conceptual space reduce mental load when discourse long in-depth highly modular dspy litellm integration language models embedding models pip install knowledge-storm
```

## Categories comparison Table1

| Paper | Domain Scope | Given Outline | Given Refs | Our setup |
|---|---|---|---|---|
| Balepur et al 2023 | One | One para | / | Yes |
| Qian et al 2023 | All | One para | / | No |
| Fan and Gardent 2022 | One | Full article | Yes | No |
| Liu et al 2018 | All | One para | / | Yes |
| Sauper and Barzilay 2009 | Two | Full article | No | No |
| Ours STORM | All | Full article | No | No |

Our setup All domains Full article No Given Outline No Given Refs emphasizes capability long-form grounded writing systems to research curate content Given topic t task find set references R and generate full-length article S s1...sn each si cites list documents in R

## Links to other systems

- GAPMAP explicit gap extraction → perspective failure identification source bias transfer
- ResearchAgent context-augmented planner → STORM perspective discovery related topics TOCs survey, role-interactive multi-agent reviewing → perspective-guided question asking multi-perspective editors
- Scientific Intelligence Survey P2 Context-Augmented (historical records KB facts), P5 Role-Interactive Multi-Agent (tournament debate judge meta-review), P3 Deliberative Reflective (generate initial reflect flaws revise), V2 tool-based (YouRM search_and_sift quantum-chemical feedback analogy), V3 HITL Expert Oversight (Wikipedia editors expert evaluation organized +25% broad +10%), V4 Multi-Agent Critique (diverse perspectives novelty feasibility impact filtering)
- SciMON iterative novelty boosting vs STORM perspective-guided questioning different optimization novelty vs breadth organization
- STORM perspective-guided question asking mirrors ResearchAgent entity retrieval cross-domain pollination but for Wikipedia broad coverage
