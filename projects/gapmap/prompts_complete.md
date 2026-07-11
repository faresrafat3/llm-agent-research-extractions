# GAPMAP — Complete Prompt Extraction

Source truth: `scripts/ex_gap_xtract.py` (official repo) + paper sections 4.3.1, 4.3.2 + README + Figures

Audited commit: `b0145b4`

---

## 1. Explicit Gap Extraction Prompts (official code)

### 1.1 System prompt (Responses API)

```text
You are an expert scientific information extraction model. Return ONLY valid JSON.
```

Location: `client.responses.create` system role

### 1.2 User prompt template PROMPT_TEMPLATE

```text
You are an expert scientific information extraction model.

TASK
Extract every “scientific knowledge gap” from the document below. A scientific knowledge gap is an explicit uncertainty, limitation, missing evidence, contradiction, or untested area stated by the authors.

GUIDELINES
- Use only the provided document.
- For the "Statement" field, return the exact sentence from the text that reflects the gap.
- For "Ignorance Cues", list the specific cue words/phrases in the Statement that signal uncertainty.
- Use an array of strings for "support_sentence/s" (empty array if none are needed).

OUTPUT FORMAT (STRICT JSON; array of objects for each candidate sentence)
[
  {{
    "Ignorance Statement": "...",                // exact ignorance sentence from the doc
    "support_sentence/s": ["..."],              // premises sentences that allow for concluding the extraction
    "justification": "...",                    // brief reason the sentence is a gap, based on wording in the doc
    "Ignorance Cues": ["...", "..."]          // cue words/phrases from the Statement
  }}
]

DOCUMENT
<<<
{chunk}
>>>

Return only the JSON array. If no gaps are found, return [].
Use double quotes for all keys and strings. Do not include explanations or any text before or after the JSON.
```

Variables:
- `{chunk}` — ≤1000-word sentence-preserving chunk or full paragraph if short, from Stanza tokenization or regex fallback

Use: IPBES and COVID-19 explicit experiments, zero-shot

### 1.3 JSON extraction post-processing

```python
REQUIRED_KEYS = {"Ignorance Statement", "support_sentence/s", "justification", "Ignorance Cues"}

def extract_json_array(text: str) -> str:
    cleaned = re.sub(r"```(?:json)?|```", "", text, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"<think>.*?</think>", "", cleaned, flags=re.DOTALL | re.IGNORECASE).strip()
    m = re.search(r"\[\s*(?:\{.*?\}\s*(?:,\s*\{.*?\}\s*)*)?\]", cleaned, flags=re.DOTALL)
    return m.group(0) if m else cleaned

def validate_payload(payload):
    # list of dicts, each has REQUIRED_KEYS, types str/list
```

Validation: must be list, each dict contains required keys, correct types, else ValueError.

Deduplication: by whitespace-squashed `Ignorance Statement` exact match.

---

## 2. Implicit Gap — TABI (Toulmin-Abductive Bucketed Inference)

### 2.1 Conceptual definition (paper Sec 4.3.1)

> Let D_manual = {p1..pN} N expert-annotated paragraphs, each with one gold implicit gap γ_i referring to required future direction. Provide pi to model, masking statements of future directions claims at end of pi and ask model to identify:
> - Claim: implied gap
> - Grounds: evidence span(s) that support the Claim
> - Warrant: single sentence reasoning Grounds→Claim (coherence & entailment sanity check)
> - Bucket: binary classification model confidence (more_probable vs least_probable) — calibration check

### 2.2 Reconstructed 3-shot TABI prompt (from paper description + repo notes)

Paper states: **in-context 3-shot prompting** essential, template translates raw generative ability into precise future-direction predictions. Zero-shot degenerates.

**System:**

```text
You are an expert biomedical argumentation analyst. Infer implicit knowledge gaps using Toulmin structure.
You must produce interpretable abductive reasoning with evidence grounding.
```

**User (3-shot version):**

