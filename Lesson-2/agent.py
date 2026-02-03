import ollama
import subprocess

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result
    except Exception as e:
        return str(e)

prompt = """
You are an SRE agent.
Check system disk usage.
Only reply with one Linux command.
and also show output
"""

response = ollama.chat(
    model="phi3",
    messages=[{"role": "user", "content": prompt}]
)

command = response["message"]["content"]
print("Agent decided to run:", command)

output = run_command(command)
print("Command output:\n", output)
