def remediate():
    subprocess.run(['docker', 'restart', 'my_container'])
    # Or: subprocess.run(['systemctl', 'restart', 'my_service'])