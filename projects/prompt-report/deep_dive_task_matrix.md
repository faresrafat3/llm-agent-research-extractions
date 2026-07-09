# The Prompt Report — Deep Dive Task Matrix

| Technique Family | Representative methods | Input | Output | Core Loop | Key Decision | Condition |
|---|---|---|---|---|---|---|
| Zero-Shot ICL | Emotion, Role, Style, S2A, SimToM, RaR, RE2, Self-Ask | query + instruction | answer | single pass | choose persona/style? | context_window, safety |
| Few-Shot ICL | Few-Shot, KNN, Vote-K, SG-ICL | query + k exemplars | answer | retrieve/select exemplars | k=? order=? | exemplar quality, token budget |
| Thought Generation | CoT, Zero-Shot CoT, Analogical, Step-Back, ThoT | query | reasoning trace + answer | sequential thought steps | use CoT? which variant? | reasoning_need, latency |
| Decomposition | Least-to-Most, Plan-and-Solve, ToT, PoT | complex query | sub-answers → final | decompose → solve subproblems → aggregate | decomposition granularity? | task complexity |
| Ensembling | Self-Consistency, DiVeRSe, USP | query | n samples → vote | sample n times | n=? aggregation=? | budget, variance tolerance |
| Self-Criticism | Self-Refine, CoVe, Self-Verification | draft answer | critique → revised answer | generate → feedback → refine loop | stop_criteria? | max_iters, improvement_delta |
| Answer Engineering | Verbalizer, Extractor, Answer Shape/Space | raw LLM output | structured label | parse / map | shape: token/span/free? | downstream parser |
| Prompt Optimization | APE, OPRO, Promptbreeder | demos / meta-prompt | optimized prompt | propose → evaluate → mutate | search algorithm? | eval budget |
| Agents | ReAct, Toolformer, Code Agents | query + tools | action trajectory → answer | Thought/Action/Observation loop | which tool? when stop? | tool availability, safety |
| Multilingual | Translate-then-Reason, Cross-lingual CoT | non-EN query | EN reasoning → localized answer | translate → reason → back-translate | pivot language? | language resource level |
| Multimodal | MM-CoT, Chain-of-Images, Negative Prompt | image+text / audio / video | multimodal output | modality fusion | fusion strategy? | modality alignment |
| Evaluation | LLM-as-a-Judge, G-Eval | candidate output + criteria | score / preference | judge → score → aggregate | judge model? rubric? | bias mitigation |

Operational patterns extracted from all 58+40 techniques, with inputs/outputs/loops/decisions/conditions documented.
