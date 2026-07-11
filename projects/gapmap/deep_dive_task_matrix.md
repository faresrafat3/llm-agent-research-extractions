# GAPMAP — Deep Dive Task Matrix

## Phase map

| Phase | Goal | Input unit | Model prompting | Output | Evaluation | Key finding |
|---|---|---|---|---|---|---|
| **P0 Preprocess** | Make long docs LLM-friendly without cutting semantics | Excerpt text (IPBES 257 avg, COVID up to 8K) | No LLM; Stanza pipeline `tokenize` or regex fallback `(?<=[.!?])\s+(?=[A-Z"“(])` | List chunks ≤1000 words sentence-aligned | Integrity: no sentence cut | Safe, preserves coherence; isolates >1000-word sentence alone |
| **P1 Explicit zero-shot** | Extract author-signaled gaps | Chunk `<<<{chunk}>>>` | System `Return ONLY valid JSON` + User `PROMPT_TEMPLATE` with strict JSON schema: Ignorance Statement (exact sentence), support_sentence/s array, justification, Ignorance Cues array | JSON array `[{Ignorance Statement, support_sentence/s, justification, Ignorance Cues},...]` or [] | IPBES: ROUGE-L F1 stemming one-to-one >0.55 ; COVID: accuracy + cue-dictionary must contain ≥1 cue (Boguslav) | Llama-70B best F1 no-limit 0.8307, GPT-5 close, GPT-4o conservative high P low R; chunking → GPT-4o-mini leads 0.8143, preserves performance |
| **P1b Dedupe + Error handling** | Clean per-doc outputs | all_items from chunks | Regex squashing whitespace deduplication | Deduped list per ID | Count unique vs shared | 50% shared in IPBES (913 shared, 843 unique); COVID 1.14k shared top-4 overlap; GPT-5 most unique |
| **P2 Implicit paragraph TABI** | Infer *unstated* gaps requiring discourse reasoning | Paragraph pi with future-direction sentences masked at end (212 manual), 3-shot examples provided | System: expert biomedical argumentation analyst; User: TASK paragraph masking + OUTPUT SCHEMA Claim/Grounds/Warrant/Bucket/Category/Justification + 3-shot illustrative examples (mouse→human, synthetic→real, conflicting cohorts) → strict JSON 1-3 candidates | Claim (implied gap), Grounds (quoted evidence spans), Warrant (single sentence Grounds→Claim), Bucket more vs least probable, Category 5 types | RoBERTa-large bi-directional entailment Claim vs Gold & Warrant vs Premises threshold 0.4; success if any candidate matches; Accuracy + bucket calibration log | GPT-5 84.43% (179), GPT-4o 80.66% (171), Llama-70B 77.89% (163), small models fail; 3-shot essential vs 0-shot vague; 10-24% correct bucketed least_probable → relevance vs technical limits |
| **P3 Full-text pilot** | Test holistic full-paper reasoning | Full manuscript Pi (text/tables/figures) multi-modal, 24 papers 19 domains | GPT-4o pilot prompt: identify 5-10 implicit gaps each with Evidence Spans + Warrant + Gap Category + Future Direction + Feasibility Notes + Bucket → JSON array | Pairs (Implied gap + Future direction) | Human author survey 18 corresponding authors agree/disagree + justification (irrelevance, misinterpretation, outdated) → % agreement factual 83.3%, open 56% +25.9%, impact 67%, validity 65%/35% invalid feasibility | GPT-4o effective for gap factuality but implementation feasibility harder (tech limits, budget) |
| **P4 Model comparison** | Benchmark scale vs openness | Same inputs across 7 models x2 settings (no limit vs 1K chunks) | Same prompts | Tables 3,4,5 + Figures Venn & spider | F1, Acc across categories | Scale helps; open-weight competitive; mixture-of-models recommended for recommender; FEW-SHOT matters more than scale for implicit |

## Prompt family comparison

| Prompt | Explicit vs Implicit | Shot | JSON schema | Grounding required | Threshold |
|---|---|---|---|---|---|
| Explicit zero-shot | Explicit | 0 | 4 keys | Statement exact from doc + support_sentence/s | ROUGE-L 0.55 |
| TABI 3-shot | Implicit paragraph | 3 | 6 keys Claim/Grounds/Warrant/Bucket/Category/Justification | Grounds quoted verbatim, Warrant 1 sentence | Entailment 0.4 |
| Full-paper pilot | Implicit doc | 0 long-context | 7 keys gap+evidence+warrant+cat+future+feasibility+bucket | Evidence spans with section ref | Author % |

## Data flow

```
CSV (ID, Excerpt)
  → df dropna + drop_duplicates Excerpt
  → for each file_id:
      → split_into_chunks_preserving_sentences (Stanza or regex) ≤1000 words
      → for each chunk: call_model (Responses API) → extract_json_array → validate → all_items.extend
      → dedupe_by_statement → save {file_id}.json
  → Evaluation:
      IPBES: ROUGE-L F1 one-to-one >0.55 → P,R,F1
      COVID: Accuracy filtered by ignorance cue dictionary + exclude general non-research → Venn overlap + spider category
  → Implicit:
      Manual 212 paras → 3-shot TABI → candidates → RoBERTa entail >0.4 → Accuracy + Bucket distribution
      Full-text 24 papers → GPT-4o full-manuscript prompt → 5-10 gaps + future directions → 18-author survey → agreement %

Failure path:
  exception in chunking → chunks=[excerpt] warning
  exception in model call → write {file_id}__ERROR.txt with repr(e)+Excerpt, sleep 1.5, continue
```

## Categories 5 (Boguslav overlay)

| Category | Example cue pattern | Explicit vs Implicit instance |
|---|---|---|
| Levels of Evidence | No RCT, unknown efficacy | Explicit lexical / Implicit missing link (mouse→human) |
| Barriers | not feasible, limitation | Explicit / Implicit lab/technical |
| Future Opportunities | further research needed | Explicit / Implicit generalization gap |
| Anomaly/Curious Findings | conflicting, contradictory | Explicit / Implicit conflicting findings without reconciliation |
| Research Aims | aim to investigate | Explicit / Implicit aim missing piece |

## Decision table for deployment

| Decision | Options | Recommendation from paper |
|---|---|---|
| Chunking | No limit vs 1K sentence-aligned | Use 1K chunking; safe, often improves recall for smaller models, preserves F1 within 0.02 |
| Model | GPT-5 vs Llama-70B vs mini | Prefer Llama-70B for coverage if cost sensitive; GPT-5 for max coverage + unique; mixture for recommender |
| Prompting for implicit | 0-shot vs 3-shot | Must use 3-shot TABI template; 0-shot degenerates |
| Human in loop | Auto vs HITL | Keep HITL for feasibility filtering; 35% proposed directions invalid due resource constraints |
| Evaluation | ROUGE only vs entailment+ROUGE | Use both: ROUGE for explicit, entailment for implicit with threshold 0.4 |

## Links to other systems

- GAPMAP explicit extraction → ResearchAgent's first step problem identification (target paper + references + entities)
- TABI Claim/Grounds/Warrant maps to Scientific Intelligence Survey Verifier types: self-critique (Warrant coherence) + tool-based (ROUGE/entailment) + HITL (author survey)
- Chunking strategy maps to Survey P2 Context-Augmented planners (handling long context)
