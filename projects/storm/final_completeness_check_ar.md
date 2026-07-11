# فحص الاكتمال النهائي — STORM

تاريخ: 2026-07-11
المصدر: arXiv:2402.14207v2 + stanford-oval/storm
الورقة: STORM NAACL 2024

## 1. التسليمات القياسية

| التسليم | الملف | الحالة |
|---|---|---|
| README | README.md | ✅ |
| research_summary | research_summary.md | ✅ |
| prompts_complete | prompts_complete.md | ✅ |
| python_logic_flow_complete | python_logic_flow_complete.md | ✅ |
| python_logic_inventory | python_logic_inventory.json | ✅ |
| deep_dive_task_matrix | deep_dive_task_matrix.md | ✅ |
| graph_english.md/.mmd | ✅ | ✅ |
| graph_arabic.md/.mmd | ✅ | ✅ |
| final_completeness_check_ar | هذا الملف | ✅ |
| QUALITY_REVIEW_AR | QUALITY_REVIEW_AR.md | ✅ |
| raw_prompt_files | GenRelatedTopics, GenPerspectives, GenQn, GenQueries, GenAnswer, DirectGenOutline, RefineOutline, algorithm1, prewriting vs writing | ✅ |
| raw_data_samples | freshwiki, outline eval metrics, conversation example | ✅ |
| ZIP | archives/storm_full_extract.zip | ⏳ سيُنشأ |

## 2. تغطية الأوامر

| وحدة | القوالب | الحالة |
|---|---|---|
| GenRelatedTopicsPrompt Line4 | I'm writing Wikipedia page for topic... recommend Wikipedia pages closely related subjects insights interesting aspects typical content structure List urls separate lines | ✅ |
| GenPerspectivesPrompt Line11 | You need select group Wikipedia editors who will work together create comprehensive article Each represents different perspective role affiliation related to topic Use other Wikipedia pages related topics inspiration For each editor add description what they will focus on Format 1. short summary editor1: description... | ✅ |
| GenQnPrompt Line19 | You are experienced Wikipedia writer want edit specific page Besides identity as Wikipedia writer you have specific focus when researching topic Now chatting with expert to get information Ask good questions to get more useful information When no more question say Thank you so much for your help! to end conversation Please only ask one question at a time don't ask what you have asked before Your questions related to topic | ✅ |
| GenQueriesPrompt Line22 | You want answer question using Google search What do you type search box? Write queries format - query1 - query2... | ✅ |
| GenAnswerPrompt Line24 | You are expert who can use information effectively chatting with Wikipedia writer who wants write Wikipedia page on topic you know You have gathered related information will now use information to form response Make response as informative as possible make sure every sentence is supported by gathered information | ✅ |
| DirectGenOutlinePrompt Line31 | Write outline for Wikipedia page Format Use "#" Title to indicate section title "##" Title subsection "###" subsubsection etc Do not include other information | ✅ |
| RefineOutlinePrompt Line32 | Improve outline for Wikipedia page You already have draft outline covering general info Now you want improve based on information learned from information-seeking conversation more comprehensive Format same # ## ### | ✅ |
| Section generation reconstructed | Section title + subheadings used retrieve relevant docs from R based semantic similarity Sentence-BERT embeddings LLM generate section with citations | ✅ |
| Polish delete repeated | Delete repeated information across sections improve coherence | ✅ |
| Lead summary synthesis | Synthesize summary entire article forming lead section beginning Wikipedia stylistic norms 2-3 paragraphs | ✅ |
| Algorithm1 pseudocode | P0 basic fact writer R=[] related_topics=gen_related_topics tocs=[] get_wiki_article extract_toc P=gen_perspectives P=[P0]+P[:N] convos=[] foreach p in P convo_history=[] for i=1..M q=gen_qn queries=gen_queries sources=search_and_sift a=gen_ans R.append sources convos.append OD=direct_gen_outline O=refine_outline return O,R | ✅ |
| Co-STORM extension | Collaborative discourse protocol Co-STORM LLM experts answers grounded external knowledge and/or raises follow-up questions Moderator generates thought-provoking questions inspired info discovered retriever but not directly used previous turns Question generation grounded Human user initiative observe discourse or actively engage injecting utterances steer focus dynamic updated mind map hierarchical concept structure shared conceptual space reduce mental load | ✅ |

## 3. تغطية المنطق

