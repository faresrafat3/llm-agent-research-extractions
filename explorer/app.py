"""SOTA Streamlit Explorer for LLM Agent Research Extractions.

Dynamically parses the 20+ heterogeneous research directories and presents 
them in a unified, highly visual Dashboard (Prompts, Mermaid Graphs, Logic Flow).
"""
import os
import json
import streamlit as st
from pathlib import Path
from loguru import logger

# Set wide layout for enterprise dashboard feel
st.set_page_config(page_title="LLM Agent Architectures", page_icon="🧠", layout="wide")

PROJECTS_DIR = Path("projects")

@st.cache_data
def load_all_projects():
    """Scans the directory tree and builds a unified index of all research data."""
    projects = []
    if not PROJECTS_DIR.exists():
        return projects
        
    for d in PROJECTS_DIR.iterdir():
        if d.is_dir() and not d.name.startswith("."):
            project_data = {
                "id": d.name,
                "name": d.name.replace("-", " ").title(),
                "json_logic": None,
                "mermaid_graph": None,
                "prompts": None,
                "research_summary": None
            }
            
            # Read JSON Inventory safely
            json_file = d / "python_logic_inventory.json"
            if json_file.exists():
                try:
                    with open(json_file, "r", encoding="utf-8") as f:
                        project_data["json_logic"] = json.load(f)
                except Exception:
                    pass

            # Read Mermaid Graph
            mmd_file = d / "graph_english.mmd"
            if not mmd_file.exists():
                mmd_file = d / "MASTER_GRAPH_ENGLISH.mmd"
            if mmd_file.exists():
                with open(mmd_file, "r", encoding="utf-8") as f:
                    project_data["mermaid_graph"] = f.read()

            # Read Prompts
            prompts_file = d / "prompts_complete.md"
            if prompts_file.exists():
                with open(prompts_file, "r", encoding="utf-8") as f:
                    project_data["prompts"] = f.read()
                    
            # Read Summary
            summary_file = d / "research_summary.md"
            if summary_file.exists():
                with open(summary_file, "r", encoding="utf-8") as f:
                    project_data["research_summary"] = f.read()

            projects.append(project_data)
            
    # Sort alphabetically by name
    return sorted(projects, key=lambda x: x["name"])

def render_mermaid(code: str):
    """Embeds Mermaid.js graph dynamically into Streamlit."""
    import base64
    # Create a simple iframe holding the mermaid graph to prevent streamlit rendering issues
    b64 = base64.b64encode(code.encode("utf-8")).decode("utf-8")
    html = f"""
    <div class="mermaid">
        {code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
    </script>
    """
    st.components.v1.html(html, height=600, scrolling=True)

def main():
    st.title("🧠 LLM Agent Architectures (Research Extractions)")
    st.markdown("Explore the raw Logic, Flow, and Prompts extracted from 20+ SOTA AI Papers.")
    
    projects = load_all_projects()
    
    if not projects:
        st.warning("No projects found in the 'projects/' directory.")
        return

    # Sidebar Navigation
    st.sidebar.header("🔍 Research Directory")
    selected_project_name = st.sidebar.selectbox("Select a System to Analyze:", [p["name"] for p in projects])
    
    selected_project = next(p for p in projects if p["name"] == selected_project_name)
    
    # Main Content Area
    st.header(selected_project["name"])
    
    # Top Level Metrics / Overview
    if selected_project["json_logic"]:
        data = selected_project["json_logic"]
        if isinstance(data, dict):
            st.caption(f"**Source:** {data.get('arxiv', 'N/A')} | **Repo:** {data.get('repo', 'N/A')}")
        else:
            st.caption(f"**Data Structure:** Array of {len(data)} logical segments.")
    
    tabs = st.tabs(["📊 Architecture (Graph)", "📜 Prompts", "⚙️ Logic Inventory", "📚 Summary"])
    
    with tabs[0]:
        st.subheader("Architectural Flowchart")
        if selected_project["mermaid_graph"]:
            # Streamlit native mermaid support via markdown component (works in newer versions)
            st.markdown(f"```mermaid\n{selected_project['mermaid_graph']}\n```")
        else:
            st.info("No Mermaid Graph (.mmd) available for this project.")
            
    with tabs[1]:
        st.subheader("Extracted System Prompts")
        if selected_project["prompts"]:
            st.markdown(selected_project["prompts"])
        else:
            st.info("No Prompts Markdown file available.")
            
    with tabs[2]:
        st.subheader("Raw Python/Logic Inventory")
        if selected_project["json_logic"]:
            st.json(selected_project["json_logic"], expanded=False)
        else:
            st.info("No JSON Inventory available.")
            
    with tabs[3]:
        st.subheader("Executive Research Summary")
        if selected_project["research_summary"]:
            st.markdown(selected_project["research_summary"])
        else:
            st.info("No Research Summary available.")

if __name__ == "__main__":
    main()
