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
                
        # If the root is a list, we skip for now to maintain stability, or parse if it has a specific structure
        if isinstance(data, list):
            # In some of your repos, the list contains the dicts directly
            if len(data) > 0 and isinstance(data[0], dict):
                data = data[0]
            else:
                logger.warning(f"Skipping {json_path} as it contains an unparseable list.")
                continue
                
        project_name = data.get("project", project_folder.replace("-", "_").title())
        # Safety fallback if project_name isn't string
        if not isinstance(project_name, str): project_name = str(project_name)
        
        class_name = re.sub(r'[^a-zA-Z0-9]', '', project_name)
        if not class_name: class_name = "AgentSystem"
        file_name = f"{class_name.lower()}.py"
        
        prompts = data.get("prompts", {})
        if not prompts:
            continue
            
        py_code = f'"""Auto-generated SDK for {project_name}."""\n\n'
        py_code += "from typing import Dict, Any\n\n"
        py_code += f"class {class_name}:\n"
        py_code += f"    \"\"\"Prompts extracted from: {data.get('repo', 'N/A')}\"\"\"\n\n"
        
        prompt_items = prompts.items() if isinstance(prompts, dict) else enumerate(prompts)
        
        for prompt_key, prompt_data in prompt_items:
            if isinstance(prompt_data, str):
                continue
                
            prompt_name = prompt_key if isinstance(prompt_key, str) else prompt_data.get("name", f"prompt_{prompt_key}")
            
            # Clean up names for python methods
            safe_method_name = re.sub(r'[^a-zA-Z0-9]', '_', prompt_name).lower()
            
            desc = prompt_data.get("description", prompt_data.get("prompt", ""))
            if not isinstance(desc, str): desc = str(desc)
            desc = desc.replace('"', "'").replace('\n', ' ')
            
            inputs = prompt_data.get("input", prompt_data.get("inputs", ""))
            outputs = prompt_data.get("output", prompt_data.get("outputs", "prompt string"))
            
            py_code += f"    @staticmethod\n"
            py_code += f"    def get_{safe_method_name}_prompt() -> str:\n"
            py_code += f"        \"\"\"Inputs: {inputs}\n        Returns: {outputs}\"\"\"\n"
            py_code += f"        return \"\"\"{desc}\"\"\"\n\n"
            
        out_path = os.path.join(OUTPUT_DIR, file_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(py_code)
            
        logger.success(f"Generated SDK module for: {class_name}")
        init_imports.append(f"from .{file_name.replace('.py', '')} import {class_name}")
        
    with open(os.path.join(OUTPUT_DIR, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("\n".join(init_imports))
        
    with open("llm_agent_prompts/__init__.py", "w", encoding="utf-8") as f:
        f.write("from .systems import *")

if __name__ == "__main__":
    generate_sdk()
