# DevOpsAgent-Task-Sai-Kishore



This project is an intelligent agent that monitors **CPU usage**, detects **anomalies**, performs **root cause analysis** using an LLM (Ollama or OpenAI), and automatically takes **remediation actions**. It can also send alerts to **Slack**.

---

##  Features

-  Real-time **CPU monitoring**
-  AI-based log analysis (via **Ollama** or **OpenAI GPT**)
- **Automated remediation** (e.g., stopping high-CPU processes)
-  Logs retrieved from system (`/var/log/syslog`)
-  **Slack alerting** support
-  Easy to run on **local, EC2, or Docker**

---

##  Architecture

[Prometheus or psutil] → [Python Monitor] → [Log Fetcher] → [LLM Analysis (Ollama/OpenAI)] → [Remediation Action] → [Slack Notification]



---

##  Prerequisites

- Python 3.8+
- Linux-based system (Ubuntu/Debian preferred)
- `Ollama` installed **OR** OpenAI API Key
- Optional: Slack webhook

---

##  Installation

### 1. Clone the Repository


git clone https://github.com/your-username/ai-devops-agent.git
cd ai-devops-agent
2. Install Dependencies


pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash

pip install psutil requests
 Configuration
Edit the values in orchestration.py:

python

CPU_THRESHOLD = 80  # % CPU to trigger analysis
SUSTAINED_DURATION = 120  # seconds of sustained high CPU
SERVICE_TO_RESTART = "yes"  # or replace with your actual service name
LOG_FILE_PATH = "/var/log/syslog"
USE_OLLAMA = True  # Set to False to use OpenAI
Then set any required environment variables:

bash

# If using OpenAI GPT
export OPENAI_API_KEY=your_openai_key

# (Optional) For Slack alerts
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
 Usage
Start the Agent
bash

python orchestration.py
Simulate High CPU (for testing)
bash

yes > /dev/null
Agent will:

Detect high CPU

Fetch last 100 lines from syslog

Analyze logs using LLM

Kill the high CPU process (e.g., yes)

Send Slack alert if enabled

 LLM Modes
Mode	Description
Ollama	Runs locally with models like mistral, llama3
OpenAI	Uses GPT-3.5/GPT-4 via API (needs OPENAI_API_KEY)

If both fail, you'll get a fallback error message.


 Sample Output

 CPU Usage: 91.2%
 High CPU sustained. Initiating analysis...
 Analysis:
The "yes" command is running in a tight loop with no sleep, consuming 100% CPU.

 Terminated high CPU process: yes

 Alert sent to Slack.

