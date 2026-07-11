# STORM — Complete Prompt Extraction

Source: arXiv:2402.14207 Listings 1-2 + Algorithm 1 + Figure 1-2 + Sec 3.1-3.4

Audited via fitz extraction /tmp/2402.14207.txt

---

## 1. GenRelatedTopicsPrompt — Line 4 Algorithm 1

**DSPy Signature:**

```python
class GenRelatedTopicsPrompt(dspy.Signature):
    """
    I'm writing a Wikipedia page for a topic mentioned below. Please identify and
    recommend some Wikipedia pages on closely related subjects. I'm looking for
    examples that provide insights into interesting aspects commonly associated
    with this topic , or examples that help me understand the typical content and
    structure included in Wikipedia pages for similar topics.

    Please list the urls in separate lines.
    """

    topic = dspy.InputField(prefix=" Topic of interest:", format=str)
    related_topics = dspy.OutputField()
```

**Use:** Input topic t, output list of related topics Wikipedia URLs. Prompt LLM to generate list related topics. Subsequently extracts tables of contents from corresponding Wikipedia articles if obtainable via Wikipedia API https://pypi.org/project/Wikipedia-API/ Figure2 1. These TOCs concatenated create context to prompt LLM to identify N perspectives.

**Example for 2022 Winter Olympics opening ceremony:** related topics might be Winter Olympics history, opening ceremonies of other Olympics, Beijing National Stadium, etc.

---

## 2. GenPerspectivesPrompt — Line 11 Algorithm 1

```python
class GenPerspectivesPrompt(dspy.Signature):
    """
    You need to select a group of Wikipedia editors who will work together to create
    a comprehensive article on the topic. Each of them represents a different
    perspective , role , or affiliation related to this topic. You can use other
    Wikipedia pages of related topics for inspiration. For each editor , add
    description of what they will focus on.

    Give your answer in the following format: 1. short summary of editor 1:
    description\n2. short summary of editor 2: description\n...
    """

    topic = dspy.InputField(prefix='Topic of interest:', format=str)
    examples = dspy.InputField(prefix='Wiki page outlines of related topics for\ninspiration :\n', format=str)
    perspectives = dspy.OutputField()
```

**Use:** Input topic + examples = wiki page outlines of related topics for inspiration (TOCs concatenated). Output perspectives P = {p1..pN} that collectively contribute comprehensive article on t Figure2 2. To ensure basic information coverage add p0 = "basic fact writer focusing on broadly covering the basic facts about the topic" into P. Each perspective p∈P utilized to guide LLM question asking in parallel. N hyperparameter 5.

**Format expected:** 1. short summary of editor 1: description of what they will focus on ...

**Example perspective types (implicit):** event planner focusing preparation opening ceremony, transportation arrangements, budget, cultural significance, broadcasting, security, etc.

---

## 3. GenQnPrompt — Line 19 Algorithm 1 (Question Asking)

```python
class GenQnPrompt(dspy.Signature):
    """
    You are an experienced Wikipedia writer and want to edit a specific page.
    Besides your identity as a Wikipedia writer , you have a specific focus when
    researching the topic.

    Now , you are chatting with an expert to get information. Ask good questions to
    get more useful information.

    When you have no more question to ask , say "Thank you so much for your help!" to
    end the conversation.

    Please only ask one question at a time and don't ask what you have asked before.
    Your questions should be related to the topic you want to write.
    """

    topic = dspy.InputField(prefix='Topic you want to write: ', format=str)
    persona = dspy.InputField(prefix='Your specific perspective: ', format=str)
    conv = dspy.InputField(prefix='Conversation history :\n', format=str)
    question = dspy.OutputField()
```

**Use:** Input topic t, persona perspective p, conversation history dlg_history (questions and answers so far). Output next question q = gen_qn(t,p,dlg_history) Figure2 3 Read & Ask. Hyperparameter M =5 rounds per perspective. Simulated conversations denoted {C0,C1,…,CN} N+1 conversations each M turns.

**Direct prompting baseline comparison:** Prompt: Ask 30 questions about given topic. Example: When was opening ceremony held? Where? How many countries participated? ... surface-level basic What When Where Figure1A. Perspective-Guided Question Asking: You are an event planner who focuses on preparation of opening ceremony ... leads varied questions. Conversational Question Asking: Can you provide list participating countries ... Answer: Diverse group over 90 countries entering stadium specific order. Follow-up: How is order determined? Can you provide information transportation arrangements? budget for 2022 Winter Olympics opening ceremony? ... elicits iterative research follow-up in-depth questions transportation budget Figure1C vs surface facts.

