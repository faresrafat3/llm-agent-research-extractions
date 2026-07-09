# LATS — Complete Prompt / Prompt-Source Extraction

Source repo: `https://github.com/lapisrocks/LanguageAgentTreeSearch`  
Audited commit: `853d81614607dd27433faf17c7b0a7d660f95d22`

## Paper-level schema

LATS combines LM-generated reasoning/actions with Monte Carlo Tree Search. Nodes store thought/action/observation state; expansion samples candidate next actions; evaluation uses LM-powered value functions; rollout simulates trajectories with environment feedback; backpropagation updates node values; self-reflection summarizes failed trajectories and conditions future prompts.

## Raw prompt/source files copied

- `README.md` (4211 bytes) → `raw_prompt_files/README.md`
- `hotpot/lats.sh` (266 bytes) → `raw_prompt_files/hotpot/lats.sh`
- `hotpot/tot.sh` (289 bytes) → `raw_prompt_files/hotpot/tot.sh`
- `hotpot/tot_10it.log` (68104 bytes) → `raw_prompt_files/hotpot/tot_10it.log`
- `index.md` (3980 bytes) → `raw_prompt_files/index.md`
- `programming/generators/todo.md` (98 bytes) → `raw_prompt_files/programming/generators/todo.md`
- `programming/run_dfs.sh` (248 bytes) → `raw_prompt_files/programming/run_dfs.sh`
- `programming/run_lats_gpt3.sh` (292 bytes) → `raw_prompt_files/programming/run_lats_gpt3.sh`
- `programming/run_lats_gpt4.sh` (257 bytes) → `raw_prompt_files/programming/run_lats_gpt4.sh`
- `programming/run_reflexion.sh` (246 bytes) → `raw_prompt_files/programming/run_reflexion.sh`
- `webshop/lats.sh` (342 bytes) → `raw_prompt_files/webshop/lats.sh`
- `webshop/logs/example.log` (347431 bytes) → `raw_prompt_files/webshop/logs/example.log`
- `webshop/prompt.py` (17973 bytes) → `raw_prompt_files/webshop/prompt.py`

## Raw source contents / previews

---

### Source 1: `README.md`

**Size:** 4211 bytes  
**Lines:** 136  
**Raw copy:** `raw_prompt_files/README.md`

```text
# Official Repo of Language Agent Tree Search (LATS) - ICML 2024

<p>
    <a href="https://www.python.org/">
        <img alt="Build" src="https://img.shields.io/badge/Python-3.7+-1f425f.svg?color=purple">
    </a>
    <a href="https://copyright.illinois.edu/">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-blue">
    </a>
</p>

![teaser](pics/teaser.png)

Official implementation for ICML 2024 paper [Language Agent Tree Search Unifies Reasoning Acting and Planing in Language Models](https://arxiv.org/abs/2310.04406) with code, prompts, model outputs. 

More can be found at our [project website](https://lapisrocks.github.io/LanguageAgentTreeSearch/) or [paper](https://arxiv.org/abs/2310.04406)

Check out our demo, CodeLATS at our [demo](https://huggingface.co/spaces/AIatUIUC/CodeLATS/tree/main)

For a more general implementation for your AI applications, please look at the LangChain implementation in LangGraph.
[LATS-LangChain](https://github.com/langchain-ai/langgraph/tree/main/examples/lats) 

or the LlamaIndex implementation
[LATS-LlamaIndex](https://docs.llamaindex.ai/en/latest/api_reference/agent/lats/)


### Reasoning + Acting (HotPotQA)

#### Setup

To get started:

1. Clone this repo and move to the HotPotQA directory:
```bash
git clone https://github.com/andyz245/LanguageAgentTreeSearch && cd LanguageAgentTreeSearch/hotpot
```

2. Install the module dependencies into your environment:
```bash
pip install -r requirements.txt
```

3. Set `OPENAI_API_KEY` environment variable to your OpenAI API key:
```bash
export OPENAI_API_KEY=<your key>
```

4. Set the scripts and run paper experiments
```bash
sh lats.sh
```

- ``--n_generate_sample``: number of times to prompt during expansion/sampling
- ``--n_evaluate_sample``: number of times to prompt for state evaluation
- ``--iterations``: maximum number of trajectories to sample

### Reasoning (Programming)

#### Setup

To get started:

1. Clone this repo and move to the HotPotQA directory:
```bash
git clone https://github.com/andyz245/LanguageAgentTreeSearch && cd LanguageAgentTreeSearch/programming
```

2. Install the module dependencies into your environment:
```bash
pip install -r requirements.txt
```

3. Set `OPENAI_API_KEY` environment variable to your OpenAI API key:
```bash
export OPENAI_API_KEY=<your key>
```

4. Set the scripts and run paper experiments
```bash
sh run_lats.sh
```

Code adapted from https://github.com/noahshinn024/reflexion/tree/main

### Decision-making (WebShop)

#### Setup

To get started:

1. Clone this repo and move to the WebShop directory:
```bash
git clone https://github.com/andyz245/LanguageAgentTreeSearch && cd LanguageAgentTreeSearch/webshop
```

2. Install WebShop from source and run environment instance locally. Follow the instructions here (https://github.com/princeton-nlp/WebShop)

3. Install the module dependencies into your environment:
```bash
pip install -r requirements.txt
```

4. Set `OPENAI_API_KEY` environment variable to your OpenAI API key:
```bash
export OPENAI_API_KEY=<your key>
```

5. Change localhost in lats.py to your local port running WebShop

6. Set the scripts and run paper experiments
```bash
sh lats.sh
```

- ``--n_generate_sample``: number of times to prompt during expansion/sampling
- ``--n_evaluate_sample``: number of times to prompt for state evaluation
- ``--iterations``: maximum number of trajectories to sample

## Trajectories
``programming/root/`` contains all the trajectories from the paper's experiments on programming. Please use get_acc.py with the log path to get the actual accuracy. HotPotQA and WebShop logs were too large to upload, feel free to email if interested.

## Citations
Please cite the paper and star this repo if you use LATS and find it interesting. Feel free to contact andyz3@illinois.edu or open an issue if you have any questions.

```bibtex
@misc{zhou2023language,
      title={Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models}, 
      author={Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},
      year={2023},
      eprint={2310.04406},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}

```

```

---

### Source 2: `hotpot/lats.sh`

**Size:** 266 bytes  
**Lines:** 12  
**Raw copy:** `raw_prompt_files/hotpot/lats.sh`

```bash
python run.py \
    --backend gpt-3.5-turbo \
    --task_start_index 0 \
    --task_end_index 100 \
    --n_generate_sample 5 \
    --n_evaluate_sample 1 \
    --prompt_sample cot \
    --temperature 1.0 \
    --iterations 30 \
    --log logs/tot_10k.log \
    ${@}

```

---

### Source 3: `hotpot/tot.sh`

**Size:** 289 bytes  
**Lines:** 13  
**Raw copy:** `raw_prompt_files/hotpot/tot.sh`

```bash
python run.py \
    --backend gpt-3.5-turbo \
    --task_start_index 0 \
    --task_end_index 50 \
    --n_generate_sample 5 \
    --n_evaluate_sample 1 \
    --prompt_sample cot \
    --temperature 1.0 \
    --iterations 150 \
    --log logs/tot_150k.log \
    --algorithm tot \
    ${@}

```

---

### Source 4: `hotpot/tot_10it.log`

**Size:** 68104 bytes  
**Lines:** 378  
**Raw copy:** `raw_prompt_files/hotpot/tot_10it.log`

