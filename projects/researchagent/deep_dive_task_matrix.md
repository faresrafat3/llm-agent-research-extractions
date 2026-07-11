
# ResearchAgent — Deep Dive Task Matrix

| Phase | Goal | Input | Prompt template | Output | Evaluation | Insight |
|---|---|---|---|---|---|---|
| **P0 Data** | Build benchmark post-LLM cutoff | Semantic Scholar API papers after May01 2023, >20 cites | No LLM | 300 core papers (sample) avg 87 refs, abstract 2.17 entities; 50,091 papers May-Dec 2023 + refs for entity store | Distribution disciplines Figure7 | Ensures novelty vs GPT-4 training Apr2023 cutoff |
| **P1 Entity store K** | Capture cross-domain concept affinity | Titles+abstracts 50,091 papers | BLINK linker off-the-shelf EL(l) multiset | Sparse matrix K∈R^{m×m} co-occurrence counts + single counts, m unique entities, pairs C(|E|,2) | Off-shelf works Table16 | Versatile any linker, enables database↔hematology cross-pollination |
| **P2 Retrieval Ret** | Augment context with novel external entities | E_{l0..ln}=Union EL(li), K | Eq1 probabilistic argmax prod P(ei|E), Eq2 Bayes indep approx prod(prod P(ej|ei))*P(ei) from normalized K; alternative embedding cosine similarity in linker latent space | Top-k external entities not in current set | Ablation Table2: w/o Entities drop, random better than none; Table5 co vs embedding comparable 4.52 vs 4.49 problem | Relevant refs especially helpful; random still helpful LLM filters noise |
| **P3 Problem generation** | Identify promising original clear feasible relevant significant problem | Target paper title abstract + {len refs} related titles abstracts + {len entities} entities | Table6 System identify promising new key scientific problems + User systematic reading target→related→entities, revisit target as focal point before crafting | Problem: + Rationale: | Model+human scoring Clarity Relevance Originality Feasibility Significance Likert1-5 | Full > w/o Entity > Naive; Originality gain biggest via entities |
| **P4 Method generation** | Propose innovative rigorous valid method to solve problem | Problem+Rationale + existing studies target+related + entities | Table7 System propose innovative rigorous valid methodologies + User systematic reading problem rationale cornerstone→existing studies→entities | Method: + Rationale: clear innovative rigorous valid generalizable | Validity Rigorousness etc | Gains Innovativeness |
| **P5 Experiment design** | Design robust feasible impactful experiments validating method | Problem+Rationale + Method+Rationale + existing studies + entities | Table8 System design robust feasible impactful experiments + User systematic reading problem+method rationales + existing studies + entities, revisit both central | Experiment: + Rationale: clear robust reproducible valid feasible | Robustness Feasibility Reproducibility | Experiment scores slightly lower agreement inherent subjectivity but still high |
| **P6 ReviewingAgents** | Simulate peer feedback, align with human | Generated ideas + existing studies + research problem/method contexts + induced criteria Tables13-15 | Table9 problem {metric} assessment, Table10 method, Table11 experiment, each systematic reading + review feedback constructive helpful concise focusing {metric} + score 1-5 discerning critical avoid uniform high | Review: Feedback: Rating (1-5): per metric per idea (15 reviewers per iteration) | Agreements Table1 human-human scoring Spearman 0.83/0.76/0.67 pairwise kappa 0.62/0.62/0.41 human-model scoring 0.64/0.58/0.49 pairwise 0.71/0.62/0.52 | LLM judgments aligned via criteria induction 10 pairs per criterion (Lin et al 2024) 5 annotators judge quality induced 2 strongly 3 moderately |
| **P7 Iterative refinement** | Improve drafts like humans | Ideas + reviews feedback history | Implicit refinement prompt (concatenate previous idea + feedback → improved version) | Improved Problem/Method/Experiment per step | Figure4 scores vs refinement steps 0-4 improvements saturated after 3 diminishing returns Du et al 2023 | Up to 3 iterations optimal |
| **P8 Evaluation scoring** | Rate quality reference-free | Idea + rationale + context + induced criteria | Scoring prompt Reasoning + Rating 1-5; Pairwise prompt Reasoning + Winner A|B|Tie | Figure2 main results scoring human+model avg & per metric; Figure3 win ratio % | Full ResearchAgent highest win ratio |
| **P9 Ablation** | Measure contribution | Variants w/o / random entities/references | Same prompts with/without sources | Table2 ablation 4.52/4.28/4.18 full vs 4.20/4.03/3.92 w/o both; Table5 retrieval strategies | References biggest drop | Each source contributes |
| **P10 Domain & citation** | Check generalizability | Papers bucketed low/middle/high citations, domains CS Medicine Eng Env Bio Materials Physics Chem Math | Same scoring | Figure6 citation correlation scores increase with citation high-impact papers lead higher quality; Figure9 domain breakdown high-resource > low-resource | Criteria induced mainly CS still generalizable |
| **P11 Comparison** | Vs prior hypothesis gen | - | Same eval | Table3 SciMON 4.04/4.37/4.56/3.98/4.15 Hypo Proposer 3.97/4.14/4.07/4.01/4.11 ResearchAgent 4.11/4.88/4.77/4.05/4.81 | Outperforms baselines significantly relevance originality significance | Open-ended > link prediction |

