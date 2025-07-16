#tools/tool_definitions.py

TOOL_TIPS = {
    "WebSearchTool": "🔍 Search the web using DuckDuckGo, Brave, or SerpAPI.",
    "VisitWebpageTool": "🌐 Fetch and convert a webpage into readable markdown.",
    "PythonTool": "🐍 Execute Python code securely in a sandboxed environment.",
    "PythonInterpreterTool": "🧪 A stateful Python interpreter with retained execution context.",
    "TerminalTool": "💻 Run shell commands. Use with caution.",
    "FileTool": "🗂️ Read, write, and manipulate local files for your agent.",
    "ImageTool": "🖼️ Handle image input/output — caption, generate, or analyze.",
    "FinalAnswerTool": "✅ Marks the final agent response to stop processing.",
    "UserInputTool": "👤 Allows dynamic user prompts mid-task.",
    "LangChainTool": "🔗 Wrap LangChain tools like SerpAPI, SQL Toolkit, Wolfram Alpha.",
    "HFModelDownloadsTool": "📊 Fetch most downloaded HF models for a given task.",
    "ApiWebSearchTool": "🛰️ Search APIs like Bing or Google for fresh results.",
    "Tool.from_hub()": "📦 Load external tools from Hugging Face Hub repos.",
    "Tool.from_space()": "🧪 Import Gradio Spaces as tools.",
    "Tool.from_mcp()": "🧠 Load tools dynamically from registered MCP servers.",
    "Tool.from_langchain()": "🧬 Convert LangChain tool definitions into SmolAgent-compatible formats.",
    "Tool.from_gradio()": "🎛️ Wrap Gradio interfaces as callable tools.",
    "ToolCollection.from_mcp()": "🌐 Fetch and register toolsets from Glama, Smithery, and other MCP providers."
}


✅ This file gives you tooltip metadata for dynamic dropdowns, tool help panels, and config-driven rendering. You can link this file to model_config.json, or expand to include categories, icons, or flags like streaming=True.