```text
2024-03-21 20:13:37,532 - INFO - This is a test log entryyyyyy.
2024-03-21 20:13:37,650 - INFO - Logging has been configured.
2024-03-21 20:13:37,653 - INFO - Logging has been configured.
2024-03-21 20:13:37,657 - INFO - DFS at node depth 0...
2024-03-21 20:13:37,677 - INFO - PROMPT: 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78–1.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron "Bumblefoot" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

Question: Which magazine was started first Arthur's Magazine or First for Women?Thought 1: 

2024-03-21 20:13:39,258 - INFO - SAMPLED ACTION: ["Thought 1: I need to search for the start dates of Arthur's Magazine and First for Women to determine which one was started first.\nAction 1: Search[Arthur's Magazine start date]\n", "Thought 1: I need to search when Arthur's Magazine and First for Women were started to determine which one was started first.\nAction 1: Search[Arthur's Magazine start date]\n", "Thought 1: I need to search when Arthur's Magazine and First for Women were started to determine which one started first.\nAction 1: Search[Arthur's Magazine start date]\n", "Thought 1: I need to find out which magazine was started first, Arthur's Magazine or First for Women. I should search for the history of both magazines.\nAction 1: Search[Arthur's Magazine]\n", "Thought 1: I need to determine which magazine was started first, Arthur's Magazine or First for Women.\nAction 1: Search[Arthur's Magazine]\n"]
2024-03-21 20:13:40,129 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, thought=I need to search for the start dates of Arthur's Magazine and First for Women to determine which one was started first., action=Search[Arthur's Magazine start date], observation=Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'Magazine', 'International Date Line', 'Arthur (TV series)', 'Pulp magazine'].)
2024-03-21 20:13:40,129 - INFO - Feedback: {'steps': 1, 'answer': None}
2024-03-21 20:13:40,918 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, thought=I need to search when Arthur's Magazine and First for Women were started to determine which one was started first., action=Search[Arthur's Magazine start date], observation=Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'International Date Line', 'Arthur (TV series)', 'Pulp magazine', 'Magazine'].)
2024-03-21 20:13:40,919 - INFO - Feedback: {'steps': 2, 'answer': None}
2024-03-21 20:13:41,703 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, thought=I need to search when Arthur's Magazine and First for Women were started to determine which one started first., action=Search[Arthur's Magazine start date], observation=Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'Arthur (TV series)', 'Magazine', 'International Date Line', 'Pulp magazine'].)
2024-03-21 20:13:41,703 - INFO - Feedback: {'steps': 3, 'answer': None}
2024-03-21 20:13:41,975 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, thought=I need to find out which magazine was started first, Arthur's Magazine or First for Women. I should search for the history of both magazines., action=Search[Arthur's Magazine], observation=Arthur's Magazine (1844–1846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3].)
2024-03-21 20:13:41,975 - INFO - Feedback: {'steps': 4, 'answer': None}
2024-03-21 20:13:42,354 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, thought=I need to determine which magazine was started first, Arthur's Magazine or First for Women., action=Search[Arthur's Magazine], observation=Arthur's Magazine (1844–1846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3].)
2024-03-21 20:13:42,354 - INFO - Feedback: {'steps': 5, 'answer': None}
2024-03-21 20:13:42,354 - INFO - State of all_nodes after iteration: [(<tot.Node object at 0x7fc79df52ee0>, 0), (<tot.Node object at 0x7fc79df52f10>, 0), (<tot.Node object at 0x7fc84f704640>, 0), (<tot.Node object at 0x7fc7a0456880>, 0), (<tot.Node object at 0x7fc84f6d3760>, 0), (<tot.Node object at 0x7fc84f6f1b80>, 0)]
2024-03-21 20:13:42,354 - INFO - DFS at node depth 1...
2024-03-21 20:13:42,366 - INFO - PROMPT: 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78–1.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron "Bumblefoot" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search for the start dates of Arthur's Magazine and First for Women to determine which one was started first.
Action 1: Search[Arthur's Magazine start date]
Observation 1: Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'Magazine', 'International Date Line', 'Arthur (TV series)', 'Pulp magazine'].Thought 2: 

2024-03-21 20:13:44,287 - INFO - SAMPLED ACTION: ["Thought 2: I need to search for the start date of First for Women and compare it with Arthur's Magazine.\nAction 2: Search[First for Women start date]", "Thought 2: I couldn't find the start date for Arthur's Magazine, maybe I should search for First for Women start date and compare.\nAction 2: Search[First for Women start date]", "Thought 2: I couldn't find the start date for Arthur's Magazine. I should try searching for the start date of First for Women.\nAction 2: Search[First for Women start date]\n", "Thought 2: I couldn't find the start date of Arthur's Magazine, so I need to search for the start date of First for Women.\nAction 2: Search[First for Women start date]", "Thought 2: I couldn't find the start date for Arthur's Magazine. Let me try searching for the start date of First for Women.\nAction 2: Search[First for Women start date]"]
2024-03-21 20:13:45,258 - INFO - NEW NODE: Node(depth=2, value=0.00, visits=0, thought=I need to search for the start date of First for Women and compare it with Arthur's Magazine., action=Search[First for Women start date], observation=Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'Blind date'].)
2024-03-21 20:13:45,258 - INFO - Feedback: {'steps': 6, 'answer': None}
2024-03-21 20:13:46,301 - INFO - NEW NODE: Node(depth=2, value=0.00, visits=0, thought=I couldn't find the start date for Arthur's Magazine, maybe I should search for First for Women start date and compare., action=Search[First for Women start date], observation=Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'It Starts with Us'].)
2024-03-21 20:13:46,301 - INFO - Feedback: {'steps': 7, 'answer': None}
2024-03-21 20:13:47,260 - INFO - NEW NODE: Node(depth=2, value=0.00, visits=0, thought=I couldn't find the start date for Arthur's Magazine. I should try searching for the start date of First for Women., action=Search[First for Women start date], observation=Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'It Starts with Us'].)
2024-03-21 20:13:47,260 - INFO - Feedback: {'steps': 8, 'answer': None}
2024-03-21 20:13:48,167 - INFO - NEW NODE: Node(depth=2, value=0.00, visits=0, thought=I couldn't find the start date of Arthur's Magazine, so I need to search for the start date of First for Women., action=Search[First for Women start date], observation=Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'Blind date'].)
2024-03-21 20:13:48,167 - INFO - Feedback: {'steps': 9, 'answer': None}
2024-03-21 20:13:49,224 - INFO - NEW NODE: Node(depth=2, value=0.00, visits=0, thought=I couldn't find the start date for Arthur's Magazine. Let me try searching for the start date of First for Women., action=Search[First for Women start date], observation=Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'Blind date'].)
2024-03-21 20:13:49,224 - INFO - Feedback: {'steps': 10, 'answer': None}
2024-03-21 20:13:49,225 - INFO - State of all_nodes after iteration: [(<tot.Node object at 0x7fc79df52ee0>, 0), (<tot.Node object at 0x7fc79df52f10>, 0), (<tot.Node object at 0x7fc84f688d30>, 0), (<tot.Node object at 0x7fc84f685bb0>, 0), (<tot.Node object at 0x7fc84f6682e0>, 0), (<tot.Node object at 0x7fc84f633820>, 0), (<tot.Node object at 0x7fc84f583ac0>, 0), (<tot.Node object at 0x7fc84f704640>, 0), (<tot.Node object at 0x7fc7a0456880>, 0), (<tot.Node object at 0x7fc84f6d3760>, 0), (<tot.Node object at 0x7fc84f6f1b80>, 0)]
2024-03-21 20:13:49,225 - INFO - DFS at node depth 2...
2024-03-21 20:13:49,237 - INFO - PROMPT: 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78–1.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron "Bumblefoot" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search for the start dates of Arthur's Magazine and First for Women to determine which one was started first.
Action 1: Search[Arthur's Magazine start date]
Observation 1: Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'Magazine', 'International Date Line', 'Arthur (TV series)', 'Pulp magazine'].
Thought 2: I need to search for the start date of First for Women and compare it with Arthur's Magazine.
Action 2: Search[First for Women start date]
Observation 2: Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'Blind date'].Thought 3: 

2024-03-21 20:13:51,833 - INFO - SAMPLED ACTION: ["Thought 3: I need to try a different approach. Maybe I can search for the history of Arthur's Magazine and First for Women to find out which one started first.\nAction 3: Search[Arthur's Magazine history]\n", "Thought 3: I couldn't find the start dates of Arthur's Magazine and First for Women. Maybe I can look up the founding dates of the magazines instead.\nAction 3: Search[Arthur's Magazine founding date]", "Thought 3: I couldn't find the start dates for either Arthur's Magazine or First for Women. I should try to search for a list of oldest magazines and compare the start dates of both magazines.\nAction 3: Search[List of oldest magazines]", "Thought 3: I need to think of another way to determine which magazine was started first. Maybe I can look up the history of both magazines to see which one mentions starting earlier.\nAction 3: Search[Arthur's Magazine history]\n", "Thought 3: I need to find another way to determine which magazine was started first. I should look up the history of both magazines.\nAction 3: Search[history of Arthur's Magazine]\n"]
2024-03-21 20:13:52,727 - INFO - NEW NODE: Node(depth=3, value=0.00, visits=0, thought=I need to try a different approach. Maybe I can search for the history of Arthur's Magazine and First for Women to find out which one started first., action=Search[Arthur's Magazine history], observation=Could not find Arthur's Magazine history. Similar: ["Arthur's Magazine", "Arthur's Lady's Home Magazine", 'Chester A. Arthur', 'Timothy Shay Arthur', 'Bea Arthur'].)
2024-03-21 20:13:52,728 - INFO - Feedback: {'steps': 11, 'answer': None}
2024-03-21 20:13:53,567 - INFO - NEW NODE: Node(depth=3, value=0.00, visits=0, thought=I couldn't find the start dates of Arthur's Magazine and First for Women. Maybe I can look up the founding dates of the magazines instead., action=Search[Arthur's Magazine founding date], observation=Could not find Arthur's Magazine founding date. Similar: ['Arthur (2011 film)', 'Chester A. Arthur', 'Magazine', 'Magazine (firearms)', 'Arthur (TV series)'].)
2024-03-21 20:13:53,567 - INFO - Feedback: {'steps': 12, 'answer': None}
2024-03-21 20:13:54,313 - INFO - NEW NODE: Node(depth=3, value=0.00, visits=0, thought=I couldn't find the start dates for either Arthur's Magazine or First for Women. I should try to search for a list of oldest magazines and compare the start dates of both magazines., action=Search[List of oldest magazines], observation=Could not find List of oldest magazines. Similar: ['List of oldest living people', 'List of oldest cats', 'List of oldest companies', 'List of oldest trees', 'List of oldest church buildings'].)
2024-03-21 20:13:54,313 - INFO - Feedback: {'steps': 13, 'answer': None}
2024-03-21 20:13:55,080 - INFO - NEW NODE: Node(depth=3, value=0.00, visits=0, thought=I need to think of another way to determine which magazine was started first. Maybe I can look up the history of both magazines to see which one mentions starting earlier., action=Search[Arthur's Magazine history], observation=Could not find Arthur's Magazine history. Similar: ["Arthur's Magazine", "Arthur's Lady's Home Magazine", 'Chester A. Arthur', "Arthur's Pass National Park", 'Timothy Shay Arthur'].)
2024-03-21 20:13:55,081 - INFO - Feedback: {'steps': 14, 'answer': None}
2024-03-21 20:13:56,048 - INFO - NEW NODE: Node(depth=3, value=0.00, visits=0, thought=I need to find another way to determine which magazine was started first. I should look up the history of both magazines., action=Search[history of Arthur's Magazine], observation=Could not find history of Arthur's Magazine. Similar: ["Arthur's Magazine", "Arthur's Lady's Home Magazine", 'Chester A. Arthur', "Arthur's Pass National Park", 'Timothy Shay Arthur'].)
2024-03-21 20:13:56,048 - INFO - Feedback: {'steps': 15, 'answer': None}
2024-03-21 20:13:56,048 - INFO - State of all_nodes after iteration: [(<tot.Node object at 0x7fc79df52ee0>, 0), (<tot.Node object at 0x7fc79df52f10>, 0), (<tot.Node object at 0x7fc84f688d30>, 0), (<tot.Node object at 0x7fc84f5bbb80>, 0), (<tot.Node object at 0x7fc84f54ca60>, 0), (<tot.Node object at 0x7fc84f516b20>, 0), (<tot.Node object at 0x7fc84f576280>, 0), (<tot.Node object at 0x7fc84f4edfd0>, 0), (<tot.Node object at 0x7fc84f685bb0>, 0), (<tot.Node object at 0x7fc84f6682e0>, 0), (<tot.Node object at 0x7fc84f633820>, 0), (<tot.Node object at 0x7fc84f583ac0>, 0), (<tot.Node object at 0x7fc84f704640>, 0), (<tot.Node object at 0x7fc7a0456880>, 0), (<tot.Node object at 0x7fc84f6d3760>, 0), (<tot.Node object at 0x7fc84f6f1b80>, 0)]
2024-03-21 20:13:56,048 - INFO - DFS at node depth 3...
2024-03-21 20:13:56,061 - INFO - PROMPT: 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78–1.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron "Bumblefoot" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search for the start dates of Arthur's Magazine and First for Women to determine which one was started first.
Action 1: Search[Arthur's Magazine start date]
Observation 1: Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'Magazine', 'International Date Line', 'Arthur (TV series)', 'Pulp magazine'].
Thought 2: I need to search for the start date of First for Women and compare it with Arthur's Magazine.
Action 2: Search[First for Women start date]
Observation 2: Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'Blind date'].
Thought 3: I need to try a different approach. Maybe I can search for the history of Arthur's Magazine and First for Women to find out which one started first.
Action 3: Search[Arthur's Magazine history]
Observation 3: Could not find Arthur's Magazine history. Similar: ["Arthur's Magazine", "Arthur's Lady's Home Magazine", 'Chester A. Arthur', 'Timothy Shay Arthur', 'Bea Arthur'].Thought 4: 

2024-03-21 20:13:57,614 - INFO - SAMPLED ACTION: ["Thought 4: I need to search for the history of First for Women and compare it with Arthur's Magazine.\nAction 4: Search[First for Women history]", "Thought 4: I need to search for the history of First for Women to compare it with Arthur's Magazine.\nAction 4: Search[First for Women history]", "Thought 4: I need to search for the history of First for Women and compare it with Arthur's Magazine to determine which one started first.\nAction 4: Search[First for Women history]", 'Thought 4: I need to search for the history of First for Women as well.\nAction 4: Search[First for Women history]', "Thought 4: I need to search for the history of First for Women to compare it with Arthur's Magazine.\nAction 4: Search[First for Women history]"]
2024-03-21 20:13:58,839 - INFO - NEW NODE: Node(depth=4, value=0.00, visits=0, thought=I need to search for the history of First for Women and compare it with Arthur's Magazine., action=Search[First for Women history], observation=Could not find First for Women history. Similar: ["Women's History Month", "Women's history", 'Women and children first', 'Women in medicine', 'History of women in Canada'].)
2024-03-21 20:13:58,840 - INFO - Feedback: {'steps': 16, 'answer': None}
2024-03-21 20:13:59,994 - INFO - NEW NODE: Node(depth=4, value=0.00, visits=0, thought=I need to search for the history of First for Women to compare it with Arthur's Magazine., action=Search[First for Women history], observation=Could not find First for Women history. Similar: ["Women's History Month", 'Women and children first', "Women's history", 'Women in medicine', 'History of women in Canada'].)
2024-03-21 20:13:59,995 - INFO - Feedback: {'steps': 17, 'answer': None}
2024-03-21 20:14:01,256 - INFO - NEW NODE: Node(depth=4, value=0.00, visits=0, thought=I need to search for the history of First for Women and compare it with Arthur's Magazine to determine which one started first., action=Search[First for Women history], observation=Could not find First for Women history. Similar: ["Women's History Month", "Women's history", 'Women and children first', 'Women in medicine', 'History of women in Canada'].)
2024-03-21 20:14:01,256 - INFO - Feedback: {'steps': 18, 'answer': None}
2024-03-21 20:14:02,477 - INFO - NEW NODE: Node(depth=4, value=0.00, visits=0, thought=I need to search for the history of First for Women as well., action=Search[First for Women history], observation=Could not find First for Women history. Similar: ["Women's History Month", 'Women and children first', "Women's history", 'Women in medicine', 'History of women in Canada'].)
2024-03-21 20:14:02,477 - INFO - Feedback: {'steps': 19, 'answer': None}
2024-03-21 20:14:02,477 - INFO - State of all_nodes after iteration: [(<tot.Node object at 0x7fc79df52ee0>, 0), (<tot.Node object at 0x7fc79df52f10>, 0), (<tot.Node object at 0x7fc84f688d30>, 0), (<tot.Node object at 0x7fc84f5bbb80>, 0), (<tot.Node object at 0x7fc84f4b5eb0>, 0), (<tot.Node object at 0x7fc84f499370>, 0), (<tot.Node object at 0x7fc84f407d30>, 0), (<tot.Node object at 0x7fc84f3d4d30>, 0), (<tot.Node object at 0x7fc84f54ca60>, 0), (<tot.Node object at 0x7fc84f516b20>, 0), (<tot.Node object at 0x7fc84f576280>, 0), (<tot.Node object at 0x7fc84f4edfd0>, 0), (<tot.Node object at 0x7fc84f685bb0>, 0), (<tot.Node object at 0x7fc84f6682e0>, 0), (<tot.Node object at 0x7fc84f633820>, 0), (<tot.Node object at 0x7fc84f583ac0>, 0), (<tot.Node object at 0x7fc84f704640>, 0), (<tot.Node object at 0x7fc7a0456880>, 0), (<tot.Node object at 0x7fc84f6d3760>, 0), (<tot.Node object at 0x7fc84f6f1b80>, 0)]
2024-03-21 20:14:02,477 - INFO - DFS at node depth 4...
2024-03-21 20:14:02,490 - INFO - PROMPT: 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78–1.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron "Bumblefoot" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search for the start dates of Arthur's Magazine and First for Women to determine which one was started first.
Action 1: Search[Arthur's Magazine start date]
Observation 1: Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'Magazine', 'International Date Line', 'Arthur (TV series)', 'Pulp magazine'].
Thought 2: I need to search for the start date of First for Women and compare it with Arthur's Magazine.
Action 2: Search[First for Women start date]
Observation 2: Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'Blind date'].
Thought 3: I need to try a different approach. Maybe I can search for the history of Arthur's Magazine and First for Women to find out which one started first.
Action 3: Search[Arthur's Magazine history]
Observation 3: Could not find Arthur's Magazine history. Similar: ["Arthur's Magazine", "Arthur's Lady's Home Magazine", 'Chester A. Arthur', 'Timothy Shay Arthur', 'Bea Arthur'].
Thought 4: I need to search for the history of First for Women and compare it with Arthur's Magazine.
Action 4: Search[First for Women history]
Observation 4: Could not find First for Women history. Similar: ["Women's History Month", "Women's history", 'Women and children first', 'Women in medicine', 'History of women in Canada'].Thought 5: 

2024-03-21 20:14:04,135 - INFO - SAMPLED ACTION: ["Thought 5: I need to find another way to determine which magazine was started first. Maybe I can look up the publication dates of the first issues of Arthur's Magazine and First for Women.\nAction 5: Search[Arthur's Magazine first issue publication date]", "Thought 5: I seem to be struggling to find the start dates or history of both magazines. Maybe I can try a different search approach to find out which one was started first.\nAction 5: Search[difference between Arthur's Magazine and First for Women]\n", "Thought 5: I need to find another way to determine which magazine was started first. Maybe I can search for any information that directly compares the start dates of Arthur's Magazine and First for Women.\nAction 5: Search[Arthur's Magazine vs First for Women start date comparison]", "Thought 5: I need to find a different approach to solve this question. Maybe I can search for the founding year of Arthur's Magazine and First for Women to determine which one was started first.\nAction 5: Search[Arthur's Magazine founding year]\n", "Thought 5: I need to find another way to determine which magazine was started first. Maybe I can search for the founding dates of the companies behind Arthur's Magazine and First for Women.\nAction 5: Search[Arthur's Magazine founding date]\n"]
2024-03-21 20:14:04,998 - INFO - NEW NODE: Node(depth=5, value=0.00, visits=0, thought=I need to find another way to determine which magazine was started first. Maybe I can look up the publication dates of the first issues of Arthur's Magazine and First for Women., action=Search[Arthur's Magazine first issue publication date], observation=Could not find Arthur's Magazine first issue publication date. Similar: ['Allure (magazine)', 'Doctor Who Magazine', 'Mad (magazine)', 'If (magazine)', 'New Worlds (magazine)'].)
2024-03-21 20:14:04,998 - INFO - Feedback: {'steps': 20, 'answer': None}
2024-03-21 20:14:05,888 - INFO - NEW NODE: Node(depth=5, value=0.00, visits=0, thought=I seem to be struggling to find the start dates or history of both magazines. Maybe I can try a different search approach to find out which one was started first., action=Search[difference between Arthur's Magazine and First for Women], observation=Could not find difference between Arthur's Magazine and First for Women. Similar: ['King Arthur (2004 film)', 'Astrid et Raphaëlle (redirect from Astrid and Raphaëlle)', 'Elaine of Corbenic', 'Society and culture of the Victorian era', 'Arthur Balfour'].)
2024-03-21 20:14:05,888 - INFO - Feedback: {'steps': 21, 'answer': None}
2024-03-21 20:14:06,851 - INFO - NEW NODE: Node(depth=5, value=0.00, visits=0, thought=I need to find another way to determine which magazine was started first. Maybe I can search for any information that directly compares the start dates of Arthur's Magazine and First for Women., action=Search[Arthur's Magazine vs First for Women start date comparison], observation=Could not find Arthur's Magazine vs First for Women start date comparison. Similar: ['Wikipedia (redirect from Wikipedia Selection for Schools)', '2016 United States presidential election (redirect from Trump vs Clinton)', 'Roman Reigns', 'Oldest football clubs (redirect from List of Association football clubs by date of foundation)', 'Joker (2019 film) (category Template film date with 2 release dates)'].)
2024-03-21 20:14:06,851 - INFO - Feedback: {'steps': 22, 'answer': None}
2024-03-21 20:14:07,650 - INFO - NEW NODE: Node(depth=5, value=0.00, visits=0, thought=I need to find a different approach to solve this question. Maybe I can search for the founding year of Arthur's Magazine and First for Women to determine which one was started first., action=Search[Arthur's Magazine founding year], observation=Could not find Arthur's Magazine founding year. Similar: ['Founding Fathers of the United States', 'Chester A. Arthur', 'Oui (magazine)', 'The Strand Magazine', "Arthur's Pass National Park"].)
2024-03-21 20:14:07,650 - INFO - Feedback: {'steps': 23, 'answer': None}
2024-03-21 20:14:08,447 - INFO - NEW NODE: Node(depth=5, value=0.00, visits=0, thought=I need to find another way to determine which magazine was started first. Maybe I can search for the founding dates of the companies behind Arthur's Magazine and First for Women., action=Search[Arthur's Magazine founding date], observation=Could not find Arthur's Magazine founding date. Similar: ['Arthur (2011 film)', 'Chester A. Arthur', 'Magazine', 'Magazine (firearms)', 'Arthur (TV series)'].)
2024-03-21 20:14:08,447 - INFO - Feedback: {'steps': 24, 'answer': None}
2024-03-21 20:14:08,447 - INFO - State of all_nodes after iteration: [(<tot.Node object at 0x7fc79df52ee0>, 0), (<tot.Node object at 0x7fc79df52f10>, 0), (<tot.Node object at 0x7fc84f688d30>, 0), (<tot.Node object at 0x7fc84f5bbb80>, 0), (<tot.Node object at 0x7fc84f4b5eb0>, 0), (<tot.Node object at 0x7fc84f688fd0>, 0), (<tot.Node object at 0x7fc84f709eb0>, 0), (<tot.Node object at 0x7fc84f4acb80>, 0), (<tot.Node object at 0x7fc84f4290a0>, 0), (<tot.Node object at 0x7fc84f416f70>, 0), (<tot.Node object at 0x7fc84f499370>, 0), (<tot.Node object at 0x7fc84f407d30>, 0), (<tot.Node object at 0x7fc84f3d4d30>, 0), (<tot.Node object at 0x7fc84f54ca60>, 0), (<tot.Node object at 0x7fc84f516b20>, 0), (<tot.Node object at 0x7fc84f576280>, 0), (<tot.Node object at 0x7fc84f4edfd0>, 0), (<tot.Node object at 0x7fc84f685bb0>, 0), (<tot.Node object at 0x7fc84f6682e0>, 0), (<tot.Node object at 0x7fc84f633820>, 0), (<tot.Node object at 0x7fc84f583ac0>, 0), (<tot.Node object at 0x7fc84f704640>, 0), (<tot.Node object at 0x7fc7a0456880>, 0), (<tot.Node object at 0x7fc84f6d3760>, 0), (<tot.Node object at 0x7fc84f6f1b80>, 0)]
2024-03-21 20:14:08,447 - INFO - DFS at node depth 5...
2024-03-21 20:14:08,460 - INFO - PROMPT: 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78–1.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron "Bumblefoot" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search for the start dates of Arthur's Magazine and First for Women to determine which one was started first.
Action 1: Search[Arthur's Magazine start date]
Observation 1: Could not find Arthur's Magazine start date. Similar: ['Chester A. Arthur', 'Magazine', 'International Date Line', 'Arthur (TV series)', 'Pulp magazine'].
Thought 2: I need to search for the start date of First for Women and compare it with Arthur's Magazine.
Action 2: Search[First for Women start date]
Observation 2: Could not find First for Women start date. Similar: ['First date', 'Dating', "Women's Premier League (cricket)", "International Women's Day", 'Blind date'].
Thought 3: I need to try a different approach. Maybe I can search for the history of Arthur's Magazine and First for Women to find out which one started first.
Action 3: Search[Arthur's Magazine history]
Observation 3: Could not find Arthur's Magazine history. Similar: ["Arthur's Magazine", "Arthur's Lady's Home Magazine", 'Chester A. Arthur', 'Timothy Shay Arthur', 'Bea Arthur'].
Thought 4: I need to search for the history of First for Women and compare it with Arthur's Magazine.
Action 4: Search[First for Women history]
Observation 4: Could not find First for Women history. Similar: ["Women's History Month", "Women's history", 'Women and children first', 'Women in medicine', 'History of women in Canada'].
Thought 5: I need to find another way to determine which magazine was started first. Maybe I can look up the publication dates of the first issues of Arthur's Magazine and First for Women.
Action 5: Search[Arthur's Magazine first issue publication date]
Observation 5: Could not find Arthur's Magazine first issue publication date. Similar: ['Allure (magazine)', 'Doctor Who Magazine', 'Mad (magazine)', 'If (magazine)', 'New Worlds (magazine)'].Thought 6: 

2024-03-21 20:14:10,049 - INFO - SAMPLED ACTION: ["Thought 6: I need to search for the publication date of the first issue of First for Women and compare it with Arthur's Magazine.\nAction 6: Search[First for Women first issue publication date]", "Thought 6: I need to search for the publication date of the first issue of First for Women and compare it with Arthur's Magazine.\nAction 6: Search[First for Women first issue publication date]", "Thought 6: I need to search for the publication date of the first issue of First for Women and compare it with Arthur's Magazine.\nAction 6: Search[First for Women first issue publication date]", "Thought 6: I need to search for the publication date of the first issue of First for Women and compare it with the information I have on Arthur's Magazine.\nAction 6: Search[First for Women first issue publication date]", "Thought 6: I need to search the publication date of the first issue of First for Women and compare it with the potential publication date of Arthur's Magazine.\nAction 6: Search[First for Women first issue publication date]"]

```

---

### Source 5: `index.md`

**Size:** 3980 bytes  
**Lines:** 64  
**Raw copy:** `raw_prompt_files/index.md`