## Prompt wiring map extended

| Stage | Knowledge augmentation | Criteria source | Loop condition |
|---|---|---|---|
| Problem | l0 + l1..ln + Ret(K) | induced Table13 | 1 problem per core |
| Method | Problem+Rationale as cornerstone + l0..ln + Ret | Table14 | 1 method per problem |
| Experiment | Problem+Rationale + Method+Rationale + l0..ln + Ret | Table15 | 1 experiment per method |
| Review | {metric} per idea, criteria induced level 1-5 | Tables13-15 | 5 per idea ×3 ideas × refinement steps |
| Refinement | Feedback concatenated | - | 0-4 steps saturation 3 |
| Eval scoring | Context l0..ln + criteria | Tables13-15 | per criterion |
| Eval pairwise | Idea A vs B + criteria | Tables13-15 | per pair models |

## Data flow diagram textual

```
Semantic Scholar API L after May01 2023 >20 cites → sample 300 core
Core each avg 87 refs → titles+abstracts
Entity extraction BLINK EL(l) titles+abstracts only (footnote length) → multiset E
Build K sparse m×m co-occurrence + counts from 50,091 papers May-Dec2023 + refs
For each core group {l0..ln}:
    E_{l0..ln}=Union EL
    Ret Eq1/Eq2 top-k external entities ∉ E → {Entities}
    ResearchAgent T({l0..ln}, Ret):
        Table6 → Problem + Rationale (original clear feasible relevant significant)
        Table7 → Method + Rationale (clear innovative rigorous valid generalizable) using Problem as cornerstone
        Table8 → Experiment + Rationale (clear robust reproducible valid feasible) using Problem+Method
    ReviewingAgents Tables9-11 per metric per idea with induced criteria Tables13-15 → Review/Feedback/Rating 1-5 discerning
    Iterative refinement 0-4 steps feedback history → improved ideas (Figure4 saturation 3)
    Evaluation:
        Model: GPT-4 Nov06 2023 judge scoring Likert + pairwise win ratio
        Human: 10 experts ≥3 papers own papers only, 20% double-annotated Spearman κ
        Figure5 alignment distribution human vs model with/without induced criteria
        Figure6 citation buckets low/mid/high correlation
        Figure9 domain breakdown high-resource CS Medicine Eng > low-resource
    Ablations Table2 w/o Entities w/ Random Entities w/o References w/ Random References w/o both
    Retrieval comparison Table5 co-occurrence vs embedding vs w/o
    Comparison Table3 vs SciMON vs Hypothesis Proposer
Output examples Table16: KG QA multimodal system IMKO LIRE PLON C-MILS UCAPF + Drosophila connectome variability multi-tiered investigation
```
