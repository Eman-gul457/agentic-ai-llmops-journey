🥗 NourishBot – AI-Powered Food Analysis & Recipe Assistant
---
📌 Project Overview 
---
NourishBot is an AI-powered application that helps users:
- Analyze food images to understand nutritional values
- Get healthy recipe suggestions based on dietary preferences

The user uploads a food image, selects what they want to do (recipe ideas or nutrition analysis), and the system intelligently responds using modern AI models.
👉 This project was completed as a guided learning project, focusing on understanding AI systems, workflows, and DevOps concepts used in real-world applications.

---
🎯 Why This Project Matters
---
This project demonstrates how modern applications are built using:
- Artificial Intelligence (AI)
- Multi-agent systems
- Structured workflows
- Clear separation of responsibilities (a key DevOps principle)

Even though AI is the core feature, the architecture and organization strongly reflect Modern DevOps practices.

---
🧠 How the Application Works 
---
1. The user uploads a food image

2. The system looks at the image

3. Different AI “workers” (agents) do specific jobs:
  - One identifies food items
  - One checks dietary rules
  - One analyzes nutrition
  - One suggests recipes
4. The result is shown in a clean web interface
Each “worker” only does one job, which makes the system easy to manage and scale.

---
File Structure:
---
```bash
Smart-Nutritional-App-Crew/
│
├── config/
│   ├── agents.yaml               # Configuration for agents
│   └── tasks.yaml                # Configuration for tasks
│
├── src/
│   ├── crew.py                   # Crew definitions (agents, tasks, workflows)
│   ├── tools.py                  # Tool definitions for ingredient detection, filtering, etc.
│   └── main.py                   # Main script for running the application
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```
---
Setup Instructions
---
Clone the repository:
---
```bash
git clone https://github.com/HaileyTQuach/Smart-Nutritional-App.git
cd Smart-Nutritional-App
```

---
Create and activate a virtual environment:
---
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
---
Install the required dependencies:
---
```bash
pip install -r requirements.txt
```
---
Create a .env file in the root directory with the following keys:
---
```bash
 WATSONX_API_KEY=your_watsonx_api_key
 WATSONX_URL=your_watsonx_url
 WATSONX_PROJECT_ID=your_watsonx_project_id
```
Usage
---
Run the Application
---
You can run the application using the following commands:
1.For recipe suggestions
---
```bash
python main.py <image_path> <dietary_restrictions> recipe
```

Example:
---
```bash
python main.py food.jpg vegan recipe
```
---
2.For food analysis
---
```bash
python main.py <image_path> analysis
```

Example:
---
```bash
python main.py food.jpg analysis
```

3.For training (future functionality - TODO)
---
```bash
python main.py train <n_iterations> <output_filename> <image_path> <dietary_restrictions> <workflow_type>
```
🔧 How This Project Relates to Modern DevOps
---
Even though this is an AI application, it strongly reflects Modern DevOps thinking:

✅ DevOps Concepts Used
---
DevOps Concept	          How It Appears in This Project
Modular design	          Separate files for logic, tools, agents
Automation	              AI agents execute tasks automatically
Scalability	              New agents/tasks can be added easily
Maintainability	          Clear structure and responsibilities
Workflow orchestration	  Tasks run in defined sequences
Reproducibility	          Same behavior every time

This is how real production systems are designed.

---
📘 Learning Disclaimer (Important)
---
⚠️ This project was built as a guided learning project.
- The goal was learning architecture, AI workflows, and DevOps concepts
- Code structure and best practices were studied and implemented
- Enhancements such as documentation, explanations, and project presentation were done independently

This project is used as a portfolio learning artifact, not a commercial product.

---
🧪 How to Run the Project (Simple)
---
```bash
python app.py
```
<img width="718" height="191" alt="output" src="https://github.com/user-attachments/assets/144a2f50-c49d-4b32-8602-e025c503f588" />


Then open:
```bash
http://localhost:5000
```
<img width="1217" height="630" alt="Landing page" src="https://github.com/user-attachments/assets/d4fbb13a-71d8-4100-8fd0-58dce4730706" />

---
<img width="1170" height="591" alt="recipe of pizza" src="https://github.com/user-attachments/assets/f2e310cc-0f12-4e75-b4b7-1fa1fe66849f" />

---
<img width="1277" height="645" alt="Analysis of pizza" src="https://github.com/user-attachments/assets/89857d5d-2e39-4b91-834f-fa86fcf4743f" />

---
Upload an image and try both workflows.

---
🚀 What I Learned
---
- How AI systems are organized in production
- How multi-agent workflows work
- How DevOps principles apply beyond servers
- How to build readable, maintainable projects
- How AI + DevOps work together in modern apps

---

🏁 Final Note
---
This project helped me understand how modern DevOps is not only about servers, but also about:
- System design
- Workflow automation
- Scalability
- Clean architecture

---
