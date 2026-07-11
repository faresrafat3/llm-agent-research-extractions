# pip install stanza  # (uncomment and run once if you want Stanza splitting)
import os, re, json, time, pandas as pd
from openai import OpenAI
try:
    import stanza
    _STANZA_AVAILABLE = True
except Exception:
    _STANZA_AVAILABLE = False

def build_stanza_pipeline(lang="en"):
    try:
        return stanza.Pipeline(lang=lang, processors="tokenize", tokenize_pretokenized=False, verbose=False)
    except Exception:
        stanza.download(lang, processors="tokenize", verbose=False)
        return stanza.Pipeline(lang=lang, processors="tokenize", tokenize_pretokenized=False, verbose=False)

def regex_sentence_split(text: str):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z"“(])', text.strip())
    merged, buf = [], ""
    for p in parts:
        if not buf:
            buf = p
        else:
            if len(p) < 5:
                buf += " " + p
            else:
                merged.append(buf)
                buf = p
    if buf:
        merged.append(buf)
    return [s.strip() for s in merged if s.strip()]

def stanza_sentence_tokens(text: str, nlp):
    doc = nlp(text)
    results = []
    for sent in doc.sentences:
        s_text = sent.text.strip()
        t_count = sum(1 for _ in sent.words)
        if s_text:
            results.append((s_text, t_count))
    return results

def split_into_chunks_preserving_sentences(text: str, max_tokens: int = 1000, lang: str = "en"):
    if not text or not text.strip():
        return []
    if _STANZA_AVAILABLE:
        nlp = build_stanza_pipeline(lang=lang)
        sents = stanza_sentence_tokens(text, nlp)
    else:
        s_texts = regex_sentence_split(text)
        sents = [(s, len(s.split())) for s in s_texts]
    chunks, cur, cur_tokens = [], [], 0
    for s_text, s_tok in sents:
        if s_tok > max_tokens:
            if cur:
                chunks.append(" ".join(cur).strip())
                cur, cur_tokens = [], 0
            chunks.append(s_text)
            continue
        if cur_tokens + s_tok > max_tokens:
            if cur:
                chunks.append(" ".join(cur).strip())
            cur = [s_text]
            cur_tokens = s_tok
        else:
            cur.append(s_text)
            cur_tokens += s_tok
    if cur:
        chunks.append(" ".join(cur).strip())
    return chunks

csv_file_path = "path"
output_dir = "path"
MODEL_NAME = "gpt-5"
os.makedirs(output_dir, exist_ok=True)
os.environ["OPENAI_API_KEY"] = "XXXXX"
client = OpenAI()

df = pd.read_csv(csv_file_path)
df = df.dropna(subset=["Excerpt"])
df = df.drop_duplicates(subset=["Excerpt"]).reset_index(drop=True)

PROMPT_TEMPLATE = """You are an expert scientific information extraction model.

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
    "Ignorance Statement": "...",
    "support_sentence/s": ["..."],
    "justification": "...",
    "Ignorance Cues": ["...", "..."]
  }}
]

DOCUMENT
<<<
{chunk}
>>>

Return only the JSON array. If no gaps are found, return [].
Use double quotes for all keys and strings. Do not include explanations or any text before or after the JSON.
"""

REQUIRED_KEYS = {"Ignorance Statement", "support_sentence/s", "justification", "Ignorance Cues"}

def extract_json_array(text: str) -> str:
    cleaned = re.sub(r"```(?:json)?|```", "", text, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"<think>.*?</think>", "", cleaned, flags=re.DOTALL | re.IGNORECASE).strip()
    m = re.search(r"\[\s*(?:\{.*?\}\s*(?:,\s*\{.*?\}\s*)*)?\]", cleaned, flags=re.DOTALL)
    return m.group(0) if m else cleaned

def validate_payload(payload):
    if not isinstance(payload, list):
        return False
    for obj in payload:
        if not isinstance(obj, dict):
            return False
        if not REQUIRED_KEYS.issubset(obj.keys()):
            return False
        if not isinstance(obj["Ignorance Statement"], str):
            return False
        if not isinstance(obj["support_sentence/s"], list):
            return False
        if not isinstance(obj["justification"], str):
            return False
        if not isinstance(obj["Ignorance Cues"], list):
            return False
    return True

def call_model(chunk: str):
    resp = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": "You are an expert scientific information extraction model. Return ONLY valid JSON."},
            {"role": "user", "content": PROMPT_TEMPLATE.format(chunk=chunk)}
        ]    )
    raw = resp.output_text
    json_text = extract_json_array(raw or "")
    data = json.loads(json_text)
    if not validate_payload(data):
        raise ValueError("Model returned JSON that failed validation against the required schema.")
    return data

def dedupe_by_statement(items):
    seen, out = set(), []
    for obj in items:
        key = re.sub(r"\s+", " ", obj.get("Ignorance Statement", "").strip())
        if key and key not in seen:
            seen.add(key)
            out.append(obj)
    return out

MAX_TOKENS_PER_CHUNK = 1000
STANZA_LANG = "en"

for _, row in df.iterrows():
    file_id = str(row["ID"]).strip()
    excerpt = str(row["Excerpt"]).strip()
    print(f"Processing: {file_id}")
    try:
        chunks = split_into_chunks_preserving_sentences(
            excerpt, max_tokens=MAX_TOKENS_PER_CHUNK, lang=STANZA_LANG
        )
    except Exception as e:
        chunks = [excerpt]
        print(f"Warning: sentence chunking failed for {file_id}: {e}")
    all_items = []
    try:
        for i, chunk in enumerate(chunks):
            print(f"  Chunk {i+1}/{len(chunks)} (approx ≤ {MAX_TOKENS_PER_CHUNK} tokens)")
            items = call_model(chunk)
            all_items.extend(items)
            time.sleep(1.5)
        all_items = dedupe_by_statement(all_items)
    except Exception as e:
        diag_path = os.path.join(output_dir, f"{file_id}__ERROR.txt")
        with open(diag_path, "w", encoding="utf-8") as f:
            f.write(f"Error: {repr(e)}\n\nExcerpt:\n{excerpt}\n")
        print(f"Failed: {file_id} ({e})")
        time.sleep(1.5)
        continue
    out_path = os.path.join(output_dir, f"{file_id}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)
    print(f"Saved: {file_id}.json")
    time.sleep(1.0)

print("All outputs saved.")
