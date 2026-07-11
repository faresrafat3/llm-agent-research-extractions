# SciMON / SciPIP — Complete Prompt Extraction

Source: SciMON 2305.14259 Text 77k chars + SciPIP 2410.23166 Text extraction + GitHub clbd + STORM-like comparison

Audited via fitz /tmp/2305.14259.txt and /tmp/2410.23166.txt

---

## 1. SciMON Problem Setting Prompt (Background Context + Seed Term)

**Paper Sec 2.1:**

> We are motivated by imagining an AI-based assistant that suggests ideas in natural language. The assistant takes as input background context B consisting of (1) current problems, motivations, experimental settings and constraints, denoted as M; and optionally (2) a seed term v that should be a focus point of the generated idea I. The seed term is motivated by considering a user-provided cue for the model to limit its hypothesis space. Importantly, generated ideas should not merely paraphrase the background—the output should be novel with respect to B and the broader literature corpus.

**Reconstructed System Prompt for SciMON Idea Generation:**

```text
You are a scientific inspiration machine optimized for novelty (SciMON). You are an AI-based assistant that suggests new research directions in natural language.

Input: Background context B consisting of:
- M: current problems, motivations, experimental settings and constraints (e.g., Continual learning aims to enable information systems to learn from continuous data stream across time... knowledge acquisition done by using Method Current pre-trained...)
- Optionally seed term v that should be focus point of generated idea I (e.g., "speech unit boundaries", "Irish language learning", "data augmentation is an effective solution to data scarcity in low-resource scenarios...").

Your goal: Generate natural language idea I that is novel with respect to B and broader literature corpus, not merely paraphrasing background. Idea should be grounded in literature inspirations retrieved.

Approach systematic:
- Step1: Read background context B to understand problems, motivations, experimental settings, constraints.
- Step2: Consider seed term v if provided to limit hypothesis space.
- Step3: Review inspirations from past scientific papers retrieved: semantic neighbors, KG neighbors, citation neighbors (related problems and their solutions along with contexts from scientific knowledge graph). These inspirations ground generated ideas in existing literature.
- Step4: Generate initial idea: "Given [context], a [new idea], Δ vs prior work..." Focus on novelty vs B and broader literature.
- Step5: Acknowledge technical depth requirement: avoid generic suggestions woven specifics copied directly from context (e.g., "NLP with ML algorithms and sentiment analysis" for some problem X, or "data augmentation and transfer learning" for Y, or "BERT or RoBERTa" for Z, or "Data preprocessing: Clean the text data, remove unnecessary characters, perform tokenization..."). Reduce copying rephrasing directly from context. Apply logical modifications beyond simple flipping high latency→low latency or efficiency limitations→highly efficient.

Output format:
Idea: [Natural language description of proposed method/idea]
Novelty Δ: [How differs from prior work and background]
Grounding: [Which inspirations support idea]
```

**Seed Term Prompts (from Table10 and examples):**

Example input from paper:

- Seed Term: "speech unit boundaries"
- Context (abridged): "... generate partial sentence translation given a streaming speech input. existing approaches ... break the acoustic units in speech, as boundaries between acoustic units in speech are not even. ..."
- Initial idea: "A pause prediction model to identify speech unit boundaries ..."
- Iteration1: "A method that leverages acoustic and linguistic features to predict speech unit boundaries dynamically, ensuring smooth transitions ... differs from existing research as it combines both acoustic properties and linguistic context ... adapting to variations in speaker characteristics, speaking styles, and languages."
- Iteration2: "A novel method called Adaptive Speech Unit Boundary Detection (ASUBD) ... combination of attention mechanisms to focus on relevant acoustic and linguistic features and reinforcement learning to guide system to make optimal predictions of unit boundaries based on previous decisions..."
- Ground Truth: "... an efficient monotonic segmentation module ... accumulate acoustic information incrementally and detect proper speech unit boundaries."

Second example:

