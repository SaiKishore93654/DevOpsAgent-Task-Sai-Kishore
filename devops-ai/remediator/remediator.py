import subprocess

# List of critical services to restart during auto-remediation
CRITICAL_SERVICES = ["grafana-server", "prometheus", "loki", "docker"]

def restart_service(service_name):
    print(f" Restarting service: {service_name}...")
    try:
        subprocess.run(["sudo", "systemctl", "restart", service_name], check=True)
        print(f" Service '{service_name}' restarted successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f" Failed to restart '{service_name}'. Error:\n{e}")
        return False

def auto_remediate():
    report = []
    for service in CRITICAL_SERVICES:
        success = restart_service(service)
        status = "Success" if success else "Failed"
        report.append(f"{service}: {status}")
    
    return "\n".join(report)

# Optional: run as standalone script to test
if __name__ == "__main__":
    print(" Running remediation test...")
    result = auto_remediate()
    print("\n Remediation Summary:")
    print(result)