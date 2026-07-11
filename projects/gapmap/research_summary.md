# GAPMAP — Research Summary

## Paper identity

- **Title:** GAPMAP: Mapping Scientific Knowledge Gaps in Biomedical Literature Using Large Language Models
- **ArXiv:** 2510.25055v1, Oct 29 2025, NeurIPS 2025 Workshop AI for Science
- **Authors:** Nourah M Salem (Colorado Anschutz/Chicago), Elizabeth White, Michael Bada, Lawrence Hunter (Chicago)
- **License:** CC BY 4.0
- **Repo:** https://github.com/lhunter-lab/GAPMAP
- **Funding:** Chan Zuckerberg Initiative AWD105712 Rare as One Ignorome

## Problem solved

Scientific literature grows faster than human ability to track **known unknowns**. Prior work focused on explicit lexical cues (uncertainty, hedging, negation). GAPMAP adds **implicit gaps** — gaps that are never stated by authors but inferrable from discourse: missing links in claim chains, generalization failures, conflicting findings without reconciliation.

## Taxonomy introduced

### Explicit vs Implicit overlay
- Preserves prior taxonomy from Boguslav et al 2023: Levels of Evidence, Barriers, Future Opportunities, Anomalous Findings, Research Aims
- Adds orthogonal dimension: explicit vs implicit **within** each category

**Explicit definition:** directly signaled by high-uncertainty cues ("unknown", "further research needed", "no RCT") or low-uncertainty hedging ("may lead to", "could cause") or negation, typically recoverable at sentence/short paragraph.

Example explicit: "It remains unknown whether long-term GLP-1 agonist therapy improves renal outcomes in non-diabetic CKD" → cue "remains unknown"

**Implicit definition:**
- (i) chain of claims containing missing link
- (ii) generalization gap where claims under limited scope but out-of-scope applicability questionable
- (iii) conflicting findings without reconciliation/experiment

Example implicit:
- Grounds: Compound E improves biomarker F in mice.
- Grounds: Biomarker F correlates poorly with clinical outcomes in humans.
- ⇒ Inferred gap Claim: It is unknown whether E improves patient outcomes.

## TABI: Toulmin-Abductive Bucketed Inference

To address implicit gaps, paper casts detection as **abductive NLI with generation** and introduces **TABI**:

- Uses **Toulmin Argument Model** (Karbach 1987): Claim–Grounds–Warrant (CGW)
- **Claim:** implied gap (required future direction)
- **Grounds:** evidence span(s) supporting Claim (quoted from source)
- **Warrant:** single sentence reasoning Grounds→Claim (coherence + entailment sanity check)
- **Bucket:** binary confidence: `more_probable` vs `least_probable` (calibration check)

Output is interpretable, allows overlap-based scoring vs gold premises/claims, and tracks source of errors.

## Datasets (4)

| # | Category | Name | Unit | Domain | Size |
|---|---|---|---|---|---|
| 1 | Explicit | IPBES | paragraph-level | Biodiversity & Ecosystem | 286 paragraphs, 657 statements |
| 2 | Explicit | Scientific Challenges & Directions (Lahav et al 2022) | section-level (up to 8K tokens) | COVID-19 | 2,894 statements from 1,786 studies |
| 3 | Implicit | Manual implicit-gap corpus | paragraph | Biomedical | 212 paragraphs from 137 PubMed articles, each with masked future direction gold |
| 4 | Implicit | Full-Text Pilot | full-paper | STEM mixed 19 domains (Immuno, Astro, Materials etc) | 24 full-texts → 23 evaluated, GPT-4o interface, author survey 18 corresponding authors |

## Experimental setups (2 experiments)

**Exp 1: Explicit knowledge gaps**
- Corpus C = sections S_i = {p1..pn}, each paragraph pj = {sentences}
- Input: sequence pj (avg 257 words, some >2500 words) tolerable; COVID sections often >8K tokens → chunking
- Chunking: Stanza parser, aligned at sentence boundaries, |T_k| ≤1000 words, defer sentence if overflow
- Prompt: zero-shot explicit extraction JSON (see prompts_complete.md)

