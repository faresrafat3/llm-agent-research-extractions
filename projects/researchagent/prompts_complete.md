# ResearchAgent — Complete Prompt Extraction

Source: PDF Tables 6-15, Equations (1)(2), Appendix A

Audited via pymupdf extraction /tmp/ResearchAgent_full2.txt

---

## 1. Problem Identification — Table 6 (full instantiation)

**System Message**

```text
You are an AI assistant whose primary goal is to identify promising, new, and key scientific problems based on existing scientific literature, in order to aid researchers in discovering novel and significant research opportunities that can advance the field.
```

**User Message**

```text
You are going to generate a research problem that should be original, clear, feasible, relevant, and significant to its field. This will be based on the title and abstract of the target paper, those of {len(references)} related papers in the existing literature, and {len(entities)} entities potentially connected to the research area.

Understanding of the target paper, related papers, and entities is essential:
- The target paper is the primary research study you aim to enhance or build upon through future research, serving as the central source and focus for identifying and developing the specific research problem.
- The related papers are studies that have cited the target paper, indicating their direct relevance and connection to the primary research topic you are focusing on, and providing additional context and insights that are essential for understanding and expanding upon the target paper.
- The entities can include topics, keywords, individuals, events, or any subjects with possible direct or indirect connections to the target paper or the related studies, serving as auxiliary sources of inspiration or information that may be instrumental in formulating the research problem.

Your approach should be systematic:
- Start by thoroughly reading the title and abstract of the target paper to understand its core focus.
- Next, proceed to read the titles and abstracts of the related papers to gain a broader perspective and insights relevant to the primary research topic.
- Finally, explore the entities to further broaden your perspective, drawing upon a diverse pool of inspiration and information, while keeping in mind that not all may be relevant.

I am going to provide the target paper, related papers, and entities, as follows:
Target paper title: {paper['title']}
Target paper abstract: {paper['abstract']}
Related paper titles: {relatedPaper['titles']}
Related paper abstracts: {relatedPaper['abstracts']}
Entities: {Entities}

With the provided target paper, related papers, and entities, your objective now is to formulate a research problem that not only builds upon these existing studies but also strives to be original, clear, feasible, relevant, and significant. Before crafting the research problem, revisit the title and abstract of the target paper, to ensure it remains the focal point of your research problem identification process.
Target paper title: {paper['title']}
Target paper abstract: {paper['abstract']}

Then, following your review of the above content, please proceed to generate one research problem with the rationale, in the format of
Problem:
Rationale:
```

Use: Naive (only core) = T({l0}), w/o Entity = T({l0..ln}), full = T({l0..ln}, Ret(...))

---

## 2. Method Development — Table 7

**System**

```text
You are an AI assistant whose primary goal is to propose innovative, rigorous, and valid methodologies to solve newly identified scientific problems derived from existing scientific literature, in order to empower researchers to pioneer groundbreaking solutions that catalyze breakthroughs in their fields.
```

**User**

```text
You are going to propose a scientific method to address a specific research problem. Your method should be clear, innovative, rigorous, valid, and generalizable. This will be based on a deep understanding of the research problem, its rationale, existing studies, and various entities.

Understanding of the research problem, existing studies, and entities is essential:
- The research problem has been formulated based on an in-depth review of existing studies and a potential exploration of relevant entities, which should be the cornerstone of your method development.
- The existing studies refer to the target paper that has been pivotal in identifying the problem, as well as the related papers that have been additionally referenced in the problem discovery phase, all serving as foundational material for developing the method.
- The entities can include topics, keywords, individuals, events, or any subjects with possible direct or indirect connections to the existing studies, serving as auxiliary sources of inspiration or information that may be instrumental in method development.

Your approach should be systematic:
- Start by thoroughly reading the research problem and its rationale, to understand your primary focus.
- Next, proceed to review the titles and abstracts of existing studies, to gain a broader perspective and insights relevant to the primary research topic.
- Finally, explore the entities to further broaden your perspective, drawing upon a diverse pool of inspiration and information, while keeping in mind that not all may be relevant.

I am going to provide the research problem, existing studies (target paper & related papers), and entities, as follows:
Research problem: {researchProblem}
Rationale: {researchProblemRationale}
Target paper title: {paper['title']}
Target paper abstract: {paper['abstract']}
Related paper titles: {relatedPaper['titles']}
Related paper abstracts: {relatedPaper['abstracts']}
Entities: {Entities}

With the provided research problem, existing studies, and entities, your objective now is to formulate a method that not only leverages these resources but also strives to be clear, innovative, rigorous, valid, and generalizable. Before crafting the method, revisit the research problem, to ensure it remains the focal point of your method development process.
Research problem: {researchProblem}
Rationale: {researchProblemRationale}

Then, following your review of the above content, please proceed to propose your method with its rationale, in the format of
Method:
Rationale:
```

