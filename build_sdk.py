"""SOTA SDK Generator.
Parses the incredible logic inventories from the 20 extracted projects
and auto-generates a typed Python SDK to allow immediate execution.
"""
import os
import json
import re
from loguru import logger

PROJECTS_DIR = "projects"
OUTPUT_DIR = "llm_agent_prompts/systems"

def generate_sdk():
    logger.info("🛠️ Building SOTA Prompt SDK from Extractions...")
    
    init_imports = []
    
    for project_folder in os.listdir(PROJECTS_DIR):
        json_path = os.path.join(PROJECTS_DIR, project_folder, "python_logic_inventory.json")
        if not os.path.isfile(json_path):
            continue
            
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                logger.warning(f"Failed to parse {json_path}")
                continue
                
        if isinstance(data, list):
            logger.warning(f"Skipping {json_path} as it contains a list instead of a dict mapping.")
            continue
                
        # Clean project name to make it a valid Python Class name
        project_name = data.get("project", project_folder.replace("-", "_").title())
        class_name = re.sub(r'[^a-zA-Z0-9]', '', project_name)
        file_name = f"{class_name.lower()}.py"
        
        # We look for prompts in the JSON
        prompts = data.get("prompts", {})
        if not prompts:
            # Some older extractions might not have standard format, we skip or handle later
            continue
            
        py_code = f"\"\"\"Auto-generated SDK for {project_name} ({data.get('arxiv', 'No ArXiv')}).\"\"\"\n\n"
        py_code += "from typing import Dict, Any\n\n"
        py_code += f"class {class_name}:\n"
        py_code += f"    \"\"\"Prompts extracted from: {data.get('repo', 'N/A')}\"\"\"\n\n"
        
        for prompt_name, prompt_data in prompts.items():
            desc = prompt_data.get("description", "").replace('"', "'").replace('\n', ' ')
            
            # Identify required variables (naive but effective for extraction)
            inputs = prompt_data.get("input", "")
            
            py_code += f"    @staticmethod\n"
            py_code += f"    def get_{prompt_name.lower()}_prompt() -> str:\n"
            py_code += f"        \"\"\"{inputs}\\nReturns:\\n    {prompt_data.get('output', 'prompt string')}\"\"\"\n"
            py_code += f"        return \"\"\"{desc}\"\"\"\n\n"
            
        out_path = os.path.join(OUTPUT_DIR, file_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(py_code)
            
        logger.success(f"Generated SDK module for: {class_name}")
        init_imports.append(f"from .{class_name.lower()} import {class_name}")
        
    # Write init file
    with open(os.path.join(OUTPUT_DIR, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("\n".join(init_imports))
        
    with open("llm_agent_prompts/__init__.py", "w", encoding="utf-8") as f:
        f.write("from .systems import *")

if __name__ == "__main__":
    generate_sdk()
