# ResearchAgent — Python Logic Flow Complete

Audited: PDF full text extracted, Equations, Tables 6-15, Figures 2-9, Implementation details Sec 4.4

---

## 0. Data preparation

```
L = scientific literature from Semantic Scholar Academic Graph API
Filter: papers appearing after May 01 2023 (LLM trained up to Apr 2023 per GPT-4 Nov 06 2023)
Select high-impact papers >20 citations as core papers (human tendency leverage influential)
Sample subset 300 papers as core to obtain reasonably sized benchmark
Avg number reference papers per core = 87
Abstract avg 2.17 entities
Distribution disciplines Figure7 (to be reproduced)
```

---

## 1. Entity-centric knowledge store building

```
K ∈ R^{m×m} sparse matrix, m = total unique entities

Papers for store: May 01 2023 to Dec 31 2023 available from Semantic Scholar API + their references, number 50,091 total

For each paper l in L:
    El = EL(l) where EL = BLINK entity linker (Wu et al 2020) off-the-shelf
         Tags and canonicalizes entities in l
         Target restricted to titles+abstracts due extensive length scientific publications
         Returns multiset allowing repetitions

For each E:
    Consider all possible pairs {ei,ej} (i,j)∈C(|E|,2) where e∈E
    Count co-occurrences between entity pairs within individual papers + count single entity
    Store into K (sparse format)

Result: K implemented sparse, enables retrieval
```

---

## 2. Entity retrieval Ret({l0..ln};K)

### Co-occurrence based (Equation 2)

```
Given group interconnected papers {l0..ln}
E_{l0..ln} = Union_{i=0..n} EL(li) = multiset entities extracted from group

Goal: retrieve top-k relevant external entities not in current set:
Ret = argmax_{I⊂[m]:|I|=k} ∏ P(ei | E_{l0..ln}) where ei ∉ E_{l0..ln}   Eq (1)

Applying Bayes + independence assumption entities independent:
Eq (2): argmax_{I} ∏ (∏_{ej∈E} P(ej|ei)) × P(ei)

Where P(ej|ei) and P(ei) derived from values in K suitably normalized

Instantiation research proposal generation augmented:
o = LLM(T({l0..ln}, Ret({l0..ln};K)))
We call knowledge-augmented LLM-powered idea generation approach ResearchAgent
Templates Tables 6,7,8
```

### Embedding-based alternative (Appendix B.3)

```
Uses entities highest similarity to entities appearing in current literature (core+refs)
Similarities calculated embedding-level between entities over latent space represented by entity linker
Provides mostly similar concepts vs co-occurrence may provide opposite concepts (since limitations mentioned alongside proposed ideas)
Results Table5 comparable: Co-occurrence 4.52/4.28/4.18 vs Embedding 4.49/4.34/4.16 vs w/o Entity 4.35/4.13/4.02 problem/method/experiment
May confirm not much difference quality, most entities from co-occurrence relevant
```

---

## 3. Research idea generation stages

### Stage A: Naive ResearchAgent baseline

```
o = LLM(T({l0}))   # only core paper
Uses Table6 prompt with len(references)=0 len(entities)=0
```

### Stage B: ResearchAgent w/o Entity Retrieval

```
o = LLM(T({l0,l1..ln}))  # core + relevant references without entities
Uses Table6 prompt without entities field or empty
```

### Stage C: Full ResearchAgent (ours)

```
o = LLM(T({l0..ln}, Ret({l0..ln};K)))   # relevant refs + entities
Full prompts Tables 6-8 with both
```

### Sequential generation Problem → Method → Experiment

```
Problem step:
    Input: target paper title abstract, relatedPaper titles abstracts (len), Entities
    Approach systematic: read target → read related broader perspective → explore entities diverse pool
    Revisit target title abstract to ensure focal point before crafting problem
    Output format Problem: Rationale:

Method step:
    Input: researchProblem + Rationale (from previous), target+related papers, Entities
    Systematic: read problem rationale cornerstone → review existing studies titles abstracts → explore entities
    Revisit research problem ensure focal point
    Output Method: Rationale: with clear/innovative/rigorous/valid/generalizable

Experiment step:
    Input: researchProblem+Rationale, scientificMethod+Rationale, target+related, Entities
    Systematic: read problem rationale + method rationale → review existing studies → explore entities
    Revisit problem+method central
    Output Experiment: Rationale: clear/robust/reproducible/valid/feasible
```

---

## 4. Iterative refinements with ReviewingAgents