- Seed Term Prompt: "Irish language learning is done by using Method"
- Context: "Irish is a minority language which means that l2 learners have limited opportunities for exposure to the language, and additionally, there are also limited (digital) learning resources available."
- Model outputs: See Table10 human annotation results expanded.

---

## 2. SciMON Inspiration Retrieval Prompts

Paper does not give explicit prompt text for retrieval but describes three types:

**Semantic Neighbors:** Examples: st and automatic speech recognition (asr), low-resource tagging tasks, end-to-end speech translation, neural online chats response selection, neural machine translation, semi-supervised ner, entity and context learning, semi-supervised setting, dependency parsing, low-resource machine translation, slot filling, dialog state tracking, visual question answering, VQA, low-resource neural machine translation

**KG Neighbors:** Examples: nmt-based text normalization, task-oriented dialog systems, low-resource languages LRL, end-to-end speech translation, visual question answering VQA, multiclass utterance classification, clinical semantic textual similarity, neural online chats response selection, context-aware neural machine translation

**Citation Neighbors:** Examples: Contextual Augmentation: Data Augmentation by Words with Paradigmatic Relations, An Analysis of Simple Data Augmentation for Named Entity Recognition, Data Augmentation for Low-Resource Neural Machine Translation, DAGA: Data Augmentation with Generation Approach for Low-resource Tagging Tasks, EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks

Ground Truth: ELM: Data Augmentation with Masked Entity Language Modeling for Low-Resource NER

Table8 example retrieved inspirations similar to ground truth underlined.

**Reconstructed Retrieval Prompt:**

```text
Given background context B and seed term v, retrieve inspirations from past scientific papers:

Task: Retrieve 3 types:

1. Semantic Neighbors: semantically similar problems and solutions via semantic similarity graphs (e.g., low-resource tagging tasks, end-to-end speech translation, visual question answering etc)

2. KG Neighbors: knowledge graph neighbors via scientific knowledge graph from PubTator 3 etc (e.g., task-oriented dialog systems, low-resource languages LRL, clinical semantic textual similarity etc)

3. Citation Neighbors: citation co-occurrence neighbors (e.g., Contextual Augmentation: Data Augmentation by Words with Paradigmatic Relations, etc)

Collection: 67,408 ACL Anthology papers 1952-2022 via Semantic Scholar Academic Graph API non-commercial, plus 5,708 PubMed papers 1988-2024 via Entrez Programming Utilities API, IE system PubTator 3 extracts KG from abstracts, sentence classifier trained annotated abstracts selects background context.

For each retrieved inspiration, provide: Title, Background context, Idea summary.

Return list inspirations similar to ground truth underlined.
```

**Specific Prompt Data Example from Paper:**

Input:
- context: "data augmentation is an effective solution to data scarcity in low-resource scenarios. however, when applied to token-level tasks such as ner, data augmentation methods often suffer from token-label misalignment, which leads to unsatisfactory performance."
- Semantic Neighbors: [list low-resource tagging etc]
- KG Neighbors: [list]
- Citation Neighbors: [list papers]
- Ground Truth: ELM: Data Augmentation with Masked Entity Language Modeling for Low-Resource NER

Goal: retrieve inspirations that lead to ground truth.

---

## 3. SciMON Idea Generation Initial + Iterations

**Flow:**

Given [context], a [new idea], Δ vs prior work...

Initial Idea: used-for used-for etc linked knowledge graph inductive learning techniques...

Idea Generation then Iterative Novelty Boosting Prior Literature {(Background_i, idea_i)} Δ Problems motivations focus points "Given [context], a [new idea], Δ vs prior work..."

**Iterative Novelty Boosting Prompt (Reconstructed from description):**

