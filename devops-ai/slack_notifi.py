import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env variables into the environment

def send_slack_notification(message):
    webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    if not webhook_url:
        print(" SLACK_WEBHOOK_URL not found.")
        return
    payload = {"text": message}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 200:
        print(" Slack notification sent.")
    else:
        print(f" Failed to send Slack notification: {response.status_code}")