```
Note: attempting write full idea one go may not effective; humans write drafts continually improved multiple rounds reviews feedback. Model community of peers by introducing set LLM-powered reviewing agents.

ReviewingAgents instantiated similarly but different templates Tables 9,10,11

Each generated idea (problem, method, experiment design) separately evaluated according its own specific five criteria (labels Figure2 detailed Table12)

Based on reviews & feedback from ReviewingAgents, ResearchAgent iteratively updates refines generation

Loop logic:
    For refinement_step in 0..max_steps (4 in Figure4):
        For each idea in [problem,method,experiment]:
            For each metric in 5 per idea (total 15 reviewers perhaps):
                ReviewingAgent evaluates idea for metric focusing criteria
                Generates Review, Feedback, Rating (1-5 Likert) ensuring discerning critical avoid uniform high unless justified
                Criteria = human-induced detailed descriptions Tables13-15 reflecting underlying preferences
        Aggregate feedback per idea
        ResearchAgent revises idea based on feedback (prompt not explicitly given but implies concatenation previous idea + reviews + feedback → improved version)

        Model-based evaluation scoring after each refinement step → Figure4 shows improvements with increased steps saturated after 3 iterations diminishing returns aligning Du et al 2023.

Implementation:
    Number refinement steps 0-4 (Figure4)
    At step 0 = initial generation without review
    Each step repeats review→refine

Human alignment for evaluation:
    Collect 10 pairs ideas + scores per criterion on 5-point Likert annotated by human researchers ≥3 papers
    Prompt LLM with human-annotated pairs to induce detailed descriptions evaluation criteria (Lin et al 2024) Tables13-15
    These criteria reflect underlying human preferences used as evaluation criteria by ReviewingAgents
    Ask 5 human annotators judge quality induced criteria: 2 agree strongly, 3 moderately

Evaluation judges (both human and model) induced criteria aligned
```

---

## 5. Evaluation logic

### Model-based evaluation (LLM as judge)

```
Uses GPT-4 Nov 06 2023 as judge
Each problem/method/experiment evaluated with 5 criteria
Ask LLM evaluation model either rate generated idea 5-point Likert per criterion or pairwise comparisons between two ideas different models
Prompts Appendix A (reconstructed in prompts_complete.md)

Scoring evaluation prompt:
- Provide criteria description induced
- Provide idea text + rationale + context target paper + related
- Request Reasoning then Rating 1-5

Pairwise evaluation prompt:
- Provide criterion + idea_type
- Provide Idea A text, Idea B text, context
- Request Reasoning + Winner A|B|Tie
- Compute win ratio % Figure3 Human vs Model evaluation

Scoring distributions Figure5: compare human evaluation vs model evaluation without alignment vs with human-aligned criteria alignment → skewed without alignment, calibrated after alignment resembles human distribution

```

### Human evaluation

```
Carefully select annotators well-versed field provide ideas highly relevant to expertise
Choose 10 expert researchers authored at least 3 papers ask judge only ideas generated based on own papers
Also experiment non-domain-experts suboptimal focus experts reliable judgments

Perform scoring each criterion + pairwise comparisons between two ideas (similar model)

Inter-annotator agreements Table1: 20% ideas evaluated by two judges
- Scoring: rank scores from each annotator measure Spearman correlation coefficient (Pirie 2006) between ranked scores
- Pairwise: Cohen kappa (Cohen 1960)
Results: Human-Human Scoring 0.83 problem 0.76 method 0.67 experiment, Pairwise 0.62/0.62/0.41 ; Human-Model Scoring 0.64/0.58/0.49 Pairwise 0.71/0.62/0.52 → high reliability

Correlation citation counts Figure6: categorize papers by citation count proxy impact visualize average score per bucket model-based evaluations → high-impact core papers lead higher quality ideas likely ability identify gaps propose feasible methods connect other works; computer science vs all scores increase when citation increases supporting generalizability human-preference-induced criteria despite induced mainly CS papers

Breakdown by domain Figure9: average scores per domain categories core papers → high-resource CS Medicine Engineering Environmental Science better than low-resource Biology Materials Physics Chem Math due LLM training data predominance high-resource
```

---

## 6. Ablation logic

```
Table2 Ablation references and entities (model-based eval scores)
- ResearchAgent full 4.52/4.28/4.18 problem/method/experiment
- w/o Entities 4.35/4.13/4.02
- w/ Random Entities 4.41/4.19/4.13
- w/o References 4.26/4.08/3.97
- w/ Random References 4.35/4.16/4.02
- w/o Entities & References 4.20/4.03/3.92

Interpretation: each knowledge source contributes performance improvement, relevant references especially helpful; random elements more helpful than none hypothesized LLM capability filter noise while still gaining incidental value

Table5 Entity retrieval strategies: Co-occurrence vs Embedding vs w/o → comparable co vs embedding, both > w/o
```

---

## 7. Comparison to hypothesis generation Table3

