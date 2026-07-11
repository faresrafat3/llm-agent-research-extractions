# STORM — Research Summary

## Identity

- Title: Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models
- ArXiv: 2402.14207v2 Apr 8 2024, NAACL 2024 Main Conference, 27 pages
- Authors: Yijia Shao, Yucheng Jiang, Theodore A. Kanell, Peter Xu, Omar Khattab, Monica S. Lam (Stanford OVAL Lab Open Virtual Assistant Lab)
- Code: https://github.com/stanford-oval/storm, package knowledge-storm pip install knowledge-storm, logo overview.svg two_stages.jpg, demo https://storm.genie.stanford.edu 70k+ users, Co-STORM extension collaborative discourse protocol EMNLP 2024 https://arxiv.org/abs/2408.15232
- Resources: FreshWiki dataset recent high-quality Wikipedia articles to avoid data leakage, evaluation criteria outline and final article quality

## Motivation

- Prior work generating Wikipedia articles generally bypassed pre-writing stage: Liu et al 2018 presume reference docs provided in advance multi-document summarization problem, Fan and Gardent 2022 assume outline available focus expanding each section, Balepur et al 2023 one paragraph, Qian et al 2023 one paragraph, Sauper and Barzilay 2009 two domains full article but no references no outline etc Table1 comparison One vs All vs Given Outline Given Refs. Generating one paragraph does not need outline.
- Creating new Wikipedia-like article demands fluent writing plus good research skills. Modern LLMs trained on Wikipedia text, mitigate leakage seeking recent articles created/heavily edited after training cutoff LLMs test. Need to research topic and prepare outline prior to writing (pre-writing stage Rohman 1965 discovery stage). Human educators supervise students at outline stage extensive outline indicates comprehensive understanding solid foundation for full-length article Dietz and Foley 2019. Also educational exercise academic training Tardy 2010.
- As pre-trained LMs inherently possess wealth knowledge, direct approach rely parametric knowledge generating outlines or entire articles (Direct Gen) limited lack details hallucinations Xu et al 2023 particularly long-tail topics Kandpal et al 2023 importance leveraging external sources current strategies RAG circles back problem researching topic pre-writing stage much information cannot be surfaced through simple topic searches.
- Human learning theories Tawfik et al 2020 Booth et al 2003 highlight asking effective questions information acquisition. Instruction-tuned models Ouyang et al 2022 can be prompted directly generate questions but typically produce basic What When Where questions Figure1A which only address surface-level facts. To endow LLMs capacity conduct better research propose STORM paradigm Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking.

## Main contributions

- To evaluate capacity LLM systems generating long-form grounded articles from scratch and pre-writing challenge in particular curate FreshWiki dataset establish evaluation criteria both outline and final article quality
- Propose STORM novel system automates pre-writing stage researches topic creates outline by using LLMs ask incisive questions retrieving trusted information from Internet
- Both automatic and human evaluation demonstrate effectiveness. Expert feedback reveals new challenges generating grounded long-form articles (bias on Internet affects articles, LLMs fabricate connections between unrelated facts - source bias transfer and over-association)
- Overview: STORM identifies core automating research process as automatically coming up with good questions to ask. Directly prompting LM ask questions does not work well. To improve depth breadth questions STORM adopts two strategies: Perspective-Guided Question Asking discovering different perspectives surveying existing articles from similar topics uses them control question-asking process, Simulated Conversation simulating conversation between Wikipedia writer and topic expert grounded in Internet sources enable LM update understanding topic and ask follow-up questions
- Design based two hypotheses: diverse perspectives lead varied questions; formulating in-depth questions requires iterative research. Building upon hypotheses STORM employs multi-stage approach: first discovers diverse perspectives retrieving analyzing Wikipedia articles from similar topics then personifies LLM with specific perspectives for question asking Figure1B; next to elicit follow-up questions for iterative research Figure1C simulates multi-turn conversations where answers grounded on Internet; finally based LLM internal knowledge collected information STORM creates outline that can be expanded section by section develop full-length Wikipedia-like article
- Evaluate using FreshWiki dataset §2.1 curating recent high-quality Wikipedia articles avoid data leakage during pre-training. Define metrics evaluating outline quality against human-written articles. Invite group experienced Wikipedia editors expert evaluation. Editors found STORM outperforms outline-driven RAG baseline especially breadth organization. They also identified challenges addressing cases where bias on Internet affects generated articles, LLMs fabricate connections between unrelated facts. These challenges present new frontiers to grounded writing systems

