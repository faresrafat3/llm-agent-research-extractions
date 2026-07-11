
# SciMON / SciPIP — Python Logic Flow Complete

Audited via fitz /tmp/2305.14259.txt + /tmp/2410.23166.txt + GitHub clbd

---

## 0. Data collection logic SciMON

```
Collect 67,408 ACL Anthology papers 1952-2022 using Semantic Scholar Academic Graph API under API license agreement https://api.semanticscholar.org/license/ Ensure data collection procedure follows Terms of Use https://allenai.org/terms According agreement dataset can only be used non-commercial purposes All annotators human evaluation voluntary participants fair wage Further collect 5,708 PubMed papers 1988-2024 using Entrez Programming Utilities API www.ncbi.nlm.nih.gov/books/NBK25501/ Follow data usage guidelines www.ncbi.nlm.nih.gov/books/about/copyright/

Biomedical domain additional initial experiment similar data creation procedure collecting dataset from PubMed papers use PubTator 3 Islamaj et al Wei et al Luo Lai as IE system extract KG from paper abstracts Use sentence classifier trained annotated abstracts Huang et al 2020 select background context Fine-tune SOTA biomedical LLM Chen et al 2023 on data evaluate test split past pretraining cutoff date Two biochemical domain experts graduate-level education evaluate quality results finding overall rate 80% generated directions positively Finally contrast NLP-domain experiments evaluators more satisfied generated outputs than ground truth regarding technical detail Detailed results Table4 preliminary experiment meant mainly demonstrate generality approach more in-depth exploration utility quality left future work

Subset annotation interface Figure5 Gold subset annotation interface: anthology and PubMed papers written English might alienate readers historically underrepresented NLP/biochemical domains Data collection details Appendix E.2

Data format:
Background Context M: current problems motivations experimental settings constraints e.g. Continual learning aims enable information systems learn from continuous data stream across time ... method that combines continual learning with dynamic knowledge distillation approach efficient knowledge acquisition more efficient than exhaustive pre-training all existing data knowledge acquisition done using Method Current pre-trained...
Seed term v: optional focus point e.g. speech unit boundaries, Irish language learning, data augmentation...
Output: Background contexts + seed term examples Table10 Input for sample human annotation results Seed Term Prompt Irish language learning is done by using Method Context Irish is minority language ... etc
```

---

## 1. Inspiration retrieval logic SciMON

```
Given background problem description models first dynamically retrieve inspirations from past literature in form related problems and their solutions along with contexts from scientific knowledge graph These retrieved inspirations serve ground generated ideas existing literature

Three types:

- Semantic Neighbors: semantic similarity graphs, e.g., st and automatic speech recognition asr low-resource tagging tasks end-to-end speech translation neural online chats response selection neural machine translation semi-supervised ner entity and context learning dependency parsing low-resource machine translation slot filling dialog state tracking visual question answering VQA etc

- KG Neighbors: KG via PubTator 3 + scientific KG, e.g., nmt-based text normalization task-oriented dialog systems low-resource languages LRL end-to-end speech translation VQA multiclass utterance classification clinical semantic textual similarity neural online chats response selection context-aware neural machine translation

- Citation Neighbors: citation networks co-occurrence, e.g., Contextual Augmentation Data Augmentation by Words with Paradigmatic Relations Analysis Simple Data Augmentation for Named Entity Recognition Data Augmentation for Low-Resource Neural Machine Translation DAGA Data Augmentation with Generation Approach for Low-resource Tagging Tasks EDA Easy Data Augmentation Techniques Boosting Performance Text Classification Tasks Ground Truth ELM Data Augmentation with Masked Entity Language Modeling for Low-Resource NER Table8 Example from Zhou et al 2022 retrieved inspirations similar ground truth underlined Input context data augmentation effective solution data scarcity low-resource scenarios however when applied token-level tasks such ner data augmentation methods often suffer token-label misalignment leads unsatisfactory performance Semantic Neighbors list KG Neighbors list Citation Neighbors list Ground Truth ELM

Implementation: Semantic similarity graphs, knowledge graphs, citation networks retrieval related problems and solutions along with contexts from scientific KG

Example seed term speech unit boundaries context abridged generate partial sentence translation given streaming speech input existing approaches break acoustic units in speech as boundaries between acoustic units not even ... Initial idea pause prediction model identify speech unit boundaries differs existing research combines acoustic properties linguistic context adapting variations speaker characteristics speaking styles languages Iteration1 method leverages acoustic linguistic features predict speech unit boundaries dynamically ensuring smooth transitions ... Iteration2 novel method called Adaptive Speech Unit Boundary Detection ASUBD combination attention mechanisms focus relevant acoustic linguistic features reinforcement learning guide system make optimal predictions unit boundaries based previous decisions Ground Truth efficient monotonic segmentation module accumulate acoustic information incrementally detect proper speech unit boundaries
```