```text
You are an AI-based assistant that suggests ideas iteratively boosting novelty.

You have background context B and idea I generated at step t.

Task: Compare I with existing research literature: Prior Literature {(Background_i, idea_i)}.

If you find strongly overlapping research, update idea to be more novel relative to prior work, much like a good researcher would do.

Steps:

1. Take idea I at step t.
2. Compare I with existing research in literature: Check semantic overlap with prior papers (Background_i, idea_i) from inspiration retrieval.
3. If strongly overlapping, identify overlapping concepts and propose update that increases Δ vs prior work.
4. Output updated idea I_{t+1} that is more novel relative to prior work and still grounded.

Example:

Initial Idea: "A pause prediction model to identify speech unit boundaries ..."

Prior literature includes: Existing pause prediction models...

If overlap high, update:

Iteration1: "A method that leverages acoustic and linguistic features to predict speech unit boundaries dynamically, ensuring smooth transitions ... differs from existing research as it combines both acoustic properties and linguistic context ..."

Iteration2: "A novel method called Adaptive Speech Unit Boundary Detection (ASUBD) ... combination of attention mechanisms to focus on relevant acoustic and linguistic features and reinforcement learning to guide system to make optimal predictions of unit boundaries based on previous decisions..."

Goal: Sufficient novelty achieved. Continue iterations until novelty threshold met.

Return: Updated Idea + Novelty Δ explanation + which prior literature compared.
```

Paper notes: Models often made generic suggestions woven together specific details copied directly from context. Techniques reduced behavior but not fully solved. GPT4 especially generated generic descriptions common steps NLP workflows Data preprocessing Clean text etc. All models often copied rephrased directly from context. In certain cases applied simple logical modifications to context e.g., high latency problems → low latency or efficiency limitations → highly efficient. Novelty iteration method enhances ideas overall; however ideas often based on superficial recombinations common concepts far from technical depth scientific papers.

**In-context Contrastive Model:**

Encourages novelty with respect to background context. In-context contrastive model encourages novelty w.r.t background context. Contrastive augmentation CL model with in-context contrastive augmentation.

Model types:

- T5 baseline fine-tuned
- T5+CL: model with in-context contrastive augmentation
- T5+SN: semantic inspirations
- T5+KG: KG inspirations
- T5+CT: citation inspirations
- T5+SN+CL
- T5+KG+CL
- T5+CT+CL
- GPT4ZS zero-shot
- GPT4FS few-shot
- GPT4FS+SN, KG, CT etc.

Table9 automatic evaluation challenging and gold subsets R-L ROUGE-L BERT BERTscore SciBERT encoder. Example: GPT4ZS 0.120 0.581 0.130 0.583 GPT4FS 0.143 0.618 0.151 0.624 T5 0.223 0.672† etc T5+CL 0.225† 0.671† T5+SN+CL 0.228† 0.671† 0.258† 0.686† etc differences not statistically significant p≤0.05 compared each other but still significant when compared other models t-test.

---

## 4. SciPIP Prompts — Full Extraction (Tables 6-8 and Appendix A prompts)

From PDF extraction /tmp/2410.23166.txt Listings.

### 4.1 Entity Extraction τ2 (Table 6 prompt for entity extraction namely τ2)

**System Message:**

```text
Now you are an expert in extracting key entities from research contents. You are good at identifying the most important keywords or phrases that summarize the main topics or concepts discussed in the content.
```

**User Message:**

```text
Task Description:
I will provide you with a content from a research paper.
Your task is to extract the key entities from this content. These entities are the most important keywords or phrases that summarize the main topics or concepts discussed in the content.
Instruction:
Content: The content is your key focus, and the extracted entities should be based on the content. In other words, the entities you extract should be concrete manifestations of the main themes and topics discussed in the content.
Your approach should be systematic:
- Start by thoroughly reading the content to understand its main themes and topics.
- Identify and list the key entities that are central to the content.
- Ensure that the entities are relevant, meaningful, and representative of the content.
- Each entity in entities should be no longer than 5 words.
- Each entity in entities should contain at least 2 words.
- The number of entities should be less than or equal to 5.
- Each entity in entities should be nouns or noun phrases.
examples:
{examples}
Your turn:
Given the following content:
{content}
Your answer should follow this format:
entity1, entity2, entity3, ......
```

**Use:** For building literature database 78K papers top-tier AI conferences re-summarize each paper into structured quintuple. This extracts keywords/entities part of quintuple.