**Exp 2: Implicit gaps**
- **2a Paragraph-level manual:** D_manual = {p1..pN} expert-annotated, each with gold implicit gap γ_i future direction. Provide pi masking future-direction claims at end. Ask model to produce Claim, Grounds, Warrant, Bucket. Success if any predicted claim matches gold. 3-shot in-context crucial; 0-shot degenerates to vague restatements.
- **2b Full-document pilot:** Each full paper P_i → GPT-4o, multi-modal, long context, generate structured pairs (Implied gap + Suggested future direction). 18 authors surveyed: agree/disagree + justification.

## Evaluation

| Task | Metric | Logic |
|---|---|---|
| Explicit IPBES | ROUGE-L F1 + stemming, one-to-one matching threshold 0.55 | TP if score>0.55; unmatched pred FP, unmatched gold FN; exact matches recorded but not required |
| Explicit COVID-19 | Accuracy + ignorance-cue dictionary validation (Boguslav et al) | Avoid penalizing plausible extra predictions beyond single gold per section; validate predicted statements carry at least one cue from dictionary |
| Implicit paragraph | Accuracy via bi-directional entailment RoBERTa-large (Cohen et al?) threshold 0.4 | (Claim vs gold) & (Warrant vs Premises) must exceed threshold to be correct |
| Full-text pilot | Human agreement percentages | Factual true 83.3%, open question 56% fully agree + 25.9% partially, impact potential 67% of partial, implementation validity 65% valid / 35% invalid due to feasibility |
| Long-context robustness | Comparison no-chunk vs chunk | Sentence-aligned ~1K-word chunks preserve F1, often boost recall |

## Results headline

**IPBES (Table 3):**
- No context limit: Llama-3.3-70B best F1 0.8307 (recall driven), GPT-5 0.7949, GPT-4o-mini 0.7907, Gemma 0.6854. GPT-4o most conservative (high precision 0.8445 low recall 0.4223)
- 1K chunks: GPT-4o-mini leads F1 0.8143, Llama-3.3-70B 0.8138. Top systems shift ~0.02 F1, chunking safe, can raise recall for smaller models.

**COVID-19 (Table 4, n=973 each setup):**
- More challenging: only one gap per section annotated vs many latent, authors use numeric contrasts/anomalies not lexical.
- 1K chunks / No limit: GPT-5 highest accuracy 63.51% / 60.64%, Llama-70B 41.73% / 39.57%, Llama-4-17B 37.2% / 38.85%, GPT-4o-mini 30.94% / 43.06%, GPT-4o 27.85% / 25.9%, Gemma 17.16% etc.
- Model complementarity: ~1.14k shared among top 4; GPT-5 many unique; IPBES ~50% shared (913) vs 843 unique.

Figure 2 spider chart: 5 categories (Research Aim, Levels of Evidence, Anomaly/Curious Findings, Barriers, Future Opportunities) — GPT-5 outermost polygon every axis, followed by Llama models, GPT-4o-mini innermost.

**Implicit paragraph (Table 5):**
- GPT-5 84.43% (179 FD Count), GPT-4o 80.66% (171), GPT-4o-mini 80.66% (171), Llama-3.3-70B 77.89% (163), Llama-4-17B 63.68% (135), Llama-3.1-8B 30.67% (65), Gemma-2-9B 22.64% (48)
- Critical factor: 3-shot vs 0-shot; even GPT-5 degenerates zero-shot
- Bucket calibration: 10-24% of correct claims bucketed as least_probable → relevance to lab/technical limitations etc.

**Implicit full-text:**
- 83.3% gaps factually true, 56% fully agree remain open + 25.9% partially, 67% of partials significant advance, 65% future directions valid.

## Takeaways

- Scale helps, larger > smaller, but open-weight competitive (Llama-70B)
- Chunking 1K sentence-aligned is safe preprocessing, boosts recall
- TABI makes implicit gaps interpretable and scorable
- 3-shot essential for implicit
- Mixture-of-LLMs recommended, unique coverages complement
- Deployment needs human-in-loop, domain adaptation, feasibility filtering

## Systems relationship

- Feeds into ResearchAgent: gap identification is first step of problem identification
- Validates against Boguslav ignorance-base 2023 taxonomy + cue dictionary
- Foundation for CONSTITUTION Part 6: HOW TO TRACK KNOWLEDGE

## Failure modes reported

- Vague restatements under zero-shot
- Over-filtering general non-research gaps needed (e.g., "SARS-CoV-2 declared pandemic" excluded)
- Feasibility invalidity 35% in full-text pilot (tech limits, budget, relevance to other groups)
- Small models struggle beyond lexical markers