---

## 2. Idea generation logic SciMON

```
We are motivated by imagining AI-based assistant suggests ideas natural language Assistant takes as input background context B consisting 1 current problems motivations experimental settings constraints denoted M and optionally 2 seed term v that should be focus point generated idea I Seed term motivated considering user-provided cue model limit hypothesis space Importantly generated ideas should not merely paraphrase background output should be novel w.r.t B and broader literature corpus Figure2 illustrates setting

Flow Figure1: SCIMON takes background context and generates ideas grounded in literature inspirations optimizing novelty by iteratively comparing to related work

Background Context Problems motivations focus points... Given [context], a [new idea], Δ vs prior work...

We develop framework named SCIMON Scientific Inspiration Machines with Optimization for Novelty named after Nobel laureate and AI pioneer Herbert Simon who authored early foundational work automated scientific discovery Newell and Simon 1956 Simon 1973 We first present automated data collection methodology collecting examples past problems proposed ideas from scientific papers Then use data for both fine-tuning and in-context training LLMs training them take problem descriptions output proposed ideas address them Observe SOTA LLMs GPT-4 OpenAI 2023 struggle generating novel scientific ideas contribute new modeling framework generating hypotheses makes progress improving ability Figure1 Given background problem description models first dynamically retrieve inspirations from past literature in form related problems solutions along with contexts from scientific knowledge graph These retrieved inspirations serve ground generated ideas existing literature Then endow models ability iteratively boost novelty of generated ideas Given idea I at step t model compares I with existing research literature if finds strongly overlapping research model tasked updating idea more novel relative prior work much like good researcher would do Also introduce in-context contrastive model encourages novelty w.r.t background context

Models: T5 fine-tuned vs GPT4 few-shot zero-shot etc

Initial idea generation prompt: Background Context M + seed term v + inspirations semantic KG citation → Idea: Given [context], a [new idea], Δ vs prior work...
```

---

## 3. Iterative Novelty Boosting logic SciMON

```
Given idea I generated by LLM at step t model compares I with existing research in literature if finds strongly overlapping research model tasked updating idea more novel relative prior work much like good researcher would do

Prior Literature {(Background_i, idea_i)} Δ Problems motivations focus points

Iterative loop:

Idea_0 = initial idea from generation
For t in iterations (e.g., 2 iterations example speech unit boundaries):
  Compare Idea_t with existing research literature Prior Literature {(Background_i, idea_i)}
  If strongly overlapping:
    Update Idea_t to be more novel relative to prior work
    Example Iteration1: method leverages acoustic linguistic features predict speech unit boundaries dynamically ensuring smooth transitions ... differs existing research as combines both acoustic properties linguistic context adapting variations speaker characteristics speaking styles languages
    Iteration2: novel method called ASUBD combination attention mechanisms focus relevant acoustic linguistic features reinforcement learning guide system make optimal predictions unit boundaries based previous decisions...
  Else break sufficient novelty achieved

Our novelty iteration method enhances ideas overall however ideas often based on superficial recombinations common concepts far from technical depth scientific papers

Error analysis: Models often made generic suggestions woven together specific details copied directly from context e.g. NLP with ML algorithms sentiment analysis for some problem X or data augmentation and transfer learning for Y or BERT or RoBERTa for Z Techniques reduced behavior but not fully solve GPT4 especially seemed generate generic descriptions common steps NLP workflows Data preprocessing Clean text data remove unnecessary characters perform tokenization... All models often copied rephrased directly from context In certain cases applied simple logical modifications to context e.g. when contexts described problems such as high latency or efficiency limitations suggestions would include phrases such as low latency or highly efficient

In-context contrastive model encourages novelty w.r.t background context helps models perform better than baseline fine-tuning by reducing reliance copying See results Table9 Appendix B.4
```