---

## 3. Experiment Design — Table 8

**System**

```text
You are an AI assistant whose primary goal is to design robust, feasible, and impactful experiments based on identified scientific problems and proposed methodologies from existing scientific literature, in order to enable researchers to systematically test hypotheses and validate groundbreaking discoveries that can transform their respective fields.
```

**User**

```text
You are going to design an experiment, aimed at validating a proposed method to address a specific research problem. Your experiment design should be clear, robust, reproducible, valid, and feasible. This will be based on a deep understanding of the research problem, scientific method, existing studies, and various entities.

Understanding of the research problem, scientific method, existing studies, and entities is essential:
- The research problem has been formulated based on an in-depth review of existing studies and a potential exploration of relevant entities.
- The scientific method has been proposed to tackle the research problem, which has been informed by insights gained from existing studies and relevant entities.
- The existing studies refer to the target paper that has been pivotal in identifying the problem and method, as well as the related papers that have been additionally referenced in the discovery phase of the problem and method, all serving as foundational material for designing the experiment.
- The entities can include topics, keywords, individuals, events, or any subjects with possible direct or indirect connections to the existing studies, serving as auxiliary sources of inspiration or information that may be instrumental in your experiment design.

Your approach should be systematic:
- Start by thoroughly reading the research problem and its rationale followed by the proposed method and its rationale, to pinpoint your primary focus.
- Next, proceed to review the titles and abstracts of existing studies, to gain a broader perspective and insights relevant to the primary research topic.
- Finally, explore the entities to further broaden your perspective, drawing upon a diverse pool of inspiration and information, while keeping in mind that not all may be relevant.

I am going to provide the research problem, scientific method, existing studies (target paper & related papers), and entities, as follows:
Research problem: {researchProblem}
Rationale: {researchProblemRationale}
Scientific method: {scientificMethod}
Rationale: {scientificMethodRationale}
Target paper title: {paper['title']}
Target paper abstract: {paper['abstract']}
Related paper titles: {relatedPaper['titles']}
Related paper abstracts: {relatedPaper['abstracts']}
Entities: {Entities}

With the provided research problem, scientific method, existing studies, and entities, your objective now is to design an experiment that not only leverages these resources but also strives to be clear, robust, reproducible, valid, and feasible. Before crafting the experiment design, revisit the research problem and proposed method, to ensure they remain at the center of your experiment design process.
Research problem: {researchProblem}
Rationale: {researchProblemRationale}
Scientific method: {scientificMethod}
Rationale: {scientificMethodRationale}

Then, following your review of the above content, please proceed to outline your experiment with its rationale, in the format of
Experiment:
Rationale:
```

---

## 4. ReviewingAgent Problem Validation — Table 9

**System**

```text
You are an AI assistant whose primary goal is to assess the quality and validity of scientific problems across diverse dimensions, in order to aid researchers in refining their problems based on your evaluations and feedback, thereby enhancing the impact and reach of their work.
```

**User**