---

## 4. GenQueriesPrompt — Line 22 Algorithm 1 (Query Generation for search)

```python
class GenQueriesPrompt(dspy.Signature):
    """
    You want to answer the question using Google search. What do you type in the
    search box?

    Write the queries you will use in the following format:- query 1\n- query 2\n...
    """

    topic = dspy.InputField(prefix='Topic you are discussing about: ', format=str)
    question = dspy.InputField(prefix='Question you want to answer: ', format=str)
    queries = dspy.OutputField()
```

**Use:** Input topic t and question q to answer. Output search queries that will be typed into Google search box. Format - query1 newline - query2 ... This is step ④ Split Queries Figure2. Then search_and_sift(queries) via You.com search API (or BingSearch, VectorRM, SerperRM etc) to collect sources. Ground truth Wikipedia article excluded search results. search_top_k hyperparameter 10, max_thread_num 1 etc. Step ⑤ Search & Sift.

---

## 5. GenAnswerPrompt — Line 24 Algorithm 1 (Answer generation grounded)

```python
class GenAnswerPrompt(dspy.Signature):
    """
    You are an expert who can use information effectively. You are chatting with a
    Wikipedia writer who wants to write a Wikipedia page on topic you know. You
    have gathered the related information and will now use the information to
    form a response.

    Make your response as informative as possible and make sure every sentence is
    supported by the gathered information.
    """

    topic = dspy.InputField(prefix='Topic you are discussing about:', format=str)
    conv = dspy.InputField(prefix='Question :\n', format=str)
    info = dspy.InputField(prefix='Gathered information :\n', format=str)
    answer = dspy.OutputField(prefix='Now give your response :\n')
```

**Use:** Expert grounded on trusted Internet sources. Input topic t, conv Question (q), gathered information info = sources from search_and_sift. Output answer a = gen_ans(t,q,sources) Figure2 ⑥ Synthesize. Make every sentence supported by gathered information. This is chat with Wikipedia writer.

---

## 6. DirectGenOutlinePrompt — Line 31 Algorithm 1 (Draft outline from intrinsic knowledge)

```python
class DirectGenOutlinePrompt(dspy.Signature):
    """
    Write an outline for a Wikipedia page.

    Here is the format of your writing:

    1. Use "#" Title" to indicate section title , "##" Title" to indicate
    subsection title , "###" Title" to indicate subsubsection title , and so
    on.

    2. Do not include other information.
    """

    topic = dspy.InputField(prefix=" Topic you want to write: ", format=str)
    outline = dspy.OutputField(prefix=" Write the Wikipedia page outline :\n")
```

**Use:** DirectGenOutlinePrompt prompts LLM to generate draft outline OD given only topic t Figure2 ⑦ Direct Generate. OD typically provides general but organized framework leveraging internal knowledge LLMs. Format uses # Title, ## Title, ### Title etc. No other info.

---

## 7. RefineOutlinePrompt — Line 32 Algorithm 1 (Refine outline with conversations)

```python
class RefineOutlinePrompt(dspy.Signature):
    """
    Improve an outline for a Wikipedia page. You already have a draft outline that
    covers the general information. Now you want to improve it based on the
    information learned from an information -seeking conversation to make it more
    comprehensive.

    Here is the format of your writing:

    1. Use "#" Title" to indicate section title , "##" Title" to indicate
    subsection title , "###" Title" to indicate subsubsection title , and so
    on.

    2. Do not include other information.
    """

    topic = dspy.InputField(prefix=" Topic you want to write: ", format=str)
    conv = dspy.InputField(prefix=" Conversation history :\n", format=str)
    old_outline = dspy.OutputField(prefix=" Current outline :\n", format=str)
    outline = dspy.OutputField(prefix='Write the Wikipedia page outline :\n')
```

**Use:** Input topic t, conv = simulated conversations {C0,C1,…,CN} collected N+1 perspectives each M rounds, old_outline = OD draft. Output improved outline O which will be used for producing full-length article Figure2 ⑧ Refine. Subsequently LLM prompted with topic t draft outline OD and simulated conversations to refine outline resulting improved outline O. This leverages internal knowledge + gathered conversations from different perspectives.

---

## 8. Algorithm 1 Pseudocode Skeleton (STORM)