```text

[Paper](https://arxiv.org/abs/2310.04406) | [Code](https://github.com/andyz245/LanguageAgentTreeSearch) | [Demo](https://huggingface.co/spaces/AIatUIUC/CodeLATS) 
  

![teaser](pics/related.png)

# Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

Language models can use reasoning and enhance acting for decision-making tasks (ReAct, Reflexion). Planning can also enhance reasoning through search (RAP, ToT). We show that through LATS, unifying reasoning, acting, and planning is the best approach for both reasoning and decision-making tasks.

  

## Abstract

  

While large language models (LLMs) have demonstrated impressive performance on a range of decision-making tasks, they rely on simple acting processes and fall short of broad deployment as autonomous agents. We introduce LATS (Language Agent Tree Search), a general framework that synergizes the capabilities of LLMs in planning, acting, and reasoning. Drawing inspiration from Monte Carlo tree search in model-based reinforcement learning, LATS employs LLMs as agents, value functions, and optimizers, repurposing their latent strengths for enhanced decision-making. What is crucial in this method is the use of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism that moves beyond the limitations of existing techniques. Our experimental evaluation across diverse domains, such as programming, HotPotQA, and WebShop, illustrates the applicability of LATS for both reasoning and acting. In particular, LATS achieves 94.4% for programming on HumanEval with GPT-4 and an average score of 75.9 for web browsing on WebShop with GPT-3.5, demonstrating the effectiveness and generality of our method.
  

## Results

  
  | Prompting Method          | HotpotQA (question answering, exact match) | HumanEval (programming, pass@1) | WebShop (web interaction, score) |
|---------------------------|---------------------------------------------------|-----------------------------------------------|----------------------------------------------|
| CoT                       | 0.34                                               | 46.9                                           | N/A (cannot act)                                          |
| ReAct                     | 0.32                                              | 56.9                                           | 53.8                                          |
| ToT                       | 0.55                                               | 54.4                                           | N/A (cannot act)                                           |
| Reflexion                 | 0.51                                               | 68.1                                           | 64.2                                          |
| LATS                      | 0.71                                               | 83.8                                           | 75.9                                          |


With GPT-3.5, LATS outperforms ReAct, Reflexion, CoT, ToT, and RAP across a variety of tasks, including programming and web-browsing.

  

## QA Example

  

![example](pics/qual.png)

  

LATS can sample many ReAct trajectories and construct the best one. This is done by deconstructing trajectories into states, which form the nodes of the tree. An LLM evaluates each state to guide the search algorithm.

  

## Citations

Please cite the paper and star this repo if you use LATS and find it interesting/useful, thanks! Feel free to contact andyz3@illinois.edu or open an issue if you have any questions.

  

```bibtex
@misc{zhou2023language,
      title={Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models}, 
      author={Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},
      year={2023},
      eprint={2310.04406},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```

```

---

### Source 6: `programming/generators/todo.md`

**Size:** 98 bytes  
**Lines:** 6  
**Raw copy:** `raw_prompt_files/programming/generators/todo.md`

```text
# TODO

- remove func signature during evaluation
- edit prompts for rust
- add a parse_rust_code

```

---

### Source 7: `programming/run_dfs.sh`

**Size:** 248 bytes  
**Lines:** 11  
**Raw copy:** `raw_prompt_files/programming/run_dfs.sh`

```bash
python main.py \
  --run_name "test_dfs_humaneval2" \
  --root_dir "root" \
  --dataset_path ./benchmarks/humaneval-py.jsonl \
  --strategy "dfs" \
  --language "py" \
  --model "gpt-3.5-turbo" \
  --pass_at_k "1" \
  --max_iters "8" \
  --verbose

```

---

### Source 8: `programming/run_lats_gpt3.sh`

**Size:** 292 bytes  
**Lines:** 13  
**Raw copy:** `raw_prompt_files/programming/run_lats_gpt3.sh`

```bash
python main.py \
  --run_name "test_gpt3" \
  --root_dir "root" \
  --dataset_path ./benchmarks/humaneval-py.jsonl \
  --strategy "mcts" \
  --language "py" \
  --model "gpt-3.5-turbo" \
  --pass_at_k "1" \
  --max_iters "4" \
  --expansion_factor "3" \
  --number_of_tests "4" \
  --verbose

```

---

### Source 9: `programming/run_lats_gpt4.sh`

**Size:** 257 bytes  
**Lines:** 12  
**Raw copy:** `raw_prompt_files/programming/run_lats_gpt4.sh`

```bash
python main.py \
  --run_name "test_gpt4" \
  --root_dir "root" \
  --dataset_path ./benchmarks/humaneval-py.jsonl \
  --strategy "mcts" \
  --language "py" \
  --model "gpt-4" \
  --pass_at_k "1" \
  --max_iters "8" \
  --number_of_tests "2" \
  --verbose

```

---

### Source 10: `programming/run_reflexion.sh`

**Size:** 246 bytes  
**Lines:** 11  
**Raw copy:** `raw_prompt_files/programming/run_reflexion.sh`

```bash
python main.py \
  --run_name "test_react3" \
  --root_dir "root" \
  --dataset_path ./benchmarks/humaneval-py.jsonl \
  --strategy "reflexion" \
  --language "py" \
  --model "gpt-3.5-turbo" \
  --pass_at_k "1" \
  --max_iters "8" \
  --verbose

```

---

### Source 11: `webshop/lats.sh`

**Size:** 342 bytes  
**Lines:** 15  
**Raw copy:** `raw_prompt_files/webshop/lats.sh`

```bash
python run.py \
    --backend gpt-3.5-turbo \
    --task_start_index 0 \
    --task_end_index 50 \
    --n_generate_sample 5 \
    --n_evaluate_sample 1 \
    --prompt_sample cot \
    --temperature 1.0 \
    --iterations 30 \
    --log logs/new_run.log \
    ${@}

# remember to change the url in lats.py to your local instance of WebShop 


```

---

### Source 12: `webshop/logs/example.log`

**Size:** 347431 bytes  
**Lines:** 7270  
**Raw copy:** `raw_prompt_files/webshop/logs/example.log`

Large artifact/log; full raw copy saved. Preview first 8000 chars:
```text
2023-10-10 01:48:25,478 - INFO - {}
2023-10-10 01:48:25,501 - INFO - Iteration 1...
2023-10-10 01:48:25,502 - INFO - PROMPT: Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: think[For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.]
Observation: OK.

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]


WebShop 
Instruction:  
i need a long clip-in hair extension which is natural looking, and price lower than 40.00 dollars 
[Search] 
Action: 

2023-10-10 01:49:05,776 - INFO - {}
2023-10-10 01:49:05,791 - INFO - Iteration 1...
2023-10-10 01:49:05,791 - INFO - PROMPT: Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: think[For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.]
Observation: OK.

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]


WebShop 
Instruction:  
i need a long clip-in hair extension which is natural looking, and price lower than 40.00 dollars 
[Search] 
Action: 

2023-10-10 01:49:07,988 - INFO - SAMPLED ACTION: ['\nAction: search[long clip-in hair extension natural looking]', '\nAction: search[long clip-in hair extension natural looking]', '\nAction: search[long clip-in hair extension natural looking]\n', '\nAction: search[long clip-in hair extension natural looking]\n', '\nAction: search[long clip-in hair extension natural looking]', '\nAction: search[long clip-in hair extension natural looking]\n', '\nAction: search[long clip-in hair extension natural looking under 40.00 dollars]', '\nAction: search[long clip-in hair extension natural looking price < 40.00 dollars]\n', '\nAction: search[long clip-in hair extension natural looking]\n', '\nAction: search[long clip-in hair extension natural looking]\n']
2023-10-10 01:49:07,988 - INFO - {'fixed_0': {'session': 'fixed_0', 'page_type': 'init'}}
2023-10-10 01:49:07,988 - INFO - {'fixed_0': {'session': 'fixed_0', 'page_type': 'init'}}
2023-10-10 01:49:08,355 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, action=search[long clip-in hair extension natural looking], observation=
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B09QQLDJ93] 
Lroveb Fashion Long Curly Wig Head Dyed Black Gradient Golden Long Straight Wig African Long Curly Hair Wigs Ladies Gradient Color Chemical Fiber Silk Corn Perm Wig for Women 
$34.89 
[B09QQKPZJR] 
Lroveb Beanie Hat Knit with Long Wavy Curly Hair Extensions Wig Winter Warm Fashion Long Curly Hair Hat Wig Wool Curl Corn Perm Curl Knitted Cap Attached Synthetic Hairpiece 
$36.06 
[B08H5DCD65] 
Corn Wave Ponytail Extension Clip in - 22 Inch Long Wavy Curly Wrap Around Pony Tail Heat Resistant Synthetic Hairpiece for Women (Natural Black #1B) 
$9.98 
[B093BKWHFK] 
[B09MFQTNQ5] 
[B09MFJ95ZB] 
[B09C337K8S] 
[B09KL5W7R2] 
[B09PYJFR97] 
[B09PYJTQCK] )
2023-10-10 01:49:08,356 - INFO - {'fixed_0': {'session': 'fixed_0', 'page_type': 'init'}}
2023-10-10 01:49:08,356 - INFO - {'fixed_0': {'session': 'fixed_0', 'page_type': 'init'}}
2023-10-10 01:49:08,478 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, action=search[long clip-in hair extension natural looking], observation=
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B09QQLDJ93] 
Lroveb Fashion Long Curly Wig Head Dyed Black Gradient Golden Long Straight Wig African Long Curly Hair Wigs Ladies Gradient Color Chemical Fiber Silk Corn Perm Wig for Women 
$34.89 
[B09QQKPZJR] 
Lroveb Beanie Hat Knit with Long Wavy Curly Hair Extensions Wig Winter Warm Fashion Long Curly Hair Hat Wig Wool Curl Corn Perm Curl Knitted Cap Attached Synthetic Hairpiece 
$36.06 
[B08H5DCD65] 
Corn Wave Ponytail Extension Clip in - 22 Inch Long Wavy Curly Wrap Around Pony Tail Heat Resistant Synthetic Hairpiece for Women (Natural Black #1B) 
$9.98 
[B093BKWHFK] 
[B09MFQTNQ5] 
[B09MFJ95ZB] 
[B09C337K8S] 
[B09KL5W7R2] 
[B09PYJFR97] 
[B09PYJTQCK] )
2023-10-10 01:49:08,478 - INFO - {'fixed_0': {'session': 'fixed_0', 'page_type': 'init'}}
2023-10-10 01:49:08,478 - INFO - {'fixed_0': {'session': 'fixed_0', 'page_type': 'init'}}
2023-10-10 01:49:08,619 - INFO - NEW NODE: Node(depth=1, value=0.00, visits=0, action=search[long clip-in hair extension natural looking], observation=
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B09QQLDJ93] 
Lroveb Fashion Long Curly Wig Head Dyed Black Gradient Golden Long Straight Wig African Long Curly Hair Wigs Ladies Gradient Color Chemical Fiber Silk Corn Perm Wig for Women 
$34.89 
[B09QQKPZJR] 
Lroveb Beanie Hat Knit with Long Wavy Curly Hair Extensions Wig Winter Warm Fashion Long Curly Hair Hat Wig Wool Curl Corn Perm Curl Knitted Cap Attached Synthetic Hairpiece 
$36.06 
[B08H5DCD65] 
Corn Wave Ponytail Extension Clip in - 22 Inch Long Wavy Curly Wrap Around Pony Tail Heat Resistant Synthetic Hairpiece for Women (Natural Black #1B) 
$9.98 
[B093BKWHFK] 
[B09MFQTNQ5] 
[B09MFJ95ZB] 
[B09C337K8S] 
[B09KL5W7R2] 
[
```

---

### Source 13: `webshop/prompt.py`

**Size:** 17973 bytes  
**Lines:** 442  
**Raw copy:** `raw_prompt_files/webshop/prompt.py`

```python
prompt1 = """Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: think[For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.]
Observation: OK.

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]

{input}
"""


prompt1_feedback = """You are also an advanced reasoning agent that can improve based on self refection. Follow the instruction and purchase an item meeting all of the correct specifications by navigating the website. 
Here is an example:
Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: think[For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.]
Observation: OK.

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]

Here are some previous trials in which you were given access to relevant context and a item to purchase. You were unsuccessful in buying the correct item either because you did not find an item meeting all of the required specifications or because you did not select the correct item. Carefully consider the errors and make sure not to repeat the same mistakes. {trajectories}

{input}
"""

# In[4]:
score_prompt = '''Given an item to purchase and a trajectory that aims to buy an item that exactly matches the specification, which corresponds to the ideal score of 1.0, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Here are some examples

Webshop
Instruction:
i am looking for dairy free and apple variety pack of chips, and price lower than 30.00 dollars
[Search]

Action: search[dairy free and apple variety pack of chips]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B07HRFJWP8]
Enjoy Life Foods Soft Baked Ovals, Breakfast Bars, Nut Free Bars, Soy Free, Dairy Free, Non GMO, Gluten Free, Vegan, Variety Pack, 4 Boxes (20 Bars Total)
$100.0
[B01KMHY5PG]
Enjoy Life Soft Baked Chewy Bars, Variety Pack, Nut Free Bars, Soy Free, Dairy Free, Gluten Free, 6 Boxes (30 Total Bars)
$21.49
[B008D2X8C4]
Enjoy Life Lentil Chips Variety Pack, Dairy Free Chips, Soy Free, Nut Free, Non GMO, Vegan, Gluten Free, 24 Bags (0.8 oz)
$100.0

Action: think[The first two items are not what I want. The third item is the dairy free and apple variety pack of chips I want.]
Observation: OK.

Action: click[B008D2X8C4]
Observation:
[Back to Search]
[< Prev]
flavor name [dill and sour cream][garlic & parmesan][light sea salt][margherita pizza][thai chili lime][variety pack]
size [0.8 ounce (pack of 24)][4 ounce (pack of 12)]
Price: $100.0
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The item has options 'variety pack' and '0.8 ounce (pack of 24)' and seems good to buy.]
Observation: OK.

Action: click[variety pack]
Observation: You have clicked variety pack.

Action: click[0.8 ounce (pack of 24)]
Observation: You have clicked 0.8 ounce (pack of 24).

Action: click[Buy Now]

Reflection: In this attempt, I was unsuccessful. I accidentally bought a product that was $100, which is more than my budget of $30. Either way, the initial search results were not good. Next time, I will do search["variety pack of chips"] and then check if the results meet the dairy free and the $30 budget constraints. I will continue to refine my searches so that I can find more products.
Thus the correctness score is 5

Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.
Reflection: Although the task is not yet complete, the first search is correct and returns relevant results. The thought is also logical and has potential to lead to the correct selection.
Thus the correctness score is 9
{input}
'''

score_prompt_feedback = '''Given an item to purchase and a trajectory, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.
Here are some examples

Webshop
Instruction:
i am looking for dairy free and apple variety pack of chips, and price lower than 30.00 dollars
[Search]

Action: search[dairy free and apple variety pack of chips]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B07HRFJWP8]
Enjoy Life Foods Soft Baked Ovals, Breakfast Bars, Nut Free Bars, Soy Free, Dairy Free, Non GMO, Gluten Free, Vegan, Variety Pack, 4 Boxes (20 Bars Total)
$100.0
[B01KMHY5PG]
Enjoy Life Soft Baked Chewy Bars, Variety Pack, Nut Free Bars, Soy Free, Dairy Free, Gluten Free, 6 Boxes (30 Total Bars)
$21.49
[B008D2X8C4]
Enjoy Life Lentil Chips Variety Pack, Dairy Free Chips, Soy Free, Nut Free, Non GMO, Vegan, Gluten Free, 24 Bags (0.8 oz)
$100.0

Action: think[The first two items are not what I want. The third item is the dairy free and apple variety pack of chips I want.]
Observation: OK.

Action: click[B008D2X8C4]
Observation:
[Back to Search]
[< Prev]
flavor name [dill and sour cream][garlic & parmesan][light sea salt][margherita pizza][thai chili lime][variety pack]
size [0.8 ounce (pack of 24)][4 ounce (pack of 12)]
Price: $100.0
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The item has options 'variety pack' and '0.8 ounce (pack of 24)' and seems good to buy.]
Observation: OK.

Action: click[variety pack]
Observation: You have clicked variety pack.

Action: click[0.8 ounce (pack of 24)]
Observation: You have clicked 0.8 ounce (pack of 24).

Action: click[Buy Now]

Reflection: In this attempt, I was unsuccessful. I accidentally bought a product that was $100, which is more than my budget of $30. Either way, the initial search results were not good. Next time, I will do search["variety pack of chips"] and then check if the results meet the dairy free and the $30 budget constraints. I will continue to refine my searches so that I can find more products.
Thus the correctness score is 5

Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.
Reflection: Although the task is not yet complete, the first search is correct and returns relevant results. The thought is also logical and has potential to lead to the correct selection.
Thus the correctness score is 9
{trajectories}
{input}
'''

# trivial search & item, choose option
prompt1_actonly = """Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]
"""

reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an shopping website and a specific type of item to buy. You were given access to relevant context and a item to purchase. You were unsuccessful in buying the correct item either because you did not find an item meeting all of the required specifications or because you did not select the correct item. The ideal score is 1.0, and anything less is incorrect. In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  
Here are some examples:

Previous Trial
Instruction:
i am looking for dairy free and apple variety pack of chips, and price lower than 30.00 dollars
[Search]

Action: search[dairy free and apple variety pack of chips]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B07HRFJWP8]
Enjoy Life Foods Soft Baked Ovals, Breakfast Bars, Nut Free Bars, Soy Free, Dairy Free, Non GMO, Gluten Free, Vegan, Variety Pack, 4 Boxes (20 Bars Total)
$100.0
[B01KMHY5PG]
Enjoy Life Soft Baked Chewy Bars, Variety Pack, Nut Free Bars, Soy Free, Dairy Free, Gluten Free, 6 Boxes (30 Total Bars)
$21.49
[B008D2X8C4]
Enjoy Life Lentil Chips Variety Pack, Dairy Free Chips, Soy Free, Nut Free, Non GMO, Vegan, Gluten Free, 24 Bags (0.8 oz)
$100.0

Action: think[The first two items are not what I want. The third item is the dairy free and apple variety pack of chips I want.]
Observation: OK.

Action: click[B008D2X8C4]
Observation:
[Back to Search]
[< Prev]
flavor name [dill and sour cream][garlic & parmesan][light sea salt][margherita pizza][thai chili lime][variety pack]
size [0.8 ounce (pack of 24)][4 ounce (pack of 12)]
Price: $100.0
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The item has options 'variety pack' and '0.8 ounce (pack of 24)' and seems good to buy.]
Observation: OK.

Action: click[variety pack]
Observation: You have clicked variety pack.

Action: click[0.8 ounce (pack of 24)]
Observation: You have clicked 0.8 ounce (pack of 24).

Action: click[Buy Now]

STATUS: FAIL

Reflection: In this attempt, I was unsuccessful. I accidentally bought a product that was $100, which is more than my budget of $30. Either way, the initial search results were not good. Next time, I will do search["variety pack of chips"] and then check if the results meet the dairy free and the $30 budget constraints. I will continue to refine my searches so that I can find more products.

Previous Trial
Instruction:
i need gluten free vegetarian smoked peppered bacon - 4 ounce (pack of 2), and price lower than 40.00 dollars
[Search]

Action: search[gluten free vegetarian smoked peppered bacon 4 ounce pack of 2]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B06Y96MXJV]
Smoked Bacon Sea Salt 3-Pack: Smoked Bacon Chipotle, Smoked Bacon and Onion, Smoked Peppered Bacon - All-Natural Sea Salts Slowly Smoked Over Alderwood - No Gluten, No MSG, Non-GMO (12 total oz.)
$29.99
[B06Y96N1KG]
Spicy Hot Pepper Sea Salt 3-Pack: Ghost Pepper, Jalapeno, Habanero - All Natural, Delicious Blends of Peppers & Sea Salt - Gluten-Free, Kosher, No MSG, Non-GMO (12 total oz.)
$29.99
[B07GJTKYJQ]
Louisville Vegan Jerky - 5 Flavor Variety Pack, Non-GMO Soy Protein, Gluten-Free (Black Pepper, Buffalo Dill, Pepperoni, Maple Bacon, and Carolina BBQ, 3 Ounces)
$42.99

Action: think[The first two items are not what I want. The third item is not what I want, but it is the closest one.]
Observation: OK.

Action: click[B07GJTKYJQ]
Observation:
[Back to Search]
[< Prev]
Louisville Vegan Jerky - 5 Flavor Variety Pack, Non-GMO Soy Protein, Gluten-Free (Black Pepper, Buffalo Dill, Pepperoni, Maple Bacon, and Carolina BBQ, 3 Ounces)
Price: $42.99
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The price is too high and it is not what I want.]
Observation: OK.

Action: click[< Prev]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B06Y96MXJV]
Smoked Bacon Sea Salt 3-Pack: Smoked Bacon Chipotle, Smoked Bacon and Onion, Smoked Peppered Bacon - All-Natural Sea Salts Slowly Smoked Over Alderwood - No Gluten, No MSG, Non-GMO (12 total oz.)
$29.99
[B06Y96N1KG]
Spicy Hot Pepper Sea Salt 3-Pack: Ghost Pepper, Jalapeno, Habanero - All Natural, Delicious Blends of Peppers & Sea Salt - Gluten-Free, Kosher, No MSG, Non-GMO (12 total oz.)
$29.99
[B07GJTKYJQ]
Louisville Vegan Jerky - 5 Flavor Variety Pack, Non-GMO Soy Protein, Gluten-Free (Black Pepper, Buffalo Dill, Pepperoni, Maple Bacon, and Carolina BBQ, 3 Ounces)
$42.99

Action: think[The first two items are not what I want.]
Observation: OK.

Action: click[Next >]
Observation: Invalid action!

Action: think[I need to refine my search.]
Observation: OK.

Action: click[< Back to Search]
Observation: Invalid action!

Action: click[Back to Search]

STATUS: FAIL

Reflection: In this attempt, I was unsuccessful. The initial search results were not the products that I was looking for. Next time, I will do search["vegetarian bacon"] for a broader search. I will check that the new results will fulfill the gluten free and 4 ounce pack of 2 constraints. I will continue to refine my searches so that I can find more products.

Previous trial:
{trajectory}
Reflection:'''
```


## Python prompt-building assignments


---

### `hotpot/hotpot.py`

#### Assignment 1: L1 `standard_prompt`
````python
standard_prompt = '''
Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input}
'''
````

#### Assignment 2: L5 `reflection_prompt`
````python
reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  
Here are some examples:
Previous Trial:
Question: The Rome Protocols were signed by three Prime Ministers one of which was assassinated as part of what?
Thought 1: I need to search Rome Protocols, find the three Prime Ministers, then find what they were assassinated as part of.
Action 1: Search[Rome Protocols]
Observation 1: The Rome Protocols were a series of three international agreements concluded in Rome on 17 March 1934 between the governments of Austria, Hungary and Italy. They were signed by Italian Prime Minister Benito Mussolini, Austrian Chancellor Engelbert Dollfuss and Hungarian Prime Minister Gyula Gömbös. All of the protocols went into effect on 12 July 1934 and were registered in League of Nations Treaty Series on 12 December 1934.
Thought 2: The three Prime Ministers were Benito Mussolini, Engelbert Dollfuss, and Gyula Gömbös. I need to search Benito Mussolini and find what he was assassinated as part of.
Action 2: Search[Benito Mussolini]
Observation 2: Benito Amilcare Andrea Mussolini (UK:  MU(U)SS-ə-LEE-nee, US:  MOOSS-, Italian: [beˈniːto aˈmilkare anˈdrɛːa mussoˈliːni]; 29 July 1883 – 28 April 1945) was an Italian politician and journalist who founded and led the National Fascist Party (PNF). He was Prime Minister of Italy from the March on Rome in 1922 until his deposition in 1943, as well as "Duce" of Italian fascism from the establishment of the Italian Fasces of Combat in 1919 until his summary execution in 1945 by Italian partisans. As dictator of Italy and principal founder of fascism, Mussolini inspired and supported the international spread of fascist movements during the inter-war period.Mussolini was originally a socialist politician and a journalist at the Avanti! newspaper. In 1912, he became a member of the National Directorate of the Italian Socialist Party (PSI), but he was expelled from the PSI for advocating military intervention in World War I, in opposition to the party's stance on neutrality. In 1914, Mussolini founded a new journal, Il Popolo d'Italia, and served in the Royal Italian Army during the war until he was wounded and discharged in 1917. Mussolini denounced the PSI, his views now centering on Italian nationalism instead of socialism, and later founded the fascist movement which came to oppose egalitarianism and class conflict, instead advocating "revolutionary nationalism" transcending class lines. On 31 October 1922, following the March on Rome (28–30 October), Mussolini was appointed prime minister by King Victor Emmanuel III, becoming the youngest individual to hold the office up to that time. After removing all political opposition through his secret police and outlawing labor strikes, Mussolini and his followers consolidated power through a series of laws that transformed the nation into a one-party dictatorship. Within five years, Mussolini had established dictatorial authority by both legal and illegal means and aspired to create a totalitarian state. In 1929, Mussolini signed the Lateran Treaty with the Holy See to establish Vatican City.
Mussolini's foreign policy aimed to restore the ancient grandeur of the Roman Empire by expanding Italian colonial possessions and the fascist sphere of influence. In the 1920s, he ordered the Pacification of Libya, instructed the bombing of Corfu over an incident with Greece, established a protectorate over Albania, and incorporated the city of Fiume into the Italian state via agreements with Yugoslavia. In 1936, Ethiopia was conquered following the Second Italo-Ethiopian War and merged into Italian East Africa (AOI) with Eritrea and Somalia. In 1939, Italian forces annexed Albania. Between 1936 and 1939, Mussolini ordered the successful Italian military intervention in Spain in favor of Francisco Franco during the Spanish Civil War. Mussolini's Italy initially tried to avoid the outbreak of a second global war, sending troops at the Brenner Pass to delay Anschluss and taking part in the Stresa Front, the Lytton Report, the Treaty of Lausanne, the Four-Power Pact and the Munich Agreement. However, Italy then alienated itself from Britain and France by aligning with Germany and Japan. Germany invaded Poland on 1 September 1939, resulting in declarations of war by France and the UK and the start of World War II.
On 10 June 1940, Mussolini decided to enter the war on the Axis side. Despite initial success, the subsequent Axis collapse on multiple fronts and eventual Allied invasion of Sicily made Mussolini lose the support of the population and members of the Fascist Party. As a consequence, early on 25 July 1943, the Grand Council of Fascism passed a motion of no confidence in Mussolini; later that day King Victor Emmanuel III dismissed him as head of government and had him placed in custody, appointing Pietro Badoglio to succeed him as Prime Minister. After the king agreed to an armistice with the Allies, on 12 September 1943 Mussolini was rescued from captivity in the Gran Sasso raid by German paratroopers and Waffen-SS commandos led by Major Otto-Harald Mors. Adolf Hitler, after meeting with the rescued former dictator, then put Mussolini in charge of a puppet regime in northern Italy, the Italian Social Republic (Italian: Repubblica Sociale Italiana, RSI), informally known as the Salò Republic, causing a civil war. In late April 1945, in the wake of near total defeat, Mussolini and his mistress Clara Petacci attempted to flee to Switzerland, but both were captured by Italian communist partisans and summarily executed by firing squad on 28 April 1945 near Lake Como. The bodies of Mussolini and his mistress were then taken to Milan, where they were hung upside down at a service station to publicly confirm their demise.
Thought 3: Benito Mussolini was assassinated as part of the collapse of the Axis powers during World War II. So the Rome Protocols were signed by three Prime Ministers one of which was assassinated as part of World War II.
Action 3: Finish[World War II]

Reflection: I searched one of the prime ministers involved in the signing, then attemted to answer right away. I should have searched each of the prime ministers, then looked up 'death' on each of their pages in order to get more information before answering.

Previous Trial:
Question: Kam Heskin plays Paige Morgan in a 2004 film directed by who?
Thought 1: I need to search Kam Heskin and Paige Morgan, find the 2004 film they are in, then find the director of the film.
Action 1: Search[Kam Heskin]
Observation 1: Kam Erika Heskin (born May 8, 1973) is an American actress. She began her career playing Caitlin Deschanel on the NBC daytime soap opera Sunset Beach (1998–1999), before appearing in films Planet of the Apes (2001) and Catch Me If You Can (2002). Heskin went on in 2003 to play Elizabeth Bennet in an independent film Pride & Prejudice: A Latter-Day Comedy, Robin in Charmed (2004),  and Paige Morgan in The Prince and Me film franchise (2006–2010).
Thought 2: Kam Heskin plays Paige Morgan in The Prince and Me film franchise. I need to search The Prince and Me film franchise and find the director of the 2004 film.
Action 2: Search[The Prince and Me film franchise]
Observation 2: Could not find [The Prince and Me film franchise]. Similar: ['Kam Heskin', 'Prince of Persia', 'Harry Potter and the Half-Blood Prince (film)', 'Prince of Persia: The Sands of Time (film)', 'The Chronicles of Narnia (film series)', 'Majestic Prince (franchise)', 'Kingsman (franchise)', 'The Little Prince (2015 film)', 'Shrek (franchise)', 'Harry Potter (film series)']
Thought 3: I need to search The Prince and Me (2004 film) instead.
Action 3: Search[The Prince and Me (2004 film)]
Observation 3: Could not find [The Prince and Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Kam Heskin', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince of Persia', 'Brooklynn Prince', 'Prince (musician)']
Thought 4: I need to search The Prince & Me (2004 film).
Action 4: Search[The Prince & Me (2004 film)]
Observation 4: Could not find [The Prince & Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince (musician)', 'Prince of Persia', 'Kam Heskin', 'Brooklynn Prince']
Thought 5: I need to search The Prince & Me (2004 film) instead.
Action 5: Search[The Prince & Me (2004 film)]
Observation 5: Could not find [The Prince & Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince (musician)', 'Prince of Persia', 'Kam Heskin', 'Brooklynn Prince']
Thought 6: I need to search The Prince & Me (2004 film).
Action 6: Search[The Prince & Me (2004 film)]
Observation 6: Could not find [The Prince & Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince (musician)', 'Prince of Persia', 'Kam Heskin', 'Brooklynn Prince']

Reflection: I got stuck in a loop where I kept trying to search 'The Prince & Me (2004 film)' but the page could not be found. Instead I should have tried to search the similar results that had a similar name to see and they were made in 2004.

Previous Trial:
Question: The Oberoi family is part of a hotel company that has a head office in what city?
Thought 1: I need to search the Oberoi family and find the city where the hotel company's head office is located.
Action 1: Search[Oberoi family]
Observation 1: The Oberoi Group is a luxury hotel group with its head office in New Delhi, India.[2] Founded in 1934, the company owns and operates 32 luxury hotels and two river cruise ships in 7 countries, primarily under its Oberoi Hotels & Resorts and Trident brands.[3] The group also operates The Oberoi Centre for Learning and Development, which is regarded as one of Asia's top institutions for hospitality education.[4]. The foundations of the Oberoi Group date back to 1934 when The Rai Bahadur Mohan Singh Oberoi, the founder of the group, bought two properties: the Maidens in Delhi and the Clarke's in Shimla.[5] In the following years Oberoi, assisted by his two sons, Tilak Raj Singh Oberoi and Prithvi Raj Singh Oberoi (P.R.S. Oberoi
Thought 2: The Oberoi Group has its head office in New Delhi, India. I just need to finish with New Delhi.
Action 2: Finish[New Delhi]
Observation 2: Episode finished, reward = 0

Reflection: I appeared to have retrieved the correct information about The Oberoi Family and the location of it's head office, and provided a corresponding answer. However this answer does not exactly match the ground truth answer so I should try a different wording, such as Delhi.

Previous trial:
{trajectory}Reflection:'''
````

#### Assignment 3: L59 `cot_prompt`
````python
cot_prompt = '''
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron \"Bumblefoot\" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

{input}
'''
````

#### Assignment 4: L104 `cot_prompt_short`
````python
cot_prompt_short = '''
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

{input}
'''
````

#### Assignment 5: L139 `cot_prompt_feedback_short`
````python
cot_prompt_feedback_short = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

You have attempted to answer the following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.

{trajectories}

{input}
'''
````

#### Assignment 6: L177 `cot_prompt_feedback`
````python
cot_prompt_feedback = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron \"Bumblefoot\" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

You have attempted to answer the following question before and failed, either because your reasoning for the answer was incorrect or the phrasing of your response did not exactly match the answer. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.

{trajectories}
When providing the thought and action for the current trial, that into account these failed trajectories and make sure not to repeat the same mistakes and incorrect answers. 

{input}
'''
````

#### Assignment 7: L226 `vote_prompt`
````python
vote_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a list of trajectories, decide which trajectory is most promising. Analyze each trajectory in detail and consider possible errors, then conclude in the last line "The best trajectory is {s}", where s the integer id of the trajectory.
'''
````

#### Assignment 8: L234 `compare_prompt`
````python
compare_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Briefly analyze the correctness of the following two trajectories. Conclude in the last line "The more correct trajectory is 1", "The more correct trajectory is 2", or "The two trajectories are similarly correct".
'''
````

#### Assignment 9: L242 `score_prompt`
````python
score_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.
'''
````

#### Assignment 10: L250 `value_prompt`
````python
value_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
Thus the correctness score is 3

Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?
Thought 1: I need to search for the football manager who recruited David Beckham, and then find out the timeframe in which he managed Manchester United.
Action 1: Search[David Beckham's football manager]
Observation 1: Could not find David Beckham's football manager. Similar: ['David Beckham', 'Inter Miami CF (redirect from Miami Beckham United)', 'Victoria Beckham', 'The Beckham Experiment', 'Miami Freedom Park'].
Thought 2: I couldn't find the information on David Beckham's football manager. I need to search Manchester United and find out the timeframe of the manager.
Action 2: Search[Manchester United]
Observation 2: Manchester United Football Club, commonly referred to as Man United (often stylised as Man Utd), or simply United, is a professional football club based in Old Trafford, Greater Manchester, England. The club competes in the Premier League, the top division in the English football league system. Nicknamed the Red Devils, they were founded as Newton Heath LYR Football Club in 1878, but changed their name to Manchester United in 1902. After a spell playing in Clayton, Manchester, the club moved to their current stadium, Old Trafford, in 1910.. Domestically, Manchester United have won a record 20 league titles, 12 FA Cups, six League Cups and a record 21 FA Community Shields.
Thought 3: The information about David Beckham's football manager is not available. I will search for Manchester United's managers to find the timeframe.
Action 3: Search[Manchester United managers]
Observation 3: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thought 4: The information about David Beckham's football manager is not available. The question asks for the timeframe when the manager managed Manchester United, so I need to find a list of Manchester United managers.
Action 4: Search[list of Manchester United managers]
Observation 4: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thus the correctness score is 4

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
Thus the correctness score is 10

{input}
'''
````

#### Assignment 11: L295 `value_prompt_feedback`
````python
value_prompt_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
Thus the correctness score is 3

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
Thus the correctness score is 10

{trajectories}
Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
Thus the correctness score is 10

{input}
'''
````

#### Assignment 12: L337 `value_prompt_reasoning`
````python
value_prompt_reasoning = '''You are an advanced reasoning agent that can improve based on self refection. Analyze the trajectories of your previous solutions to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
This trajectory is incorrect as my search should be related to Mexican Formula One race car drivers, not winners of the Mexican Grand Prix, a seperate event. A better search would have been for the List of Formula One Grand Prix winners, as suggested.
Thus the correctness score is 3

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
This trajectory is correct as it is reasonable to search for the first magazine provided in the question. It is also better to have simple searches corresponding to a single entity, making this the best action.
Thus the correctness score is 10

Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?
Thought 1: I need to search for the football manager who recruited David Beckham, and then find out the timeframe in which he managed Manchester United.
Action 1: Search[David Beckham's football manager]
Observation 1: Could not find David Beckham's football manager. Similar: ['David Beckham', 'Inter Miami CF (redirect from Miami Beckham United)', 'Victoria Beckham', 'The Beckham Experiment', 'Miami Freedom Park'].
Thought 2: I couldn't find the information on David Beckham's football manager. I need to search Manchester United and find out the timeframe of the manager.
Action 2: Search[Manchester United]
Observation 2: Manchester United Football Club, commonly referred to as Man United (often stylised as Man Utd), or simply United, is a professional football club based in Old Trafford, Greater Manchester, England. The club competes in the Premier League, the top division in the English football league system. Nicknamed the Red Devils, they were founded as Newton Heath LYR Football Club in 1878, but changed their name to Manchester United in 1902. After a spell playing in Clayton, Manchester, the club moved to their current stadium, Old Trafford, in 1910.. Domestically, Manchester United have won a record 20 league titles, 12 FA Cups, six League Cups and a record 21 FA Community Shields.
Thought 3: The information about David Beckham's football manager is not available. I will search for Manchester United's managers to find the timeframe.
Action 3: Search[Manchester United managers]
Observation 3: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thought 4: The information about David Beckham's football manager is not available. The question asks for the timeframe when the manager managed Manchester United, so I need to find a list of Manchester United managers.
Action 4: Search[list of Manchester United managers]
Observation 4: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
This trajectory is mostly incorrect as I was not able to retrieve the relevant information to answer the question. The searches are too broad and not relevant to the specific player recruited, David Beckham. The last two actions are also too similar. It would be better to first search for David Beckham and lookup information related to his manager.
Thus the correctness score is 4

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
This trajectory is correct as all of my thoughts and actions are correct. It makes sense to search for Milhouse first as it is the central subject of the question. It is also correct to directly look up the relevant information in the article, instead of trying another search. 
Thus the correctness score is 10

{input}
'''
````

#### Assignment 13: L397 `value_prompt_reasoning_feedback`
````python
value_prompt_reasoning_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
This trajectory is incorrect as my search should be related to Mexican Formula One race car drivers, not winners of the Mexican Grand Prix, a seperate event. A better search would have been for the List of Formula One Grand Prix winners, as suggested.
Thus the correctness score is 3

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
This trajectory is correct as it is reasonable to search for the first magazine provided in the question. It is also better to have simple searches corresponding to a single entity, making this the best action.
Thus the correctness score is 10

Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?
Thought 1: I need to search for the football manager who recruited David Beckham, and then find out the timeframe in which he managed Manchester United.
Action 1: Search[David Beckham's football manager]
Observation 1: Could not find David Beckham's football manager. Similar: ['David Beckham', 'Inter Miami CF (redirect from Miami Beckham United)', 'Victoria Beckham', 'The Beckham Experiment', 'Miami Freedom Park'].
Thought 2: I couldn't find the information on David Beckham's football manager. I need to search Manchester United and find out the timeframe of the manager.
Action 2: Search[Manchester United]
Observation 2: Manchester United Football Club, commonly referred to as Man United (often stylised as Man Utd), or simply United, is a professional football club based in Old Trafford, Greater Manchester, England. The club competes in the Premier League, the top division in the English football league system. Nicknamed the Red Devils, they were founded as Newton Heath LYR Football Club in 1878, but changed their name to Manchester United in 1902. After a spell playing in Clayton, Manchester, the club moved to their current stadium, Old Trafford, in 1910.. Domestically, Manchester United have won a record 20 league titles, 12 FA Cups, six League Cups and a record 21 FA Community Shields.
Thought 3: The information about David Beckham's football manager is not available. I will search for Manchester United's managers to find the timeframe.
Action 3: Search[Manchester United managers]
Observation 3: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thought 4: The information about David Beckham's football manager is not available. The question asks for the timeframe when the manager managed Manchester United, so I need to find a list of Manchester United managers.
Action 4: Search[list of Manchester United managers]
Observation 4: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
This trajectory is mostly incorrect as I was not able to retrieve the relevant information to answer the question. The searches are too broad and not relevant to the specific player recruited, David Beckham. The last two actions are also too similar. It would be better to first search for David Beckham and lookup information related to his manager.
Thus the correctness score is 4

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
This trajectory is correct as all of my thoughts and actions are correct. It makes sense to search for Milhouse first as it is the central subject of the question. It is also correct to directly look up the relevant information in the article, instead of trying another search. 
Thus the correctness score is 10

{trajectories}

{input}
'''
````

#### Assignment 14: L459 `value_prompt_reasoning_feedback_short`
````python
value_prompt_reasoning_feedback_short = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
This trajectory is incorrect as my search should be related to Mexican Formula One race car drivers, not winners of the Mexican Grand Prix, a seperate event. A better search would have been for the List of Formula One Grand Prix winners, as suggested.
Thus the correctness score is 3

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
This trajectory is correct as all of my thoughts and actions are correct. It makes sense to search for Milhouse first as it is the central subject of the question. It is also correct to directly look up the relevant information in the article, instead of trying another search. 
Thus the correctness score is 10

{trajectories}

{input}
'''
````

#### Assignment 15: L498 `rap_prompt`
````python
rap_prompt = '''
Solve a question answering task with interleaving Thought and Action steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
Provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Thought 2: Then I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Thought 2: I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Thought 2: I can look up "named after" for finding the specific individual Milhouse is named after.
Action 2: Lookup[named after]
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

{input}
'''
````


---

### `hotpot/hotpotqa.py`

#### Assignment 1: L71 `failed_trajectories`
````python
failed_trajectories = "\n".join([f"{question}\n{traj}\n" for traj in z])
````

#### Assignment 2: L72 `failed_trajectories`
````python
failed_trajectories = [f"Question: {traj}" for traj in failed_trajectories.split("Question: ")[1:]]
````

#### Assignment 3: L158 `prompt`
````python
prompt = compare_prompt + f'Action 1:{last_actions[0]}\n\nAction 2:{last_actions[1]}\n'
````

#### Assignment 4: L77 `reflect_prompt`
````python
reflect_prompt = reflection_prompt.format(trajectory=traj)
````

#### Assignment 5: L102 `prompt`
````python
prompt = cot_prompt_feedback.format(trajectories=trajectories, input=input)
````

#### Assignment 6: L187 `prompt`
````python
prompt = value_prompt_reasoning_feedback.format(s="", trajectories=failed_trajectories, input=inp)
````

#### Assignment 7: L192 `failed_trajectories`
````python
failed_trajectories = "\n".join([f"{question}\n{traj}\nThus the correctness score is 1\n" for traj in z])
````

#### Assignment 8: L194 `prompt`
````python
prompt = value_prompt_feedback.format(s="", trajectories=failed_trajectories, input=inp)
````

#### Assignment 9: L205 `prompt`
````python
prompt = value_prompt_reasoning.format(s="", input=inp)
````

#### Assignment 10: L99 `traj_with_reflection`
````python
traj_with_reflection = reflection_mapping['trajectory'] + "FAILED TRAJECTORY\nReflection: " + reflection_mapping['reflection'] + "\n\n"
````

#### Assignment 11: L109 `prompt`
````python
prompt = cot_prompt_feedback_short.format(trajectories=trajectories, input=input)
````

#### Assignment 12: L190 `prompt`
````python
prompt = value_prompt_reasoning_feedback_short.format(s="", trajectories=failed_trajectories, input=inp)
````

#### Assignment 13: L197 `failed_trajectories`
````python
failed_trajectories = "\n".join([f"{question}\n{traj}\nThus the correctness score is 1\n" for traj in z[:2]])
````

#### Assignment 14: L199 `prompt`
````python
prompt = value_prompt_feedback.format(s="", trajectories=failed_trajectories, input=inp)
````

#### Assignment 15: L107 `traj_with_reflection`
````python
traj_with_reflection = reflection_mapping['trajectory'] + "FAILED TRAJECTORY\nReflection: " + reflection_mapping['reflection'] + "\n\n"
````


---

### `hotpot/lats.py`

#### Assignment 1: L32 `value_prompt`
````python
value_prompt = task.value_prompt_wrap(x, y, unique_trajectories, reflection_map)
````

#### Assignment 2: L38 `value_outputs`
````python
value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)
````

#### Assignment 3: L72 `samples`
````python
samples = gpt(prompt, n=n_generate_sample, stop=stop)
````

#### Assignment 4: L305 `sampled_actions`
````python
sampled_actions = get_samples(task, prompt, f"Thought {node.depth + 1}: ", n, prompt_sample=args.prompt_sample, stop="Observation")
````

#### Assignment 5: L355 `child_prompts`
````python
child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]
````

#### Assignment 6: L356 `votes`
````python
votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)
````

#### Assignment 7: L362 `votes`
````python
votes = votes + [0] * (len(node.children) - len(votes))
````

#### Assignment 8: L64 `reflection_map`
````python
reflection_map = task.generate_self_reflection(unique_trajectories, x)
````

#### Assignment 9: L89 `state`
````python
self.state = {'thought': '', 'action': '', 'observation': ''} if state is None else state
````

#### Assignment 10: L199 ``
````python
reward, terminal_node = rollout(max(node.children, key=lambda child: child.value), args, task, idx, max_depth=4)
````

#### Assignment 11: L208 `all_nodes`
````python
all_nodes = [(node, node.value) for node in collect_all_nodes(root)]
````

#### Assignment 12: L288 `child_prompts`
````python
child_prompts = [generate_prompt(child) for child in new_states if not child.is_terminal and child is not None]
````

#### Assignment 13: L313 `thought_line`
````python
thought_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith(f"Thought {node.depth + 1}")), '')
````

#### Assignment 14: L314 `action_line`
````python
action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)
````

#### Assignment 15: L53 `value`
````python
value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)
````