Example entities constraints: ≤5 words, ≥2 words, ≤5 entities, nouns/noun phrases.

---

### 4.2 Summary Prompt (Problem + Main Idea format)

**System Message:**

```text
Now you are a researcher in the field of AI with innovative and pioneering abilities.
```

Or variant: expert in extracting... but for summary:

**User Message For Summary (from Table extraction):**

```text
Task Description: You are provided with the title, abstract, and introduction of a research paper. Your task is to generate a concise summary of what kind of problem does this paper aim to solve and what methods are proposed to address it. The summary should follow this format: The problem of [problem] can be addressed by [main idea/approach].
Instructions:
Title: Read the title to understand the general topic of the paper.
Abstract: Read the abstract to get a concise summary of the research, including the problem addressed, the methods used, and the main findings.
Introduction: Read the introduction to gain a deeper understanding of the background, significance, and specific problem the paper addresses, as well as the proposed approach or solution. Based on the provided information, generate a single sentence that captures the essence of the paper, following the format specified above.
Your Turn:
Given the following paper information:
Title: {title}
Abstract: {abstract}
Introduction: {introduction}
Output: The problem of [problem] can be addressed by [main idea/approach].
```

Use: For quintuple backgrounds ideas concise methods references — summarizing problem and main idea.

---

### 4.3 Background and Main Ideas Prompt (Motivations + Details)

**User Message For Background And Main Ideas:**

```text
Please read the title, abstract, and introduction of the paper again, as well as the summary you provided. Complete the following two tasks:
1. Briefly provide the two most critical motivations behind proposing these methods to address the problems.
2. Briefly provide the three most critical or innovative details of the paper that were not mentioned in your summary (It's best if these details are the new methods or techniques adopted in this paper).
Output:
Motivations:1.[motivation1]. 2.[motivation2]. Details:1.[detail1]. 2.[detail2]. 3.[detail3].
```

Use: For extracting motivations and innovative details part of quintuple.

---

### 4.4 Concise Methods τ3 — Example Style Transform (Table 7)

**System Message:**

```text
Now you are a researcher in the field of AI with innovative and pioneering abilities.
```

**User Message:**

```text
# Task Description:
You are an AI researcher conducting studies in a specific domain. Someone has provided you with a methodology section, and your task is to transform it into another style. I will give you an example. The example begins with "# Example 1" and includes a Example Summarized Methods. Then, your task starts with "# Your Task", containing "Your Methodology Section". Your job is to transform Your Methodology Section into a Summarized Methods by referring to Example 1. Note that the ideas in Example 1 are unrelated to your idea, so the key focus should be on the style of Example Summarized Methods. You should directly start with your response and do not start with a section title like "## Your Summarized Methods".
# Example 1
## Example Summarized Methods
{Example Summarized Methods}
# Your Task
## Your Methodology Section
{methodology}
## Your Summarized Methods
```

Use: Transform methodology section into summarized methods style — part of quintuple concise methods.

---

### 4.5 Background Transformation — Teacher Student Prompt (Table 8)

**System Message:**

```text
You are a teacher in the field of AI, skilled at clearly explaining AI concepts to students. Your student is an undergraduate in AI with a basic understanding of deep learning.
```

**User Message:**

```text
# Task Description:
You are teaching your undergraduate about a specific subfield of AI research. You have a brief description of the research background, and now you need to explain its meaning and purpose in detail to your undergraduate. Keep in mind that your undergraduate may be completely unfamiliar with the technical terms in the research background. I will give you an example. The example begin...
```

Incomplete in extraction but pattern: Transform research background description into detailed explanation for undergraduate unfamiliar technical terms, example-based style.

Use: For backgrounds part of quintuple — teaching explanation.

---

### 4.6 Idea Proposer Prompt — Dual-Path 10 Ideas (Appendix A)

**System Message:**

```text
Now you are a researcher in the field of AI with innovative and pioneering abilities. You are good at using innovative and original methods to solve cutting-edge problems in the field of AI.
```

**User Message:**