---

## 4. SciPIP database construction logic

```
Collect approximately 78K papers from several top-tier academic conferences AI field utilize LLMs to re-summarize each paper into structured quintuple consisting of keywords, backgrounds, ideas, concise methods, references These components individually preprocessed e.g. encoded into vectors and stored database enable more precise efficient retrieval Based on constructed database propose multi-granularity retrieval method comprehensively leverages keywords semantic embeddings citation relations enabling thorough literature retrieval etc

Quintuple components:

- Keywords: via entity extraction τ2 prompt constraints ≤5 words ≥2 words ≤5 entities nouns noun phrases entity1, entity2...

- Backgrounds: via summary problem main idea format prompt The problem of [problem] can be addressed by [main idea/approach] Instructions Title read title understand general topic Abstract read abstract get concise summary research including problem addressed methods used main findings Introduction read introduction gain deeper understanding background significance specific problem paper addresses as well as proposed approach solution Based on provided information generate single sentence captures essence paper following format specified Your Turn Given following paper information Title title Abstract abstract Introduction introduction Output The problem of [problem] can be addressed by [main idea/approach] + Background motivations details prompt Please read title abstract introduction again as well as summary you provided Complete two tasks Briefly provide two most critical motivations behind proposing methods to address problems Briefly provide three most critical innovative details of paper that were not mentioned in summary It's best if these details are new methods techniques adopted in this paper Output Motivations:1.[motivation1]. 2.[motivation2]. Details:1.[detail1]. 2.[detail2]. 3.[detail3] + Background transformation teacher student prompt You are teacher in field AI skilled at clearly explaining AI concepts to students Your student is undergraduate AI basic understanding deep learning You are teaching your undergraduate about specific subfield AI research You have brief description research background and now need explain its meaning purpose detail to undergraduate Keep in mind undergraduate may be completely unfamiliar technical terms research background Example...

- Ideas: via summary problem main idea format maybe

- Concise Methods: via concise methods τ3 example style transform prompt # Task Description You are AI researcher conducting studies specific domain Someone provided methodology section task transform into another style I will give example begins Example 1 includes Example Summarized Methods Then your task starts Your Task containing Your Methodology Section Your job transform Your Methodology Section into Summarized Methods by referring to Example1 Note ideas in Example1 unrelated to your idea so key focus should be style of Example Summarized Methods You should directly start response and do not start with section title like ## Your Summarized Methods # Example1 ## Example Summarized Methods {Example Summarized Methods} # Your Task ## Your Methodology Section {methodology} ## Your Summarized Methods

- References: original citation relations

These components individually preprocessed e.g. encoded into vectors and stored database enable more precise efficient retrieval
```

---

## 5. SciPIP multi-granularity retrieval logic

```
Comprehensively leverages keywords semantic embeddings citation relations enabling thorough literature retrieval

Three granularity:

- Keywords retrieval: exact keyword match entity extraction τ2 output entities

- Semantic embeddings: semantic-entity based retrieval SE proposed semantic-entity based retrieval encode quintuple components individually into vectors vs encoding entire sections e.g. abstracts into vectors entire sections typically contains multifaceted information such approach makes difficult capture key points effectively This impacts both encoding quality retrieval performance

- Citation relations: citation co-occurrence CC and clustering CL

Multi-granularity retrieval algorithm comprehensive leverages keywords semantic embeddings citation relations enabling thorough literature retrieval

Literature retrieval results Table4 groundtruth real citations tested papers Recall10 recall rate top10 ranked among retrieved literature compared ground truth citations Recall10 means recall rate top10 ranked papers among retrieved literature compared ground truth citations Table5 ablation SE means proposed semantic-entity based retrieval CC means citation co-occurrence CL means clustering Since AI Scientist does not perform literature retrieval when generating ideas results primarily on SCIMON Wang et al 2024 and ResearchAgent Baek et al 2024 However experimental setups literature database SCIMON and ResearchAgent for generating scientific paper ideas differ from those in this study

Results: AI Scientist Not Applicable SCIMON-like Recall10 0.381 0.481 0.548 0.587 0.616 ResearchAgent-like 0.377 0.484 0.550 0.598 0.622 SciPIP Ours 0.419 0.544 0.615 0.657 0.684 demonstrating more thorough exhaustive retrieval

Ablation Table5: SE CC CL combinations

Novelty experiments idea proposal Table indicates non-matching ideas may be more valuable because SciPIP generate novel ideas that do not appear or even do not put forward by human Table4 retrieval results groundtruth real citations Recall10 means recall rate top10 ranked among retrieved literature compared to ground truth citations Table5 ablation studies SE means proposed semantic-entity based retrieval CC means citation co-occurrence CL means clustering Since AI Scientist does not perform literature retrieval when generating ideas results primarily on SCIMON Wang et al 2024 and ResearchAgent Baek et al 2024 etc
```