#### Assignment 16: L68 `prompt`
````python
prompt = task.cot_prompt_wrap(x, y, reflection_map)
````

#### Assignment 17: L129 `thought`
````python
thought = line.split(", thought=")[1].split(", action=")[0].strip()
````

#### Assignment 18: L130 `action`
````python
action = line.split(", action=")[1].split(", observation=")[0].strip()
````

#### Assignment 19: L131 `observation`
````python
observation = line.split(", observation=")[1].split(")")[0].strip()
````

#### Assignment 20: L214 `best_node`
````python
best_node = max(terminal_nodes_with_reward_1, key=lambda x: x.value)
````

#### Assignment 21: L291 `values`
````python
values = get_values(task, node.question, child_prompts, args.n_evaluate_sample)
````

#### Assignment 22: L325 `action_type`
````python
action_type = action_line.split('[')[0] if '[' in action_line else action_line
````

#### Assignment 23: L326 `action_param`
````python
action_param = action_line.split('[')[1].split(']')[0] if '[' in action_line else ""
````

#### Assignment 24: L328 ``
````python
obs, r, done, info = step(env, f"{action_type.lower()}[{action_param}]")
````

#### Assignment 25: L335 `new_node`
````python
new_node = Node(state=new_state, question=node.question, parent=node)
````