```
Existing methods focus predicting links between variables or generating hypotheses based on links, differs from open-ended research ideas (problems, methods, experiments)

Nevertheless compare quality generated ideas prior works Wang et al 2023b SciMON and Yang et al 2023 Hypothesis Proposer vs ResearchAgent

Metrics Clarity Relevance Originality Feasibility Significance for Problem? Table3 shows:
SciMON 4.04/4.37/4.56/3.98/4.15
Hypothesis Proposer 3.97/4.14/4.07/4.01/4.11
ResearchAgent 4.11/4.88/4.77/4.05/4.81 → higher relevance originality significance

Shows open-ended generation advantage with entity retrieval + peer review
```

---

## 8. Implementation details Sec 4.4

```
- GPT-4 OpenAI 2023 release Nov 06 2023 as basis all models, trained data up to Apr 2023 (papers used for idea generation after May 2023)
- Entity extraction BLINK linker (Wu et al 2020) with papers May 01 2023 to Dec 31 2023 (Semantic Scholar API) + references total 50,091
- Prompts Appendix A.3 detailed responses
- Semantic Scholar Academic Graph API https://www.semanticscholar.org/product/api
```

---

## 9. Decision catalog

| ID | Decision | Location |
|---|---|---|
| D1 | Naive vs w/o Entity vs Full | Baselines Sec 4.2 |
| D2 | Co-occurrence vs Embedding retrieval vs Random vs w/o | Ablation + B.3 |
| D3 | Entity extraction target titles+abstracts only vs full papers | footnote 4 due length |
| D4 | Include references? w/o References ablation | Table2 |
| D5 | Human-induced criteria vs vanilla? | Figure5 alignment |
| D6 | Refinement steps 0..4? saturation after 3 | Figure4 |
| D7 | Human expert selection only own papers vs non-experts? | Sec 4.3 human eval note footnote 9 |
| D8 | 10 human annotation pairs per criterion for induction? | Sec 3 |
| D9 | Scoring vs Pairwise evaluation? | Sec 4.3 eval setup |
| D10 | Top five criteria selected most important vs others future work | footnote 6 |
| D11 | Core papers >20 citations sampling 300? | Sec 4.1 data |
| D12 | Use GPT-4 as evaluator despite same family as generator? | justification model-based proxy high agreement |

---

## 10. Loop inventory

| Loop | Bound | File/Logic |
|---|---|---|
| Core papers benchmark | 300 sampled | Data sec 4.1 |
| References per core | avg 87 | Academic graph |
| Entity extraction over L | 50,091 papers | Build K |
| Entity pairs per paper | C(|E|,2) | K building |
| Retrieval top-k external | k unspecified but method | Ret eq |
| Generation Problem→Method→Experiment | 3 stages sequential | Tables6-8 |
| ReviewingAgents per idea | 5 criteria ×3 idea types =15 reviewers | Tables9-11 |
| Refinement steps | 0-4 (Figure4 saturation 3) | Iterative refinement |
| Evaluation scoring | per criterion 5-point | LLM judge |
| Pairwise comparisons | pairwise per 2 models | Win ratio |
| Human annotation pairs for induction | 10 per criterion | Criteria induction |
| Domain breakdown | 9 domains + All | Figure9 |

---

## 11. I/O summary

| Stage | Input | Output |
|---|---|---|
| Data L | Semantic Scholar API papers after May01 2023 | Core 300 >20 cites + 50,091 entity store papers |
| Entity extraction | Titles+abstracts | Multiset El, K matrix co-occurrence + counts |
| Retrieval | {l0..ln}, K | Top-k external entities Ret |
| Problem gen | l0 title abstract + related titles abstracts + Entities | Problem + Rationale |
| Method gen | Problem+Rationale + existing studies + Entities | Method + Rationale |
| Experiment gen | Problem+Rationale + Method+Rationale + existing studies + Entities | Experiment + Rationale |
| ReviewingAgents | idea + problem context + existing studies + criteria induced | Review + Feedback + Rating 1-5 per metric |
| Refinement | idea + feedback history | Improved idea, updated scores |
| Evaluation scoring | idea + criteria + context | Reasoning + Rating 1-5 |
| Evaluation pairwise | Idea A vs B + criteria | Reasoning + Winner A|B|Tie, Win ratio % |
| Ablations | w/o / random variants | Scores Table2+5 |
| Final outputs | full ResearchAgent ideas | Example Table16 multimodal KB prompting + Drosophila connectome |

---

## 12. Key patterns for CONSTITUTION Part 6

- GAP→Problem continuity: GAPMAP explicit gaps feed target paper problem identification
- Context augmentation: target + references + entities holistic reading systematic approach
- Peer review loop: generating review/feedback/rating with discerning critical avoidance uniform high
- Human-aligned criteria induction from few human pairs bridging LLM judge ↔ human preferences
- Iterative refinement saturation after 3 steps principle for agent-based refinement work
