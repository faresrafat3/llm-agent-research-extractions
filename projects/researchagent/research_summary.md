# ResearchAgent — Research Summary

## Identity

- **Title:** ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models
- **ArXiv:** 2404.07738 v2 Feb 9 2025, NAACL 2025
- **Code:** https://github.com/JinheonBaek/ResearchAgent
- **Authors:** Baek, Jauhar, Cucerzan, Hwang
- **Goal:** Automate first phase of scientific research — ideation of novel problems, methods, experiments — leveraging LLM encyclopedic knowledge + linguistic reasoning + cross-domain pollination

## Motivation

Traditional research: slow, effort-intensive, requires synthesizing 7M+ papers/year, plus deep expertise. Recent LLMs work accelerates second phase (experimental validation: code for ML, chemical space, molecular dynamics). ResearchAgent targets first phase (idea generation) open-ended.

Inspired by how researchers:
- Read related literature broadly/deeply (citation graph)
- Maintain encyclopedic view of concepts across domains (entity co-occurrence)
- Rely on colleague feedback (ReviewingAgents)

## Architecture

### (A) Scientific Knowledge Sources

1. **Academic Graph**: Start with core paper l0, explore related papers via references/citations via Semantic Scholar API. Average 87 refs per core.
2. **Entity-Centric Knowledge Store K**:
   - Matrix K ∈ R^{m×m} where m = unique entities, sparse
   - Build by extracting entities over all available literature L (50,091 papers May–Dec 2023 + refs) using BLINK linker (Wu et al 2020) tagging canonical entities from titles+abstracts (since full papers long). Even off-the-shelf works despite not trained for science (Table 16 examples).
   - Multiset El = EL(l) for paper l
   - Consider all pairs {ei,ej} C(|E|,2) count co-occurrences + single counts
   - Versatile, can use any entity linker
   - Example: term “database” might appear in hematology via co-occurrence enabling cross-domain inspiration (physics ↔ hematology)

### Entity Retrieval

Given group interconnected papers {l0..ln}, define entities E_{l0..ln} = Union EL(li)

Retrieval Ret(...;K) = argmax_{I⊂[m],|I|=k} ∏ P(ei | E) where ei ∉ E_{l0..ln} (Equation 1)

By Bayes independence approximation:

Equation (2): argmax ∏ (∏_{ej∈E} P(ej|ei)) × P(ei) where P(ej|ei), P(ei) derived from normalized K

Alternatively embedding-based retrieval: similarities in latent space of entity linker, using entities highest similarity to current literature entities; comparable results Table5.

Retrieved top-k external entities augment LLM context.

Instantiation: o = LLM(T({l0..ln}, Ret({l0..ln};K))) called ResearchAgent.

### (B) Iterative Research Idea Refinement — ReviewingAgents

- Attempting to write full idea in one go ineffective; humans write drafts iteratively improving based on reviews.
- Introduce LLM-powered ReviewingAgents providing reviews & feedback per 5 criteria per idea type.
- ReviewingAgents instantiated similarly to ResearchAgent with different templates Tables 9-11.
- Each of problem/method/experiment evaluated with own specific 5 criteria (Table12 labels, Figure2).
- Based on reviews, ResearchAgent iteratively updates refines idea.

Crucially: LLM judgments may not align with human researchers; no ground truth available; collecting annotations expensive. Ensure alignment by automatically generating human preference-aligned evaluation criteria with few human annotations:
- Collect 10 pairs idea + scores per criterion on 5-point Likert annotated by researchers ≥3 papers
- Prompt LLM with these pairs to induce detailed descriptions for criteria (Lin et al 2024) Tables 13-15
- These induced criteria reflect underlying human preferences and are used by ReviewingAgents
- Also 5 human annotators judge quality of induced criteria; 2 strongly agree, 3 moderately agree.

## Idea generation templates

See prompts_complete.md for full prompts Tables 6-8.

- Problem identification: System "identify promising, new, key scientific problems" + User systematic reading target → related → entities, then formulate Problem + Rationale with original/clear/feasible/relevant/significant goal, revisiting target title/abstract.
- Method development: System propose innovative rigorous valid methodologies; similar systematic reading problem+rationale + existing studies + entities → Method + Rationale clear/innovative/rigorous/valid/generalizable.
- Experiment design: System design robust feasible impactful experiments; reading problem+method rationales + existing studies + entities → Experiment + Rationale clear/robust/reproducible/valid/feasible.

All prompts keep target paper as focal point before crafting final output.

## ReviewingAgent templates Tables 9-11

- Problem validation: System assess quality/validity across dimensions to aid refining; User evaluate problem for {metric} clarity etc., refer existing studies target+related, systematic approach reading problem+context → constructive review/feedback + score 1-5 Likert with criteria, ensure discerning critical evaluation avoid uniform 4-5 unless justified, format Review/Feedback/Rating.

- Method validation: similar but evaluate method for {metric} addressing problem, context research problem + existing studies, format same.

- Experiment design validation: evaluate experiment for {metric} validating method to address problem, context problem+method+existing studies → same format.

Each metric has 5 levels induced.

## Criteria Tables 12-15