```text
You are going to evaluate a research problem for its {metric}, focusing on how well it is defined in a clear, precise, and understandable manner.

As part of your evaluation, you can refer to the existing studies that may be related to the problem, which will help in understanding the context of the problem for a more comprehensive assessment.
- The existing studies refer to the target paper that has been pivotal in identifying the problem, as well as the related papers that have been additionally referenced in the discovery phase of the problem.

The existing studies (target paper & related papers) are as follows:
Target paper title: {paper['title']}
Target paper abstract: {paper['abstract']}
Related paper titles: {relatedPaper['titles']}
Related paper abstracts: {relatedPaper['abstracts']}

Now, proceed with your {metric} evaluation approach that should be systematic:
- Start by thoroughly reading the research problem and its rationale, keeping in mind the context provided by the existing studies mentioned above.
- Next, generate a review and feedback that should be constructive, helpful, and concise, focusing on the {metric} of the problem.
- Finally, provide a score on a 5-point Likert scale, with 1 being the lowest, please ensuring a discerning and critical evaluation to avoid a tendency towards uniformly high ratings (4-5) unless fully justified:
{criteria}

I am going to provide the research problem with its rationale, as follows:
Research problem: {researchProblem}
Rationale: {researchProblemRationale}

After your evaluation of the above content, please provide your review, feedback, and rating, in the format of
Review:
Feedback:
Rating (1-5):
```

`{metric}` ∈ {Clarity, Relevance, Originality, Feasibility, Significance} ; `{criteria}` = induced description from Table13 (5-level rubric)

---

## 5. ReviewingAgent Method Validation — Table 10

**System**

```text
You are an AI assistant whose primary goal is to assess the quality and soundness of scientific methods across diverse dimensions, in order to aid researchers in refining their methods based on your evaluations and feedback, thereby enhancing the impact and reach of their work.
```

**User**

```text
You are going to evaluate a scientific method for its {metric} in addressing a research problem, focusing on how well it is described in a clear, precise, and understandable manner that allows for replication and comprehension of the approach.

As part of your evaluation, you can refer to the research problem, and existing studies, which will help in understanding the context of the proposed method for a more comprehensive assessment.
- The research problem has been used as the cornerstone of the method development, formulated based on an in-depth review of existing studies and a potential exploration of relevant entities.
- The existing studies refer to the target paper that has been pivotal in identifying the problem and method, as well as the related papers that have been additionally referenced in the discovery phase of the problem and method.

The research problem and existing studies (target paper & related papers) are as follows:
Research problem: {researchProblem}
Rationale: {researchProblemRationale}
Target paper title: {paper['title']}
Target paper abstract: {paper['abstract']}
Related paper titles: {relatedPaper['titles']}
Related paper abstracts: {relatedPaper['abstracts']}

Now, proceed with your {metric} evaluation approach that should be systematic:
- Start by thoroughly reading the proposed method and its rationale, keeping in mind the context provided by the research problem, and existing studies mentioned above.
- Next, generate a review and feedback that should be constructive, helpful, and concise, focusing on the {metric} of the method.
- Finally, provide a score on a 5-point Likert scale, with 1 being the lowest, please ensuring a discerning and critical evaluation to avoid a tendency towards uniformly high ratings (4-5) unless fully justified:
{criteria}

I am going to provide the proposed method with its rationale, as follows:
Scientific method: {scientificMethod}
Rationale: {scientificMethodRationale}

After your evaluation of the above content, please provide your review, feedback, and rating, in the format of
Review:
Feedback:
Rating (1-5):
```

`{metric}` ∈ {Clarity, Validity, Rigorousness, Innovativeness, Generalizability}

---

## 6. ReviewingAgent Experiment Validation — Table 11

**System**

```text
You are an AI assistant whose primary goal is to meticulously evaluate the experimental designs of scientific papers across diverse dimensions, in order to aid researchers in refining their experimental approaches based on your evaluations and feedback, thereby amplifying the quality and impact of their scientific contributions.
```

**User**

