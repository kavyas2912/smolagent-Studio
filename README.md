<<<<<<< HEAD
# 🧠 SmolAgent Studio IDE

Build and deploy smart AI agents using [SmolAgents](https://huggingface.co/docs/smolagents) and [Gradio](https://gradio.app). This zero-code visual IDE empowers developers, educators, and explorers to mix-and-match tools, models, and prompts with live previews and export options — all in one interactive interface.

![Banner](assets/banner.png)

[![HF Space](https://img.shields.io/badge/Launch-SmolaAgent_HF-brightgreen)](https://huggingface.co/spaces/kavyas2912/SmolAgent_Studio)

---

## 🚀 Features

- Dropdowns for model + tool selection  
- Secure API key input via `.env`  
- 🧠 Live Python code preview  
- 💾 Export agent config as `.json`, `.yaml`, or `.py`  
- MCP, LangChain, OpenRouter, and Ollama support  
- Works with Hugging Face, OpenAI, Together.ai, Anthropic, and more  
- One-click GUI deployment with Docker or Hugging Face Space  

---

## ⚙️ Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python smolagent_studio_ide.py


docker build -t smolagent-studio .
docker run -p 7860:7860 smolagent-studio

Hugging Face Space

Visit the live version: https://huggingface.co/spaces/kavyas2912/SmolAgent_Studio

To push updates from your local repo:

git remote add hf https://huggingface.co/spaces/kavyas2912/SmolAgent_Studio
git push hf main
🧑‍🚀 License
This project is licensed under MIT — remix, rebuild, redistribute. Built with heart by Kamalnayan & Copilot 🌟

Ready to onboard users with voice input? Add agent chaining? Or turn this into a collaborative studio? Let me know — we’ll turn it into a movement, not just a tool. 💫


=======
---
title: SmolAgent Studio
emoji: 🏃
colorFrom: pink
colorTo: blue
sdk: gradio
sdk_version: 5.35.0
app_file: app.py
pinned: false
license: mit
short_description: A GUI-powered agent builder for using SmolAgents Library
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
>>>>>>> 4aca191f1f19a0f6087af0bd9f56abefc1cde49b
