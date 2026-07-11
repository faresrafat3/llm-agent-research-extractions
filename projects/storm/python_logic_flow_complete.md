
# STORM — Python Logic Flow Complete

Audited commit main knowledge-storm package + PDF Algorithm 1 Listings 1-2

---

## 0. Entry point STORMWikiRunner

```
STORMWikiRunnerArguments:
  output_dir
  max_conv_turn = 4 or 5 (M)
  max_perspective = 3 or 5 (N)
  search_top_k = 10
  max_thread_num = 1
  device = cpu
  vector_db_mode = offline/online

STORMWikiLMConfigs:
  conv_simulator_lm = gpt-3.5-turbo (cheap/fast split queries synthesize answers conversation)
  question_asker_lm = gpt-3.5-turbo
  outline_gen_lm = gpt-4 more powerful organizing collected info
  article_gen_lm = gpt-4 more powerful verifiable text citations
  article_polish_lm = gpt-4

Retrieval module RM:
  YouRM You.com search API documentation.you.com/api-reference/search
  BingSearch, VectorRM collection_name embedding_model device k search_top_k init_offline_vector_db vector_store_path db_dir Qdrant, SerperRM, BraveRM, SearXNG, DuckDuckGoSearchRM, TavilySearchRM, GoogleSearch, AzureAISearch

Runner = STORMWikiRunner(engine_args, engine_lm_configs, rm)
runner = set_instructions(runner)  # custom instructions for research algorithm
runner.run(topic=topic, do_research=True, do_generate_outline=True, do_generate_article=True, do_polish_article=True)
runner.post_run()
runner.summary()
generate_markdown_article(output_dir)
```

---

## 1. Pre-writing stage logic detailed Algorithm 1

```
Input Topic t, maximum perspective N=5, maximum conversation round M=5
Output Outline O, references R

1 P0 = "basic fact writer focusing on broadly covering the basic facts about the topic" // Constant to ensure basic information coverage
2 R <- []
3 // Discover perspectives P.
4 related_topics <- gen_related_topics(t)  // GenRelatedTopicsPrompt dspy: I'm writing Wikipedia page for topic mentioned below. Please identify recommend Wikipedia pages on closely related subjects insights interesting aspects commonly associated or help understand typical content structure included in Wikipedia pages similar topics. List urls separate lines.
5 tocs <- []
6 foreach related_t in related_topics do
    article <- get_wiki_article(related_t) via Wikipedia-API https://pypi.org/project/Wikipedia-API/
    if article then tocs.append(extract_toc(article))
  end
11 P <- gen_perspectives(t, tocs) // GenPerspectivesPrompt: You need select group Wikipedia editors who will work together to create comprehensive article on topic Each represents different perspective role affiliation related to topic You can use other Wikipedia pages related topics inspiration For each editor add description what they will focus on Give answer format 1. short summary editor1: description...
12 P <- [P0] + P[:N]  // Add basic fact writer + N perspectives
13 // Simulate conversations.
14 convos <- []
15 foreach p in P do   // Parallel perspectives N+1 including p0
    convo_history <- []
    for i=1 to M do
      // Question asking.
      q <- gen_qn(t,p,dlg_history) // GenQnPrompt: You are experienced Wikipedia writer want edit specific page Besides identity as Wikipedia writer you have specific focus when researching topic Now you are chatting with expert to get information Ask good questions to get more useful information When you have no more question to ask say Thank you so much for your help! to end conversation Please only ask one question at a time don't ask what you have asked before Your questions should be related to topic you want to write. Input topic persona conv history Output question
      convo_history.append(q)
      // Question answering.
      queries <- gen_queries(t,q) // GenQueriesPrompt: You want answer question using Google search What do you type search box? Write queries format - query1 - query2...
      sources <- search_and_sift(queries) // Search via YouRM You.com search API search_top_k 10, ground truth Wikipedia article excluded, search_and_sift filters trusted sources
      a <- gen_ans(t,q,sources) // GenAnswerPrompt: You are expert who can use information effectively chatting with Wikipedia writer who wants write Wikipedia page on topic you know You have gathered related information will now use information to form response Make response as informative as possible make sure every sentence is supported by gathered information Input topic Question Gathered info Output Now give your response
      convo_history.append(a)
      R.append(sources)  // Collect references
    end
    convos.append(convo_history) // Gather conversations {C0,...,CN} each C contains M Q/A pairs
  end
30 // Create outline.
31 OD <- direct_gen_outline(t) // DirectGenOutlinePrompt: Write outline for Wikipedia page format Use "#" Title to indicate section title "##" Title subsection "###" subsubsection etc Do not include other information Input topic Output Write Wikipedia page outline This leverages internal knowledge LLM provides general but organized framework
32 O <- refine_outline(t, OD, convos) // RefineOutlinePrompt: Improve outline for Wikipedia page You already have draft outline covering general info Now you want improve based on information learned from information-seeking conversation to make it more comprehensive Format same # ## ### Input topic Conversation history Current outline Output Write Wikipedia page outline Resulting improved outline O used for producing full-length article
33 return O,R
```