#### Assignment 26: L397 `value`
````python
node.value = (node.value * (node.visits - 1) + value) / node.visits
````

#### Assignment 27: L391 `value`
````python
node.value = (node.value * (node.visits - 1) + (-1)) / node.visits
````

#### Assignment 28: L394 `value`
````python
node.value = (node.value * (node.visits - 1) + value) / node.visits
````


---

### `hotpot/models.py`

#### Assignment 1: L59 `cost`
````python
cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03
````

#### Assignment 2: L61 `cost`
````python
cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.0015
````

#### Assignment 3: L63 `cost`
````python
cost = completion_tokens / 1000 * 0.004 + prompt_tokens / 1000 * 0.003
````


---

### `hotpot/rap.py`

#### Assignment 1: L20 `value_prompt`
````python
value_prompt = task.value_prompt_wrap(x, y, unique_trajectories, reflection_map)
````

#### Assignment 2: L26 `value_outputs`
````python
value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)
````

#### Assignment 3: L57 `samples`
````python
samples = gpt(prompt, n=n_generate_sample, stop=stop)
````

#### Assignment 4: L250 `sampled_actions`
````python
sampled_actions = get_samples(task, prompt, f"Thought {node.depth + 1}: ", args.n_generate_sample, prompt_sample=args.prompt_sample, stop="Observation")
````

#### Assignment 5: L294 `child_prompts`
````python
child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]
````

#### Assignment 6: L295 `votes`
````python
votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)
````

#### Assignment 7: L301 `votes`
````python
votes = votes + [0] * (len(node.children) - len(votes))
````

#### Assignment 8: L74 `state`
````python
self.state = {'thought': '', 'action': '', 'observation': ''} if state is None else state
````

#### Assignment 9: L189 `all_nodes`
````python
all_nodes = [(node, node.value) for node in collect_all_nodes(root)]
````

#### Assignment 10: L257 `thought_line`
````python
thought_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith(f"Thought {node.depth + 1}")), '')
````

#### Assignment 11: L258 `action_line`
````python
action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)
````

#### Assignment 12: L41 `value`
````python
value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)
````

#### Assignment 13: L53 ``
````python
prompt, reflection_map = task.cot_prompt_wrap(x, y, unique_trajectories)
````

#### Assignment 14: L123 `thought`
````python
thought = line.split(", thought=")[1].split(", action=")[0].strip()
````

#### Assignment 15: L124 `action`
````python
action = line.split(", action=")[1].split(", observation=")[0].strip()
````

#### Assignment 16: L125 `observation`
````python
observation = line.split(", observation=")[1].split(")")[0].strip()
````

#### Assignment 17: L195 `best_node`
````python
best_node = max(terminal_nodes_with_reward_1, key=lambda x: x.value)
````

#### Assignment 18: L268 `action_type`
````python
action_type = action_line.split('[')[0] if '[' in action_line else action_line
````

#### Assignment 19: L269 `action_param`
````python
action_param = action_line.split('[')[1].split(']')[0] if '[' in action_line else ""
````

#### Assignment 20: L270 ``
````python
obs, r, done, info = step(env, f"{action_type.lower()}[{action_param}]")
````

#### Assignment 21: L277 `new_node`
````python
new_node = Node(state=new_state, question=node.question, parent=node)
````

#### Assignment 22: L335 `value`
````python
node.value = (node.value * (node.visits - 1) + value) / node.visits
````

#### Assignment 23: L329 `value`
````python
node.value = (node.value * (node.visits - 1) + value) / node.visits
````

#### Assignment 24: L332 `value`
````python
node.value = (node.value * (node.visits - 1) + (-1)) / node.visits
````


---

### `hotpot/tot.py`

#### Assignment 1: L35 `value_prompt`
````python
value_prompt = task.value_prompt_wrap(x, y, unique_trajectories, reflection_map)
````

#### Assignment 2: L41 `value_outputs`
````python
value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)
````

#### Assignment 3: L72 `samples`
````python
samples = gpt(prompt, n=n_generate_sample, stop=stop)
````

#### Assignment 4: L304 `sampled_actions`
````python
sampled_actions = get_samples(task, prompt, f"Thought {node.depth + 1}: ", args.n_generate_sample, prompt_sample=args.prompt_sample, stop="Observation")
````

#### Assignment 5: L348 `child_prompts`
````python
child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]
````

#### Assignment 6: L349 `votes`
````python
votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)
````

#### Assignment 7: L355 `votes`
````python
votes = votes + [0] * (len(node.children) - len(votes))
````

#### Assignment 8: L89 `state`
````python
self.state = {'thought': '', 'action': '', 'observation': ''} if state is None else state
````

#### Assignment 9: L196 `all_nodes`
````python
all_nodes = [(node, node.value) for node in collect_all_nodes(root)]
````

#### Assignment 10: L243 `all_nodes`
````python
all_nodes = [(node, node.value) for node in collect_all_nodes(root)]
````

#### Assignment 11: L311 `thought_line`
````python
thought_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith(f"Thought {node.depth + 1}")), '')
````

#### Assignment 12: L312 `action_line`
````python
action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)
````

#### Assignment 13: L56 `value`
````python
value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)
````

#### Assignment 14: L138 `thought`
````python
thought = line.split(", thought=")[1].split(", action=")[0].strip()
````

#### Assignment 15: L139 `action`
````python
action = line.split(", action=")[1].split(", observation=")[0].strip()
````

#### Assignment 16: L140 `observation`
````python
observation = line.split(", observation=")[1].split(")")[0].strip()
````

#### Assignment 17: L249 `best_node`
````python
best_node = max(terminal_nodes_with_reward_1, key=lambda x: x.value)
````

#### Assignment 18: L322 `action_type`
````python
action_type = action_line.split('[')[0] if '[' in action_line else action_line
````

#### Assignment 19: L323 `action_param`
````python
action_param = action_line.split('[')[1].split(']')[0] if '[' in action_line else ""
````

#### Assignment 20: L324 ``
````python
obs, r, done, info = step(env, f"{action_type.lower()}[{action_param}]")
````

#### Assignment 21: L331 `new_node`
````python
new_node = Node(state=new_state, question=node.question, parent=node)
````

#### Assignment 22: L389 `value`
````python
node.value = (node.value * (node.visits - 1) + value) / node.visits
````

#### Assignment 23: L383 `value`
````python
node.value = (node.value * (node.visits - 1) + value) / node.visits
````

#### Assignment 24: L386 `value`
````python
node.value = (node.value * (node.visits - 1) + (-1)) / node.visits
````


---

### `hotpot/wikienv.py`

#### Assignment 1: L37 `observation_space, action_space`
````python
self.observation_space = self.action_space = textSpace()
````


---

### `hotpot/wrappers.py`

#### Assignment 1: L59 `normalized_prediction`
````python
normalized_prediction = normalize_answer(prediction)
````

#### Assignment 2: L60 `normalized_ground_truth`
````python
normalized_ground_truth = normalize_answer(ground_truth)
````

#### Assignment 3: L85 `data`
````python
self.data = [(d['question'], d['answer']) for d in self.data]
````

#### Assignment 4: L97 `observation`
````python
observation = f"Question: {self.data[self.data_idx][0]}"
````

#### Assignment 5: L166 `observation`
````python
observation = f"Claim: {self.data[self.data_idx][0]}"
````

#### Assignment 6: L217 `traj`
````python
self.traj = {"observations": [observation], "actions": []}
````

#### Assignment 7: L111 `pred`
````python
pred = normalize_answer(self.data[self.data_idx][1])
````

#### Assignment 8: L119 `pred`
````python
pred = normalize_answer(self.data[self.data_idx][1])
````

#### Assignment 9: L180 `label`
````python
label = normalize_answer(self.data[self.data_idx][1])
````

#### Assignment 10: L36 `observation`
````python
observation = self.env.traj["observations"][0] + "\n"
````


---

### `programming/dfs.py`

#### Assignment 1: L139 `reflection`
````python
reflection = gen.self_reflection(cur_func_impl, feedback, model)
````

#### Assignment 2: L107 `tests_i`
````python
tests_i = gen.internal_tests(item["prompt"], model, 6)
````

#### Assignment 3: L110 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(item["prompt"], model, "simple")
````

#### Assignment 4: L160 `new_solution`
````python
new_solution = gen.func_impl(
                    func_sig=item["prompt"],
                    model=model,
                    strategy="simple",
                    prev_func_impl=prev_func_impl,
                    feedback=feedback,
                    self_reflection=reflection,
                    acc_feedback = acc_feedback,
                    acc_reflection = acc_reflection
                )
````

#### Assignment 5: L177 `reflection`
````python
reflection = gen.self_reflection(child.solution, feedback_internal, model)
````

#### Assignment 6: L188 `passed_section`
````python
passed_section = feedback_internal.split("Tests failed:")[0]
````


---

### `programming/executors/go_executor.py`

#### Assignment 1: L332 `test_compiletime`
````python
test_compiletime = r"""
# go-lats-35116-6739b2903daabf6d
.\lats.go:10:7: undefined: math
.\lats.go:11:18: too many return values
        have (bool, bool)
        want (bool)
.\lats.go:15:16: too many return values
        have (bool, bool)
        want (bool)
    """
````


---

### `programming/executors/leet_executor.py`

#### Assignment 1: L37 `submission`
````python
submission = LeetCodeSubmission(
            code=leetcode_formatted_func,
            lang=self.lang,
            question_id=id_from_slug(name, self.env.api_instance),
            question_slug=name,
            timeout=timeout
        )
````


---

### `programming/executors/rs_executor.py`

