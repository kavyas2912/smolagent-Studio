import gradio as gr
import os
import json
import yaml
from pathlib import Path
from smolagents import (
    CodeAgent, ToolCallingAgent, ManagedAgent,
    InferenceClientModel, TransformersModel, LiteLLMModel,
    OllamaModel, OpenAIModel, AnthropicModel,
    TogetherModel, OpenRouterModel,
    WebSearchTool, PythonTool, FileTool, ImageTool,
    TerminalTool, FinalAnswerTool, UserInputTool,
    LangChainTool, HFModelDownloadsTool
)

# 🎯 Tool and Model Mappings
TOOL_MAP = {
    "WebSearchTool": (WebSearchTool, "🔍 Search the internet"),
    "PythonTool": (PythonTool, "🐍 Execute Python code"),
    "FileTool": (FileTool, "📂 Read/write local files"),
    "ImageTool": (ImageTool, "🖼️ Handle image input/output"),
    "TerminalTool": (TerminalTool, "💻 Run shell commands"),
    "FinalAnswerTool": (FinalAnswerTool, "✅ Finalize agent response"),
    "UserInputTool": (UserInputTool, "👤 Interactive user input"),
    "LangChainTool": (LangChainTool, "🔗 Wrap LangChain tools"),
    "HFModelDownloadsTool": (HFModelDownloadsTool, "📊 Hugging Face stats")
}

MODEL_MAP = {
    "Hugging Face API": (InferenceClientModel, "Use hosted HF models"),
    "Transformers (local)": (TransformersModel, "Run local models"),
    "LiteLLM": (LiteLLMModel, "Connect to LiteLLM"),
    "OpenAI": (OpenAIModel, "Use OpenAI GPT models"),
    "Anthropic": (AnthropicModel, "Access Claude via Anthropic"),
    "Ollama": (OllamaModel, "Use local Ollama models"),
    "Together.ai": (TogetherModel, "Use Together-hosted models"),
    "OpenRouter": (OpenRouterModel, "Universal model router")
}

AGENT_TYPES = {
    "CodeAgent": "Generates and runs Python code",
    "ToolCallingAgent": "Uses structured tool calls",
    "ManagedAgent": "Manages tool routing and sub-agents"
}

# ✏️ Helper: Generate Agent Code Preview
def generate_code_preview(model_choice, tools_selected, agent_type, prompt):
    model_cls_name = model_choice.replace(" ", "")
    imports = f"from smolagents import {agent_type}, {model_cls_name}, {', '.join(tools_selected)}\nimport os"
    setup = f'os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_token_here"'
    model = f'model = {model_cls_name}(provider="{model_choice}", token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))'
    tools = f'tools = [{", ".join(tool + "()" for tool in tools_selected)}]'
    agent = f'agent = {agent_type}(tools=tools, model=model, stream_outputs=True)'
    run = f'result = agent.run("{prompt}")\nprint(result)'
    return "\n".join([imports, setup, model, tools, agent, run])

# 🚀 Main Execution Logic
def run_agent(model_choice, token, tools_selected, agent_type, prompt):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = token
    model_cls = MODEL_MAP[model_choice][0]
    model = model_cls(provider=model_choice, token=token)
    tools = [TOOL_MAP[t][0]() for t in tools_selected]

    if agent_type == "CodeAgent":
        agent = CodeAgent(tools=tools, model=model, stream_outputs=True)
    elif agent_type == "ToolCallingAgent":
        agent = ToolCallingAgent(tools=tools, model=model)
    else:
        agent = ManagedAgent(tools=tools, model=model)

    try:
        result = agent.run(prompt)
    except Exception as e:
        result = f"⚠️ Agent Error: {e}"

    code = generate_code_preview(model_choice, tools_selected, agent_type, prompt)
    return result, code

# 💾 Export Agent Setup
def export_agent_config(model_choice, tools_selected, agent_type, prompt, format):
    config = {
        "model": model_choice,
        "tools": tools_selected,
        "agent_type": agent_type,
        "prompt": prompt
    }
    path = Path(f"agent_config.{format}")
    if format == "yaml":
        path.write_text(yaml.dump(config, sort_keys=False))
    elif format == "py":
        code = generate_code_preview(model_choice, tools_selected, agent_type, prompt)
        path.write_text(code)
    else:
        path.write_text(json.dumps(config, indent=2))
    return f"✅ Exported to {path}"

# 🧪 Gradio Interface
with gr.Blocks(title="SmolAgent Studio IDE") as demo:
    gr.Markdown("# 🛠️ SmolAgent Studio")
    gr.Markdown("Build and deploy smart agents visually. Select tools, models, and prompts — with live code preview and export.")

    with gr.Row():
        model_dropdown = gr.Dropdown(list(MODEL_MAP.keys()), label="Model Provider", info="Choose LLM backend")
        token_input = gr.Textbox(label="API Token", type="password", placeholder="Paste your token securely")

    with gr.Row():
        tool_selector = gr.CheckboxGroup(list(TOOL_MAP.keys()), label="Tools", info="Select tools for your agent")
        agent_dropdown = gr.Dropdown(list(AGENT_TYPES.keys()), label="Agent Type", info="Select agent logic")

    prompt_box = gr.Textbox(label="Prompt", lines=4, placeholder="Ask your agent something...")

    code_view = gr.Code(label="Generated Python Code", language="python")
    output_box = gr.Textbox(label="Agent Output")

    with gr.Row():
        run_button = gr.Button("🚀 Run Agent")
        format_dropdown = gr.Dropdown(["json", "yaml", "py"], label="Export Format", value="json")
        export_button = gr.Button("💾 Export Config")

    run_button.click(
        fn=run_agent,
        inputs=[model_dropdown, token_input, tool_selector, agent_dropdown, prompt_box],
        outputs=[output_box, code_view]
    )

    export_button.click(
        fn=export_agent_config,
        inputs=[model_dropdown, tool_selector, agent_dropdown, prompt_box, format_dropdown],
        outputs=gr.Textbox(label="Export Status")
    )

demo.launch()
