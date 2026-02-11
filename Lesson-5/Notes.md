# Lesson 5 – Learning Notes: Workflows vs Agents – AI Agents: Types & When to Use Them


## What I thought before
Before this lesson, I thought:
AI = chatbot

I believed AI only generates text, images, or code.

---

## What I understand now

There are three main paradigms:

### 1. Single LLM Features
These are simple one-shot systems.

Examples:
- Summarization
- Translation
- Sentiment analysis

Characteristics:
- No memory
- No planning
- No multi-step logic

They are fast and cheap, but not intelligent.

---

### 2. Structured Workflows
These systems use LLMs inside fixed pipelines.

Example:
Insurance processing:
OCR → Extract → Validate → Store

Characteristics:
- Deterministic
- Easy to monitor
- Good for enterprise systems

Problem:
They cannot adapt or reason in new situations.

---

### 3. Autonomous Agents (Agentic AI)
These systems can:
- Plan tasks
- Use tools
- Learn from feedback
- Change strategy

They follow a loop:
Perceive → Decide → Act → Learn

This makes them:
- Context-aware
- Goal-driven
- Proactive

---

## Important Insight from Videos

Generative AI is reactive:
It waits for humans.

Agentic AI is proactive:
It acts like a junior employee.

---

## Real-world truth

Modern AI systems are not purely agents or workflows.

They are hybrid systems:
- Workflows provide safety and control
- Agents provide reasoning and flexibility

This is how real companies design AI today.

---

## Personal Reflection

This lesson changed how I see AI.

Now I understand:
The future of AI is not just chat.
The future of AI is systems that can think, plan, and act.

---

## Types of AI Agents

### 1. Simple Reflex Agent
- Uses simple if–then rules.
- No memory, no learning.
- Reacts only to current input.
- Example: Thermostat.

### 2. Model-Based Reflex Agent
- Has internal memory (state).
- Tracks how the environment changes.
- Makes better decisions using past info.
- Example: Robot vacuum.

### 3. Goal-Based Agent
- Works based on defined goals.
- Simulates future outcomes.
- Chooses actions that reach the goal.
- Example: Self-driving car.

### 4. Utility-Based Agent
- Chooses best possible outcome.
- Uses utility score (preference/value).
- Optimizes multiple factors.
- Example: Delivery drone.

### 5. Learning Agent
- Learns from experience.
- Improves using feedback (rewards).
- Most powerful but slow and data-heavy.
- Example: Chess AI.

---

## When to Use AI Agents

### AI System Spectrum
- **Simple AI features:** one-shot tasks (summarization, translation)
- **Workflows:** structured multi-step processes
- **Agents:** complex, adaptive reasoning

### 4-Question Framework
1. Is the task ambiguous? → Use agent  
2. Is the value worth the cost? → Agents are expensive  
3. Does the agent meet key skills? → Test first  
4. What if it makes mistakes? → Use only if risk is manageable  

### When NOT to Use Agents
- High-volume low-value tasks
- Real-time systems
- Zero-error systems (medical, security)
- Highly regulated environments

### Best Practices
- Start simple
- Use human-in-the-loop
- Add logging and monitoring
- Deploy in phases

