# GAPMAP — English Logic Graph

Full Mermaid source: `graph_english.mmd`

## Overview diagram description

The system has two main experimental tracks (Explicit and Implicit) plus preprocessing.

1. **Preprocess**: CSV → dedupe Excerpts → chunk with Stanza sentence-aligned ≤1000 words (fallback regex) preserving coherence.

2. **Explicit zero-shot track**:
   - For each chunk → call LLM with System `Return ONLY valid JSON` + User `PROMPT_TEMPLATE` requiring Ignorance Statement (exact sentence), support_sentence/s, justification, Ignorance Cues.
   - Extract JSON via regex, strip fences and `<think>` tags, validate REQUIRED_KEYS.
   - Accumulate `all_items`, dedupe by squashed Ignorance Statement.
   - Save per ID JSON.
   - Evaluation IPBES: ROUGE-L F1 stemming one-to-one threshold 0.55 → P,R,F1.
   - Evaluation COVID: Filter non-research, validate against ignorance-cue dictionary (must contain ≥1 cue) → Accuracy + Venn overlap + spider category chart.

3. **Implicit TABI track**:
   - Paragraph-level manual 212 paras from 137 PubMed, future directions masked.
   - 3-shot prompt with examples (mouse→human translational gap, synthetic→real barrier, conflicting cohorts anomaly) → produce Claim, Grounds (quoted), Warrant (single sentence), Bucket (more vs least probable), Category (5 types).
   - Evaluation via RoBERTa-large bi-directional entailment threshold 0.4 for Claim vs Gold + Warrant vs Premises; success if any candidate matches.
   - Full-text pilot: 24 papers 19 domains → GPT-4o multi-modal long context → structured 5-10 gaps each with evidence spans, warrant, category, future direction, feasibility notes, bucket → survey 18 authors agree/disagree percentages.

4. **Model benchmarking**: 7 models (GPT-5, GPT-4o, mini, Gemma-9B, Llama 70B/17B MoE/8B) × 2 settings (no limit vs 1K chunks).

See Mermaid file for executable flowchart.
