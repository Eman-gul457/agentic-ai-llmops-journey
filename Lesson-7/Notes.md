# Lesson 7 – Multi-Agent & Agentic AI

## Why Multi-Agent Systems Matter
Single LLMs struggle with complex workflows:
- Context overload when juggling multiple tasks
- Role confusion (writing vs analysis)
- Hard to debug errors
- “Jack-of-all-trades, master of none”

Multi-agent systems split tasks among **specialized LLM agents**:
- Research, analysis, writing, critique
- Customer support automation
- Legal document review
- Modular, scalable, accurate

---

## Communication & Coordination
Multi-agent systems rely on clear communication:
- **Sequential (Pipeline):** Output passes downstream from one agent to another  
- **Parallel with Aggregation:** Multiple agents work simultaneously; results combined by a compiler agent  
- **Interactive Dialogue:** Agents exchange messages to clarify and refine information  

### Protocols & Frameworks
- **MCP:** Standard for LLM-to-tool interaction  
- **ACP:** Standard for agent-to-agent communication  
- **Frameworks:** LangGraph, AutoGen, CrewAI, BeeAI

---

## Retrieval Augmented Generation (RAG)
- LLM retrieves relevant information from **vector databases** before answering
- Keeps responses **accurate, sourced, and up-to-date**
- **Agentic RAG:** LLM decides which database to query, can adapt response type (text, chart, code)

---

## AI Assistants vs AI Agents
- **Assistants:** “Do it yourself” – follow user instructions  
- **Agents:** “Do it for you” – autonomous, can make decisions, trigger workflows

---

## Orchestrator Agents
- Manage multiple agents and tasks
- Route work to specialized agents
- Ensure workflows are **coordinated and efficient**
- Benefits:
  - Increased efficiency
  - Better experience (de-siloing tools)
  - Scalable workflows

---

## Governance for Agentic AI
Autonomy = increased risk  
Risks: misinformation, errors, security vulnerabilities  

**Governance Layers:**
1. Technical safeguards (model, orchestration, tool layers)  
2. Process controls (permissions, auditability, monitoring)  
3. Accountability (human and organizational responsibility)

---

## Key Takeaway
Multi-agent systems + RAG + agentic AI + orchestrators = **smarter, reliable, autonomous AI**  
Autonomy requires governance. Human oversight is critical for safe, responsible deployment.