```text
### Task Description: You will be provided with a research problem along with its rationales. Your task is to brainstorm some ideas that are clear, innovative, valid, and comprehensive to address the problem. Additionally, some cue words along with summaries, backgrounds, and contributions (methods) of related papers will be provided as sources of inspiration for generating novel ideas.
### Information Provided:
1. **Research Problem & Rationales**: The key issues or aspects of the problem that need to be addressed. These will form the foundation for generating your ideas.
2. **Related Papers**: Draw inspiration from the abstracts, backgrounds, and methods of these papers. Delve deeply into these methods, understand the motivations behind them, and think critically about how they might inform your approach. Avoid merely stacking existing methods; instead, integrate relevant aspects with your own insights to create original solutions.
### Approach: Your approach should be systematic:
- **Step 1**: Thoroughly read the research problem to understand your primary focus.
- **Step 2**: Review the summaries, backgrounds, and contributions (methods) of the related papers to gain a broader perspective and insights relevant to the problem.
- **Step 3**: Based on the provided information, propose some ideas that are clear, innovative, valid, and comprehensive.
### Specific Information: I will provide you with specific information now, please use them according to the instructions above:
1. **Research Problem & Rationales**: {problem}
2. **Related Papers**: {related__papers__information}
### Format for Your Response: Please ensure that your final ideas include about 10 entries, presented in the following format:
**Idea 1**: [The first method idea]
**Idea 2**: [The second method idea]
**Idea 3**: [The third method idea]
...
```

Use: Idea proposer dual-path framework integrates content retrieved papers + internal knowledge LLM. About 10 ideas per problem. Avoid merely stacking existing methods integrate relevant aspects with own insights create original solutions.

Related papers information includes cue words along with summaries backgrounds contributions methods.

---

## 5. SciPIP Literature Database Construction — Multi-Granularity Retrieval Prompts

**Quintuple construction:**

For each of ~78K papers top-tier AI conferences:

- Keywords (via entity extraction τ2 prompt)
- Backgrounds (via background transformation teacher-student prompt + summary problem main idea format)
- Ideas (summary)
- Concise Methods (via concise methods τ3 example style transform)
- References (original citation relations)

These components individually preprocessed e.g. encoded into vectors and stored database enable more precise efficient retrieval.

**Multi-granularity retrieval algorithm:**

Comprehensively leverages keywords, semantic embeddings, citation relations:

- Keywords retrieval: exact keyword match?
- Semantic embeddings: semantic-entity based retrieval SE, encode quintuple components into vectors, vector-based retrieval but key points captured because quintuple components individually preprocessed vs encoding entire sections multifaceted difficult capture key points
- Citation relations: citation co-occurrence CC and clustering CL

Ablation Table5: SE means proposed semantic-entity based retrieval, CC means citation co-occurrence, CL means clustering. Since AI Scientist does not perform literature retrieval when generating ideas results primarily on SCIMON and ResearchAgent for generating scientific paper ideas differ from those in this study

Literature retrieval results Table4: groundtruth real citations tested papers Recall10 recall rate top10 ranked papers among retrieved literature compared ground truth citations

Example: AI Scientist Not Applicable, SCIMON-like Recall10 0.381 Recall20 0.481 Recall30 0.548 Recall40 0.587 Recall50 0.616, ResearchAgent-like 0.377 0.484 0.550 0.598 0.622, SciPIP Ours 0.419 0.544 0.615 0.657 0.684 demonstrating more thorough exhaustive retrieval.

Idea generation phase dual-path framework integration content retrieved papers + extensive internal knowledge LLMs significantly boosts novelty feasibility practical value.

---

## 6. Evaluation Prompts for SciMON

**Automatic evaluation:**

- ROUGE-L, BERTScore Zhang* et al 2020 with SciBERT encoder, BARTScore Yuan et al 2021 similarity between ground truth and generated output
- Example Table9 challenging gold subsets R-L BERT: GPT4ZS 0.120 0.581 0.130 0.583 GPT4FS 0.143 0.618 etc T5 0.223 0.672† 0.246 0.685 T5+CL 0.225† 0.671† etc T5+SN+CL 0.228† 0.671† etc
- Note T5-based models outperformed GPT-based models due longer outputs GPT4 vs T5 fine-tuned many examples scores higher superficially templates e.g. "In this paper we propose new ... for ..."

