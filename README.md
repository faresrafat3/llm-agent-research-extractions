<div align="center">

# 🧠 LLM Agent Research Extractions (The Definitive SOTA SDK)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Research_Grade_SDK-brightgreen.svg?style=for-the-badge)](#)

**The world's largest consolidated archive of LLM Agent Architectures.** 
We have surgically extracted the exact prompts, state-machine logic, execution flows, and evaluation metrics from **20 State-of-the-Art (SOTA)** AI research papers and unified them into a single, executable Python SDK.

</div>

---

## 🚀 The SDK (New for 2026)

This repository is no longer just a reading library. It is now a **Python SDK**. Instead of copy-pasting prompts from whitepapers, you can import the exact academic prompts directly into your pipeline.

```bash
# Install the SOTA Extractor SDK
pip install -e .
```

```python
from llm_agent_prompts import STORM, Reflexion, TreeOfThoughts

# 1. Use the Stanford STORM perspective-guided generation prompt
storm_prompt = STORM.get_genperspectivesprompt_prompt()

# 2. Use the exact Reflexion episodic memory prompt
reflexion_prompt = Reflexion.get_reflect_prompt()
```

## 📚 The 20-System Arsenal (Analyzed & Deconstructed)

We have dissected the following SOTA systems. Click on any folder to view the absolute raw material (System Prompts, Hyperparameters, Mermaid Graphs) extracted directly from the papers' source code.

### 🌳 Search & Reasoning (MCTS / Beam)
- **[LATS (Language Agent Tree Search)](./projects/lats/)**: MCTS + PRM integration.
- **[Tree of Thoughts (ToT)](./projects/tot/)**: Deliberate tree search.
- **[Chain-of-Thought](./projects/cot/)**: Reasoning elicitation baseline.

### 🔄 Reflection & Memory
- **[Reflexion](./projects/reflexion/)**: Verbal episodic memory and failure reflection.
- **[Self-Refine](./projects/self-refine/)**: Iterative critique and self-correction loops.
- **[Voyager](./projects/voyager/)**: Lifelong learning via procedural vector memory.

### 🗣️ Multi-Agent & Orchestration
- **[STORM](./projects/storm/)**: Perspective-guided question asking (Stanford).
- **[Meta-Prompting](./projects/meta-prompting/)**: Expert persona dispatching.
- **[CAMEL](./projects/camel/)**: Multi-Agent Role-Playing.
- **[AutoGen](./projects/autogen/)**: Conversational framework orchestration.

### 🛠️ Tooling & Scientific Discovery
- **[Toolformer](./projects/toolformer/)**: Language Models teaching themselves tools.
- **[ReAct](./projects/react/)**: Synergizing reasoning and acting.
- **[AI Scientist v2](./projects/ai-scientist-v2/)**: Automated peer review and crystallization.
- **[SciMON / SciPIP](./projects/scimon-scipip/)**: Scientific Idea Proposers.
- **[ResearchAgent](./projects/researchagent/)**: Iterative idea generation.

### 🎯 Prompt Optimization (Meta-Learning)
- **[OPRO](./projects/opro/)**: Optimization by Prompting.
- **[APE](./projects/ape/)**: Automatic Prompt Engineering.
- **[The Prompt Report](./projects/prompt-report/)**: Systematic survey of 58 techniques.

## 🧠 Why This Matters (The Engineering Edge)
Most AI platforms rely on black-box wrappers like LangChain. By extracting the **raw logic and prompts** from these papers, we allow AI Architects to build highly deterministic, cost-aware *Neuro-Symbolic State Machines* (like [ARSENAL](https://github.com/faresrafat3/arsenal-unified-master-pipeline)) without the overhead of generic frameworks.

---
<div align="center">
  <em>Extracted with precision — from Cairo to the open web.</em>
</div>