#### Assignment 1: L363 `test_compiletime`
````python
test_compiletime = r"""
    {"reason":"compiler-message","package_id":"testing 0.1.0 (path+file:///home/elleven/Downloads/testing)","manifest_path":"/home/elleven/Downloads/testing/Cargo.toml","target":{"kind":["bin"],"crate_types":["bin"],"name":"testing","src_path":"/home/elleven/Downloads/testing/src/main.rs","edition":"2021","doc":true,"doctest":false,"test":true},"message":{"rendered":"error[E0282]: type annotations needed\n --> src/main.rs:2:9\n  |\n2 |     let sakfsdfjfndslv;\n  |         ^^^^^^^^^^^^^^\n  |\nhelp: consider giving `sakfsdfjfndslv` an explicit type\n  |\n2 |     let sakfsdfjfndslv: _;\n  |                       +++\n\n","children":[{"children":[],"code":null,"level":"help","message":"consider giving `sakfsdfjfndslv` an explicit type","rendered":null,"spans":[{"byte_end":34,"byte_start":34,"column_end":23,"column_start":23,"expansion":null,"file_name":"src/main.rs","is_primary":true,"label":null,"line_end":2,"line_start":2,"suggested_replacement":": _","suggestion_applicability":"HasPlaceholders","text":[{"highlight_end":23,"highlight_start":23,"text":"    let sakfsdfjfndslv;"}]}]}],"code":{"code":"E0282","explanation":"The compiler could not infer a type and asked for a type annotation.\n\nErroneous code example:\n\n```compile_fail,E0282\nlet x = \"hello\".chars().rev().collect();\n```\n\nThis error indicates that type inference did not result in one unique possible\ntype, and extra information is required. In most cases this can be provided\nby adding a type annotation. Sometimes you need to specify a generic type\nparameter manually.\n\nA common example is the `collect` method on `Iterator`. It has a generic type\nparameter with a `FromIterator` bound, which for a `char` iterator is\nimplemented by `Vec` and `String` among others. Consider the following snippet\nthat reverses the characters of a string:\n\nIn the first code example, the compiler cannot infer what the type of `x` should\nbe: `Vec<char>` and `String` are both suitable candidates. To specify which type\nto use, you can use a type annotation on `x`:\n\n```\nlet x: Vec<char> = \"hello\".chars().rev().collect();\n```\n\nIt is not necessary to annotate the full type. Once the ambiguity is resolved,\nthe compiler can infer the rest:\n\n```\nlet x: Vec<_> = \"hello\".chars().rev().collect();\n```\n\nAnother way to provide the compiler with enough information, is to specify the\ngeneric type parameter:\n\n```\nlet x = \"hello\".chars().rev().collect::<Vec<char>>();\n```\n\nAgain, you need not specify the full type if the compiler can infer it:\n\n```\nlet x = \"hello\".chars().rev().collect::<Vec<_>>();\n```\n\nApart from a method or function with a generic type parameter, this error can\noccur when a type parameter of a struct or trait cannot be inferred. In that\ncase it is not always possible to use a type annotation, because all candidates\nhave the same return type. For instance:\n\n```compile_fail,E0282\nstruct Foo<T> {\n    num: T,\n}\n\nimpl<T> Foo<T> {\n    fn bar() -> i32 {\n        0\n    }\n\n    fn baz() {\n        let number = Foo::bar();\n    }\n}\n```\n\nThis will fail because the compiler does not know which instance of `Foo` to\ncall `bar` on. Change `Foo::bar()` to `Foo::<T>::bar()` to resolve the error.\n"},"level":"error","message":"type annotations needed","spans":[{"byte_end":34,"byte_start":20,"column_end":23,"column_start":9,"expansion":null,"file_name":"src/main.rs","is_primary":true,"label":null,"line_end":2,"line_start":2,"suggested_replacement":null,"suggestion_applicability":null,"text":[{"highlight_end":23,"highlight_start":9,"text":"    let sakfsdfjfndslv;"}]}]}}
    {"reason":"compiler-message","package_id":"testing 0.1.0 (path+file:///home/elleven/Downloads/testing)","manifest_path":"/home/elleven/Downloads/testing/Cargo.toml","target":{"kind":["bin"],"crate_types":["bin"],"name":"testing","src_path":"/home/elleven/Downloads/testing/src/main.rs","edition":"2021","doc":true,"doctest":false,"test":true},"message":{"rendered":"error: aborting due to previous error\n\n","children":[],"code":null,"level":"error","message":"aborting due to previous error","spans":[]}}
    {"reason":"compiler-message","package_id":"testing 0.1.0 (path+file:///home/elleven/Downloads/testing)","manifest_path":"/home/elleven/Downloads/testing/Cargo.toml","target":{"kind":["bin"],"crate_types":["bin"],"name":"testing","src_path":"/home/elleven/Downloads/testing/src/main.rs","edition":"2021","doc":true,"doctest":false,"test":true},"message":{"rendered":"For more information about this error, try `rustc --explain E0282`.\n","children":[],"code":null,"level":"failure-note","message":"For more information about this error, try `rustc --explain E0282`.","spans":[]}}
    {"reason":"build-finished","success":false}
    """
````


---

### `programming/generators/generator_utils.py`

#### Assignment 1: L128 `accumulated_context`
````python
accumulated_context = "\n\n".join(
        [f"[previous impl {i+1}]:\n{add_code_block(impl)}\n[unit test results from previous impl {i+1}]:\n{feedback}\n[reflection on previous impl {i+1}]:\n{reflection}" 
         for i, (impl, feedback, reflection) in enumerate(zip(prev_func_impl, accumulated_feedback, accumulated_reflection))]
    )
````

#### Assignment 2: L220 `prompt`
````python
prompt = f'{test_generation_completion_instruction}\n\nfunc signature:\n{func_sig}\nunit tests:'
````

#### Assignment 3: L264 `reflection`
````python
reflection = model.generate(
            f'{self_reflection_completion_instruction}\n{add_code_block(func)}\n\n{feedback}\n\nExplanation:')
````

#### Assignment 4: L34 `message`
````python
message = f"{reflection_few_shot}\n[previous impl]:\n{add_code_block(prev_func_impl)}\n\n[unit test results from previous impl]:\n{feedback}\n\n[reflection on previous impl]:\n{self_reflection}\n\n[improved impl]:\n{func_sig}"
````

#### Assignment 5: L35 `prompt`
````python
prompt = f"{reflection_chat_instruction}\n{code_block_instruction}"
````

#### Assignment 6: L38 `messages`
````python
messages = [
                Message(
                    role="system",
                    content=prompt,
                ),
                Message(
                    role="user", # TODO: check this
                    content=reflection_few_shot,
                ),
                Message(
                    role="assistant",
                    content=add_code_block(prev_func_impl),
                ),
                Message(
                    role="user",
                    content=f"[unit test results from previous impl]:\n{feedback}\n\n[reflection on previous impl]:",
                ),
                Message(
                    role="assistant",
                    content=self_reflection,
                ),
                Message(
                    role="user",
                    content=f"[improved impl]:\n{func_sig}",
                ),
            ]
````

#### Assignment 7: L66 `system_prompt`
````python
system_prompt = f"{simple_chat_instruction}\n{code_block_instruction}"
````

#### Assignment 8: L68 `messages`
````python
messages = [
                Message(
                    role="system",
                    content=f"{simple_chat_instruction}\n{code_block_instruction}",
                ),
                Message(
                    role="user",
                    content=func_sig,
                ),
            ]
````

#### Assignment 9: L81 `prompt`
````python
prompt = f"{reflection_completion_instruction}\n{add_code_block(prev_func_impl)}\n\nunit tests:\n{feedback}\n\nhint:\n{self_reflection}\n\n# improved implementation\n{func_sig}\n{code_block_instruction}"
````

#### Assignment 10: L82 `func_bodies`
````python
func_bodies = model.generate(
                prompt, num_comps=num_comps, temperature=temperature)
````

#### Assignment 11: L85 `prompt`
````python
prompt = f"{simple_completion_instruction}\n{func_sig}\n{code_block_instruction}"
````

#### Assignment 12: L86 `func_bodies`
````python
func_bodies = model.generate(
                prompt, num_comps=num_comps, temperature=temperature)
````

#### Assignment 13: L136 `messages`
````python
messages = [
                Message(role="system", content=f"{reflection_chat_instruction}\n{code_block_instruction}"),
                Message(role="user", content=reflection_few_shot)
            ]
````

#### Assignment 14: L146 `prompt`
````python
prompt = "\n".join([message.content for message in messages])
````

#### Assignment 15: L147 `message`
````python
message = (f"{reflection_few_shot}\n{accumulated_context}\n\n[improved impl]:\n{func_sig}")
````

#### Assignment 16: L152 `system_prompt`
````python
system_prompt = f"{simple_chat_instruction}\n{code_block_instruction}"
````

#### Assignment 17: L154 `messages`
````python
messages = [
                Message(role="system", content=f"{simple_chat_instruction}\n{code_block_instruction}"),
                Message(role="user", content=func_sig)
            ]
````

#### Assignment 18: L161 `prompt`
````python
prompt = f"{reflection_completion_instruction}\n{accumulated_context}\n\n# improved implementation\n{func_sig}\n{code_block_instruction}"
````

#### Assignment 19: L162 `func_bodies`
````python
func_bodies = model.generate(prompt, num_comps=num_comps, temperature=temperature)
````

#### Assignment 20: L165 `prompt`
````python
prompt = f"{simple_completion_instruction}\n{func_sig}\n{code_block_instruction}"
````

#### Assignment 21: L166 `func_bodies`
````python
func_bodies = model.generate(prompt, num_comps=num_comps, temperature=temperature)
````

#### Assignment 22: L195 `messages`
````python
messages = [
                Message(
                    role="system",
                    content=test_generation_chat_instruction,
                ),
                Message(
                    role="user",
                    content=f"{test_generation_few_shot}\n\n[func signature]:\n{func_sig}\n\n[think]:"
                )
            ]
````

#### Assignment 23: L208 `messages`
````python
messages = [
                Message(
                    role="system",
                    content=f"{test_generation_chat_instruction}\n\n{test_generation_few_shot}",
                ),
                Message(
                    role="user",
                    content=f"[func signature]:\n{func_sig}\n\n[unit tests]:",
                )
            ]
````

#### Assignment 24: L239 `messages`
````python
messages = [
                Message(
                    role="system",
                    content=self_reflection_chat_instruction,
                ),
                Message(
                    role="user",
                    content=f'{self_reflection_few_shot}\n\n[function impl]:\n{add_code_block(func)}\n\n[unit test results]:\n{feedback}\n\n[self-reflection]:',
                )
            ]
````

#### Assignment 25: L249 `reflection`
````python
reflection = model.generate_chat(messages=messages)
````

#### Assignment 26: L252 `messages`
````python
messages = [
                Message(
                    role="system",
                    content=self_reflection_chat_instruction,
                ),
                Message(
                    role="user",
                    content=f'[function impl]:\n{add_code_block(func)}\n\n[unit test results]:\n{feedback}\n\n[self-reflection]:',
                )
            ]
````

#### Assignment 27: L262 `reflection`
````python
reflection = model.generate_chat(messages=messages)
````


---

### `programming/generators/go_generate.py`

#### Assignment 1: L9 `GO_SIMPLE_COMPLETION_INSTRUCTION`
````python
GO_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."
````

#### Assignment 2: L10 `GO_REFLECTION_COMPLETION_INSTRUCTION`
````python
GO_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"
````

#### Assignment 3: L11 `GO_SELF_REFLECTION_COMPLETION_INSTRUCTION`
````python
GO_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation.\n\n-----"
````

#### Assignment 4: L12 `USE_GO_CODEBLOCK_INSTRUCTION`
````python
USE_GO_CODEBLOCK_INSTRUCTION = "Use a Go code block to write your response. For example:\n```go\nfunc main() {\n    fmt.Println(\"Hello, World!\")\n}\n```"
````

#### Assignment 5: L14 `GO_SIMPLE_CHAT_INSTRUCTION`
````python
GO_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Go code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."
````

#### Assignment 6: L15 `GO_REFLECTION_CHAT_INSTRUCTION`
````python
GO_REFLECTION_CHAT_INSTRUCTION = "You are an AI Go assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."
````

#### Assignment 7: L16 `GO_SELF_REFLECTION_CHAT_INSTRUCTION`
````python
GO_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Go programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation."
````

#### Assignment 8: L18 `GO_REFLECTION_FEW_SHOT_ADD`
````python
GO_REFLECTION_FEW_SHOT_ADD = '''Example 1:
[previous impl]:
```go
func add(a, b int) int {
    // Given integers a and b, return the total value of a and b.
	return a - b
}
```

[unit test results from previous impl]:
Tested passed:

Tests failed:
lats_test.go:49: add(1, 2) = -1, want 3
lats_test.go:49: add(2, 3) = -1, want 5

[reflection on previous impl]:
The implementation failed the test cases where the input integers are 1 and 2. The issue arises because the code does not add the two integers together, but instead subtracts the second integer from the first. To fix this issue, we should change the operator from `-` to `+` in the return statement. This will ensure that the function returns the correct output for the given input.

[improved impl]:
```Go
func add(a, b int) int {
    // Given integers a and b, return the total value of a and b.
    return a + b
}
```

END EXAMPLES
'''
````

#### Assignment 9: L48 `GO_TEST_GENERATION_FEW_SHOT`
````python
GO_TEST_GENERATION_FEW_SHOT = """For example:

func signature:
/// Add three numbers together.
/// This function takes three numbers as input and returns the sum of the three numbers.
func Add3Numbers(x int, y int, z int) int {

unit tests:
func TestAdd(t *testing.T) {
    assert := assert.New(t)
    assert.Equal(7, Add3Numbers(2, 3+rand.Intn(1000)*0, 2))
    assert.Equal(15, Add3Numbers(5, 7, 3))
}
"""
````

#### Assignment 10: L63 `GO_SELF_REFLECTION_FEW_SHOT`
````python
GO_SELF_REFLECTION_FEW_SHOT = '''Example 1:
[function impl]:
```Go
func SortArray(array []int) []int {
// Given an array of non-negative integers, return a copy of the given array after sorting,
// you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
// or sort it in descending order if the sum( first index value, last index value) is even.
// 
// Note:
// * don't change the given array.
// 
// Examples:
// * SortArray([]) => []
// * SortArray([5]) => [5]
// * SortArray([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
// * SortArray([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]

func SortArray(array []int) []int {
	arr := make([]int, len(array))
	copy(arr, array)
	if len(arr) == 0 {
		return arr
	}
	if (arr[0]+arr[len(arr)-1])%2 == 0 {
		sort.Slice(arr, func(i, j int) bool {
			return arr[i] > arr[j]
		})
	} else {
		sort.Slice(arr, func(i, j int) bool {
			return arr[i] < arr[j]
		})
	}
	return arr
}
```

[unit test results]:
Tested passed:
func TestSortArray(t *testing.T) {
    assert := assert.New(t)
    assert.Equal([]int{}, SortArray([]int{}), \"Error\")
}
func TestSortArray(t *testing.T) {
    assert := assert.New(t)
    assert.Equal([]int{5}, SortArray([]int{5}), \"Error\")
}

Tests failed:
func TestSortArray(t *testing.T) {\n    assert := assert.New(t)\n    assert.Equal([]int{5, 4, 3, 2, 1, 0}, SortArray([]int{2, 4, 3, 0, 1, 5}), \"Error\")\n}\n # output:  []int{0, 1, 2, 3, 4, 5}, []int{5, 4, 3, 2, 1, 0}

[self-reflection]:
The implementation failed to sort the array correctly. It sorted the array in ascending order, when it needed to do it in descending order, which is not the intended behavior. The issue lies in using the sum of the first index value and the last index value as the key select if the order is ascending or descending, rather than always doing it ascending. To overcome this error, I should verify the value of the sum of the first index value and the last index value before sorting. This will ensure that the array will be sorted in the correct order, which is the desired output. Next time I approach the problem, I will make sure to use the correct sum of indexes.

END EXAMPLES

'''
````

#### Assignment 11: L119 `GO_TEST_GENERATION_COMPLETION_INSTRUCTION`
````python
GO_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring. You only responds with Go code, NOT ENGLISH.

{GO_TEST_GENERATION_FEW_SHOT}"""
````

#### Assignment 12: L123 `GO_TEST_GENERATION_CHAT_INSTRUCTION`
````python
GO_TEST_GENERATION_CHAT_INSTRUCTION = """You are a Go programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""
````


---

### `programming/generators/model.py`

#### Assignment 1: L11 `MessageRole`
````python
MessageRole = Literal["system", "user", "assistant"]
````

#### Assignment 2: L37 `response`
````python
response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=stop_strs,
        n=num_comps,
    )
````