## FreshWiki dataset Sec 2.1

- Study generating Wikipedia-like articles from scratch placing emphasis pre-writing stage Rohman 1965 which involves demanding sub-tasks gathering curating relevant information research. Models human writing approach prompted some educators view Wikipedia article writing as educational exercise academic training Tardy 2010. Table1 compares work against prior benchmarks for Wikipedia generation. Existing work generally focused evaluating generation shorter snippets e.g. one paragraph within narrower scope e.g. specific domain or two or when explicit outline or reference documents supplied. Notable example WikiSum Liu et al 2018 treats generating Wikipedia articles as multi-document summarization problem w.r.t reference documents. Setup emphasizes capability long-form grounded writing systems to research curate content. Given topic t task find set references R and generate full-length article S = s1 s2 ... sn where each sentence si cites list documents in R. In practice S also includes organizational elements such as section subsection titles which do not require citations.
- Creating new Wikipedia-like article demands not only fluent writing but good research skills. As modern LLMs generally trained on Wikipedia text mitigate leakage seeking recent Wikipedia articles created or very heavily edited after training cutoff LLMs test. Process repeated at future dates when new LLMs emerge.
- To apply date criteria focus on top 100 most-edited pages based edit counts for each month Feb 2022 to Sep 2023. To ensure high-quality references filter articles keep only those having B-class quality or above assessed ORES. Exclude list articles and articles that have no subsections. While high-quality Wikipedia articles usually contain structured data e.g. tables and multi-modal only consider plain text component simplifying task. More details Appendix A.
- Resources code released https://github.com/stanford-oval/storm

## Outline Creation and Evaluation Sec 2.2

- Full-length article hard generate or evaluate Xu et al 2023 Krishna et al 2023. When human educators teach students academic writing sometimes supervise students at outline stage Eriksson and Mäkitalo 2015 because extensive outline indicates comprehensive understanding topic solid foundation writing full-length article Dietz and Foley 2019 inspired decompose generation S into two stages. Pre-writing stage require system create outline O defined as list multi-level section headings. Since LMs process produce sequences linearize O by adding # to indicate section titles ## subsection etc. Writing stage system uses topic t references R outline O produce full-length article S.
- To evaluate outline coverage introduce two metrics heading soft recall and heading entity recall compare multi-level section headings human-written article considered ground truth and those in O. Recognizing exact match between elements in these two sets unnecessary calculate heading soft recall Fränti and Mariescu-Istodor 2023 using cosine similarity derived Sentence-BERT Reimers and Gurevych 2019 embeddings headings details Appendix C1. Also compute heading entity recall quantified as percentage named entities in human-written article headings covered by O extract entities FLAIR NER Akbik et al 2019.

## Method Sec 3 STORM

Present STORM automate pre-writing stage researching given topic via effective question asking Sec3.1 Sec3.2 and creating outline Sec3.3. Outline extended full-length article grounded on collected references Sec3.4 Figure2 overview and pseudocode Appendix B

### Figure2 overview (8 steps):

