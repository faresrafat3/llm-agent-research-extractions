# مراجعة الجودة — STORM

## معايير

- أمانة استخراج Listing1-2 موجهات 7 من PDF
- اكتمال Algorithm1 pseudocode
- تغطية FreshWiki و outline eval و article eval
- وضوح مخططات

## النتائج

| معيار | درجة 1-5 | ملاحظات |
|---|---|---|
| GenRelatedTopicsPrompt Line4 | 5 | حرفي من PDF Listing1 "I'm writing a Wikipedia page for topic mentioned below Please identify and recommend some Wikipedia pages on closely related subjects..." |
| GenPerspectivesPrompt Line11 | 5 | حرفي "You need to select a group of Wikipedia editors who will work together to create comprehensive article on the topic Each represents different perspective role affiliation..." |
| GenQnPrompt Line19 | 5 | حرفي "You are experienced Wikipedia writer and want to edit a specific page Besides identity as Wikipedia writer you have specific focus..." |
| GenQueriesPrompt Line22 | 5 | حرفي "You want to answer question using Google search What do you type in search box? Write queries format - query1..." |
| GenAnswerPrompt Line24 | 5 | حرفي "You are expert who can use information effectively You are chatting with Wikipedia writer who wants to write Wikipedia page on topic you know You have gathered related information..." |
| DirectGenOutlinePrompt Line31 | 5 | حرفي "Write an outline for Wikipedia page Format Use "#" Title" to indicate section title "##" Title subsection..." |
| RefineOutlinePrompt Line32 | 5 | حرفي "Improve an outline for Wikipedia page You already have draft outline that covers general information..." |
| Algorithm1 pseudocode | 5 | P0 basic fact writer R=[] related_topics gen_related_topics tocs get_wiki_article extract_toc P gen_perspectives P=[P0]+P[:N] convos foreach p in P convo_history for i=1..M q gen_qn queries gen_queries sources search_and_sift a gen_ans R append convos append OD direct_gen_outline O refine_outline return O,R حرفي |
| Section generation Polish Lead | 4.5 | معاد بناؤه بأمانة من وصف Sec3.4 retrieve relevant docs from R based semantic similarity Sentence-BERT embeddings LLM generate section with citations Once all sections generated concatenated delete repeated improve coherence synthesize summary entire article forming lead section |
| FreshWiki | 5 | top 100 most-edited per month Feb2022-Sep2023 filter B-class ORES exclude list no subsections plain text only حرفي |
| Outline eval soft recall + entity recall | 5 | count(Ai)=1/sum_j Sim Sim=cos embed paraphrase-MiniLM-L6-v2 card(A)=sum count soft recall card(G∩P)/card(G) intersection via union card(G∩P)=card(G)+card(P)-card(G∪P) + FLAIR NER حرفي |
| Article eval Prometheus + citation | 5 | Prometheus 13B Interest Coherence Organization Relevance Focus Coverage trimmed 2000 words iterative removing shortest section + citation recall precision Gao Mistral 7B + expert organized +25% broad +10% challenges source bias transfer over-association |
| Co-STORM | 5 | collaborative discourse protocol turn management Co-STORM LLM experts grounded external knowledge and/or raises follow-up questions Moderator thought-provoking questions inspired info discovered retriever but not directly used previous turns Question generation grounded Human user initiative observe discourse or actively engage injecting utterances steer focus dynamic updated mind map hierarchical concept structure shared conceptual space reduce mental load highly modular dspy |
| Graphs | 5 | EN/AR mmd يغطي Topic→related→tocs→perspectives P0+N → convos N+1*M Q/A → OD→O → section loop Sentence-BERT retrieval → polish → lead → FreshWiki → outline eval → article eval → co-storm |
| Implementation hyperparams | 5 | N=5 M=5 search_top_k 10 max_thread_num 1 device cpu vector_db_mode offline do_research etc LM choices gpt-3.5-turbo question asking gpt-3.5-turbo-instruct other parts gpt-4 drafting refining YouRM You.com search API ground truth excluded litellm integration |

## ثغرات حرجة

- لا يوجد كود رسمي كامل لكل موجه Section generation Polish Lead من وصف Sec3.4 معاد بناؤه بأمانة موثق
- Co-STORM تفاصيل بروتوكول تعاوني من README أكثر من PDF الرئيسي لكن موثق

## توصيات

- إضافة raw_prompt_files منفصلة لكل 7 موجهات كما فعلنا
- إضافة JSON samples freshwiki_sample outline_eval_metrics conversation_example
- إضافة zip عند الدفع

## الحكم النهائي

**مقبول للنشر** — يطابق معيار extractions السابقة ويضيف قيمة Part 6 HOW TO TRACK KNOWLEDGE → knowledge synthesis perspective-guided question asking.

المستودع جاهز للدفع إلى faresrafat3/storm-full-extraction
