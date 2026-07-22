.PHONY: help install run

help:
	@echo "🧠 LLM Agent Architectures Explorer"
	@echo "-----------------------------------"
	@echo "Commands:"
	@echo "  make install  - Install the required dependencies"
	@echo "  make run      - Launch the Interactive Streamlit Explorer"

install:
	pip install --upgrade pip
	pip install -e .

run:
	streamlit run explorer/app.py