---

## 6. SciPIP dual-path idea generation logic

```
For idea generation dual-path framework effectively integrates both content retrieved papers and extensive internal knowledge LLMs Integration significantly boosts novelty feasibility practical value proposed ideas

Prompt: System Now you are researcher in field AI with innovative pioneering abilities You are good at using innovative original methods to solve cutting-edge problems in field AI User Task Description You will be provided with research problem along with rationales Your task brainstorm ideas clear innovative valid comprehensive address problem Additionally some cue words along with summaries backgrounds contributions methods of related papers will be provided as sources inspiration for generating novel ideas Information Provided 1 Research Problem & Rationales key issues aspects problem need addressed These form foundation generating ideas 2 Related Papers Draw inspiration abstracts backgrounds methods these papers Delve deeply methods understand motivations behind them think critically how they might inform approach Avoid merely stacking existing methods integrate relevant aspects with own insights create original solutions Approach systematic Step1 Thoroughly read research problem understand primary focus Step2 Review summaries backgrounds contributions methods related papers gain broader perspective insights relevant problem Step3 Based on provided information propose ideas clear innovative valid comprehensive Specific Information I will provide specific information now please use them according instructions above 1 Research Problem & Rationales {problem} 2 Related Papers {related__papers__information} Format Your Response ensure final ideas include about 10 entries presented format Idea1 [first method idea] Idea2 [second method idea] Idea3 [third method idea] ...

Related papers information includes cue words along summaries backgrounds contributions methods

Dual-path: Path1 content retrieved papers (summaries backgrounds contributions methods) + Path2 extensive internal knowledge LLM

Output about 10 ideas per problem

Experiments conducted various domains NLP CV demonstrate capability generate multitude innovative useful ideas Findings underscore potential valuable tool researchers seeking advance fields groundbreaking concepts

Novelty experiments: non-matching ideas may be more valuable because SciPIP generate novel ideas that do not appear or even do not put forward by human

Example idea Example Table: Knowledge-Augmented Language Model Prompting etc
```

---

## 7. Evaluation logic SciMON + SciPIP