```text
You are going to evaluate an experiment design for its {metric} in validating a scientific method to address a research problem, focusing on how well it is described in a clear, precise, and understandable manner, enabling others to grasp the setup, procedure, and expected outcomes.

As part of your evaluation, you can refer to the research problem, scientific method, and existing studies, which will help in understanding the context of the designed experiment for a more comprehensive assessment.
- The research problem has been formulated based on an in-depth review of existing studies and a potential exploration of relevant entities.
- The scientific method has been proposed to tackle the research problem, which has been informed by insights gained from existing studies and relevant entities.
- The existing studies refer to the target paper that has been pivotal in identifying the problem, method, and experiment, as well as the related papers that have been additionally referenced in their discovery phases.

The research problem, scientific method, and existing studies (target paper & related papers) are as follows:
Research problem: {researchProblem}
Rationale: {researchProblemRationale}
Scientific method: {scientificMethod}
Rationale: {scientificMethodRationale}
Target paper title: {paper['title']}
Target paper abstract: {paper['abstract']}
Related paper titles: {relatedPaper['titles']}
Related paper abstracts: {relatedPaper['abstracts']}

Now, proceed with your {metric} evaluation approach that should be systematic:
- Start by thoroughly reading the experiment design and its rationale, keeping in mind the context provided by the research problem, scientific method, and existing studies mentioned above.
- Next, generate a review and feedback that should be constructive, helpful, and concise, focusing on the {metric} of the experiment.
- Finally, provide a score on a 5-point Likert scale, with 1 being the lowest, please ensuring a discerning and critical evaluation to avoid a tendency towards uniformly high ratings (4-5) unless fully justified:
{criteria}

I am going to provide the designed experiment with its rationale, as follows:
Experiment design: {experimentDesign}
Rationale: {experimentDesignRationale}

After your evaluation of the above content, please provide your review, feedback, and rating, in the format of
Review:
Feedback:
Rating (1-5):
```

`{metric}` ∈ {Clarity, Validity, Robustness, Feasibility, Reproducibility}

---

## 7. Criteria (Table 12 base, Tables 13-15 induced)

### Table 12 base one-sentence

**Problem:**
- Clarity: whether problem defined clear precise understandable
- Relevance: pertinent applicable to current field/context
- Originality: novel challenge unique perspective not extensively explored
- Feasibility: realistically investigated with available resources reasonable constraints
- Significance: importance potential impact contribution broader implications

**Method:**
- Clarity: described clear precise understandable allows replication comprehension
- Validity: accuracy relevance soundness appropriate directly relevant to objectives
- Rigorousness: thoroughness precision consistency systematic well-structured high standards
- Innovativeness: introduces new techniques approaches perspectives differ standard advance field
- Generalizability: extent applicable other contexts populations settings beyond scope

**Experiment:**
- Clarity: described clear precise understandable enabling grasp setup procedure expected outcomes
- Validity: appropriateness soundness accurately addressing questions effectively validating methods ensuring tests what intended
- Robustness: durability across wide range conditions variables ensuring outcomes not reliant few specific cases remains consistent broad spectrum scenarios
- Feasibility: realistically implemented with available resources time technological constraints practical achievable
- Reproducibility: information sufficient detailed enough other researchers reproduce same methodology conditions ensuring reliability findings

### Table 13 induced Problem criteria (5 levels each)

**Clarity**
1. Highly ambiguous manner lacking clear definition leaving significant room interpretation confusion.
2. Somewhat defined but vague terms insufficient detail challenging grasp full scope objective.
3. Straightforward but lacks depth specificity needed fully convey nuances boundaries.
4. Clearly articulated precise terminology sufficient detail providing solid understanding scope objectives minimal ambiguity.
5. Exceptionally clear concise specific every term aspect well-defined leaving no room misinterpretation fully encapsulating scope aims.

**Relevance**
1. Almost no relevance failing connect established context or build upon existing work.
2. Minimal relevance only superficial connections lack meaningful integration prior studies.
3. Somewhat relevant moderate attempt align field but lacking significant innovation depth.
4. Relevant well-connected field demonstrating good understanding existing work offering promising contributions.
5. Highly relevant deeply integrated current context significant advancement.

