# Lesson 3 – Secure DevOps AI Agent (Reason → Act) 🤖🔐

In this lesson, I built a secure AI agent that can:

- Think like a DevOps engineer  
- Suggest a Linux command  
- Pass through a security filter  
- Execute the command automatically  

This is my first real Agentic AI system where the AI does not just talk — it takes actions.

---

## What Is Happening in This Project? 

Normally:
- AI gives answers.
- Humans do the work.

In this project:
- AI decides what command to run.
- System checks if it’s safe.
- If safe → it runs automatically.
- If unsafe → it is blocked.

This is how future AI systems will manage servers without humans.

---
Tech Stack Used
---
- Python
- Ollama (local LLM)
- Phi-3 model
- Subprocess execution
---

## How the File `safe_agent.py` Works (Simple English)

The program follows 4 steps:

### 1. AI Thinks
We ask the AI:
"You are a DevOps AI agent. Suggest a safe Linux command."

The AI replies with something like:
- df -h  
- uname -a  
- whoami  

---

### 2. Clean the AI Output
Sometimes the AI adds formatting like:

```bash
df -h
```
The code cleans this so only the real command remains:
df -h
This is important because in real systems, AI output is not always clean.

---
#3. Security Layer (Guardrails)
---

Only these commands are allowed:

- ls
- pwd
- whoami
- uname
- df
- free
If the AI suggests anything dangerous:

- It is blocked
- Not executed

This is called AI Guardrails / AI Security.

---
4.Agent Takes Action
---
If the command is safe:

- The system runs it
- Shows the real output from the computer

This creates a full Reason → Act loop.

---
Example Runs (Real Screenshots)
---
These are real executions from my system.
<img width="1086" height="246" alt="LLMOps-6(lesson-3)" src="https://github.com/user-attachments/assets/a6d213f9-6e3c-4e33-b03f-5effe3356014" />

----
<img width="1110" height="358" alt="LLMOps-7(lesson-3)" src="https://github.com/user-attachments/assets/69fc2809-231e-48e7-a976-f615930fa139" />

---
Why This Lesson Is Important
---
This small project demonstrates real industry concepts:
- AI agent design
- Output sanitization
- Security guardrails
- Autonomous execution
- DevOps automation
This same pattern is used in:
- AutoGPT
- CrewAI
- LangGraph
- Self-healing cloud systems
- AI DevOps tools

---
