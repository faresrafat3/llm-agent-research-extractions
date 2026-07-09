# AI Scientist v2 — Complete Python Logic / Flow / Inputs / Outputs Audit

Source repository: `https://github.com/SakanaAI/AI-Scientist-v2`  
Audited local commit: `96bd51617cfdbb494a9fc283af00fe090edfae48`  

This report is AST-assisted. It lists every Python file, classes, functions, loops, conditions, decisions, returns, prompt-like assignments, LLM/VLM calls, and relevant I/O calls. The separate `prompts_complete.md` contains full prompt text extracted earlier.

## Repository Python file map

- `ai_scientist/__init__.py`
- `ai_scientist/ideas/i_cant_believe_its_not_better.py`
- `ai_scientist/ideas/i_cant_believe_its_not_betterrealworld.py`
- `ai_scientist/llm.py`
- `ai_scientist/perform_icbinb_writeup.py`
- `ai_scientist/perform_ideation_temp_free.py`
- `ai_scientist/perform_llm_review.py`
- `ai_scientist/perform_plotting.py`
- `ai_scientist/perform_vlm_review.py`
- `ai_scientist/perform_writeup.py`
- `ai_scientist/tools/__init__.py`
- `ai_scientist/tools/base_tool.py`
- `ai_scientist/tools/semantic_scholar.py`
- `ai_scientist/treesearch/__init__.py`
- `ai_scientist/treesearch/agent_manager.py`
- `ai_scientist/treesearch/backend/__init__.py`
- `ai_scientist/treesearch/backend/backend_anthropic.py`
- `ai_scientist/treesearch/backend/backend_openai.py`
- `ai_scientist/treesearch/backend/utils.py`
- `ai_scientist/treesearch/bfts_utils.py`
- `ai_scientist/treesearch/interpreter.py`
- `ai_scientist/treesearch/journal.py`
- `ai_scientist/treesearch/journal2report.py`
- `ai_scientist/treesearch/log_summarization.py`
- `ai_scientist/treesearch/parallel_agent.py`
- `ai_scientist/treesearch/perform_experiments_bfts_with_agentmanager.py`
- `ai_scientist/treesearch/utils/__init__.py`
- `ai_scientist/treesearch/utils/config.py`
- `ai_scientist/treesearch/utils/data_preview.py`
- `ai_scientist/treesearch/utils/metric.py`
- `ai_scientist/treesearch/utils/response.py`
- `ai_scientist/treesearch/utils/serialize.py`
- `ai_scientist/treesearch/utils/tree_export.py`
- `ai_scientist/utils/token_tracker.py`
- `ai_scientist/vlm.py`
- `launch_scientist_bfts.py`

## End-to-end execution summary

1. `launch_scientist_bfts.py` loads idea JSON(s), optional code/dataset references, and BFTS config.  
2. `perform_ideation_temp_free.py` can generate idea JSON via LLM + Semantic Scholar + FinalizeIdea loop.  
3. `perform_experiments_bfts_with_agentmanager.py` loads config/task, creates `AgentManager`, runs staged BFTS experiments, saves journals/summaries.  
4. `AgentManager` creates stage goals, checks completion/progression, orchestrates `ParallelAgent`/`MinimalAgent`.  
5. `parallel_agent.py` drafts/debugs/improves/hyperparameter-tunes/ablates code nodes, executes code, parses metrics, generates plots, invokes VLM feedback.  
6. `journal.py`, `log_summarization.py`, and `journal2report.py` select/summarize/report experiment results.  
7. `perform_plotting.py` aggregates final plots through an LLM-generated script plus reflection loop.  
8. `perform_writeup.py` or `perform_icbinb_writeup.py` gathers citations, generates LaTeX, reflects/compiles; ICBINB variant adds VLM figure/caption/page-limit reflection.  
9. `perform_llm_review.py` and `perform_vlm_review.py` review generated papers/figures.


---

## File: `ai_scientist/__init__.py`

**Lines:** 1  


### Imports / external dependencies

- None

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

- None

---

## File: `ai_scientist/ideas/i_cant_believe_its_not_better.py`

**Lines:** 414  


### Imports / external dependencies

- `import warnings`
- `from datetime import datetime`
- `import numpy as np`
- `import time`
- `import os`
- `import torch`
- `import torch.nn as nn`
- `import torch.optim as optim`
- `import torchvision.transforms as T`
- `from torch.utils.data import DataLoader`
- `from datasets import load_dataset`
- `from torchvision.models import resnet50`
- `from huggingface_hub import login`
- `from transformers import pipeline`
- `from PIL import Image`
- `import requests`

### Module-level assignments / constants

- L24: `medmnist = load_dataset("albertvillanova/medmnist-v2", "pathmnist")`
- L29: `eurosat = load_dataset("tanganke/eurosat")`
- L34: `mnist = load_dataset("ylecun/mnist")`
- L39: `fashion_mnist = load_dataset("zalando-datasets/fashion_mnist")`
- L44: `cifar = load_dataset("uoft-cs/cifar10")`
- L49: `imdb = load_dataset("stanfordnlp/imdb")`
- L54: `amazon_polarity = load_dataset("fancyzhx/amazon_polarity")`
- L59: `emotion = load_dataset("dair-ai/emotion")`
- L64: `silicone = load_dataset("eusip/silicone", "dyda_da", trust_remote_code=True)`
- L69: `math_examples = load_dataset( "deepmind/math_dataset", "algebra__linear_1d", trust_remote_code=True )`
- L83: `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")`
- L84: `pipe = pipeline( task="image-feature-extraction", model="google/vit-base-patch16-384", device=device, pool=True, )`
- L90: `img_urls = [ "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.png", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.jpeg", ]`
- L94: `image_real = Image.open(requests.get(img_urls[0], stream=True).raw).convert("RGB")`
- L95: `image_gen = Image.open(requests.get(img_urls[1], stream=True).raw).convert("RGB")`
- L96: `outputs = pipe([image_real, image_gen])`
- L97: `similarity_score = cosine_similarity( torch.Tensor(outputs[0]), torch.Tensor(outputs[1]), dim=1 )`
- L102: `pipe = pipeline( task="image-feature-extraction", model="facebook/dinov2-base", device=device, pool=True, )`
- L108: `pipe = pipeline( task="image-feature-extraction", model="microsoft/rad-dino", device=device, pool=True, )`
- L116: `feature_extractor = pipeline( "feature-extraction", framework="pt", model="facebook/bart-base" )`
- L119: `text = "Transformers is an awesome library!"`
- L121: `embed = feature_extractor(text, return_tensors="pt")[0].numpy().mean(axis=0)`
- L129: `BATCH_SIZE = 512`
- L130: `LEARNING_RATE = 3e-3`
- L131: `WEIGHT_DECAY = 1e-2`
- L132: `IMAGE_SIZE = 84`
- L133: `NUM_WORKERS = 8`
- L134: `DATASET_NAME = "mini-imagenet"`
- L135: `NUM_EPOCHS = 20`
- L136: `STEPS_TO_LOG = 25`
- L137: `NUM_TEST_BATCHES = 20`
- L138: `DATASET = "timm/mini-imagenet"`
- L139: `WARMUP_EPOCHS = 2`
- L141: `transform = T.Compose( [ T.Lambda(lambda img: img.convert("RGB")), T.Resize((IMAGE_SIZE, IMAGE_SIZE)), T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ] )`
- L149: `weights = None`
- L152: `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")`
- L155: `train_dataset_hf = load_dataset( DATASET, # or the appropriate dataset name split="train", trust_remote_code=True, # Allow running custom code from the dataset )`
- L161: `val_dataset_hf = load_dataset( DATASET, # or the appropriate dataset name split="validation", trust_remote_code=True, # Allow running custom code from the dataset )`
- L167: `test_dataset_hf = load_dataset( DATASET, # or the appropriate dataset name split="test", trust_remote_code=True, # Allow running custom code from the dataset )`
- L193: `train_dataset = HuggingFaceImageNet(train_dataset_hf, transform=transform)`
- L194: `val_dataset = HuggingFaceImageNet(val_dataset_hf, transform=transform)`
- L195: `test_dataset = HuggingFaceImageNet(test_dataset_hf, transform=transform)`
- L198: `train_loader = DataLoader( train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS, # Decodes/transforms in parallel pin_memory=True, )`
- L206: `val_loader = DataLoader( val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS, pin_memory=True, )`
- L214: `test_loader = DataLoader( test_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS, pin_memory=True, )`
- L223: `model = resnet50(weights=weights)`
- L224: `model = model.to(device)`
- L226: `start_time = time.time()`
- L234: `criterion = nn.CrossEntropyLoss(label_smoothing=0.1)`
- L237: `optimizer = optim.SGD( model.parameters(), lr=0.1, # Higher initial LR for SGD momentum=0.9, weight_decay=WEIGHT_DECAY, # Lower weight decay for SGD nesterov=True, # Enable Nesterov momentum )`
- L247: `scheduler = optim.lr_scheduler.SequentialLR( optimizer, schedulers=[ optim.lr_scheduler.LinearLR( optimizer, start_factor=0.1, total_iters=WARMUP_EPOCHS * len(train_loader) ), optim.lr_scheduler.CosineAnnealingLR( optimizer, T_max=(NUM_EPOCHS - WARMUP_EPOCHS) * len(train_loader), eta_min=1e-6, # ...`
- L263: `GRAD_CLIP_NORM = 2.0`
- L284: `timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")`
- L285: `log_file = f"{DATASET_NAME}_training_log_{timestamp}.npy"`
- L286: `checkpoint_dir = f"{DATASET_NAME}_checkpoints_{timestamp}"`
- L290: `metrics = { "epoch": [], "step": [], "loss": [], "train_accuracy": [], "val_accuracy": [], "test_accuracy": [], }`
- L301: `best_val_accuracy = 0.0`
- L403: `final_checkpoint_path = os.path.join(checkpoint_dir, "model_final.pt")`

### Prompt-like assignments in this file

- L141 `transform` — snippet: `transform = T.Compose( [ T.Lambda(lambda img: img.convert("RGB")), T.Resize((IMAGE_SIZE, IMAGE_SIZE)), T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ] )`

### Top-level decisions / loops / try blocks

- IF L228: `torch.cuda.is_available()`; body=1 else=0
- LOOP L302: `{'line': 302, 'type': 'for', 'target': 'epoch', 'iter': 'range(NUM_EPOCHS)', 'body_len': 11, 'orelse_len': 0}`

### Classes

#### Class `HuggingFaceImageNet` (L175)
- Bases: `torch.utils.data.Dataset`
##### `__init__(self, hf_dataset, transform)` (L176)
- Inputs: parameters from signature `__init__(self, hf_dataset, transform)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `__len__(self)` (L180)
- Inputs: parameters from signature `__len__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L181: `len(self.hf_dataset)`
- Main call graph hints: `len`
##### `__getitem__(self, idx)` (L183)
- Inputs: parameters from signature `__getitem__(self, idx)` plus referenced module/global/config state.
- Outputs / returns:
  - L190: `(img, label)`
- Conditions / decisions:
  - L188: IF `self.transform is not None`; body=1 else=0
- Main call graph hints: `self.transform`

### Functions

#### `calculate_accuracy(model, data_loader, device, max_batches)` (L267)
- Inputs: parameters from signature `calculate_accuracy(model, data_loader, device, max_batches)` plus referenced module/global/config state.
- Outputs / returns:
  - L280: `100 * correct / total`
- Loops:
  - L272: {'line': 272, 'type': 'for', 'target': '(batch_idx, (images, labels))', 'iter': 'enumerate(data_loader)', 'body_len': 6, 'orelse_len': 0}
- Conditions / decisions:
  - L273: IF `max_batches and batch_idx >= max_batches`; body=1 else=0
- Main call graph hints: `model.eval`, `torch.no_grad`, `enumerate`, `model`, `torch.max`, `labels.size`, `Compare.sum.item`, `images.to`, `labels.to`, `Compare.sum`

---

## File: `ai_scientist/ideas/i_cant_believe_its_not_betterrealworld.py`

**Lines:** 382  


### Imports / external dependencies

- `import warnings`
- `from datetime import datetime`
- `import numpy as np`
- `import time`
- `import os`
- `import torch`
- `import torch.nn as nn`
- `import torch.optim as optim`
- `import torchvision.transforms as T`
- `from torch.utils.data import DataLoader`
- `from datasets import load_dataset`
- `from torchvision.models import resnet50`
- `from huggingface_hub import login`
- `from transformers import pipeline`
- `from PIL import Image`
- `import requests`

### Module-level assignments / constants

- L51: `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")`
- L52: `pipe = pipeline( task="image-feature-extraction", model="google/vit-base-patch16-384", device=device, pool=True, )`
- L58: `img_urls = [ "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.png", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.jpeg", ]`
- L62: `image_real = Image.open(requests.get(img_urls[0], stream=True).raw).convert("RGB")`
- L63: `image_gen = Image.open(requests.get(img_urls[1], stream=True).raw).convert("RGB")`
- L64: `outputs = pipe([image_real, image_gen])`
- L65: `similarity_score = cosine_similarity( torch.Tensor(outputs[0]), torch.Tensor(outputs[1]), dim=1 )`
- L70: `pipe = pipeline( task="image-feature-extraction", model="facebook/dinov2-base", device=device, pool=True, )`
- L76: `pipe = pipeline( task="image-feature-extraction", model="microsoft/rad-dino", device=device, pool=True, )`
- L84: `feature_extractor = pipeline( "feature-extraction", framework="pt", model="facebook/bart-base" )`
- L87: `text = "Transformers is an awesome library!"`
- L89: `embed = feature_extractor(text, return_tensors="pt")[0].numpy().mean(axis=0)`
- L97: `BATCH_SIZE = 512`
- L98: `LEARNING_RATE = 3e-3`
- L99: `WEIGHT_DECAY = 1e-2`
- L100: `IMAGE_SIZE = 84`
- L101: `NUM_WORKERS = 8`
- L102: `DATASET_NAME = "mini-imagenet"`
- L103: `NUM_EPOCHS = 20`
- L104: `STEPS_TO_LOG = 25`
- L105: `NUM_TEST_BATCHES = 20`
- L106: `DATASET = "timm/mini-imagenet"`
- L107: `WARMUP_EPOCHS = 2`
- L109: `transform = T.Compose( [ T.Lambda(lambda img: img.convert("RGB")), T.Resize((IMAGE_SIZE, IMAGE_SIZE)), T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ] )`
- L117: `weights = None`
- L120: `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")`
- L123: `train_dataset_hf = load_dataset( DATASET, # or the appropriate dataset name split="train", trust_remote_code=True, # Allow running custom code from the dataset )`
- L129: `val_dataset_hf = load_dataset( DATASET, # or the appropriate dataset name split="validation", trust_remote_code=True, # Allow running custom code from the dataset )`
- L135: `test_dataset_hf = load_dataset( DATASET, # or the appropriate dataset name split="test", trust_remote_code=True, # Allow running custom code from the dataset )`
- L161: `train_dataset = HuggingFaceImageNet(train_dataset_hf, transform=transform)`
- L162: `val_dataset = HuggingFaceImageNet(val_dataset_hf, transform=transform)`
- L163: `test_dataset = HuggingFaceImageNet(test_dataset_hf, transform=transform)`
- L166: `train_loader = DataLoader( train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS, # Decodes/transforms in parallel pin_memory=True, )`
- L174: `val_loader = DataLoader( val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS, pin_memory=True, )`
- L182: `test_loader = DataLoader( test_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS, pin_memory=True, )`
- L191: `model = resnet50(weights=weights)`
- L192: `model = model.to(device)`
- L194: `start_time = time.time()`
- L202: `criterion = nn.CrossEntropyLoss(label_smoothing=0.1)`
- L205: `optimizer = optim.SGD( model.parameters(), lr=0.1, # Higher initial LR for SGD momentum=0.9, weight_decay=WEIGHT_DECAY, # Lower weight decay for SGD nesterov=True, # Enable Nesterov momentum )`
- L215: `scheduler = optim.lr_scheduler.SequentialLR( optimizer, schedulers=[ optim.lr_scheduler.LinearLR( optimizer, start_factor=0.1, total_iters=WARMUP_EPOCHS * len(train_loader) ), optim.lr_scheduler.CosineAnnealingLR( optimizer, T_max=(NUM_EPOCHS - WARMUP_EPOCHS) * len(train_loader), eta_min=1e-6, # ...`
- L231: `GRAD_CLIP_NORM = 2.0`
- L252: `timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")`
- L253: `log_file = f"{DATASET_NAME}_training_log_{timestamp}.npy"`
- L254: `checkpoint_dir = f"{DATASET_NAME}_checkpoints_{timestamp}"`
- L258: `metrics = { "epoch": [], "step": [], "loss": [], "train_accuracy": [], "val_accuracy": [], "test_accuracy": [], }`
- L269: `best_val_accuracy = 0.0`
- L371: `final_checkpoint_path = os.path.join(checkpoint_dir, "model_final.pt")`

### Prompt-like assignments in this file

- L109 `transform` — snippet: `transform = T.Compose( [ T.Lambda(lambda img: img.convert("RGB")), T.Resize((IMAGE_SIZE, IMAGE_SIZE)), T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ] )`

### Top-level decisions / loops / try blocks

- IF L196: `torch.cuda.is_available()`; body=1 else=0
- LOOP L270: `{'line': 270, 'type': 'for', 'target': 'epoch', 'iter': 'range(NUM_EPOCHS)', 'body_len': 11, 'orelse_len': 0}`

### Classes

#### Class `HuggingFaceImageNet` (L143)
- Bases: `torch.utils.data.Dataset`
##### `__init__(self, hf_dataset, transform)` (L144)
- Inputs: parameters from signature `__init__(self, hf_dataset, transform)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `__len__(self)` (L148)
- Inputs: parameters from signature `__len__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L149: `len(self.hf_dataset)`
- Main call graph hints: `len`
##### `__getitem__(self, idx)` (L151)
- Inputs: parameters from signature `__getitem__(self, idx)` plus referenced module/global/config state.
- Outputs / returns:
  - L158: `(img, label)`
- Conditions / decisions:
  - L156: IF `self.transform is not None`; body=1 else=0
- Main call graph hints: `self.transform`

### Functions

#### `calculate_accuracy(model, data_loader, device, max_batches)` (L235)
- Inputs: parameters from signature `calculate_accuracy(model, data_loader, device, max_batches)` plus referenced module/global/config state.
- Outputs / returns:
  - L248: `100 * correct / total`
- Loops:
  - L240: {'line': 240, 'type': 'for', 'target': '(batch_idx, (images, labels))', 'iter': 'enumerate(data_loader)', 'body_len': 6, 'orelse_len': 0}
- Conditions / decisions:
  - L241: IF `max_batches and batch_idx >= max_batches`; body=1 else=0
- Main call graph hints: `model.eval`, `torch.no_grad`, `enumerate`, `model`, `torch.max`, `labels.size`, `Compare.sum.item`, `images.to`, `labels.to`, `Compare.sum`

---

## File: `ai_scientist/llm.py`

**Lines:** 545  


### Imports / external dependencies

- `import json`
- `import os`
- `import re`
- `from typing import Any`
- `from ai_scientist.utils.token_tracker import track_token_usage`
- `import anthropic`
- `import backoff`
- `import openai`

### Module-level assignments / constants

- L11: `MAX_NUM_TOKENS = 4096`
- L13: `AVAILABLE_LLMS = [ "claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20241022", # OpenAI models "gpt-4o-mini", "gpt-4o-mini-2024-07-18", "gpt-4o", "gpt-4o-2024-05-13", "gpt-4o-2024-08-06", "gpt-4.1", "gpt-4.1-2025-04-14", "gpt-4.1-mini", "gpt-4.1-mini-2025-04-14", "o1", "o1-2024-12-17", "o1-previe...`

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `get_batch_responses_from_llm(prompt, client, model, system_message, print_debug, msg_history, temperature, n_responses)` (L87)
- Inputs: parameters from signature `get_batch_responses_from_llm(prompt, client, model, system_message, print_debug, msg_history, temperature, n_responses)` plus referenced module/global/config state.
- Outputs / returns:
  - L212: `(content, new_msg_history)`
- Loops:
  - L206: {'line': 206, 'type': 'for', 'target': '(j, msg)', 'iter': 'enumerate(new_msg_history[0])', 'body_len': 1, 'orelse_len': 0}
  - L189: {'line': 189, 'type': 'for', 'target': '_', 'iter': 'range(n_responses)', 'body_len': 3, 'orelse_len': 0}
- Conditions / decisions:
  - L98: IF `msg_history is None`; body=1 else=0
  - L101: IF `model.startswith('ollama/')`; body=4 else=1
  - L202: IF `print_debug`; body=6 else=0
  - L118: IF `'gpt' in model`; body=4 else=1
  - L136: IF `model == 'deepseek-coder-v2-0724'`; body=4 else=1
  - L153: IF `model == 'llama-3-1-405b-instruct'`; body=4 else=1
  - L170: IF `'gemini' in model`; body=4 else=2
- LLM/VLM calls:
  - L103: `client.chat.completions.create`
  - L120: `client.chat.completions.create`
  - L138: `client.chat.completions.create`
  - L155: `client.chat.completions.create`
  - L172: `client.chat.completions.create`
  - L190: `get_response_from_llm`
- Main call graph hints: `backoff.on_exception`, `model.startswith`, `client.chat.completions.create`, `print`, `enumerate`, `model.replace`, `range`, `get_response_from_llm`, `content.append`, `new_msg_history.append`
#### `make_llm_call(client, model, temperature, system_message, prompt)` (L216)
- Inputs: parameters from signature `make_llm_call(client, model, temperature, system_message, prompt)` plus referenced module/global/config state.
- Outputs / returns:
  - L218: `client.chat.completions.create(model=model.replace('ollama/', ''), messages=[{'role': 'system', 'content': system_message}, *prompt], temperature=temperature, max_tokens=MAX_NUM_TOKENS, n=1, stop=None)`
  - L230: `client.chat.completions.create(model=model, messages=[{'role': 'system', 'content': system_message}, *prompt], temperature=temperature, max_tokens=MAX_NUM_TOKENS, n=1, stop=None, seed=0)`
  - L243: `client.chat.completions.create(model=model, messages=[{'role': 'user', 'content': system_message}, *prompt], temperature=1, n=1, seed=0)`
- Conditions / decisions:
  - L217: IF `model.startswith('ollama/')`; body=1 else=1
  - L229: IF `'gpt' in model`; body=1 else=1
  - L242: IF `'o1' in model or 'o3' in model`; body=1 else=1
- Raises:
  - L255: `ValueError(f'Model {model} not supported.')`
- LLM/VLM calls:
  - L218: `client.chat.completions.create`
  - L230: `client.chat.completions.create`
  - L243: `client.chat.completions.create`
- Main call graph hints: `model.startswith`, `client.chat.completions.create`, `model.replace`, `ValueError`
#### `get_response_from_llm(prompt, client, model, system_message, print_debug, msg_history, temperature)` (L267)
- Inputs: parameters from signature `get_response_from_llm(prompt, client, model, system_message, print_debug, msg_history, temperature)` plus referenced module/global/config state.
- Outputs / returns:
  - L449: `(content, new_msg_history)`