```
Algorithm 1: STORM
Input: Topic t, maximum perspective N, maximum conversation round M
Output: Outline O, references R
1 P0 = "basic fact writer focusing on broadly covering the basic facts about the topic" // Constant
2 R ← []
3 // Discover perspectives P.
4 related_topics ← gen_related_topics(t)  // GenRelatedTopicsPrompt
5 tocs ← []
6 foreach related_t in related_topics do
    article ← get_wiki_article(related_t)
    if article then tocs.append(extract_toc(article))
  end
11 P ← gen_perspectives(t, tocs)  // GenPerspectivesPrompt
12 P ← [P0] + P[:N]
13 // Simulate conversations.
14 convos ← []
15 foreach p in P do
    convo_history ← []
    for i=1 to M do
      // Question asking.
      q ← gen_qn(t, p, dlg_history)  // GenQnPrompt
      convo_history.append(q)
      // Question answering.
      queries ← gen_queries(t, q)  // GenQueriesPrompt
      sources ← search_and_sift(queries)  // YouRM You.com search API search_top_k 10, ground truth excluded
      a ← gen_ans(t, q, sources)  // GenAnswerPrompt
      convo_history.append(a)
      R.append(sources)
    end
    convos.append(convo_history)
  end
30 // Create outline.
31 OD ← direct_gen_outline(t)  // DirectGenOutlinePrompt
32 O ← refine_outline(t, OD, convos)  // RefineOutlinePrompt
33 return O,R
```

Hyperparameters N=5 M=5 both set 5. Use chat model gpt-3.5-turbo for question asking and gpt-3.5-turbo-instruct for other parts of STORM. Also experiment using gpt-4 for drafting refining outline Figure2. For reported results simulated topic expert grounded on You.com search API although pipeline compatible other search engines BingSearch VectorRM etc (knowledge-storm rm.py). Ground truth Wikipedia article excluded from search results.

---

## 9. Full-length Article Generation Prompts (post pre-writing)

After pre-writing stage, given topic t outline O references R collected, full-length article S = s1 s2 ... sn each sentence si cites list documents in R.

Process:

- Building upon references R collected outline O developed during prewriting stage full-length article composed section by section. Section title headings subsections used retrieve relevant documents from R based semantic similarity calculated Sentence-BERT embeddings. LLM then prompted to generate section with citations.
- Once all sections generated concatenated form full-length article. LLM then prompted to delete repeated information improve coherence. Furthermore in alignment Wikipedia stylistic norms LLM also utilized to synthesize summary entire article forming lead section at beginning.
- Titles to generate article section by section (implementation detail Sec 3.4)

**Reconstructed section generation prompt (from description):**

```text
You are writing a section for a Wikipedia page on topic {{topic}}.

Outline:
{{outline_O}}

Section to write: {{section_title}}
Subsections: {{subheadings}}

Relevant references (retrieved from R based on semantic similarity Sentence-BERT):
{{relevant_docs}}

Task: Write this section with citations. Every claim should be supported by references. Use format [1][2] etc. to cite.

Make section comprehensive, coherent, grounded.

Write section:
```

**Polish prompt (delete repeated):**

```text
You have written a full-length Wikipedia article draft with sections:

{{draft_article}}

Task: Delete repeated information across sections to improve coherence while preserving coverage and citations.

Return polished article.
```

**Lead summary prompt (Wikipedia lead):**

```text
You have a full-length Wikipedia article:

{{polished_article}}

In alignment with Wikipedia stylistic norms, synthesize a summary of entire article forming lead section at beginning. Lead should be concise overview 2-3 paragraphs capturing main points.

Return lead section.
```

---

## 10. FreshWiki Evaluation Prompts / Metrics (not LLM prompts but evaluation formulas)

- Heading soft recall: Given set A={Ai} soft count = inverse sum similarity to other items count(Ai)=1 / sum_j Sim(Ai,Aj) Sim=cos embed(Ai) embed(Aj) embed parameterized paraphrase-MiniLM-L6-v2 Sentence-Transformers library. Cardinality card(A)=sum_i count(Ai). Soft heading recall = card(G∩P)/card(G) where intersection via union card(G∩P)=card(G)+card(P)-card(G∪P). Compares multi-level headings prediction P vs ground truth G human-written article considered ground truth.
- Heading entity recall: percentage named entities in human-written article headings covered by O extract entities FLAIR NER Akbik et al 2019.
- LLM Evaluator: Prometheus Kim et al 2023 13B open-source evaluator LLM assess long-form text based customized 1-5 scale rubric grade article aspects Interest level Coherence and Organization Relevance and Focus Coverage Table8 grading rubric while best used with score 5 reference answer find adding reference exceeds context limit model since Kim et al show Prometheus ratings without reference also correlate well human preferences omit reference trim input article within 2000 words iteratively removing contents shortest section ensure fit context window.
- Citation recall precision based definition Gao et al 2023 use Mistral 7B etc.
- Expert evaluation experienced Wikipedia editors organized +25% absolute broad coverage +10% vs outline-driven RAG baseline.

