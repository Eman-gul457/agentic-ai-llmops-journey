# Lesson 6 – Tools, Tool Calling & MCP (Model Context Protocol)

## Why AI Agents Need Tools
LLMs are good at generating text but cannot reliably:
- Do exact math
- Access real-time data
- Call APIs or databases
- Run real code

Tools turn LLMs from "text generators" into real-world problem solvers.

---

## Tool Calling
Tool calling allows an LLM to:
- See available tools (APIs, databases, code)
- Decide which tool to use
- Request the tool execution
- Use the tool result to generate final answers

This enables agents to interact with the real world.

---

## Traditional vs Embedded Tool Calling

### Traditional Tool Calling
- App sends tools + prompt to LLM
- LLM suggests which tool to call
- App executes tool
- Result is sent back to LLM

Limitation: LLM may hallucinate or suggest wrong tool calls.

### Embedded Tool Calling
- A library/framework sits between app and LLM
- Library manages tool definitions and execution
- Automatically retries and validates tool calls

Benefit: More reliable, less hallucination, safer execution.

---

## AI-Powered SQL Agents
AI SQL agents allow users to query databases using natural language.

Flow:
User → LLM → SQL Query → Database → Raw Data → LLM → Final Answer

Capabilities:
- Understand database schemas
- Auto-fix failed queries
- Support multi-step queries

Limitations:
- May misinterpret complex questions
- Requires testing and validation

---

## MCP (Model Context Protocol)
MCP is an open standard to connect AI agents with real data sources.

### Core Components:
- MCP Host: The main app (chat app, IDE, website)
- MCP Client: Communication layer
- MCP Server: Connects to databases, APIs, files, or code

### Why MCP Matters:
- Standard way to connect tools
- Plug-and-play architecture
- Scalable multi-agent systems
- Future-proof agent infrastructure

---

## Key Takeaway
Tools + Tool Calling + MCP are what transform LLMs into real intelligent agents.
Without tools, AI can talk.
With tools, AI can act.