**Human evaluation:**

- Human annotators domain expertise assess relevance utility novelty technical depth
- Input Type Content: Seed Term Prompt Irish language learning is done by using Method Context Irish is minority language ... Table10 Input for sample human annotation results Model Output Label GPT3.5FS The use of Social Media in Irish Language Learning: A Case Study helpful GPT3.5Retr One method that could be used for Irish language learning is CALL unhelpful etc
- Annotation interface Figure5 Gold subset annotation interface extractive text summarization etc plus questions Is output trivially overlap with context IE is sufficient quality not generic correct context contains relevant information for target relation Conservative filter only flag cases where context highly irrelevant Relation is part main idea proposed paper etc
- Comprehensive evaluation reveal GPT-4 overall low technical depth novelty methods partially mitigate ideas still far behind scientific papers terms novelty depth utility raising fundamental challenges

**Error analysis prompts (not explicit but described):**

Models often made generic suggestions woven together specific details copied directly from context e.g. NLP with ML algorithms sentiment analysis for some problem X or data augmentation transfer learning for Y or BERT RoBERTa for Z Techniques reduced behavior not fully solved GPT4 especially seemed generate generic descriptions common steps NLP workflows Data preprocessing Clean text data remove unnecessary characters perform tokenization... All models often copied rephrased directly from context In certain cases applied simple logical modifications to context e.g. high latency or efficiency limitations suggestions would include phrases such as low latency or highly efficient

---

## 7. Prompt wiring map SciMON + SciPIP

| Prompt | Phase | Input | Output | Idea |
|---|---|---|---|---|
| Background context collection + seed term | Data collection | ACL Anthology 67,408 1952-2022 Semantic Scholar API + PubMed 5,708 1988-2024 Entrez PubTator 3 KG extraction sentence classifier background selection | Background contexts M problems motivations experimental settings constraints + seed term v optional focus | Define problem setting assistant takes B = M + optionally v |
| Inspiration retrieval semantic KG citation | Retrieval | Background context seed term | Inspirations past papers semantic neighbors KG neighbors citation neighbors Table8 example similar ground truth underlined | Ground ideas literature |
| Idea generation initial | Generation | Background context + inspirations + seed term | Initial idea "Given [context], a [new idea], Δ vs prior work..." | Initial |
| Iterative novelty boosting | Novelty optimization | Idea I at step t + prior literature {(Background_i, idea_i)} | Updated idea more novel relative prior work until sufficient novelty, like good researcher would do | Iterative novelty |
| In-context contrastive augmentation CL | Novelty encouragement | Background context + contrastive examples | Novelty w.r.t background context reducing reliance copying | CL model SN semantic KG KG CT citation T5+CL etc Table9 |
| SciPIP quintuple summarization | Database construction 78K papers top-tier AI | Title abstract introduction methodology | Structured quintuple keywords backgrounds ideas concise methods references individually encoded vectors stored | Precise efficient retrieval |
| Entity extraction τ2 | Keywords | Content research paper | Key entities ≤5 each ≤5 words ≥2 words nouns noun phrases entity1, entity2... | Keywords part quintuple |
| Summary problem main idea format | Summary | Title abstract introduction | The problem of [problem] can be addressed by [main idea/approach] single sentence essence | Summary part quintuple |
| Background motivations details | Analysis | Title abstract introduction summary | Motivations 1. 2. Details 1. 2. 3. three most critical innovative details methods not mentioned summary | Background analysis |
| Concise methods τ3 example style transform | Methods | Methodology section + Example Summarized Methods example 1 unrelated style focus | Summarized Methods transformed style | Concise methods part quintuple |
| Background transformation teacher student | Teaching | Research background brief description subfield AI | Detailed explanation meaning purpose undergraduate unfamiliar technical terms example-based | Backgrounds part quintuple |
| Idea proposer dual-path ~10 ideas | Idea generation | Research problem rationales + related papers summaries backgrounds contributions methods cue words | ~10 ideas Idea1 Idea2 ... clear innovative valid comprehensive integrating content retrieved papers + internal knowledge LLM avoiding merely stacking | Dual-path framework boosts novelty feasibility practical value |
| Multi-granularity retrieval SE CC CL | Retrieval | Research problem + literature database quintuple encoded vectors + citation relations | Retrieved literature comprehensive keywords semantic embeddings citation relations thorough Recall10 0.419 Recall20 0.544 etc vs SCIMON-like 0.381 vs ResearchAgent-like 0.377 | More thorough exhaustive |

