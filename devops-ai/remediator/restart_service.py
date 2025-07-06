import subprocess

def restart_service(service_name):
    print(f" Restarting service: {service_name}...")
    try:
        subprocess.run(["sudo", "systemctl", "restart", service_name], check=True)
        print(f" Service '{service_name}' restarted successfully.")
        return f"{service_name}:  Restarted successfully."
    except subprocess.CalledProcessError as e:
        print(f" Failed to restart '{service_name}'. Error:\n{e}")
        return f"{service_name}:  Failed to restart.\nError: {e}"