Related Articles Topic t ① Survey ② Identify Perspectives Draft Outline OD ⑦ Direct Generate References R Question q Answer a Wikipedia Writer ③ Read & Ask Expert ④ Split Queries ⑤ Search & Sift ⑥ Synthesize Add Specific Perspective Outline O Gather Conversations {C',...,C#} ⑧ Refine P Add Trusted Sources

Description: Starting with given topic STORM identifies various perspectives on covering topic by surveying related Wikipedia articles 1-2 then simulates conversations between Wikipedia writer who asks questions guided by given perspective and expert grounded on trustworthy online sources 3-6 final outline curated based LLM intrinsic knowledge and gathered conversations from different perspectives 7-8

### Sec3.1 Perspective-Guided Question Asking

Rohman 1965 defines pre-writing as stage discovery in writing process. In parallel with stakeholder theory business Freeman et al 2010 where diverse stakeholders prioritize varying facets company individuals with distinct perspectives may concentrate different aspects when researching same topic discover multifaceted information. Further...

STORM discovers different perspectives by surveying existing articles from similar topics and uses these perspectives to control question asking process. Specifically STORM prompts LLM to generate list of related topics and subsequently extracts tables of contents from their corresponding Wikipedia articles if such articles can be obtained through Wikipedia API https://pypi.org/project/Wikipedia-API/ Figure2 1. These tables of contents concatenated create context to prompt LLM to identify N perspectives P = {p1,…,pN} that can collectively contribute comprehensive article on t Figure2 2. To ensure basic information about t also covered add p0 as basic fact writer focusing broadly covering basic facts about topic into P. Each perspective p∈P will be utilized to guide LLM process of question asking in parallel

Starting with given topic STORM identifies various perspectives on covering topic by surveying related Wikipedia articles .-. . It then simulates conversations between writer who asks questions guided by given perspective and expert grounded on trustworthy online sources .-. . Final outline curated based LLM intrinsic knowledge and gathered conversations from different perspectives .-.

In §3 we introduce STORM framework automates pre-writing stage by discovering different perspectives, simulating information-seeking conversations, creating comprehensive outline. Algorithm1 displays skeleton.

### Algorithm1 skeleton:

Input Topic t maximum perspective N maximum conversation round M Output Outline O references R
1 P0 = "basic fact writer focusing on broadly covering the basic facts about the topic" Constant
2 R ← []
3 // Discover perspectives P
4 related_topics ← gen_related_topics(t)
5 tocs ← []
6 foreach related_t in related_topics do article ← get_wiki_article(related_t) if article then tocs.append(extract_toc(article)) end end
11 P ← gen_perspectives(t, tocs)
12 P ← [P0] + P[:N]
13 // Simulate conversations
14 convos ← []
15 foreach p in P do convo_history ← [] for i=1 to M do // Question asking q ← gen_qn(t,p,dlg_history) convo_history.append(q) // Question answering queries ← gen_queries(t,q) sources ← search_and_sift(queries) a ← gen_ans(t,q,sources) convo_history.append(a) R.append(sources) end convos.append(convo_history) end
30 // Create outline
31 OD ← direct_gen_outline(t)
32 O ← refine_outline(t, OD, convos)
33 return O,R

We implement STORM with zero-shot prompting using DSPy framework Khattab et al 2023. Listing 1 and 2 show prompts used in implementation. Highlight STORM offers general framework designed to assist creation grounded long-form articles without depending extensively prompt engineering for single domain.

### Prompts Listing1:

GenRelatedTopicsPrompt dspy.Signature """ I'm writing a Wikipedia page for topic mentioned below. Please identify and recommend some Wikipedia pages on closely related subjects. I'm looking for examples that provide insights into interesting aspects commonly associated with this topic, or examples that help me understand typical content and structure included in Wikipedia pages for similar topics. Please list the urls in separate lines. """ Input topic Output related_topics

GenPerspectivesPrompt """ You need to select a group of Wikipedia editors who will work together to create comprehensive article on the topic. Each of them represents different perspective, role, or affiliation related to this topic. You can use other Wikipedia pages of related topics for inspiration. For each editor add description what they will focus on. Give answer format 1. short summary of editor 1: description \n2. short summary of editor 2: description \n... """ Input topic examples = wiki page outlines of related topics for inspiration Output perspectives

GenQnPrompt """ You are experienced Wikipedia writer and want to edit specific page. Besides identity as Wikipedia writer you have specific focus when researching topic. Now you are chatting with expert to get information. Ask good questions to get more useful information. When you have no more question to ask say "Thank you so much for your help!" to end conversation. Please only ask one question at a time and don't ask what you have asked before. Your questions should be related to topic you want to write. """ Input topic persona conv history Output question

GenQueriesPrompt """ You want to answer question using Google search. What do you type in search box? Write queries you will use in following format: - query1 \n- query2 \n... """ Input topic question Output queries

### Prompts Listing2:

GenAnswerPrompt """ You are expert who can use information effectively. You are chatting with Wikipedia writer who wants to write Wikipedia page on topic you know. You have gathered related information and will now use information to form response. Make response as informative as possible and make sure every sentence is supported by gathered information. """ Input topic conv Question Gathered information Output Now give your response

DirectGenOutlinePrompt """ Write an outline for Wikipedia page. Here is format 1. Use "#" Title to indicate section title "##" Title to indicate subsection title "###" Title etc 2. Do not include other information. """ Input Topic you want to write Output Write Wikipedia page outline

RefineOutlinePrompt """ Improve an outline for Wikipedia page. You already have draft outline that covers general information. Now you want to improve it based on information learned from information-seeking conversation to make it more comprehensive. Here is format 1. Use "#" Title... 2. Do not include other information. """ Input Topic you want to write Conversation history Current outline Output Write Wikipedia page outline

Figure1 example 2022 Winter Olympics Opening Ceremony: Direct Prompting Ask 30 questions about topic When was opening held Where how many countries participated basic What When Where. Perspective-Guided: You are event planner focusing preparation opening ceremony ... Conversational: Can you provide list participating countries... Diverse answers transportation arrangements budget etc. Demonstrates perspective-guided leads varied questions, iterative research elicits follow-up in-depth questions transportation budget vs surface facts.

### Sec3.4 Writing full article from outline

Building upon references R collected outline O developed during prewriting stage full-length article can be composed section by section. Section title headings subsections used retrieve relevant documents from R based semantic similarity calculated Sentence-BERT embeddings. LLM then prompted generate section with citations. Once all sections generated concatenated form full-length article. LLM then prompted delete repeated information improve coherence. Furthermore in alignment Wikipedia stylistic norms LLM also utilized synthesize summary entire article forming lead section at beginning. Titles to generate article section by section. Implementation zero-shot prompting DSPy Appendix B includes pseudo code corresponding prompts. Hyperparameters N M both set 5. Use chat model gpt-3.5-turbo for question asking use gpt-3.5-turbo-instruct for other parts. Also experiment using gpt-4 for drafting refining outline Figure2. For reported results simulated topic expert grounded on You.com search API https://documentation.you.com/api-reference/search although pipeline compatible other search engines. Ground truth Wikipedia article excluded from search results.

### Evaluation

Automatic Evaluation Details C1 Soft Heading Recall calculation soft heading recall between multi-level headings generated outline considered prediction P those human-written article considered ground truth G based soft recall definition Fränti and Mariescu-Istodor 2023. Given set A={Ai} soft count inverse sum similarity other items count(Ai)=1 / sum_j Sim(Ai,Aj) Sim=cos embed(Ai),embed(Aj) embed parameterized paraphrase-MiniLM-L6-v2 Sentence-Transformers. Cardinality card(A)=sum_i count(Ai). Soft heading recall = card(G∩P)/card(G) intersection via union card(G∩P)=card(G)+card(P)-card(G∪P).

C2 LLM Evaluator use Prometheus Kim et al 2023 13B open-source evaluator LLM assess long-form text based customized 1-5 scale rubric grade article aspects Interest level Coherence Organization Relevance Focus Coverage Table8 grading rubric while Prometheus best used score 5 reference answer find adding reference exceeds context limit model since Kim et al show Prometheus ratings without reference also correlate well human preferences omit reference trim input article within 2000 words iteratively removing contents from shortest section ensure input fit context window.

C3 Citation Quality: verifying? Calculate citation recall precision based definition Gao et al 2023 use Mistral 7B...

For FreshWiki... etc

Expert evaluation experienced Wikipedia editors...

Results: Compared to articles generated by outline-driven retrieval-augmented baseline more of STORM's articles deemed organized by 25% absolute increase and broad coverage by 10%. Expert feedback helps identify new challenges such as source bias transfer and over-association unrelated facts

Limitations: bias on Internet affects articles, fabricate connections between unrelated facts

## Implementation details STORM library

Installation pip install knowledge-storm, conda create storm python3.11 pip install -r requirements.txt

API support language model components All language models supported by litellm https://docs.litellm.ai/docs/providers, embedding models supported by litellm, retrieval module components YouRM BingSearch VectorRM SerperRM BraveRM SearXNG DuckDuckGoSearchRM TavilySearchRM GoogleSearch AzureAISearch

Both STORM and Co-STORM working information curation layer need set up information retrieval module language model module create Runner classes respectively

STORM knowledge curation engine defined as simple Python STORMWikiRunner class example using You.com search engine and OpenAI models: from knowledge_storm import STORMWikiRunnerArguments STORMWikiRunner STORMWikiLMConfigs from knowledge_storm.lm import LitellmModel from knowledge_storm.rm import YouRM lm_configs = STORMWikiLMConfigs openai_kwargs api_key temperature 1.0 top_p 0.9 STORM LM system so different components can be powered by different models to reach good balance cost quality For good practice choose cheaper/faster model for conv_simulator_lm used split queries synthesize answers conversation Choose more powerful model for article_gen_lm generate verifiable text with citations etc conv_simulator_lm question_asker_lm outline_gen_lm article_gen_lm article_polish_lm max_conv_turn 4 max_perspective 3 search_top_k 10 max_thread_num 1 device cpu vector_db_mode offline do_research etc Initialize engine arguments STORMWikiRunnerArguments output_dir max_conv_turn max_perspective search_top_k max_thread_num Setup VectorRM retrieve information own data rm = VectorRM collection_name embedding_model device k search_top_k init_offline_vector_db vector_store_path db_dir Initialize STORM Wiki Runner runner = STORMWikiRunner engine_args engine_lm_configs rm Set instructions for STORM AI Research algorithm runner=set_instructions(runner) run pipeline runner.run topic do_research do_generate_outline do_generate_article do_polish_article runner.post_run runner.summary generate_markdown_article output_dir

Co-STORM collaborative discourse protocol turn management policy support smooth collaboration among Co-STORM LLM experts generates answers grounded on external knowledge sources and/or raises follow-up questions based discourse history Moderator generates thought-provoking questions inspired by information discovered retriever but not directly used previous turns Question generation grounded! Human user takes initiative either observe discourse gain deeper understanding topic or actively engage conversation injecting utterances steer discussion focus. Co-STORM also maintains dynamic updated mind map organize collected information hierarchical concept structure aiming build shared conceptual space between human user and system mind map proven help reduce mental load when discourse goes long in-depth

Both implemented highly modular using dspy

Latest News: litellm integration v1.1.0 Jan 2025, Co-STORM codebase released integrated knowledge-storm v1.0.0 pip install --upgrade Sep 2024, collaborative STORM Co-STORM to support human-AI collaborative knowledge curation EMNLP 2024 main conference Sep 2024, install package pip install knowledge-storm Jul 2024, VectorRM to support grounding on user-provided documents complementing existing YouRM BingSearch etc Jul 2024, demo light streamlit Jul 2024, Bing Search support rm.py test GPT-4o etc May 2024, refactored version defining interface knowledge_storm/interface.py reimplement STORM-wiki src/storm_wiki to demonstrate instantiate pipeline provide API support customization different LMs retrieval/search integration Apr 2024

## Relation to other systems

- Provides pre-writing research paradigm vs GAPMAP gap identification (perspective failure identification), ResearchAgent context-augmented planner perspective, Scientific Intelligence Survey P2 Context-Augmented P5 Role-Interactive P3 Deliberative Reflective V2 tool-based V3 HITL expert oversight (Wikipedia editors)
- SciMON iterative novelty boosting vs STORM perspective-guided questioning different optimization novelty vs breadth organization
- STORM perspective-guided question asking mirrors ResearchAgent entity retrieval cross-domain pollination but for Wikipedia broad coverage
