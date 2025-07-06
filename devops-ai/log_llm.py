import subprocess
from log_fetcher import fetch_recent_logs

def get_logs():
    """
    Fetch recent system logs for analysis.
    """
    return fetch_recent_logs(minutes=5)

def analyze_logs_with_llm(logs):
    """
    Analyze logs using a local LLM (LLaMA3 via Ollama) to detect root cause of high CPU.
    """
    prompt = f"""
You are a DevOps AI assistant. Analyze the following system logs and identify the most likely root cause of high CPU usage.
Be concise and only respond with the root cause.

Logs:
{logs}
"""
    print(" Sending prompt to Ollama...\n")
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            text=True,
            check=True
        )
        print(" LLM Response:")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f" Error analyzing logs: {e.stderr}"
    except Exception as e:
        return f" Unexpected error: {e}"

#  Optional: Run test directly
if __name__ == "__main__":
    logs = get_logs()
    print(" Logs Preview:\n", logs[:1000])  # Print partial logs for readability
    print("\n AI Analysis:\n")
    print(analyze_logs_with_llm(logs))