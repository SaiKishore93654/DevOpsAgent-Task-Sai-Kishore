import time
from cpu_monitor import get_cpu_usage
from log_llm import analyze_logs_with_llm, get_logs
from remediator.remediator import auto_remediate
from slack_notifi import send_slack_notification

CPU_THRESHOLD = 10
SUSTAINED_DURATION = 10  # seconds
CHECK_INTERVAL = 10       # seconds

def main():
    sustained_high_cpu_time = 0

    while True:
        cpu_usage = get_cpu_usage()
        print(f" CPU Usage: {cpu_usage:.2f}%")

        if cpu_usage > CPU_THRESHOLD:
            sustained_high_cpu_time += CHECK_INTERVAL
            print(f" High CPU duration: {sustained_high_cpu_time}s")
        else:
            sustained_high_cpu_time = 0

        # Trigger remediation if sustained high CPU
        if sustained_high_cpu_time >= SUSTAINED_DURATION:
            print("\n Sustained High CPU Detected!\n")
            logs = get_logs()
            analysis = analyze_logs_with_llm(logs)
            print(" AI Analysis:\n", analysis)

            print(" Attempting Auto Remediation...\n")
            remediation_report = auto_remediate()

            #  Post-remediation CPU check
            post_remediation_cpu = get_cpu_usage()
            print(f" CPU Usage after remediation: {post_remediation_cpu:.2f}%")

            # Optional: Log remediation effectiveness
            if post_remediation_cpu < CPU_THRESHOLD:
                print(" CPU usage normalized after remediation.")
            else:
                print(" CPU still high after remediation.")

            # Send Slack Notification
            message = f""" *Sustained High CPU Alert* 
*CPU Usage (Before)*: {cpu_usage:.2f}%
*Duration*: {SUSTAINED_DURATION} seconds

*AI Analysis*:
{analysis}

*Auto-Remediation Report*:
{remediation_report}

*CPU Usage (After Remediation)*: {post_remediation_cpu:.2f}%
"""
            send_slack_notification(message)

            # Reset timer after remediation
            sustained_high_cpu_time = 0

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()