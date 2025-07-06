import subprocess
from datetime import datetime, timedelta

def fetch_recent_logs(minutes=5):
    """
    Fetch system logs from the last 'minutes' using journalctl,
    with fallback to /var/log/syslog (last 200 lines).
    """
    since_time = (datetime.now() - timedelta(minutes=minutes)).isoformat()

    try:
        # Try journalctl first (systemd-based systems)
        logs = subprocess.check_output(
            ['journalctl', '--since', since_time, '--no-pager'],
            stderr=subprocess.DEVNULL
        ).decode('utf-8')
        return logs if logs else "No logs from journalctl in the past few minutes."

    except Exception:
        # Fallback to tailing syslog for non-systemd or permission issues
        try:
            with open('/var/log/syslog', 'r') as f:
                lines = f.readlines()
                recent_lines = lines[-200:]  # get last 200 lines
                return ''.join(recent_lines)
        except Exception as e:
            return f" Error fetching logs: {e}"

#  Optional test when running standalone
if __name__ == "__main__":
    logs = fetch_recent_logs()
    print("Recent Logs:\n")
    print(logs[:3000]) 