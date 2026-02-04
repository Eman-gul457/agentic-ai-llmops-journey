import ollama
import subprocess
import re

# Only these commands are allowed for safety
ALLOWED_COMMANDS = ["ls", "pwd", "whoami", "uname", "df", "free"]

def clean_command(text):
    """
    Cleans LLM output by removing markdown and extra symbols,
    while keeping the actual command.
    """
    text = text.strip()
    # Remove markdown code fences like ```bash or ```shell
    text = re.sub(r"```(bash|shell)?", "", text)
    text = text.replace("```", "")
    text = text.replace("`", "")
    return text.strip()

def is_safe(command):
    """
    Check if the command starts with one of the allowed commands.
    """
    for allowed in ALLOWED_COMMANDS:
        if command.startswith(allowed):
            return True
    return False

def run_command(cmd):
    """
    Executes a shell command safely.
    """
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result
    except Exception as e:
        return str(e)

# Prompt for the AI agent

prompt = """
You are a DevOps AI agent.
Check system kernel and OS information.
Only use: ls, pwd, whoami, uname, df, free.
Only reply with the command.
No markdown.
"""



# Ask the local LLM
response = ollama.chat(
    model="phi3",
    messages=[{"role": "user", "content": prompt}]
)

raw = response["message"]["content"]
command = clean_command(raw)

print("Raw agent output:", raw)
print("Parsed command:", command)

if is_safe(command):
    print("Command is safe. Executing...")
    output = run_command(command)
else:
    print("Command blocked for safety!")
    output = "Not executed"

print("Output:\n", output)
