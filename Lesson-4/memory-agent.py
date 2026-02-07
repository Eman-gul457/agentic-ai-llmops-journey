# memory_agent.py
import ollama
import subprocess
import json
import re
from datetime import datetime

# Only allow very safe basic commands
ALLOWED_COMMANDS = [
    "ls",
    "pwd",
    "whoami",
    "uname",
    "df -h"
]

MEMORY_FILE = "agent_memory.json"

def clean_command(text):
    """
    Remove markdown/code formatting from LLM output.
    """
    text = text.strip()
    text = re.sub(r"```(bash|shell)?", "", text)
    text = text.replace("```", "")
    text = text.replace("`", "")
    return text.strip()

def is_safe(command):
    """
    Check if command starts with allowed commands.
    """
    for allowed in ALLOWED_COMMANDS:
        if command.startswith(allowed):
            return True
    return False

def run_command(cmd):
    """
    Run shell command and return output.
    """
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result
    except Exception as e:
        return str(e)

def load_memory():
    """
    Load previous memory from file.
    """
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(memory):
    """
    Save memory to file.
    """
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# Load previous memory
memory = load_memory()

# Prompt for the agent
prompt = """
You are a DevOps AI agent.
Suggest ONE safe system command.
Only use: ls, pwd, whoami, uname, df -h
No markdown. Only the command.
"""

# Ask the local LLM
response = ollama.chat(
    model="phi3",
    messages=[{"role": "user", "content": prompt}]
)

raw = response["message"]["content"]
command = clean_command(raw)

print("Agent suggested:", command)

if is_safe(command):
    print("Command is safe. Executing...")
    output = run_command(command)
else:
    print("Command blocked for safety!")
    output = "Not executed"

print("Output:\n", output)

# Save interaction to memory
memory_entry = {
    "time": datetime.now().isoformat(),
    "agent_command": command,
    "output": output
}

memory.append(memory_entry)
save_memory(memory)

print("\nSaved to memory:", MEMORY_FILE)
