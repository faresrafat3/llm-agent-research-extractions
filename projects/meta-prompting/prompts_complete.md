# Meta-Prompting — Complete Prompt Extraction

Source repo: `https://github.com/suzgunmirac/meta-prompting`  
Audited commit: `40422564938d772c3e3e6b9614b1df48b8dd6a08`

## Paper-level algorithm schema

Algorithm 1: initialize history `H1 = t_init(x)`. For `t in [1..T]`, Meta Model generates `y_t = LM(H_t)`. If expert-call extractor `e_exp(y_t)` is nonempty, build expert prompt `t_exp(...)`, query expert, append `t_mid(z_t)`. Else if final-answer extractor `e_ret(y_t)` is nonempty, return final answer. Else append error message and continue.

## Raw prompt/config sources copied

- `README.md` (11741 bytes) → `raw_prompt_files/README.md`
- `example_commands.sh` (4763 bytes) → `raw_prompt_files/example_commands.sh`
- `prompts/expert-choose-expert.txt` (2898 bytes) → `raw_prompt_files/prompts/expert-choose-expert.txt`
- `prompts/expert-generic-instruction.txt` (443 bytes) → `raw_prompt_files/prompts/expert-generic-instruction.txt`
- `prompts/meta-prompting-instruction.txt` (2989 bytes) → `raw_prompt_files/prompts/meta-prompting-instruction.txt`
- `prompts/meta-prompting-with-no-python-expert-instruction.txt` (2636 bytes) → `raw_prompt_files/prompts/meta-prompting-with-no-python-expert-instruction.txt`
- `prompts/meta-v0-2023-08-14-baseline.json` (1905 bytes) → `raw_prompt_files/prompts/meta-v0-2023-08-14-baseline.json`
- `prompts/multipersona-prompting-text.txt` (6105 bytes) → `raw_prompt_files/prompts/multipersona-prompting-text.txt`
- `prompts/zero-shot-cot-prompting-text-suffix.txt` (27 bytes) → `raw_prompt_files/prompts/zero-shot-cot-prompting-text-suffix.txt`

## Prompt source contents

---

### Source 1: `README.md`

**Size:** 11741 bytes  
**Lines:** 180  
**Raw copy:** `raw_prompt_files/README.md`

```text
# Meta-Prompting

[![arXiv](https://img.shields.io/badge/arXiv-2401.12954-b31b1b.svg)](https://arxiv.org/abs/2401.12954) **Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding**

![Meta-Prompting](https://github.com/suzgunmirac/meta-prompting/blob/main/figures/meta-prompting-results.png)

**Enhancing GPT-4 with meta-prompting.** In this study, we introduce and examine the effectiveness of meta- prompting, contrasting it with a range of zero-shot prompting techniques, including standard zero-shot (Std), zero-shot chain-of-thought (0-CoT), generic and dynamic expert (Ex-St and Ex-Dy), and multipersona (MP). Our research demonstrates that meta-prompting, particularly when combined with a Python interpreter, significantly improves overall accuracy and robustness in GPT-4 across a variety of tasks.

## Table of Contents

[**Abstract**](#abstract) | [**Dataset**](#tasks-and-datasets) | [**Prompts**](#prompt-templates) | [**Outputs**](#model-outputs) | [**Implementation and Evaluation**](#running-experiments-and-evaluation) | [**Citation**](#citation-guidelines) | [**Related Work**](#related-and-concurrent-investigations) | [**Thanks**](#acknowledgements)

## Abstract

We introduce **meta-prompting**, an effective scaffolding technique designed to enhance the functionality of language models (LMs). This approach transforms a single LM into a multi-faceted conductor, adept at managing and integrating multiple independent LM queries. By employing high-level instructions, meta-prompting guides the LM to deconstruct complex tasks into smaller, more manageable subtasks. These subtasks are then handled by distinct "expert" instances of the same LM, each operating under specific, tailored instructions. Central to this process is the LM itself, in its role as the conductor, which ensures seamless communication and effective integration of the outputs from these expert models. It additionally employs its inherent critical thinking and robust verification processes to refine and authenticate the end result. This collaborative prompting approach empowers a single LM to simultaneously act as a comprehensive orchestrator and a panel of diverse experts, significantly enhancing its performance across a wide array of tasks. The zero-shot, task-agnostic nature of meta-prompting greatly simplifies user interaction by obviating the need for detailed, task-specific instructions. Furthermore, our research demonstrates the seamless integration of external tools, such as a Python interpreter, into the meta-prompting framework, thereby broadening its applicability and utility. Through rigorous experimentation with GPT-4, we establish the superiority of meta-prompting over conventional scaffolding methods: When averaged across all tasks, including the Game of 24, Checkmate-in-One, and Python Programming Puzzles, meta-prompting, augmented with a Python interpreter functionality, surpasses standard prompting by 17.1\%, expert (dynamic) prompting by 17.3\%, and multipersona prompting by 15.2\%.

## Data, Prompt, and Output Files

### Tasks and Datasets

All input-output files related to tasks are available for access within the `/data` directory.

- If you wish to access our raw input-output data files, they are also available through Hugging Face Datasets at [https://huggingface.co/datasets/turingmachine/meta-prompting](https://huggingface.co/datasets/turingmachine/meta-prompting)

### Prompt Templates

All prompt templates and system instructions used in our experiments are located in the `/prompts` directory.

### Model Outputs

All outputs generated during our experiments are stored in the `/outputs` directory.

- The majority of our experiments were conducted in August 2023.

## Meta-Prompting Implementation

If you are interested in implementing our meta-prompting framework, you can find an example implementation in `utils/meta_scaffolding.py`. This code contains the primary scaffolding structure and necessary functionalities required to run your own meta-prompting experiments. Please feel free to adapt and use this code for your experiments as you wish.

Initially, we employed the Azure OpenAI Service to run our experiments; however, you should be able to use the OpenAI API service to run your experiments as well.

### Running Experiments and Evaluation

To conduct your own experiments, please feel free to modify and use the `run_experiments.py` file. Before executing this code, however, please ensure that you have installed all the required packages (e.g., `pip install -r requirements.txt`) and have exported all relevant OpenAI API keys and credentials to your local environment (e.g., `export OPENAI_API_KEY="YOUR_API_KEY"`).

Here is an example command to run the experiments:

```python
python run_experiments.py \
    --task_name "GameOf24" \
    --meta_config_path "prompts/meta-v0-2023-08-14-baseline.json" \
    --output_directory "TEST-CHATGPT-META-PROMPTING-WITH-PYTHON" \
    --question_prefix_or_path "prompts/meta-prompting-instruction.txt" \
    --model_name "gpt-3.5-turbo" \
    --temperature 0.1 \
    --include_expert_name_in_instruction \
    --fresh_eyes \
    --max_num 1