```text
TASK: Given a biomedical paragraph with future-direction sentences masked at end, infer the implicit knowledge gap.

OUTPUT SCHEMA — strict JSON object per candidate:
{
  "Claim": "The implied gap — what remains unknown / required future direction (one sentence, clear)",
  "Grounds": ["Evidence sentence 1 verbatim from paragraph", "Evidence sentence 2 verbatim"],
  "Warrant": "Single sentence that logically connects Grounds to Claim, explaining why gap follows",
  "Bucket": "more_probable | least_probable",
  "Category": "Levels of Evidence | Barriers | Future Opportunities | Anomaly/Curious Findings | Research Aims (choose one)",
  "Justification": "Brief why Bucket chosen"
}

RULES:
- Claim must be a defeasible abductive inference, not a copy of explicit cue.
- Grounds must be quoted spans from input paragraph.
- Warrant must be one sentence, generalizable reasoning pattern (e.g., "Mouse biomarker improvement does not guarantee human outcome if correlation poor").
- Bucket: more_probable if gap is central to paper's argument, least_probable if peripheral/speculative.
- Return JSON array of 1-3 candidates, ordered most probable first.

EXAMPLES (3-shot):

Example 1:
Paragraph: "Compound E improves biomarker F in mice. Biomarker F correlates poorly with clinical outcomes in humans."
Gold implicit gap: "It is unknown whether E improves patient outcomes."

Output:
[
  {
    "Claim": "It is unknown whether compound E improves patient outcomes in humans.",
    "Grounds": ["Compound E improves biomarker F in mice.", "Biomarker F correlates poorly with clinical outcomes in humans."],
    "Warrant": "If a surrogate marker fails to correlate with clinical endpoints, efficacy on surrogate does not imply clinical benefit.",
    "Bucket": "more_probable",
    "Category": "Levels of Evidence",
    "Justification": "Translational barrier central to paragraph"
  }
]

Example 2:
Paragraph: "We demonstrated 95% accuracy on synthetic dataset with 10K samples. Real-world clinical dataset has missing values, distribution shift, and only 200 labeled cases."
Output:
[
  {
    "Claim": "It is unknown whether model maintains accuracy on real-world clinical data with limited labels and shift.",
    "Grounds": ["We demonstrated 95% accuracy on synthetic dataset with 10K samples.", "Real-world clinical dataset has missing values, distribution shift, and only 200 labeled cases."],
    "Warrant": "Performance on idealized synthetic data does not transfer to noisy low-resource real data without validation.",
    "Bucket": "more_probable",
    "Category": "Barriers"
  }
]

Example 3:
Paragraph: "Study A reported significant benefit of X in European cohort (n=5000, p<0.001). Study B found no effect in East Asian cohort (n=3000, p=0.45). No reconciliation offered."
Output:
[
  {
    "Claim": "It is unknown why efficacy of X differs by population and what modifiers explain conflicting results.",
    "Grounds": ["Study A reported significant benefit of X in European cohort (n=5000, p<0.001).", "Study B found no effect in East Asian cohort (n=3000, p=0.45)."],
    "Warrant": "Conflicting findings across populations without mechanistic explanation indicate missing understanding of effect modifiers.",
    "Bucket": "more_probable",
    "Category": "Anomaly/Curious Findings"
  }
]

NOW YOUR TURN:

Paragraph (future directions masked):
<<<
{paragraph}
>>>

Return only valid JSON array (1-3 candidates). No extra text.
```

Use: paragraph-level manual implicit-gap dataset (212 paras). Model: tested GPT-5, GPT-4o, Llama etc. Success counting if any predicted claim matches gold via entailment >0.4.

### 2.3 Scoring detail for TABI

- Bi-directional entailment probability using RoBERTa-large (Cohen et al 2021 style)
- Compute P(entail Claim→Gold) and P(entail Gold→Claim) and similarly Warrant vs Premises? threshold 0.4
- Accuracy = validated pairs count / total
- Bucket distribution logged for calibration

### 2.4 Full-document pilot prompt (GPT-4o multi-modal)

Paper Sec 4.3.2: Each full paper passed to GPT-4o to generate structured outputs of pairs identifying (1) Implied knowledge gaps supported by textual evidence and (2) Suggested future direction.