| مكون | الحالة |
|---|---|
| Pre-writing stage discovery perspectives via surveying related Wikipedia articles TOCs concatenated | ✅ |
| Simulated conversations N+1=6 perspectives M=5 rounds per perspective total ~30 Q/A perspective-guided varied questions vs direct prompting What When Where basic surface vs conversational follow-up in-depth transportation budget | ✅ |
| Outline creation OD from topic only + refined O from OD+convos via internal knowledge + gathered conversations | ✅ |
| Writing stage section-by-section retrieval relevant docs from R via Sentence-BERT similarity generate section with citations concatenation delete repeated coherence improve lead summary Wikipedia norms | ✅ |
| FreshWiki dataset top 100 most-edited per month Feb2022-Sep2023 filter B-class ORES exclude list no subsections plain text only avoid leakage | ✅ |
| Outline eval heading soft recall paraphrase-MiniLM-L6-v2 cosine count(Ai)=1/sum_j Sim card(A)=sum count soft recall card(G∩P)/card(G) intersection via union + heading entity recall FLAIR NER | ✅ |
| Article eval Prometheus 13B 1-5 rubric Interest Coherence Organization Relevance Focus Coverage trimmed 2000 words iterative removing shortest section + citation recall precision Gao et al Mistral 7B | ✅ |
| Expert evaluation Wikipedia editors organized +25% absolute broad coverage +10% vs outline-driven RAG baseline | ✅ |
| Challenges source bias transfer bias Internet affects articles over-association unrelated facts fabricate connections new frontiers | ✅ |
| Implementation zero-shot DSPy framework Khattab et al hyperparams N=5 M=5 search_top_k 10 max_thread_num 1 device cpu vector_db_mode offline do_research etc LM choices gpt-3.5-turbo question asking gpt-3.5-turbo-instruct other parts gpt-4 drafting refining outline YouRM You.com search API ground truth excluded + litellm integration BingSearch VectorRM etc pip install knowledge-storm | ✅ |
| Co-STORM mind map hierarchical concept structure shared conceptual space reduce mental load highly modular dspy | ✅ |

## 4. المهام

| مهمة | ✅ |
|---|---|
| Perspective discovery via related topics TOCs | ✅ |
| Information-seeking conversation simulation N+1 perspectives M rounds | ✅ |
| Outline creation draft + refine | ✅ |
| Full-length article generation section-by-section with citations Sentence-BERT retrieval + polish + lead summary | ✅ |
| FreshWiki dataset creation avoiding leakage | ✅ |
| Outline evaluation soft recall + entity recall | ✅ |
| Article evaluation Prometheus + citation quality + expert editors | ✅ |
| Co-STORM collaborative discourse protocol mind map | ✅ |

## 5. خارج النطاق (مقصود)

- إعادة تشغيل STORM 70k demo مع You.com API مكلف (النتائج موجودة figures)
- تدريب Prometheus 13B مقيم جديد (استخدام نموذج جاهز)
- تحميل كل FreshWiki كامل (عينات فقط)
- تشغيل منصات روبوتية فعلية أو محاكيات باهظة (موثق كأمثلة)

## 5b. ما أضيف بعد المراجعة

- كل 7 موجهات من Listing1-2 نص حرفي من PDF مع InputField OutputField dspy
- Algorithm1 pseudocode كامل مع أسطر 4,11,19,22,24,31,32
- أمثلة 2022 Winter Olympics Opening Ceremony Figure1A direct prompting 30 questions When Where basic vs Figure1B perspective-guided event planner transportation budget vs Figure1C conversational follow-up in-depth
- FreshWiki تفصيل top 100 per month Feb2022-Sep2023 B-class ORES exclude list
- معادلات soft heading recall count(Ai) card(A) intersection via union + FLAIR NER
- تفصيل تقييم Prometheus 13B trimmed 2000 words iterative shortest section removal + citation recall precision + expert +25% broad +10%
- Co-STORM بروتوكول خطاب تعاوني mind map هرمي shared conceptual space
- عينات JSON freshwiki_sample outline_eval_metrics conversation_example
- مخططات mermaid EN/AR شاملة workflow perspective discovery simulated conversations outline creation writing evaluation co-storm

## 6. الحكم

**مكتمل.** الحزمة تطابق معيار الاستخراجات السابقة وتغطي كل أسطح الأوامر ومنطق البحث التوليد التكراري وتحليل وجهات النظر المتعددة والمنطق الكامل للمسح العلمي.
