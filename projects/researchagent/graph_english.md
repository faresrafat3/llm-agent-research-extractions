
# ResearchAgent — English Logic Graph

Source: `graph_english.mmd`

## Narrative

1. **Data sourcing**: Semantic Scholar Academic Graph API papers after May01 2023 >20 cites sample 300 core, avg 87 refs, abstract 2.17 entities, distribution disciplines Figure7. Separate 50,091 papers May-Dec 2023 + refs for entity store.

2. **Entity store K**: Matrix sparse R^{m×m}, m unique entities. BLINK linker EL(l) multiset entities titles+abstracts only due length. Pairs C(|E|,2) counted co-occurrence + single counts into K.

3. **Retrieval Ret**: For group {l0..ln}, E=Union EL, Eq1 argmax prod P(ei|E) external ei∉E, Eq2 Bayes indep approx prod(prod P(ej|ei))*P(ei) normalized K. Alternative embedding cosine similarity latent space. Top-k external entities.

4. **Generation ResearchAgent**: o=LLM(T({l0..ln}, Ret)). Table6 Problem identification systematic reading target→related→entities revisit target focal → Problem: Rationale: original clear feasible relevant significant. Table7 Method development problem rationale cornerstone → existing studies → entities → Method: Rationale: clear innovative rigorous valid generalizable. Table8 Experiment design problem+method rationales → existing studies → entities → Experiment: Rationale: clear robust reproducible valid feasible.

5. **ReviewingAgents**: Tables9-11 per metric (5 per idea: Problem Clarity Relevance Originality Feasibility Significance; Method Clarity Validity Rigorousness Innovativeness Generalizability; Experiment Clarity Validity Robustness Feasibility Reproducibility). System assess quality. User evaluate for {metric} focusing clear precise understandable manner, refer existing studies target+related, systematic reading problem/method/experiment + context, generate Review/Feedback/Rating 1-5 discerning critical avoid uniform high unless justified, criteria from induced Tables13-15.

6. **Criteria induction**: Collect 10 pairs idea + scores per criterion Likert annotated researchers ≥3 papers, prompt LLM with pairs to induce detailed level 1-5 descriptions (Lin et al 2024) Tables13-15 reflecting human preferences. 5 annotators judge quality induced 2 strongly 3 moderately.

7. **Iterative refinement**: Note one-go ineffective, humans drafts improved via reviews. Introduce reviewing agents community, iteratively updates refines ideas. Loop 0-4 steps Figure4 saturation after 3 diminishing returns Du et al 2023 pattern.

8. **Evaluation**: No ground truth open-ended many valid ideas exhaustive suboptimal. Use model-based GPT-4 Nov06 2023 judge rate Likert or pairwise comparisons per criterion + human evaluation 10 experts ≥3 papers only own papers relevant field, 20% double-annotated Spearman & Cohen κ. Alignment check human-human vs human-model Table1. Distribution Figure5 human vs model without alignment skewed vs with alignment calibrated resembles human. Citation buckets Figure6 high-impact high quality. Domain breakdown Figure9 high-resource > low-resource due LLM training distribution. Ablation Table2 references especially helpful random > none LLM filters noise. Retrieval comparison Table5 co vs embedding comparable. Comparison hypothesis generation Table3 vs SciMON Hypothesis Proposer ResearchAgent wins relevance originality significance.

See Mermaid file for flowchart.