Note: Implementation zero-shot prompting using DSPy framework Khattab et al 2023 Listing1 Listings correspond Line 4,11,19,22 Algorithm1 Listing2 24,31,32

Figure1 flow: Research via Question Asking 2022 Winter Olympics Opening Ceremony example. (A) Direct Prompting Ask 30 questions When was opening ceremony held? Where? How many countries? basic What When Where limited planning capacity. (B) Perspective-Guided Question Asking You are event planner who focuses on preparation opening ceremony ... leads varied questions transportation arrangements budget cultural broadcasting security etc different perspectives lead varied questions. (C) Conversational Question Asking Can you provide list participating countries ... Answer diverse group over 90 countries entering stadium specific order How is order determined? Can you provide information transportation arrangements? budget? ... To elicit follow-up questions iterative research simulating multi-turn conversations where answers grounded Internet. Finally based LLM internal knowledge collected information STORM creates outline expanded section by section develop full-length Wikipedia-like article.

---

## 2. Writing stage logic

```
Input: Topic t, Outline O (list multi-level section headings # ## ### linearized), References R collected pre-writing stage

Building upon references R collected outline O developed during prewriting stage full-length article composed section by section.
Section title headings subsections used retrieve relevant documents from R based semantic similarity calculated Sentence-BERT embeddings.

For each section in O:
  relevant_docs = retrieve from R via Sentence-BERT similarity using section title + subheadings as query
  Prompt LLM to generate section with citations (every sentence supported by references)
  Section text with citations [1][2] format

Once all sections generated concatenated form full-length article.

LLM then prompted to delete repeated information to improve coherence (polish stage):
  Input draft article concatenated sections
  Output polished article

Furthermore in alignment Wikipedia stylistic norms LLM also utilized to synthesize summary entire article forming lead section at beginning (lead synthesis):
  Input polished article
  Output lead section 2-3 paragraphs concise overview main points

Titles to generate article section by section.

Example hyperparams max_conv_turn 4 max_perspective 3 search_top_k 10 max_thread_num 1 device cpu vector_db_mode offline do_research do_generate_outline do_generate_article do_polish_article True
```

Implementation example code from GitHub README + medium article:

