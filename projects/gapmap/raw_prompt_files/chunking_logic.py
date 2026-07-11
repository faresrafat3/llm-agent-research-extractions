# Chunking logic extracted from ex_gap_xtract.py
import re
try:
    import stanza
    _STANZA_AVAILABLE = True
except:
    _STANZA_AVAILABLE = False

def build_stanza_pipeline(lang="en"):
    return stanza.Pipeline(lang=lang, processors="tokenize", verbose=False) if _STANZA_AVAILABLE else None

def split_into_chunks_preserving_sentences(text, max_tokens=1000, lang="en"):
    # Stanza sentence token counts or regex fallback whitespace
    # Preserves sentence boundaries, isolates overly long sentences alone
    pass
