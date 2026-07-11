# Pre-writing vs Writing Stage in STORM

## Pre-writing stage (automated by STORM):
- Researching topic via effective question asking: perspective-guided question asking + simulated conversations grounded on Internet
- Discovering diverse perspectives by surveying existing articles from similar topics and using them to control question-asking process
- Simulating multi-turn conversations where answers to generated questions are grounded on Internet
- Creating outline based on LLM internal knowledge and collected information
- Figure2: Starting with given topic 1-2 identifies various perspectives on covering topic by surveying related Wikipedia articles, then simulates conversations between Wikipedia writer who asks questions guided by given perspective and expert grounded on trustworthy online sources 3-6, final outline curated based on LLM intrinsic knowledge and gathered conversations from different perspectives 7-8
- Direct prompting Ask 30 questions about given topic When was opening ceremony held? Where? How many countries? basic What When Where limited planning capacity Figure1A
- Perspective-Guided Question Asking: You are event planner who focuses on preparation of opening ceremony ... leads varied questions transportation arrangements budget cultural broadcasting security etc Figure1B
- Conversational Question Asking: Can you provide list participating countries... Diverse group over 90 countries entering stadium specific order How is order determined? transportation arrangements? budget? elicits follow-up in-depth questions iterative research grounded Internet Figure1C
- Output: Outline O plus references R

## Writing stage:
- Building upon references R collected outline O developed during prewriting stage full-length article composed section by section
- Section title headings subsections used retrieve relevant documents from R based semantic similarity calculated Sentence-BERT embeddings
- LLM then prompted generate section with citations
- Once all sections generated concatenated form full-length article
- LLM then prompted delete repeated information improve coherence polished article
- Furthermore in alignment Wikipedia stylistic norms LLM also utilized synthesize summary entire article forming lead section at beginning
- Titles to generate article section by section
- Implementation zero-shot prompting DSPy framework Khattab et al 2023 Appendix B pseudocode corresponding prompts Hyperparameters N M both set 5 Use chat model gpt-3.5-turbo for question asking and gpt-3.5-turbo-instruct for other parts Also experiment using gpt-4 for drafting and refining outline Figure2 For reported results simulated topic expert grounded on You.com search API compatible other search engines ground truth excluded

## Co-STORM extension:
- Collaborative discourse protocol turn management policy smooth collaboration among Co-STORM LLM experts generates answers grounded on external knowledge sources and/or raises follow-up questions based discourse history Moderator generates thought-provoking questions inspired by information discovered retriever but not directly used previous turns Question generation grounded Human user takes initiative either observe discourse gain deeper understanding topic or actively engage conversation injecting utterances steer discussion focus
- Dynamic updated mind map organize collected information hierarchical concept structure aiming build shared conceptual space between human user and system mind map proven help reduce mental load when discourse goes long in-depth
- Highly modular using dspy

## Comparison Table1:
Domain Scope Given Outline Given Refs
Balepur et al One One para / Yes
Qian et al All One para / No
Fan and Gardent One Full article Yes No
Liu et al All One para / Yes
Sauper and Barzilay Two Full article No No
Ours All Full article No No

Our setup All domains Full article No Given Outline No Given Refs emphasizes capability long-form grounded writing systems to research curate content Given topic t task find set references R and generate full-length article S s1 s2 ... sn where each sentence si cites list documents in R