**Originality**
1. No discernible originality closely mirroring existing without novel perspectives challenges.
2. Minimal originality slight variations known studies lacking significant new insights innovative approaches.
3. Moderate originality some new insights angles but not sufficiently groundbreaking distinct.
4. Notably original unique challenge perspective well-differentiated existing studies contributing valuable new understanding.
5. Highly original pioneering challenge perspective not explored before setting new direction.

**Feasibility**
1. Fundamentally infeasible insurmountable resource constraints lack foundational research critical methodological flaws.
2. Significant feasibility challenges resource availability knowledge gaps technical limitations unlikely progress.
3. Feasible to some extent but notable obstacles resources support technical implementation could hinder advancements.
4. Mostly feasible manageable challenges supported adequate existing research clear achievable methodology minor issues persist.
5. Highly feasible minimal barriers well-supported ample resources robust clear methodology promising advancements.

**Significance**
1. Minimal to no significance lacking relevance potential impact advancing field contributing practical applications.
2. Limited significance narrow impact minor contributions little no practical implications.
3. Average significance some contributions potential practical implications but lacks innovation broader impact.
4. Significant notable contributions valuable practical implications evidence potential broader impact advancement.
5. Exceptional significance groundbreaking contributions broad transformative potential impacts substantial practical applications diverse domains.

### Table 14 Method induced (abbrev)

Clarity L1 extremely vague ambiguous impossible understand replicate without additional info... L5 exceptionally clear precise detailed enabling straightforward replication thorough understanding no ambiguities.

Validity L1 fundamental misunderstanding lacks credible alignment... L5 exceptional understanding robust scientific foundation exemplary integration advancement.

Rigorousness L1 fundamental lack systematic inconsistencies inaccuracies disregard standards... L5 exceptional rigorousness outstanding thoroughness precision consistency benchmark.

Innovativeness L1 no novel fully relying existing techniques without modification... L5 groundbreaking innovation fundamentally transforming approach novel techniques redefining field standard practices.

Generalizability L1 no adaptability failing extend beyond original... L5 highly adaptable clear evidence broad applicability across diverse contexts populations settings.

### Table 15 Experiment induced

Clarity L1 extremely unclear critical details missing ambiguous nearly impossible understand setup procedure expected outcomes... L5 exceptionally clear precise detailed enabling easy understanding no ambiguity need further clarification.

Validity L1 fundamental misunderstanding lacks alignment no evidence validity... L5 excellently aligns robust evidence outstandingly addressing questions testing methods without significant limitations.

Robustness L1 fundamental lack durability adaptability highly unreliable non-replicable... L5 exceptional commitment meticulous attention durability adaptability all possible conditions highly reliable universally applicable.

Feasibility L1 fundamentally unfeasible insurmountable constraints virtually impossible... L5 highly feasible no significant constraints implemented smoothly successfully.

Reproducibility L1 lacks critical details virtually impossible replicate same conditions methodologies... L5 exemplary clarity detail comprehensiveness ensuring precisely effortlessly replicate identical conditions methodologies.

---

## 8. Criteria Induction Prompt (for generating Tables 13-15 from human pairs)

From paper Sec 4: "we first collect 10 pairs of research ideas and their associated scores for every evaluation criterion on 5-point Likert scale, annotated by human researchers having at least 3 papers. After that, we prompt the LLM with these human-annotated pairs to induce detailed descriptions for evaluation criteria (Lin et al 2024)."

**Reconstructed prompt:**

```text
You are an expert evaluator aligning model judgments with human preferences.

You have 10 examples of human judgments for criterion {metric} for {idea_type} (Problem/Method/Experiment). Each example contains:
- Research idea text
- Human score 1-5 on Likert

Examples:
{example_1_idea}
Human Score: {score_1}
...
{example_10_idea}
Human Score: {score_10}

Task: Induce a detailed description for each level 1 to 5 of this criterion, reflecting underlying human preferences observed in examples. Each level description should be specific, distinguishable, and actionable for future evaluators.

Return JSON:
{
  "criterion": "{metric}",
  "level_1": "Description when score is 1...",
  "level_2": "...",
  "level_3": "...",
  "level_4": "...",
  "level_5": "..."
}

Focus on nuances that differentiate levels: clarity of definition, integration with prior work, novelty, feasibility constraints, etc.

Make descriptions mirror human annotator reasoning but generalized.
```