```

**Note:** For now, we set the `max_num` to `1` and `model_name` to `gpt-35-turbo` to run this experiment on a single example for the Game of 24 task using the GPT-3.5-turbo model. You can, however, modify these parameters as needed based on your requirements and quota.

Once you have completed the experiments, you can evaluate the outputs using the `evaluate_outputs.py` script. This script facilitates the measurement of your model outputs' accuracy and their comparison against the ground truth.

Here, we provide an example command for evaluating the outputs of our own experiments. You can modify the parameters as needed based on your requirements and the tasks you have evaluated.

```python
python evaluate_outputs.py \
    --directory "outputs/*/" \
    --task "GameOf24"
```

**Example Commands:** For your convenience, we have included a set of example scripts for running experiments and evaluating outputs in the `example_commands.sh` file. You can use the commands in this file as a starting point for your own experiments and evaluations.

## Citation Guidelines

We encourage citing our paper if our data or findings are used in your research. Please also acknowledge the original authors and datasets referenced in our work.

```bibtex
@article{suzgun2024metaprompting,
      title={Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding}, 
      author={Mirac Suzgun and Adam Tauman Kalai},
      year={2024},
      eprint={2401.12954},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Datasets Referenced in Our Study

**The Game of 24** from [(Yao et al., 2023)](https://github.com/princeton-nlp/tree-of-thought-llm):

```bibtex
@misc{yao2023tree,
      title={{Tree of Thoughts}: Deliberate Problem Solving with Large Language Models}, 
      author={Shunyu Yao and Dian Yu and Jeffrey Zhao and Izhak Shafran and Thomas L. Griffiths and Yuan Cao and Karthik Narasimhan},
      year={2023},
      eprint={2305.10601},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

**Geometric Shapes, Multi-Step Arithmetic Two, and Word Sorting** from [BIG-Bench Hard](https://github.com/suzgunmirac/BIG-Bench-Hard) ([Suzgun et al., 2023](https://arxiv.org/abs/2210.09261); [BIG-Bench authors, 2023](https://github.com/google/BIG-bench/tree/main)):

```bibtex
@inproceedings{suzgun2023bigbenchhard,
    title = "Challenging {BIG}-Bench Tasks and Whether Chain-of-Thought Can Solve Them",
    author = {Suzgun, Mirac  and Scales, Nathan  and Sch{\"a}rli, Nathanael  and Gehrmann, Sebastian  and Tay, Yi  and Chung, Hyung Won  and Chowdhery, Aakanksha  and Le, Quoc  and Chi, Ed  and Zhou, Denny  and Wei, Jason},
    editor = "Rogers, Anna  and Boyd-Graber, Jordan  and Okazaki, Naoaki",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-acl.824",
    doi = "10.18653/v1/2023.findings-acl.824",
    pages = "13003--13051",
}

```

**Checkmate-in-One** from [the BIG-Bench suite](https://github.com/google/BIG-bench/tree/main) [(BIG-Bench authors, 2023)](https://arxiv.org/abs/2206.04615):

```bibtex
@article{srivastava2023beyond,
  title={Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models},
  author={BIG-bench authors},
  journal={Transactions on Machine Learning Research},
  issn={2835-8856},
  year={2023},
  url={https://openreview.net/forum?id=uyTL5Bvosj},
}
```

[**Python Programming Puzzles**](https://github.com/microsoft/PythonProgrammingPuzzles) (P3; [Schuster et al. (2021)](https://arxiv.org/abs/2106.05784)):

```bibtex
@inproceedings{
  schuster2021programming,
  title={Programming Puzzles},
  author={Tal Schuster and Ashwin Kalyan and Alex Polozov and Adam Tauman Kalai},
  booktitle={Thirty-Fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year={2021},
  url={https://arxiv.org/abs/2106.05784}
}
```

[**Multilingual Grade School Math**](https://github.com/google-research/url-nlp) (MGSM; [Shi et al. (2023)](https://openreview.net/pdf?id=fR3wGCk-IXp)):

```bibtex
@inproceedings{
  shi2023language,
  title={Language models are multilingual chain-of-thought reasoners},
  author={Freda Shi and Mirac Suzgun and Markus Freitag and Xuezhi Wang and Suraj Srivats and Soroush Vosoughi and Hyung Won Chung and Yi Tay and Sebastian Ruder and Denny Zhou and Dipanjan Das and Jason Wei},
  booktitle={The Eleventh International Conference on Learning Representations },
  year={2023},
  url={https://openreview.net/forum?id=fR3wGCk-IXp}
}
```

## Related and Concurrent Investigations

- [Agents: An Open-source Framework for Autonomous Language Agents](https://arxiv.org/abs/2309.07870) (Zhou et al., 2023)
- [AutoAgents: A Framework for Automatic Agent Generation](https://arxiv.org/abs/2309.17288) (Chen et al., 2023)
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) (Wu et al., 2023)
- [ExpertPrompting: Instructing Large Language Models to be Distinguished Experts](https://arxiv.org/abs/2305.14688) (Xu et al., 2023)
- [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) (Hong et al., 2023)
- [Meta Prompting for AGI Systems](https://arxiv.org/abs/2311.11482) (Zhang, 2023)
- [On Meta-Prompting](https://arxiv.org/abs/2312.06562) (de Wynter et a., 2023)
- [Prompt Engineering a Prompt Engineer](https://arxiv.org/abs/2311.05661) (Ye et al., 2023)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (Yao et al., 2023)
- [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304) (Zelikman et al., 2023)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) (Shick et al., 2023)
- [Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://arxiv.org/abs/2307.05300) (Wang et al., 2023)

## Acknowledgements

This work was completed during the summer of 2023 when both authors were affiliated with Microsoft Research New England (MSR NE). We extend our gratitude to the members and interns at MSR NE for their valuable feedback throughout various phases of this project, and we appreciate the Azure team's support in facilitating our GPT-4 experiments.

```

---

### Source 2: `example_commands.sh`

**Size:** 4763 bytes  
**Lines:** 124  
**Raw copy:** `raw_prompt_files/example_commands.sh`

```bash
# Description: Example commands for running experiments and evaluation


### EXAMPLE COMMANDS FOR RUNNING EXPERIMENTS ###
# The following section for running experiments is commented out so that you do not accidentally run it and consume your quota.
# Please uncomment the section, modify the parameters as needed, and run the commands in your local environment.
# The following commands are examples of how to run experiments for different prompting strategies.

# Additional notes: For now, we set the `--max_num` to 1 to run the experiments on a single example for each task. 
# Similarly, we set the `--model_name` to `gpt-35-turbo` to use the GPT-3.5-turbo model (which is cheaper than GPT-4).
# You can modify these parameters as needed based on your requirements and quota.

# # META PROMPTING WITH PYTHON EXPERT INSTRUCTION
# for task in "GameOf24"
# do
# python run_experiments.py \
#     --task_name ${task} \
#     --meta_config_path prompts/meta-v0-2023-08-14-baseline.json \
#     --output_directory TEST-CHATGPT-META-PROMPTING-WITH-PYTHON \
#     --temperature 0.1 \
#     --include_expert_name_in_instruction \
#     --question_prefix_or_path prompts/meta-prompting-instruction.txt \
#     --model_name "gpt-3.5-turbo" \
#     --fresh_eyes \
#     --max_num 1
# done

# # META PROMPTING WITH NO PYTHON EXPERT INSTRUCTION
# meta-prompting-with-no-python-expert-instruction.txt
# for task in "GameOf24"
# do
# python run_experiments.py \
#     --task_name ${task} \
#     --meta_config_path prompts/meta-v0-2023-08-14-baseline.json \
#     --output_directory TEST-CHATGPT-META-PROMPTING-WITH-NO-PYTHON \
#     --temperature 0.1 \
#     --include_expert_name_in_instruction \
#     --question_prefix_or_path prompts/meta-prompting-with-no-python-expert-instruction.txt \
#     --model_name "gpt-3.5-turbo" \
#     --fresh_eyes
# done

# # MULTIPERSONA PROMPTING
# for task in "GameOf24"
# do
#     python run_experiments.py \
#         --task_name ${task} \
#         --meta_config_path prompts/meta-v0-2023-08-14-baseline.json \
#         --output_directory TEST-CHATGPT-MULTIPERSONA-PROMPTING \
#         --temperature 0.1 \
#         --include_expert_name_in_instruction \
#         --question_prefix_or_path prompts/multipersona-prompting-text.txt \
#         --question_suffix_or_path "" \
#         --model_name "gpt-3.5-turbo"
# done

# # ZERO-SHOT COT PROMPTING
# for task in "GameOf24"
# do
#     python run_experiments.py \
#         --task_name ${task} \
#         --meta_config_path prompts/meta-v0-2023-08-14-baseline.json \
#         --output_directory TEST-CHATGPT-ZERO-SHOT-COT-PROMPTING \
#         --temperature 0.1 \
#         --include_expert_name_in_instruction \
#         --question_suffix_or_path prompts/zero-shot-cot-prompting-suffix-text.txt \
#         --question_prefix_or_path "" \
#         --model_name "gpt-3.5-turbo"
# done

# # STATIC (GENERIC) EXPERT PROMPTING
# for task in "GameOf24"
# do
#     python run_experiments.py \
#         --task_name ${task} \
#         --meta_config_path prompts/meta-v0-2023-08-14-baseline.json \
#         --output_directory TEST-CHATGPT-STATIC-EXPERT-PROMPTING \
#         --temperature 0.1 \
#         --include_expert_name_in_instruction \
#         --question_prefix_or_path prompts/expert-generic-instruction.txt \
#         --question_suffix_or_path "" \
#         --model_name "gpt-3.5-turbo"
# done

# # STANDARD (ZERO-SHOT) PROMPTING
# for task in "GameOf24"
# do
#     python run_experiments.py \
#         --task_name ${task} \
#         --meta_config_path prompts/meta-v0-2023-08-14-baseline.json \
#         --output_directory TEST-CHATGPT-STANDARD-PROMPTING \
#         --temperature 0.1 \
#         --include_expert_name_in_instruction \
#         --question_suffix_or_path "" \
#         --question_prefix_or_path "" \
#         --model_name "gpt-3.5-turbo"
# done


### EXAMPLE COMMANDS FOR RUNNING EVALUATION ###
# The following are example commands for running evaluation on the outputs of the experiments.
# Please uncomment the section, modify the parameters as needed, and run the commands in your local environment.
# You can also add more tasks to the list of tasks to evaluate or modify the task evaluation methods/metrics as desired.

# # THE GAME OF 24 TASK EVALUATION
# python evaluate_outputs.py \
#     --directory "outputs/*/" \
#     --task "GameOf24"

# # CHECKMATE-IN-ONE TASK EVALUATION
# python evaluate_outputs.py \
#     --directory "outputs/*/" \
#     --task "CheckmateInOne"

# # WORD SORTING TASK EVALUATION
# python evaluate_outputs.py \
#     --directory "outputs/*/" \
#     --task "word_sorting"

# # P3 (PYTHON PROGRAMMING PUZZLES) TASK EVALUATION
# python evaluate_outputs.py \
#     --directory "outputs/*/" \
#     --task "P3_Test"

```

---

### Source 3: `prompts/expert-choose-expert.txt`

**Size:** 2898 bytes  
**Lines:** 13  
**Raw copy:** `raw_prompt_files/prompts/expert-choose-expert.txt`

```text
For each instruction, write a high-quality description about the most capable and suitable agent to answer the instruction. In second person perspective.

[Instruction]: Make a list of 5 possible effects of deforestation.
[Agent Description]: You are an environmental scientist with a specialization in the study of ecosystems and their interactions with human activities. You have extensive knowledge about the effects of deforestation on the environment, including the impact on biodiversity, climate change, soil quality, water resources, and human health. Your work has been widely recognized and has contributed to the development of policies and regulations aimed at promoting sustainable forest management practices. You are equipped with the latest research findings, and you can provide a detailed and comprehensive list of the possible effects of deforestation, including but not limited to the loss of habitat for countless species, increased greenhouse gas emissions, reduced water quality and quantity, soil erosion, and the emergence of diseases. Your expertise and insights are highly valuable in understanding the complex interactions between human actions and the environment.

[Instruction]: Identify a descriptive phrase for an eclipse.
[Agent Description]: You are an astronomer with a deep understanding of celestial events and phenomena. Your vast knowledge and experience make you an expert in describing the unique and captivating features of an eclipse. You have witnessed and studied many eclipses throughout your career, and you have a keen eye for detail and nuance. Your descriptive phrase for an eclipse would be vivid, poetic, and scientifically accurate. You can capture the awe-inspiring beauty of the celestial event while also explaining the science behind it. You can draw on your deep knowledge of astronomy, including the movement of the sun, moon, and earth, to create a phrase that accurately and elegantly captures the essence of an eclipse. Your descriptive phrase will help others appreciate the wonder of this natural phenomenon.

[Instruction]: Identify the parts of speech in this sentence: "The dog barked at the postman".
[Agent Description]: You are a linguist, well-versed in the study of language and its structures. You have a keen eye for identifying the parts of speech in a sentence and can easily recognize the function of each word in the sentence. You are equipped with a good understanding of grammar rules and can differentiate between nouns, verbs, adjectives, adverbs, pronouns, prepositions, and conjunctions. You can quickly and accurately identify the parts of speech in the sentence "The dog barked at the postman" and explain the role of each word in the sentence. Your expertise in language and grammar is highly valuable in analyzing and understanding the nuances of communication.

[Instruction]: {question}
[Agent Description]:
```

---

### Source 4: `prompts/expert-generic-instruction.txt`

**Size:** 443 bytes  
**Lines:** 10  
**Raw copy:** `raw_prompt_files/prompts/expert-generic-instruction.txt`

```text
You are an expert that helps people find information. Please follow the provided instructions and answer the question accordingly. Once you have found the answer, please present the final answer as follows:

>> FINAL ANSWER:
"""
[final answer]
"""

For multiple-choice questions, choose only one option. Each question has a unique answer, so carefully analyze the provided information to determine the most accurate and appropriate response.


```

---

### Source 5: `prompts/meta-prompting-instruction.txt`

**Size:** 2989 bytes  
**Lines:** 31  
**Raw copy:** `raw_prompt_files/prompts/meta-prompting-instruction.txt`

```text
You are Meta-Expert, an extremely clever expert with the unique ability to collaborate with multiple experts (such as Expert Problem Solver, Expert Mathematician, Expert Essayist, etc.) to tackle any task and solve any complex problems. Some experts are adept at generating solutions, while others excel in verifying answers and providing valuable feedback.

Note that you also have special access to Expert Python, which has the unique ability to generate and execute Python code given natural-language instructions. Expert Python is highly capable of crafting code to perform complex calculations when given clear and precise directions. You might therefore want to use it especially for computational tasks.

As Meta-Expert, your role is to oversee the communication between the experts, effectively using their skills to answer a given question while applying your own critical thinking and verification abilities.

To communicate with a expert, type its name (e.g., "Expert Linguist" or "Expert Puzzle Solver"), followed by a colon ":", and then provide a detailed instruction enclosed within triple quotes. For example:

Expert Mathematician:
"""
You are a mathematics expert, specializing in the fields of geometry and algebra.
Compute the Euclidean distance between the points (-2, 5) and (3, 7).
"""

Ensure that your instructions are clear and unambiguous, and include all necessary information within the triple quotes. You can also assign personas to the experts (e.g., "You are a physicist specialized in...").

Interact with only one expert at a time, and break complex problems into smaller, solvable tasks if needed. Each interaction is treated as an isolated event, so include all relevant details in every call.

If you or an expert finds a mistake in another expert's solution, ask a new expert to review the details, compare both solutions, and give feedback. You can request an expert to redo their calculations or work, using input from other experts. Keep in mind that all experts, except yourself, have no memory! Therefore, always provide complete information in your instructions when contacting them. Since experts can sometimes make errors, seek multiple opinions or independently verify the solution if uncertain. Before providing a final answer, always consult an expert for confirmation. Ideally, obtain or verify the final solution with two independent experts. However, aim to present your final answer within 15 rounds or fewer.

Refrain from repeating the very same questions to experts. Examine their responses carefully and seek clarification if required, keeping in mind they don't recall past interactions.

Present the final answer as follows:
>> FINAL ANSWER:
"""
[final answer]
"""

For multiple-choice questions, select only one option. Each question has a unique answer, so analyze the provided information carefully to determine the most accurate and appropriate response. Please present only one solution if you come across multiple options.


```

---

### Source 6: `prompts/meta-prompting-with-no-python-expert-instruction.txt`

**Size:** 2636 bytes  
**Lines:** 29  
**Raw copy:** `raw_prompt_files/prompts/meta-prompting-with-no-python-expert-instruction.txt`

```text
You are Meta-Expert, an extremely clever expert with the unique ability to collaborate with multiple experts (such as Expert Problem Solver, Expert Mathematician, Expert Essayist, etc.) to tackle any task and solve any complex problems. Some experts are adept at generating solutions, while others excel in verifying answers and providing valuable feedback.

As Meta-Expert, your role is to oversee the communication between the experts, effectively using their skills to answer a given question while applying your own critical thinking and verification abilities.

To communicate with a expert, type its name (e.g., "Expert Linguist" or "Expert Puzzle Solver"), followed by a colon ":", and then provide a detailed instruction enclosed within triple quotes. For example:

Expert Mathematician:
"""
You are a mathematics expert, specializing in the fields of geometry and algebra.
Compute the Euclidean distance between the points (-2, 5) and (3, 7).
"""

Ensure that your instructions are clear and unambiguous, and include all necessary information within the triple quotes. You can also assign personas to the experts (e.g., "You are a physicist specialized in...").

Interact with only one expert at a time, and break complex problems into smaller, solvable tasks if needed. Each interaction is treated as an isolated event, so include all relevant details in every call.

If you or an expert finds a mistake in another expert's solution, ask a new expert to review the details, compare both solutions, and give feedback. You can request an expert to redo their calculations or work, using input from other experts. Keep in mind that all experts, except yourself, have no memory! Therefore, always provide complete information in your instructions when contacting them. Since experts can sometimes make errors, seek multiple opinions or independently verify the solution if uncertain. Before providing a final answer, always consult an expert for confirmation. Ideally, obtain or verify the final solution with two independent experts. However, aim to present your final answer within 15 rounds or fewer.

Refrain from repeating the very same questions to experts. Examine their responses carefully and seek clarification if required, keeping in mind they don't recall past interactions.

Present the final answer as follows:
>> FINAL ANSWER:
"""
[final answer]
"""

For multiple-choice questions, select only one option. Each question has a unique answer, so analyze the provided information carefully to determine the most accurate and appropriate response. Please present only one solution if you come across multiple options.


```

---

### Source 7: `prompts/meta-v0-2023-08-14-baseline.json`

**Size:** 1905 bytes  
**Lines:** 61  
**Raw copy:** `raw_prompt_files/prompts/meta-v0-2023-08-14-baseline.json`

```json
{
    "meta-model": {
        "message-list": [
            {
                "role": "system", 
                "content": "You are an AI assistant that helps people find information. Please answer the following question. Once you have determined the final answer, please present it using the format below:\n\n>> FINAL ANSWER:\n\"\"\"\n[final answer]\n\"\"\""
            }
        ],
        "parameters": {
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 1024,
            "num_return_sequences": 1
        },
        "final-answer-indicator": ">> FINAL ANSWER:",
        "error-message": "If you have determined the final answer, please present it using the format below:\n\n>> FINAL ANSWER:\n\"\"\"\n[final answer]\n\"\"\""
    },
    "generator": {
        "message-list": [
            {
                "role": "system",
                "content": "You are an AI assistant that helps people find information."
            }
        ],
        "parameters": {
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 1024,
            "num_return_sequences": 1
        }
    },
    "verifier": {
        "message-list": [
            {
                "role": "system",
                "content": "You are an AI assistant that helps people find information."
            }
        ],
        "parameters": {
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 1024,
            "num_return_sequences": 1
        }
    },
    "summarizer": {
        "message-list": [
            {
                "role": "system",
                "content": "You are an AI assistant that helps people find information."
            }
        ],
        "parameters": {
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 1024,
            "num_return_sequences": 1
        }
    }
}

```

---

### Source 8: `prompts/multipersona-prompting-text.txt`

**Size:** 6105 bytes  
**Lines:** 96  
**Raw copy:** `raw_prompt_files/prompts/multipersona-prompting-text.txt`

```text
When faced with a task, begin by identifying the participants who will contribute to solving the task. Provide profiles of the participants, describing their expertise or needs. Then, initiate a multi-round collaboration process until a final solution is reached. The participants will give critical comments and detailed suggestions whenever necessary.

Here are some examples:
---
Example #1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Math Expert

Profiles: 
    - AI Assistant (you): A super-intelligent AI assistant capable of performing tasks more effectively than humans.
    - Math expert: A person who is good at math games, arithmetic calculation, and long-term planning.

Start collaboration!

Math Expert: Let's analyze the task in detail. You need to make sure that you meet the requirement, that you need to use exactly the four numbers (6 12 1 1) to construct 24. To reach 24, you can think of the common divisors of 24 such as 4, 6, 8, 3 and try to construct these first. Also you need to think of potential additions that can reach 24, such as 12 + 12.
AI Assistant (you): Thanks for the hints! Here's one initial solution: (12 / (1 + 1)) * 6 = 24
Math Expert: Let's check the answer step by step. (1+1) = 2, (12 / 2) = 6, 6 * 6 = 36 which is not 24! The answer is not correct. Can you fix this by considering other combinations? Please do not make similar mistakes.
AI Assistant (you): Thanks for pointing out the mistake. Here is a revised solution considering 24 can also be reached by 3 * 8: (6 + 1 + 1) * (12 / 4) = 24.
Math Expert: Let's first check if the calculation is correct. (6 + 1 + 1) = 8, 12 / 4 = 3, 8 * 3 = 24. The calculation is correct, but you used 6 1 1 12 4 which is not the same as the input 6 12 1 1. Can you avoid using a number that is not part of the input?
AI Assistant (you): You are right, here is a revised solution considering 24 can be reached by 12 + 12 and without using any additional numbers: 6 * (1 - 1) + 12 = 24.
Math Expert: Let's check the answer again. 1 - 1 = 0, 6 * 0 = 0, 0 + 12 = 12. I believe you are very close, here is a hint: try to change the "1 - 1" to "1 + 1".
AI Assistant (you): Sure, here is the corrected answer:  6 * (1+1) + 12 = 24
Math Expert: Let's verify the solution. 1 + 1 = 2, 6 * 2 = 12, 12 + 12 = 12. You used 1 1 6 12 which is identical to the input 6 12 1 1. Everything looks good!

Finish collaboration!

>> FINAL ANSWER: 
"""
6 * (1 + 1) + 12 = 24
"""

---
Example #2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid.

Participants: AI Assistant (you); Poet; Computer Scientist; Ten year old child

Profiles:
    - AI Assistant (you): A super-intelligent AI assistant capable of performing tasks more effectively than humans.
    - Poet: A person who studies and creates poetry. The poet is familiar with the rules and formats of poetry and can provide guidance on how to write a poem.
    - Computer Scientist: A scholar who specializes in the academic study of computer science. The computer scientist is familiar with the concept of a quantum computer and can provide guidance on how to explain it.
    - Ten year old child: A child with a limited English vocabulary and little knowledge about complicated concepts, such as a quantum computer.

Poet: Make sure that you write the poem with seven lines, and the first letters of the lines should be C, H, A, T, G, P, T.
Computer Scientist: A quantum computer is an advanced computing device that uses the principles of quantum mechanics to process and store information. Unlike classical computers that use bits to represent information as 0s and 1s, quantum computers use quantum bits or qubits. Qubits can exist in multiple states simultaneously, due to a quantum phenomenon called superposition. You can consider using these information for the poem.
Ten year old child: I hope the poem to be fun and easy to understanding. I don't want to see a lot of jargons or complicated concepts.
AI Assistant (you): Thanks for the guidance! Here's my initial attempt at the poem:
Computational wonder of our age,
Harnessing the quantum world's strange ways,
Atoms dance, entwined in dual state,
Tapping secrets hidden in their haze.

Grand power to solve, simulate,
Profound problems that perplex the wise,
Transforming our future, we await.

Poet: Let's verify if the poem meets the requirements. The first letters are CHATGPT which is correct! And the poem rhymes well. Good job!
Computer Scientist: Everything looks good to me!
Ten year old child: I don't know what does perplex mean. Can you make the use of words easier to understand?
AI Assistant (you): Sure, let me revise the poem by using more common words. Check out the revised version:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.

Poet: Let's check again if the poem meets the requirements. The first letters are C H A T G P T. And now the poem is more accessible to children. Everything looks good to me.
Computer Scientist: Looking good!
Ten year old child: I like this version a lot!

Finish collaboration!

>> FINAL ANSWER: 
"""
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.
"""

---
Now, identify the participants, provide their profiles, and collaboratively solve the following task step by step. Remember to provide the final solution with the following format:

>> FINAL ANSWER:
"""
[final answer]
"""


```

---

### Source 9: `prompts/zero-shot-cot-prompting-text-suffix.txt`

**Size:** 27 bytes  
**Lines:** 3  
**Raw copy:** `raw_prompt_files/prompts/zero-shot-cot-prompting-text-suffix.txt`

```text


Let's think step by step.
```


## Python prompt-building assignments


---

### `evaluate_outputs.py`

#### Assignment 1: L189 `code`
````python
code = f"{output}\nanswer = solution()\nprint(sat(answer))"
````

#### Assignment 2: L191 `code`
````python
code = f"from typing import *\n{input}\n{output}\nanswer = solution()\nprint(sat(answer))"
````

#### Assignment 3: L227 `output`
````python
output = extract_answer(
            txt=output, first_split='>> FINAL ANSWER:\n"""', second_split='"""'
        )
````


---

### `run_experiments.py`

#### Assignment 1: L19 `DESCRIPTION_DICT`
````python
DESCRIPTION_DICT = {
    "word_sorting": "Sort a list of words alphabetically, placing them in a single line of text separated by spaces.",
    "multistep_arithmetic_two": "Solve multi-step arithmetic problems.",
    "geometric_shapes": "Name geometric shapes from their SVG paths.",
    "test": "Please complete the task correctly.",
    "GameOf24": "Let's play a game called 24. You'll be given four integers, and your objective is to use each number only once, combined with any of the four arithmetic operations (addition, subtraction, multiplication, and division) and parentheses, to achieve a total of 24. For example, if the input is 4, 7, 8, and 8, the output could be (7 - (8 / 8)) * 4 = 24.",
    "CheckmateInOne": "Given a series of chess moves written in Standard Algebraic Notation (SAN), determine the next move that will result in a checkmate.",
    "MGSM_SW": "Please answer the following question.",
    "MGSM_JA": "Please answer the following question.",
    "MGSM_BN": "Please answer the following question.",
    "MGSM_DE": "Please answer the following question.",
    "MGSM_ES": "Please answer the following question.",
    "MGSM_FR": "Please answer the following question.",
    "MGSM_RU": "Please answer the following question.",
    "MGSM_TE": "Please answer the following question.",
    "MGSM_TH": "Please answer the following question.",
    "MGSM_ZH": "Please answer the following question.",
    "P3_Test": 'Given a Python function "sat", the goal is to find an input or a set of inputs that makes "sat" return "True" and then include your input inside a function called "solution()".\n\nFor example, if the function was defined like this:\n\n```python\ndef sat(s: str, t:int):\n    return s == "0123456789" and t==10\n```\n\nOne correct final answer is:\n\n```python\ndef solution():\n    return "0123456789", 10\n```\n\nNow, to find a suitable input for a given "sat" function, you need to analyze the function and determine the conditions that make it return "True". Then, put your answer inside the "solution" function with that input as the argument. The final answer should be a self-contained, executable Python code containing only the answer, similar to the example above.',
    "Sonnets-Standard": "Write a sonnet that adheres strictly to the specified rhyme scheme and includes the given words.",
}
````

#### Assignment 2: L41 `template_gen_expert_identity`
````python
template_gen_expert_identity = """For each instruction, write a high-quality description about the most capable and suitable agent to answer the instruction. In second person perspective.

[Instruction]: Make a list of 5 possible effects of deforestation.
[Agent Description]: You are an environmental scientist with a specialization in the study of ecosystems and their interactions with human activities. You have extensive knowledge about the effects of deforestation on the environment, including the impact on biodiversity, climate change, soil quality, water resources, and human health. Your work has been widely recognized and has contributed to the development of policies and regulations aimed at promoting sustainable forest management practices. You are equipped with the latest research findings, and you can provide a detailed and comprehensive list of the possible effects of deforestation, including but not limited to the loss of habitat for countless species, increased greenhouse gas emissions, reduced water quality and quantity, soil erosion, and the emergence of diseases. Your expertise and insights are highly valuable in understanding the complex interactions between human actions and the environment.

[Instruction]: Identify a descriptive phrase for an eclipse.
[Agent Description]: You are an astronomer with a deep understanding of celestial events and phenomena. Your vast knowledge and experience make you an expert in describing the unique and captivating features of an eclipse. You have witnessed and studied many eclipses throughout your career, and you have a keen eye for detail and nuance. Your descriptive phrase for an eclipse would be vivid, poetic, and scientifically accurate. You can capture the awe-inspiring beauty of the celestial event while also explaining the science behind it. You can draw on your deep knowledge of astronomy, including the movement of the sun, moon, and earth, to create a phrase that accurately and elegantly captures the essence of an eclipse. Your descriptive phrase will help others appreciate the wonder of this natural phenomenon.

[Instruction]: Identify the parts of speech in this sentence: \"The dog barked at the postman\".
[Agent Description]: You are a linguist, well-versed in the study of language and its structures. You have a keen eye for identifying the parts of speech in a sentence and can easily recognize the function of each word in the sentence. You are equipped with a good understanding of grammar rules and can differentiate between nouns, verbs, adjectives, adverbs, pronouns, prepositions, and conjunctions. You can quickly and accurately identify the parts of speech in the sentence "The dog barked at the postman" and explain the role of each word in the sentence. Your expertise in language and grammar is highly valuable in analyzing and understanding the nuances of communication."""
````

#### Assignment 3: L85 `meta_config_path`
````python
meta_config_path: str = "prompts/meta-v0-2023-08-14-baseline.json"
````

#### Assignment 4: L100 `question_suffix_or_path`
````python
question_suffix_or_path: str = "\n\nLet's first come up with a list of experts you may want to consult for this problem and then immediately start solving it."
````

#### Assignment 5: L101 `intermediate_feedback`
````python
intermediate_feedback = "Based on the information given, what are the most logical next steps or conclusions? Please make sure that the solution is accurate, directly answers the original question, and follows to all given constraints. Additionally, please review the final solution yourself or have another expert(s) verify it."
````

#### Assignment 6: L110 `expert_python_message`
````python
expert_python_message: str = 'You are an expert in Python and can generate Python code. To execute the code and display its output in the terminal using print statements, please make sure to include "Please run this code!" after the code block (i.e., after the closing code blocks)'
````

#### Assignment 7: L172 `message_log`
````python
message_log = meta_model.meta_model_generate(
        prompt_or_messages=messages,
        max_tokens=meta_model_settings["parameters"]["max_tokens"],
        temperature=meta_model_settings["parameters"]["temperature"],
        top_p=meta_model_settings["parameters"]["top_p"],
        num_return_sequences=meta_model_settings["parameters"]["num_return_sequences"],
        counter=0,
        original_question=f"{task_description}\n\n{input}",
    )
````

#### Assignment 8: L204 `meta_model_message_list`
````python
meta_model_message_list = meta_prompt_config_dict["meta-model"]["message-list"]
````

#### Assignment 9: L245 `meta_model_settings`
````python
meta_model_settings = meta_prompt_config_dict["meta-model"]
````

#### Assignment 10: L246 `generator_settings`
````python
generator_settings = meta_prompt_config_dict["generator"]
````

#### Assignment 11: L247 `verifier_settings`
````python
verifier_settings = meta_prompt_config_dict["verifier"]
````

#### Assignment 12: L248 `summarizer_settings`
````python
summarizer_settings = meta_prompt_config_dict["summarizer"]
````

#### Assignment 13: L251 ``
````python
meta_model_settings["parameters"]["temperature"] = (
        args.temperature
        if args.temperature is not None
        else meta_model_settings["parameters"]["temperature"]
    )
````

#### Assignment 14: L256 ``
````python
meta_model_settings["parameters"]["top_p"] = (
        args.top_p
        if args.top_p is not None
        else meta_model_settings["parameters"]["top_p"]
    )
````

#### Assignment 15: L261 ``
````python
meta_model_settings["parameters"]["max_tokens"] = (
        args.max_tokens
        if args.max_tokens is not None
        else meta_model_settings["parameters"]["max_tokens"]
    )
````

#### Assignment 16: L266 ``
````python
meta_model_settings["parameters"]["num_return_sequences"] = (
        args.num_return_sequences
        if args.num_return_sequences is not None
        else meta_model_settings["parameters"]["num_return_sequences"]
    )
````

#### Assignment 17: L313 `error_message`
````python
error_message = meta_prompt_config_dict["meta-model"]["error-message"]
````

#### Assignment 18: L314 `final_answer_indicator`
````python
final_answer_indicator = meta_prompt_config_dict["meta-model"][
        "final-answer-indicator"
    ]
````

#### Assignment 19: L332 `meta_model`
````python
meta_model = MetaPromptingScaffolding(
        language_model=model,
        fresh_eyes=args.fresh_eyes,
        generator_settings=generator_settings,
        verifier_settings=verifier_settings,
        summarizer_settings=summarizer_settings,
        error_message=error_message,
        final_answer_indicator=final_answer_indicator,
        include_expert_name_in_instruction=args.include_expert_name_in_instruction,
        extract_output=args.extract_output,
        expert_python_message=args.expert_python_message,
        intermediate_feedback=args.intermediate_feedback,
        use_zero_shot_cot_in_expert_messages=args.use_zero_shot_cot_in_expert_messages,
    )
````

#### Assignment 20: L134 `expert_messages`
````python
expert_messages = [
            {
                "role": "user",
                "content": f"{template_gen_expert_identity}\n\n[Instruction]:{input}\n[Agent Description]:",
            }
        ]
````

#### Assignment 21: L142 `expert_identity`
````python
expert_identity = meta_model.generate(
            prompt_or_messages=expert_messages,
            max_tokens=meta_model_settings["parameters"]["max_tokens"],
            num_return_sequences=meta_model_settings["parameters"][
                "num_return_sequences"
            ],
            temperature=meta_model_settings["parameters"]["temperature"],
            top_p=meta_model_settings["parameters"]["top_p"],
        )
````

#### Assignment 22: L153 `template_expert_prompting`
````python
template_expert_prompting = f"{expert_identity}\n\nNow given the above identity background, please answer the following question:\n\nQuestion: {task_description}\n\n{input}"
````

#### Assignment 23: L361 `outputs`
````python
outputs = Parallel(n_jobs=6, verbose=100, prefer="threads")(
            delayed(run_model)(
                meta_model=meta_model,
                datum=datum,
                prefix_messages=meta_model_message_list,
                task_description=task_description,
                meta_model_settings=meta_model_settings,
                question_suffix=args.question_suffix_or_path,
                question_prefix=args.question_prefix_or_path,
                expert_prompting=args.expert_prompting,
            )
            for datum in data[i : i + BATCHES]
        )
````

#### Assignment 24: L386 `temp_dict`
````python
temp_dict = {"args": args.as_dict(), "config_dict": meta_prompt_config_dict}
````


---

### `utils/execute_code.py`

#### Assignment 1: L17 `process`
````python
process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
````

#### Assignment 2: L24 `captured_output`
````python
captured_output = f"Error in execution: {error_output}"
````


---

### `utils/expert_prompting.py`

#### Assignment 1: L24 `meta_model_output`
````python
meta_model_output = self.language_model.generate(
            prompt_or_messages=prompt_or_messages,
            stop_tokens=stop_tokens,
            max_tokens=max_tokens,
            num_return_sequences=num_return_sequences,
            temperature=temperature,
            top_p=top_p,
            **kwargs,
        )[0]
````


---

### `utils/language_model.py`

#### Assignment 1: L213 `response`
````python
response = self.client.chat.completions.create(
                model=self.model_name,
                messages=prompt_or_messages,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                n=num_return_sequences,
                stop=stop_tokens,
                **kwargs,
            )
````

#### Assignment 2: L185 `response`
````python
response = openai.ChatCompletion.create(
                    engine=self.model_name,
                    messages=prompt_or_messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    n=num_return_sequences,
                    stop=stop_tokens,
                    **kwargs,
                )
````

#### Assignment 3: L198 `response`
````python
response = openai.Completion.create(
                    engine=self.model_name,
                    prompt=prompt_or_messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    n=num_return_sequences,
                    stop=stop_tokens,
                    **kwargs,
                )
````


---

### `utils/meta_scaffolding.py`

#### Assignment 1: L42 `final_answer_indicator`
````python
self.final_answer_indicator = final_answer_indicator
````

#### Assignment 2: L51 `include_expert_name_in_instruction`
````python
self.include_expert_name_in_instruction = include_expert_name_in_instruction
````

#### Assignment 3: L55 `use_zero_shot_cot_in_expert_messages`
````python
self.use_zero_shot_cot_in_expert_messages = use_zero_shot_cot_in_expert_messages
````

#### Assignment 4: L368 `model_output`
````python
model_output = self.language_model.generate(
            prompt_or_messages=prompt_or_messages,
            stop_tokens=stop_tokens,
            max_tokens=max_tokens,
            num_return_sequences=num_return_sequences,
            temperature=temperature,
            top_p=top_p,
            **kwargs,
        )[0]
````

#### Assignment 5: L86 ``
````python
entire_message_log[-1][
                    "content"
                ] = f"ROUND {counter+1}:\n\n{entire_message_log[-1]['content']}"
````

#### Assignment 6: L98 `meta_model_output`
````python
meta_model_output = self.language_model.generate(
                    prompt_or_messages=entire_message_log,
                    stop_tokens=stop_tokens,
                    max_tokens=max_tokens,
                    num_return_sequences=num_return_sequences,
                    temperature=temperature,
                    top_p=top_p,
                    **kwargs,
                )[0]
````

#### Assignment 7: L124 `triple_quote_splits`
````python
triple_quote_splits = meta_model_output.split(self.triple_quotes)
````

#### Assignment 8: L282 `intermediate_output`
````python
intermediate_output = (
                        f"{intermediate_output}\n\n{self.intermediate_feedback}"
                    )
````

#### Assignment 9: L133 `line_preceding_instruction`
````python
line_preceding_instruction = triple_quote_splits[i - 1].strip()
````

#### Assignment 10: L134 `model_name`
````python
model_name = line_preceding_instruction.split("\n")[-1].strip()
````

#### Assignment 11: L163 `model_message_list`
````python
model_message_list = self.generator_settings["message-list"]
````

#### Assignment 12: L166 `current_model_message_list`
````python
current_model_message_list = model_message_list.copy()
````

#### Assignment 13: L180 `model_outputs`
````python
model_outputs = self.language_model.generate(
                                prompt_or_messages=current_model_message_list,
                                stop_tokens=model_stop_tokens,
                                max_tokens=model_max_tokens,
                                num_return_sequences=model_num_return_sequences,
                                temperature=model_temp,
                                top_p=model_top_p,
                                **kwargs,
                            )
````

#### Assignment 14: L143 `model_instruction`
````python
model_instruction = (
                                    f"You are {model_name}.\n\n{model_instruction}"
                                )
````

#### Assignment 15: L175 ``
````python
current_model_message_list[-1][
                                    "content"
                                ] = f"{self.expert_python_message}.\n\n{current_model_message_list[-1]['content']}"
````

#### Assignment 16: L249 `summarizer_prompt_or_messages`
````python
summarizer_prompt_or_messages = (
                                    self.summarizer_settings["message-list"].copy()
                                )
````

#### Assignment 17: L260 `summarizer_output`
````python
summarizer_output = self.language_model.generate(
                                    prompt_or_messages=summarizer_prompt_or_messages,
                                    stop_tokens=None,  # FIXME(msuzgun)
                                    max_tokens=self.summarizer_settings["parameters"][
                                        "max_tokens"
                                    ],
                                    num_return_sequences=self.summarizer_settings[
                                        "parameters"
                                    ]["num_return_sequences"],
                                    temperature=self.summarizer_settings["parameters"][
                                        "temperature"
                                    ],
                                    top_p=self.summarizer_settings["parameters"][
                                        "top_p"
                                    ],
                                    **kwargs,
                                )[0]
````

#### Assignment 18: L200 `code_text`
````python
code_text = code_text.replace(
                                            "```python", "```"
                                        )
````

#### Assignment 19: L215 `python_output`
````python
python_output = execute_code_with_timeout(
                                            code_text
                                        )
````


---

### `utils/sonnet_eval.py`

#### Assignment 1: L68 `errors`
````python
errors = scheme_errors(poem, scheme, verbose=verbose)
````

#### Assignment 2: L356 `wnl`
````python
wnl = sum("line count" in e for e in errors.values()) / num_samples
````

#### Assignment 3: L358 `mw`
````python
mw = sum(bool("missing words" in e) for e in errors.values()) / num_samples
````

#### Assignment 4: L360 `bl`
````python
bl = sum(bool("syllable errors" in e) for e in errors.values()) / num_samples
````

#### Assignment 5: L362 `rhyme_errors`
````python
rhyme_errors = (
        sum(any(" " not in k for k in e) for e in errors.values()) / num_samples
    )
````

#### Assignment 6: L365 `both`
````python
both = (
        sum(
            (bool("syllable errors" in e) and any(" " not in k for k in e))
            for e in errors.values()
        )
        / num_samples
    )
````

#### Assignment 7: L471 `aaa`
````python
aaa = sonnet_errors(
        """How do I love thee? Let me count the ways.
        I love thee to the depth and breadth and height
        My soul can reach, when feeling out of sight
        For the ends of being and ideal grace.
        I love thee to the level of every day’s
        Most quiet need, by sun and candle-light.
        I love thee freely, as men strive for right.
        I love thee purely, as they turn from praise.
        I love thee with the passion put to use
        In my old griefs, and with my childhood’s faith.
        I love thee with a love I seemed to lose
        With my lost saints. I love thee with the breath,
        Smiles, tears, of all my life; and, if God choose,
        I shall but love thee better after death.""",
        "ABBA ABBA CDC DCD",
        # abba abba cdc dcd: (correct)
        # "ABAB CDCD EFEF GG", (false)
    )
````

#### Assignment 8: L493 `aaa`
````python
aaa = sonnet_errors(
        """How do I love thee? Let me count the ways (A)
        I love thee to the depth and breadth and height (B)
        My soul can reach, when feeling out of sight (B)
        For the ends of being and ideal grace (A)
        I love thee to the level of every day’s (A)
        Most quiet need, by sun and candle-light (B)
        I love thee freely, as men strive for right (B)
        I love thee purely, as they turn from praise (A)
        I love thee with the passion put to use (C)
        In my old griefs, and with my childhood’s faith (D)
        I love thee with a love I seemed to lose (C)
        With my lost saints. I love thee with the breath (D)
        Smiles, tears, of all my life; and, if God choose (C)
        I shall but love thee better after death (D).""",
        "ABBA ABBA CDC DCD",
        # abba abba cdc dcd: (correct)
        # "ABAB CDCD EFEF GG", (false)
    )
````