#### Assignment 3: L204 `DEFAULT_SYSTEM_PROMPT`
````python
DEFAULT_SYSTEM_PROMPT = """\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""
````

#### Assignment 4: L139 `outputs`
````python
outputs = self.model.generate(
            prompt,
            max_new_tokens=min(
                max_tokens, self.model.config.max_position_embeddings),
            use_cache=True,
            do_sample=True,
            temperature=temperature,
            top_p=0.95,
            eos_token_id=self.eos_token_id,
            num_return_sequences=num_comps,
        )
````

#### Assignment 5: L240 `messages_tokens`
````python
messages_tokens: List[int] = sum(
            [
                self.tokenizer.encode(
                    f"{self.B_INST} {(prompt.content).strip()} {self.E_INST} {(answer.content).strip()} ",
                )
                for prompt, answer in zip(
                    messages[::2],
                    messages[1::2],
                )
            ],
            [],
        )
````

#### Assignment 6: L227 `messages`
````python
messages = [
                Message(role="system", content=self.DEFAULT_SYSTEM_PROMPT)
            ] + messages
````


---

### `programming/generators/parse.py`

#### Assignment 1: L77 `CODE`
````python
CODE = """def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    \"\"\"
    Write a function that accepts two lists of strings and returns the list that has
    total number of chars in the all strings of the list less than the other list.
    
    if the two lists have the same number of chars, return the first list.
    
    Examples
    >>> total_match([], [])
    []
    >>> total_match(['hi', 'admin'], ['hI', 'Hi'])
    ['hI', 'Hi']
    >>> total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    ['hi', 'admin']
    >>> total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
    ['hI', 'hi', 'hi']
    >>> total_match(['4'], ['1', '2', '3', '4', '5'])
    ['4']
    \"\"\"
    total_chars_lst1 = sum(len(word) for word in lst1)
    total_chars_lst2 = sum(len(word) for word in lst2)
    
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst1 > total_chars_lst2:
        return lst2
    else:
        return lst1
    """
````


---

### `programming/generators/py_generate.py`

#### Assignment 1: L10 `PY_SIMPLE_COMPLETION_INSTRUCTION`
````python
PY_SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."
````

#### Assignment 2: L11 `PY_REFLEXION_COMPLETION_INSTRUCTION`
````python
PY_REFLEXION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"
````

#### Assignment 3: L12 `PY_SELF_REFLECTION_COMPLETION_INSTRUCTION`
````python
PY_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Python writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation.\n\n-----"
````

#### Assignment 4: L13 `USE_PYTHON_CODEBLOCK_INSTRUCTION`
````python
USE_PYTHON_CODEBLOCK_INSTRUCTION = "Use a Python code block to write your response. For example:\n```python\nprint('Hello world!')\n```"
````

#### Assignment 5: L15 `PY_SIMPLE_CHAT_INSTRUCTION`
````python
PY_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with python code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."
````

#### Assignment 6: L16 `PY_SIMPLE_CHAT_INSTRUCTION_V2`
````python
PY_SIMPLE_CHAT_INSTRUCTION_V2 = "You are an AI that only responds with only python code. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."
````

#### Assignment 7: L17 `PY_REFLEXION_CHAT_INSTRUCTION`
````python
PY_REFLEXION_CHAT_INSTRUCTION = "You are an AI Python assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."
````

#### Assignment 8: L18 `PY_REFLEXION_CHAT_INSTRUCTION_V2`
````python
PY_REFLEXION_CHAT_INSTRUCTION_V2 = "You are an AI Python assistant. You will be given your previous implementation of a function, a series of unit tests results, and your self-reflection on your previous implementation. Write your full implementation (restate the function signature)."
````

#### Assignment 9: L19 `PY_REFLEXION_FEW_SHOT_ADD`
````python
PY_REFLEXION_FEW_SHOT_ADD = '''Example 1:
[previous impl]:
```python
def add(a: int, b: int) -> int:
    """
    Given integers a and b, return the total value of a and b.
    """
    return a - b
```

[unit test results from previous impl]:
Tested passed:

Tests failed:
assert add(1, 2) == 3 # output: -1
assert add(1, 2) == 4 # output: -1

[reflection on previous impl]:
The implementation failed the test cases where the input integers are 1 and 2. The issue arises because the code does not add the two integers together, but instead subtracts the second integer from the first. To fix this issue, we should change the operator from `-` to `+` in the return statement. This will ensure that the function returns the correct output for the given input.

[improved impl]:
```python
def add(a: int, b: int) -> int:
    """
    Given integers a and b, return the total value of a and b.
    """
    return a + b
```
'''
````

#### Assignment 10: L49 `PY_REFLEXION_FEW_SHOT`
````python
PY_REFLEXION_FEW_SHOT = '''Example 1:
[previous impl]:
```python
from typing import *
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    """
    Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly maxWidth characters.
    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
    For the last line of text, it should be left justified and no extra space is inserted between words.
    Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array `words` contains at least one word.
    """
    res = []
    cur_line = []
    cur_len = 0

    for word in words:
        if cur_len + len(word) + len(cur_line) > maxWidth:
            if len(cur_line) == 1:
                res.append(cur_line[0] + ' ' * (maxWidth - cur_len))
            else:
                spaces = maxWidth - cur_len
                space_between = spaces // (len(cur_line) - 1)
                extra_spaces = spaces % (len(cur_line) - 1)
                line = ''
                for i, w in enumerate(cur_line[:-1]):
                    line += w + ' ' * (space_between + (i < extra_spaces))
                line += cur_line[-1]
                res.append(line)
            cur_line = []
            cur_len = 0
        cur_line.append(word)
        cur_len += len(word)

    last_line = ' '.join(cur_line)
    last_line += ' ' * (maxWidth - len(last_line))
    res.append(last_line)

    return res
```

[unit test results from previous impl]:
Tested passed:

Tests failed:
assert fullJustify([], 10) == [] # output: ['          ']
assert fullJustify([], 0) == [] # output: ['']

[reflection on previous impl]:
The implementation failed the test cases where the input list of words is empty. The issue arises because the code does not handle the case where there are no words to process. As a result, it still appends a line with spaces to the result list, even when there are no words. To fix this issue, we should add a condition at the beginning of the function to check if the input list is empty, and return an empty list if it is. This will ensure that the function returns the correct output for empty input lists.

[improved impl]:
```python
from typing import *
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    """
    Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly maxWidth characters.
    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
    For the last line of text, it should be left justified and no extra space is inserted between words.
    Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array `words` contains at least one word.
    """
    if not words:
        return []

    res = []
    cur_line = []
    cur_len = 0

    for word in words:
        if cur_len + len(word) + len(cur_line) > maxWidth:
            if len(cur_line) == 1:
                res.append(cur_line[0] + ' ' * (maxWidth - cur_len))
            else:
                spaces = maxWidth - cur_len
                space_between = spaces // (len(cur_line) - 1)
                extra_spaces = spaces % (len(cur_line) - 1)
                line = ''
                for i, w in enumerate(cur_line[:-1]):
                    line += w + ' ' * (space_between + (i < extra_spaces))
                line += cur_line[-1]
                res.append(line)
            cur_line = []
            cur_len = 0
        cur_line.append(word)
        cur_len += len(word)

    last_line = ' '.join(cur_line)
    last_line += ' ' * (maxWidth - len(last_line))
    res.append(last_line)

    return res
```
END EXAMPLES

'''
````

#### Assignment 11: L151 `PY_SELF_REFLECTION_CHAT_INSTRUCTION`
````python
PY_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Python programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation."
````

#### Assignment 12: L152 `PY_SELF_REFLECTION_CHAT_INSTRUCTION_V2`
````python
PY_SELF_REFLECTION_CHAT_INSTRUCTION_V2 = "You are a Python programming assistant. You will be given a function implementation and a series of unit test results. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as guidance when you try again later. Only provide the few sentence description in your answer, not the implementation. You will be given a few examples by the user."
````

#### Assignment 13: L153 `PY_SELF_REFLECTION_FEW_SHOT`
````python
PY_SELF_REFLECTION_FEW_SHOT = """Example 1:
[function impl]:
```python
def longest_subarray_with_sum_limit(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left, right = 0, 0
    max_length = 0
    current_sum = 0
    result = []
    while right < n:
        current_sum += nums[right]
        while current_sum > target:
            current_sum -= nums[left]
            left += 1
        if right - left + 1 >= max_length:
            max_length = right - left + 1
            result = nums[left:right+1]
        right += 1
    return result
```
[unit test results]:
Tests passing:
assert longest_subarray_with_sum_limit([1, 2, 3, 4, 5], 8) == [1, 2, 3]
assert longest_subarray_with_sum_limit([1, 2, 3, 4, 5], 15) == [1, 2, 3, 4, 5]
assert longest_subarray_with_sum_limit([1, -1, 2, -2, 3, -3], 2) == [1, -1, 2, -2, 3]
assert longest_subarray_with_sum_limit([], 10) == []
assert longest_subarray_with_sum_limit([], 0) == []
assert longest_subarray_with_sum_limit([], -5) == []  
Tests failing:
assert longest_subarray_with_sum_limit([5, 6, 7, 8, 9], 4) == [] # output: [5]
[self-reflection]:
The implementation failed the where no subarray fulfills the condition. The issue in the implementation is due to the use of >= instead of > in the condition to update the result. Because of this, it returns a subarray even when the sum is greater than the target, as it still updates the result when the current subarray length is equal to the previous longest subarray length. To overcome this error, we should change the condition to only update the result when the current subarray length is strictly greater than the previous longest subarray length. This can be done by replacing >= with > in the condition.

Example 2:
[function impl]:
```python
def longest_subarray_with_sum_limit(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left, right = 0, 0
    max_length = 0
    current_sum = 0
    result = []
    while current_sum + nums[right] <= target:
        current_sum += nums[right]
        right += 1
    while right < n:
        current_sum += nums[right]
        while current_sum > target:
            current_sum -= nums[left]
            left += 1
        if right - left + 1 > max_length:
            max_length = right - left + 1
            result = nums[left:right+1]
        right += 1
    return result
```
[unit test results]:
Tests passing:
assert longest_subarray_with_sum_limit([], 10) == []
assert longest_subarray_with_sum_limit([], 0) == []
assert longest_subarray_with_sum_limit([], -5) == []
Tests failing:
assert longest_subarray_with_sum_limit([1, 2, 3, 4, 5], 8) == [1, 2, 3] # output: list index out of range
assert longest_subarray_with_sum_limit([1, 2, 3, 4, 5], 15) == [1, 2, 3, 4, 5] # output: list index out of range
assert longest_subarray_with_sum_limit([5, 6, 7, 8, 9], 4) == [] # output: list index out of range
assert longest_subarray_with_sum_limit([1, -1, 2, -2, 3, -3], 2) == [1, -1, 2, -2, 3] # output: list index out of range
[self-reflection]:
The implementation failed 4 out of the 7 test cases due to an IndexError. The issue stems from the while loop while current_sum + nums[right] <= target:, which directly accesses nums[right] without checking if right is within the bounds of the list. This results in a runtime error when right goes beyond the list length. To overcome this error, we need to add a bounds check for the right variable in the mentioned while loop. We can modify the loop condition to while right < len(nums) and current_sum + nums[right] <= target:. This change will ensure that we only access elements within the bounds of the list, thus avoiding the IndexError.
END OF EXAMPLES
"""
````

#### Assignment 14: L224 `PY_TEST_GENERATION_FEW_SHOT`
````python
PY_TEST_GENERATION_FEW_SHOT = """Examples:
func signature:
def add3Numbers(x, y, z):
    \"\"\" Add three numbers together.
    This function takes three numbers as input and returns the sum of the three numbers.
    \"\"\"
unit tests:
assert add3Numbers(1, 2, 3) == 6
assert add3Numbers(-1, 2, 3) == 4
assert add3Numbers(1, -2, 3) == 2
assert add3Numbers(1, 2, -3) == 0
assert add3Numbers(-3, -2, -1) == -6
assert add3Numbers(0, 0, 0) == 0
"""
````

#### Assignment 15: L239 `PY_TEST_GENERATION_COMPLETION_INSTRUCTION`
````python
PY_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring.

{PY_TEST_GENERATION_FEW_SHOT}"""
````

#### Assignment 16: L243 `PY_TEST_GENERATION_CHAT_INSTRUCTION`
````python
PY_TEST_GENERATION_CHAT_INSTRUCTION = """You are an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""
````


---

### `programming/generators/rs_generate.py`

#### Assignment 1: L8 `RS_SIMPLE_COMPLETION_INSTRUCTION`
````python
RS_SIMPLE_COMPLETION_INSTRUCTION = "// Write the body of this function only."
````

#### Assignment 2: L9 `RS_REFLEXION_COMPLETION_INSTRUCTION`
````python
RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature).\n\n-----"
````

#### Assignment 3: L10 `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION`
````python
RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust writing assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation.\n\n-----"
````

#### Assignment 4: L11 `USE_RUST_CODEBLOCK_INSTRUCTION`
````python
USE_RUST_CODEBLOCK_INSTRUCTION = "Use a Rust code block to write your response. For example:\n```rust\nfn main() {\n    println!(\"Hello\");\n}\n```"
````

#### Assignment 5: L13 `RS_SIMPLE_CHAT_INSTRUCTION`
````python
RS_SIMPLE_CHAT_INSTRUCTION = "You are an AI that only responds with Rust code, NOT ENGLISH. You will be given a function signature and its docstring by the user. Write your full implementation (restate the function signature)."
````

#### Assignment 6: L14 `RS_REFLEXION_CHAT_INSTRUCTION`
````python
RS_REFLEXION_CHAT_INSTRUCTION = "You are an AI Rust assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Write your full implementation (restate the function signature)."
````

#### Assignment 7: L15 `RS_SELF_REFLECTION_CHAT_INSTRUCTION`
````python
RS_SELF_REFLECTION_CHAT_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation."
````

#### Assignment 8: L17 `RS_REFLEXION_COMPLETION_INSTRUCTION`
````python
RS_REFLEXION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given your past function implementation, a series of unit tests, and a hint to change the implementation appropriately. Apply the changes below by writing the body of this function only.\n\n-----"
````

#### Assignment 9: L18 `RS_SELF_REFLECTION_COMPLETION_INSTRUCTION`
````python
RS_SELF_REFLECTION_COMPLETION_INSTRUCTION = "You are a Rust programming assistant. You will be given a function implementation and a series of unit tests. Your goal is to write a few sentences to explain why your implementation is wrong as indicated by the tests. You will need this as a hint when you try again later. Only provide the few sentence description in your answer, not the implementation.\n\n-----"
````

#### Assignment 10: L20 `RS_REFLEXION_FEW_SHOT_ADD`
````python
RS_REFLEXION_FEW_SHOT_ADD = '''Example 1:
[previous impl]:
```rust
fn add(a: i32, b: i32) -> i32 {
    // Given integers a and b, return the total value of a and b.
    a - b
}
```

[unit test results from previous impl]:
Tested passed:

Tests failed:
assert_eq!(add(1, 2), 3); // output: -1
assert_eq!(add(1, 2), 4); // output: -1

[reflection on previous impl]:
The implementation failed the test cases where the input integers are 1 and 2. The issue arises because the code does not add the two integers together, but instead subtracts the second integer from the first. To fix this issue, we should change the operator from `-` to `+` in the return statement. This will ensure that the function returns the correct output for the given input.

[improved impl]:
```rust
fn add(a: i32, b: i32) -> i32 {
    // Given integers a and b, return the total value of a and b.
    a + b
}
```

END EXAMPLES
'''
````

#### Assignment 11: L50 `RS_TEST_GENERATION_FEW_SHOT`
````python
RS_TEST_GENERATION_FEW_SHOT = """For example:

func signature:
/// Add three numbers together.
/// This function takes three numbers as input and returns the sum of the three numbers.
fn add3Numbers(x: i32, y: i32, z: i32) -> i32 {

unit tests:
assert_eq!(add3Numbers(1, 2, 3), 6);
assert_eq!(add3Numbers(-1, 2, 3), 4);
assert_eq!(add3Numbers(1, -2, 3), 2);
assert_eq!(add3Numbers(1, 2, -3), 0);
assert_eq!(add3Numbers(-3, -2, -1), -6);
assert_eq!(add3Numbers(0, 0, 0), 0);
"""
````

#### Assignment 12: L66 `RS_SELF_REFLECTION_FEW_SHOT`
````python
RS_SELF_REFLECTION_FEW_SHOT = '''Example 1:
[function impl]:
```rust
pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
  use std::collections::HashMap;
  let mut map: HashMap<[u8;26], Vec<String>> = HashMap::with_capacity(strs.len());
  let offset = 'a' as usize;

  for str in strs.into_iter() {
    let mut chars: [u8; 26] = [0; 26];

    for char in str.chars() {
      chars[char.to_ascii_lowercase() as usize - offset] += 1;
    }

    // Flaw: using str.len() instead of chars in the hashmap key
    map.entry(str.len())
      .and_modify(|v| v.push(str.clone()))
      .or_insert(vec![str]);
  }
  
  let mut arr: Vec<Vec<String>> = Vec::new();
  for v in map.into_values() {
    arr.push(v);
  }
  arr
}
```

[unit test results]:
Tested passed:
assert_eq!(func(vec![""]), vec![vec![""]]);
assert_eq!(func(vec!["a"]), vec![vec!["a"]]);

Tests failed:
assert_eq!(func(vec!["eat", "tea", "tan", "ate", "nat", "bat"]), vec![vec!["bat"], vec!["nat", "tan"], vec!["ate", "eat", "tea"]]); # output:  [["bat", "tan", "nat"], ["eat", "tea", "ate"]]

[self-reflection]:
The implementation failed to group the anagrams together correctly. Instead, it grouped words by their length, which is not the intended behavior. The issue lies in using the length of the input strings (str.len()) as the key for the hashmap, rather than the count of each character in the strings (chars). To overcome this error, I should change the hashmap key to the character count array (chars). This will ensure that words with the same character counts (anagrams) are grouped together, which is the desired output. Next time I approach the problem, I will make sure to use the correct hashmap key to group the anagrams.

END EXAMPLES

'''
````

#### Assignment 13: L111 `RS_TEST_GENERATION_COMPLETION_INSTRUCTION`
````python
RS_TEST_GENERATION_COMPLETION_INSTRUCTION = f"""You are a Rust programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring.

{RS_TEST_GENERATION_FEW_SHOT}"""
````

#### Assignment 14: L115 `RS_TEST_GENERATION_CHAT_INSTRUCTION`
````python
RS_TEST_GENERATION_CHAT_INSTRUCTION = """You are a Rust programming assistant, an AI coding assistant that can write unique, diverse, and intuitive unit tests for functions given the signature and docstring."""
````


---

### `programming/immediate_refinement.py`

#### Assignment 1: L33 `tests_i`
````python
tests_i = gen.internal_tests(item["prompt"], model, 1)
````

#### Assignment 2: L36 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(item["prompt"], model, "simple")
````

#### Assignment 3: L53 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(
                    func_sig=item["prompt"],
                    model=model,
                    strategy="reflexion",
                    prev_func_impl=cur_func_impl,
                    feedback=cur_feedback,
                    self_reflection="No self-reflection"
                )
````


---

### `programming/immediate_reflexion.py`

#### Assignment 1: L34 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(item["prompt"], model, "simple")
````

#### Assignment 2: L42 `reflection`
````python
reflection = gen.self_reflection(
                    cur_func_impl, feedback, model)
````

#### Assignment 3: L47 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(
                    func_sig=item["prompt"],
                    model=model,
                    strategy="reflexion",
                    prev_func_impl=cur_func_impl,
                    feedback=feedback,
                    self_reflection=reflection
                )
````


---

### `programming/mcts.py`

#### Assignment 1: L11 `react_prompt_header`
````python
react_prompt_header = "Here are some previous solutions and the corresponding test results.\n"
````

#### Assignment 2: L146 `reflection`
````python
reflection = gen.self_reflection(cur_func_impl, feedback, model)
````

#### Assignment 3: L115 `tests_i`
````python
tests_i = gen.internal_tests(item["prompt"], test_model, number_of_tests)
````

#### Assignment 4: L118 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(item["prompt"], model, "simple")
````

#### Assignment 5: L153 `tests_i`
````python
tests_i = gen.internal_tests(item["prompt"], test_model, number_of_tests)
````

#### Assignment 6: L156 `trajectory`
````python
trajectory = {
                'solutions': [],
                'feedbacks': []
            }
````

#### Assignment 7: L175 `new_solution`
````python
new_solution = gen.func_impl(
                        func_sig=item["prompt"],
                        model=model,
                        strategy=strategy,
                        prev_func_impl=prev_func_impl,
                        feedback=feedback,
                        self_reflection=reflection,
                        acc_feedback = acc_feedback,
                        acc_reflection = acc_reflection
                    )
````

#### Assignment 8: L196 `reflection`
````python
reflection = gen.self_reflection(child.solution, feedback_internal, model)
````

#### Assignment 9: L208 `passed_section`
````python
passed_section = feedback_internal.split("Tests failed:")[0]
````


---

### `programming/reflexion.py`

#### Assignment 1: L38 `tests_i`
````python
tests_i = gen.internal_tests(item["prompt"], model, number_of_tests)
````

#### Assignment 2: L42 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(item["prompt"], model, "simple")
````

#### Assignment 3: L61 `reflection`
````python
reflection = gen.self_reflection(
                    cur_func_impl, cur_feedback, model)
````

#### Assignment 4: L70 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(
                    func_sig=prompt,
                    model=model,
                    strategy="simple",
                    prev_func_impl=cur_func_impl,
                    feedback="",
                    self_reflection="",
                )
````


---

### `programming/simple.py`

#### Assignment 1: L7 `SIMPLE_COMPLETION_INSTRUCTION`
````python
SIMPLE_COMPLETION_INSTRUCTION = "# Write the body of this function only."
````

#### Assignment 2: L8 `SIMPLE_CHAT_INSTRUCTION`
````python
SIMPLE_CHAT_INSTRUCTION = "You are a programming assistant. You will be given a function signature and docstring. You should fill in the following text of the missing function body. For example, the first line of the completion should have 4 spaces for the indentation so that it fits syntactically with the preceding signature."
````

#### Assignment 3: L32 `cur_func_impl`
````python
cur_func_impl = gen.func_impl(item["prompt"], model, "simple")
````


---

### `programming/test_acc.py`

#### Assignment 1: L30 `tests_i`
````python
tests_i = gen.internal_tests(item["prompt"], model, 1)
````

#### Assignment 2: L33 `cur_func_impl`
````python
cur_func_impl = item["prompt"] + item["canonical_solution"]
````


---

### `webshop/lats.py`

#### Assignment 1: L30 `ACTION_TO_TEMPLATE`
````python
ACTION_TO_TEMPLATE = {
    'Description': 'description_page.html',
    'Features': 'features_page.html',
    'Reviews': 'review_page.html',
    'Attributes': 'attributes_page.html',
}
````

#### Assignment 2: L240 `value_prompt`
````python
value_prompt = task.value_prompt_wrap(x, y, failed_trajectories, reflection_map)
````

#### Assignment 3: L246 `value_outputs`
````python
value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)
````

#### Assignment 4: L286 `samples`
````python
samples = gpt(prompt, n=n_generate_sample, stop=stop)
````

#### Assignment 5: L616 `sampled_actions`
````python
sampled_actions = get_samples(task, prompt, "\nAction: ", n, prompt_sample=args.prompt_sample, stop="Observation")
````

#### Assignment 6: L683 `child_prompts`
````python
child_prompts = [generate_prompt(child) for child in node.children if not child.is_terminal]
````

#### Assignment 7: L685 `votes`
````python
votes = get_values(task, node.question, child_prompts, args.n_evaluate_sample)
````

#### Assignment 8: L691 `votes`
````python
votes = votes + [0] * (len(node.children) - len(votes))
````

#### Assignment 9: L225 `uct_values`
````python
uct_values = [child.uct() for child in node.children if not child.is_terminal]
````

#### Assignment 10: L229 `probabilities`
````python
probabilities = softmax(np.array(uct_values), temperature)
````

#### Assignment 11: L278 `reflection_map`
````python
reflection_map = task.generate_self_reflection(failed_trajectories, x)
````

#### Assignment 12: L303 `state`
````python
self.state = {'action': '', 'observation': ''} if state is None else state
````

#### Assignment 13: L453 `terminal_node`
````python
terminal_node = rollout(max(node.children, key=lambda child: child.value), args, task, idx, max_depth=15)
````

#### Assignment 14: L562 `child_prompts`
````python
child_prompts = [generate_prompt(child) for child in new_states if not child.is_terminal and child is not None]
````

#### Assignment 15: L625 `action_line`
````python
action_line = next((line.split(":")[1].strip() for line in action.split("\n") if line.startswith("Action") and ":" in line), None)
````

#### Assignment 16: L717 `value`
````python
node.value = (node.value * (node.visits - 1) + value) / node.visits
````

#### Assignment 17: L130 `observation`
````python
observation = 'Your score (min 0.0, max 1.0): ' + (visible_texts[idx + 1])
````

#### Assignment 18: L261 `value`
````python
value = get_value(task, x, y, n_evaluate_sample, cache_value=cache_value)
````

#### Assignment 19: L282 `prompt`
````python
prompt = task.cot_prompt_wrap(x, y, reflection_map)
````

#### Assignment 20: L355 `action`
````python
action = line.split(", action=")[1].split(", observation=")[0].strip()
````

#### Assignment 21: L356 `observation`
````python
observation = line.split(", observation=")[1].split(")")[0].strip()
````

#### Assignment 22: L565 `values`
````python
values = get_values(task, node.question, child_prompts, args.n_evaluate_sample)
````

#### Assignment 23: L654 `new_node`
````python
new_node = Node(state=new_state, question=node.question, env_state=env_state_clone, parent=node)
````


---

### `webshop/models.py`

#### Assignment 1: L28 `response`
````python
response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=stop
        )
````

#### Assignment 2: L69 `cost`
````python
cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03
````

#### Assignment 3: L71 `cost`
````python
cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.0015
````

#### Assignment 4: L73 `cost`
````python
cost = completion_tokens / 1000 * 0.004 + prompt_tokens / 1000 * 0.003
````


---

### `webshop/prompt.py`

#### Assignment 1: L1 `prompt1`
````python
prompt1 = """Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: think[For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.]
Observation: OK.

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]

{input}
"""
````

#### Assignment 2: L53 `prompt1_feedback`
````python
prompt1_feedback = """You are also an advanced reasoning agent that can improve based on self refection. Follow the instruction and purchase an item meeting all of the correct specifications by navigating the website. 
Here is an example:
Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: think[For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.]
Observation: OK.

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]

Here are some previous trials in which you were given access to relevant context and a item to purchase. You were unsuccessful in buying the correct item either because you did not find an item meeting all of the required specifications or because you did not select the correct item. Carefully consider the errors and make sure not to repeat the same mistakes. {trajectories}

{input}
"""
````

#### Assignment 3: L109 `score_prompt`
````python
score_prompt = '''Given an item to purchase and a trajectory that aims to buy an item that exactly matches the specification, which corresponds to the ideal score of 1.0, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Here are some examples

Webshop
Instruction:
i am looking for dairy free and apple variety pack of chips, and price lower than 30.00 dollars
[Search]

Action: search[dairy free and apple variety pack of chips]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B07HRFJWP8]
Enjoy Life Foods Soft Baked Ovals, Breakfast Bars, Nut Free Bars, Soy Free, Dairy Free, Non GMO, Gluten Free, Vegan, Variety Pack, 4 Boxes (20 Bars Total)
$100.0
[B01KMHY5PG]
Enjoy Life Soft Baked Chewy Bars, Variety Pack, Nut Free Bars, Soy Free, Dairy Free, Gluten Free, 6 Boxes (30 Total Bars)
$21.49
[B008D2X8C4]
Enjoy Life Lentil Chips Variety Pack, Dairy Free Chips, Soy Free, Nut Free, Non GMO, Vegan, Gluten Free, 24 Bags (0.8 oz)
$100.0

Action: think[The first two items are not what I want. The third item is the dairy free and apple variety pack of chips I want.]
Observation: OK.

Action: click[B008D2X8C4]
Observation:
[Back to Search]
[< Prev]
flavor name [dill and sour cream][garlic & parmesan][light sea salt][margherita pizza][thai chili lime][variety pack]
size [0.8 ounce (pack of 24)][4 ounce (pack of 12)]
Price: $100.0
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The item has options 'variety pack' and '0.8 ounce (pack of 24)' and seems good to buy.]
Observation: OK.

Action: click[variety pack]
Observation: You have clicked variety pack.

Action: click[0.8 ounce (pack of 24)]
Observation: You have clicked 0.8 ounce (pack of 24).

Action: click[Buy Now]

Reflection: In this attempt, I was unsuccessful. I accidentally bought a product that was $100, which is more than my budget of $30. Either way, the initial search results were not good. Next time, I will do search["variety pack of chips"] and then check if the results meet the dairy free and the $30 budget constraints. I will continue to refine my searches so that I can find more products.
Thus the correctness score is 5

Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.
Reflection: Although the task is not yet complete, the first search is correct and returns relevant results. The thought is also logical and has potential to lead to the correct selection.
Thus the correctness score is 9
{input}
'''
````

#### Assignment 4: L190 `score_prompt_feedback`
````python
score_prompt_feedback = '''Given an item to purchase and a trajectory, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.
Here are some examples

Webshop
Instruction:
i am looking for dairy free and apple variety pack of chips, and price lower than 30.00 dollars
[Search]

Action: search[dairy free and apple variety pack of chips]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B07HRFJWP8]
Enjoy Life Foods Soft Baked Ovals, Breakfast Bars, Nut Free Bars, Soy Free, Dairy Free, Non GMO, Gluten Free, Vegan, Variety Pack, 4 Boxes (20 Bars Total)
$100.0
[B01KMHY5PG]
Enjoy Life Soft Baked Chewy Bars, Variety Pack, Nut Free Bars, Soy Free, Dairy Free, Gluten Free, 6 Boxes (30 Total Bars)
$21.49
[B008D2X8C4]
Enjoy Life Lentil Chips Variety Pack, Dairy Free Chips, Soy Free, Nut Free, Non GMO, Vegan, Gluten Free, 24 Bags (0.8 oz)
$100.0

Action: think[The first two items are not what I want. The third item is the dairy free and apple variety pack of chips I want.]
Observation: OK.

Action: click[B008D2X8C4]
Observation:
[Back to Search]
[< Prev]
flavor name [dill and sour cream][garlic & parmesan][light sea salt][margherita pizza][thai chili lime][variety pack]
size [0.8 ounce (pack of 24)][4 ounce (pack of 12)]
Price: $100.0
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The item has options 'variety pack' and '0.8 ounce (pack of 24)' and seems good to buy.]
Observation: OK.

Action: click[variety pack]
Observation: You have clicked variety pack.

Action: click[0.8 ounce (pack of 24)]
Observation: You have clicked 0.8 ounce (pack of 24).

Action: click[Buy Now]

Reflection: In this attempt, I was unsuccessful. I accidentally bought a product that was $100, which is more than my budget of $30. Either way, the initial search results were not good. Next time, I will do search["variety pack of chips"] and then check if the results meet the dairy free and the $30 budget constraints. I will continue to refine my searches so that I can find more products.
Thus the correctness score is 5

Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.]
Observation: OK.
Reflection: Although the task is not yet complete, the first search is correct and returns relevant results. The thought is also logical and has potential to lead to the correct selection.
Thus the correctness score is 9
{trajectories}
{input}
'''
````

#### Assignment 5: L272 `prompt1_actonly`
````python
prompt1_actonly = """Webshop 
Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Action: click[B078GWRC1J]
Observation: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Action: click[bright citrus]
Observation: You have clicked bright citrus. 

Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1). 

Action: click[Buy Now]
"""
````

#### Assignment 6: L315 `reflection_prompt`
````python
reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an shopping website and a specific type of item to buy. You were given access to relevant context and a item to purchase. You were unsuccessful in buying the correct item either because you did not find an item meeting all of the required specifications or because you did not select the correct item. The ideal score is 1.0, and anything less is incorrect. In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  
Here are some examples:

Previous Trial
Instruction:
i am looking for dairy free and apple variety pack of chips, and price lower than 30.00 dollars
[Search]

Action: search[dairy free and apple variety pack of chips]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B07HRFJWP8]
Enjoy Life Foods Soft Baked Ovals, Breakfast Bars, Nut Free Bars, Soy Free, Dairy Free, Non GMO, Gluten Free, Vegan, Variety Pack, 4 Boxes (20 Bars Total)
$100.0
[B01KMHY5PG]
Enjoy Life Soft Baked Chewy Bars, Variety Pack, Nut Free Bars, Soy Free, Dairy Free, Gluten Free, 6 Boxes (30 Total Bars)
$21.49
[B008D2X8C4]
Enjoy Life Lentil Chips Variety Pack, Dairy Free Chips, Soy Free, Nut Free, Non GMO, Vegan, Gluten Free, 24 Bags (0.8 oz)
$100.0

Action: think[The first two items are not what I want. The third item is the dairy free and apple variety pack of chips I want.]
Observation: OK.

Action: click[B008D2X8C4]
Observation:
[Back to Search]
[< Prev]
flavor name [dill and sour cream][garlic & parmesan][light sea salt][margherita pizza][thai chili lime][variety pack]
size [0.8 ounce (pack of 24)][4 ounce (pack of 12)]
Price: $100.0
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The item has options 'variety pack' and '0.8 ounce (pack of 24)' and seems good to buy.]
Observation: OK.

Action: click[variety pack]
Observation: You have clicked variety pack.

Action: click[0.8 ounce (pack of 24)]
Observation: You have clicked 0.8 ounce (pack of 24).

Action: click[Buy Now]

STATUS: FAIL

Reflection: In this attempt, I was unsuccessful. I accidentally bought a product that was $100, which is more than my budget of $30. Either way, the initial search results were not good. Next time, I will do search["variety pack of chips"] and then check if the results meet the dairy free and the $30 budget constraints. I will continue to refine my searches so that I can find more products.

Previous Trial
Instruction:
i need gluten free vegetarian smoked peppered bacon - 4 ounce (pack of 2), and price lower than 40.00 dollars
[Search]

Action: search[gluten free vegetarian smoked peppered bacon 4 ounce pack of 2]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B06Y96MXJV]
Smoked Bacon Sea Salt 3-Pack: Smoked Bacon Chipotle, Smoked Bacon and Onion, Smoked Peppered Bacon - All-Natural Sea Salts Slowly Smoked Over Alderwood - No Gluten, No MSG, Non-GMO (12 total oz.)
$29.99
[B06Y96N1KG]
Spicy Hot Pepper Sea Salt 3-Pack: Ghost Pepper, Jalapeno, Habanero - All Natural, Delicious Blends of Peppers & Sea Salt - Gluten-Free, Kosher, No MSG, Non-GMO (12 total oz.)
$29.99
[B07GJTKYJQ]
Louisville Vegan Jerky - 5 Flavor Variety Pack, Non-GMO Soy Protein, Gluten-Free (Black Pepper, Buffalo Dill, Pepperoni, Maple Bacon, and Carolina BBQ, 3 Ounces)
$42.99

Action: think[The first two items are not what I want. The third item is not what I want, but it is the closest one.]
Observation: OK.

Action: click[B07GJTKYJQ]
Observation:
[Back to Search]
[< Prev]
Louisville Vegan Jerky - 5 Flavor Variety Pack, Non-GMO Soy Protein, Gluten-Free (Black Pepper, Buffalo Dill, Pepperoni, Maple Bacon, and Carolina BBQ, 3 Ounces)
Price: $42.99
Rating: N.A.
[Description]
[Features]
[Reviews]
[Buy Now]

Action: think[The price is too high and it is not what I want.]
Observation: OK.

Action: click[< Prev]
Observation:
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B06Y96MXJV]
Smoked Bacon Sea Salt 3-Pack: Smoked Bacon Chipotle, Smoked Bacon and Onion, Smoked Peppered Bacon - All-Natural Sea Salts Slowly Smoked Over Alderwood - No Gluten, No MSG, Non-GMO (12 total oz.)
$29.99
[B06Y96N1KG]
Spicy Hot Pepper Sea Salt 3-Pack: Ghost Pepper, Jalapeno, Habanero - All Natural, Delicious Blends of Peppers & Sea Salt - Gluten-Free, Kosher, No MSG, Non-GMO (12 total oz.)
$29.99
[B07GJTKYJQ]
Louisville Vegan Jerky - 5 Flavor Variety Pack, Non-GMO Soy Protein, Gluten-Free (Black Pepper, Buffalo Dill, Pepperoni, Maple Bacon, and Carolina BBQ, 3 Ounces)
$42.99

Action: think[The first two items are not what I want.]
Observation: OK.

Action: click[Next >]
Observation: Invalid action!

Action: think[I need to refine my search.]
Observation: OK.

Action: click[< Back to Search]
Observation: Invalid action!

Action: click[Back to Search]

STATUS: FAIL

Reflection: In this attempt, I was unsuccessful. The initial search results were not the products that I was looking for. Next time, I will do search["vegetarian bacon"] for a broader search. I will check that the new results will fulfill the gluten free and 4 ounce pack of 2 constraints. I will continue to refine my searches so that I can find more products.

Previous trial:
{trajectory}
Reflection:'''
````


---

### `webshop/webshop.py`

#### Assignment 1: L61 `reflect_prompt`
````python
reflect_prompt = reflection_prompt.format(trajectory=traj)
````

#### Assignment 2: L65 `traj_with_reflection`
````python
traj_with_reflection = traj + "Reflection: " + reflection[0] + "\n"
````

#### Assignment 3: L67 `reflection_mapping`
````python
reflection_mapping = {
            'question': question,
            'reflection': reflection[0]
        }
````

#### Assignment 4: L157 `prompt`
````python
prompt = compare_prompt + f'Action 1:{last_actions[0]}\n\nAction 2:{last_actions[1]}\n'
````

#### Assignment 5: L84 `reflect_prompt`
````python
reflect_prompt = reflection_prompt.format(trajectory=traj)
````

#### Assignment 6: L109 `prompt`
````python
prompt = prompt1_feedback.format(trajectories=trajectories, input=input)
````

#### Assignment 7: L193 `prompt`
````python
prompt = score_prompt_feedback.format(s="", trajectories=failed_trajectories, input=inp)
````

#### Assignment 8: L106 `traj_with_reflection`
````python
traj_with_reflection = reflection_mapping['trajectory'] + "Reflection: " + reflection_mapping['reflection'] + "\n"
````

#### Assignment 9: L188 `new_trajectory`
````python
new_trajectory = 'Action: '.join([first_part] + remaining_parts)
````