```
lm_configs = STORMWikiLMConfigs()
openai_kwargs = {'api_key': os.getenv("OPENAI_API_KEY"), 'temperature':1.0, 'top_p':0.9}
STORM is LM system different components powered different models to reach balance cost quality
For good practice cheaper/faster model for conv_simulator_lm used split queries synthesize answers conversation
Choose more powerful model for article_gen_lm generate verifiable text citations
conv_simulator_lm = ModelClass(model=gpt_35_model_name, max_tokens=10000, **openai_kwargs)
question_asker_lm = ModelClass(model=gpt_35_model_name, max_tokens=10000, **openai_kwargs)
outline_gen_lm = ModelClass(model=gpt_4_model_name, max_tokens=10000, **openai_kwargs)
article_gen_lm = ModelClass(model=gpt_4_model_name, max_tokens=10000, **openai_kwargs)
article_polish_lm = ModelClass(model=gpt_4_model_name, max_tokens=10000, **openai_kwargs)
elif model_type == "ollama": ...
engine_lm_configs.set_conv_simulator_lm(conv_simulator_lm) ...

max_conv_turn=4 max_perspective=3 search_top_k=10 max_thread_num=1 device="cpu" vector_db_mode="offline" do_research=True etc

Initialize engine arguments output_dir engine_args = STORMWikiRunnerArguments(output_dir, max_conv_turn, max_perspective, search_top_k, max_thread_num)

Setup VectorRM to retrieve information from own data rm = VectorRM(collection_name, embedding_model, device, k=search_top_k) init_offline_vector_db...

Initialize STORM Wiki Runner runner = STORMWikiRunner(engine_args, engine_lm_configs, rm)
Set instructions runner = set_instructions(runner)
run pipeline runner.run(topic=topic, do_research=do_research, do_generate_outline=do_generate_outline, do_generate_article=do_generate_article, do_polish_article=do_polish_article)
runner.post_run()
runner.summary()
generate_markdown_article(output_dir)
```

---

## 3. FreshWiki dataset creation logic

```
To mitigate data leakage explicitly seeking recent Wikipedia articles created or very heavily edited after training cutoff LLMs test. Process repeated future dates when new LLMs emerge.
Focus top 100 most-edited pages based edit counts for each month Feb 2022 to Sep 2023 via https://wikimedia.org/api/rest_v1/metrics/edited-pages/top-by-edits/en.wikipedia/all-editor-types/content/{year}/{month}/all-days
Filter keep only those having B-class quality or above assessed ORES https://www.mediawiki.org/wiki/ORES
Exclude list articles https://en.wikipedia.org/wiki/Wikipedia:Stand-alone_lists and articles that have no subsections
While high-quality Wikipedia articles usually contain structured data e.g. tables and multi-modal only consider plain text component simplifying task
More details Appendix A
Resources code released https://github.com/stanford-oval/storm
```

Dataset comparison Table1: Domain Scope Given Outline Given Refs
Balepur et al One One para / Yes
Qian et al All One para / No
Fan and Gardent One Full article Yes No
Liu et al All One para / Yes
Sauper and Barzilay Two Full article No No
Ours All Full article No No

Our setup emphasizes capability long-form grounded writing systems to research curate content Given topic t task find set references R and generate full-length article S = s1 s2 ... sn where each sentence si cites list documents in R In practice S also includes organizational elements such as section subsection titles which do not require citations.

---

## 4. Outline evaluation metrics logic

```
Outline Creation Evaluation: Full-length article hard generate or evaluate Xu et al 2023 Krishna et al 2023 Human educators teach students academic writing sometimes supervise students at outline stage Eriksson and Mäkitalo 2015 because extensive outline indicates comprehensive understanding topic solid foundation writing full-length article Dietz and Foley 2019 inspired decompose generation S into two stages Pre-writing stage require system create outline O defined as list multi-level section headings Since LMs process produce sequences linearize O by adding # to indicate section titles ## subsection etc Writing stage system uses topic t references R outline O produce full-length article S

To evaluate outline coverage introduce two metrics heading soft recall and heading entity recall compare multi-level section headings human-written article considered ground truth and those in O Recognizing exact match unnecessary calculate heading soft recall Fränti and Mariescu-Istodor 2023 using cosine similarity derived Sentence-BERT Reimers and Gurevych 2019 embeddings headings details Appendix C1 Also compute heading entity recall quantified as percentage named entities in human-written article headings covered by O extract entities FLAIR NER Akbik et al 2019

Soft Heading Recall calculation:
Given set A={Ai}K_i=1 soft count inverse sum similarity other items in set:
count(Ai)=1 / sum_j Sim(Ai,Aj) Sim=cos(embed(Ai),embed(Aj)) embed parameterized paraphrase-MiniLM-L6-v2 Sentence-Transformers https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
Cardinality card(A)=sum_i count(Ai)
Soft heading recall = card(G∩P)/card(G) where G ground truth human-written headings P predicted outline headings Intersection via union card(G∩P)=card(G)+card(P)-card(G∪P)

Heading entity recall: percentage named entities in human-written article headings covered by O FLAIR
```