Used to generate Tables 13-15.

---

## 9. Evaluation Prompts (Appendix A)

### Scoring prompt (Likert)

```text
You are an expert evaluator for scientific ideas.

Task: rate the following {idea_type} based on criterion {metric} on 5-point Likert scale.

Criteria description:
{criteria_description_for_metric}  # from induced Table 13-15

Idea to evaluate:
{idea_type}: {idea_text}
Rationale: {rationale}
(Optional) Context: target paper {title, abstract} + related papers titles/abstracts

Provide reasoning step-by-step, then final Rating (1-5).

Format:
Reasoning: ...
Rating: 1-5
```

### Pairwise comparison prompt

```text
You are an expert evaluator comparing two research ideas.

Criterion: {metric} for {idea_type}

Idea A:
{idea_A_text}

Idea B:
{idea_B_text}

Context: {target paper + related...}

Which idea is better for criterion {metric}? Consider {criteria_description}.

Return:
Reasoning: ...
Winner: A|B|Tie
```

Both model-based evaluation use GPT-4 Nov 06 2023.

Human evaluation similar but with domain experts ≥3 papers, judging only ideas based on own papers, ensuring relevance; 20% double-annotated for agreements.

---

## 10. Entity Retrieval Logic — Equations (1)(2)

**Formal knowledge store K ∈ R^{m×m} sparse**

- m = total unique entities identified
- Counting co-occurrences between entity pairs within individual papers + count each entity
- EL(l): entity linker tags canonicalizes entities in paper l, returns multiset E_l (allowing repetitions) from titles+abstracts due length

- Build: consider all possible pairs of E represented as {ei,ej} (i,j)∈C(|E|,2) where e∈E, store in K

**Retrieval probabilistic form top-k relevant external entities:**

Equation (1):
Ret({l0..ln};K) = argmax_{I⊂[m]:|I|=k} ∏ P(ei | E_{l0..ln}) where ei ∉ E_{l0..ln}

Equation (2) Bayes + independence approx:
argmax_{I} ∏ (∏_{ej∈E} P(ej|ei)) × P(ei) where P(ej|ei), P(ei) derived from normalized K sparse matrix.

Alternative embedding-based retrieval: entities highest similarity to entities appearing in current literature used for generation, similarities calculated embedding-level between entities over latent space represented by entity linker (Wu et al 2020). Provides similar-concept entities vs co-occurrence may retrieve opposite concepts (e.g., limitations mentioned alongside proposed ideas) — both comparable results Table5.

Implementation in raw_prompt_files/entity_retrieval_logic.py

---

## 11. Prompt wiring map

| Prompt | Idea type | Knowledge sources | Output |
|---|---|---|---|
| Problem identification Table6 | Problem | l0 + {l1..ln} + Ret(K) | Problem + Rationale |
| Method development Table7 | Method | Problem+Rationale + l0..ln + Ret(K) | Method + Rationale |
| Experiment design Table8 | Experiment | Problem+Rationale + Method+Rationale + l0..ln + Ret(K) | Experiment + Rationale |
| Reviewing Problem Table9 | Review | {metric} + criteria + problem+rationale + l0..ln | Review/Feedback/Rating 1-5 |
| Reviewing Method Table10 | Review | {metric} + criteria + problem+rationale + method+rationale + l0..ln | Review/Feedback/Rating |
| Reviewing Experiment Table11 | Review | {metric}+criteria+problem+method+rationale + l0..ln | Review/Feedback/Rating |
| Criteria induction | Induction | 10 human-annotated pairs per criterion | Level 1-5 descriptions |
| Evaluation scoring | Eval | idea + criteria induced + context | Reasoning + Rating |
| Evaluation pairwise | Eval | idea A vs B + criteria | Reasoning + Winner |

Loop: Generate → ReviewingAgents feedback → refine → iterate until 3 steps saturation or max iterations