- Loops:
  - L443: {'line': 443, 'type': 'for', 'target': '(j, msg)', 'iter': 'enumerate(new_msg_history)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L277: IF `msg_history is None`; body=1 else=0
  - L280: IF `'claude' in model`; body=4 else=1
  - L440: IF `print_debug`; body=6 else=0
  - L312: IF `model.startswith('ollama/')`; body=4 else=1
  - L327: IF `'gpt' in model`; body=4 else=1
  - L338: IF `'o1' in model or 'o3' in model`; body=4 else=1
  - L349: IF `model == 'deepseek-coder-v2-0724'`; body=4 else=1
  - L364: IF `model == 'deepcoder-14b'`; body=3 else=1
  - L408: IF `model in ['meta-llama/llama-3.1-405b-instruct', 'llama-3-1-405b-instruct']`; body=4 else=1
  - L423: IF `'gemini' in model`; body=4 else=1
  - L402: IF `response.status_code == 200`; body=1 else=1
- Exception handling:
  - L366: handlers=['Exception'] else=0 final=0
- Raises:
  - L438: `ValueError(f'Model {model} not supported.')`
  - L405: `ValueError(f'Error from HuggingFace API: {response.text}')`
- LLM/VLM calls:
  - L292: `client.messages.create`
  - L314: `client.chat.completions.create`
  - L351: `client.chat.completions.create`
  - L367: `client.chat.completions.create`
  - L410: `client.chat.completions.create`
  - L425: `client.chat.completions.create`
- I/O / network / subprocess side effects:
  - L397: `requests.post`
- Main call graph hints: `backoff.on_exception`, `client.messages.create`, `model.startswith`, `print`, `enumerate`, `client.chat.completions.create`, `make_llm_call`, `model.replace`, `requests.post`, `ValueError`, `response.json`
#### `extract_json_between_markers(llm_output)` (L452)
- Inputs: parameters from signature `extract_json_between_markers(llm_output)` plus referenced module/global/config state.
- Outputs / returns:
  - L477: `None`
  - L466: `parsed_json`
  - L473: `parsed_json`
- Loops:
  - L462: {'line': 462, 'type': 'for', 'target': 'json_string', 'iter': 'matches', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L457: IF `not matches`; body=2 else=0
- Exception handling:
  - L464: handlers=['json.JSONDecodeError'] else=0 final=0
  - L469: handlers=['json.JSONDecodeError'] else=0 final=0
- I/O / network / subprocess side effects:
  - L465: `json.loads`
  - L472: `json.loads`
- Main call graph hints: `re.findall`, `json_string.strip`, `json.loads`, `re.sub`
#### `create_client(model)` (L480)
- Inputs: parameters from signature `create_client(model)` plus referenced module/global/config state.
- Outputs / returns:
  - L483: `(anthropic.Anthropic(), model)`
  - L487: `(anthropic.AnthropicBedrock(), client_model)`
  - L491: `(anthropic.AnthropicVertex(), client_model)`
  - L494: `(openai.OpenAI(api_key=os.environ.get('OLLAMA_API_KEY', ''), base_url='http://localhost:11434/v1'), model)`
  - L500: `(openai.OpenAI(), model)`
  - L503: `(openai.OpenAI(), model)`
  - L506: `(openai.OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'], base_url='https://api.deepseek.com'), model)`
  - L518: `(openai.OpenAI(api_key=os.environ['HUGGINGFACE_API_KEY'], base_url='https://api-inference.huggingface.co/models/agentica-org/DeepCoder-14B-Preview'), model)`
  - L527: `(openai.OpenAI(api_key=os.environ['OPENROUTER_API_KEY'], base_url='https://openrouter.ai/api/v1'), 'meta-llama/llama-3.1-405b-instruct')`
  - L536: `(openai.OpenAI(api_key=os.environ['GEMINI_API_KEY'], base_url='https://generativelanguage.googleapis.com/v1beta/openai/'), model)`
- Conditions / decisions:
  - L481: IF `model.startswith('claude-')`; body=2 else=1
  - L484: IF `model.startswith('bedrock') and 'claude' in model`; body=3 else=1
  - L488: IF `model.startswith('vertex_ai') and 'claude' in model`; body=3 else=1
  - L492: IF `model.startswith('ollama/')`; body=2 else=1
  - L498: IF `'gpt' in model`; body=2 else=1
  - L501: IF `'o1' in model or 'o3' in model`; body=2 else=1
  - L504: IF `model == 'deepseek-coder-v2-0724'`; body=2 else=1
  - L513: IF `model == 'deepcoder-14b'`; body=3 else=1
  - L516: IF `'HUGGINGFACE_API_KEY' not in os.environ`; body=1 else=0
  - L525: IF `model == 'llama3.1-405b'`; body=2 else=1
  - L534: IF `'gemini' in model`; body=2 else=1
- Raises:
  - L517: `ValueError('HUGGINGFACE_API_KEY environment variable not set')`
  - L544: `ValueError(f'Model {model} not supported.')`
- I/O / network / subprocess side effects:
  - L494: `openai.OpenAI`
  - L500: `openai.OpenAI`
  - L503: `openai.OpenAI`
  - L507: `openai.OpenAI`
  - L519: `openai.OpenAI`
  - L528: `openai.OpenAI`
  - L537: `openai.OpenAI`
- Main call graph hints: `model.startswith`, `print`, `anthropic.Anthropic`, `model.split`, `anthropic.AnthropicBedrock`, `anthropic.AnthropicVertex`, `openai.OpenAI`, `os.environ.get`, `ValueError`

---

## File: `ai_scientist/perform_icbinb_writeup.py`

**Lines:** 1293  


### Imports / external dependencies

- `import argparse`
- `import json`
- `import os`
- `import os.path as osp`
- `import re`
- `import shutil`
- `import subprocess`
- `import traceback`
- `import unicodedata`
- `import uuid`
- `import tempfile`
- `from ai_scientist.llm import ( get_response_from_llm, extract_json_between_markers, create_client, AVAILABLE_LLMS, )`
- `from ai_scientist.utils.token_tracker import track_token_usage`
- `from ai_scientist.tools.semantic_scholar import search_for_papers`
- `from ai_scientist.perform_vlm_review import ( generate_vlm_img_review, perform_imgs_cap_ref_review, perform_imgs_cap_ref_review_selection, detect_duplicate_figures, )`
- `from ai_scientist.vlm import create_client as create_vlm_client`

### Module-level assignments / constants

- L533: `writeup_system_message_template = """You are an ambitious AI researcher who is looking to publish a paper to the "I Can't Believe It's Not Better" (ICBINB) Workshop at ICLR 2025. This workshop aims to highlight real-world pitfalls, challenges, and negative or inconclusive results in deep learning...`
- L602: `writeup_prompt = """Your goal is to write up the following idea: ```markdown {idea_text} ``` We have the following experiment summaries (JSON): ```json {summaries} ``` We also have a script used to produce the final plots (use this to see how the plots are generated and what names are used in the...`

### Prompt-like assignments in this file

- L533 `writeup_system_message_template` — snippet: `writeup_system_message_template = """You are an ambitious AI researcher who is looking to publish a paper to the "I Can't Believe It's Not Better" (ICBINB) Workshop at ICLR 2025. This workshop aims to highlight real-world pitfalls, challenges, and negative or inconclusive results in deep learning, encouraging open discussion. You must accurately...`
- L602 `writeup_prompt` — snippet: `writeup_prompt = """Your goal is to write up the following idea: ```markdown {idea_text} ``` We have the following experiment summaries (JSON): ```json {summaries} ``` We also have a script used to produce the final plots (use this to see how the plots are generated and what names are used in the legend): ```python {aggregator_code} ``` Please a...`
- L342 `citation_system_msg_template` — snippet: `citation_system_msg_template = """You are an ambitious AI researcher who is looking to publish a paper to a workshop at ICLR 2025 that explores real-world pitfalls, failures, and challenges in deep learning. You have already completed the experiments and now you are looking to collect citations to related papers. This phase focuses on collecting...`
- L365 `citation_first_prompt_template` — snippet: `citation_first_prompt_template = """Round {current_round}/{total_rounds}: You planned and executed the following idea: ```markdown {Idea} ``` You produced the following report: ```markdown {report} ``` Your current list of citations is: ``` {citations} ``` Identify the most important citation that you still need to add, and the query to find the...`
- L403 `citation_second_prompt_template` — snippet: `citation_second_prompt_template = """Search has recovered the following articles: {papers} Respond in the following format: THOUGHT: <THOUGHT> RESPONSE: ```json <JSON> ``` In <THOUGHT>, briefly reason over the search results and identify which citation(s) best fit your paper. If none are appropriate or would contribute significantly to the write...`
- L526 `references_format` — snippet: `references_format = """% {description} {bibtex}"""`
- L981 `big_model_system_message` — snippet: `big_model_system_message = writeup_system_message_template.format( page_limit=page_limit )`
- L988 `combined_prompt` — snippet: `combined_prompt = writeup_prompt.format( idea_text=idea_text, summaries=combined_summaries_str, aggregator_code=aggregator_code, plot_list=", ".join(plot_names), latex_writeup=writeup_text, plot_descriptions=plot_descriptions_str, )`
- L1195 `final_reflection_prompt` — snippet: `final_reflection_prompt = """{reflection_page_info} USE MINIMAL EDITS TO OPTIMIZE THE PAGE LIMIT USAGE."""`
- L1051 `reflection_prompt` — snippet: `reflection_prompt = f""" Now let's reflect and identify any issues (including but not limited to): 1) Are there any LaTeX syntax errors or style violations we can fix? Refer to the chktex output below. 2) Is the writing clear, and scientifically rigorous for a workshop focusing on real-world pitfalls? 3) Have we included all relevant details fro...`
- L1126 `img_reflection_prompt` — snippet: `img_reflection_prompt = f"""Now let's reflect on The following figures are currently used in the paper: {sorted(used_figs)} The following figures are available in the folder but not used in the LaTeX: {sorted(unused_figs)} {reflection_page_info} The following is the VLM review on figures: {review_img_selection} Please review the figures and make...`

### Top-level decisions / loops / try blocks

- IF L1245: `__name__ == '__main__'`; body=10 else=0

### Classes

- None

### Functions

#### `remove_accents_and_clean(s)` (L33)
- Inputs: parameters from signature `remove_accents_and_clean(s)` plus referenced module/global/config state.
- Outputs / returns:
  - L42: `ascii_str`
- Main call graph hints: `unicodedata.normalize`, `nfkd_form.encode.decode`, `re.sub`, `ascii_str.lower`, `nfkd_form.encode`
#### `compile_latex(cwd, pdf_file, timeout)` (L45)
- Inputs: parameters from signature `compile_latex(cwd, pdf_file, timeout)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L55: {'line': 55, 'type': 'for', 'target': 'command', 'iter': 'commands', 'body_len': 1, 'orelse_len': 0}
- Exception handling:
  - L80: handlers=['FileNotFoundError'] else=0 final=0
  - L56: handlers=['subprocess.TimeoutExpired', 'subprocess.CalledProcessError'] else=0 final=0
- I/O / network / subprocess side effects:
  - L57: `subprocess.run`
- Main call graph hints: `print`, `shutil.move`, `subprocess.run`, `osp.join`, `traceback.format_exc`, `Constant.join`
#### `is_header_or_footer(line)` (L88)
- Docstring: Returns True if the line is likely a header or footer.
Filters out:
  - Lines that are too short (< 4 characters after stripping).
  - Lines that are only digits.
  - Lines starting with known phrases (e.g., "Under review").
  - Lines that consist solely of capital letters and spaces.
- Inputs: parameters from signature `is_header_or_footer(line)` plus referenced module/global/config state.
- Outputs / returns:
  - L108: `False`
  - L99: `True`
  - L107: `True`
- Loops:
  - L105: {'line': 105, 'type': 'for', 'target': 'pattern', 'iter': 'header_footer_patterns', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L98: IF `len(line_stripped) < 1`; body=1 else=0
  - L106: IF `re.match(pattern, line_stripped)`; body=1 else=0
- Main call graph hints: `line.strip`, `len`, `re.match`
#### `clean_lines(content)` (L111)
- Docstring: Given raw text content, split it into lines and remove lines that are
likely headers/footers or otherwise not part of the main content.
- Inputs: parameters from signature `clean_lines(content)` plus referenced module/global/config state.
- Outputs / returns:
  - L118: `[line for line in lines if not is_header_or_footer(line)]`
- Main call graph hints: `content.splitlines`, `is_header_or_footer`
#### `detect_references_position_clean(pdf_file)` (L121)
- Docstring: Locate the first occurrence of the word "References" (or variations like
"R EFERENCES") within the cleaned content extracted from the PDF.
Uses pdftotext with layout preservation and cleans the extracted text.

Returns a tuple (ref_page, ref_line) if found (with ref_line counting only
the cleaned lines), otherwise None.
- Inputs: parameters from signature `detect_references_position_clean(pdf_file)` plus referenced module/global/config state.
- Outputs / returns:
  - L183: `None`
  - L131: `None`
  - L182: `(page, idx + 1)`
- Loops:
  - L138: {'line': 138, 'type': 'for', 'target': 'page', 'iter': 'range(1, 51)', 'body_len': 5, 'orelse_len': 0}
  - L179: {'line': 179, 'type': 'for', 'target': '(idx, line)', 'iter': 'enumerate(cleaned)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L130: IF `not osp.exists(pdf_file)`; body=1 else=0
  - L158: IF `not osp.exists(page_txt)`; body=2 else=0
  - L180: IF `pattern.search(line)`; body=1 else=0
- Exception handling:
  - L141: handlers=['Exception'] else=0 final=0
  - L161: handlers=['Exception'] else=0 final=1
- I/O / network / subprocess side effects:
  - L142: `subprocess.run`
  - L162: `open`
- Main call graph hints: `re.compile`, `range`, `osp.exists`, `tempfile.mkdtemp`, `osp.join`, `clean_lines`, `enumerate`, `subprocess.run`, `pattern.search`, `shutil.rmtree`, `print`, `str`, `open`, `fp.read`, `traceback.format_exc`
#### `extract_page_line_counts(pdf_file, first_page, last_page)` (L186)
- Docstring: Extract the number of cleaned text lines for each page from first_page to last_page.
This uses pdftotext with layout preservation and the clean_lines helper.
Returns a dictionary {page_number: number_of_cleaned_lines}.
Pages for which extraction fails are omitted.
- Inputs: parameters from signature `extract_page_line_counts(pdf_file, first_page, last_page)` plus referenced module/global/config state.
- Outputs / returns:
  - L235: `page_lines`
- Loops:
  - L194: {'line': 194, 'type': 'for', 'target': 'page', 'iter': 'range(first_page, last_page + 1)', 'body_len': 5, 'orelse_len': 0}
- Conditions / decisions:
  - L214: IF `not osp.exists(page_txt)`; body=2 else=0
- Exception handling:
  - L197: handlers=['Exception'] else=0 final=0
  - L217: handlers=['Exception'] else=0 final=1
- I/O / network / subprocess side effects:
  - L198: `subprocess.run`
  - L218: `open`
- Main call graph hints: `range`, `tempfile.mkdtemp`, `osp.join`, `clean_lines`, `len`, `subprocess.run`, `osp.exists`, `shutil.rmtree`, `print`, `str`, `open`, `fp.read`, `traceback.format_exc`
#### `check_page_limit(pdf_file, page_limit, timeout)` (L238)
- Docstring: Compile the LaTeX project in a temporary folder, then determine where the
"References" section begins using cleaned text extraction. Next, count the
number of cleaned text lines used before the word "References" and compare that
to the total number of cleaned lines available in the allowed number of pages (page_limit).

Returns a dictionary with:
  - 'ref_page': page number where "References" was found (or None)
  - 'ref_line': cleaned line number within that page (or None)
  - 'used_lines': number of cleaned lines used for main content (before "References")
  - 'allowed_lines': total number of cleaned text lines available in pages 1..page_limit
  - 'excess': if used_lines > allowed_lines (number of lines over the limit),
  - 'available': if used_lines < allowed_lines (number of lines still available)

If compilation or extraction fails, returns None.
- Inputs: parameters from signature `check_page_limit(pdf_file, page_limit, timeout)` plus referenced module/global/config state.
- Outputs / returns:
  - L296: `result`
  - L258: `None`
  - L264: `None`
  - L271: `None`
  - L301: `None`
- Loops:
  - L281: {'line': 281, 'type': 'for', 'target': 'page', 'iter': 'range(1, ref_page)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L257: IF `not osp.exists(pdf_file)`; body=1 else=0
  - L262: IF `ref_pos is None`; body=1 else=0
  - L270: IF `not page_line_counts`; body=1 else=0
  - L292: IF `used_lines > allowed_lines`; body=1 else=1
- Exception handling:
  - L255: handlers=['Exception'] else=0 final=0
- Main call graph hints: `detect_references_position_clean`, `max`, `extract_page_line_counts`, `sum`, `range`, `osp.exists`, `page_line_counts.get`, `print`, `traceback.format_exc`
#### `get_reflection_page_info(reflection_pdf, page_limit)` (L304)
- Inputs: parameters from signature `get_reflection_page_info(reflection_pdf, page_limit)` plus referenced module/global/config state.
- Outputs / returns:
  - L334: `reflection_page_info`
- Conditions / decisions:
  - L306: IF `info is not None`; body=1 else=1
  - L307: IF `'excess' in info`; body=1 else=1
  - L315: IF `'available' in info`; body=1 else=1
- Main call graph hints: `check_page_limit`, `info.get`
#### `get_citation_addition(client, model, context, current_round, total_rounds, idea_text)` (L337)
- Inputs: parameters from signature `get_citation_addition(client, model, context, current_round, total_rounds, idea_text)` plus referenced module/global/config state.
- Outputs / returns:
  - L530: `(references_prompt, False)`
  - L458: `(None, False)`
  - L445: `(None, True)`
  - L454: `(None, False)`
  - L491: `(None, False)`
  - L519: `(None, False)`
  - L524: `(None, False)`
- Loops:
  - L461: {'line': 461, 'type': 'for', 'target': '(i, paper)', 'iter': 'enumerate(papers)', 'body_len': 1, 'orelse_len': 0}
  - L500: {'line': 500, 'type': 'for', 'target': 'x', 'iter': "selected_papers.strip('[]').split(',')", 'body_len': 2, 'orelse_len': 0}
  - L510: {'line': 510, 'type': 'for', 'target': 'bibtex', 'iter': 'bibtexs', 'body_len': 4, 'orelse_len': 0}
- Conditions / decisions:
  - L456: IF `papers is None`; body=2 else=0
  - L443: IF `'No more citations needed' in text`; body=2 else=0
  - L489: IF `'Do not add any' in text`; body=2 else=0
  - L498: IF `selected_papers != '[]'`; body=8 else=1
  - L502: IF `x_str`; body=1 else=0
- Exception handling:
  - L426: handlers=['Exception'] else=0 final=0
  - L474: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L427: `get_response_from_llm`
  - L475: `get_response_from_llm`
- Main call graph hints: `enumerate`, `Constant.join`, `references_format.format`, `get_response_from_llm`, `extract_json_between_markers`, `search_for_papers`, `print`, `paper_strings.append`, `str`, `Constant.format`, `selected_papers.strip.split`, `all`, `citation_first_prompt_template.format`, `citation_system_msg_template.format`, `traceback.format_exc`, `citation_second_prompt_template.format`, `x.strip.strip.strip`, `bibtex.find`, `remove_accents_and_clean`, `cleaned_bibtexs.append`, `selected_papers.strip`, `selected_indices.append`, `x.strip.strip`, `int`, `len`, `x.strip`
#### `load_idea_text(base_folder)` (L648)
- Docstring: Load the idea text from the base folder.
- Inputs: parameters from signature `load_idea_text(base_folder)` plus referenced module/global/config state.
- Outputs / returns:
  - L662: `idea_text`
- Conditions / decisions:
  - L654: IF `osp.exists(research_idea_path)`; body=1 else=2
  - L659: IF `osp.exists(idea_md_path)`; body=1 else=0
- I/O / network / subprocess side effects:
  - L655: `open`
  - L660: `open`
- Main call graph hints: `osp.join`, `osp.exists`, `open`, `f_idea.read`
#### `load_exp_summaries(base_folder)` (L665)
- Docstring: Load the experiment summaries from the base folder.
- Inputs: parameters from signature `load_exp_summaries(base_folder)` plus referenced module/global/config state.
- Outputs / returns:
  - L688: `loaded_summaries`
- Loops:
  - L675: {'line': 675, 'type': 'for', 'target': '(fname, key)', 'iter': 'summary_files', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L677: IF `osp.exists(path)`; body=1 else=1
- Exception handling:
  - L678: handlers=['json.JSONDecodeError'] else=0 final=0
- I/O / network / subprocess side effects:
  - L679: `open`
  - L680: `json.load`
- Main call graph hints: `osp.join`, `osp.exists`, `open`, `json.load`, `print`
#### `filter_experiment_summaries(exp_summaries, step_name)` (L691)
- Inputs: parameters from signature `filter_experiment_summaries(exp_summaries, step_name)` plus referenced module/global/config state.
- Outputs / returns:
  - L742: `filtered_summaries`
- Loops:
  - L722: {'line': 722, 'type': 'for', 'target': 'stage_name', 'iter': 'exp_summaries.keys()', 'body_len': 1, 'orelse_len': 0}
  - L725: {'line': 725, 'type': 'for', 'target': 'key', 'iter': 'exp_summaries[stage_name].keys()', 'body_len': 1, 'orelse_len': 0}
  - L735: {'line': 735, 'type': 'for', 'target': 'ablation_summary', 'iter': 'exp_summaries[stage_name]', 'body_len': 2, 'orelse_len': 0}
  - L728: {'line': 728, 'type': 'for', 'target': 'node_key', 'iter': 'exp_summaries[stage_name][key].keys()', 'body_len': 1, 'orelse_len': 0}
  - L737: {'line': 737, 'type': 'for', 'target': 'node_key', 'iter': 'ablation_summary.keys()', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L692: IF `step_name == 'citation_gathering'`; body=1 else=1
  - L699: IF `step_name == 'writeup'`; body=1 else=1
  - L723: IF `stage_name in {'BASELINE_SUMMARY', 'RESEARCH_SUMMARY'}`; body=2 else=1
  - L708: IF `step_name == 'plot_aggregation'`; body=1 else=1
  - L733: IF `stage_name == 'ABLATION_SUMMARY' and step_name == 'plot_aggregation'`; body=2 else=0
  - L726: IF `key in {'best node'}`; body=2 else=0
  - L729: IF `node_key in node_keys_to_keep`; body=1 else=0
  - L738: IF `node_key in node_keys_to_keep`; body=1 else=0
- Raises:
  - L719: `ValueError(f'Invalid step name: {step_name}')`
- Main call graph hints: `exp_summaries.keys`, `exp_summaries[...].keys`, `ValueError`, `exp_summaries[...][...].keys`, `ablation_summary.keys`
#### `gather_citations(base_folder, num_cite_rounds, small_model)` (L745)
- Docstring: Gather citations for a paper, with ability to resume from previous progress.

Args:
    base_folder: Path to project folder
    num_cite_rounds: Maximum number of citation gathering rounds
    small_model: Model to use for citation collection
    resume: Whether to try to resume from previous progress

Returns:
    str: The gathered citations text, or None if failed
- Inputs: parameters from signature `gather_citations(base_folder, num_cite_rounds, small_model)` plus referenced module/global/config state.
- Outputs / returns:
  - L849: `citations_text if citations_text else None`
  - L854: `citations_text if citations_text else None`
- Loops:
  - L793: {'line': 793, 'type': 'for', 'target': 'round_idx', 'iter': 'range(current_round, num_cite_rounds)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L767: IF `osp.exists(citations_cache_path) and osp.exists(progress_path)`; body=1 else=0
  - L805: IF `done`; body=3 else=0
  - L816: IF `addition is not None`; body=2 else=0
  - L819: IF `title_match`; body=4 else=0
  - L825: IF `new_title not in existing_titles`; body=3 else=0
- Exception handling:
  - L781: handlers=['Exception'] else=0 final=0
  - L768: handlers=['Exception'] else=0 final=0
  - L794: handlers=['Exception'] else=0 final=0
- I/O / network / subprocess side effects:
  - L788: `json.dumps`
  - L769: `open`
  - L771: `open`
  - L772: `json.load`
  - L807: `open`
  - L809: `open`
  - L810: `json.dump`
  - L843: `open`
  - L845: `open`
  - L846: `json.dump`
  - L828: `open`
  - L830: `open`
  - L831: `json.dump`
- Main call graph hints: `osp.join`, `osp.exists`, `load_idea_text`, `load_exp_summaries`, `filter_experiment_summaries`, `json.dumps`, `create_client`, `range`, `print`, `open`, `f.read`, `json.load`, `progress.get`, `get_citation_addition`, `traceback.format_exc`, `re.search`, `f.write`, `json.dump`, `title_match.group.lower`, `re.findall`, `t.lower`, `title_match.group`
#### `perform_writeup(base_folder, citations_text, no_writing, num_cite_rounds, small_model, big_model, n_writeup_reflections, page_limit)` (L857)
- Inputs: parameters from signature `perform_writeup(base_folder, citations_text, no_writing, num_cite_rounds, small_model, big_model, n_writeup_reflections, page_limit)` plus referenced module/global/config state.
- Outputs / returns:
  - L1237: `osp.exists(reflection_pdf)`
  - L919: `osp.exists(pdf_file)`
  - L1007: `False`
  - L1242: `False`
- Loops:
  - L877: {'line': 877, 'type': 'for', 'target': 'old_pdf', 'iter': 'os.listdir(base_folder)', 'body_len': 1, 'orelse_len': 0}
  - L1013: {'line': 1013, 'type': 'for', 'target': 'i', 'iter': 'range(n_writeup_reflections)', 'body_len': 25, 'orelse_len': 0}
  - L904: {'line': 904, 'type': 'for', 'target': 'fplot', 'iter': 'os.listdir(figures_dir)', 'body_len': 1, 'orelse_len': 0}
  - L955: {'line': 955, 'type': 'for', 'target': 'pf', 'iter': 'plot_names', 'body_len': 5, 'orelse_len': 0}
  - L972: {'line': 972, 'type': 'for', 'target': 'fname', 'iter': 'plot_names', 'body_len': 2, 'orelse_len': 0}
  - L1226: {'line': 1226, 'type': 'for', 'target': '(bad_str, repl_str)', 'iter': 'cleanup_map.items()', 'body_len': 1, 'orelse_len': 0}
  - L1107: {'line': 1107, 'type': 'for', 'target': '(bad_str, repl_str)', 'iter': 'cleanup_map.items()', 'body_len': 1, 'orelse_len': 0}
  - L1174: {'line': 1174, 'type': 'for', 'target': '(bad_str, repl_str)', 'iter': 'cleanup_map.items()', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L871: IF `osp.exists(latex_folder)`; body=1 else=0
  - L873: IF `osp.exists(pdf_file)`; body=1 else=0
  - L878: IF `old_pdf.endswith('.pdf') and 'reflection' in old_pdf`; body=1 else=0
  - L891: IF `not osp.exists(osp.join(latex_folder, 'template.tex'))`; body=1 else=0
  - L903: IF `osp.exists(figures_dir)`; body=1 else=0
  - L911: IF `osp.exists(aggregator_path)`; body=1 else=1
  - L917: IF `no_writing`; body=2 else=0
  - L922: IF `citations_text is None`; body=3 else=0
  - L943: IF `citations_text`; body=4 else=0
  - L1006: IF `not latex_code_match`; body=1 else=0
  - L1217: IF `reflection_code_match`; body=2 else=0
  - L924: IF `osp.exists(citations_cache_path)`; body=1 else=0
  - L934: IF `not citations_text`; body=2 else=0
  - L1098: IF `reflection_code_match`; body=2 else=2
  - L1156: IF `'I am done' in reflection_response`; body=2 else=0
  - L1165: IF `reflection_code_match`; body=2 else=2
  - L1219: IF `reflected_latex_code != current_latex`; body=6 else=1
  - L905: IF `fplot.lower().endswith('.png')`; body=1 else=0
  - L938: IF `citations_text is None`; body=2 else=0
  - L957: IF `not osp.exists(ppath)`; body=1 else=0
  - L964: IF `review_data`; body=1 else=1
  - L1100: IF `reflected_latex_code != current_latex`; body=6 else=2
  - L1167: IF `reflected_latex_code != current_latex`; body=6 else=2
- Exception handling:
  - L881: handlers=['Exception'] else=0 final=0
  - L952: handlers=['Exception'] else=0 final=0
  - L925: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L997: `get_response_from_llm`
  - L1197: `get_response_from_llm`
  - L1085: `get_response_from_llm`
  - L1147: `get_response_from_llm`
- I/O / network / subprocess side effects:
  - L874: `os.remove`
  - L888: `json.dumps`
  - L879: `os.remove`
  - L892: `shutil.copytree`
  - L897: `open`
  - L985: `open`
  - L1009: `open`
  - L1047: `os.popen.read`
  - L912: `open`
  - L944: `open`
  - L948: `open`
  - L1014: `open`
  - L1047: `os.popen`
  - L1230: `open`
  - L926: `open`
  - L1111: `open`
  - L1178: `open`
- Main call graph hints: `osp.join`, `osp.exists`, `os.listdir`, `shutil.rmtree`, `os.remove`, `load_idea_text`, `load_exp_summaries`, `filter_experiment_summaries`, `json.dumps`, `writeup_system_message_template.format`, `create_client`, `writeup_prompt.format`, `get_response_from_llm`, `re.search`, `latex_code_match.group.strip`, `range`, `get_reflection_page_info`, `print`, `old_pdf.endswith`, `shutil.copytree`, `open`, `f.read`, `compile_latex`, `content.replace`, `create_vlm_client`, `Constant.join`, `f.write`, `re.findall`, `set`, `perform_imgs_cap_ref_review`, `detect_duplicate_figures`, `os.popen.read`, `perform_imgs_cap_ref_review_selection`, `reflection_code_match.group.strip`, `osp.basename`, `fplot.lower.endswith`, `fa.read`, `gather_citations`, `generate_vlm_img_review`, `desc_map.get`, ...

---

## File: `ai_scientist/perform_ideation_temp_free.py`

**Lines:** 320  


### Imports / external dependencies

- `import argparse`
- `import json`
- `import os.path as osp`
- `import re`
- `import traceback`
- `from typing import Any, Dict, List`
- `import sys`
- `from ai_scientist.llm import ( AVAILABLE_LLMS, create_client, get_response_from_llm, )`
- `from ai_scientist.tools.semantic_scholar import SemanticScholarSearchTool`
- `from ai_scientist.tools.base_tool import BaseTool`

### Module-level assignments / constants

- L21: `semantic_scholar_tool = SemanticScholarSearchTool()`
- L24: `tools = [ semantic_scholar_tool, { "name": "FinalizeIdea", "description": """Finalize your idea by providing the idea details. The IDEA JSON should include the following fields: - "Name": A short descriptor of the idea. Lowercase, no spaces, underscores allowed. - "Title": A catchy and informativ...`
- L42: `tools_dict = {tool.name: tool for tool in tools if isinstance(tool, BaseTool)}`
- L45: `tool_descriptions = "\n\n".join( ( f"- **{tool.name}**: {tool.description}" if isinstance(tool, BaseTool) else f"- **{tool['name']}**: {tool['description']}" ) for tool in tools )`
- L55: `tool_names = [ f'"{tool.name}"' if isinstance(tool, BaseTool) else f'"{tool["name"]}"' for tool in tools ]`
- L59: `tool_names_str = ", ".join(tool_names)`
- L61: `system_prompt = f"""You are an experienced AI researcher who aims to propose high-impact research ideas resembling exciting grant proposals. Feel free to propose any novel ideas or experiments; make sure they are novel. Be very creative and think out of the box. Each proposal should stem from a s...`
- L99: `idea_generation_prompt = """{workshop_description} Here are the proposals that you have already generated: ''' {prev_ideas_string} ''' Begin by generating an interestingly new high-level research proposal that differs from what you have previously proposed. """`
- L111: `idea_reflection_prompt = """Round {current_round}/{num_reflections}. In your thoughts, first carefully consider the quality, novelty, and feasibility of the proposal you just created. Include any other factors that you think are important in evaluating the proposal. Ensure the proposal is clear a...`

### Prompt-like assignments in this file

- L45 `tool_descriptions` — snippet: `tool_descriptions = "\n\n".join( ( f"- **{tool.name}**: {tool.description}" if isinstance(tool, BaseTool) else f"- **{tool['name']}**: {tool['description']}" ) for tool in tools )`
- L61 `system_prompt` — snippet: `system_prompt = f"""You are an experienced AI researcher who aims to propose high-impact research ideas resembling exciting grant proposals. Feel free to propose any novel ideas or experiments; make sure they are novel. Be very creative and think out of the box. Each proposal should stem from a simple and elegant question, observation, or hypoth...`
- L99 `idea_generation_prompt` — snippet: `idea_generation_prompt = """{workshop_description} Here are the proposals that you have already generated: ''' {prev_ideas_string} ''' Begin by generating an interestingly new high-level research proposal that differs from what you have previously proposed. """`
- L111 `idea_reflection_prompt` — snippet: `idea_reflection_prompt = """Round {current_round}/{num_reflections}. In your thoughts, first carefully consider the quality, novelty, and feasibility of the proposal you just created. Include any other factors that you think are important in evaluating the proposal. Ensure the proposal is clear and concise, and the JSON is in the correct format....`
- L161 `prompt_text` — snippet: `prompt_text = idea_generation_prompt.format( workshop_description=workshop_description, prev_ideas_string=prev_ideas_string, )`
- L167 `prompt_text` — snippet: `prompt_text = idea_reflection_prompt.format( current_round=reflection_round + 1, num_reflections=num_reflections, last_tool_results=last_tool_results or "No new results.", )`

### Top-level decisions / loops / try blocks

- IF L269: `__name__ == '__main__'`; body=14 else=0

### Classes

- None

### Functions

#### `generate_temp_free_idea(idea_fname, client, model, workshop_description, max_num_generations, num_reflections, reload_ideas)` (L128)
- Inputs: parameters from signature `generate_temp_free_idea(idea_fname, client, model, workshop_description, max_num_generations, num_reflections, reload_ideas)` plus referenced module/global/config state.
- Outputs / returns:
  - L266: `ideas`
- Loops:
  - L148: {'line': 148, 'type': 'for', 'target': 'gen_idx', 'iter': 'range(max_num_generations)', 'body_len': 3, 'orelse_len': 0}
  - L142: {'line': 142, 'type': 'for', 'target': 'idea', 'iter': 'idea_str_content', 'body_len': 1, 'orelse_len': 0}
  - L158: {'line': 158, 'type': 'for', 'target': 'reflection_round', 'iter': 'range(num_reflections)', 'body_len': 3, 'orelse_len': 0}
- Conditions / decisions:
  - L139: IF `reload_ideas and osp.exists(idea_fname)`; body=1 else=1
  - L252: IF `idea_finalized`; body=1 else=0
  - L159: IF `reflection_round == 0`; body=1 else=1
  - L194: IF `not all([action_match, arguments_match])`; body=1 else=0
  - L203: IF `arguments_text.startswith('```json')`; body=1 else=0
  - L209: IF `action in tools_dict`; body=3 else=1
  - L225: IF `action == 'FinalizeIdea'`; body=1 else=2
  - L230: IF `not idea`; body=1 else=0
- Exception handling:
  - L151: handlers=['Exception'] else=0 final=0
  - L182: handlers=['Exception'] else=0 final=0
  - L213: handlers=['json.JSONDecodeError'] else=0 final=0
  - L219: handlers=['Exception'] else=0 final=0
  - L227: handlers=['json.JSONDecodeError'] else=0 final=0
- Raises:
  - L195: `ValueError('Failed to parse the LLM response.')`
  - L216: `ValueError(f'Invalid arguments JSON for {action}.')`
  - L231: `ValueError("Missing 'idea' in arguments.")`
  - L239: `ValueError('Invalid arguments JSON for FinalizeIdea.')`
- LLM/VLM calls:
  - L173: `get_response_from_llm`
- I/O / network / subprocess side effects:
  - L261: `json.loads`
  - L263: `open`
  - L264: `json.dump`
  - L140: `open`
  - L141: `json.load`
  - L143: `json.dumps`
  - L214: `json.loads`
  - L228: `json.loads`
  - L234: `json.dumps`
- Main call graph hints: `range`, `print`, `osp.exists`, `json.loads`, `open`, `json.dump`, `json.load`, `Constant.join`, `idea_str_archive.append`, `get_response_from_llm`, `traceback.print_exc`, `len`, `json.dumps`, `idea_generation_prompt.format`, `idea_reflection_prompt.format`, `re.search`, `action_match.group.strip`, `arguments_match.group.strip`, `arguments_text.startswith`, `all`, `ValueError`, `re.search.group`, `action_match.group`, `arguments_match.group`, `tool.use_tool`, `arguments_json.get`, `str`

---

## File: `ai_scientist/perform_llm_review.py`

**Lines:** 370  


### Imports / external dependencies

- `import os`
- `import json`
- `import numpy as np`
- `from pypdf import PdfReader`
- `import pymupdf`
- `import pymupdf4llm`
- `from ai_scientist.llm import ( get_response_from_llm, get_batch_responses_from_llm, extract_json_between_markers, )`

### Module-level assignments / constants

- L13: `reviewer_system_prompt_base = ( "You are an AI researcher who is reviewing a paper that was submitted to a prestigious ML venue." "Be critical and cautious in your decision." )`
- L17: `reviewer_system_prompt_neg = ( reviewer_system_prompt_base + "If a paper is bad or you are unsure, give it bad scores and reject it." )`
- L21: `reviewer_system_prompt_pos = ( reviewer_system_prompt_base + "If a paper is good or you are unsure, give it good scores and accept it." )`
- L26: `template_instructions = """ Respond in the following format: THOUGHT: <THOUGHT> REVIEW JSON: ```json <JSON> ``` In <THOUGHT>, first briefly discuss your intuitions and reasoning for the evaluation. Detail your high-level arguments, necessary choices and desired outcomes of the review. Do not make...`
- L64: `neurips_form = ( """ ## Review Form Below is a description of the questions you will be asked on the review form for each paper and some guidelines on what to consider when answering these questions. When writing your review, please keep in mind that after decisions have been made, reviews and me...`
- L236: `reviewer_reflection_prompt = """Round {current_round}/{num_reflections}. In your thoughts, first carefully consider the accuracy and soundness of the review you just created. Include any other factors that you think are important in evaluating the paper. Ensure the review is clear and concise, an...`
- L297: `dir_path = os.path.dirname(os.path.realpath(__file__))`
- L299: `fewshot_papers = [ os.path.join(dir_path, "fewshot_examples/132_automated_relational.pdf"), os.path.join(dir_path, "fewshot_examples/attention.pdf"), os.path.join(dir_path, "fewshot_examples/2_carpe_diem.pdf"), ]`
- L305: `fewshot_reviews = [ os.path.join(dir_path, "fewshot_examples/132_automated_relational.json"), os.path.join(dir_path, "fewshot_examples/attention.json"), os.path.join(dir_path, "fewshot_examples/2_carpe_diem.json"), ]`
- L343: `meta_reviewer_system_prompt = """You are an Area Chair at a machine learning conference. You are in charge of meta-reviewing a paper that was reviewed by {reviewer_count} reviewers. Your job is to aggregate the reviews into a single meta-review in the same format. Be critical and cautious in your...`

### Prompt-like assignments in this file

- L13 `reviewer_system_prompt_base` — snippet: `reviewer_system_prompt_base = ( "You are an AI researcher who is reviewing a paper that was submitted to a prestigious ML venue." "Be critical and cautious in your decision." )`
- L17 `reviewer_system_prompt_neg` — snippet: `reviewer_system_prompt_neg = ( reviewer_system_prompt_base + "If a paper is bad or you are unsure, give it bad scores and reject it." )`
- L21 `reviewer_system_prompt_pos` — snippet: `reviewer_system_prompt_pos = ( reviewer_system_prompt_base + "If a paper is good or you are unsure, give it good scores and accept it." )`
- L26 `template_instructions` — snippet: `template_instructions = """ Respond in the following format: THOUGHT: <THOUGHT> REVIEW JSON: ```json <JSON> ``` In <THOUGHT>, first briefly discuss your intuitions and reasoning for the evaluation. Detail your high-level arguments, necessary choices and desired outcomes of the review. Do not make generic comments here, but be specific to your cu...`
- L64 `neurips_form` — snippet: `neurips_form = ( """ ## Review Form Below is a description of the questions you will be asked on the review form for each paper and some guidelines on what to consider when answering these questions. When writing your review, please keep in mind that after decisions have been made, reviews and meta-reviews of accepted papers and opted-in rejecte...`
- L236 `reviewer_reflection_prompt` — snippet: `reviewer_reflection_prompt = """Round {current_round}/{num_reflections}. In your thoughts, first carefully consider the accuracy and soundness of the review you just created. Include any other factors that you think are important in evaluating the paper. Ensure the review is clear and concise, and the JSON is in the correct format. Do not make t...`
- L343 `meta_reviewer_system_prompt` — snippet: `meta_reviewer_system_prompt = """You are an Area Chair at a machine learning conference. You are in charge of meta-reviewing a paper that was reviewed by {reviewer_count} reviewers. Your job is to aggregate the reviews into a single meta-review in the same format. Be critical and cautious in your decision, find consensus, and respect the opinion...`
- L313 `fewshot_prompt` — snippet: `fewshot_prompt = """ Below are some sample reviews, copied from previous machine learning conferences. Note that while each review is formatted differently according to each reviewer's style, the reviews are well-structured and therefore easy to navigate. """`

### Classes

- None

### Functions

#### `perform_review(text, model, client, num_reflections, num_fs_examples, num_reviews_ensemble, temperature, msg_history, return_msg_history, reviewer_system_prompt, review_instruction_form)` (L125)
- Inputs: parameters from signature `perform_review(text, model, client, num_reflections, num_fs_examples, num_reviews_ensemble, temperature, msg_history, return_msg_history, reviewer_system_prompt, review_instruction_form)` plus referenced module/global/config state.
- Outputs / returns:
  - L231: `(review, msg_history)`
  - L233: `review`
- Loops:
  - L162: {'line': 162, 'type': 'for', 'target': '(idx, rev)', 'iter': 'enumerate(llm_reviews)', 'body_len': 1, 'orelse_len': 0}
  - L171: {'line': 171, 'type': 'for', 'target': '(score, limits)', 'iter': "[('Originality', (1, 4)), ('Quality', (1, 4)), ('Clarity', (1, 4)), ('Significance', (1, 4)), ('Soundness', (1, 4)), ('Presentation', (1, 4)), ('Contribution', (1, 4)), ('Overall', (1, 10)), ('Confidence', (1, 5))]", 'body_len': 3, 'orelse_len': 0}
  - L216: {'line': 216, 'type': 'for', 'target': 'j', 'iter': 'range(num_reflections - 1)', 'body_len': 4, 'orelse_len': 0}
  - L183: {'line': 183, 'type': 'for', 'target': 'r', 'iter': 'parsed_reviews', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L138: IF `num_fs_examples > 0`; body=2 else=1
  - L150: IF `num_reviews_ensemble > 1`; body=9 else=2
  - L215: IF `num_reflections > 1`; body=1 else=0
  - L230: IF `return_msg_history`; body=1 else=1
  - L169: IF `review is None`; body=1 else=0
  - L186: IF `scores`; body=1 else=0
  - L227: IF `'I am done' in text`; body=1 else=0
  - L184: IF `score in r and limits[0] <= r[score] <= limits[1]`; body=1 else=0
- Exception handling:
  - L163: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L151: `get_batch_responses_from_llm`
  - L204: `get_response_from_llm`
  - L217: `get_response_from_llm`
- I/O / network / subprocess side effects:
  - L198: `json.dumps`
- Main call graph hints: `get_review_fewshot_examples`, `get_batch_responses_from_llm`, `enumerate`, `get_meta_review`, `get_response_from_llm`, `extract_json_between_markers`, `range`, `parsed_reviews.append`, `int`, `print`, `scores.append`, `round`, `np.mean`, `json.dumps`
#### `load_paper(pdf_path, num_pages, min_size)` (L257)
- Inputs: parameters from signature `load_paper(pdf_path, num_pages, min_size)` plus referenced module/global/config state.
- Outputs / returns:
  - L288: `text`
- Loops:
  - L274: {'line': 274, 'type': 'for', 'target': 'page', 'iter': 'doc', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L259: IF `num_pages is None`; body=1 else=3
  - L265: IF `len(text) < min_size`; body=1 else=0
  - L271: IF `num_pages`; body=1 else=0
  - L276: IF `len(text) < min_size`; body=1 else=0
  - L281: IF `num_pages is None`; body=1 else=1
  - L286: IF `len(text) < min_size`; body=1 else=0
- Exception handling:
  - L258: handlers=['Exception'] else=0 final=0
  - L269: handlers=['Exception'] else=0 final=0
- Raises:
  - L266: `Exception('Text too short')`
  - L277: `Exception('Text too short')`
  - L287: `Exception('Text too short')`
- I/O / network / subprocess side effects:
  - L270: `pymupdf.open`
- Main call graph hints: `pymupdf4llm.to_markdown`, `PdfReader`, `min`, `len`, `Exception`, `print`, `pymupdf.open`, `list`, `page.get_text`, `Constant.join`, `range`, `page.extract_text`
#### `load_review(json_path)` (L291)
- Inputs: parameters from signature `load_review(json_path)` plus referenced module/global/config state.
- Outputs / returns:
  - L294: `loaded['review']`
- I/O / network / subprocess side effects:
  - L292: `open`
  - L293: `json.load`
- Main call graph hints: `open`, `json.load`
#### `get_review_fewshot_examples(num_fs_examples)` (L312)
- Inputs: parameters from signature `get_review_fewshot_examples(num_fs_examples)` plus referenced module/global/config state.
- Outputs / returns:
  - L340: `fewshot_prompt`
- Loops:
  - L317: {'line': 317, 'type': 'for', 'target': '(paper_path, review_path)', 'iter': 'zip(fewshot_papers[:num_fs_examples], fewshot_reviews[:num_fs_examples])', 'body_len': 4, 'orelse_len': 0}
- Conditions / decisions:
  - L321: IF `os.path.exists(txt_path)`; body=1 else=1
- I/O / network / subprocess side effects:
  - L322: `open`
- Main call graph hints: `zip`, `paper_path.replace`, `os.path.exists`, `load_review`, `load_paper`, `open`, `f.read`
#### `get_meta_review(model, client, temperature, reviews)` (L349)
- Inputs: parameters from signature `get_meta_review(model, client, temperature, reviews)` plus referenced module/global/config state.
- Outputs / returns:
  - L369: `meta_review`
- Loops:
  - L351: {'line': 351, 'type': 'for', 'target': '(i, r)', 'iter': 'enumerate(reviews)', 'body_len': 1, 'orelse_len': 0}
- LLM/VLM calls:
  - L359: `get_response_from_llm`
- I/O / network / subprocess side effects:
  - L355: `json.dumps`
- Main call graph hints: `enumerate`, `get_response_from_llm`, `extract_json_between_markers`, `meta_reviewer_system_prompt.format`, `len`, `json.dumps`

---

## File: `ai_scientist/perform_plotting.py`

**Lines:** 285  


### Imports / external dependencies

- `import argparse`
- `import json`
- `import os`
- `import re`
- `import shutil`
- `import subprocess`
- `import sys`
- `import traceback`
- `from rich import print`
- `from ai_scientist.llm import create_client, get_response_from_llm`
- `from ai_scientist.utils.token_tracker import token_tracker`
- `from ai_scientist.perform_icbinb_writeup import ( load_idea_text, load_exp_summaries, filter_experiment_summaries, )`

### Module-level assignments / constants

- L19: `MAX_FIGURES = 12`
- L21: `AGGREGATOR_SYSTEM_MSG = f"""You are an ambitious AI researcher who is preparing final plots for a scientific paper submission. You have multiple experiment summaries (baseline, research, ablation), each possibly containing references to different plots or numerical insights. There is also a top-l...`

### Prompt-like assignments in this file

- L21 `AGGREGATOR_SYSTEM_MSG` — snippet: `AGGREGATOR_SYSTEM_MSG = f"""You are an ambitious AI researcher who is preparing final plots for a scientific paper submission. You have multiple experiment summaries (baseline, research, ablation), each possibly containing references to different plots or numerical insights. There is also a top-level 'research_idea.md' file that outlines the ove...`
- L204 `reflection_prompt` — snippet: `reflection_prompt = f"""We have run your aggregator script and it produced {figure_count} figure(s). The script's output is: ``` {aggregator_out} ``` Please criticize the current script for any flaws including but not limited to: - Are these enough plots for a final paper submission? Don't create more than {MAX_FIGURES} plots. - Have you made su...`

### Top-level decisions / loops / try blocks

- IF L283: `__name__ == '__main__'`; body=1 else=0

### Classes

- None

### Functions

#### `build_aggregator_prompt(combined_summaries_str, idea_text)` (L52)
- Inputs: parameters from signature `build_aggregator_prompt(combined_summaries_str, idea_text)` plus referenced module/global/config state.
- Outputs / returns:
  - L53: `f"""\nWe have three JSON summaries of scientific experiments: baseline, research, ablation.\nThey may contain lists of figure descriptions, code to generate the figures, and paths to the .npy files containing the numerical results.\nOur goal is to produce final, publishable figures.\n\n--- RESEAR...`
#### `extract_code_snippet(text)` (L89)
- Docstring: Look for a Python code block in triple backticks in the LLM response.
Return only that code. If no code block is found, return the entire text.
- Inputs: parameters from signature `extract_code_snippet(text)` plus referenced module/global/config state.
- Outputs / returns:
  - L96: `matches[0].strip() if matches else text.strip()`
- Main call graph hints: `re.findall`, `matches[...].strip`, `text.strip`
#### `run_aggregator_script(aggregator_code, aggregator_script_path, base_folder, script_name)` (L99)
- Inputs: parameters from signature `run_aggregator_script(aggregator_code, aggregator_script_path, base_folder, script_name)` plus referenced module/global/config state.
- Outputs / returns:
  - L133: `aggregator_out`
  - L104: `''`
- Conditions / decisions:
  - L102: IF `not aggregator_code.strip()`; body=2 else=0
- Exception handling:
  - L113: handlers=['subprocess.CalledProcessError', 'Exception'] else=0 final=0
- I/O / network / subprocess side effects:
  - L105: `open`
  - L114: `subprocess.run`
- Main call graph hints: `print`, `aggregator_code.strip`, `open`, `f.write`, `subprocess.run`, `str`
#### `aggregate_plots(base_folder, model, n_reflections)` (L136)
- Inputs: parameters from signature `aggregate_plots(base_folder, model, n_reflections)` plus referenced module/global/config state.
- Outputs / returns:
  - L183: `None`
  - L176: `None`
  - L233: `None`
- Loops:
  - L191: {'line': 191, 'type': 'for', 'target': 'i', 'iter': 'range(n_reflections)', 'body_len': 9, 'orelse_len': 0}
- Conditions / decisions:
  - L144: IF `os.path.exists(aggregator_script_path)`; body=1 else=0
  - L146: IF `os.path.exists(figures_dir)`; body=2 else=0
  - L179: IF `not aggregator_code.strip()`; body=2 else=0
  - L194: IF `os.path.exists(figures_dir)`; body=1 else=0
  - L236: IF `figure_count > 0 and 'I am done' in reflection_response`; body=2 else=0
  - L243: IF `aggregator_new_code.strip() and aggregator_new_code.strip() != aggregator_code.strip()`; body=2 else=1
- Exception handling:
  - L164: handlers=['Exception'] else=0 final=0
  - L220: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L165: `get_response_from_llm`
  - L221: `get_response_from_llm`
- I/O / network / subprocess side effects:
  - L156: `json.dumps`
  - L145: `os.remove`
- Main call graph hints: `os.path.join`, `os.path.exists`, `load_idea_text`, `load_exp_summaries`, `filter_experiment_summaries`, `json.dumps`, `build_aggregator_prompt`, `create_client`, `extract_code_snippet`, `run_aggregator_script`, `range`, `os.remove`, `shutil.rmtree`, `print`, `get_response_from_llm`, `aggregator_code.strip`, `traceback.print_exc`, `len`, `aggregator_new_code.strip`, `os.listdir`, `os.path.isfile`
#### `main()` (L257)
- Inputs: parameters from signature `main()` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `aggregate_plots`

---

## File: `ai_scientist/perform_vlm_review.py`

**Lines:** 483  


### Imports / external dependencies

- `import os`
- `import hashlib`
- `import pymupdf`
- `import re`
- `import base64`
- `from ai_scientist.vlm import ( get_response_from_vlm, get_batch_responses_from_vlm, extract_json_between_markers, )`
- `from ai_scientist.perform_llm_review import load_paper`

### Module-level assignments / constants

- L28: `reviewer_system_prompt_base = ( "You are an AI researcher who is reviewing a paper that was submitted to a prestigious ML venue." "Be critical and cautious in your decision." )`
- L33: `img_cap_ref_review_prompt = """The abstract of the paper is: {abstract} You will be given an image via the vision API. As a careful scientist reviewer, your task is to: 1. Examine the provided image closely. 2. Describe in detail what the image shows in a scientific manner. 3. Critically analyze ...`
- L74: `img_cap_selection_prompt = """The abstract of the paper is: {abstract} You will be given an image via the vision API. As a careful scientist reviewer, your task is to: 1. Examine the provided image closely. 2. Describe in detail what the image shows in a scientific manner. 3. Critically analyze w...`
- L126: `img_review_prompt = """ You will be given an image via the vision API. As a careful scientist reviewer, your task is to: 1. Examine the provided image closely. 2. Describe in detail what the image shows in a scientific manner. You should: - Examine the figure in detail: conclude elements in figur...`

### Prompt-like assignments in this file

- L28 `reviewer_system_prompt_base` — snippet: `reviewer_system_prompt_base = ( "You are an AI researcher who is reviewing a paper that was submitted to a prestigious ML venue." "Be critical and cautious in your decision." )`
- L33 `img_cap_ref_review_prompt` — snippet: `img_cap_ref_review_prompt = """The abstract of the paper is: {abstract} You will be given an image via the vision API. As a careful scientist reviewer, your task is to: 1. Examine the provided image closely. 2. Describe in detail what the image shows in a scientific manner. 3. Critically analyze whether the image content aligns with the given ca...`
- L74 `img_cap_selection_prompt` — snippet: `img_cap_selection_prompt = """The abstract of the paper is: {abstract} You will be given an image via the vision API. As a careful scientist reviewer, your task is to: 1. Examine the provided image closely. 2. Describe in detail what the image shows in a scientific manner. 3. Critically analyze whether the image content aligns with the given cap...`
- L126 `img_review_prompt` — snippet: `img_review_prompt = """ You will be given an image via the vision API. As a careful scientist reviewer, your task is to: 1. Examine the provided image closely. 2. Describe in detail what the image shows in a scientific manner. You should: - Examine the figure in detail: conclude elements in figures (e.g. name of axis) and describe what informati...`
- L351 `prompt` — snippet: `prompt = img_cap_ref_review_prompt.format( abstract=abstract, caption=img["caption"], main_text_figrefs=img["main_text_figrefs"], )`
- L399 `messages` — snippet: `messages = [ { "role": "system", "content": ( "You are an expert at identifying duplicate or highly similar images. " "Please analyze these images and determine if they are duplicates or variations of the same visualization. " "Response format: reasoning, followed by `Duplicate figures: <list of duplicate figure names>`." "Make sure you use the ...`
- L451 `prompt` — snippet: `prompt = img_cap_selection_prompt.format( abstract=abstract, caption=img["caption"], main_text_figrefs=img["main_text_figrefs"], reflection_page_info=reflection_page_info, )`

### Classes

- None

### Functions

#### `encode_image_to_base64(image_data)` (L15)
- Docstring: Encode image data to base64 string.
- Inputs: parameters from signature `encode_image_to_base64(image_data)` plus referenced module/global/config state.
- Outputs / returns:
  - L19: `base64.b64encode(image_file.read()).decode('utf-8')`
  - L21: `base64.b64encode(image_data[0]).decode('utf-8')`
  - L23: `base64.b64encode(image_data).decode('utf-8')`
- Conditions / decisions:
  - L17: IF `isinstance(image_data, str)`; body=1 else=1
  - L20: IF `isinstance(image_data, list)`; body=1 else=1
  - L22: IF `isinstance(image_data, bytes)`; body=1 else=1
- Raises:
  - L25: `TypeError(f'Unsupported image data type: {type(image_data)}')`
- I/O / network / subprocess side effects:
  - L18: `open`
- Main call graph hints: `isinstance`, `open`, `base64.b64encode.decode`, `TypeError`, `base64.b64encode`, `image_file.read`, `type`
#### `extract_figure_screenshots(pdf_path, img_folder_path, num_pages, min_text_length, min_vertical_gap)` (L154)
- Docstring: Extract screenshots for figure captions ("Figure X." or "Figure X:")
and also gather text blocks (anywhere in the PDF) mentioning that
exact figure with "Figure", "Fig.", or "Fig-ure" (including line breaks).
Avoid partial matches, e.g. "Figure 11" doesn't match "Figure 1".
- Inputs: parameters from signature `extract_figure_screenshots(pdf_path, img_folder_path, num_pages, min_text_length, min_vertical_gap)` plus referenced module/global/config state.
- Outputs / returns:
  - L308: `result_pairs`
  - L205: `bool(subfigure_pattern.search(txt))`
- Loops:
  - L175: {'line': 175, 'type': 'for', 'target': 'page_num', 'iter': 'page_range', 'body_len': 2, 'orelse_len': 0}
  - L210: {'line': 210, 'type': 'for', 'target': 'page_num', 'iter': 'page_range', 'body_len': 5, 'orelse_len': 0}
  - L220: {'line': 220, 'type': 'for', 'target': 'blk', 'iter': 'page_blocks', 'body_len': 12, 'orelse_len': 0}
  - L180: {'line': 180, 'type': 'for', 'target': 'b', 'iter': 'blocks', 'body_len': 2, 'orelse_len': 0}
  - L231: {'line': 231, 'type': 'for', 'target': 'ab', 'iter': 'page_blocks', 'body_len': 1, 'orelse_len': 0}
  - L290: {'line': 290, 'type': 'for', 'target': 'tb', 'iter': 'text_blocks', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L223: IF `not m`; body=1 else=0
  - L251: IF `above_blocks`; body=2 else=1
  - L262: IF `clip_bottom > clip_top and clip_right > clip_left`; body=12 else=0
  - L182: IF `txt`; body=2 else=0
  - L232: IF `ab['bbox'].y1 < fig_y0`; body=5 else=0
  - L242: IF `len(ab['text']) >= min_text_length and (not is_subfigure_caption(ab['text'])) and (ab_height_gap >= min_vertical_gap) and (horiz_overlap_ratio > 0.3)`; body=1 else=0
  - L292: IF `tb is blk`; body=1 else=0
  - L295: IF `main_text_figure_pattern.search(tb['text'])`; body=1 else=0
- Exception handling:
  - L177: handlers=['Exception'] else=0 final=0
- I/O / network / subprocess side effects:
  - L167: `os.makedirs`
  - L168: `pymupdf.open`
- Main call graph hints: `os.makedirs`, `pymupdf.open`, `re.compile`, `range`, `bool`, `page_blocks.sort`, `len`, `min`, `page.get_text`, `subfigure_pattern.search`, `figure_caption_pattern.match`, `m.group`, `b[...].strip`, `print`, `max`, `pymupdf.Rect`, `page.get_pixmap`, `re.escape`, `os.path.join`, `pix.save`, `result_pairs.append`, `text_blocks.append`, `hashlib.md5.hexdigest`, `main_text_figure_pattern.search`, `above_blocks.append`, `references_in_doc.append`, `float`, `is_subfigure_caption`, `hashlib.md5`, `JoinedStr.encode`
#### `extract_abstract(text)` (L311)
- Inputs: parameters from signature `extract_abstract(text)` plus referenced module/global/config state.
- Outputs / returns:
  - L347: `abstract_text`
  - L333: `''`
- Loops:
  - L321: {'line': 321, 'type': 'for', 'target': '(i, line)', 'iter': 'enumerate(lines)', 'body_len': 2, 'orelse_len': 0}
  - L337: {'line': 337, 'type': 'for', 'target': 'j', 'iter': 'range(abstract_start + 1, len(lines))', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L331: IF `abstract_start is None`; body=1 else=0
  - L324: IF `match`; body=2 else=0
  - L339: IF `heading_pattern.match(lines[j])`; body=1 else=0
  - L327: IF `'abstract' in heading_text.lower()`; body=2 else=0
- Main call graph hints: `text.split`, `re.compile`, `enumerate`, `range`, `Constant.join.strip`, `heading_pattern.match`, `len`, `abstract_lines.append`, `match.group`, `Constant.join`, `heading_text.lower`
#### `generate_vlm_img_cap_ref_review(img, abstract, model, client)` (L350)
- Inputs: parameters from signature `generate_vlm_img_cap_ref_review(img, abstract, model, client)` plus referenced module/global/config state.
- Outputs / returns:
  - L360: `img_cap_ref_review_json`
- LLM/VLM calls:
  - L356: `get_response_from_vlm`
- Main call graph hints: `img_cap_ref_review_prompt.format`, `get_response_from_vlm`, `extract_json_between_markers`
#### `generate_vlm_img_review(img, model, client)` (L363)
- Inputs: parameters from signature `generate_vlm_img_review(img, model, client)` plus referenced module/global/config state.
- Outputs / returns:
  - L369: `img_review_json`
- LLM/VLM calls:
  - L365: `get_response_from_vlm`
- Main call graph hints: `get_response_from_vlm`, `extract_json_between_markers`
#### `perform_imgs_cap_ref_review(client, client_model, pdf_path)` (L372)
- Inputs: parameters from signature `perform_imgs_cap_ref_review(client, client_model, pdf_path)` plus referenced module/global/config state.
- Outputs / returns:
  - L386: `img_reviews`
- Loops:
  - L383: {'line': 383, 'type': 'for', 'target': 'img', 'iter': 'img_pairs', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L378: IF `not os.path.exists(img_folder_path)`; body=1 else=0
- I/O / network / subprocess side effects:
  - L379: `os.makedirs`
- Main call graph hints: `load_paper`, `os.path.join`, `extract_figure_screenshots`, `extract_abstract`, `os.path.dirname`, `os.path.exists`, `os.makedirs`, `generate_vlm_img_cap_ref_review`, `os.path.splitext`, `os.path.basename`
#### `detect_duplicate_figures(client, client_model, pdf_path)` (L389)
- Inputs: parameters from signature `detect_duplicate_figures(client, client_model, pdf_path)` plus referenced module/global/config state.
- Outputs / returns:
  - L441: `analysis`
  - L445: `{'error': str(e)}`
- Loops:
  - L422: {'line': 422, 'type': 'for', 'target': 'img_info', 'iter': 'img_pairs', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L395: IF `not os.path.exists(img_folder_path)`; body=1 else=0
- Exception handling:
  - L432: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L433: `client.chat.completions.create`
- I/O / network / subprocess side effects:
  - L396: `os.makedirs`
- Main call graph hints: `load_paper`, `os.path.join`, `extract_figure_screenshots`, `os.path.dirname`, `os.path.exists`, `os.makedirs`, `messages[...][...].append`, `client.chat.completions.create`, `print`, `str`, `os.path.splitext`, `os.path.basename`, `encode_image_to_base64`
#### `generate_vlm_img_selection_review(img, abstract, model, client, reflection_page_info)` (L448)
- Inputs: parameters from signature `generate_vlm_img_selection_review(img, abstract, model, client, reflection_page_info)` plus referenced module/global/config state.
- Outputs / returns:
  - L461: `img_cap_ref_review_json`
- LLM/VLM calls:
  - L457: `get_response_from_vlm`
- Main call graph hints: `img_cap_selection_prompt.format`, `get_response_from_vlm`, `extract_json_between_markers`
#### `perform_imgs_cap_ref_review_selection(client, client_model, pdf_path, reflection_page_info)` (L464)
- Inputs: parameters from signature `perform_imgs_cap_ref_review_selection(client, client_model, pdf_path, reflection_page_info)` plus referenced module/global/config state.
- Outputs / returns:
  - L482: `img_reviews`
- Loops:
  - L477: {'line': 477, 'type': 'for', 'target': 'img', 'iter': 'img_pairs', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L472: IF `not os.path.exists(img_folder_path)`; body=1 else=0
- I/O / network / subprocess side effects:
  - L473: `os.makedirs`
- Main call graph hints: `load_paper`, `os.path.join`, `extract_figure_screenshots`, `extract_abstract`, `os.path.dirname`, `os.path.exists`, `os.makedirs`, `generate_vlm_img_selection_review`, `os.path.splitext`, `os.path.basename`

---

## File: `ai_scientist/perform_writeup.py`

**Lines:** 811  


### Imports / external dependencies

- `import argparse`
- `import json`
- `import os`
- `import os.path as osp`
- `import re`
- `import shutil`
- `import subprocess`
- `import traceback`
- `import unicodedata`
- `import uuid`
- `from ai_scientist.llm import ( get_response_from_llm, extract_json_between_markers, create_client, AVAILABLE_LLMS, )`
- `from ai_scientist.tools.semantic_scholar import search_for_papers`
- `from ai_scientist.perform_vlm_review import generate_vlm_img_review`
- `from ai_scientist.vlm import create_client as create_vlm_client`

### Module-level assignments / constants

- L345: `writeup_system_message_template = """You are an ambitious AI researcher who is looking to publish a paper that will contribute significantly to the field. Ensure that the paper is scientifically accurate, objective, and truthful. Accurately report the experimental results, even if they are negati...`
- L410: `writeup_prompt = """Your goal is to write up the following idea: ```markdown {idea_text} ``` We have the following experiment summaries (JSON): ```json {summaries} ``` We also have a script used to produce the final plots (use this to see how the plots are generated and what names are used in the...`

### Prompt-like assignments in this file

- L345 `writeup_system_message_template` — snippet: `writeup_system_message_template = """You are an ambitious AI researcher who is looking to publish a paper that will contribute significantly to the field. Ensure that the paper is scientifically accurate, objective, and truthful. Accurately report the experimental results, even if they are negative or inconclusive. You are planning to submit to ...`
- L410 `writeup_prompt` — snippet: `writeup_prompt = """Your goal is to write up the following idea: ```markdown {idea_text} ``` We have the following experiment summaries (JSON): ```json {summaries} ``` We also have a script used to produce the final plots (use this to see how the plots are generated and what names are used in the legend): ```python {aggregator_code} ``` Please a...`
- L154 `citation_system_msg_template` — snippet: `citation_system_msg_template = """You are an ambitious AI researcher who is looking to publish a paper to a top-tier ML conference that will contribute significantly to the field. You have already completed the experiments and now you are looking to collect citations to related papers. This phase focuses on collecting references and annotating t...`
- L176 `citation_first_prompt_template` — snippet: `citation_first_prompt_template = """Round {current_round}/{total_rounds}: You planned and executed the following idea: ```markdown {Idea} ``` You produced the following report: ```markdown {report} ``` Your current list of citations is: ``` {citations} ``` Identify the most important citation that you still need to add, and the query to find the...`
- L214 `citation_second_prompt_template` — snippet: `citation_second_prompt_template = """Search has recovered the following articles: {papers} Respond in the following format: THOUGHT: <THOUGHT> RESPONSE: ```json <JSON> ``` In <THOUGHT>, first briefly reason over the search results and identify which citation(s) best fit your paper. If none are appropriate or would contribute significantly to the...`
- L337 `references_format` — snippet: `references_format = """% {description} {bibtex}"""`
- L622 `big_model_system_message` — snippet: `big_model_system_message = writeup_system_message_template.format( page_limit=page_limit )`
- L629 `combined_prompt` — snippet: `combined_prompt = writeup_prompt.format( idea_text=idea_text, summaries=combined_summaries_str, aggregator_code=aggregator_code, plot_list=", ".join(plot_names), latex_writeup=writeup_text, plot_descriptions=plot_descriptions_str, )`
- L688 `reflection_prompt` — snippet: `reflection_prompt = f""" Now let's reflect and identify any issues (including but not limited to): 1) Are there any LaTeX syntax errors or style violations we can fix? Refer to the chktex output below. 2) Is the writing clear, and scientifically rigorous? 3) Have we included all relevant details from the summaries without hallucinating? 4) The f...`

### Top-level decisions / loops / try blocks

- IF L763: `__name__ == '__main__'`; body=10 else=0

### Classes

- None

### Functions

#### `remove_accents_and_clean(s)` (L25)
- Inputs: parameters from signature `remove_accents_and_clean(s)` plus referenced module/global/config state.
- Outputs / returns:
  - L36: `ascii_str`
- Main call graph hints: `unicodedata.normalize`, `nfkd_form.encode.decode`, `re.sub`, `ascii_str.lower`, `nfkd_form.encode`
#### `compile_latex(cwd, pdf_file, timeout)` (L39)
- Inputs: parameters from signature `compile_latex(cwd, pdf_file, timeout)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L49: {'line': 49, 'type': 'for', 'target': 'command', 'iter': 'commands', 'body_len': 1, 'orelse_len': 0}
- Exception handling:
  - L74: handlers=['FileNotFoundError'] else=0 final=0
  - L50: handlers=['subprocess.TimeoutExpired', 'subprocess.CalledProcessError'] else=0 final=0
- I/O / network / subprocess side effects:
  - L51: `subprocess.run`
- Main call graph hints: `print`, `shutil.move`, `subprocess.run`, `osp.join`, `traceback.format_exc`, `Constant.join`
#### `detect_pages_before_impact(latex_folder, timeout)` (L82)
- Docstring: Temporarily copy the latex folder, compile, and detect on which page
the phrase "Impact Statement" appears.
Returns a tuple (page_number, line_number) if found, otherwise None.
- Inputs: parameters from signature `detect_pages_before_impact(latex_folder, timeout)` plus referenced module/global/config state.
- Outputs / returns:
  - L142: `None`
  - L114: `None`
  - L144: `None`
  - L110: `None`
  - L141: `(i, idx + 1)`
- Loops:
  - L99: {'line': 99, 'type': 'for', 'target': 'command', 'iter': 'commands', 'body_len': 1, 'orelse_len': 0}
  - L117: {'line': 117, 'type': 'for', 'target': 'i', 'iter': 'range(1, 51)', 'body_len': 6, 'orelse_len': 0}
  - L139: {'line': 139, 'type': 'for', 'target': '(idx, line)', 'iter': 'enumerate(lines)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L113: IF `not osp.exists(temp_pdf_file)`; body=1 else=0
  - L134: IF `not osp.exists(page_txt)`; body=1 else=0
  - L140: IF `'Impact Statement' in line`; body=1 else=0
- Exception handling:
  - L89: handlers=['Exception'] else=0 final=1
  - L100: handlers=['(subprocess.TimeoutExpired, subprocess.CalledProcessError)'] else=0 final=0
- I/O / network / subprocess side effects:
  - L90: `shutil.copytree`
  - L119: `subprocess.run`
  - L101: `subprocess.run`
  - L136: `open`
- Main call graph hints: `osp.join`, `shutil.copytree`, `range`, `shutil.rmtree`, `osp.exists`, `subprocess.run`, `page_content.split`, `enumerate`, `open`, `fp.read`, `uuid.uuid4`, `str`
#### `get_citation_addition(client, model, context, current_round, total_rounds, idea_text)` (L149)
- Inputs: parameters from signature `get_citation_addition(client, model, context, current_round, total_rounds, idea_text)` plus referenced module/global/config state.
- Outputs / returns:
  - L341: `(references_prompt, False)`
  - L269: `(None, False)`
  - L256: `(None, True)`
  - L265: `(None, False)`
  - L302: `(None, False)`
  - L330: `(None, False)`
  - L335: `(None, False)`
- Loops:
  - L272: {'line': 272, 'type': 'for', 'target': '(i, paper)', 'iter': 'enumerate(papers)', 'body_len': 1, 'orelse_len': 0}
  - L311: {'line': 311, 'type': 'for', 'target': 'x', 'iter': "selected_papers.strip('[]').split(',')", 'body_len': 2, 'orelse_len': 0}
  - L321: {'line': 321, 'type': 'for', 'target': 'bibtex', 'iter': 'bibtexs', 'body_len': 4, 'orelse_len': 0}
- Conditions / decisions:
  - L267: IF `papers is None`; body=2 else=0
  - L254: IF `'No more citations needed' in text`; body=2 else=0
  - L300: IF `'Do not add any' in text`; body=2 else=0
  - L309: IF `selected_papers != '[]'`; body=8 else=1
  - L313: IF `x_str`; body=1 else=0
- Exception handling:
  - L237: handlers=['Exception'] else=0 final=0
  - L285: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L238: `get_response_from_llm`
  - L286: `get_response_from_llm`
- Main call graph hints: `enumerate`, `Constant.join`, `references_format.format`, `get_response_from_llm`, `extract_json_between_markers`, `search_for_papers`, `print`, `paper_strings.append`, `str`, `Constant.format`, `selected_papers.strip.split`, `all`, `citation_first_prompt_template.format`, `citation_system_msg_template.format`, `traceback.format_exc`, `citation_second_prompt_template.format`, `x.strip.strip.strip`, `bibtex.find`, `remove_accents_and_clean`, `cleaned_bibtexs.append`, `selected_papers.strip`, `selected_indices.append`, `x.strip.strip`, `int`, `len`, `x.strip`
#### `perform_writeup(base_folder, no_writing, num_cite_rounds, small_model, big_model, n_writeup_reflections, page_limit)` (L455)
- Inputs: parameters from signature `perform_writeup(base_folder, no_writing, num_cite_rounds, small_model, big_model, n_writeup_reflections, page_limit)` plus referenced module/global/config state.
- Outputs / returns:
  - L755: `osp.exists(base_pdf_file + f'_{compile_attempt - 1}.pdf')`
  - L540: `osp.exists(base_pdf_file + '.pdf')`
  - L648: `False`
  - L760: `False`
- Loops:
  - L494: {'line': 494, 'type': 'for', 'target': '(fname, key)', 'iter': 'summary_files', 'body_len': 2, 'orelse_len': 0}
  - L544: {'line': 544, 'type': 'for', 'target': 'round_idx', 'iter': 'range(num_cite_rounds)', 'body_len': 2, 'orelse_len': 0}
  - L654: {'line': 654, 'type': 'for', 'target': 'i', 'iter': 'range(n_writeup_reflections)', 'body_len': 17, 'orelse_len': 0}
  - L525: {'line': 525, 'type': 'for', 'target': 'fplot', 'iter': 'os.listdir(figures_dir)', 'body_len': 1, 'orelse_len': 0}
  - L594: {'line': 594, 'type': 'for', 'target': 'pf', 'iter': 'plot_names', 'body_len': 5, 'orelse_len': 0}
  - L612: {'line': 612, 'type': 'for', 'target': 'fname', 'iter': 'plot_names', 'body_len': 2, 'orelse_len': 0}
  - L736: {'line': 736, 'type': 'for', 'target': '(bad_str, repl_str)', 'iter': 'cleanup_map.items()', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L469: IF `osp.exists(latex_folder)`; body=1 else=0
  - L478: IF `osp.exists(research_idea_path)`; body=1 else=2
  - L512: IF `not osp.exists(osp.join(latex_folder, 'template.tex'))`; body=1 else=0
  - L524: IF `osp.exists(figures_dir)`; body=1 else=0
  - L532: IF `osp.exists(aggregator_path)`; body=1 else=1
  - L538: IF `no_writing`; body=2 else=0
  - L647: IF `not latex_code_match`; body=1 else=0
  - L483: IF `osp.exists(idea_md_path)`; body=1 else=0
  - L496: IF `osp.exists(path)`; body=1 else=1
  - L674: IF `impact_loc is not None`; body=2 else=1
  - L718: IF `'I am done' in reflection_response`; body=2 else=0
  - L727: IF `reflection_code_match`; body=2 else=2
  - L526: IF `fplot.lower().endswith('.png')`; body=1 else=0
  - L553: IF `references_bib is None`; body=1 else=0
  - L566: IF `done`; body=1 else=0
  - L569: IF `addition is not None`; body=2 else=0
  - L596: IF `not osp.exists(ppath)`; body=1 else=0
  - L603: IF `review_data`; body=1 else=1
  - L729: IF `reflected_latex_code != current_latex`; body=8 else=2
  - L572: IF `title_match`; body=4 else=0
  - L578: IF `new_title not in existing_titles`; body=3 else=0
- Exception handling:
  - L474: handlers=['Exception'] else=0 final=0
  - L591: handlers=['Exception'] else=0 final=0
  - L547: handlers=['Exception'] else=0 final=0
  - L497: handlers=['json.JSONDecodeError'] else=0 final=0
- Raises:
  - L554: `ValueError('No references.bib found in template.tex')`
- LLM/VLM calls:
  - L638: `get_response_from_llm`
  - L709: `get_response_from_llm`
- I/O / network / subprocess side effects:
  - L509: `json.dumps`
  - L513: `shutil.copytree`
  - L518: `open`
  - L626: `open`
  - L650: `open`
  - L684: `os.popen.read`
  - L479: `open`
  - L533: `open`
  - L545: `open`
  - L655: `open`
  - L484: `open`
  - L684: `os.popen`
  - L498: `open`
  - L499: `json.load`
  - L740: `open`
  - L583: `open`
- Main call graph hints: `osp.join`, `osp.exists`, `shutil.rmtree`, `json.dumps`, `create_client`, `range`, `writeup_system_message_template.format`, `writeup_prompt.format`, `get_response_from_llm`, `re.search`, `latex_code_match.group.strip`, `shutil.copytree`, `open`, `f.read`, `os.listdir`, `compile_latex`, `create_vlm_client`, `Constant.join`, `f.write`, `re.findall`, `set`, `print`, `detect_pages_before_impact`, `os.popen.read`, `osp.basename`, `f_idea.read`, `fplot.lower.endswith`, `fa.read`, `references_bib.group`, `get_citation_addition`, `generate_vlm_img_review`, `desc_map.get`, `plot_descriptions_list.append`, `latex_code_match.group`, `reflection_code_match.group.strip`, `traceback.format_exc`, `plot_names.append`, `ValueError`, `review_data.get`, `os.path.basename`, ...

---

## File: `ai_scientist/tools/__init__.py`

**Lines:** 1  


### Imports / external dependencies

- None

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

- None

---

## File: `ai_scientist/tools/base_tool.py`

**Lines:** 29  


### Imports / external dependencies

- `from abc import ABC, abstractmethod`
- `from typing import Any, Dict, List`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

#### Class `BaseTool` (L5)
- Bases: `ABC`
- Docstring: An abstract base class for defining custom tools.

Attributes:
-----------
- name (str): The name of the tool.
- description (str): A short description of what the tool does.
- parameters (list): A list of parameters that the tool requires, each parameter should be a dictionary with 'name', 'type', and 'description' key/value pairs.

Usage:
------
To use this class, you should subclass it and provide an implementation for the `use_tool` abstract method.
##### `__init__(self, name, description, parameters)` (L20)
- Inputs: parameters from signature `__init__(self, name, description, parameters)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `use_tool(self, **kwargs)` (L26)
- Docstring: Abstract method that should be implemented by subclasses to define the functionality of the tool.
- Inputs: parameters from signature `use_tool(self, **kwargs)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).

### Functions

- None

---

## File: `ai_scientist/tools/semantic_scholar.py`

**Lines:** 139  


### Imports / external dependencies

- `import os`
- `import requests`
- `import time`
- `import warnings`
- `from typing import Dict, List, Optional, Union`
- `import backoff`
- `from ai_scientist.tools.base_tool import BaseTool`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

#### Class `SemanticScholarSearchTool` (L19)
- Bases: `BaseTool`
##### `__init__(self, name, description, max_results)` (L20)
- Inputs: parameters from signature `__init__(self, name, description, max_results)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Conditions / decisions:
  - L39: IF `not self.S2_API_KEY`; body=1 else=0
- Main call graph hints: `super.__init__`, `os.getenv`, `warnings.warn`, `super`
##### `use_tool(self, query)` (L45)
- Inputs: parameters from signature `use_tool(self, query)` plus referenced module/global/config state.
- Outputs / returns:
  - L48: `self.format_papers(papers)`
  - L50: `'No papers found.'`
- Conditions / decisions:
  - L47: IF `papers`; body=1 else=1
- Main call graph hints: `self.search_for_papers`, `self.format_papers`
##### `search_for_papers(self, query)` (L57)
- Inputs: parameters from signature `search_for_papers(self, query)` plus referenced module/global/config state.
- Outputs / returns:
  - L85: `papers`
  - L59: `None`
  - L80: `None`
- Conditions / decisions:
  - L58: IF `not query`; body=1 else=0
  - L62: IF `self.S2_API_KEY`; body=1 else=0
  - L79: IF `total == 0`; body=1 else=0
- I/O / network / subprocess side effects:
  - L65: `requests.get`
- Main call graph hints: `backoff.on_exception`, `requests.get`, `print`, `rsp.raise_for_status`, `rsp.json`, `results.get`, `papers.sort`, `x.get`
##### `format_papers(self, papers)` (L87)
- Inputs: parameters from signature `format_papers(self, papers)` plus referenced module/global/config state.
- Outputs / returns:
  - L98: `'\n\n'.join(paper_strings)`
- Loops:
  - L89: {'line': 89, 'type': 'for', 'target': '(i, paper)', 'iter': 'enumerate(papers)', 'body_len': 2, 'orelse_len': 0}
- Main call graph hints: `enumerate`, `Constant.join`, `paper_strings.append`, `author.get`, `paper.get`

### Functions

#### `on_backoff(details)` (L12)
- Inputs: parameters from signature `on_backoff(details)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `print`, `time.strftime`
#### `search_for_papers(query, result_limit)` (L104)
- Inputs: parameters from signature `search_for_papers(query, result_limit)` plus referenced module/global/config state.
- Outputs / returns:
  - L138: `papers`
  - L115: `None`
  - L135: `None`
- Conditions / decisions:
  - L107: IF `not S2_API_KEY`; body=1 else=1
  - L114: IF `not query`; body=1 else=0
  - L134: IF `not total`; body=1 else=0
- I/O / network / subprocess side effects:
  - L117: `requests.get`
- Main call graph hints: `backoff.on_exception`, `os.getenv`, `requests.get`, `print`, `rsp.raise_for_status`, `rsp.json`, `time.sleep`, `warnings.warn`

---

## File: `ai_scientist/treesearch/__init__.py`

**Lines:** 1  


### Imports / external dependencies

- None

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

- None

---

## File: `ai_scientist/treesearch/agent_manager.py`

**Lines:** 1222  


### Imports / external dependencies

- `from typing import List, Optional, Dict, Callable, Any, Tuple`
- `import pickle`
- `from dataclasses import dataclass`
- `from enum import Enum, auto`
- `from pathlib import Path`
- `import logging`
- `from .parallel_agent import ParallelAgent`
- `from .journal import Journal, Node`
- `import copy`
- `import re`
- `from .backend import query, FunctionSpec`
- `import json`
- `from rich import print`
- `from .utils.serialize import parse_markdown_to_dict`
- `from .utils.metric import WorstMetricValue`

### Module-level assignments / constants

- L18: `logger = logging.getLogger(__name__)`
- L21: `stage_config_spec = FunctionSpec( name="generate_stage_config", description="Generate configuration for the next experimental stage", json_schema={ "type": "object", "properties": { "name": { "type": "string", "description": "Brief, descriptive name for the stage", }, "description": { "type": "st...`
- L49: `stage_progress_eval_spec = FunctionSpec( name="evaluate_stage_progression", description="Evaluate readiness to progress to next experimental stage", json_schema={ "type": "object", "properties": { "ready_for_next_stage": { "type": "boolean", "description": "Whether the experiment is ready to prog...`
- L78: `stage_completion_eval_spec = FunctionSpec( name="evaluate_stage_completion", description="Evaluate if the current stage is complete", json_schema={ "type": "object", "properties": { "is_complete": { "type": "boolean", "description": "Whether the current stage is complete", }, "reasoning": { "type...`

### Prompt-like assignments in this file

- L352 `eval_prompt` — snippet: `eval_prompt = f""" Evaluate if the current sub-stage is complete based on the following evidence: 1. Figure Analysis: {vlm_feedback} Requirements for completion: - {current_substage.goals} Provide a detailed evaluation of completion status. """`
- L568 `prompt` — snippet: `prompt = f""" Based on the current experimental progress, generate focused goals for the next sub-stage. Main Stage Goals: {main_stage_goal} Current Progress: - Total attempts: {metrics['total_nodes']} - Successful implementations: {metrics['good_nodes']} - Best performance: {metrics['best_metric']['value'] if metrics['best_metric'] else 'N/A'} ...`
- L838 `prompt_parts` — snippet: `prompt_parts = [ f"Task Description: {self._curate_task_desc(previous_stages[-1])}", f"Current Stage Number: {previous_stages[-1].stage_number}", ]`
- L1156 `eval_prompt` — snippet: `eval_prompt = f""" Evaluate whether the current experimental stage should progress to the next stage. Consider all available evidence holistically: Current Stage Information: - Name: {current_stage.name} - Description: {current_stage.description} - Goals: {', '.join(current_stage.goals) if isinstance(current_stage.goals, list) else current_stage...`
- L456 `eval_prompt` — snippet: `eval_prompt = f""" Evaluate if stage 2 (baseline tuning) is complete based on the following evidence: 1. Figure Analysis: {vlm_feedback} 2. Datasets Tested: {best_node.datasets_successfully_tested} Requirements for completion: 1. Training curves should show stable convergence 2. Results should be tested on at least two datasets 3. No major insta...`

### Classes

#### Class `Stage` (L104)
- Bases: `object`
#### Class `StageTransition` (L114)
- Bases: `object`
- Docstring: Records transition between stages and the reasoning
#### Class `AgentManager` (L123)
- Bases: `object`
##### `__init__(self, task_desc, cfg, workspace_dir)` (L124)
- Inputs: parameters from signature `__init__(self, task_desc, cfg, workspace_dir)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L126: {'line': 126, 'type': 'for', 'target': 'k', 'iter': "['Title', 'Abstract', 'Short Hypothesis', 'Experiments', 'Risk Factors and Limitations']", 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L133: IF `k not in self.task_desc.keys()`; body=1 else=0
- Raises:
  - L134: `ValueError(f'Key {k} not found in task_desc')`
- I/O / network / subprocess side effects:
  - L125: `json.loads`
- Main call graph hints: `json.loads`, `self._create_initial_stage`, `self.task_desc.keys`, `ValueError`
##### `_get_max_iterations(self, stage_number)` (L171)
- Docstring: Get max iterations for a stage from config or default
- Inputs: parameters from signature `_get_max_iterations(self, stage_number)` plus referenced module/global/config state.
- Outputs / returns:
  - L173: `getattr(self.cfg.agent.stages, f'stage{stage_number}_max_iters', self.cfg.agent.steps)`
- Main call graph hints: `getattr`
##### `_get_task_desc_str(self)` (L179)
- Inputs: parameters from signature `_get_task_desc_str(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L198: `task_desc`
- Conditions / decisions:
  - L196: IF `'Code' in self.task_desc`; body=1 else=0
##### `_create_initial_stage(self)` (L200)
- Docstring: Create the initial stage configuration
- Inputs: parameters from signature `_create_initial_stage(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `Stage`, `self.stages.append`, `Journal`, `self._get_max_iterations`
##### `_curate_task_desc(self, stage)` (L216)
- Inputs: parameters from signature `_curate_task_desc(self, stage)` plus referenced module/global/config state.
- Outputs / returns:
  - L247: `task_desc`
- Conditions / decisions:
  - L219: IF `stage.name.startswith('3_')`; body=2 else=1
  - L220: IF `isinstance(self.task_desc['Experiments'], list)`; body=1 else=1
  - L238: IF `stage.name.startswith('4_')`; body=2 else=0
  - L221: IF `isinstance(self.task_desc['Experiments'][0], str)`; body=1 else=1
  - L231: IF `isinstance(self.task_desc['Experiments'], str)`; body=1 else=1
  - L239: IF `isinstance(self.task_desc['Risk Factors and Limitations'], list)`; body=1 else=1
  - L223: IF `isinstance(self.task_desc['Experiments'][0], dict)`; body=1 else=0
- Raises:
  - L234: `ValueError(f"Experiments is not a list or string: {self.task_desc['Experiments']}")`
- Main call graph hints: `self._get_task_desc_str`, `stage.name.startswith`, `isinstance`, `Constant.join`, `ValueError`, `d.items`
##### `_save_checkpoint(self)` (L249)
- Docstring: Save the current state of the experiment
- Inputs: parameters from signature `_save_checkpoint(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L253: `None`
- Conditions / decisions:
  - L251: IF `self.current_stage is None`; body=2 else=0
- I/O / network / subprocess side effects:
  - L271: `open`
  - L272: `pickle.dump`
- Main call graph hints: `print`, `logger.warning`, `open`, `pickle.dump`, `Path`
##### `_create_agent_for_stage(self, stage)` (L274)
- Docstring: Create a ParallelAgent configured for the given stage
- Inputs: parameters from signature `_create_agent_for_stage(self, stage)` plus referenced module/global/config state.
- Outputs / returns:
  - L321: `ParallelAgent(task_desc=task_desc, cfg=stage_cfg, journal=self.journals[stage.name], stage_name=stage.name, best_stage3_node=best_stage3_node, best_stage2_node=best_stage2_node, best_stage1_node=best_stage1_node)`
- Conditions / decisions:
  - L292: IF `main_stage == 2`; body=5 else=1
  - L294: IF `not stage1_substages`; body=1 else=0
  - L299: IF `main_stage == 3`; body=5 else=1
  - L301: IF `not stage2_substages`; body=1 else=0
  - L306: IF `main_stage == 4`; body=2 else=3
  - L309: IF `stage3_substages`; body=4 else=1
- Raises:
  - L295: `ValueError(f'No stage 1 substages found in {self.stages}')`
  - L302: `ValueError(f'No stage 2 substages found in {self.stages}')`
  - L315: `ValueError(f'No stage 3 substages found in {self.stages}')`
- Main call graph hints: `self.cfg.copy`, `self._curate_task_desc`, `self.parse_stage_names`, `print`, `ParallelAgent`, `self._get_best_implementation`, `ValueError`, `s.name.startswith`
##### `_parse_vlm_feedback(self, node)` (L331)
- Docstring: Parse the feedback from the VLM
- Inputs: parameters from signature `_parse_vlm_feedback(self, node)` plus referenced module/global/config state.
- Outputs / returns:
  - L341: `feedback`
- Conditions / decisions:
  - L333: IF `len(node.plot_analyses) > 0`; body=1 else=2
- Main call graph hints: `len`, `logger.warning`
##### `_check_substage_completion(self, current_substage, journal)` (L343)
- Docstring: Check if the current sub-stage is complete
- Inputs: parameters from signature `_check_substage_completion(self, current_substage, journal)` plus referenced module/global/config state.
- Outputs / returns:
  - L408: `False`
  - L349: `(False, 'No best node found')`
  - L405: `(True, 'Reached max iterations')`
  - L378: `(True, 'Found working implementation')`
  - L387: `(False, 'Missing criteria: ' + missing)`
  - L392: `(False, f'Error in sub-stage {current_substage.name} completion evaluation')`
- Conditions / decisions:
  - L348: IF `not best_node`; body=1 else=0
  - L398: IF `len(journal.nodes) >= current_substage.max_iterations`; body=3 else=0
  - L371: IF `evaluation['is_complete']`; body=3 else=4
- Exception handling:
  - L363: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L364: `query`
- Main call graph hints: `journal.get_best_node`, `self._parse_vlm_feedback`, `print`, `query`, `len`, `logger.info`, `Constant.join`, `logger.error`
##### `_check_stage_completion(self, stage)` (L410)
- Docstring: Check if current stage is complete based on criteria
- Inputs: parameters from signature `_check_stage_completion(self, stage)` plus referenced module/global/config state.
- Outputs / returns:
  - L536: `(False, 'stage not completed')`
  - L429: `(True, 'Failed to find working implementation')`
  - L431: `(True, 'Reached max iterations')`
  - L442: `(True, 'Found working implementation')`
  - L447: `(False, 'No best node found')`
  - L449: `(False, 'No improvement found from the base node (which is the best node from the previous stage)')`
  - L503: `(False, 'No best node found')`
  - L505: `(False, 'No improvement found from the base node (which is the best node from the previous stage)')`
  - L488: `(True, 'Found working implementation')`
  - L495: `(False, 'Missing criteria: ' + missing)`
  - L498: `(False, 'Error in stage 2 completion evaluation')`
  - L530: `(False, exec_time_feedback)`
- Conditions / decisions:
  - L414: IF `len(journal.nodes) >= stage.max_iterations`; body=3 else=0
  - L434: IF `stage.stage_number == 1`; body=1 else=0
  - L444: IF `stage.stage_number == 2`; body=6 else=0
  - L500: IF `stage.stage_number == 3`; body=6 else=0
  - L531: IF `stage.stage_number == 4`; body=1 else=0
  - L419: IF `stage.stage_number == 1`; body=4 else=1
  - L435: IF `len(journal.good_nodes) > 0`; body=3 else=0
  - L446: IF `not best_node`; body=1 else=0
  - L448: IF `best_node == journal.nodes[0]`; body=1 else=0
  - L502: IF `not best_node`; body=1 else=0
  - L504: IF `best_node == journal.nodes[0]`; body=1 else=0
  - L514: IF `len(self.journals[stage.name].nodes) > self.cfg.agent.stages.stage3_max_iters / 2`; body=1 else=0
  - L481: IF `evaluation['is_complete']`; body=3 else=4
  - L517: IF `exec_time_minutes < self.cfg.exec.timeout / 60 / 2`; body=4 else=0
- Exception handling:
  - L472: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L473: `query`
- Main call graph hints: `print`, `len`, `logger.info`, `journal.get_best_node`, `self._parse_vlm_feedback`, `logger.error`, `query`, `Constant.join`
##### `_get_best_implementation(self, stage_name)` (L538)
- Docstring: Get the best implementation from a completed stage
- Inputs: parameters from signature `_get_best_implementation(self, stage_name)` plus referenced module/global/config state.
- Outputs / returns:
  - L550: `None`
  - L541: `None`
  - L549: `copied_node`
- Conditions / decisions:
  - L540: IF `stage_name not in self.journals`; body=1 else=0
  - L543: IF `best_node`; body=4 else=0
- Main call graph hints: `self.journals[...].get_best_node`, `copy.deepcopy`, `set`
##### `_generate_substage_goal(self, main_stage_goal, journal)` (L552)
- Docstring: Generate the next sub-stage goal based on what has been done so far.

Args:
    main_stage_goal: The overall goal for the current main stage
    journal: Journal containing the results and progress so far

Returns:
    str: Specific goals for the next sub-stage
- Inputs: parameters from signature `_generate_substage_goal(self, main_stage_goal, journal)` plus referenced module/global/config state.
- Outputs / returns:
  - L628: `(goal_str.strip(), response['sub_stage_name'])`
  - L633: `f'\n Sub-stage Goals:\n Continue progress on main stage objectives while addressing current issues.\n '`
- Exception handling:
  - L613: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L615: `query`
- I/O / network / subprocess side effects:
  - L581: `json.dumps`
  - L584: `json.dumps`
- Main call graph hints: `self._gather_stage_metrics`, `self._identify_issues`, `self._analyze_progress`, `FunctionSpec`, `query`, `json.dumps`, `goal_str.strip`, `logger.error`
##### `_create_next_substage(self, current_substage, journal, substage_feedback)` (L638)
- Docstring: Create the next sub-stage. Ask LLM to come up with the next sub-stage name and goals
based on what has been done so far.
- Inputs: parameters from signature `_create_next_substage(self, current_substage, journal, substage_feedback)` plus referenced module/global/config state.
- Outputs / returns:
  - L652: `Stage(name=f'{main_stage_num}_{main_stage_name}_{sub_stage_num + 1}_{sub_stage_name}', description=sub_stage_name, goals='Main stage goals:\n' + main_stage_goal + '\n\nSub-stage goals:\n' + sub_stage_goal, max_iterations=self._get_max_iterations(main_stage_num), num_drafts=0, stage_number=current...`
- Main call graph hints: `self.parse_stage_names`, `self._generate_substage_goal`, `Stage`, `self._get_max_iterations`
##### `_create_next_main_stage(self, current_substage, journal)` (L664)
- Inputs: parameters from signature `_create_next_main_stage(self, current_substage, journal)` plus referenced module/global/config state.
- Outputs / returns:
  - L683: `Stage(name=f'{main_stage_num + 1}_{next_main_stage_name}_{sub_stage_num}_{sub_stage_name}', description=description, goals=main_stage_goal, max_iterations=self._get_max_iterations(main_stage_num + 1), num_drafts=num_drafts, stage_number=stage_number)`
  - L674: `None`
- Conditions / decisions:
  - L673: IF `main_stage_num == 4`; body=1 else=0
- Main call graph hints: `self.parse_stage_names`, `Stage`, `self._get_max_iterations`
##### `run(self, exec_callback, step_callback)` (L692)
- Docstring: Run the experiment through generated stages
- Inputs: parameters from signature `run(self, exec_callback, step_callback)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L694: {'line': 694, 'type': 'while', 'test': 'self.current_stage', 'body_len': 7, 'orelse_len': 0}
  - L700: {'line': 700, 'type': 'while', 'test': 'current_substage', 'body_len': 2, 'orelse_len': 0}
  - L721: {'line': 721, 'type': 'while', 'test': 'True', 'body_len': 7, 'orelse_len': 0}
- Conditions / decisions:
  - L807: IF `self.current_stage`; body=2 else=0
  - L811: IF `next_main_stage`; body=4 else=3
  - L705: IF `self.stage_history`; body=5 else=0
  - L710: IF `prev_best`; body=1 else=4
  - L723: IF `step_callback`; body=1 else=0
  - L736: IF `main_stage_complete`; body=3 else=0
  - L779: IF `substage_complete`; body=3 else=0
  - L738: IF `current_substage.stage_number in [1, 2, 3, 4]`; body=2 else=0
  - L786: IF `next_substage`; body=4 else=1
  - L742: IF `best_node`; body=5 else=4
  - L746: IF `step_callback`; body=1 else=0
  - L752: IF `step_callback`; body=1 else=0
- Main call graph hints: `print`, `self._save_checkpoint`, `self.parse_stage_names`, `self._create_next_main_stage`, `self._create_agent_for_stage`, `self.stage_history.append`, `self.stages.append`, `Journal`, `logger.info`, `self._get_best_implementation`, `agent.step`, `self._check_stage_completion`, `self._check_substage_completion`, `StageTransition`, `self.journals[...].append`, `step_callback`, `self._create_next_substage`, `agent._run_multi_seed_evaluation`, `agent._run_plot_aggregation`, `logger.error`
##### `_create_stage_analysis_prompt(self, previous_stages, previous_results, is_initial_stage)` (L831)
- Docstring: Create detailed prompt to determine next stage configuration
- Inputs: parameters from signature `_create_stage_analysis_prompt(self, previous_stages, previous_results, is_initial_stage)` plus referenced module/global/config state.
- Outputs / returns:
  - L925: `'\n\n'.join(prompt_parts)`
- Loops:
  - L865: {'line': 865, 'type': 'for', 'target': 'analysis', 'iter': "plot_insights['analyses']", 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L843: IF `previous_stages`; body=2 else=0
  - L850: IF `previous_results`; body=10 else=0
  - L852: IF `'node_summaries' in previous_results['metrics']`; body=2 else=0
  - L862: IF `'plot_insights' in previous_results`; body=3 else=0
- I/O / network / subprocess side effects:
  - L907: `open`
  - L908: `json.dump`
- Main call graph hints: `prompt_parts.append`, `Constant.join`, `notes_dir.mkdir`, `Path`, `open`, `json.dump`, `self._curate_task_desc`, `previous_results[...].get`, `previous_results.get`, `enumerate`
##### `parse_stage_names(self, stage_name)` (L927)
- Docstring: Parse stage name into main stage number, main stage name,
sub-stage number, and sub-stage name
- Inputs: parameters from signature `parse_stage_names(self, stage_name)` plus referenced module/global/config state.
- Outputs / returns:
  - L941: `(main_stage, main_stage_name, sub_stage_num, sub_stage_name)`
- Main call graph hints: `Constant.join`, `re.split[...].strip`, `int`, `re.split`, `re.findall`, `p.strip`
##### `_save_stage_summary(self, current_results, evaluation)` (L943)
- Docstring: Save comprehensive stage completion summary
- Inputs: parameters from signature `_save_stage_summary(self, current_results, evaluation)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- I/O / network / subprocess side effects:
  - L975: `open`
  - L976: `json.dump`
- Main call graph hints: `notes_dir.mkdir`, `Path`, `open`, `json.dump`, `current_results.get`
##### `_get_response(self, prompt)` (L978)
- Docstring: Get structured response from LLM for stage configuration.

Args:
    prompt: The analysis prompt to send to the LLM

Returns:
    Dictionary containing stage configuration with keys:
    - name: str
    - description: str
    - goals: List[str]
    - max_iterations: int
    - success_metric_threshold: Optional[float]
- Inputs: parameters from signature `_get_response(self, prompt)` plus referenced module/global/config state.
- Outputs / returns:
  - L1028: `response`
  - L1033: `{'name': 'fallback_stage', 'description': 'Fallback stage due to LLM error', 'goals': ['Recover from error and continue execution'], 'max_iterations': 3, 'success_metric_threshold': None}`
- Exception handling:
  - L1020: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L1021: `query`
- Main call graph hints: `query`, `logger.error`
##### `_gather_stage_metrics(self, journal)` (L1041)
- Docstring: Gather detailed metrics and analysis from the stage's nodes
- Inputs: parameters from signature `_gather_stage_metrics(self, journal)` plus referenced module/global/config state.
- Outputs / returns:
  - L1082: `metrics`
- Loops:
  - L1053: {'line': 1053, 'type': 'for', 'target': 'node', 'iter': 'journal.nodes', 'body_len': 1, 'orelse_len': 0}
  - L1059: {'line': 1059, 'type': 'for', 'target': 'node', 'iter': 'journal.good_nodes', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L1064: IF `best_node`; body=1 else=0
  - L1054: IF `hasattr(node, '_agent')`; body=2 else=0
  - L1060: IF `hasattr(node, '_vlm_feedback')`; body=1 else=0
- Main call graph hints: `journal.get_best_node`, `len`, `hasattr`, `node._agent._generate_node_summary`, `metrics[...].append`
##### `_identify_issues(self, journal)` (L1084)
- Docstring: Identify systemic issues and challenges from the current stage's results
- Inputs: parameters from signature `_identify_issues(self, journal)` plus referenced module/global/config state.
- Outputs / returns:
  - L1125: `issues`
- Loops:
  - L1108: {'line': 1108, 'type': 'for', 'target': 'node', 'iter': 'journal.good_nodes', 'body_len': 1, 'orelse_len': 0}
  - L1096: {'line': 1096, 'type': 'for', 'target': 'node', 'iter': 'buggy_leaves', 'body_len': 1, 'orelse_len': 0}
  - L1102: {'line': 1102, 'type': 'for', 'target': '(error_msg, node_ids)', 'iter': 'error_patterns.items()', 'body_len': 1, 'orelse_len': 0}
  - L1117: {'line': 1117, 'type': 'for', 'target': 'analysis', 'iter': "vlm_feedback['plot_analyses']", 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L1093: IF `buggy_leaves`; body=3 else=0
  - L1109: IF `hasattr(node, '_vlm_feedback')`; body=2 else=0
  - L1097: IF `hasattr(node, 'analysis')`; body=1 else=0
  - L1103: IF `len(node_ids) >= 2`; body=1 else=0
  - L1111: IF `isinstance(vlm_feedback, dict)`; body=2 else=0
  - L1113: IF `'systemic_issues' in vlm_feedback`; body=1 else=0
  - L1116: IF `'plot_analyses' in vlm_feedback`; body=1 else=0
  - L1118: IF `'limitation' in analysis.get('type', '').lower()`; body=1 else=0
- Main call graph hints: `set`, `issues.extend`, `error_patterns.items`, `hasattr`, `list`, `isinstance`, `error_patterns.setdefault.append`, `len`, `issues.append`, `vlm_issues.update`, `error_patterns.setdefault`, `analysis.get.lower`, `vlm_issues.add`, `analysis.get`
##### `_analyze_progress(self, journal)` (L1127)
- Docstring: Analyze progress and convergence in the current stage
- Inputs: parameters from signature `_analyze_progress(self, journal)` plus referenced module/global/config state.
- Outputs / returns:
  - L1149: `progress`
- Loops:
  - L1139: {'line': 1139, 'type': 'for', 'target': 'node', 'iter': 'recent_nodes', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L1140: IF `not node.is_buggy`; body=2 else=0
- Main call graph hints: `len`, `progress[...].append`, `hasattr`
##### `_evaluate_stage_progression(self, current_stage, previous_results)` (L1151)
- Docstring: Evaluate whether experiment is ready for next stage
- Inputs: parameters from signature `_evaluate_stage_progression(self, current_stage, previous_results)` plus referenced module/global/config state.
- Outputs / returns:
  - L1209: `evaluation`
  - L1213: `{'ready_for_next_stage': False, 'reasoning': 'Error in evaluation process - continuing current stage', 'recommendations': ['Address evaluation error', 'Continue current approach'], 'suggested_focus': 'Maintain current direction while resolving evaluation issues'}`
- Exception handling:
  - L1195: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L1196: `query`
- I/O / network / subprocess side effects:
  - L1166: `json.dumps`
  - L1169: `json.dumps`
  - L1172: `json.dumps`
  - L1206: `json.dumps`
- Main call graph hints: `query`, `logger.info`, `json.dumps`, `logger.error`, `isinstance`, `Constant.join`, `previous_results.get`

### Functions

- None

---

## File: `ai_scientist/treesearch/backend/__init__.py`

**Lines:** 78  


### Imports / external dependencies

- `from . import backend_anthropic, backend_openai`
- `from .utils import FunctionSpec, OutputType, PromptType, compile_prompt_to_md`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `get_ai_client(model, **model_kwargs)` (L4)
- Docstring: Get the appropriate AI client based on the model string.

Args:
    model (str): string identifier for the model to use (e.g. "gpt-4-turbo")
    **model_kwargs: Additional keyword arguments for model configuration.
Returns:
    An instance of the appropriate AI client.
- Inputs: parameters from signature `get_ai_client(model, **model_kwargs)` plus referenced module/global/config state.
- Outputs / returns:
  - L15: `backend_anthropic.get_ai_client(model=model, **model_kwargs)`
  - L17: `backend_openai.get_ai_client(model=model, **model_kwargs)`
- Conditions / decisions:
  - L14: IF `'claude-' in model`; body=1 else=1
- I/O / network / subprocess side effects:
  - L17: `backend_openai.get_ai_client`
- Main call graph hints: `backend_anthropic.get_ai_client`, `backend_openai.get_ai_client`
#### `query(system_message, user_message, model, temperature, max_tokens, func_spec, **model_kwargs)` (L19)
- Docstring: General LLM query for various backends with a single system and user message.
Supports function calling for some backends.

Args:
    system_message (PromptType | None): Uncompiled system message (will generate a message following the OpenAI/Anthropic format)
    user_message (PromptType | None): Uncompiled user message (will generate a message following the OpenAI/Anthropic format)
    model (str): string identifier for the model to use (e.g. "gpt-4-turbo")
    temperature (float | None, optional): Temperature to sample at. Defaults to the model-specific default.
    max_tokens (int | None, optional): Maximum number of tokens to generate. Defaults to the model-specific max tokens.
    func_spec (FunctionSpec | None, optional): Optional FunctionSpec object defining a function call. If given, the return value will be a dict.

Returns:
    OutputType: A string completion if func_spec is None, otherwise a dict with the function call details.
- Inputs: parameters from signature `query(system_message, user_message, model, temperature, max_tokens, func_spec, **model_kwargs)` plus referenced module/global/config state.
- Outputs / returns:
  - L77: `output`
- Conditions / decisions:
  - L51: IF `model.startswith('o1')`; body=5 else=1
  - L52: IF `system_message and user_message is None`; body=1 else=1
  - L54: IF `system_message is None and user_message`; body=1 else=1
  - L56: IF `system_message and user_message`; body=3 else=0
- LLM/VLM calls:
  - L70: `query_func`
- Main call graph hints: `model.startswith`, `query_func`, `model_kwargs.pop`, `compile_prompt_to_md`

---

## File: `ai_scientist/treesearch/backend/backend_anthropic.py`

**Lines:** 78  


### Imports / external dependencies

- `import time`
- `import os`
- `from .utils import FunctionSpec, OutputType, opt_messages_to_list, backoff_create`
- `from funcy import notnone, once, select_values`
- `import anthropic`

### Module-level assignments / constants

- L9: `ANTHROPIC_TIMEOUT_EXCEPTIONS = ( anthropic.RateLimitError, anthropic.APIConnectionError, anthropic.APITimeoutError, anthropic.InternalServerError, anthropic.APIStatusError, )`

### Prompt-like assignments in this file

- L50 `message` — snippet: `message = backoff_create( client.messages.create, ANTHROPIC_TIMEOUT_EXCEPTIONS, messages=messages, **filtered_kwargs, )`

### Classes

- None

### Functions

#### `get_ai_client(model, max_retries)` (L17)
- Inputs: parameters from signature `get_ai_client(model, max_retries)` plus referenced module/global/config state.
- Outputs / returns:
  - L19: `client`
- Main call graph hints: `anthropic.AnthropicBedrock`
#### `query(system_message, user_message, func_spec, **model_kwargs)` (L21)
- Inputs: parameters from signature `query(system_message, user_message, func_spec, **model_kwargs)` plus referenced module/global/config state.
- Outputs / returns:
  - L77: `(output, req_time, in_tokens, out_tokens, info)`
- Conditions / decisions:
  - L30: IF `'max_tokens' not in filtered_kwargs`; body=1 else=0
  - L33: IF `func_spec is not None`; body=1 else=0
  - L40: IF `system_message is not None and user_message is None`; body=1 else=0
  - L44: IF `system_message is not None`; body=1 else=0
  - L59: IF `'thinking' in filtered_kwargs`; body=2 else=2
- Raises:
  - L34: `NotImplementedError('Anthropic does not support function calling for now.')`
- Main call graph hints: `get_ai_client`, `select_values`, `opt_messages_to_list`, `time.time`, `backoff_create`, `print`, `model_kwargs.get`, `NotImplementedError`, `len`

---

## File: `ai_scientist/treesearch/backend/backend_openai.py`

**Lines:** 89  


### Imports / external dependencies

- `import json`
- `import logging`
- `import time`
- `from .utils import FunctionSpec, OutputType, opt_messages_to_list, backoff_create`
- `from funcy import notnone, once, select_values`
- `import openai`
- `from rich import print`

### Module-level assignments / constants

- L10: `logger = logging.getLogger("ai-scientist")`
- L13: `OPENAI_TIMEOUT_EXCEPTIONS = ( openai.RateLimitError, openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError, )`

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `get_ai_client(model, max_retries)` (L20)
- Inputs: parameters from signature `get_ai_client(model, max_retries)` plus referenced module/global/config state.
- Outputs / returns:
  - L28: `client`
- Conditions / decisions:
  - L21: IF `model.startswith('ollama/')`; body=1 else=1
- I/O / network / subprocess side effects:
  - L22: `openai.OpenAI`
  - L27: `openai.OpenAI`
- Main call graph hints: `model.startswith`, `openai.OpenAI`
#### `query(system_message, user_message, func_spec, **model_kwargs)` (L31)
- Inputs: parameters from signature `query(system_message, user_message, func_spec, **model_kwargs)` plus referenced module/global/config state.
- Outputs / returns:
  - L88: `(output, req_time, in_tokens, out_tokens, info)`
- Conditions / decisions:
  - L42: IF `func_spec is not None`; body=2 else=0
  - L47: IF `filtered_kwargs.get('model', '').startswith('ollama/')`; body=1 else=0
  - L61: IF `func_spec is None`; body=1 else=3
- Exception handling:
  - L70: handlers=['json.JSONDecodeError'] else=0 final=0
- Raises:
  - L77: `e`
- I/O / network / subprocess side effects:
  - L72: `json.loads`
- Main call graph hints: `get_ai_client`, `select_values`, `opt_messages_to_list`, `filtered_kwargs.get.startswith`, `time.time`, `backoff_create`, `model_kwargs.get`, `filtered_kwargs[...].replace`, `filtered_kwargs.get`, `print`, `json.loads`, `logger.error`

---

## File: `ai_scientist/treesearch/backend/utils.py`

**Lines:** 132  


### Imports / external dependencies

- `from dataclasses import dataclass`
- `import jsonschema`
- `from dataclasses_json import DataClassJsonMixin`
- `import backoff`
- `import logging`
- `from typing import Callable`

### Module-level assignments / constants

- L6: `PromptType = str | dict | list`
- L7: `FunctionCallType = dict`
- L8: `OutputType = str | FunctionCallType`
- L15: `logger = logging.getLogger("ai-scientist")`

### Prompt-like assignments in this file

- None detected

### Classes

#### Class `FunctionSpec` (L106)
- Bases: `DataClassJsonMixin`
##### `__post_init__(self)` (L111)
- Inputs: parameters from signature `__post_init__(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `jsonschema.Draft7Validator.check_schema`
##### `as_openai_tool_dict(self)` (L116)
- Inputs: parameters from signature `as_openai_tool_dict(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L117: `{'type': 'function', 'function': {'name': self.name, 'description': self.description, 'parameters': self.json_schema}}`
##### `openai_tool_choice_dict(self)` (L127)
- Inputs: parameters from signature `openai_tool_choice_dict(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L128: `{'type': 'function', 'function': {'name': self.name}}`

### Functions

#### `backoff_create(create_fn, retry_exceptions, *args, **kwargs)` (L23)
- Inputs: parameters from signature `backoff_create(create_fn, retry_exceptions, *args, **kwargs)` plus referenced module/global/config state.
- Outputs / returns:
  - L27: `create_fn(*args, **kwargs)`
  - L30: `False`
- Exception handling:
  - L26: handlers=['retry_exceptions'] else=0 final=0
- Main call graph hints: `backoff.on_predicate`, `create_fn`, `logger.info`
#### `opt_messages_to_list(system_message, user_message)` (L33)
- Inputs: parameters from signature `opt_messages_to_list(system_message, user_message)` plus referenced module/global/config state.
- Outputs / returns:
  - L41: `messages`
- Conditions / decisions:
  - L37: IF `system_message`; body=1 else=0
  - L39: IF `user_message`; body=1 else=0
- Main call graph hints: `messages.append`
#### `compile_prompt_to_md(prompt, _header_depth)` (L44)
- Docstring: Convert a prompt into markdown format
- Inputs: parameters from signature `compile_prompt_to_md(prompt, _header_depth)` plus referenced module/global/config state.
- Outputs / returns:
  - L52: `''`
  - L55: `prompt.strip() + '\n'`
  - L60: `''`
  - L64: `prompt`
  - L68: `result`
  - L79: `prompt`
  - L89: `'\n'.join(out)`
- Loops:
  - L85: {'line': 85, 'type': 'for', 'target': '(k, v)', 'iter': 'prompt.items()', 'body_len': 3, 'orelse_len': 0}
  - L72: {'line': 72, 'type': 'for', 'target': '(i, item)', 'iter': 'enumerate(prompt)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L48: IF `isinstance(prompt, (list, dict))`; body=1 else=0
  - L51: IF `prompt is None`; body=1 else=0
  - L54: IF `isinstance(prompt, str)`; body=1 else=0
  - L57: IF `isinstance(prompt, list)`; body=3 else=0
  - L76: IF `isinstance(prompt, dict)`; body=2 else=0
  - L59: IF `not prompt`; body=1 else=0
  - L62: IF `all((isinstance(item, dict) and 'type' in item for item in prompt))`; body=1 else=0
  - L78: IF `'type' in prompt`; body=1 else=0
- Exception handling:
  - L46: handlers=['Exception'] else=0 final=0
  - L66: handlers=['Exception'] else=0 final=0
  - L82: handlers=['Exception'] else=0 final=0
- Raises:
  - L95: `ValueError(f'Unsupported prompt type: {type(prompt)}')`
  - L102: ``
  - L74: ``
  - L93: ``
- Main call graph hints: `logger.debug`, `isinstance`, `ValueError`, `all`, `logger.error`, `prompt.strip`, `Constant.join`, `prompt.items`, `type`, `enumerate`, `out.append`, `compile_prompt_to_md`, `str`, `s.strip`

---

## File: `ai_scientist/treesearch/bfts_utils.py`

**Lines:** 77  


### Imports / external dependencies

- `import os`
- `import os.path as osp`
- `import shutil`
- `import yaml`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `idea_to_markdown(data, output_path, load_code)` (L7)
- Docstring: Convert a dictionary into a markdown file.

Args:
    data: Dictionary containing the data to convert
    output_path: Path where the markdown file will be saved
    load_code: Path to a code file to include in the markdown
- Inputs: parameters from signature `idea_to_markdown(data, output_path, load_code)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L17: {'line': 17, 'type': 'for', 'target': '(key, value)', 'iter': 'data.items()', 'body_len': 3, 'orelse_len': 0}
  - L24: {'line': 24, 'type': 'for', 'target': 'item', 'iter': 'value', 'body_len': 1, 'orelse_len': 0}
  - L28: {'line': 28, 'type': 'for', 'target': '(sub_key, sub_value)', 'iter': 'value.items()', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L35: IF `load_code`; body=4 else=0
  - L23: IF `isinstance(value, (list, tuple))`; body=2 else=1
  - L27: IF `isinstance(value, dict)`; body=1 else=1
- I/O / network / subprocess side effects:
  - L16: `open`
  - L40: `open`
- Main call graph hints: `open`, `data.items`, `key.replace.title`, `f.write`, `isinstance`, `os.path.exists`, `code_file.read`, `key.replace`, `value.items`
#### `edit_bfts_config_file(config_path, idea_dir, idea_path)` (L45)
- Docstring: Edit the bfts_config.yaml file to point to the idea.md file

Args:
    config_path: Path to the bfts_config.yaml file
    idea_dir: Directory where the idea.md file is located
    idea_path: Path to the idea.md file

Returns:
    Path to the edited bfts_config.yaml file
- Inputs: parameters from signature `edit_bfts_config_file(config_path, idea_dir, idea_path)` plus referenced module/global/config state.
- Outputs / returns:
  - L76: `run_config_path`
- I/O / network / subprocess side effects:
  - L58: `shutil.copy`
  - L66: `os.makedirs`
  - L71: `os.makedirs`
  - L59: `open`
  - L74: `open`
- Main call graph hints: `osp.join`, `shutil.copy`, `os.makedirs`, `open`, `yaml.load`, `yaml.dump`

---

## File: `ai_scientist/treesearch/interpreter.py`

**Lines:** 314  

**Module docstring:** Python interpreter for executing code snippets and capturing their output.
Supports:
- captures stdout and stderr
- captures exceptions and stack traces
- limits execution time


### Imports / external dependencies

- `import logging`
- `import os`
- `import queue`
- `import signal`
- `import sys`
- `import time`
- `import traceback`
- `from dataclasses import dataclass`
- `from multiprocessing import Process, Queue`
- `from pathlib import Path`
- `import humanize`
- `from dataclasses_json import DataClassJsonMixin`

### Module-level assignments / constants

- L23: `logger = logging.getLogger("ai-scientist")`

### Prompt-like assignments in this file

- None detected

### Classes

#### Class `ExecutionResult` (L27)
- Bases: `DataClassJsonMixin`
- Docstring: Result of executing a code snippet in the interpreter.
Contains the output, execution time, and exception information.
#### Class `RedirectQueue` (L70)
- Bases: `object`
##### `__init__(self, queue)` (L71)
- Inputs: parameters from signature `__init__(self, queue)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `write(self, msg)` (L74)
- Inputs: parameters from signature `write(self, msg)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `self.queue.put`
##### `flush(self)` (L77)
- Inputs: parameters from signature `flush(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
#### Class `Interpreter` (L81)
- Bases: `object`
##### `__init__(self, working_dir, timeout, format_tb_ipython, agent_file_name, env_vars)` (L82)
- Docstring: Simulates a standalone Python REPL with an execution time limit.

Args:
    working_dir (Path | str): working directory of the agent
    timeout (int, optional): Timeout for each code execution step. Defaults to 3600.
    format_tb_ipython (bool, optional): Whether to use IPython or default python REPL formatting for exceptions. Defaults to False.
    agent_file_name (str, optional): The name for the agent's code file. Defaults to "runfile.py".
    env_vars (dict[str, str], optional): Environment variables to set in the child process. Defaults to {}.
- Inputs: parameters from signature `__init__(self, working_dir, timeout, format_tb_ipython, agent_file_name, env_vars)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `Path.resolve`, `self.working_dir.exists`, `Path`
##### `child_proc_setup(self, result_outq)` (L111)
- Inputs: parameters from signature `child_proc_setup(self, result_outq)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L117: {'line': 117, 'type': 'for', 'target': '(key, value)', 'iter': 'self.env_vars.items()', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `shutup.mute_warnings`, `self.env_vars.items`, `os.chdir`, `sys.path.append`, `RedirectQueue`, `str`
##### `_run_session(self, code_inq, result_outq, event_outq)` (L130)
- Inputs: parameters from signature `_run_session(self, code_inq, result_outq, event_outq)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L136: {'line': 136, 'type': 'while', 'test': 'True', 'body_len': 6, 'orelse_len': 0}
- Conditions / decisions:
  - L153: IF `e_cls_name == 'KeyboardInterrupt'`; body=1 else=0
- Exception handling:
  - L143: handlers=['BaseException'] else=1 final=0
- I/O / network / subprocess side effects:
  - L139: `open`
- Main call graph hints: `self.child_proc_setup`, `code_inq.get`, `os.chdir`, `event_outq.put`, `result_outq.put`, `str`, `open`, `f.write`, `exec`, `compile`, `exception_summary`
##### `create_process(self)` (L163)
- Inputs: parameters from signature `create_process(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `Process`, `self.process.start`, `Queue`
##### `_drain_queues(self)` (L176)
- Docstring: Quickly drain all in-flight messages to prevent blocking.
- Inputs: parameters from signature `_drain_queues(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L178: {'line': 178, 'type': 'while', 'test': 'not self.result_outq.empty()', 'body_len': 1, 'orelse_len': 0}
  - L184: {'line': 184, 'type': 'while', 'test': 'not self.event_outq.empty()', 'body_len': 1, 'orelse_len': 0}
  - L190: {'line': 190, 'type': 'while', 'test': 'not self.code_inq.empty()', 'body_len': 1, 'orelse_len': 0}
- Exception handling:
  - L179: handlers=['Exception'] else=0 final=0
  - L185: handlers=['Exception'] else=0 final=0
  - L191: handlers=['Exception'] else=0 final=0
- Main call graph hints: `self.result_outq.empty`, `self.event_outq.empty`, `self.code_inq.empty`, `self.result_outq.get_nowait`, `self.event_outq.get_nowait`, `self.code_inq.get_nowait`
##### `cleanup_session(self)` (L196)
- Inputs: parameters from signature `cleanup_session(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L198: `None`
- Conditions / decisions:
  - L197: IF `self.process is None`; body=1 else=0
  - L204: IF `self.process.exitcode is None`; body=4 else=0
- Main call graph hints: `self.process.terminate`, `self._drain_queues`, `self.process.join`, `self.process.close`, `logger.warning`, `self.process.kill`
##### `run(self, code, reset_session)` (L213)
- Docstring: Execute the provided Python command in a separate process and return its output.

Parameters:
    code (str): Python code to execute.
    reset_session (bool, optional): Whether to reset the interpreter session before executing the code. Defaults to True.

Returns:
    ExecutionResult: Object containing the output and metadata of the code execution.
- Inputs: parameters from signature `run(self, code, reset_session)` plus referenced module/global/config state.
- Outputs / returns:
  - L313: `ExecutionResult(output, exec_time, e_cls_name, exc_info, exc_stack)`
- Loops:
  - L257: {'line': 257, 'type': 'while', 'test': 'True', 'body_len': 1, 'orelse_len': 0}
  - L299: {'line': 299, 'type': 'while', 'test': "not self.result_outq.empty() or not output or output[-1] != '<|EOF|>'", 'body_len': 1, 'orelse_len': 0}
  - L247: {'line': 247, 'type': 'while', 'test': 'not self.result_outq.empty()', 'body_len': 1, 'orelse_len': 0}
  - L269: {'line': 269, 'type': 'while', 'test': 'not self.result_outq.empty()', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L228: IF `reset_session`; body=2 else=1
  - L305: IF `e_cls_name == 'TimeoutError'`; body=1 else=1
  - L229: IF `self.process is not None`; body=1 else=0
  - L266: IF `not child_in_overtime and (not self.process.is_alive())`; body=4 else=0
  - L276: IF `self.timeout is None`; body=1 else=0
  - L279: IF `running_time > self.timeout`; body=4 else=0
  - L287: IF `running_time > self.timeout + 60`; body=5 else=0
- Exception handling:
  - L242: handlers=['queue.Empty'] else=0 final=0
  - L258: handlers=['queue.Empty'] else=0 final=0
- Raises:
  - L249: `RuntimeError(msg)`
  - L273: `RuntimeError(msg)`
- Main call graph hints: `logger.debug`, `self.process.is_alive`, `self.code_inq.put`, `time.time`, `output.pop`, `ExecutionResult`, `self.create_process`, `self.event_outq.get`, `output.append`, `self.cleanup_session`, `logger.critical`, `RuntimeError`, `self.result_outq.empty`, `self.result_outq.get`, `logger.error`, `os.kill`, `humanize.naturaldelta`, `logger.warning`

### Functions

#### `exception_summary(e, working_dir, exec_file_name, format_tb_ipython)` (L40)
- Docstring: Generates a string that summarizes an exception and its stack trace (either in standard python repl or in IPython format).
- Inputs: parameters from signature `exception_summary(e, working_dir, exec_file_name, format_tb_ipython)` plus referenced module/global/config state.
- Outputs / returns:
  - L67: `(tb_str, e.__class__.__name__, exc_info, exc_stack)`
- Loops:
  - L60: {'line': 60, 'type': 'for', 'target': 'att', 'iter': "['name', 'msg', 'obj']", 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L42: IF `format_tb_ipython`; body=3 else=2
  - L58: IF `hasattr(e, 'args')`; body=1 else=0
  - L61: IF `hasattr(e, att)`; body=1 else=0
- Main call graph hints: `tb_str.replace`, `hasattr`, `traceback.extract_tb`, `IPython.core.ultratb.VerboseTB`, `str`, `traceback.format_exception`, `Constant.join`, `tb.text`, `getattr`, `sys.exc_info`

---

## File: `ai_scientist/treesearch/journal.py`

**Lines:** 613  


### Imports / external dependencies

- `from __future__ import annotations`
- `import time`
- `import uuid`
- `from dataclasses import dataclass, field`
- `from typing import Literal, Optional, Any`
- `import copy`
- `import os`
- `import json`
- `from dataclasses_json import DataClassJsonMixin`
- `from .interpreter import ExecutionResult`
- `from .utils.metric import MetricValue, WorstMetricValue`
- `from .utils.response import trim_long_string`
- `from .backend import FunctionSpec, query`
- `from rich import print`
- `import logging`
- `from pathlib import Path`

### Module-level assignments / constants

- L21: `logger = logging.getLogger(__name__)`
- L23: `node_selection_spec = FunctionSpec( name="select_best_implementation", description="Select the best implementation based on comprehensive analysis", json_schema={ "type": "object", "properties": { "selected_id": { "type": "string", "description": "ID of the selected best implementation", }, "reas...`

### Prompt-like assignments in this file

- L436 `prompt` — snippet: `prompt = { "Introduction": ( "You are an experienced AI researcher evaluating different implementations " "of an experiment to select the best one. You should consider all aspects " "including performance metrics, training dynamics, generated plots quality." ), "Task": ( "Select the best implementation from the candidates below, considering all ...`
- L509 `prompt` — snippet: `prompt = { "Introduction": ( "You are an AI researcher summarizing experimental progress. " "Please analyze both successful and failed experiments to provide insights " "for future improvements." ), "Successful Experiments": "", "Failed Experiments": "", }`
- L591 `summary_prompt` — snippet: `summary_prompt = { "Introduction": "Synthesize the experimental findings from this stage", "Node Summaries": node_summaries, "Best Node": ( { "id": self.get_best_node().id, "metric": str(self.get_best_node(cfg=cfg).metric), } if self.get_best_node(cfg=cfg) else None ), }`

### Classes

#### Class `Node` (L44)
- Bases: `DataClassJsonMixin`
- Docstring: A single node in the solution tree. Contains code, execution results, and evaluation information.
##### `__post_init__(self)` (L120)
- Inputs: parameters from signature `__post_init__(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Conditions / decisions:
  - L122: IF `isinstance(self.children, list)`; body=1 else=0
  - L125: IF `self.parent is not None and (not isinstance(self.parent, str))`; body=1 else=0
- Main call graph hints: `isinstance`, `set`, `self.parent.children.add`
##### `__deepcopy__(self, memo)` (L128)
- Inputs: parameters from signature `__deepcopy__(self, memo)` plus referenced module/global/config state.
- Outputs / returns:
  - L143: `result`
- Loops:
  - L135: {'line': 135, 'type': 'for', 'target': '(k, v)', 'iter': 'self.__dict__.items()', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L136: IF `k not in ('parent', 'children')`; body=1 else=0
- Main call graph hints: `cls.__new__`, `self.__dict__.items`, `set`, `id`, `setattr`, `copy.deepcopy`
##### `__getstate__(self)` (L145)
- Docstring: Return state for pickling
- Inputs: parameters from signature `__getstate__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L151: `state`
- Conditions / decisions:
  - L149: IF `hasattr(self, 'id')`; body=1 else=0
- Main call graph hints: `self.__dict__.copy`, `hasattr`
##### `__setstate__(self, state)` (L153)
- Docstring: Set state during unpickling
- Inputs: parameters from signature `__setstate__(self, state)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `self.__dict__.update`
##### `stage_name(self)` (L159)
- Docstring: Return the stage of the node:
- "stage" if the node is an initial solution draft
- "debug" if the node is the result of a debugging step
- "improve" if the node is the result of an improvement step
- Inputs: parameters from signature `stage_name(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L168: `'debug' if self.parent.is_buggy else 'improve'`
  - L167: `'draft'`
- Conditions / decisions:
  - L166: IF `self.parent is None`; body=1 else=0
##### `absorb_exec_result(self, exec_result)` (L170)
- Docstring: Absorb the result of executing the code from this node.
- Inputs: parameters from signature `absorb_exec_result(self, exec_result)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `absorb_plot_exec_result(self, plot_exec_result)` (L178)
- Docstring: Absorb the result of executing the plotting code from this node.
- Inputs: parameters from signature `absorb_plot_exec_result(self, plot_exec_result)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `term_out(self)` (L187)
- Docstring: Get the terminal output of the code execution (after truncating it).
- Inputs: parameters from signature `term_out(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L189: `trim_long_string(''.join(self._term_out))`
- Main call graph hints: `trim_long_string`, `Constant.join`
##### `is_leaf(self)` (L192)
- Docstring: Check if the node is a leaf node in the solution tree.
- Inputs: parameters from signature `is_leaf(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L194: `not self.children`
##### `__eq__(self, other)` (L196)
- Inputs: parameters from signature `__eq__(self, other)` plus referenced module/global/config state.
- Outputs / returns:
  - L197: `isinstance(other, Node) and self.id == other.id`
- Main call graph hints: `isinstance`
##### `__hash__(self)` (L199)
- Inputs: parameters from signature `__hash__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L200: `hash(self.id)`
- Main call graph hints: `hash`
##### `debug_depth(self)` (L203)
- Docstring: Length of the current debug path
- 0 if the node is not a debug node (parent is not buggy)
- 1 if the parent is buggy but the skip parent isn't
- n if there were n consecutive debugging steps
- Inputs: parameters from signature `debug_depth(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L212: `self.parent.debug_depth + 1`
  - L211: `0`
- Conditions / decisions:
  - L210: IF `self.stage_name != 'debug'`; body=1 else=0
##### `to_dict(self)` (L214)
- Docstring: Convert node to dictionary for serialization
- Inputs: parameters from signature `to_dict(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L216: `{'code': self.code, 'plan': self.plan, 'overall_plan': self.overall_plan if hasattr(self, 'overall_plan') else None, 'plot_code': self.plot_code, 'plot_plan': self.plot_plan, 'step': self.step, 'id': self.id, 'ctime': self.ctime, '_term_out': self._term_out, 'parse_metrics_plan': self.parse_metri...`
- Main call graph hints: `hasattr`, `str`, `Path.resolve.relative_to`, `os.getcwd`, `analysis.get`, `Path.resolve`, `Path`
##### `from_dict(cls, data, journal)` (L294)
- Docstring: Create a Node from a dictionary, optionally linking to journal for relationships
- Inputs: parameters from signature `from_dict(cls, data, journal)` plus referenced module/global/config state.
- Outputs / returns:
  - L328: `node`
- Conditions / decisions:
  - L302: IF `metric_data`; body=1 else=0
  - L322: IF `journal is not None and parent_id`; body=2 else=0
  - L303: IF `isinstance(metric_data, dict)`; body=1 else=1
  - L324: IF `parent`; body=2 else=0
- Main call graph hints: `data.pop`, `cls`, `isinstance`, `journal.get_node_by_id`, `MetricValue`, `parent.children.add`, `data.get`, `WorstMetricValue`
#### Class `InteractiveSession` (L332)
- Bases: `DataClassJsonMixin`
- Docstring: A collection of nodes for an interaction session
(when the agent interacts with a Jupyter notebook-like interface).
##### `append(self, node)` (L341)
- Inputs: parameters from signature `append(self, node)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `len`, `self.nodes.append`
##### `generate_nb_trace(self, include_prompt, comment_headers)` (L345)
- Docstring: Generate a trace of the interactive session in IPython format.
- Inputs: parameters from signature `generate_nb_trace(self, include_prompt, comment_headers)` plus referenced module/global/config state.
- Outputs / returns:
  - L358: `'\n'.join(trace).strip()`
- Loops:
  - L349: {'line': 349, 'type': 'for', 'target': 'n', 'iter': 'self.nodes', 'body_len': 4, 'orelse_len': 0}
- Conditions / decisions:
  - L355: IF `include_prompt and self.nodes`; body=1 else=0
- Main call graph hints: `Constant.join.strip`, `trace.append`, `Constant.join`
#### Class `Journal` (L362)
- Bases: `object`
- Docstring: A collection of nodes representing the solution tree.
##### `__getitem__(self, idx)` (L367)
- Inputs: parameters from signature `__getitem__(self, idx)` plus referenced module/global/config state.
- Outputs / returns:
  - L368: `self.nodes[idx]`
##### `__len__(self)` (L370)
- Docstring: Return the number of nodes in the journal.
- Inputs: parameters from signature `__len__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L372: `len(self.nodes)`
- Main call graph hints: `len`
##### `append(self, node)` (L374)
- Docstring: Append a new node to the journal.
- Inputs: parameters from signature `append(self, node)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `len`, `self.nodes.append`
##### `draft_nodes(self)` (L380)
- Docstring: Return a list of nodes representing intial coding drafts
- Inputs: parameters from signature `draft_nodes(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L382: `[n for n in self.nodes if n.parent is None]`
##### `buggy_nodes(self)` (L385)
- Docstring: Return a list of nodes that are considered buggy by the agent.
- Inputs: parameters from signature `buggy_nodes(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L387: `[n for n in self.nodes if n.is_buggy]`
##### `good_nodes(self)` (L390)
- Docstring: Return a list of nodes that are not considered buggy by the agent.
- Inputs: parameters from signature `good_nodes(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L405: `[n for n in self.nodes if n.is_buggy is False and n.is_buggy_plots is False]`
- Main call graph hints: `print`
##### `get_node_by_id(self, node_id)` (L409)
- Docstring: Get a node by its ID.
- Inputs: parameters from signature `get_node_by_id(self, node_id)` plus referenced module/global/config state.
- Outputs / returns:
  - L414: `None`
  - L413: `node`
- Loops:
  - L411: {'line': 411, 'type': 'for', 'target': 'node', 'iter': 'self.nodes', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L412: IF `node.id == node_id`; body=1 else=0
##### `get_metric_history(self)` (L416)
- Docstring: Return a list of all metric values in the journal.
- Inputs: parameters from signature `get_metric_history(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L418: `[n.metric for n in self.nodes]`
##### `get_best_node(self, only_good, use_val_metric_only, cfg)` (L420)
- Docstring: Return the best solution found so far.
- Inputs: parameters from signature `get_best_node(self, only_good, use_val_metric_only, cfg)` plus referenced module/global/config state.
- Outputs / returns:
  - L430: `max(nodes, key=lambda n: n.metric)`
  - L433: `nodes[0]`
  - L425: `None`
  - L494: `selected_node`
  - L497: `max(nodes, key=lambda n: n.metric)`
  - L502: `max(nodes, key=lambda n: n.metric)`
- Loops:
  - L452: {'line': 452, 'type': 'for', 'target': 'node', 'iter': 'nodes', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L422: IF `only_good`; body=2 else=1
  - L429: IF `use_val_metric_only`; body=1 else=0
  - L432: IF `len(nodes) == 1`; body=1 else=0
  - L424: IF `not nodes`; body=1 else=0
  - L453: IF `not node.is_seed_node`; body=2 else=0
  - L470: IF `cfg is None or cfg.agent.get('select_node', None) is None`; body=2 else=2
  - L489: IF `selected_node`; body=3 else=2
- Exception handling:
  - L469: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L476: `query`
- Main call graph hints: `max`, `len`, `query`, `next`, `logger.warning`, `logger.error`, `cfg.agent.get`, `hasattr`, `str`
##### `generate_summary(self, include_code, **model_kwargs)` (L504)
- Docstring: Generate a summary of the research progress using LLM, including both successes and failures.
- Inputs: parameters from signature `generate_summary(self, include_code, **model_kwargs)` plus referenced module/global/config state.
- Outputs / returns:
  - L548: `summary`
  - L507: `'No experiments conducted yet.'`
- Loops:
  - L519: {'line': 519, 'type': 'for', 'target': 'node', 'iter': 'self.good_nodes', 'body_len': 5, 'orelse_len': 0}
  - L527: {'line': 527, 'type': 'for', 'target': 'node', 'iter': 'self.buggy_nodes', 'body_len': 6, 'orelse_len': 0}
- Conditions / decisions:
  - L506: IF `not self.nodes`; body=1 else=0
  - L523: IF `include_code`; body=1 else=0
  - L532: IF `include_code`; body=1 else=0
- LLM/VLM calls:
  - L536: `query`
- Main call graph hints: `query`, `model_kwargs.get`, `str`, `hasattr`
##### `generate_summary_old(self, include_code)` (L550)
- Inputs: parameters from signature `generate_summary_old(self, include_code)` plus referenced module/global/config state.
- Outputs / returns:
  - L559: `'\n-------------------------------\n'.join(summary)`
- Loops:
  - L552: {'line': 552, 'type': 'for', 'target': 'n', 'iter': 'self.good_nodes', 'body_len': 5, 'orelse_len': 0}
- Conditions / decisions:
  - L554: IF `include_code`; body=1 else=0
- Main call graph hints: `Constant.join`, `summary.append`
##### `to_dict(self)` (L561)
- Docstring: Convert journal to a JSON-serializable dictionary
- Inputs: parameters from signature `to_dict(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L563: `{'nodes': [node.to_dict() for node in self.nodes]}`
- Main call graph hints: `node.to_dict`
##### `save_experiment_notes(self, workspace_dir, stage_name, cfg)` (L565)
- Docstring: Save experimental notes and summaries to files
- Inputs: parameters from signature `save_experiment_notes(self, workspace_dir, stage_name, cfg)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L572: {'line': 572, 'type': 'for', 'target': 'node', 'iter': 'self.nodes', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L573: IF `hasattr(node, '_agent')`; body=3 else=0
- LLM/VLM calls:
  - L604: `query`
- I/O / network / subprocess side effects:
  - L568: `os.makedirs`
  - L611: `open`
  - L583: `open`
  - L589: `json.dump`
- Main call graph hints: `os.path.join`, `os.makedirs`, `query`, `hasattr`, `open`, `f.write`, `node._agent._generate_node_summary`, `node_summaries.append`, `self.get_best_node`, `json.dump`, `str`, `cfg.agent.get`

### Functions

- None

---

## File: `ai_scientist/treesearch/journal2report.py`

**Lines:** 32  


### Imports / external dependencies

- `from .backend import query`
- `from .journal import Journal`
- `from .utils.config import StageConfig`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- L11 `system_prompt_dict` — snippet: `system_prompt_dict = { "Role": "You are a research assistant that always uses concise language.", "Goal": "The goal is to write a technical report summarising the empirical findings and technical decisions.", "Input": "You are given a raw research journal with list of design attempts and their outcomes, and a research idea description.", "Output...`
- L21 `context_prompt` — snippet: `context_prompt = ( f"Here is the research journal of the agent: <journal>{report_input}<\\journal>, " f"and the research idea description is: <research_proposal>{task_desc}<\\research_proposal>." )`

### Classes

- None

### Functions

#### `journal2report(journal, task_desc, rcfg)` (L6)
- Docstring: Generate a report from a journal, the report will be in markdown format.
- Inputs: parameters from signature `journal2report(journal, task_desc, rcfg)` plus referenced module/global/config state.
- Outputs / returns:
  - L25: `query(system_message=system_prompt_dict, user_message=context_prompt, model=rcfg.model, temperature=rcfg.temp, max_tokens=4096)`
- LLM/VLM calls:
  - L25: `query`
- Main call graph hints: `journal.generate_summary`, `query`

---

## File: `ai_scientist/treesearch/log_summarization.py`

**Lines:** 453  


### Imports / external dependencies

- `import json`
- `import os`
- `import sys`
- `from .journal import Node, Journal`
- `from ai_scientist.llm import get_response_from_llm, extract_json_between_markers`
- `from ai_scientist.treesearch.backend import get_ai_client`

### Module-level assignments / constants

- L7: `parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))`
- L13: `report_summarizer_sys_msg = """You are an expert machine learning researcher. You are given multiple experiment logs, each representing a node in a stage of exploring scientific ideas and implementations. Your task is to aggregate these logs and provide scientifically insightful information. Impo...`
- L23: `output_format_control = """Respond in the following format: THOUGHT: <THOUGHT> JSON: ```json <JSON> ``` In <THOUGHT>, thoroughly reason as an expert researcher. First, reason about each node, and then reason carefully by combining all the information. It is okay to be very detailed. In <JSON>, pr...`
- L50: `report_summarizer_prompt = ( """You are given multiple experiment logs from different "nodes". Each node represents attempts and experiments exploring various scientific ideas. One key point is that these nodes collectively illustrate a stage of testing different methods or approaches. The crucia...`
- L66: `stage_aggregate_prompt = """You are given: 1) The summary of all previous experiment stages: {prev_summary} 2) The name of the current experiment stage: {stage_name} 3) The summary of the current stage: {current_summary} Your task is to produce an **updated comprehensive summary** of all experime...`
- L232: `overall_plan_summarizer_prompt = """You have been provided with the plans for both the parent node and the current node. Your task is to synthesize a comprehensive summary of the overall plan by integrating details from both the parent and current node plans. The summary should be thorough and cl...`

### Prompt-like assignments in this file

- L23 `output_format_control` — snippet: `output_format_control = """Respond in the following format: THOUGHT: <THOUGHT> JSON: ```json <JSON> ``` In <THOUGHT>, thoroughly reason as an expert researcher. First, reason about each node, and then reason carefully by combining all the information. It is okay to be very detailed. In <JSON>, provide the review in JSON format with the following...`
- L50 `report_summarizer_prompt` — snippet: `report_summarizer_prompt = ( """You are given multiple experiment logs from different "nodes". Each node represents attempts and experiments exploring various scientific ideas. One key point is that these nodes collectively illustrate a stage of testing different methods or approaches. The crucial task is to identify the scientific insights glea...`
- L66 `stage_aggregate_prompt` — snippet: `stage_aggregate_prompt = """You are given: 1) The summary of all previous experiment stages: {prev_summary} 2) The name of the current experiment stage: {stage_name} 3) The summary of the current stage: {current_summary} Your task is to produce an **updated comprehensive summary** of all experiment stages, including the newly introduced results ...`
- L232 `overall_plan_summarizer_prompt` — snippet: `overall_plan_summarizer_prompt = """You have been provided with the plans for both the parent node and the current node. Your task is to synthesize a comprehensive summary of the overall plan by integrating details from both the parent and current node plans. The summary should be thorough and clearly articulate the underlying motivations. For e...`
- L203 `prompt` — snippet: `prompt = stage_aggregate_prompt.format( prev_summary=prev_summary, stage_name=cur_stage_name, current_summary=cur_summary, )`

### Top-level decisions / loops / try blocks

- IF L364: `__name__ == '__main__'`; body=21 else=0

### Classes

- None

### Functions

#### `get_nodes_infos(nodes)` (L109)
- Inputs: parameters from signature `get_nodes_infos(nodes)` plus referenced module/global/config state.
- Outputs / returns:
  - L135: `node_infos`
- Loops:
  - L111: {'line': 111, 'type': 'for', 'target': 'n', 'iter': 'nodes', 'body_len': 7, 'orelse_len': 0}
  - L130: {'line': 130, 'type': 'for', 'target': 'plot', 'iter': 'n.plot_analyses', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L129: IF `hasattr(n, 'plot_analyses') and n.plot_analyses`; body=1 else=1
- Main call graph hints: `hasattr`, `plot.get`
#### `get_summarizer_prompt(journal, stage_name)` (L138)
- Inputs: parameters from signature `get_summarizer_prompt(journal, stage_name)` plus referenced module/global/config state.
- Outputs / returns:
  - L144: `(report_summarizer_sys_msg, report_summarizer_prompt.format(node_infos=node_infos, stage_name=stage_name))`
- Conditions / decisions:
  - L140: IF `not good_leaf_nodes`; body=2 else=0
- Main call graph hints: `get_nodes_infos`, `print`, `report_summarizer_prompt.format`
#### `get_stage_summary(journal, stage_name, model, client)` (L149)
- Inputs: parameters from signature `get_stage_summary(journal, stage_name, model, client)` plus referenced module/global/config state.
- Outputs / returns:
  - L153: `summary_json`
- LLM/VLM calls:
  - L151: `get_response_from_llm`
- Main call graph hints: `get_summarizer_prompt`, `get_response_from_llm`, `extract_json_between_markers`
#### `get_node_log(node)` (L156)
- Inputs: parameters from signature `get_node_log(node)` plus referenced module/global/config state.
- Outputs / returns:
  - L195: `ret`
- Conditions / decisions:
  - L177: IF `'exp_results_dir' in ret`; body=6 else=0
  - L182: IF `idx != -1`; body=1 else=0
  - L187: IF `os.path.isdir(original_dir_path)`; body=2 else=1
- Main call graph hints: `node.to_dict`, `original_dir_path.find`, `os.path.isdir`, `os.path.join`, `os.listdir`, `f.endswith`
#### `update_summary(prev_summary, cur_stage_name, cur_journal, cur_summary, model, client, max_retry)` (L198)
- Inputs: parameters from signature `update_summary(prev_summary, cur_stage_name, cur_journal, cur_summary, model, client, max_retry)` plus referenced module/global/config state.
- Outputs / returns:
  - L229: `summary_json`
  - L217: `update_summary(prev_summary, cur_stage_name, cur_journal, cur_summary, model, client, max_retry - 1)`
- Conditions / decisions:
  - L215: IF `max_retry > 0`; body=2 else=2
- Exception handling:
  - L208: handlers=['Exception'] else=0 final=0
- Raises:
  - L228: ``
- LLM/VLM calls:
  - L209: `get_response_from_llm`
- Main call graph hints: `get_nodes_infos`, `stage_aggregate_prompt.format`, `get_response_from_llm`, `extract_json_between_markers`, `print`, `update_summary`
#### `annotate_history(journal, cfg)` (L262)
- Inputs: parameters from signature `annotate_history(journal, cfg)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L263: {'line': 263, 'type': 'for', 'target': 'node', 'iter': 'journal.nodes', 'body_len': 1, 'orelse_len': 0}
  - L267: {'line': 267, 'type': 'while', 'test': 'retry_count < max_retries', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L264: IF `node.parent`; body=3 else=1
  - L269: IF `cfg.agent.get('summary', None) is not None`; body=1 else=1
  - L289: IF `retry_count == max_retries`; body=2 else=0
- Exception handling:
  - L268: handlers=['Exception'] else=0 final=0
- Raises:
  - L291: ``
- LLM/VLM calls:
  - L274: `get_response_from_llm`
- Main call graph hints: `get_ai_client`, `get_response_from_llm`, `cfg.agent.get`, `overall_plan_summarizer_prompt.format`, `extract_json_between_markers`, `print`
#### `overall_summarize(journals, cfg)` (L299)
- Inputs: parameters from signature `overall_summarize(journals, cfg)` plus referenced module/global/config state.
- Outputs / returns:
  - L361: `(draft_summary, baseline_summary, research_summary, ablation_summary)`
  - L319: `{'best node': get_node_log(best_node), 'best node with different seeds': [get_node_log(n) for n in multi_seed_nodes]}`
  - L326: `{'best node': get_node_log(best_node), 'best node with different seeds': [get_node_log(n) for n in multi_seed_nodes], 'aggregated results of nodes with different seeds': get_node_log(agg_node)}`
  - L339: `[get_node_log(n) for n in good_leaf_nodes]`
  - L347: `summary_json`
- Loops:
  - L313: {'line': 313, 'type': 'for', 'target': 'n', 'iter': 'child_nodes', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L305: IF `idx in [1, 2]`; body=6 else=1
  - L317: IF `agg_node is None`; body=1 else=1
  - L335: IF `idx == 3`; body=2 else=1
  - L314: IF `n.is_seed_node and n.is_seed_agg_node`; body=2 else=0
  - L340: IF `idx == 0`; body=4 else=0
  - L341: IF `cfg.agent.get('summary', None) is not None`; body=1 else=1
- Main call graph hints: `annotate_history`, `ThreadPoolExecutor`, `list`, `journal.get_best_node`, `tqdm`, `executor.map`, `get_node_log`, `get_ai_client`, `get_stage_summary`, `range`, `len`, `cfg.agent.get`, `cfg.agent.summary.get`

---

## File: `ai_scientist/treesearch/parallel_agent.py`

**Lines:** 2369  


### Imports / external dependencies

- `from concurrent.futures import ProcessPoolExecutor`
- `from typing import List, Optional, Set, Any, Callable, cast, Dict, Tuple`
- `import random`
- `import subprocess`
- `import os`
- `from queue import Queue`
- `import logging`
- `import humanize`
- `from .backend import FunctionSpec, compile_prompt_to_md, query`
- `from .interpreter import ExecutionResult`
- `from .journal import Journal, Node`
- `from .utils import data_preview`
- `from .utils.config import Config`
- `from .utils.metric import MetricValue, WorstMetricValue`
- `from .utils.response import extract_code, extract_text_up_to_code, wrap_code`
- `import copy`
- `import pickle`
- `from dataclasses import asdict`
- `from omegaconf import OmegaConf`
- `from rich import print`
- `from pathlib import Path`
- `import base64`
- `import sys`

### Module-level assignments / constants

- L26: `logger = logging.getLogger("ai-scientist")`
- L28: `ExecCallbackType = Callable[[str, bool], ExecutionResult]`
- L81: `review_func_spec = FunctionSpec( name="submit_review", json_schema={ "type": "object", "properties": { "is_bug": { "type": "boolean", "description": "true if the output log shows that the execution failed or has some bug, otherwise false.", }, "summary": { "type": "string", "description": "if the...`
- L103: `vlm_feedback_spec = FunctionSpec( name="analyze_experiment_plots", json_schema={ "type": "object", "properties": { "plot_analyses": { "type": "array", "items": { "type": "object", "properties": { "analysis": { "type": "string", "description": "Detailed analysis of the plot's results and implicati...`
- L135: `metric_parse_spec = FunctionSpec( name="parse_metrics", json_schema={ "type": "object", "strict": True, "properties": { "valid_metrics_received": { "type": "boolean", "description": "True if the metrics were successfully received, False otherwise. For example if the execution output does not cont...`
- L205: `plot_selection_spec = FunctionSpec( name="select_plots", json_schema={ "type": "object", "properties": { "selected_plots": { "type": "array", "description": "List of selected plot file paths", "items": {"type": "string", "description": "Full path to a plot file"}, "maxItems": 10, } }, "required":...`

### Prompt-like assignments in this file

- L292 `env_prompt` — snippet: `env_prompt = { "Installed Packages": f"Your solution can use any relevant machine learning packages such as: {pkg_str}. Feel free to use any other packages too (all packages are already installed!). For neural networks we suggest using PyTorch rather than TensorFlow." }`
- L454 `prompt` — snippet: `prompt: Any = { "Introduction": ( "You are an AI researcher who is looking to publish a paper that will contribute significantly to the field." "Your first task is to write a python code to implement a solid baseline based on your research idea provided below, " "from data preparation to model training, as well as evaluation and visualization. "...`
- L495 `prompt` — snippet: `prompt: Any = { "Introduction": ( "You are an experienced AI researcher. Your previous code for research experiment had a bug, so based on the information below, you should revise it in order to fix this bug. " "Your response should be an implementation outline in natural language," " followed by a single markdown code block which implements the...`
- L524 `prompt` — snippet: `prompt: Any = { "Introduction": ( "You are an experienced AI researcher. You are provided with a previously developed " "implementation. Your task is to improve it based on the current experimental stage." ), "Research idea": self.task_desc, "Memory": self.memory_summary if self.memory_summary else "", "Feedback based on generated plots": parent...`
- L560 `prompt` — snippet: `prompt: Any = { "Introduction": ( "You are an experienced AI researcher. You are provided with a previously developed " "baseline implementation. Your task is to implement hyperparameter tuning for the following idea: " + hyperparam_idea.name + ". " + hyperparam_idea.description ), "Base code you are working on": wrap_code(parent_node.code), "In...`
- L606 `prompt` — snippet: `prompt: Any = { "Introduction": ( "You are an experienced AI researcher. You are provided with a previously developed " "baseline implementation. Your task is to implement the ablation study for the following idea: " + ablation_idea.name + ". " + ablation_idea.description ), "Base code you are working on": wrap_code(parent_node.code), "Instructi...`
- L690 `prompt` — snippet: `prompt = { "Introduction": ( "You are an experienced AI researcher. " "You have written code for your research experiment and now need to evaluate the output of the code execution. " "Analyze the execution output, determine if there were any bugs, and provide a summary of the findings. " ), "Research idea": self.task_desc, "Implementation": wrap...`
- L724 `prompt_guideline` — snippet: `prompt_guideline = [ "AVAILABLE DATA: ", "Experiment Data: experiment_data.npy", ]`
- L841 `determine_prompt` — snippet: `determine_prompt = { "Introduction": "You are an AI researcher analyzing experiment results. Based on the plot analyses and feedback, determine which datasets are successfully tested. Return reasoning and the dataset names that are successfully executed, or an empty string if no datasets are successfully executed.", "Plot analyses": plot_analyse...`
- L983 `user_message` — snippet: `user_message = [ { "type": "text", "text": ( "You are an experienced AI researcher analyzing experimental results. " "You have been provided with plots from a machine learning experiment. " f"This experiment is based on the following research idea: {self.task_desc}" "Please analyze these plots and provide detailed insights about the results. " "...`
- L1037 `summary_prompt` — snippet: `summary_prompt = { "Introduction": ( "You are an AI researcher analyzing experimental results. " "Please summarize the findings from this experiment iteration." ), "Research idea": self.task_desc, "Implementation": wrap_code(node.code), "Plan": node.plan, "Execution output": wrap_code(node.term_out, lang=""), "Analysis": node.analysis, "Metric":...`
- L1196 `prompt` — snippet: `prompt = { "Introduction": ( "You are an AI researcher setting up experiments. " "Please propose meaningful evaluation metrics that will help analyze " "the performance and characteristics of solutions for this research task." ), "Research idea": self.task_desc, "Instructions": [ "Propose a single evaluation metric that would be useful for analy...`
- L1804 `hyperparam_tuning_prompt` — snippet: `hyperparam_tuning_prompt = { "Introduction": ( "You are an AI researcher conducting hyperparameter tuning for baseline experiments. " "Based on the current implementation and previous hyperparameter tuning attempts (if any), " "propose ONE new hyperparameter tuning idea to see if it improves the performance." "You should first check if simply tr...`
- L1866 `ablation_prompt` — snippet: `ablation_prompt = { "Introduction": ( "You are an AI researcher conducting ablation studies. " "Based on the current implementation and previous ablations (if any), " "propose ONE new ablation study that tests a different aspect of the model." ), "Base code you are working on": wrap_code(self.best_stage3_node.code), "Previous Ablations": { "Has ...`
- L2295 `plotting_prompt` — snippet: `plotting_prompt = { "Introduction": ( "You are an expert in data visualization and plotting. " "You are given a set of evaluation results and the code that was used to plot them. " "Your task is to write a new plotting code that aggregate the results " "e.g. for example, by adding mean values and standard error bars to the plots." ), "Instructio...`
- L677 `prompt["Parsing Feedback"]` — snippet: `prompt["Parsing Feedback"] = ( "The code extraction failed. Make sure to use the format ```python ... ``` for the code blocks." )`
- L917 `prompt_select_plots` — snippet: `prompt_select_plots = { "Introduction": ( "You are an experienced AI researcher analyzing experimental results. " "You have been provided with plots from a machine learning experiment. " "Please select 10 most relevant plots to analyze. " "For similar plots (e.g. generated samples at each epoch), select only at most 5 plots at a suitable interva...`
- L1242 `prompt["Parsing Feedback"]` — snippet: `prompt["Parsing Feedback"] = ( "The code extraction failed. Make sure to use the format ```python ... ``` for the code blocks." )`
- L1555 `parse_metrics_prompt` — snippet: `parse_metrics_prompt = { "Introduction": ( "You are an AI researcher analyzing experimental results stored in numpy files. " "Write code to load and analyze the metrics from experiment_data.npy." ), "Context": [ "Original Code: " + child_node.code, ], "Instructions": [ "0. Make sure to get the working directory from os.path.join(os.getcwd(), 'wo...`
- L1608 `metrics_prompt` — snippet: `metrics_prompt = { "Introduction": "Parse the metrics from the execution output. You only need the final or best value of a metric for each dataset, not the entire list during training.", "Execution Output": metrics_exec_result.term_out, }`

### Classes

#### Class `AblationConfig` (L223)
- Bases: `object`
- Docstring: Track state of ablation experiments
##### `__init__(self, name, description, code, base_node)` (L226)
- Inputs: parameters from signature `__init__(self, name, description, code, base_node)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
#### Class `AblationIdea` (L238)
- Bases: `object`
- Docstring: Ablation idea
##### `__init__(self, name, description)` (L241)
- Inputs: parameters from signature `__init__(self, name, description)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
#### Class `HyperparamTuningIdea` (L246)
- Bases: `object`
- Docstring: Hyperparameter tuning idea
##### `__init__(self, name, description)` (L249)
- Inputs: parameters from signature `__init__(self, name, description)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
#### Class `MinimalAgent` (L254)
- Bases: `object`
- Docstring: A minimal agent class that only contains what's needed for processing nodes
##### `__init__(self, task_desc, cfg, memory_summary, evaluation_metrics, stage, stage_name)` (L257)
- Inputs: parameters from signature `__init__(self, task_desc, cfg, memory_summary, evaluation_metrics, stage, stage_name)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `_prompt_environment(self)` (L274)
- Inputs: parameters from signature `_prompt_environment(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L295: `env_prompt`
- Main call graph hints: `random.shuffle`, `Constant.join`
##### `_prompt_impl_guideline(self)` (L298)
- Inputs: parameters from signature `_prompt_impl_guideline(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L394: `{'Implementation guideline': impl_guideline}`
- Conditions / decisions:
  - L315: IF `hasattr(self.cfg.experiment, 'num_syn_datasets')`; body=2 else=0
  - L389: IF `self.cfg.agent.k_fold_validation > 1`; body=1 else=0
  - L317: IF `num_syn_datasets > 1`; body=1 else=0
- Main call graph hints: `hasattr`, `impl_guideline.extend`, `impl_guideline.append`, `str`, `humanize.naturaldelta`
##### `_prompt_resp_fmt(self)` (L397)
- Inputs: parameters from signature `_prompt_resp_fmt(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L398: `{'Response format': 'Your response should be a brief outline/sketch of your proposed solution in natural language (7-10 sentences), followed by a single markdown code block (using the format ```python ... ```) which implements this solution and prints out the evaluation metric(s) if applicable. T...`
##### `_prompt_metricparse_resp_fmt(self)` (L407)
- Inputs: parameters from signature `_prompt_metricparse_resp_fmt(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L408: `{'Response format': 'Your response should be a brief outline/sketch of your proposed solution in natural language (3-5 sentences), followed by a single markdown code block (using the format ```python ... ```) which implements the full code for the metric parsing. There should be no additional hea...`
##### `_prompt_debug_resp_fmt(self)` (L418)
- Inputs: parameters from signature `_prompt_debug_resp_fmt(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L419: `{'Response format': 'Your response should be a brief outline/sketch of your proposed solution in natural language (3-5 sentences), followed by a single markdown code block (using the format ```python ... ```) which implements the full code including the bugfix/solution. There should be no additio...`
##### `_prompt_hyperparam_tuning_resp_fmt(self)` (L430)
- Inputs: parameters from signature `_prompt_hyperparam_tuning_resp_fmt(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L431: `{'Response format': 'Your response should be a brief outline/sketch of your proposed solution in natural language (3-5 sentences), followed by a single markdown code block (using the format ```python ... ```) which implements the full code including hyperparameter tuning. There should be no addit...`
##### `_prompt_ablation_resp_fmt(self)` (L442)
- Inputs: parameters from signature `_prompt_ablation_resp_fmt(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L443: `{'Response format': 'Your response should be a brief outline/sketch of your proposed solution in natural language (3-5 sentences), followed by a single markdown code block (using the format ```python ... ```) which implements the full code including the ablation study. There should be no addition...`
##### `_draft(self)` (L453)
- Inputs: parameters from signature `_draft(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L492: `Node(plan=plan, code=code)`
- Conditions / decisions:
  - L481: IF `self.cfg.agent.data_preview`; body=1 else=0
- LLM/VLM calls:
  - L490: `self.plan_and_code_query`
- Main call graph hints: `print`, `self.plan_and_code_query`, `Node`
##### `_debug(self, parent_node)` (L494)
- Inputs: parameters from signature `_debug(self, parent_node)` plus referenced module/global/config state.
- Outputs / returns:
  - L521: `Node(plan=plan, code=code, parent=parent_node)`
- Conditions / decisions:
  - L517: IF `self.cfg.agent.data_preview`; body=1 else=0
- LLM/VLM calls:
  - L520: `self.plan_and_code_query`
- Main call graph hints: `self.plan_and_code_query`, `Node`, `wrap_code`
##### `_improve(self, parent_node)` (L523)
- Inputs: parameters from signature `_improve(self, parent_node)` plus referenced module/global/config state.
- Outputs / returns:
  - L543: `Node(plan=plan, code=code, parent=parent_node)`
- LLM/VLM calls:
  - L542: `self.plan_and_code_query`
- Main call graph hints: `self.plan_and_code_query`, `Node`, `wrap_code`
##### `_generate_seed_node(self, parent_node)` (L549)
- Inputs: parameters from signature `_generate_seed_node(self, parent_node)` plus referenced module/global/config state.
- Outputs / returns:
  - L550: `Node(plan='Seed node', code=parent_node.code, parent=parent_node, is_seed_node=True)`
- Main call graph hints: `Node`
##### `_generate_hyperparam_tuning_node(self, parent_node, hyperparam_idea)` (L557)
- Inputs: parameters from signature `_generate_hyperparam_tuning_node(self, parent_node, hyperparam_idea)` plus referenced module/global/config state.
- Outputs / returns:
  - L598: `Node(plan='Hyperparam tuning name: ' + hyperparam_idea.name + '.\n' + plan, code=code, parent=parent_node, hyperparam_name=hyperparam_idea.name)`
- LLM/VLM calls:
  - L597: `self.plan_and_code_query`
- Main call graph hints: `self.plan_and_code_query`, `Node`, `wrap_code`
##### `_generate_ablation_node(self, parent_node, ablation_idea)` (L605)
- Inputs: parameters from signature `_generate_ablation_node(self, parent_node, ablation_idea)` plus referenced module/global/config state.
- Outputs / returns:
  - L651: `Node(plan='Ablation name: ' + ablation_idea.name + '.\n' + plan, code=code, parent=parent_node, ablation_name=ablation_idea.name)`
- LLM/VLM calls:
  - L650: `self.plan_and_code_query`
- Main call graph hints: `self.plan_and_code_query`, `Node`, `wrap_code`
##### `plan_and_code_query(self, prompt, retries)` (L658)
- Docstring: Generate a natural language plan + code in the same LLM call and split them apart.
- Inputs: parameters from signature `plan_and_code_query(self, prompt, retries)` plus referenced module/global/config state.
- Outputs / returns:
  - L681: `('', completion_text)`
  - L674: `(nl_text, code)`
- Loops:
  - L661: {'line': 661, 'type': 'for', 'target': '_', 'iter': 'range(retries)', 'body_len': 6, 'orelse_len': 0}
- Conditions / decisions:
  - L672: IF `code and nl_text`; body=1 else=0
- LLM/VLM calls:
  - L662: `query`
- Main call graph hints: `range`, `print`, `query`, `extract_code`, `extract_text_up_to_code`
##### `parse_exec_result(self, node, exec_result, workspace)` (L683)
- Inputs: parameters from signature `parse_exec_result(self, node, exec_result, workspace)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- LLM/VLM calls:
  - L703: `query`
- Main call graph hints: `logger.info`, `node.absorb_exec_result`, `cast`, `print`, `wrap_code`, `query`
##### `_generate_plotting_code(self, node, working_dir, plot_code_from_prev_stage)` (L720)
- Docstring: Generate code for plotting experiment results
- Inputs: parameters from signature `_generate_plotting_code(self, node, working_dir, plot_code_from_prev_stage)` plus referenced module/global/config state.
- Outputs / returns:
  - L833: `code`
- Conditions / decisions:
  - L787: IF `self.stage_name and self.stage_name.startswith('3_') and plot_code_from_prev_stage`; body=1 else=1
  - L827: IF `not code.strip().startswith('import')`; body=1 else=0
  - L805: IF `self.stage_name and self.stage_name.startswith('4_') and plot_code_from_prev_stage`; body=1 else=0
- LLM/VLM calls:
  - L824: `self.plan_and_code_query`
- Main call graph hints: `self.plan_and_code_query`, `self.stage_name.startswith`, `prompt_guideline.extend`, `code.strip.startswith`, `code.strip`
##### `_determine_datasets_successfully_tested(self, node)` (L835)
- Docstring: Determine which datasets are successfully tested based on VLM feedback
- Inputs: parameters from signature `_determine_datasets_successfully_tested(self, node)` plus referenced module/global/config state.
- Outputs / returns:
  - L892: `['']`
  - L882: `datasets`
  - L874: `['']`
- Loops:
  - L838: {'line': 838, 'type': 'for', 'target': '(i, plot_analysis)', 'iter': 'enumerate(node.plot_analyses)', 'body_len': 1, 'orelse_len': 0}
  - L854: {'line': 854, 'type': 'while', 'test': 'retry_count < retry_limit', 'body_len': 7, 'orelse_len': 0}
- Conditions / decisions:
  - L872: IF `reasoning is not None and datasets_successfully_tested_str is not None`; body=5 else=0
  - L873: IF `datasets_successfully_tested_str == ''`; body=1 else=0
- LLM/VLM calls:
  - L855: `query`
- Main call graph hints: `enumerate`, `logger.error`, `query`, `_parse_keyword_prefix_response`, `print`, `logger.warning`, `logger.info`, `ds.strip`, `datasets_successfully_tested_str.split`, `isinstance`
##### `_analyze_plots_with_vlm(self, node)` (L894)
- Docstring: Analyze experimental plots using VLM
- Inputs: parameters from signature `_analyze_plots_with_vlm(self, node)` plus referenced module/global/config state.
- Outputs / returns:
  - L897: `None`
  - L905: `base64.b64encode(image_file.read()).decode('utf-8')`
  - L908: `None`
- Loops:
  - L1025: {'line': 1025, 'type': 'for', 'target': '(index, analysis)', 'iter': "enumerate(response['plot_analyses'])", 'body_len': 1, 'orelse_len': 0}
  - L946: {'line': 946, 'type': 'for', 'target': 'plot_path', 'iter': 'selected_plots', 'body_len': 1, 'orelse_len': 0}
  - L967: {'line': 967, 'type': 'for', 'target': 'plot_path', 'iter': 'node.plot_paths[:10]', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L896: IF `not node.plot_paths`; body=1 else=0
  - L910: IF `not len(node.plot_paths) > 10`; body=1 else=3
  - L1020: IF `response['valid_plots_received']`; body=1 else=1
  - L957: IF `valid_plots`; body=2 else=3
  - L947: IF `isinstance(plot_path, str) and os.path.exists(plot_path) and plot_path.lower().endswith(('.png', '.jpg', '.jpeg'))`; body=1 else=1
  - L968: IF `os.path.exists(plot_path) and plot_path.lower().endswith(('.png', '.jpg', '.jpeg'))`; body=1 else=1
- Exception handling:
  - L928: handlers=['Exception'] else=0 final=0
  - L904: handlers=['Exception'] else=0 final=0
- LLM/VLM calls:
  - L1009: `query`
  - L931: `query`
- I/O / network / subprocess side effects:
  - L903: `open`
- Main call graph hints: `print`, `cast`, `enumerate`, `self._determine_datasets_successfully_tested`, `query`, `open`, `len`, `response_select_plots.get`, `base64.b64encode.decode`, `logger.warning`, `logger.error`, `isinstance`, `os.path.exists`, `plot_path.lower.endswith`, `valid_plots.append`, `base64.b64encode`, `selected_plots.append`, `image_file.read`, `plot_path.lower`, `str`, `encode_image_to_base64`
##### `_generate_node_summary(self, node)` (L1035)
- Docstring: Generate a summary of the node's experimental findings
- Inputs: parameters from signature `_generate_node_summary(self, node)` plus referenced module/global/config state.
- Outputs / returns:
  - L1058: `cast(dict, query(system_message=summary_prompt, user_message=None, func_spec={'name': 'summarize_experiment', 'description': 'Summarize experimental findings', 'parameters': {'type': 'object', 'properties': {'findings': {'type': 'string', 'description': 'Key findings and results'}, 'significance'...`
- LLM/VLM calls:
  - L1060: `query`
- Main call graph hints: `cast`, `wrap_code`, `query`, `str`, `hasattr`
#### Class `GPUManager` (L1091)
- Bases: `object`
- Docstring: Manages GPU allocation across processes
##### `__init__(self, num_gpus)` (L1094)
- Inputs: parameters from signature `__init__(self, num_gpus)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `set`, `range`
##### `acquire_gpu(self, process_id)` (L1099)
- Docstring: Assigns a GPU to a process
- Inputs: parameters from signature `acquire_gpu(self, process_id)` plus referenced module/global/config state.
- Outputs / returns:
  - L1110: `gpu_id`
- Conditions / decisions:
  - L1101: IF `not self.available_gpus`; body=1 else=0
- Raises:
  - L1102: `RuntimeError('No GPUs available')`
- Main call graph hints: `print`, `min`, `self.available_gpus.remove`, `RuntimeError`
##### `release_gpu(self, process_id)` (L1112)
- Docstring: Releases GPU assigned to a process
- Inputs: parameters from signature `release_gpu(self, process_id)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Conditions / decisions:
  - L1114: IF `process_id in self.gpu_assignments`; body=3 else=0
- Main call graph hints: `self.available_gpus.add`
#### Class `ParallelAgent` (L1142)
- Bases: `object`
##### `__init__(self, task_desc, cfg, journal, stage_name, best_stage3_node, best_stage2_node, best_stage1_node)` (L1143)
- Inputs: parameters from signature `__init__(self, task_desc, cfg, journal, stage_name, best_stage3_node, best_stage2_node, best_stage1_node)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Conditions / decisions:
  - L1171: IF `self.num_gpus == 0`; body=1 else=1
  - L1178: IF `self.num_gpus > 0`; body=2 else=0
- Main call graph hints: `super.__init__`, `get_gpu_count`, `print`, `ProcessPoolExecutor`, `self._define_global_metrics`, `GPUManager`, `min`, `logger.info`, `set`, `super`
##### `_define_global_metrics(self)` (L1194)
- Docstring: Define eval metric to be used across all experiments
- Inputs: parameters from signature `_define_global_metrics(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L1222: `response`
- LLM/VLM calls:
  - L1214: `query`
- Main call graph hints: `query`, `print`
##### `plan_and_code_query(self, prompt, retries)` (L1224)
- Docstring: Generate a natural language plan + code in the same LLM call and split them apart.
- Inputs: parameters from signature `plan_and_code_query(self, prompt, retries)` plus referenced module/global/config state.
- Outputs / returns:
  - L1246: `('', completion_text)`
  - L1240: `(nl_text, code)`
- Loops:
  - L1227: {'line': 1227, 'type': 'for', 'target': '_', 'iter': 'range(retries)', 'body_len': 6, 'orelse_len': 0}
- Conditions / decisions:
  - L1238: IF `code and nl_text`; body=1 else=0
- LLM/VLM calls:
  - L1228: `query`
- Main call graph hints: `range`, `print`, `query`, `extract_code`, `extract_text_up_to_code`
##### `_generate_seed_eval_aggregation_node(self, node, agg_plotting_code)` (L1248)
- Docstring: Generate a special aggregation node for seed evaluation results
- Inputs: parameters from signature `_generate_seed_eval_aggregation_node(self, node, agg_plotting_code)` plus referenced module/global/config state.
- Outputs / returns:
  - L1252: `Node(plan='Aggregate results from multiple seeds', code='# plotting aggregation code', plot_code=agg_plotting_code, parent=node, is_seed_node=True, is_seed_agg_node=True)`
- Main call graph hints: `Node`
##### `_run_multi_seed_evaluation(self, node)` (L1261)
- Docstring: Run multiple seeds of the same node to get statistical metrics.
Returns a list of nodes with different random seeds.
- Inputs: parameters from signature `_run_multi_seed_evaluation(self, node)` plus referenced module/global/config state.
- Outputs / returns:
  - L1330: `seed_nodes`
- Loops:
  - L1272: {'line': 1272, 'type': 'for', 'target': 'seed', 'iter': 'range(self.cfg.agent.multi_seed_eval.num_seeds)', 'body_len': 12, 'orelse_len': 0}
  - L1317: {'line': 1317, 'type': 'for', 'target': 'future', 'iter': 'futures', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L1274: IF `self.gpu_manager is not None`; body=1 else=0
- Exception handling:
  - L1318: handlers=['Exception'] else=0 final=0
  - L1275: handlers=['RuntimeError'] else=0 final=0
- Main call graph hints: `node.to_dict`, `range`, `print`, `futures.append`, `self.executor.submit`, `future.result`, `Node.from_dict`, `self.journal.append`, `seed_nodes.append`, `self.gpu_manager.acquire_gpu`, `logger.info`, `self.journal.get_node_by_id`, `logger.error`, `logger.warning`, `str`
##### `_run_plot_aggregation(self, node, seed_nodes)` (L1332)
- Docstring: Generate an aggregation node for seed evaluation results
- Inputs: parameters from signature `_run_plot_aggregation(self, node, seed_nodes)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L1385: {'line': 1385, 'type': 'for', 'target': 'plot_file', 'iter': "plots_dir.glob('*.png')", 'body_len': 7, 'orelse_len': 0}
- Conditions / decisions:
  - L1334: IF `seed_nodes`; body=1 else=0
  - L1365: IF `plots_dir.exists()`; body=7 else=0
  - L1403: IF `process_interpreter`; body=1 else=0
- Exception handling:
  - L1335: handlers=['Exception'] else=0 final=0
  - L1357: handlers=[] else=0 final=1
- I/O / network / subprocess side effects:
  - L1379: `open`
- Main call graph hints: `self._aggregate_seed_eval_results`, `self._generate_seed_eval_aggregation_node`, `print`, `Interpreter`, `process_interpreter.run`, `process_interpreter.cleanup_session`, `plots_dir.exists`, `agg_node.to_dict`, `Node.from_dict`, `self.journal.append`, `Path`, `exp_results_dir.mkdir`, `plots_dir.glob`, `os.getenv`, `open`, `f.write`, `plot_file.resolve.rename`, `agg_node.plots.append`, `agg_node.plot_paths.append`, `plot_file.resolve`, `str`, `final_path.absolute`
##### `_process_node_wrapper(node_data, task_desc, cfg, gpu_id, memory_summary, evaluation_metrics, stage_name, new_ablation_idea, new_hyperparam_idea, best_stage3_plot_code, best_stage2_plot_code, best_stage1_plot_code, seed_eval)` (L1410)
- Docstring: Wrapper function that creates a fresh environment for each process
- Inputs: parameters from signature `_process_node_wrapper(node_data, task_desc, cfg, gpu_id, memory_summary, evaluation_metrics, stage_name, new_ablation_idea, new_hyperparam_idea, best_stage3_plot_code, best_stage2_plot_code, best_stage1_plot_code, seed_eval)` plus referenced module/global/config state.
- Outputs / returns:
  - L1789: `result_data`
- Loops:
  - L1672: {'line': 1672, 'type': 'while', 'test': 'True', 'body_len': 5, 'orelse_len': 0}
  - L1740: {'line': 1740, 'type': 'for', 'target': 'exp_data_file', 'iter': "plots_dir.glob('*.npy')", 'body_len': 3, 'orelse_len': 0}
  - L1745: {'line': 1745, 'type': 'for', 'target': 'plot_file', 'iter': "plots_dir.glob('*.png')", 'body_len': 10, 'orelse_len': 0}
- Conditions / decisions:
  - L1443: IF `gpu_id is not None`; body=2 else=2
  - L1471: IF `node_data`; body=2 else=2
  - L1480: IF `seed_eval`; body=3 else=1
  - L1536: IF `not data_files`; body=1 else=2
  - L1669: IF `not child_node.is_buggy`; body=2 else=0
  - L1487: IF `parent_node is None`; body=2 else=1
  - L1541: IF `seed_eval`; body=6 else=6
  - L1772: IF `child_node.plots`; body=1 else=0
  - L1490: IF `parent_node.is_buggy`; body=3 else=1
  - L1606: IF `metrics_exec_result.exc_type is None`; body=6 else=3
  - L1716: IF `plots_dir.exists()`; body=14 else=0
  - L1495: IF `new_hyperparam_idea is not None and new_ablation_idea is None`; body=4 else=1
  - L1634: IF `metrics_response['valid_metrics_received']`; body=2 else=3
  - L1673: IF `seed_eval`; body=1 else=2
  - L1698: IF `child_node.plot_exc_type and retry_count < 3`; body=5 else=1
  - L1508: IF `new_ablation_idea is not None and new_hyperparam_idea is None`; body=4 else=3
  - L1677: IF `worker_agent.stage_name and worker_agent.stage_name.startswith('3_') and best_stage2_plot_code`; body=1 else=1
  - L1683: IF `worker_agent.stage_name and worker_agent.stage_name.startswith('4_') and best_stage3_plot_code`; body=1 else=1
- Exception handling:
  - L1468: handlers=['Exception'] else=0 final=0
  - L1595: handlers=['Exception'] else=0 final=0
  - L1670: handlers=['Exception'] else=0 final=0
  - L1773: handlers=['Exception'] else=0 final=0
- Raises:
  - L1796: ``
- LLM/VLM calls:
  - L1590: `worker_agent.plan_and_code_query`
  - L1621: `query`
- I/O / network / subprocess side effects:
  - L1437: `os.makedirs`
  - L1441: `os.makedirs`
  - L1731: `open`
  - L1736: `open`
- Main call graph hints: `print`, `os.path.join`, `os.makedirs`, `MinimalAgent`, `Interpreter`, `multiprocessing.current_process`, `str`, `logger.info`, `process_interpreter.run`, `process_interpreter.cleanup_session`, `worker_agent.parse_exec_result`, `child_node.to_dict`, `Node.from_dict`, `worker_agent._generate_seed_node`, `logger.warning`, `traceback.print_exc`, `worker_agent._draft`, `os.listdir`, `f.endswith`, `worker_agent.plan_and_code_query`, `Path`, `plots_dir.exists`, `worker_agent._debug`, `worker_agent._prompt_metricparse_resp_fmt`, `cast`, `logger.error`, `WorstMetricValue`, `exp_results_dir.mkdir`, `plots_dir.glob`, `worker_agent._analyze_plots_with_vlm`, `result_data.keys`, `len`, `worker_agent._generate_hyperparam_tuning_node`, `query`, `MetricValue`, `worker_agent._generate_plotting_code`, `open`, `f.write`, `exp_data_file.resolve.rename`, `plot_file.resolve.rename`, ...
##### `_generate_hyperparam_tuning_idea(self)` (L1798)
- Docstring: Generate the next hyperparam tuning idea based on what's been done.
This is minaly for Stage 2 (baseline tuning).
- Inputs: parameters from signature `_generate_hyperparam_tuning_idea(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L1856: `HyperparamTuningIdea(name='increase learning rate', description='increase learning rate')`
  - L1844: `HyperparamTuningIdea(name=hyperparam_name, description=hyperparam_description)`
- Loops:
  - L1831: {'line': 1831, 'type': 'while', 'test': 'retry_count < retry_limit', 'body_len': 5, 'orelse_len': 0}
- Conditions / decisions:
  - L1843: IF `hyperparam_name and hyperparam_description`; body=1 else=0
- LLM/VLM calls:
  - L1832: `query`
- Main call graph hints: `list`, `logger.error`, `HyperparamTuningIdea`, `wrap_code`, `query`, `_parse_keyword_prefix_response`, `logger.warning`
##### `_generate_ablation_idea(self)` (L1860)
- Docstring: Generate the next ablation idea based on what's been done
- Inputs: parameters from signature `_generate_ablation_idea(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L1919: `AblationIdea(name='add one more layer', description='add one more layer')`
  - L1907: `AblationIdea(name=ablation_name, description=ablation_description)`
- Loops:
  - L1894: {'line': 1894, 'type': 'while', 'test': 'retry_count < retry_limit', 'body_len': 5, 'orelse_len': 0}
- Conditions / decisions:
  - L1906: IF `ablation_name and ablation_description`; body=1 else=0
- LLM/VLM calls:
  - L1895: `query`
- Main call graph hints: `list`, `logger.error`, `AblationIdea`, `wrap_code`, `query`, `_parse_keyword_prefix_response`, `logger.warning`
##### `_get_leaves(self, node)` (L1921)
- Docstring: Get all leaf nodes in the subtree rooted at node.
- Inputs: parameters from signature `_get_leaves(self, node)` plus referenced module/global/config state.
- Outputs / returns:
  - L1929: `leaves`
  - L1924: `[node]`
- Loops:
  - L1927: {'line': 1927, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L1923: IF `not node.children`; body=1 else=0
- Main call graph hints: `leaves.extend`, `self._get_leaves`
##### `_select_parallel_nodes(self)` (L1931)
- Docstring: Select N nodes to process in parallel,
balancing between tree exploration and exploitation.
Note:
- This function runs in the main process.
Some design considerations:
- For Stage 2 and 4, we generate nodes in the main process and
send them to worker processes.
This is to make sure we don't run duplicate ideas in parallel.
- For Stage 1 and 3, we generate nodes in worker processes.
- Inputs: parameters from signature `_select_parallel_nodes(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L2051: `nodes_to_process`
- Loops:
  - L1947: {'line': 1947, 'type': 'while', 'test': 'len(nodes_to_process) < self.num_workers', 'body_len': 6, 'orelse_len': 0}
  - L1974: {'line': 1974, 'type': 'for', 'target': '(i, n)', 'iter': 'enumerate(buggy_nodes)', 'body_len': 1, 'orelse_len': 0}
  - L1995: {'line': 1995, 'type': 'while', 'test': 'tree_root.parent', 'body_len': 1, 'orelse_len': 0}
  - L2027: {'line': 2027, 'type': 'while', 'test': 'tree_root.parent', 'body_len': 1, 'orelse_len': 0}
  - L2039: {'line': 2039, 'type': 'for', 'target': 'node', 'iter': 'sorted(good_nodes, key=lambda n: n.metric, reverse=True)', 'body_len': 4, 'orelse_len': 0}
  - L2041: {'line': 2041, 'type': 'while', 'test': 'tree_root.parent', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L1952: IF `len(self.journal.draft_nodes) < search_cfg.num_drafts`; body=2 else=0
  - L1964: IF `random.random() < search_cfg.debug_prob`; body=3 else=0
  - L2009: IF `self.stage_name and self.stage_name.startswith('4_')`; body=2 else=1
  - L1991: IF `debuggable_nodes`; body=6 else=0
  - L2013: IF `self.stage_name and self.stage_name.startswith('2_')`; body=2 else=9
  - L1999: IF `tree_id not in processed_trees or len(processed_trees) >= len(viable_trees)`; body=3 else=0
  - L2020: IF `not good_nodes`; body=2 else=0
  - L2031: IF `tree_id not in processed_trees or len(processed_trees) >= len(viable_trees)`; body=3 else=0
  - L1975: IF `not isinstance(n, Node)`; body=2 else=0
  - L2044: IF `tree_id not in processed_trees or len(processed_trees) >= len(viable_trees)`; body=3 else=0
- Exception handling:
  - L1967: handlers=['Exception'] else=0 final=0
- Raises:
  - L1977: `ValueError('Found non-Node object in journal.buggy_nodes')`
- Main call graph hints: `set`, `print`, `len`, `nodes_to_process.append`, `random.random`, `self.stage_name.startswith`, `enumerate`, `random.choice`, `id`, `self.journal.get_best_node`, `sorted`, `all`, `processed_trees.add`, `isinstance`, `ValueError`, `type`, `self._get_leaves`
##### `step(self, exec_callback)` (L2053)
- Inputs: parameters from signature `step(self, exec_callback)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L2060: {'line': 2060, 'type': 'for', 'target': 'node', 'iter': 'nodes_to_process', 'body_len': 1, 'orelse_len': 0}
  - L2085: {'line': 2085, 'type': 'for', 'target': 'node_data', 'iter': 'node_data_list', 'body_len': 8, 'orelse_len': 0}
  - L2149: {'line': 2149, 'type': 'for', 'target': '(i, future)', 'iter': 'enumerate(futures)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L2072: IF `self.cfg.agent.get('summary', None) is not None`; body=1 else=1
  - L2061: IF `node`; body=1 else=1
  - L2087: IF `self.gpu_manager is not None`; body=1 else=0
  - L2096: IF `self.stage_name and self.stage_name.startswith('2_') and (node_data['is_buggy'] is False)`; body=3 else=1
  - L2106: IF `self.stage_name and self.stage_name.startswith('4_') and (node_data['is_buggy'] is False)`; body=3 else=2
  - L2153: IF `'metric' in result_data`; body=2 else=0
  - L2185: IF `self.gpu_manager is not None and process_id in self.gpu_manager.gpu_assignments`; body=2 else=0
- Exception handling:
  - L2150: handlers=['TimeoutError', 'Exception'] else=0 final=2
  - L2062: handlers=['Exception'] else=0 final=0
  - L2088: handlers=['RuntimeError'] else=0 final=0
- Raises:
  - L2181: ``
  - L2068: ``
- Main call graph hints: `print`, `self._select_parallel_nodes`, `enumerate`, `self.cfg.agent.get`, `self.journal.generate_summary`, `futures.append`, `node_data_list.append`, `self.stage_name.startswith`, `self._generate_hyperparam_tuning_idea`, `self._hyperparam_tuning_state[...].add`, `self.executor.submit`, `future.result`, `Node.from_dict`, `self._update_hyperparam_tuning_state`, `self._update_ablation_state`, `self.journal.append`, `node.to_dict`, `_safe_pickle_test`, `self.gpu_manager.acquire_gpu`, `logger.info`, `self._generate_ablation_idea`, `self._ablation_state[...].add`, `logger.error`, `traceback.print_exc`, `self.gpu_manager.release_gpu`, `logger.warning`, `len`, `type`, `str`
##### `_update_hyperparam_tuning_state(self, result_node)` (L2192)
- Docstring: Update hyperparam tuning tracking state based on execution results.
- Inputs: parameters from signature `_update_hyperparam_tuning_state(self, result_node)` plus referenced module/global/config state.
- Outputs / returns:
  - L2195: `None`
  - L2202: `None`
- Conditions / decisions:
  - L2194: IF `not self.stage_name or not self.stage_name.startswith('2_')`; body=1 else=0
  - L2198: IF `hyperparam_name is None`; body=2 else=0
  - L2204: IF `not result_node.is_buggy`; body=2 else=1
- Main call graph hints: `print`, `self._hyperparam_tuning_state[...].add`, `logger.info`, `logger.warning`, `self.stage_name.startswith`
##### `_update_ablation_state(self, result_node)` (L2210)
- Docstring: Update ablation tracking state based on execution results.

Args:
    result_node: Node containing ablation execution results
- Inputs: parameters from signature `_update_ablation_state(self, result_node)` plus referenced module/global/config state.
- Outputs / returns:
  - L2217: `None`
  - L2222: `None`
- Conditions / decisions:
  - L2216: IF `not self.stage_name or not self.stage_name.startswith('4_')`; body=1 else=0
  - L2220: IF `ablation_name is None`; body=2 else=0
  - L2224: IF `not result_node.is_buggy`; body=2 else=0
- Main call graph hints: `print`, `self._ablation_state[...].add`, `logger.info`, `self.stage_name.startswith`
##### `_aggregate_seed_eval_results(self, seed_nodes, parent_node)` (L2228)
- Docstring: Generate aggregated plots from multi-seed evaluation results.

Args:
    seed_nodes: List of nodes from seed evaluation
    parent_node: The original node that was evaluated

Returns:
    str: The plotting code for aggregated results
- Inputs: parameters from signature `_aggregate_seed_eval_results(self, seed_nodes, parent_node)` plus referenced module/global/config state.
- Outputs / returns:
  - L2331: `code`
- LLM/VLM calls:
  - L2326: `self.plan_and_code_query`
- Main call graph hints: `self.plan_and_code_query`, `print`
##### `__enter__(self)` (L2333)
- Inputs: parameters from signature `__enter__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L2334: `self`
##### `cleanup(self)` (L2336)
- Docstring: Cleanup parallel workers and resources
- Inputs: parameters from signature `cleanup(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L2343: {'line': 2343, 'type': 'for', 'target': 'process_id', 'iter': 'list(self.gpu_manager.gpu_assignments.keys())', 'body_len': 1, 'orelse_len': 0}
  - L2355: {'line': 2355, 'type': 'for', 'target': 'process', 'iter': 'processes', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L2338: IF `not self._is_shutdown`; body=2 else=0
  - L2342: IF `self.gpu_manager is not None`; body=1 else=0
  - L2350: IF `self.executor._processes`; body=2 else=0
  - L2356: IF `process.is_alive()`; body=2 else=0
- Exception handling:
  - L2340: handlers=['Exception'] else=0 final=1
- Main call graph hints: `print`, `self.executor.shutdown`, `list`, `self.gpu_manager.gpu_assignments.keys`, `self.gpu_manager.release_gpu`, `self.executor._processes.values`, `process.is_alive`, `process.terminate`, `process.join`
##### `__exit__(self, exc_type, exc_val, exc_tb)` (L2367)
- Inputs: parameters from signature `__exit__(self, exc_type, exc_val, exc_tb)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `self.cleanup`

### Functions

#### `_safe_pickle_test(obj, name)` (L31)
- Docstring: Test if an object can be pickled
- Inputs: parameters from signature `_safe_pickle_test(obj, name)` plus referenced module/global/config state.
- Outputs / returns:
  - L35: `True`
  - L38: `False`
- Exception handling:
  - L33: handlers=['Exception'] else=0 final=0
- I/O / network / subprocess side effects:
  - L34: `pickle.dumps`
- Main call graph hints: `pickle.dumps`, `logger.error`, `str`
#### `_parse_keyword_prefix_response(response, keyword_prefix1, keyword_prefix2)` (L41)
- Docstring: Parse the response into name and description based on keyword prefix
- Inputs: parameters from signature `_parse_keyword_prefix_response(response, keyword_prefix1, keyword_prefix2)` plus referenced module/global/config state.
- Outputs / returns:
  - L73: `(name, description)`
  - L78: `(None, None)`
- Loops:
  - L53: {'line': 53, 'type': 'for', 'target': 'line', 'iter': 'lines', 'body_len': 1, 'orelse_len': 0}
  - L60: {'line': 60, 'type': 'for', 'target': 'next_line', 'iter': 'lines[lines.index(line) + 1:]', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L68: IF `name is None or description is None`; body=1 else=0
  - L54: IF `line.startswith(keyword_prefix1)`; body=1 else=1
  - L56: IF `line.startswith(keyword_prefix2)`; body=4 else=0
  - L65: IF `desc_lines`; body=1 else=0
  - L61: IF `not next_line.startswith((keyword_prefix1, keyword_prefix2))`; body=1 else=1
- Exception handling:
  - L45: handlers=['Exception'] else=0 final=0
- Raises:
  - L69: `ValueError(f'Missing required keywords in response: {keyword_prefix1} and/or {keyword_prefix2}')`
- Main call graph hints: `line.strip`, `line.startswith`, `ValueError`, `logger.error`, `logger.debug`, `response.split`, `line.replace.strip`, `line.replace`, `Constant.join`, `str`, `next_line.startswith`, `desc_lines.append`, `lines.index`
#### `get_gpu_count()` (L1120)
- Docstring: Get number of available NVIDIA GPUs without using torch
- Inputs: parameters from signature `get_gpu_count()` plus referenced module/global/config state.
- Outputs / returns:
  - L1131: `len(gpus)`
  - L1139: `0`
  - L1138: `len(devices)`
- Conditions / decisions:
  - L1135: IF `cuda_visible_devices`; body=2 else=0
- Exception handling:
  - L1122: handlers=['(subprocess.SubprocessError, FileNotFoundError)'] else=0 final=0
- I/O / network / subprocess side effects:
  - L1124: `subprocess.run`
- Main call graph hints: `subprocess.run`, `nvidia_smi.stdout.strip.split`, `len`, `os.environ.get`, `nvidia_smi.stdout.strip`, `cuda_visible_devices.split`

---

## File: `ai_scientist/treesearch/perform_experiments_bfts_with_agentmanager.py`

**Lines:** 263  


### Imports / external dependencies

- `import atexit`
- `import logging`
- `import shutil`
- `import json`
- `import pickle`
- `from . import backend`
- `from .journal import Journal, Node`
- `from .journal2report import journal2report`
- `from rich.columns import Columns`
- `from rich.console import Group`
- `from rich.live import Live`
- `from rich.padding import Padding`
- `from rich.panel import Panel`
- `from rich.progress import ( BarColumn, MofNCompleteColumn, Progress, TextColumn, TimeRemainingColumn, )`
- `from rich.text import Text`
- `from rich.status import Status`
- `from rich.tree import Tree`
- `from .utils.config import load_task_desc, prep_agent_workspace, save_run, load_cfg`
- `from .agent_manager import AgentManager`
- `from pathlib import Path`
- `from .agent_manager import Stage`
- `from .log_summarization import overall_summarize`

### Module-level assignments / constants

- L31: `logger = logging.getLogger("ai-scientist")`

### Prompt-like assignments in this file

- None detected

### Top-level decisions / loops / try blocks

- IF L259: `__name__ == '__main__'`; body=3 else=0

### Classes

- None

### Functions

#### `journal_to_rich_tree(journal, cfg)` (L34)
- Inputs: parameters from signature `journal_to_rich_tree(journal, cfg)` plus referenced module/global/config state.
- Outputs / returns:
  - L55: `tree`
- Loops:
  - L53: {'line': 53, 'type': 'for', 'target': 'n', 'iter': 'journal.draft_nodes', 'body_len': 1, 'orelse_len': 0}
  - L49: {'line': 49, 'type': 'for', 'target': 'child', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L38: IF `node.is_buggy`; body=1 else=2
  - L43: IF `node is best_node`; body=1 else=1
- Main call graph hints: `journal.get_best_node`, `Tree`, `tree.add`, `append_rec`
#### `perform_experiments_bfts(config_path)` (L58)
- Inputs: parameters from signature `perform_experiments_bfts(config_path)` plus referenced module/global/config state.
- Outputs / returns:
  - L101: `exec_callback`
  - L193: `Panel(Group(Padding(wide, (1, 1, 1, 1)), Columns([Padding(left, (1, 2, 1, 1)), Padding(right, (1, 1, 1, 2))], equal=True)), title=f'[b]AIDE is working on experiment: [bold green]"{cfg.exp_name}[/b]"', subtitle='Press [b]Ctrl+C[/b] to stop the run')`
  - L99: `res`
- Conditions / decisions:
  - L227: IF `cfg.generate_report`; body=15 else=0
  - L74: IF `global_step == 0`; body=1 else=0
  - L167: IF `current_journal`; body=1 else=1
  - L111: IF `journal.nodes`; body=2 else=0
  - L121: IF `cfg.agent.get('summary', None) is not None`; body=1 else=1
  - L113: IF `hasattr(latest_node, '_agent')`; body=2 else=0
- Exception handling:
  - L214: handlers=['Exception'] else=0 final=0
  - L105: handlers=['Exception'] else=0 final=0
  - L220: handlers=['Exception'] else=0 final=0
- I/O / network / subprocess side effects:
  - L215: `open`
  - L216: `pickle.dump`
  - L240: `open`
  - L241: `json.dump`
  - L243: `open`
  - L244: `json.dump`
  - L246: `open`
  - L247: `json.dump`
  - L249: `open`
  - L250: `json.dump`
  - L148: `open`
  - L149: `json.dump`
  - L221: `open`
  - L222: `pickle.dump`
  - L115: `open`
  - L118: `json.dump`
- Main call graph hints: `Path`, `load_cfg`, `logger.info`, `load_task_desc`, `print`, `backend.compile_prompt_to_md`, `atexit.register`, `AgentManager`, `Progress`, `Status`, `prog.add_task`, `Live`, `manager.run`, `prep_agent_workspace`, `TextColumn`, `BarColumn`, `MofNCompleteColumn`, `TimeRemainingColumn`, `manager.journals.get`, `Group`, `Panel`, `generate_live`, `overall_summarize`, `shutil.rmtree`, `status_obj.update`, `interpreter.run`, `notes_dir.mkdir`, `journal.get_best_node`, `save_run`, `journal_to_rich_tree`, `Tree`, `create_exec_callback`, `open`, `pickle.dump`, `logger.warning`, `manager.journals.items`, `json.dump`, `hasattr`, `cfg.agent.get`, `journal.generate_summary`, ...

---

## File: `ai_scientist/treesearch/utils/__init__.py`

**Lines:** 101  


### Imports / external dependencies

- `import logging`
- `import shutil`
- `import zipfile`
- `from pathlib import Path`

### Module-level assignments / constants

- L6: `logger = logging.getLogger("ai-scientist")`

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `copytree(src, dst, use_symlinks)` (L9)
- Docstring: Copy contents of `src` to `dst`. Unlike shutil.copytree, the dst dir can exist and will be merged.
If src is a file, only that file will be copied. Optionally uses symlinks instead of copying.

Args:
    src (Path): source directory
    dst (Path): destination directory
- Inputs: parameters from signature `copytree(src, dst, use_symlinks)` plus referenced module/global/config state.
- Outputs / returns:
  - L27: `None`
- Loops:
  - L29: {'line': 29, 'type': 'for', 'target': 'f', 'iter': 'src.iterdir()', 'body_len': 3, 'orelse_len': 0}
- Conditions / decisions:
  - L20: IF `src.is_file()`; body=4 else=0
  - L23: IF `use_symlinks`; body=1 else=1
  - L32: IF `use_symlinks`; body=1 else=1
  - L34: IF `f.is_dir()`; body=1 else=1
- I/O / network / subprocess side effects:
  - L26: `shutil.copyfile`
  - L35: `shutil.copytree`
  - L37: `shutil.copyfile`
- Main call graph hints: `dst.is_dir`, `src.is_file`, `src.iterdir`, `dest_f.exists`, `dest_f.symlink_to`, `shutil.copyfile`, `f.is_dir`, `shutil.copytree`
#### `clean_up_dataset(path)` (L40)
- Inputs: parameters from signature `clean_up_dataset(path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L41: {'line': 41, 'type': 'for', 'target': 'item', 'iter': "path.rglob('__MACOSX')", 'body_len': 1, 'orelse_len': 0}
  - L44: {'line': 44, 'type': 'for', 'target': 'item', 'iter': "path.rglob('.DS_Store')", 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L42: IF `item.is_dir()`; body=1 else=0
  - L45: IF `item.is_file()`; body=1 else=0
- Main call graph hints: `path.rglob`, `item.is_dir`, `item.is_file`, `shutil.rmtree`, `item.unlink`
#### `extract_archives(path)` (L49)
- Docstring: unzips all .zip files within `path` and cleans up task dir

[TODO] handle nested zips
- Inputs: parameters from signature `extract_archives(path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L55: {'line': 55, 'type': 'for', 'target': 'zip_f', 'iter': "path.rglob('*.zip')", 'body_len': 9, 'orelse_len': 0}
  - L85: {'line': 85, 'type': 'for', 'target': 'f', 'iter': "sub_item.rglob('*')", 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L59: IF `f_out_dir.exists()`; body=3 else=0
  - L80: IF `len(contents) == 1 and contents[0].name == f_out_dir.name`; body=2 else=0
  - L65: IF `f_out_dir.is_file() and f_out_dir.suffix != ''`; body=1 else=0
  - L83: IF `sub_item.is_dir()`; body=3 else=1
  - L89: IF `sub_item.is_file()`; body=4 else=0
- Main call graph hints: `path.rglob`, `zip_f.with_suffix`, `f_out_dir.exists`, `logger.debug`, `f_out_dir.mkdir`, `clean_up_dataset`, `list`, `zip_f.unlink`, `zipfile.ZipFile`, `zip_ref.extractall`, `f_out_dir.iterdir`, `sub_item.is_dir`, `f_out_dir.is_file`, `len`, `sub_item.rglob`, `sub_item.rmdir`, `sub_item.is_file`, `shutil.move`, `sub_item.rename`, `f_out_dir.rmdir`, `sub_item_tmp.rename`, `f_out_dir.with_suffix`
#### `preproc_data(path)` (L98)
- Inputs: parameters from signature `preproc_data(path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `extract_archives`, `clean_up_dataset`

---

## File: `ai_scientist/treesearch/utils/config.py`

**Lines:** 260  

**Module docstring:** configuration and setup utils


### Imports / external dependencies

- `from dataclasses import dataclass`
- `from pathlib import Path`
- `from typing import Hashable, cast, Literal, Optional`
- `import coolname`
- `import rich`
- `from omegaconf import OmegaConf`
- `from rich.syntax import Syntax`
- `import shutup`
- `from rich.logging import RichHandler`
- `import logging`
- `from . import tree_export`
- `from . import copytree, preproc_data, serialize`

### Module-level assignments / constants

- L22: `logger = logging.getLogger("ai-scientist")`

### Prompt-like assignments in this file

- None detected

### Classes

#### Class `ThinkingConfig` (L30)
- Bases: `object`
#### Class `StageConfig` (L36)
- Bases: `object`
#### Class `SearchConfig` (L45)
- Bases: `object`
#### Class `DebugConfig` (L52)
- Bases: `object`
#### Class `AgentConfig` (L57)
- Bases: `object`
#### Class `ExecConfig` (L77)
- Bases: `object`
#### Class `ExperimentConfig` (L84)
- Bases: `object`
#### Class `Config` (L89)
- Bases: `Hashable`

### Functions

#### `_get_next_logindex(dir)` (L112)
- Docstring: Get the next available index for a log directory.
- Inputs: parameters from signature `_get_next_logindex(dir)` plus referenced module/global/config state.
- Outputs / returns:
  - L122: `max_index + 1`
- Loops:
  - L115: {'line': 115, 'type': 'for', 'target': 'p', 'iter': 'dir.iterdir()', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L117: IF `(current_index := int(p.name.split('-')[0])) > max_index`; body=1 else=0
- Exception handling:
  - L116: handlers=['ValueError'] else=0 final=0
- Main call graph hints: `dir.iterdir`, `print`, `int`, `p.name.split`
#### `_load_cfg(path, use_cli_args)` (L125)
- Inputs: parameters from signature `_load_cfg(path, use_cli_args)` plus referenced module/global/config state.
- Outputs / returns:
  - L131: `cfg`
- Conditions / decisions:
  - L129: IF `use_cli_args`; body=1 else=0
- Main call graph hints: `OmegaConf.load`, `OmegaConf.merge`, `Path`, `OmegaConf.from_cli`
#### `load_cfg(path)` (L134)
- Docstring: Load config from .yaml file and CLI args, and set up logging directory.
- Inputs: parameters from signature `load_cfg(path)` plus referenced module/global/config state.
- Outputs / returns:
  - L136: `prep_cfg(_load_cfg(path))`
- Main call graph hints: `prep_cfg`, `_load_cfg`, `Path`
#### `prep_cfg(cfg)` (L139)
- Inputs: parameters from signature `prep_cfg(cfg)` plus referenced module/global/config state.
- Outputs / returns:
  - L176: `cast(Config, cfg)`
- Conditions / decisions:
  - L140: IF `cfg.data_dir is None`; body=1 else=0
  - L143: IF `cfg.desc_file is None and cfg.goal is None`; body=1 else=0
  - L148: IF `cfg.data_dir.startswith('example_tasks/')`; body=1 else=0
  - L152: IF `cfg.desc_file is not None`; body=1 else=0
  - L173: IF `cfg.agent.type not in ['parallel', 'sequential']`; body=1 else=0
- Raises:
  - L141: `ValueError('`data_dir` must be provided.')`
  - L144: `ValueError('You must provide either a description of the task goal (`goal=...`) or a path to a plaintext file containing the description (`desc_file=...`).')`
  - L174: `ValueError("agent.type must be either 'parallel' or 'sequential'")`
- Main call graph hints: `cfg.data_dir.startswith`, `Path.resolve`, `top_log_dir.mkdir`, `top_workspace_dir.mkdir`, `max`, `BinOp.resolve`, `OmegaConf.structured`, `OmegaConf.merge`, `cast`, `ValueError`, `_get_next_logindex`, `coolname.generate_slug`, `Path`
#### `print_cfg(cfg)` (L179)
- Inputs: parameters from signature `print_cfg(cfg)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `rich.print`, `Syntax`, `OmegaConf.to_yaml`
#### `load_task_desc(cfg)` (L183)
- Docstring: Load task description from markdown file or config str.
- Inputs: parameters from signature `load_task_desc(cfg)` plus referenced module/global/config state.
- Outputs / returns:
  - L206: `task_desc`
  - L194: `f.read()`
- Conditions / decisions:
  - L187: IF `cfg.desc_file is not None`; body=2 else=0
  - L197: IF `cfg.goal is None`; body=1 else=0
  - L203: IF `cfg.eval is not None`; body=1 else=0
  - L188: IF `not (cfg.goal is None and cfg.eval is None)`; body=1 else=0
- Raises:
  - L198: `ValueError('`goal` (and optionally `eval`) must be provided if a task description file is not provided.')`
- I/O / network / subprocess side effects:
  - L193: `open`
- Main call graph hints: `print`, `ValueError`, `logger.warning`, `open`, `f.read`
#### `prep_agent_workspace(cfg)` (L209)
- Docstring: Setup the agent's workspace and preprocess data if necessary.
- Inputs: parameters from signature `prep_agent_workspace(cfg)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Conditions / decisions:
  - L215: IF `cfg.preprocess_data`; body=1 else=0
- Main call graph hints: `BinOp.mkdir`, `copytree`, `preproc_data`
#### `save_run(cfg, journal, stage_name)` (L219)
- Inputs: parameters from signature `save_run(cfg, journal, stage_name)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L247: {'line': 247, 'type': 'for', 'target': 'existing_file', 'iter': "save_dir.glob('best_solution_*.py')", 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L220: IF `stage_name is None`; body=1 else=0
  - L246: IF `best_node is not None`; body=4 else=1
- Exception handling:
  - L226: handlers=['Exception'] else=0 final=0
  - L232: handlers=['Exception'] else=0 final=0
  - L238: handlers=['Exception'] else=0 final=0
  - L244: handlers=['Exception'] else=0 final=0
- Raises:
  - L230: ``
  - L236: ``
  - L242: ``
- I/O / network / subprocess side effects:
  - L251: `open`
  - L254: `open`
- Main call graph hints: `save_dir.mkdir`, `serialize.dump_json`, `OmegaConf.save`, `tree_export.generate`, `journal.get_best_node`, `print`, `save_dir.glob`, `existing_file.unlink`, `open`, `f.write`, `str`

---

## File: `ai_scientist/treesearch/utils/data_preview.py`

**Lines:** 154  

**Module docstring:** Contains functions to manually generate a textual preview of some common file types (.csv, .json,..) for the agent.


### Imports / external dependencies

- `import json`
- `from pathlib import Path`
- `import humanize`
- `import pandas as pd`
- `from genson import SchemaBuilder`
- `from pandas.api.types import is_numeric_dtype`

### Module-level assignments / constants

- L14: `code_files = {".py", ".sh", ".yaml", ".yml", ".md", ".html", ".xml", ".log", ".rst"}`
- L16: `plaintext_files = {".txt", ".csv", ".json", ".tsv"} | code_files`

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `get_file_len_size(f)` (L19)
- Docstring: Calculate the size of a file (#lines for plaintext files, otherwise #bytes)
Also returns a human-readable string representation of the size.
- Inputs: parameters from signature `get_file_len_size(f)` plus referenced module/global/config state.
- Outputs / returns:
  - L26: `(num_lines, f'{num_lines} lines')`
  - L29: `(s, humanize.naturalsize(s))`
- Conditions / decisions:
  - L24: IF `f.suffix in plaintext_files`; body=2 else=2
- I/O / network / subprocess side effects:
  - L25: `open`
- Main call graph hints: `sum`, `f.stat`, `humanize.naturalsize`, `open`
#### `file_tree(path, depth)` (L32)
- Docstring: Generate a tree structure of files in a directory
- Inputs: parameters from signature `file_tree(path, depth)` plus referenced module/global/config state.
- Outputs / returns:
  - L47: `'\n'.join(result)`
- Loops:
  - L38: {'line': 38, 'type': 'for', 'target': 'p', 'iter': 'sorted(files)[:max_n]', 'body_len': 1, 'orelse_len': 0}
  - L43: {'line': 43, 'type': 'for', 'target': 'p', 'iter': 'sorted(dirs)', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L40: IF `len(files) > max_n`; body=1 else=0
- Main call graph hints: `sorted`, `Constant.join`, `result.append`, `len`, `Path.iterdir`, `p.is_dir`, `file_tree`, `Path`, `get_file_len_size`
#### `_walk(path)` (L50)
- Docstring: Recursively walk a directory (analogous to os.walk but for pathlib.Path)
- Inputs: parameters from signature `_walk(path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L52: {'line': 52, 'type': 'for', 'target': 'p', 'iter': 'sorted(Path(path).iterdir())', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L53: IF `p.is_dir()`; body=2 else=0
- Main call graph hints: `sorted`, `Path.iterdir`, `p.is_dir`, `Path`, `_walk`
#### `preview_csv(p, file_name, simple)` (L59)
- Docstring: Generate a textual preview of a csv file

Args:
    p (Path): the path to the csv file
    file_name (str): the file name to use in the preview
    simple (bool, optional): whether to use a simplified version of the preview. Defaults to True.

Returns:
    str: the textual preview
- Inputs: parameters from signature `preview_csv(p, file_name, simple)` plus referenced module/global/config state.
- Outputs / returns:
  - L108: `'\n'.join(out)`
- Loops:
  - L86: {'line': 86, 'type': 'for', 'target': 'col', 'iter': 'sorted(df.columns)', 'body_len': 4, 'orelse_len': 0}
- Conditions / decisions:
  - L76: IF `simple`; body=6 else=2
  - L81: IF `len(cols) > sel_cols`; body=1 else=0
  - L92: IF `dtype == 'bool'`; body=2 else=1
  - L95: IF `df[col].nunique() < 10`; body=1 else=1
  - L99: IF `is_numeric_dtype(df[col])`; body=1 else=1
  - L103: IF `dtype == 'object'`; body=1 else=0
- Main call graph hints: `pd.read_csv`, `out.append`, `Constant.join`, `df.columns.tolist`, `sorted`, `len`, `df[...].isnull.sum`, `df[...][...].mean`, `df[...].isnull`, `df[...].nunique`, `is_numeric_dtype`, `df[...].notnull`, `df[...].unique.tolist`, `df[...].min`, `df[...].max`, `df[...].unique`, `df[...].value_counts.head.index.tolist`, `df[...].value_counts.head`, `df[...].value_counts`
#### `preview_json(p, file_name)` (L111)
- Docstring: Generate a textual preview of a json file using a generated json schema
- Inputs: parameters from signature `preview_json(p, file_name)` plus referenced module/global/config state.
- Outputs / returns:
  - L116: `f'-> {file_name} has auto-generated json schema:\n' + builder.to_json(indent=2)`
- I/O / network / subprocess side effects:
  - L114: `open`
  - L115: `json.load`
- Main call graph hints: `SchemaBuilder`, `open`, `builder.add_object`, `builder.to_json`, `json.load`
#### `generate(base_path, include_file_details, simple)` (L121)
- Docstring: Generate a textual preview of a directory, including an overview of the directory
structure and previews of individual files
- Inputs: parameters from signature `generate(base_path, include_file_details, simple)` plus referenced module/global/config state.
- Outputs / returns:
  - L153: `result`
  - L149: `generate(base_path, include_file_details=include_file_details, simple=True)`
- Loops:
  - L130: {'line': 130, 'type': 'for', 'target': 'fn', 'iter': '_walk(base_path)', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L129: IF `include_file_details`; body=1 else=0
  - L148: IF `len(result) > 6000 and (not simple)`; body=1 else=0
  - L133: IF `fn.suffix == '.csv'`; body=1 else=1
  - L135: IF `fn.suffix == '.json'`; body=1 else=1
  - L137: IF `fn.suffix in plaintext_files`; body=1 else=0
  - L138: IF `get_file_len_size(fn)[0] < 30`; body=1 else=0
  - L141: IF `fn.suffix in code_files`; body=1 else=0
- I/O / network / subprocess side effects:
  - L139: `open`
- Main call graph hints: `Constant.join`, `_walk`, `generate`, `file_tree`, `str`, `len`, `fn.relative_to`, `out.append`, `preview_csv`, `preview_json`, `get_file_len_size`, `open`, `f.read`

---

## File: `ai_scientist/treesearch/utils/metric.py`

**Lines:** 341  


### Imports / external dependencies

- `from dataclasses import dataclass, field`
- `from functools import total_ordering`
- `from typing import Any`
- `import numpy as np`
- `from dataclasses_json import DataClassJsonMixin`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

#### Class `MetricValue_old` (L11)
- Bases: `DataClassJsonMixin`
- Docstring: Represents the value of a metric to be optimized, which can be compared to other metric values.
Comparisons (and max, min) are based on which value is better, not which is larger.
##### `__post_init__(self)` (L26)
- Inputs: parameters from signature `__post_init__(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Conditions / decisions:
  - L27: IF `self.value is not None`; body=1 else=0
  - L28: IF `isinstance(self.value, dict)`; body=1 else=2
- Main call graph hints: `isinstance`, `float`, `self.value.items`
##### `__gt__(self, other)` (L34)
- Docstring: True if self is a _better_ (not necessarily larger) metric value than other
- Inputs: parameters from signature `__gt__(self, other)` plus referenced module/global/config state.
- Outputs / returns:
  - L59: `comp if self.maximize else not comp`
  - L37: `False`
  - L39: `True`
  - L56: `False`
- Conditions / decisions:
  - L36: IF `self.value is None`; body=1 else=0
  - L38: IF `other.value is None`; body=1 else=0
  - L55: IF `self_val == other_val`; body=1 else=0
- Main call graph hints: `isinstance`, `np.mean`, `type`, `list`, `self.value.values`, `other.value.values`
##### `__eq__(self, other)` (L61)
- Inputs: parameters from signature `__eq__(self, other)` plus referenced module/global/config state.
- Outputs / returns:
  - L62: `self.value == other.value`
##### `__repr__(self)` (L64)
- Inputs: parameters from signature `__repr__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L65: `str(self)`
- Main call graph hints: `str`
##### `__str__(self)` (L67)
- Inputs: parameters from signature `__str__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L78: `f'Metric{opt_dir}{metric_name}[{values_str}](mean={mean_val:.4f})'`
  - L80: `f'Metric{opt_dir}{metric_name}({self.value_npsafe:.4f})'`
- Conditions / decisions:
  - L68: IF `self.maximize is None`; body=1 else=1
  - L75: IF `isinstance(self.value_npsafe, dict)`; body=3 else=1
  - L70: IF `self.maximize`; body=1 else=1
- Main call graph hints: `isinstance`, `Constant.join`, `np.mean`, `list`, `self.value_npsafe.values`, `self.value_npsafe.items`
##### `is_worst(self)` (L83)
- Docstring: True if the metric value is the worst possible value.
- Inputs: parameters from signature `is_worst(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L85: `self.value is None`
##### `value_npsafe(self)` (L88)
- Inputs: parameters from signature `value_npsafe(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L95: `self.value`
  - L90: `float('nan')`
  - L92: `{k: v if v is not None else float('nan') for k, v in self.value.items()}`
- Conditions / decisions:
  - L89: IF `self.value is None`; body=1 else=0
  - L91: IF `isinstance(self.value, dict)`; body=1 else=0
- Main call graph hints: `isinstance`, `float`, `self.value.items`
##### `get_dataset_value(self, dataset_name)` (L97)
- Docstring: Get the metric value for a specific dataset
- Inputs: parameters from signature `get_dataset_value(self, dataset_name)` plus referenced module/global/config state.
- Outputs / returns:
  - L101: `None`
  - L100: `self.value.get(dataset_name)`
- Conditions / decisions:
  - L99: IF `isinstance(self.value, dict)`; body=1 else=0
- Main call graph hints: `isinstance`, `self.value.get`
##### `get_mean_value(self)` (L103)
- Docstring: Get the mean value across all datasets (or single value if not multi-dataset)
- Inputs: parameters from signature `get_mean_value(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L109: `float(self.value)`
  - L106: `float('nan')`
  - L108: `float(np.mean(list(self.value.values())))`
- Conditions / decisions:
  - L105: IF `self.value is None`; body=1 else=0
  - L107: IF `isinstance(self.value, dict)`; body=1 else=0
- Main call graph hints: `isinstance`, `float`, `np.mean`, `list`, `self.value.values`
#### Class `MetricValue` (L114)
- Bases: `DataClassJsonMixin`
- Docstring: Represents one or more metric values to be optimized, which can be compared to other metric values.
Comparisons (and max, min) are based on which value is better, not which is larger.

The value can be:
- A single number (float/int)
- A dictionary in the format:
  {
    "metric_names": [
      {
        "metric_name": str,
        "lower_is_better": bool,
        "description": str,
        "data": [
            {"dataset_name": str, "final_value": float, "best_value": float},
            {"dataset_name": str, "final_value": float, "best_value": float},
            ...
        ]
      },
      ...
    ]
  }
##### `__post_init__(self)` (L144)
- Inputs: parameters from signature `__post_init__(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L150: {'line': 150, 'type': 'for', 'target': 'metric', 'iter': "self.value['metric_names']", 'body_len': 1, 'orelse_len': 0}
  - L151: {'line': 151, 'type': 'for', 'target': 'data_point', 'iter': "metric['data']", 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L145: IF `self.value is not None`; body=1 else=0
  - L146: IF `isinstance(self.value, dict)`; body=1 else=2
  - L148: IF `'metric_names' in self.value`; body=1 else=1
  - L152: IF `data_point['final_value'] is not None`; body=1 else=0
  - L156: IF `data_point['best_value'] is not None`; body=1 else=0
- Main call graph hints: `isinstance`, `float`, `self.value.items`
##### `__gt__(self, other)` (L171)
- Inputs: parameters from signature `__gt__(self, other)` plus referenced module/global/config state.
- Outputs / returns:
  - L189: `comp if should_maximize else not comp`
  - L173: `False`
  - L175: `True`
  - L184: `False`
- Conditions / decisions:
  - L172: IF `self.value is None`; body=1 else=0
  - L174: IF `other.value is None`; body=1 else=0
  - L183: IF `self_val == other_val`; body=1 else=0
- Main call graph hints: `self.get_mean_value`, `other.get_mean_value`, `self._should_maximize`, `type`
##### `_should_maximize(self)` (L191)
- Docstring: Determine if we should maximize based on the metric format
- Inputs: parameters from signature `_should_maximize(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L204: `bool(self.maximize)`
  - L202: `bool(self.maximize)`
  - L198: `not self.value['metric_names'][0]['lower_is_better']`
- Conditions / decisions:
  - L193: IF `isinstance(self.value, dict)`; body=2 else=0
  - L195: IF `'metric_names' in self.value`; body=1 else=0
- Exception handling:
  - L197: handlers=['Exception'] else=0 final=0
- Main call graph hints: `isinstance`, `bool`, `print`
##### `__str__(self)` (L206)
- Inputs: parameters from signature `__str__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L235: `f'Metric{opt_dir}{metric_name}({self.value_npsafe:.4f})'`
  - L231: `f'Metric{opt_dir}({self.name})[{values_str}](mean={mean_val:.4f})'`
  - L226: `'Metrics(' + '; '.join(parts) + ')'`
- Loops:
  - L211: {'line': 211, 'type': 'for', 'target': 'metric', 'iter': "self.value['metric_names']", 'body_len': 3, 'orelse_len': 0}
- Conditions / decisions:
  - L207: IF `isinstance(self.value, dict)`; body=5 else=0
  - L209: IF `'metric_names' in self.value`; body=3 else=0
- Exception handling:
  - L217: handlers=['Exception'] else=0 final=0
- Main call graph hints: `isinstance`, `Constant.join`, `np.mean`, `parts.append`, `self.value.items`, `self.value.values`, `print`
##### `__eq__(self, other)` (L237)
- Docstring: Compare equality of metric values
- Inputs: parameters from signature `__eq__(self, other)` plus referenced module/global/config state.
- Outputs / returns:
  - L257: `self.value == other.value`
  - L242: `True`
  - L244: `False`
  - L255: `False`
  - L250: `self.value == other.value`
  - L253: `self.value == other.value`
- Conditions / decisions:
  - L239: IF `not isinstance(other, MetricValue)`; body=1 else=0
  - L241: IF `self.value is None and other.value is None`; body=1 else=0
  - L243: IF `self.value is None or other.value is None`; body=1 else=0
  - L247: IF `isinstance(self.value, dict) and isinstance(other.value, dict)`; body=2 else=0
  - L249: IF `'metric_names' in self.value and 'metric_names' in other.value`; body=1 else=1
  - L252: IF `'metric_names' not in self.value and 'metric_names' not in other.value`; body=1 else=0
- Raises:
  - L240: `NotImplementedError`
- Main call graph hints: `isinstance`
##### `__repr__(self)` (L259)
- Docstring: Return string representation
- Inputs: parameters from signature `__repr__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L261: `str(self)`
- Main call graph hints: `str`
##### `value_npsafe(self)` (L264)
- Docstring: Return a NaN-safe version of the value
- Inputs: parameters from signature `value_npsafe(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L300: `self.value if self.value is not None else float('nan')`
  - L267: `float('nan')`
  - L296: `{k: v if v is not None else float('nan') for k, v in self.value.items()}`
  - L271: `{'metric_names': [{**metric, 'data': [{**data_point, 'final_value': data_point['final_value'] if data_point['final_value'] is not None else float('nan'), 'best_value': data_point['best_value'] if data_point['best_value'] is not None else float('nan')} for data_point in metric['data']]} for metric...`
- Conditions / decisions:
  - L266: IF `self.value is None`; body=1 else=0
  - L268: IF `isinstance(self.value, dict)`; body=2 else=0
  - L270: IF `'metric_names' in self.value`; body=1 else=0
- Main call graph hints: `isinstance`, `float`, `self.value.items`
##### `get_mean_value(self)` (L302)
- Docstring: Get the mean value across all metrics and datasets
- Inputs: parameters from signature `get_mean_value(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L324: `float(self.value)`
  - L305: `float('nan')`
  - L322: `float(np.mean(values)) if values else float('nan')`
  - L319: `float(np.mean(all_values)) if all_values else float('nan')`
- Loops:
  - L310: {'line': 310, 'type': 'for', 'target': 'metric', 'iter': "self.value['metric_names']", 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L304: IF `self.value is None`; body=1 else=0
  - L306: IF `isinstance(self.value, dict)`; body=3 else=0
  - L308: IF `'metric_names' in self.value`; body=3 else=0
  - L317: IF `values`; body=1 else=0
- Main call graph hints: `isinstance`, `float`, `self.value.values`, `np.mean`, `all_values.extend`
#### Class `WorstMetricValue` (L328)
- Bases: `MetricValue`
- Docstring: Represents an invalid metric value, e.g. when the agent creates a buggy solution.
Always compares worse than any valid metric value.
##### `__repr__(self)` (L336)
- Inputs: parameters from signature `__repr__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L337: `super().__repr__()`
- Main call graph hints: `super.__repr__`, `super`
##### `__str__(self)` (L339)
- Inputs: parameters from signature `__str__(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L340: `super().__str__()`
- Main call graph hints: `super.__str__`, `super`

### Functions

- None

---

## File: `ai_scientist/treesearch/utils/response.py`

**Lines:** 92  


### Imports / external dependencies

- `import json`
- `import re`
- `import black`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `wrap_code(code, lang)` (L7)
- Docstring: Wraps code with three backticks.
- Inputs: parameters from signature `wrap_code(code, lang)` plus referenced module/global/config state.
- Outputs / returns:
  - L9: `f'```{lang}\n{code}\n```'`
#### `is_valid_python_script(script)` (L12)
- Docstring: Check if a script is a valid Python script.
- Inputs: parameters from signature `is_valid_python_script(script)` plus referenced module/global/config state.
- Outputs / returns:
  - L16: `True`
  - L18: `False`
- Exception handling:
  - L14: handlers=['SyntaxError'] else=0 final=0
- Main call graph hints: `compile`
#### `extract_jsons(text)` (L21)
- Docstring: Extract all JSON objects from the text. Caveat: This function cannot handle nested JSON objects.
- Inputs: parameters from signature `extract_jsons(text)` plus referenced module/global/config state.
- Outputs / returns:
  - L38: `json_objects`
  - L36: `json_objects`
- Loops:
  - L25: {'line': 25, 'type': 'for', 'target': 'match', 'iter': 'matches', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L33: IF `len(json_objects) == 0 and (not text.endswith('}'))`; body=2 else=0
  - L35: IF `len(json_objects) > 0`; body=1 else=0
- Exception handling:
  - L26: handlers=['json.JSONDecodeError'] else=0 final=0
- I/O / network / subprocess side effects:
  - L27: `json.loads`
- Main call graph hints: `re.findall`, `extract_jsons`, `json.loads`, `json_objects.append`, `len`, `text.endswith`
#### `trim_long_string(string, threshold, k)` (L41)
- Inputs: parameters from signature `trim_long_string(string, threshold, k)` plus referenced module/global/config state.
- Outputs / returns:
  - L50: `f'{first_k_chars}\n ... [{truncated_len} characters truncated] ... \n{last_k_chars}'`
  - L52: `string`
- Conditions / decisions:
  - L43: IF `len(string) > threshold`; body=4 else=1
- Main call graph hints: `len`
#### `extract_code(text)` (L55)
- Docstring: Extract python code blocks from the text.
- Inputs: parameters from signature `extract_code(text)` plus referenced module/global/config state.
- Outputs / returns:
  - L76: `format_code('\n\n'.join(valid_code_blocks))`
- Loops:
  - L61: {'line': 61, 'type': 'for', 'target': 'match', 'iter': 'matches', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L66: IF `len(parsed_codes) == 0`; body=2 else=0
  - L68: IF `matches`; body=2 else=0
- Main call graph hints: `re.findall`, `format_code`, `parsed_codes.append`, `len`, `Constant.join`, `is_valid_python_script`
#### `extract_text_up_to_code(s)` (L79)
- Docstring: Extract (presumed) natural language text up to the start of the first code block.
- Inputs: parameters from signature `extract_text_up_to_code(s)` plus referenced module/global/config state.
- Outputs / returns:
  - L83: `s[:s.find('```')].strip()`
  - L82: `''`
- Conditions / decisions:
  - L81: IF `'```' not in s`; body=1 else=0
- Main call graph hints: `s[...].strip`, `s.find`
#### `format_code(code)` (L86)
- Docstring: Format Python code using Black.
- Inputs: parameters from signature `format_code(code)` plus referenced module/global/config state.
- Outputs / returns:
  - L89: `black.format_str(code, mode=black.FileMode())`
  - L91: `code`
- Exception handling:
  - L88: handlers=['black.parsing.InvalidInput'] else=0 final=0
- Main call graph hints: `black.format_str`, `black.FileMode`

---

## File: `ai_scientist/treesearch/utils/serialize.py`

**Lines:** 80  


### Imports / external dependencies

- `import copy`
- `import json`
- `from pathlib import Path`
- `from typing import Type, TypeVar`
- `import re`
- `import dataclasses_json`
- `from ..journal import Journal, Node`

### Module-level assignments / constants

- L39: `G = TypeVar("G", bound=dataclasses_json.DataClassJsonMixin)`

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `dumps_json(obj)` (L11)
- Docstring: Serialize dataclasses (such as Journals) to JSON.
- Inputs: parameters from signature `dumps_json(obj)` plus referenced module/global/config state.
- Outputs / returns:
  - L31: `json.dumps(obj_dict, separators=(',', ':'))`
- Loops:
  - L16: {'line': 16, 'type': 'for', 'target': 'n', 'iter': 'obj.nodes', 'body_len': 1, 'orelse_len': 0}
  - L21: {'line': 21, 'type': 'for', 'target': 'n', 'iter': 'obj.nodes', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L13: IF `isinstance(obj, Journal)`; body=4 else=0
  - L27: IF `isinstance(obj, Journal)`; body=2 else=0
  - L17: IF `n.parent is not None`; body=2 else=0
- I/O / network / subprocess side effects:
  - L31: `json.dumps`
- Main call graph hints: `isinstance`, `obj.to_dict`, `json.dumps`, `copy.deepcopy`, `set`
#### `dump_json(obj, path)` (L34)
- Inputs: parameters from signature `dump_json(obj, path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- I/O / network / subprocess side effects:
  - L35: `open`
- Main call graph hints: `open`, `f.write`, `dumps_json`
#### `loads_json(s, cls)` (L42)
- Docstring: Deserialize JSON to AIDE dataclasses.
- Inputs: parameters from signature `loads_json(s, cls)` plus referenced module/global/config state.
- Outputs / returns:
  - L52: `obj`
- Loops:
  - L49: {'line': 49, 'type': 'for', 'target': '(child_id, parent_id)', 'iter': "obj_dict['node2parent'].items()", 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L47: IF `isinstance(obj, Journal)`; body=2 else=0
- I/O / network / subprocess side effects:
  - L44: `json.loads`
- Main call graph hints: `json.loads`, `cls.from_dict`, `isinstance`, `obj_dict[...].items`, `id2nodes[...].__post_init__`
#### `load_json(path, cls)` (L55)
- Inputs: parameters from signature `load_json(path, cls)` plus referenced module/global/config state.
- Outputs / returns:
  - L57: `loads_json(f.read(), cls)`
- I/O / network / subprocess side effects:
  - L56: `open`
- Main call graph hints: `open`, `loads_json`, `f.read`
#### `parse_markdown_to_dict(content)` (L60)
- Docstring: Reads a file that contains lines of the form:

    "Key": "Value",
    "Another Key": "Another Value",
    ...

including possible multi-line values, and returns a Python dictionary.
- Inputs: parameters from signature `parse_markdown_to_dict(content)` plus referenced module/global/config state.
- Outputs / returns:
  - L79: `data_dict`
- Loops:
  - L76: {'line': 76, 'type': 'for', 'target': '(key, value)', 'iter': 'matches', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `re.findall`

---

## File: `ai_scientist/treesearch/utils/tree_export.py`

**Lines:** 485  

**Module docstring:** Export journal to HTML visualization of tree + code.


### Imports / external dependencies

- `import json`
- `import textwrap`
- `from pathlib import Path`
- `import numpy as np`
- `from igraph import Graph`
- `from ..journal import Journal`
- `from rich import print`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `get_edges(journal)` (L14)
- Inputs: parameters from signature `get_edges(journal)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Loops:
  - L15: {'line': 15, 'type': 'for', 'target': 'node', 'iter': 'journal', 'body_len': 1, 'orelse_len': 0}
  - L16: {'line': 16, 'type': 'for', 'target': 'c', 'iter': 'node.children', 'body_len': 1, 'orelse_len': 0}
#### `generate_layout(n_nodes, edges, layout_type)` (L20)
- Docstring: Generate visual layout of graph
- Inputs: parameters from signature `generate_layout(n_nodes, edges, layout_type)` plus referenced module/global/config state.
- Outputs / returns:
  - L31: `np.array(layout_coords)`
- Loops:
  - L29: {'line': 29, 'type': 'for', 'target': 'n', 'iter': 'range(n_nodes)', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `Graph.layout`, `max`, `range`, `np.array`, `layout_coords.append`, `Graph`
#### `normalize_layout(layout)` (L34)
- Docstring: Normalize layout to [0, 1]
- Inputs: parameters from signature `normalize_layout(layout)` plus referenced module/global/config state.
- Outputs / returns:
  - L40: `layout`
- Main call graph hints: `np.nan_to_num`, `layout.min`, `layout.max`
#### `get_completed_stages(log_dir)` (L43)
- Docstring: Determine completed stages by checking for the existence of stage directories
that contain evidence of completion (tree_data.json, tree_plot.html, or journal.json).

Returns:
    list: A list of stage names (e.g., ["Stage_1", "Stage_2"])
- Inputs: parameters from signature `get_completed_stages(log_dir)` plus referenced module/global/config state.
- Outputs / returns:
  - L73: `completed_stages`
- Loops:
  - L54: {'line': 54, 'type': 'for', 'target': 'stage_num', 'iter': 'range(1, 5)', 'body_len': 3, 'orelse_len': 0}
  - L63: {'line': 63, 'type': 'for', 'target': 'stage_dir', 'iter': 'matching_dirs', 'body_len': 4, 'orelse_len': 0}
- Conditions / decisions:
  - L68: IF `has_tree_data or has_tree_plot or has_journal`; body=2 else=0
- Main call graph hints: `range`, `BinOp.exists`, `log_dir.iterdir`, `completed_stages.append`, `d.is_dir`, `d.name.startswith`
#### `cfg_to_tree_struct(cfg, jou, out_path)` (L76)
- Inputs: parameters from signature `cfg_to_tree_struct(cfg, jou, out_path)` plus referenced module/global/config state.
- Outputs / returns:
  - L359: `tmp`
- Loops:
  - L94: {'line': 94, 'type': 'for', 'target': 'n', 'iter': 'jou', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L355: IF `out_path`; body=2 else=0
  - L96: IF `n.metric`; body=1 else=1
  - L98: IF `isinstance(n.metric.value, dict) and 'metric_names' in n.metric.value`; body=1 else=1
- Exception handling:
  - L79: handlers=['Exception'] else=0 final=0
  - L84: handlers=['Exception'] else=0 final=0
  - L129: handlers=['Exception'] else=0 final=0
  - L135: handlers=['Exception'] else=0 final=0
  - L141: handlers=['Exception'] else=0 final=0
  - L150: handlers=['Exception'] else=0 final=0
  - L156: handlers=['Exception'] else=0 final=0
  - L166: handlers=['Exception'] else=0 final=0
  - L175: handlers=['Exception'] else=0 final=0
  - L181: handlers=['Exception'] else=0 final=0
  - L187: handlers=['Exception'] else=0 final=0
  - L193: handlers=['Exception'] else=0 final=0
  - L199: handlers=['Exception'] else=0 final=0
  - L205: handlers=['Exception'] else=0 final=0
  - L211: handlers=['Exception'] else=0 final=0
  - L217: handlers=['Exception'] else=0 final=0
  - L223: handlers=['Exception'] else=0 final=0
  - L229: handlers=['Exception'] else=0 final=0
  - L245: handlers=['Exception'] else=0 final=0
  - L251: handlers=['Exception'] else=0 final=0
  - L263: handlers=['Exception'] else=0 final=0
  - L271: handlers=['Exception'] else=0 final=0
  - L277: handlers=['Exception'] else=0 final=0
  - L283: handlers=['Exception'] else=0 final=0
  - L289: handlers=['Exception'] else=0 final=0
  - L295: handlers=['Exception'] else=0 final=0
  - L301: handlers=['Exception'] else=0 final=0
  - L307: handlers=['Exception'] else=0 final=0
  - L319: handlers=['Exception'] else=0 final=0
  - L325: handlers=['Exception'] else=0 final=0
  - L336: handlers=['Exception'] else=0 final=0
  - L342: handlers=['Exception'] else=0 final=0
  - L348: handlers=['Exception'] else=0 final=0
- Raises:
  - L83: ``
  - L88: ``
  - L133: ``
  - L139: ``
  - L148: ``
  - L154: ``
  - L164: ``
  - L173: ``
  - L179: ``
  - L185: ``
  - L191: ``
  - L197: ``
  - L203: ``
  - L209: ``
  - L215: ``
  - L221: ``
  - L227: ``
  - L243: ``
  - L249: ``
  - L261: ``
  - L269: ``
  - L275: ``
  - L281: ``
  - L287: ``
  - L293: ``
  - L299: ``
  - L305: ``
  - L317: ``
  - L323: ``
  - L334: ``
- Main call graph hints: `list`, `print`, `jou.get_best_node`, `get_edges`, `generate_layout`, `normalize_layout`, `is_best_node.append`, `layout.tolist`, `get_completed_stages`, `len`, `metrics.append`, `textwrap.fill`, `isinstance`, `str`
#### `generate_html(tree_graph_str)` (L362)
- Inputs: parameters from signature `generate_html(tree_graph_str)` plus referenced module/global/config state.
- Outputs / returns:
  - L373: `html`
- I/O / network / subprocess side effects:
  - L365: `open`
  - L369: `open`
- Main call graph hints: `open`, `f.read`, `js.replace`, `html.replace`, `Path`
#### `generate(cfg, jou, out_path)` (L376)
- Inputs: parameters from signature `generate(cfg, jou, out_path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Exception handling:
  - L378: handlers=['Exception'] else=0 final=0
  - L385: handlers=['Exception'] else=0 final=0
  - L393: handlers=['Exception'] else=0 final=0
  - L398: handlers=['Exception'] else=0 final=0
  - L407: handlers=['Exception'] else=0 final=0
- Raises:
  - L382: ``
  - L397: ``
  - L402: ``
- I/O / network / subprocess side effects:
  - L394: `json.dumps`
  - L403: `open`
  - L388: `open`
  - L389: `json.dump`
- Main call graph hints: `print`, `cfg_to_tree_struct`, `json.dumps`, `generate_html`, `open`, `f.write`, `create_unified_viz`, `json.dump`
#### `create_unified_viz(cfg, current_stage_viz_path)` (L414)
- Docstring: Create a unified visualization that shows all completed stages in a tabbed interface.
This will be placed in the main log directory.
- Inputs: parameters from signature `create_unified_viz(cfg, current_stage_viz_path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Conditions / decisions:
  - L424: IF `current_stage.startswith('stage_')`; body=2 else=0
  - L427: IF `len(parts) >= 2 and parts[1].isdigit()`; body=2 else=0
  - L449: IF `current_stage_data_path.exists()`; body=1 else=1
- Exception handling:
  - L447: handlers=['Exception'] else=0 final=0
- I/O / network / subprocess side effects:
  - L437: `open`
  - L440: `open`
  - L475: `json.dumps`
  - L481: `open`
  - L450: `open`
  - L451: `json.load`
- Main call graph hints: `current_stage.startswith`, `get_completed_stages`, `js.replace`, `html.replace`, `print`, `current_stage.split`, `open`, `f.read`, `current_stage_data_path.exists`, `json.dumps`, `f.write`, `parts[...].isdigit`, `Path`, `len`, `json.load`

---

## File: `ai_scientist/utils/token_tracker.py`

**Lines:** 223  


### Imports / external dependencies

- `from functools import wraps`
- `from typing import Dict, Optional, List`
- `import tiktoken`
- `from collections import defaultdict`
- `import asyncio`
- `from datetime import datetime`
- `import logging`

### Module-level assignments / constants

- L140: `token_tracker = TokenTracker()`

### Prompt-like assignments in this file

- None detected

### Classes

#### Class `TokenTracker` (L10)
- Bases: `object`
##### `__init__(self)` (L11)
- Docstring: Token counts for prompt, completion, reasoning, and cached.
Reasoning tokens are included in completion tokens.
Cached tokens are included in prompt tokens.
Also tracks prompts, responses, and timestamps.
We assume we get these from the LLM response, and we don't count
the tokens by ourselves.
- Inputs: parameters from signature `__init__(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `defaultdict`
##### `add_tokens(self, model, prompt_tokens, completion_tokens, reasoning_tokens, cached_tokens)` (L62)
- Inputs: parameters from signature `add_tokens(self, model, prompt_tokens, completion_tokens, reasoning_tokens, cached_tokens)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
##### `add_interaction(self, model, system_message, prompt, response, timestamp)` (L75)
- Docstring: Record a single interaction with the model.
- Inputs: parameters from signature `add_interaction(self, model, system_message, prompt, response, timestamp)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `self.interactions[...].append`
##### `get_interactions(self, model)` (L93)
- Docstring: Get all interactions, optionally filtered by model.
- Inputs: parameters from signature `get_interactions(self, model)` plus referenced module/global/config state.
- Outputs / returns:
  - L97: `dict(self.interactions)`
  - L96: `{model: self.interactions[model]}`
- Conditions / decisions:
  - L95: IF `model`; body=1 else=0
- Main call graph hints: `dict`
##### `reset(self)` (L99)
- Docstring: Reset all token counts and interactions.
- Inputs: parameters from signature `reset(self)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `defaultdict`
##### `calculate_cost(self, model)` (L107)
- Docstring: Calculate the cost for a specific model based on token usage.
- Inputs: parameters from signature `calculate_cost(self, model)` plus referenced module/global/config state.
- Outputs / returns:
  - L125: `prompt_cost + cached_cost + completion_cost`
  - L111: `0.0`
- Conditions / decisions:
  - L109: IF `model not in self.MODEL_PRICES`; body=2 else=0
  - L117: IF `'cached' in prices`; body=2 else=2
- Main call graph hints: `logging.warning`
##### `get_summary(self)` (L127)
- Docstring: Get summary of token usage and costs for all models.
- Inputs: parameters from signature `get_summary(self)` plus referenced module/global/config state.
- Outputs / returns:
  - L136: `summary`
- Loops:
  - L131: {'line': 131, 'type': 'for', 'target': '(model, tokens)', 'iter': 'self.token_counts.items()', 'body_len': 1, 'orelse_len': 0}
- Main call graph hints: `self.token_counts.items`, `tokens.copy`, `self.calculate_cost`

### Functions

#### `track_token_usage(func)` (L143)
- Inputs: parameters from signature `track_token_usage(func)` plus referenced module/global/config state.
- Outputs / returns:
  - L222: `async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper`
  - L182: `result`
  - L220: `result`
- Conditions / decisions:
  - L148: IF `not prompt and (not system_message)`; body=1 else=0
  - L160: IF `hasattr(result, 'usage') and result.usage.completion_tokens_details is not None`; body=2 else=0
  - L188: IF `not prompt and (not system_message)`; body=1 else=0
  - L198: IF `hasattr(result, 'usage') and result.usage.completion_tokens_details is not None`; body=2 else=0
- Raises:
  - L149: `ValueError("Either 'prompt' or 'system_message' must be provided for token tracking")`
  - L189: `ValueError("Either 'prompt' or 'system_message' must be provided for token tracking")`
- Main call graph hints: `wraps`, `kwargs.get`, `logging.info`, `func`, `asyncio.iscoroutinefunction`, `ValueError`, `hasattr`, `token_tracker.add_tokens`, `token_tracker.add_interaction`

---

## File: `ai_scientist/vlm.py`

**Lines:** 349  


### Imports / external dependencies

- `import base64`
- `from typing import Any`
- `import re`
- `import json`
- `import backoff`
- `import openai`
- `import os`
- `from PIL import Image`
- `from ai_scientist.utils.token_tracker import track_token_usage`

### Module-level assignments / constants

- L11: `MAX_NUM_TOKENS = 4096`
- L13: `AVAILABLE_VLMS = [ "gpt-4o-2024-05-13", "gpt-4o-2024-08-06", "gpt-4o-2024-11-20", "gpt-4o-mini-2024-07-18", "o3-mini", # Ollama models # llama4 "ollama/llama4:16x17b", # mistral "ollama/mistral-small3.2:24b", # qwen "ollama/qwen2.5vl:32b", "ollama/z-uo/qwen2.5vl_tools:32b", ]`

### Prompt-like assignments in this file

- None detected

### Classes

- None

### Functions

#### `encode_image_to_base64(image_path)` (L35)
- Docstring: Convert an image to base64 string.
- Inputs: parameters from signature `encode_image_to_base64(image_path)` plus referenced module/global/config state.
- Outputs / returns:
  - L49: `base64.b64encode(image_bytes).decode('utf-8')`
- Conditions / decisions:
  - L39: IF `img.mode == 'RGBA'`; body=1 else=0
- I/O / network / subprocess side effects:
  - L37: `Image.open`
- Main call graph hints: `base64.b64encode.decode`, `Image.open`, `io.BytesIO`, `img.save`, `buffer.getvalue`, `img.convert`, `base64.b64encode`
#### `make_llm_call(client, model, temperature, system_message, prompt)` (L53)
- Inputs: parameters from signature `make_llm_call(client, model, temperature, system_message, prompt)` plus referenced module/global/config state.
- Outputs / returns:
  - L55: `client.chat.completions.create(model=model.replace('ollama/', ''), messages=[{'role': 'system', 'content': system_message}, *prompt], temperature=temperature, max_tokens=MAX_NUM_TOKENS, n=1, stop=None, seed=0)`
  - L68: `client.chat.completions.create(model=model, messages=[{'role': 'system', 'content': system_message}, *prompt], temperature=temperature, max_tokens=MAX_NUM_TOKENS, n=1, stop=None, seed=0)`
  - L81: `client.chat.completions.create(model=model, messages=[{'role': 'user', 'content': system_message}, *prompt], temperature=1, n=1, seed=0)`
- Conditions / decisions:
  - L54: IF `model.startswith('ollama/')`; body=1 else=1
  - L67: IF `'gpt' in model`; body=1 else=1
  - L80: IF `'o1' in model or 'o3' in model`; body=1 else=1
- Raises:
  - L92: `ValueError(f'Model {model} not supported.')`
- LLM/VLM calls:
  - L55: `client.chat.completions.create`
  - L68: `client.chat.completions.create`
  - L81: `client.chat.completions.create`
- Main call graph hints: `model.startswith`, `client.chat.completions.create`, `model.replace`, `ValueError`
#### `make_vlm_call(client, model, temperature, system_message, prompt)` (L96)
- Inputs: parameters from signature `make_vlm_call(client, model, temperature, system_message, prompt)` plus referenced module/global/config state.
- Outputs / returns:
  - L98: `client.chat.completions.create(model=model.replace('ollama/', ''), messages=[{'role': 'system', 'content': system_message}, *prompt], temperature=temperature, max_tokens=MAX_NUM_TOKENS)`
  - L108: `client.chat.completions.create(model=model, messages=[{'role': 'system', 'content': system_message}, *prompt], temperature=temperature, max_tokens=MAX_NUM_TOKENS)`
- Conditions / decisions:
  - L97: IF `model.startswith('ollama/')`; body=1 else=1
  - L107: IF `'gpt' in model`; body=1 else=1
- Raises:
  - L118: `ValueError(f'Model {model} not supported.')`
- LLM/VLM calls:
  - L98: `client.chat.completions.create`
  - L108: `client.chat.completions.create`
- Main call graph hints: `model.startswith`, `client.chat.completions.create`, `ValueError`, `model.replace`
#### `prepare_vlm_prompt(msg, image_paths, max_images)` (L121)
- Inputs: parameters from signature `prepare_vlm_prompt(msg, image_paths, max_images)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
#### `get_response_from_vlm(msg, image_paths, client, model, system_message, print_debug, msg_history, temperature, max_images)` (L132)
- Docstring: Get response from vision-language model.
- Inputs: parameters from signature `get_response_from_vlm(msg, image_paths, client, model, system_message, print_debug, msg_history, temperature, max_images)` plus referenced module/global/config state.
- Outputs / returns:
  - L192: `(content, new_msg_history)`
- Loops:
  - L156: {'line': 156, 'type': 'for', 'target': 'image_path', 'iter': 'image_paths[:max_images]', 'body_len': 2, 'orelse_len': 0}
  - L186: {'line': 186, 'type': 'for', 'target': '(j, msg)', 'iter': 'enumerate(new_msg_history)', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L144: IF `msg_history is None`; body=1 else=0
  - L147: IF `model in AVAILABLE_VLMS`; body=7 else=1
  - L183: IF `print_debug`; body=6 else=0
  - L149: IF `isinstance(image_paths, str)`; body=1 else=0
- Raises:
  - L181: `ValueError(f'Model {model} not supported.')`
- Main call graph hints: `backoff.on_exception`, `isinstance`, `make_vlm_call`, `ValueError`, `print`, `enumerate`, `encode_image_to_base64`, `content.append`
#### `create_client(model)` (L195)
- Docstring: Create client for vision-language model.
- Inputs: parameters from signature `create_client(model)` plus referenced module/global/config state.
- Outputs / returns:
  - L205: `(openai.OpenAI(), model)`
  - L208: `(openai.OpenAI(api_key=os.environ.get('OLLAMA_API_KEY', ''), base_url='http://localhost:11434/v1'), model)`
- Conditions / decisions:
  - L197: IF `model in ['gpt-4o-2024-05-13', 'gpt-4o-2024-08-06', 'gpt-4o-2024-11-20', 'gpt-4o-mini-2024-07-18', 'o3-mini']`; body=2 else=1
  - L206: IF `model.startswith('ollama/')`; body=2 else=1
- Raises:
  - L213: `ValueError(f'Model {model} not supported.')`
- I/O / network / subprocess side effects:
  - L205: `openai.OpenAI`
  - L208: `openai.OpenAI`
- Main call graph hints: `print`, `model.startswith`, `openai.OpenAI`, `ValueError`, `os.environ.get`
#### `extract_json_between_markers(llm_output)` (L216)
- Inputs: parameters from signature `extract_json_between_markers(llm_output)` plus referenced module/global/config state.
- Outputs / returns:
  - L241: `None`
  - L230: `parsed_json`
  - L237: `parsed_json`
- Loops:
  - L226: {'line': 226, 'type': 'for', 'target': 'json_string', 'iter': 'matches', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L221: IF `not matches`; body=2 else=0
- Exception handling:
  - L228: handlers=['json.JSONDecodeError'] else=0 final=0
  - L233: handlers=['json.JSONDecodeError'] else=0 final=0
- I/O / network / subprocess side effects:
  - L229: `json.loads`
  - L236: `json.loads`
- Main call graph hints: `re.findall`, `json_string.strip`, `json.loads`, `re.sub`
#### `get_batch_responses_from_vlm(msg, image_paths, client, model, system_message, print_debug, msg_history, temperature, n_responses, max_images)` (L251)
- Docstring: Get multiple responses from vision-language model for the same input.

Args:
    msg: Text message to send
    image_paths: Path(s) to image file(s)
    client: OpenAI client instance
    model: Name of model to use
    system_message: System prompt
    print_debug: Whether to print debug info
    msg_history: Previous message history
    temperature: Sampling temperature
    n_responses: Number of responses to generate

Returns:
    Tuple of (list of response strings, list of message histories)
- Inputs: parameters from signature `get_batch_responses_from_vlm(msg, image_paths, client, model, system_message, print_debug, msg_history, temperature, n_responses, max_images)` plus referenced module/global/config state.
- Outputs / returns:
  - L348: `(contents, new_msg_histories)`
- Loops:
  - L289: {'line': 289, 'type': 'for', 'target': 'image_path', 'iter': 'image_paths[:max_images]', 'body_len': 2, 'orelse_len': 0}
  - L342: {'line': 342, 'type': 'for', 'target': '(j, msg)', 'iter': 'enumerate(new_msg_histories[0])', 'body_len': 1, 'orelse_len': 0}
- Conditions / decisions:
  - L279: IF `msg_history is None`; body=1 else=0
  - L282: IF `model in AVAILABLE_VLMS`; body=7 else=1
  - L338: IF `print_debug`; body=6 else=0
  - L284: IF `isinstance(image_paths, str)`; body=1 else=0
  - L304: IF `model.startswith('ollama/')`; body=1 else=1
- Raises:
  - L336: `ValueError(f'Model {model} not supported.')`
- LLM/VLM calls:
  - L305: `client.chat.completions.create`
  - L318: `client.chat.completions.create`
- Main call graph hints: `backoff.on_exception`, `isinstance`, `model.startswith`, `ValueError`, `print`, `enumerate`, `encode_image_to_base64`, `content.append`, `client.chat.completions.create`, `model.replace`

---

## File: `launch_scientist_bfts.py`

**Lines:** 370  


### Imports / external dependencies

- `import os.path as osp`
- `import json`
- `import argparse`
- `import shutil`
- `import torch`
- `import os`
- `import re`
- `import sys`
- `from datetime import datetime`
- `from ai_scientist.llm import create_client`
- `from contextlib import contextmanager`
- `from ai_scientist.treesearch.perform_experiments_bfts_with_agentmanager import ( perform_experiments_bfts, )`
- `from ai_scientist.treesearch.bfts_utils import ( idea_to_markdown, edit_bfts_config_file, )`
- `from ai_scientist.perform_plotting import aggregate_plots`
- `from ai_scientist.perform_writeup import perform_writeup`
- `from ai_scientist.perform_icbinb_writeup import ( perform_writeup as perform_icbinb_writeup, gather_citations, )`
- `from ai_scientist.perform_llm_review import perform_review, load_paper`
- `from ai_scientist.perform_vlm_review import perform_imgs_cap_ref_review`
- `from ai_scientist.utils.token_tracker import token_tracker`

### Module-level assignments / constants

- None

### Prompt-like assignments in this file

- None detected

### Top-level decisions / loops / try blocks

- IF L182: `__name__ == '__main__'`; body=44 else=0

### Classes

- None

### Functions

#### `print_time()` (L31)
- Inputs: parameters from signature `print_time()` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Main call graph hints: `print`, `datetime.now.strftime`, `datetime.now`
#### `save_token_tracker(idea_dir)` (L35)
- Inputs: parameters from signature `save_token_tracker(idea_dir)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- I/O / network / subprocess side effects:
  - L36: `open`
  - L37: `json.dump`
  - L38: `open`
  - L39: `json.dump`
- Main call graph hints: `open`, `json.dump`, `osp.join`, `token_tracker.get_summary`, `token_tracker.get_interactions`
#### `parse_arguments()` (L42)
- Inputs: parameters from signature `parse_arguments()` plus referenced module/global/config state.
- Outputs / returns:
  - L131: `parser.parse_args()`
- Main call graph hints: `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`
#### `get_available_gpus(gpu_ids)` (L134)
- Inputs: parameters from signature `get_available_gpus(gpu_ids)` plus referenced module/global/config state.
- Outputs / returns:
  - L137: `list(range(torch.cuda.device_count()))`
  - L136: `[int(gpu_id) for gpu_id in gpu_ids.split(',')]`
- Conditions / decisions:
  - L135: IF `gpu_ids is not None`; body=1 else=0
- Main call graph hints: `list`, `range`, `int`, `torch.cuda.device_count`, `gpu_ids.split`
#### `find_pdf_path_for_review(idea_dir)` (L140)
- Inputs: parameters from signature `find_pdf_path_for_review(idea_dir)` plus referenced module/global/config state.
- Outputs / returns:
  - L164: `pdf_path`
- Loops:
  - L152: {'line': 152, 'type': 'for', 'target': 'f', 'iter': 'reflection_pdfs', 'body_len': 2, 'orelse_len': 0}
- Conditions / decisions:
  - L143: IF `reflection_pdfs`; body=2 else=0
  - L146: IF `final_pdfs`; body=1 else=3
  - L157: IF `reflection_nums`; body=2 else=1
  - L154: IF `match`; body=1 else=0
- Main call graph hints: `os.listdir`, `f.endswith`, `osp.join`, `re.search`, `max`, `f.lower`, `reflection_nums.append`, `int`, `match.group`
#### `redirect_stdout_stderr_to_file(log_file_path)` (L168)
- Inputs: parameters from signature `redirect_stdout_stderr_to_file(log_file_path)` plus referenced module/global/config state.
- Outputs / returns: no explicit return (returns `None` unless side effects).
- Exception handling:
  - L174: handlers=[] else=0 final=3
- I/O / network / subprocess side effects:
  - L171: `open`
- Main call graph hints: `open`, `log.close`