- Table12 base criteria descriptions 1-sentence per metric (5 per idea)
- Table13 induced criteria for Problem validation 5 levels per metric (Clarity 1 ambiguous lacking definition → 5 exceptionally clear concise specific no misinterpretation; Relevance 1 almost no relevance →5 highly relevant deeply integrated advancement; Originality 1 no discernible originality mirroring →5 highly original pioneering new direction; Feasibility 1 fundamentally infeasible →5 highly feasible minimal barriers; Significance 1 minimal no significance →5 exceptional groundbreaking transformative)
- Table14 Method: Clarity 1 extremely vague impossible replicate →5 exceptionally clear precise no ambiguity; Validity 1 fundamental misunderstanding →5 exceptional understanding robust foundation; Rigorousness 1 fundamental lack systematic →5 exceptional thoroughness benchmark; Innovativeness 1 no novel relying existing →5 groundbreaking transforming redefining; Generalizability 1 no adaptability fails beyond original →5 highly adaptable broad diverse
- Table15 Experiment: Clarity, Validity, Robustness, Feasibility, Reproducibility each 1 extremely unclear missing critical →5 exemplary clarity detail comprehensiveness effortless replication.

## Evaluation setup

No ground truth due open-ended valid ideas many possible, exhaustive listing suboptimal requiring time expertise.

Thus combination model-based automatic + manual human.

Model-based: GPT-4 judge quality; each problem/method/experiment 5 criteria; LLM rates 5-point Likert or pairwise comparisons between two ideas different models; prompts Appendix A.

Human: expert researchers ≥3 papers, judge only ideas generated based on own papers (high relevance). 10 researchers, 20% double-annotated. Score + pairwise.

Implementation details: GPT-4 release Nov 06 2023 (trained up to Apr 2023) as base for all models; BLINK linker; papers May 01 2023–Dec 31 2023 50,091 total; prompts Appendix A.3.

## Experimental results

Main results Figure2 human+model scoring: full ResearchAgent outperforms all baselines large margins every metric across problems/methods/experiment designs. Particularly gains on creativity Originality problems and Innovativeness methods since entities offer novel views not observable in citation-based papers alone. Figure3 pairwise win ratio highest.

Analysis on Inter-Annotator Agreements Table1 scoring Spearman, pairwise Cohen κ: Human-Human Scoring 0.83/0.76/0.67 problem/method/experiment, Pairwise 0.62/0.62/0.41 ; Human-Model Scoring 0.64/0.58/0.49 Pairwise 0.71/0.62/0.52 → human high reliable, human-model also high indicating reasonable proxy.

Refinement Steps Figure4: improvements with increased steps, saturation after 3 iterations diminishing returns aligning Du et al 2023 agent-based refinement.

Ablation knowledge sources Table2: each source contributes, relevant references especially helpful; random elements more helpful than none (LLM filters noise incidental value).

Human alignment Figure5 distributions: model without alignment skewed different from human; after alignment calibrated distribution more closely resembles human.

Correlation citation counts Figure6 bucket low middle high: high-impact core papers tend higher quality ideas likely ability identify gaps propose feasible methods connect other works; computer science papers vs all increase score when citations increase supporting generalizability of criteria even though induced mainly with CS papers.

Comparisons hypothesis generation Table3: vs SciMON and Hypothesis Proposer focusing predicting links between variables; ResearchAgent generates open-ended ideas higher clarity 4.11 relevance 4.88 originality 4.77 feasibility 4.05 significance 4.81.

Without refinement Figure8 still full outperforms.

Domain breakdown Figure9: high-resource domains CS Medicine Engineering > low-resource Physics Chem Math due LLM pretraining distribution.

Entity retrieval strategies Table5 co-occurrence 4.52/4.28/4.18 problem/method/experiment vs embedding 4.49/4.34/4.16 vs w/o entity 4.35/4.13/4.02 → comparable between retrieval strategies, confirm most entities from co-occurrence relevant.

Examples Table16: e.g., Knowledge-Augmented Language Model Prompting for Zero-Shot KG QA + entities Natural language QA Wikipedia etc → Problem Developing Multimodal Knowledge-Aware Prompting System for Multilingual Zero-Shot QA across Structured and Unstructured Data Sources + refined method IMKO LIRE PLON C-MILS UCAPF; also Whole-brain annotation Drosophila connectome + entities Virtual Fly Brain etc → Problem Investigating Functional Implications of Connectome Variability Across Environmental and Genetic Contexts + method multi-tiered connectomics behavioral assays genetic manipulation computational modeling.

## Limitations & ethics

- Training data after cutoff ensures novelty check but entity store building uses May-Dec 2023 papers overlapping evaluation? careful.
- Human evaluation limited to 10 experts.
- Model-based proxy not perfect.
- Potential misuse generating many low-quality ideas flooding review.
- Entity linker off-the-shelf not science-optimized.

## Relation to other systems

- Follows literature-based hypothesis generation tradition (Wang et al 2023b SciMON) but open-ended.
- Pioneers iterative refinement with ReviewingAgents similar to peer discussion.
- Provides blueprint for Scientific Intelligence Survey taxonomy: P2 Context-Augmented (references + entities), P5 Role-Interactive Multi-Agent (ReviewingAgents), P3 Deliberative Reflective (refinement loops 3 steps saturation).
- Feeds GAPMAP gap identification → ResearchAgent problem formulation.