```
SciMON:

Automatic evaluation:
ROUGE Lin 2004 BERTScore Zhang et al 2020 with SciBERT encoder BARTScore Yuan et al 2021 similarity ground truth generated output
Table9 challenging gold subsets R-L↑ BERT↑
GPT4ZS 0.120 0.581 0.130 0.583
GPT4FS 0.143 0.618 0.151 0.624
T5 0.223 0.672† 0.246 0.685
GPT4FS+SN 0.144 0.620 0.149 0.627
GPT4FS+KG 0.143 0.619 0.152 0.626
GPT4FS+CT 0.144 0.617 0.149 0.622
T5+CL 0.225† 0.671† 0.251† 0.686†
T5+SN+CL 0.228† 0.671† 0.258† 0.686†
T5+KG+CL 0.223† 0.669 0.248 0.681†
T5+CT+CL 0.225† 0.671† 0.250† 0.686†
† indicates differences between models not statistically significant p≤0.05 when compared each other but still significant when compared other models t-test

GPT-based models outperformed by T5-based models GPT4 outputs much longer than T5 explaining they underperform automatic metrics but outperform human evaluations Generated sentences often follow certain templates e.g. In this paper we propose new ... for ... which also helps explain why T5 fine-tuned many examples scores higher superficially At same time in-context contrastive examples which encourage novelty w.r.t background context helped models perform better than baseline fine-tuning by reducing reliance copying See results Table9 Appendix B.4

Human evaluation:
Domain expertise assess relevance utility novelty technical depth
Input Type Content Seed Term Prompt Irish language learning is done by using Method Context Irish is minority language which means l2 learners have limited opportunities exposure language additionally there are also limited digital learning resources available Table10 Input for sample human annotation results Model Output Label GPT3.5FS The use of Social Media in Irish Language Learning A Case Study helpful GPT3.5Retr One method that could be used for Irish language learning is CALL unhelpful etc
Annotation interface Figure5 Gold subset annotation interface extractive text summarization is done by using Metric transformer-based language models usually treat texts as linear sequences however most texts also have inherent hierarchical structure i.e. parts of text can be identified using position in this hierarchy in addition section titles usually indicate common topic respective sentences Proposal novel approach formulate extract encode inject hierarchical structure information explicitly into extractive summarization model based pre-trained encoder-only Transformer HiStruct+ model which improves SOTA ROUGEs for extractive summarization PubMed arXiv substantially
Questions: Is output trivially overlap with context IE is sufficient quality not generic correct context contains relevant information for target relation Conservative filter only flag cases where context highly irrelevant Relation is part main idea proposed paper etc

Comprehensive evaluation reveal GPT-4 tends to generate ideas overall low technical depth novelty while methods partially mitigate issue Work represents first step toward evaluating developing language models generate new ideas derived from scientific literature

Biochemical domain additional initial experiment similar data creation collecting dataset PubMed papers use PubTator 3 IE system extract KG from abstracts Use sentence classifier trained annotated abstracts select background context Fine-tune SOTA biomedical LLM Chen et al 2023 on data evaluate test split past pretraining cutoff date Two biochemical domain experts graduate-level education evaluate quality results finding overall rate 80% generated directions positively Finally contrast NLP-domain experiments evaluators more satisfied generated outputs than ground truth regarding technical detail Detailed results Table4 preliminary experiment meant mainly demonstrate generality approach more in-depth exploration utility quality left future work

Error analysis: Models often made generic suggestions woven together specific details copied directly from context e.g. NLP with ML algorithms sentiment analysis for some problem X or data augmentation and transfer learning for Y or BERT or RoBERTa for Z Techniques reduced behavior but not fully solve GPT4 especially seemed generate generic descriptions common steps NLP workflows Data preprocessing Clean text data remove unnecessary characters perform tokenization... All models often copied rephrased directly from context In certain cases applied simple logical modifications to context e.g. when contexts described problems such as high latency or efficiency limitations suggestions would include phrases such as low latency or highly efficient

SciPIP evaluation:
Literature retrieval Table4 Recall10-50 vs SCIMON-like vs ResearchAgent-like
Ablation Table5 SE semantic-entity based retrieval CC citation co-occurrence CL clustering Since AI Scientist does not perform literature retrieval when generating ideas results primarily on SCIMON and ResearchAgent for generating scientific paper ideas differ from those in this study
Novelty experiments non-matching ideas may be more valuable because SciPIP generate novel ideas not appear or even not put forward by human

Relation to Spark SciPIP integrated semantic retrieval citation awareness into idea generation producing hypotheses informed by current literature but primarily evaluated within NLP domains Extending further SciMON employed iterative refinement to systematically maximize novelty of ideas but outputs often suffered low practical feasibility experimental utility Drawing inspiration from collaborative research processes VirSci orchestrated multiple LLM agents within virtual ecosystem simulate team-based ideation achieving measurable improvements idea diversity research-trend alignment Nevertheless like SciMON VirSci primarily focused novelty without directly optimizing experimental usefulness etc Early efforts such as Meta Galactica utilized specialized scientific corpora facilitate technical tasks knowledge retrieval hypothesis generation Despite strong benchmark performance Galactica encountered significant issues factual grounding hallucinated references highlighting need improved reliability