---

## 5. Automatic article quality evaluation

```
LLM Evaluator: Use Prometheus Kim et al 2023 13B open-source evaluator LLM assess long-form text based customized 1-5 scale rubric grade article aspects Interest level Coherence and Organization Relevance and Focus Coverage Table8 grading rubric While Prometheus best used with score 5 reference answer find adding reference exceeds context length limit model Since Kim et al show Prometheus ratings without reference also correlate well human preferences omit reference trim input article within 2000 words iteratively removing contents from shortest section ensure input fit model context window

Citation Quality: For verifiability calculate citation recall precision based definition Gao et al 2023 Use Mistral 7B etc LLMs hard compare directly Instead ...

Sentence-BERT embeddings relevant info retrieval section generation

Expert evaluation experienced Wikipedia editors: STORM outperforms outline-driven RAG baseline especially breadth organization more articles deemed organized by 25% absolute increase broad coverage by 10%

Expert feedback challenges: bias on Internet affects generated articles source bias transfer; LLMs fabricate connections between unrelated facts over-association
```

---

## 6. Decision catalog

| ID | Decision | Location |
|---|---|---|
| D1 | Discover perspectives via related topics TOCs vs direct prompting 30 questions | GenRelatedTopicsPrompt vs Direct |
| D2 | N perspectives =5 plus p0 basic fact writer vs single perspective | Algorithm1 line 12 |
| D3 | M conversation rounds =5 vs 1 | Algorithm1 loop i=1..M |
| D4 | Retrieval engine YouRM You.com vs BingSearch vs VectorRM user docs etc | rm.py knowledge_storm/rm.py litellm integration |
| D5 | Search queries generation via GenQueriesPrompt vs direct question as query | GenQueriesPrompt |
| D6 | Ground truth Wikipedia article excluded search results? yes | Sec 3.4 |
| D7 | Draft outline OD from topic only vs refined O from topic+OD+convos | DirectGenOutlinePrompt vs RefineOutlinePrompt |
| D8 | Section generation retrieve relevant docs from R via Sentence-BERT similarity vs using all R | Writing stage |
| D9 | Polish delete repeated info vs keep raw concatenation | Polish stage |
| D10 | Lead summary synthesis Wikipedia stylistic norms vs no lead | Lead synthesis |
| D11 | LM choice gpt-3.5-turbo question asking vs gpt-3.5-turbo-instruct other parts vs gpt-4 drafting refining vs ollama local | STORMWikiLMConfigs |
| D12 | Vector DB mode offline Qdrant vs online | VectorRM |
| D13 | FreshWiki filtering B-class ORES exclude list no subsections plain text only | Dataset creation |
| D14 | Evaluation Prometheus 13B 1-5 rubric without reference trimmed 2000 words vs with reference | C2 |
| D15 | Hyperparameters search_top_k 10 max_thread_num 1 device cpu etc | Engine arguments |

---

## 7. Loop inventory

