# The Prompt Report — Research Summary

Paper: https://arxiv.org/abs/2406.06608
v6 Feb 2025 — Schulhoff et al. (UMD, OpenAI, Stanford, Microsoft, etc.)

## Contributions
- 33 vocabulary terms standardized
- Taxonomy of 58 LLM text prompting techniques
- 40 techniques for other modalities (multilingual, multimodal, agents, evaluation)
- PRISMA systematic review: 4,247 records screened → 1,565 relevant
- Best practices for SOTA LLMs incl. ChatGPT
- Meta-analysis of prefix-prompting literature
- Case studies: MMLU benchmarking + real-world suicide-risk signal detection (frantic hopelessness)

## 6 core text technique families
1. In-Context Learning (Few-Shot / Zero-Shot)
   - Exemplar selection: KNN, Vote-K
   - Exemplar generation: SG-ICL
   - Instruction selection: APE
   - Zero-Shot variants: Emotion, Role, Style, S2A, SimToM, RaR, RE2, Self-Ask
2. Thought Generation (CoT family)
   - Zero-Shot CoT, Analogical, Step-Back, ThoT, Tab-CoT
   - Few-Shot CoT: Auto-CoT, Active-Prompt, Complexity-Based, Contrastive, Memory-of-Thought, Uncertainty-Routed
3. Decomposition
   - Least-to-Most, Plan-and-Solve, DECOMP, Faithful CoT, Program-of-Thought, Tree-of-Thought, Recursion-of-Thought, Skeleton-of-Thought, Metacognitive
4. Ensembling
   - Self-Consistency, Universal Self-Consistency, DiVeRSe, COSP, DENSE, MoRE, USP, Meta-CoT, Prompt Paraphrasing
5. Self-Criticism
   - Self-Refine, Self-Verification, Chain-of-Verification, Self-Calibration, ReverseCoT, Cumulative Reasoning, Reflexion, ReAct
6. Answer / Prompt Engineering
   - Answer shape/space, verbalizer, extractor, answer trigger
   - APE, OPRO, Meta-Prompting, Promptbreeder

## Multilingual / Multimodal / Agents
- Translate-then-Reason, Cross-lingual CoT
- Multimodal CoT, Chain-of-Images, Image-as-Text, Negative Prompt, Segmentation Prompting (SAM)
- Agents: ReAct, Toolformer-style, Code-Generation Agents, MRKL
- Evaluation: LLM-as-a-Judge, G-Eval, Constitutional Critique
- Safety: Prompt Injection defenses, alignment, sycophancy mitigation

Prompting is shifting from scattered tricks → structured engineering discipline.
