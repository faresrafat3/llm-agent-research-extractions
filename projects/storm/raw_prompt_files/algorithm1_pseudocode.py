# Algorithm 1: STORM pseudocode from paper Listing
# Input Topic t, maximum perspective N, maximum conversation round M
# Output Outline O, references R

def STORM(t, N=5, M=5):
    P0 = "basic fact writer focusing on broadly covering the basic facts about the topic"  # Constant
    R = []
    # Discover perspectives P.
    related_topics = gen_related_topics(t)  # GenRelatedTopicsPrompt
    tocs = []
    for related_t in related_topics:
        article = get_wiki_article(related_t)  # Wikipedia-API
        if article:
            tocs.append(extract_toc(article))
    P = gen_perspectives(t, tocs)  # GenPerspectivesPrompt
    P = [P0] + P[:N]
    # Simulate conversations.
    convos = []
    for p in P:
        convo_history = []
        for i in range(1, M+1):
            # Question asking.
            q = gen_qn(t, p, convo_history)  # GenQnPrompt
            convo_history.append(q)
            # Question answering.
            queries = gen_queries(t, q)  # GenQueriesPrompt
            sources = search_and_sift(queries)  # YouRM You.com search API search_top_k 10 ground truth excluded
            a = gen_ans(t, q, sources)  # GenAnswerPrompt
            convo_history.append(a)
            R.append(sources)
        convos.append(convo_history)
    # Create the outline.
    OD = direct_gen_outline(t)  # DirectGenOutlinePrompt
    O = refine_outline(t, OD, convos)  # RefineOutlinePrompt
    return O, R

# Hyperparameters N=5 M=5 both set as 5
# chat model gpt-3.5-turbo for question asking and gpt-3.5-turbo-instruct for other parts
# also experiment gpt-4 for drafting and refining outline Figure2
# simulated topic expert grounded on You.com search API https://documentation.you.com/api-reference/search compatible other search engines
# ground truth Wikipedia article excluded from search results
# Writing stage: Building upon references R collected outline O developed during prewriting stage full-length article composed section by section
# Section title headings subsections used retrieve relevant documents from R based semantic similarity calculated Sentence-BERT embeddings LLM then prompted generate section with citations
# Once all sections generated concatenated form full-length article LLM then prompted delete repeated information improve coherence
# Furthermore in alignment Wikipedia stylistic norms LLM also utilized synthesize summary entire article forming lead section at beginning