---

## 11. Co-STORM Extension (collaborative)

From GitHub README:

- Collaborative discourse protocol turn management policy to support smooth collaboration among Co-STORM LLM experts Type generates answers grounded on external knowledge sources and/or raises follow-up questions based discourse history, Moderator generates thought-provoking questions inspired by information discovered retriever but not directly used previous turns Question generation also grounded!, Human user takes initiative either observe discourse gain deeper understanding topic or actively engage conversation injecting utterances steer discussion focus.
- Co-STORM maintains dynamic updated mind map organize collected information hierarchical concept structure aiming build shared conceptual space between human user system mind map proven help reduce mental load when discourse goes long in-depth
- Highly modular using dspy

**Co-STORM perspective prompts (reconstructed):**

```text
You are a Co-STORM LLM expert. Generate answer grounded on external knowledge sources and/or raise follow-up question based on discourse history:
History: {{discourse_history}}
Retrieved info: {{retrieved}}
Task: Provide grounded answer with citations and optionally follow-up question.

Moderator prompt:
You are Moderator. Generate thought-provoking questions inspired by information discovered by retriever but not directly used in previous turns. Question generation grounded!
History: {{discourse_history}}
Unused retrieved info: {{unused}}
Generate probing question.
```

---

## 12. Prompt wiring map

| Prompt | Algorithm Line | Input | Output | Role |
|---|---|---|---|---|
| GenRelatedTopicsPrompt | 4 | topic | related_topics URLs | Survey related Wikipedia articles for inspiration |
| GenPerspectivesPrompt | 11 | topic + tocs examples wiki outlines related topics | perspectives P = {p1..pN} + p0 basic fact writer | Discover perspectives from similar topics TOCs |
| GenQnPrompt | 19 | topic + persona perspective p + conv history | question q | Wikipedia writer guided by perspective asks incisive question |
| GenQueriesPrompt | 22 | topic + question q | queries - query1 - query2 ... | Transform question into Google search queries |
| GenAnswerPrompt | 24 | topic + question conv + gathered information info sources | answer a informative every sentence supported | Expert grounded on trustworthy Internet sources |
| DirectGenOutlinePrompt | 31 | topic t | draft outline OD general framework | Leverage LLM intrinsic knowledge |
| RefineOutlinePrompt | 32 | topic t + OD + convos {C0..CN} | improved outline O comprehensive | Refine with collected multi-perspective conversations |
| Section generation (reconstructed) | Writing stage | topic + outline O + relevant docs from R via Sentence-BERT similarity | section text with citations | Section-by-section composition |
| Polish delete repeated | Writing stage | draft article concatenated sections | polished article coherence improved | Delete repeated info |
| Lead summary | Writing stage | polished article | lead section 2-3 paragraphs Wikipedia stylistic norms | Synthesize summary entire article forming lead |

Flow: related_topics → tocs → perspectives P = [P0]+P[:N] → for each p in P for M rounds: q=gen_qn → queries=gen_queries → sources=search_and_sift → a=gen_ans → R append sources → convos append → OD=direct_gen_outline → O=refine_outline → section-wise generation via Sentence-BERT retrieval from R → polish → lead summary → final S

Hyperparameters N=5 M=5 search_top_k 10 etc.

---

## 13. Non-prompt but prompt-adjacent

- Search engines: YouRM You.com search API, BingSearch, VectorRM user-provided documents, SerperRM, BraveRM, SearXNG, DuckDuckGoSearchRM, TavilySearchRM, GoogleSearch, AzureAISearch supported knowledge_storm/rm.py
- LM components litellm integration language models embedding models All models supported by litellm
- STORMWikiRunnerArguments output_dir max_conv_turn max_perspective search_top_k max_thread_num
- Device cpu vector_db_mode offline online Qdrant etc
- FreshWiki dataset top 100 most-edited pages per month Feb 2022-Sep 2023 filter B-class ORES exclude list articles no subsections plain text only
- Ground truth Wikipedia article excluded search results
- Challenges identified: source bias transfer bias on Internet affects generated articles, over-association unrelated facts LLMs fabricate connections