Flow SciMON: Background contexts problems motivations experimental settings constraints seed term v → Inspiration retrieval semantic similarity graphs knowledge graphs citation networks related problems solutions contexts scientific KG → Idea generation Given [context] new idea Δ vs prior work → Iterative novelty boosting compare I with existing research literature if strongly overlapping update more novel relative prior work like good researcher → In-context contrastive encourages novelty w.r.t background context → Human evaluation relevance utility novelty technical depth + Automated ROUGE BERTScore BARTScore

Flow SciPIP: Collect ~78K papers top-tier AI conferences → LLM re-summarize each paper into structured quintuple keywords backgrounds ideas concise methods references individually preprocessed encoded vectors stored database → Multi-granularity retrieval keywords semantic embeddings citation relations thorough literature retrieval → Dual-path idea generation integrates content retrieved papers + extensive internal knowledge LLM about 10 ideas clear innovative valid comprehensive → Novelty experiments idea proposal non-matching ideas may be more valuable because SciPIP generate novel ideas not appear or even not put forward by human + retrieval results Recall10-50

---

## 8. Non-prompt strings

- Seed terms: speech unit boundaries, Irish language learning, data augmentation is effective solution to data scarcity, continual learning aims enable information systems learn from continuous data stream, etc
- Inspiration types: Semantic Neighbors st automatic speech recognition asr low-resource tagging, KG Neighbors nmt-based text normalization task-oriented dialog, Citation Neighbors Contextual Augmentation Data Augmentation by Words Paradigmatic Relations etc
- Datasets: ACL Anthology 67,408 1952-2022 Semantic Scholar Academic Graph API non-commercial, PubMed 5,708 1988-2024 Entrez, 78K papers top-tier AI conferences SciPIP, PubTator 3 IE system
- Models: T5 fine-tuned, T5+CL contrastive, T5+SN semantic inspirations, T5+KG KG inspirations, T5+CT citation inspirations, T5+SN+CL etc, GPT3.5FS few-shot, GPT4FS, GPT4ZS zero-shot
- Metrics: ROUGE-L Lin 2004 BERTScore Zhang SciBERT encoder BARTScore Yuan et al ROUGE BERT R-L↑ BERT↑, Recall10-50 retrieval recall rate top10-50 ranked among retrieved vs ground truth citations, challenging gold subsets
- Templates: Given [context], a [new idea], Δ vs prior work...
- Seed Term Prompt: Irish language learning is done by using Method etc
- Idea format: **Idea 1**: [first method idea] etc
- Quintuple: keywords backgrounds ideas concise methods references
- Entity constraints: ≤5 words ≥2 words ≤5 entities nouns noun phrases
- Summary format: The problem of [problem] can be addressed by [main idea/approach]
- Motivations Details format: Motivations:1.[motivation1]. 2.[motivation2]. Details:1.[detail1]. 2.[detail2]. 3.[detail3]
- Data augmentation example ELM: Data Augmentation with Masked Entity Language Modeling for Low-Resource NER
- Background context collection sentence classifier Huang et al 2020
- Biomedical LLM Chen et al 2023 fine-tune etc
- Ethical: data collection follows Terms of Use https://allenai.org/terms dataset only non-commercial human evaluation voluntary fair wage Entrez data usage guidelines