| Loop | Bound | File/Location |
|---|---|---|
| related_topics generation | list of related topics | gen_related_topics t |
| tocs extraction foreach related_t get_wiki_article extract_toc | len(related_topics) | Algorithm1 6-10 |
| perspectives P = [P0]+P[:N] | N=5 | Algorithm1 11-12 |
| Simulate conversations foreach p in P | N+1 =6 perspectives | Algorithm1 15 |
| Conversation rounds for i=1..M | M=5 | Algorithm1 17 |
| Question asking gen_qn | per round | 19 |
| Query generation gen_queries | per question | 22 |
| Search and sift search_and_sift queries | per queries search_top_k 10 | 23 |
| Answer generation gen_ans | per sources | 24 |
| R append sources | per turn | 26 |
| convos append convo_history | per perspective | 28 |
| Outline creation direct_gen_outline + refine_outline | 2 calls | 31-32 |
| Section-by-section generation for each section in O | len(O) sections | Writing stage |
| Sentence-BERT retrieval relevant docs from R per section | len(R) | Writing stage |
| Polish article delete repeated | 1 call | Writing stage |
| Lead summary synthesis | 1 call | Writing stage |
| FreshWiki top 100 most-edited per month Feb2022-Sep2023 | 20 months *100 =2000 raw then filter | Dataset |
| Heading soft recall calculation count(Ai) sum_j Sim | K items per set | C1 |
| Prometheus evaluation trimming iterative removing shortest section until 2000 words | until fit | C2 |

---

## 8. I/O summary

| Stage | Input | Output |
|---|---|---|
| gen_related_topics | topic t | related_topics URLs list |
| get_wiki_article extract_toc | related_t | tocs list TOCs concatenated |
| gen_perspectives | topic t + tocs examples wiki outlines related topics for inspiration | perspectives P = {p1..pN} |
| gen_qn | topic t + persona perspective p + conv history | question q |
| gen_queries | topic t + question q | queries - query1 - query2 ... |
| search_and_sift | queries | sources filtered trusted sources search_top_k |
| gen_ans | topic t + question conv + gathered info | answer a informative every sentence supported |
| direct_gen_outline | topic t | draft outline OD general framework # ## ### |
| refine_outline | topic t + OD + convos {C0..CN} | improved outline O comprehensive # ## ### |
| section generation | topic + outline O + relevant docs from R via Sentence-BERT similarity | section text with citations [1][2] |
| polish | draft article concatenated sections | polished article coherence improved |
| lead summary | polished article | lead section 2-3 paragraphs Wikipedia stylistic norms |
| FreshWiki dataset | top 100 most-edited per month + ORES B-class filter + exclude list no subsections + plain text only | FreshWiki recent high-quality articles avoiding leakage |
| heading soft recall | prediction P headings + ground truth G headings | soft heading recall card(G∩P)/card(G) |
| heading entity recall | prediction P + ground truth G headings + FLAIR NER | percentage entities covered |
| Prometheus evaluation | input article trimmed 2000 words shortest section removal iterative | Interest Coherence Organization Relevance Focus Coverage 1-5 |

---

## 9. Key decisions preserved

- Perspective discovery via surveying related Wikipedia articles TOCs concatenated to prompt LLM identify N perspectives + p0 basic fact writer focusing broadly covering basic facts ensures breadth vs direct prompting 30 questions produces basic What When Where
- Simulated multi-turn conversations N+1 * M = ~30 Q/A pairs with search_and_sift grounding iterative research elicits follow-up in-depth questions transportation arrangements budget vs surface facts
- Draft outline from intrinsic knowledge then refined with conversations leverages both LLM internal knowledge and collected information comprehensive
- Section-by-section generation retrieving relevant docs from R via Sentence-BERT similarity ensures grounding citations every sentence supported
- Polish delete repeated info improve coherence + lead summary Wikipedia stylistic norms
- Evaluation heading soft recall paraphrase-MiniLM-L6-v2 cosine + entity recall FLAIR + Prometheus 13B 1-5 rubric Interest Coherence Organization Relevance Focus Coverage + citation recall precision Gao et al Mistral 7B + expert Wikipedia editors organized +25% absolute broad coverage +10% vs outline-driven RAG baseline
- Challenges identified source bias transfer bias on Internet affects articles + over-association unrelated facts fabricate connections between unrelated facts new frontiers grounded writing systems
