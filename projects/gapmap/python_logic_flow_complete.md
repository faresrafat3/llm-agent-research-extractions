# GAPMAP — Python Logic Flow Complete

Audited: `ex_gap_xtract.py` + paper Sec 4-5

---

## 0. Entry point `ex_gap_xtract.py`

```python
csv_file_path = "path"
output_dir = "path"
MODEL_NAME = "gpt-5"   # reasoning model; Responses API
os.makedirs(output_dir, exist_ok=True)
df = pd.read_csv(csv_file_path)
df = df.dropna(subset=["Excerpt"])
df = df.drop_duplicates(subset=["Excerpt"]).reset_index(drop=True)

for _, row in df.iterrows():
    file_id = str(row["ID"]).strip()
    excerpt = str(row["Excerpt"]).strip()
    chunks = split_into_chunks_preserving_sentences(excerpt, max_tokens=1000, lang="en")
    all_items = []
    for i, chunk in enumerate(chunks):
        items = call_model(chunk)   # LLM call
        all_items.extend(items)
        time.sleep(1.5)
    all_items = dedupe_by_statement(all_items)
    out_path = os.path.join(output_dir, f"{file_id}.json")
    json.dump(all_items, f, ...)
    time.sleep(1.0)
```

---

## 1. Chunking logic

### Optional Stanza path

```
build_stanza_pipeline(lang="en") → stanza.Pipeline(tokenize)
stanza_sentence_tokens(text, nlp) → list[(sentence_text, token_count)] where token_count = sum(1 for _ in sent.words)
```

### Fallback regex

```
regex_sentence_split: re.split(r'(?<=[.!?])\s+(?=[A-Z"“(])', text)
merge short <5 char buffers
```

### split_into_chunks_preserving_sentences

```
Input: text, max_tokens=1000
If not text → []
If Stanza available: sents = stanza_sentence_tokens
Else: sents = regex split + whitespace token count

chunks, cur, cur_tokens = [], [],0
for s_text, s_tok in sents:
    if s_tok > max_tokens:   # overly long sentence isolated
        if cur: chunks.append(join cur)
        chunks.append(s_text)
        continue
    if cur_tokens + s_tok > max_tokens:
        chunks.append(join cur)
        cur=[s_text]; cur_tokens=s_tok
    else:
        cur.append(s_text); cur_tokens+=s_tok
if cur: append final

Returns list chunks ≤1000 tokens, sentence boundaries preserved
```

Used for COVID 8K+ sections + IPBES long paragraphs.

---

## 2. Model call `call_model(chunk)`

```python
def call_model(chunk: str):
    resp = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role":"system","content":"You are an expert scientific information extraction model. Return ONLY valid JSON."},
            {"role":"user","content": PROMPT_TEMPLATE.format(chunk=chunk)}
        ]
    )
    raw = resp.output_text
    json_text = extract_json_array(raw or "")
    data = json.loads(json_text)
    if not validate_payload(data): raise ValueError
    return data
```

- Uses OpenAI Responses API (o4-mini-2025-04-16 compatible per comment)
- Rate limiting 1.5s per chunk, 1.0s per file

---

## 3. JSON extraction + validation

```
def extract_json_array(text):
    cleaned = re.sub(r"```(?:json)?|```","",text, re.I)
    cleaned = re.sub(r"<think>.*?</think>","",cleaned, re.DOTALL|re.I)
    m = re.search(r"\[\s*(?:\{.*?\}\s*(?:,\s*\{.*?\}\s*)*)?\]", cleaned, re.DOTALL)
    return m.group(0) if m else cleaned

REQUIRED_KEYS = {"Ignorance Statement","support_sentence/s","justification","Ignorance Cues"}

def validate_payload(payload):
    if not isinstance(payload,list): False
    for obj in payload:
        if not isinstance(obj,dict): False
        if not REQUIRED_KEYS.issubset(obj.keys()): False
        if not isinstance(obj["Ignorance Statement"],str): False
        if not isinstance(obj["support_sentence/s"],list): False
        if not isinstance(obj["justification"],str): False
        if not isinstance(obj["Ignorance Cues"],list): False
    return True
```

Error handling: catch exception → write `{file_id}__ERROR.txt` with repr(e) + Excerpt, print Failed, sleep 1.5, continue loop.

---

## 4. Deduplication

```
def dedupe_by_statement(items):
    seen, out = set(), []
    for obj in items:
        key = re.sub(r"\s+"," ", obj.get("Ignorance Statement","").strip())
        if key and key not in seen:
            seen.add(key); out.append(obj)
    return out
```

- Whitespace-squashed exact match
- Applied after collecting all chunk results per document

---

## 5. Explicit evaluation (IPBES)

```
ROUGE-L F1 with stemming, one-to-one matching
Threshold 0.55
Pred counted TP if ROUGE-L F1 >0.55 vs gold
Unmatched predictions FP, unmatched gold FN
Precision, Recall, F1 aggregate
Exact string matches recorded for reference but not required
```

Logic: requires solving assignment (greedy one-to-one based on similarity score)

---

## 6. Explicit COVID evaluation (post-hoc)

