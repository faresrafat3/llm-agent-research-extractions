"""
Entity retrieval logic from ResearchAgent PDF Sec 3, Eq (1)(2) and Appendix B.3

K in R^{m x m} sparse co-occurrence matrix
m = total unique entities
El = BLINK linker entities from title+abstract multiset

Eq1: Ret({l0..ln};K) = argmax_{I subset [m]:|I|=k} prod P(ei | E)
Eq2 approximation: argmax prod (prod_{ej in E} P(ej|ei)) * P(ei)
P(ej|ei), P(ei) from normalized K

Embedding alternative: cosine similarity in linker latent space highest similarity to entities in current literature
"""
import numpy as np
from collections import defaultdict, Counter

def build_K(papers_entities):
    """
    papers_entities: list of list of entities (multisets) from titles+abstracts
    Returns: dict of dict sparse + counts
    """
    co_counts = defaultdict(Counter)
    single_counts = Counter()
    for ents in papers_entities:
        uniq = set(ents)
        for e in ents:
            single_counts[e] += 1
        # all pairs C(|E|,2)
        uniq_list = list(uniq)
        for i in range(len(uniq_list)):
            for j in range(i+1, len(uniq_list)):
                ei, ej = uniq_list[i], uniq_list[j]
                co_counts[ei][ej] += 1
                co_counts[ej][ei] += 1
    return co_counts, single_counts

def retrieve_cooccurrence(E_current, K_co, K_single, k=20):
    """
    E_current: set/list entities from core+refs
    K_co: co-occurrence dict
    K_single: single counts
    Returns top-k external entities not in E_current
    Implements Eq2: score(ei) = P(ei) * prod_{ej in E} P(ej|ei)
    Approximated: P(ej|ei) = co_counts[ei][ej]/single_counts[ei] ; P(ei)=single_counts[ei]/sum(single)
    """
    total = sum(K_single.values()) or 1
    scores = {}
    E_set = set(E_current)
    vocab = set(K_single.keys()) - E_set
    for ei in vocab:
        p_ei = K_single[ei]/total
        # product in log space to avoid underflow
        log_score = np.log(p_ei+1e-9)
        for ej in E_current:
            # P(ej|ei) approx
            co = K_co.get(ei, {}).get(ej, 0)
            p_ej_given_ei = (co+1e-6)/(K_single[ei]+1e-6)  # smoothing
            log_score += np.log(p_ej_given_ei+1e-9)
        scores[ei] = log_score
    # top-k argmax
    sorted_entities = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:k]
    return [e for e,s in sorted_entities]

def retrieve_embedding(E_current, entity_embeddings, k=20):
    """
    Embedding-based alternative: highest similarity to entities in current literature
    entity_embeddings: dict entity -> vector
    Similarity calculated over latent space of linker
    """
    import numpy as np
    E_vecs = [entity_embeddings[e] for e in E_current if e in entity_embeddings]
    if not E_vecs:
        return []
    mean_current = np.mean(E_vecs, axis=0)
    scores = {}
    for e, vec in entity_embeddings.items():
        if e in set(E_current):
            continue
        # cosine similarity
        sim = np.dot(vec, mean_current) / (np.linalg.norm(vec)*np.linalg.norm(mean_current)+1e-9)
        scores[e] = sim
    sorted_e = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:k]
    return [e for e,s in sorted_e]
