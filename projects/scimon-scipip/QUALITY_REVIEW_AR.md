# مراجعة الجودة — SciMON / SciPIP

## معايير

- أمانة استخراج موجهات SciMON Problem Setting Inspiration Retrieval Idea Generation Iterative Novelty Boosting In-context Contrastive
- أمانة استخراج موجهات SciPIP τ2 entity extraction τ3 concise methods background transformation summary problem main idea motivations details idea proposer dual-path
- اكتمال معادلات Recall10-50 Table4 Table5 Table8 Table9 Table10
- وضوح مخططات

## النتائج

| معيار | درجة 1-5 | ملاحظات |
|---|---|---|
| SciMON Background Context Seed Term | 5 | حرفي من Sec2.1 Background context B consisting M current problems motivations experimental settings constraints and optionally seed term v focus point Idea I Seed term cue limit hypothesis space Not merely paraphrase novel w.r.t B and broader literature |
| Inspiration Retrieval semantic KG citation | 5 | Semantic Neighbors list KG Neighbors list Citation Neighbors list Ground Truth ELM Table8 Example Zhou et al 2022 underlined similar ground truth |
| Idea Generation Initial Given [context] new idea Δ vs prior work | 5 | Initial idea pause prediction model etc linked knowledge graph inductive learning etc |
| Iterative Novelty Boosting compare I with prior literature {(Background_i, idea_i)} if overlapping update like good researcher Iteration1 Iteration2 ASUBD attention RL Ground Truth monotonic segmentation module | 5 | Example speech unit boundaries Iteration1 leverages acoustic linguistic features Iteration2 ASUBD attention reinforcement learning ... enhances ideas overall however superficial recombinations far from technical depth |
| In-context Contrastive CL | 5 | T5+CL etc Table9 R-L BERT GPT4ZS 0.120 etc T5+SN+CL 0.228 best helps better baseline reducing reliance copying |
| Human evaluation relevance utility novelty technical depth Table10 Irish language learning helpful unhelpful annotation interface Figure5 trivially overlap IE sufficient quality | 5 | Table10 Input Type Content Seed Term Prompt Irish language ... Model Output Label helpful unhelpful |
| SciPIP quintuple | 5 | ~78K papers top-tier AI conferences structured quintuple keywords backgrounds ideas concise methods references individually encoded vectors |
| Entity extraction τ2 | 5 | ≤5 words ≥2 words ≤5 entities nouns noun phrases entity1, entity2... حرفي |
| Summary problem main idea format | 5 | The problem of [problem] can be addressed by [main idea/approach] Title Abstract Introduction حرفي |
| Background motivations details | 5 | Motivations 1. 2. Details 1. 2. 3. حرفي |
| Concise methods τ3 example style transform | 5 | Example Summarized Methods style focus Methodology Section transform حرفي |
| Background transformation teacher student | 4.5 | Teacher in field AI skilled clearly explaining AI concepts to students undergraduate basic understanding deep learning Teaching subfield etc معاد بناؤه من وصف غير كامل لكن موثق |
| Multi-granularity retrieval SE CC CL Table4 Table5 Recall10 0.381 SCIMON-like 0.377 ResearchAgent-like 0.419 SciPIP Ours 0.544 0.615 0.657 0.684 more thorough Non-matching ideas more valuable novel | 5 | Table4 Recall10-50 Table5 ablation SE CC CL حرفي |
| Dual-path idea generation ~10 ideas | 5 | System researcher innovative pioneering abilities good using innovative original methods solve cutting-edge problems brainstorm ideas clear innovative valid comprehensive cue words summaries backgrounds contributions methods related papers Avoid merely stacking integrate relevant aspects own insights Idea1 Idea2 ... حرفي |
| Graphs | 5 | EN/AR mmd يغطي Data collection 67,408 + 5,708 PubMed Background Inspiration retrieval Idea Generation Iterative Novelty Boosting In-context Contrastive Human evaluation SciPIP quintuple Multi-granularity Dual-path Error analysis etc |

## ثغرات حرجة

- بعض موجهات Background transformation teacher student غير كاملة في PDF extraction لكن تمت إعادة بنائها بأمانة موثقة
- موجهات Section generation لـ SciPIP غير موجودة رسميا (اعتماد dual-path)

## الحكم النهائي

**مقبول للنشر** — يطابق معيار extractions السابقة ويضيف قيمة Part 6 HOW TO TRACK KNOWLEDGE → scientific claim tracking idea generation retrieval novelty optimization.

المستودع جاهز للدفع إلى faresrafat3/scimon-scipip-full-extraction