```
Inputs: LLM predicted more candidates than single gold per section
Step1: Filter general non-research gaps (e.g., "SARS-CoV-2 has been declared a pandemic")
Step2: Validate predicted statements against ignorance-cues dictionary (Boguslav et al)
       Must contain at least one cue
Step3: Accuracy = proportion correctly identified gap statements (as defined by dictionary match)
Step4: Overlap analysis Venn, unique counts, normalized category performance spider (5 categories)
```

---

## 7. Implicit paragraph TABI evaluation

```
D_manual = {p1..pN} 212 paragraphs, each gold γ_i future direction
Per paragraph:
    Provide pi masked (future-direction sentences removed from end)
    LLM returns list candidates [{Claim, Grounds, Warrant, Bucket, Category}, ...]

Scoring:
    Use RoBERTa-large bi-directional entailment
    For each candidate:
        P_entail(Claim -> Gold) and P_entail(Gold -> Claim) > threshold? similarly Warrant vs Premises
    Threshold 0.4
    If any candidate matches → paragraph success
    Accuracy = success count / N
    Report Bucket distribution: fraction correct in more_probable vs least_probable (observed 10-24% least_probable are correct)
```

Critical factor prompting: 3-shot vs 0-shot: 0-shot → vague restatements → sharp drop accuracy → prompt design essential (template translates raw generative ability into precise future-direction predictions)

---

## 8. Full-text pilot (GPT-4o multi-modal)

```
For each full paper P_i (24 papers, 19 domains):
    Pass full-document to GPT-4o interface (handles PDF formats, long context)
    Generate structured pairs: (Implied gap + Suggested future direction) supported by textual evidence

Survey:
    18 corresponding authors of each paper reviewed model's gaps + directions
    Indicate agreed/disagreed + justification (irrelevance, misinterpretation, outdated issue)
    Metrics: factual true 83.3%, remain open 56% fully +25.9% partially, impact 67% of partials, implementation valid 65% / invalid 35% (tech limits, budget, relevance)
```

---

## 9. Model benchmarking matrix

```
Models tested:
- GPT-5
- gpt-4o
- GPT-4o mini
- Gemma-2-9B
- Llama-3.3-70B
- Llama-4-17B MoE
- Llama-3.1-8B

Settings:
- No context window limit
- 1000-word chunks (sentence-aligned)

Metrics per task:
- IPBES: P,R,F1 per model per setting (Table 3)
- COVID: Correct count + Acc (%) per model per setting, plus union All Models count 782/80.37% chunks, 730/75.03% no limit
- Implicit paragraph: FD Count + Acc % per model (Table 5)

Decision catalog:
- D1: Which dataset? IPBES vs COVID vs manual implicit vs full-text
- D2: Chunking? no limit vs 1K
- D3: Model size family? closed vs open, 8B vs 70B+ vs MoE
- D4: Explicit prompt zero-shot vs implicit 3-shot?
- D5: Evaluation threshold 0.55 ROUGE vs 0.4 entailment?
- D6: Dedupe by Ignorance Statement exact match?
- D7: Validation payload passes REQUIRED_KEYS?
- D8: Bucket assignment more vs least probable?
- D9: Filter general non-research gaps?
- D10: Cue dictionary contains at least one cue?
```

---

## 10. Loop inventory

| Loop | Bound | Location |
|---|---|---|
| df rows (documents) | N (286 IPBES, 1786 COVID) | ex_gap_xtract main |
| chunks per excerpt | len(excerpt)/1000 | split_into_chunks |
| items per chunk accumulation | all_items.extend | main |
| dedupe loop | len(all_items) | dedupe_by_statement |
| evaluation matching one-to-one ROUGE | predictions × gold | eval IPBES |
| implicit candidates per paragraph | 1-3 candidates | TABI generation |
| entailment scoring | | RoBERTa bi-directional |
| model benchmarking | 7 models ×2 settings | tables |
| author survey | 18 authors | full-text pilot |

---

## 11. I/O summary

| Stage | Input | Output |
|---|---|---|
| CSV load | csv_file_path with ID, Excerpt | df filtered deduped |
| Chunking | excerpt string | List chunks ≤1000 tokens |
| call_model | chunk | List JSON gaps {Ignorance Statement, support_sentence/s, justification, Cues} |
| dedupe | all_items list | deduped list by statement |
| save JSON | all_items deduped | {file_id}.json |
| IPBES eval | predictions + gold 657 statements | P,R,F1 |
| COVID eval | predictions + gold + cue dictionary | Correct, Acc, Venn overlaps unique/shared counts |
| TABI implicit | masked paragraph pi | Claim/ Grounds/ Warrant/ Bucket candidates |
| entailment eval | predicted vs gold | Accuracy + Bucket distribution |
| full-text pilot | full paper Pi | 5-10 gaps + future directions + author agreement % |

---

## 12. Key decisions preserved

- Sentence-aligned chunking preserves coherence, safe fallback to regex if Stanza not available
- Strict JSON schema forces model to quote exact sentence for traceability
- support_sentence/s array allows premise tracking
- Ignorance Cues extraction enables post-hoc dictionary validation
- 3-shot essential for implicit to avoid vague speculation
- Bucket binary gives calibration signal about central vs peripheral gap
- Warrant single sentence makes entailment sanity check possible
