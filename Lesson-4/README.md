# Lesson 4 – AI Agent with Memory (Stateful Agent)

In this lesson, I built my first **AI agent that has memory**.

This means the AI does not just answer and forget.  
It can **remember what it did before** and store it in a file.

This is one of the most important concepts in **Agentic AI**.

---

## What is happening in simple words?

Normally, AI works like this:

> You ask → AI answers → everything is forgotten

In this project, the AI works like this:

> You ask → AI decides a command → runs it → saves result in memory

So now the AI has a **brain + memory**.

---

## Files in this folder

### 1. memory_agent.py

This is the main program.

It does 5 things:

1. Asks the AI what Linux command to run
2. Checks if the command is safe
3. Runs the command on the system
4. Gets the output
5. Saves everything to memory

So the AI can:
- Think
- Act
- Observe
- Remember

Just like a real agent.

---

### 2. agent_memory.json

This file is the **memory of the AI**.

Every time the agent runs, it saves:

- Time
- What it was asked
- What command it chose
- What output it got

Example:

```json
{
  "time": "2026-02-07 10:53:46",
  "agent_command": "pwd",
  "output": "/c/Users/perve/OneDrive/Pictures/Agentic AI for Devops screenshots"
}
```

This means:
The AI ran the command pwd and remembered the result.

----

__Why is this important?__
Because this is how real AI agents work in companies.

This same concept is used in:

- DevOps AI bots
- Cloud automation
- Support chatbots
- Security AI systems
- AutoGPT, CrewAI, LangGraph

## Without memory:
- AI is just a chatbot.
## With memory:
- AI becomes an agent.

---

What I learned in this lesson
---

## From this lesson, I learned:

- How AI can use system tools
- How to add safety rules
- How to store AI memory
- How real Agentic AI systems are built

This is the foundation of LLMOps and Agentic Engineering.
---