**Reconstructed prompt:**

```text
SYSTEM: You are a senior scientific reviewer analyzing full manuscripts for unstated knowledge gaps and actionable future directions.

USER:
You will receive a full research manuscript (text, may include tables/figures). Task:

- Identify 5-10 implicit knowledge gaps: gaps NOT explicitly stated but inferrable from context (missing link, generalization limit, conflict).
- For each gap, provide:
  {
    "Implied Gap": "Declarative unknown",
    "Evidence Spans": ["Quote sentence/paragraph supporting inference with section reference", ...],
    "Warrant": "Single sentence reasoning why evidence implies gap",
    "Gap Category": "Levels of Evidence / Barriers / Future Opportunities / Anomaly / Research Aims",
    "Future Direction": "Concrete feasible next experiment/study to address gap",
    "Feasibility Notes": "Tech limits, budget, domain constraints",
    "Bucket": "more_probable vs least_probable (central vs peripheral)"
  }

Constraints:
- Use only manuscript evidence
- Avoid hallucinating references
- Ensure future direction is distinct from authors' stated future work if any, and testable
- Handle long context holistically

Input manuscript:
<<< 
{full_paper_text}
>>>

Return strict JSON array of gaps as defined. No preamble.
```

- Then separate survey sent to 18 corresponding authors: agreed/disagreed + justification (irrelevance, misinterpretation, outdated issue)

---

## 3. Chunking prompt-adjacent logic (not LLM but procedural)

### 3.1 Stanza segmentation

```python
stanza.Pipeline(lang=lang, processors="tokenize")
sentence_text, token_count = sum(1 for _ in sent.words)
```

### 3.2 Chunk building

```
chunks, cur, cur_tokens = [], [], 0
for s_text, s_tok in sents:
    if s_tok > max_tokens: # sentence alone
        if cur: chunks.append(...)
        chunks.append(s_text)
        continue
    if cur_tokens + s_tok > max_tokens:
        chunks.append(join cur)
        cur = [s_text]; cur_tokens = s_tok
    else: cur.append(s_text); cur_tokens+=s_tok
if cur: chunks.append(...)
```

max_tokens = 1000 words (approx Stanza tokens or whitespace fallback)

Preserves sentence boundaries.

---

## 4. Prompt wiring map

| Prompt | Task | Called from | Mode | Input |
|---|---|---|---|---|
| System expert extraction | Explicit | ex_gap_xtract call_model | zero-shot | chunk |
| PROMPT_TEMPLATE explicit | IPBES + COVID | call_model | JSON array per chunk | chunk ≤1000 words |
| TABI 3-shot | Implicit paragraph manual | manual experiment | 3-shot few-shot | paragraph with masked future |
| Full-paper pilot | Implicit full-text | GPT-4o interface experiment | zero-shot + long context | full manuscript |
| RoBERTa entailment | Implicit scoring | evaluation script | NLI scoring | Claim vs Gold, Warrant vs Premises |
| Knowledge cue dictionary filter | Explicit COVID extra | post-hoc validation | rule check | predicted statement must contain at least one cue from Boguslav et al ignorance dictionary |

---

## 5. Non-prompt strings

- Ignorance cue examples: "remains unknown", "No RCT", "further research is needed", "May lead to", "could cause", negation patterns
- Bucket values: "more_probable", "least_probable"
- Gap categories: Research Aim, Levels of Evidence, Anomaly/Curious Findings, Barriers, Future Opportunities
- ROUGE-L F1 threshold 0.55, entailment threshold 0.4
- JSON keys: Ignorance Statement, support_sentence/s, justification, Ignorance Cues, Claim, Grounds, Warrant, Bucket

---

## 6. Failure handling prompts (implicit)

When model output fails validation → write error file: `{file_id}__ERROR.txt` containing Error repr + Excerpt, sleep 1.5s rate limiting, continue.

```
 diag_path = os.path.join(output_dir, f"{file_id}__ERROR.txt")
 with open... write Error + Excerpt
```
