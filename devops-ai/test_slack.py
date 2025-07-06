from slack_notifi import send_slack_notification

message = """
 *Test Alert from DevOps AI Agent*
This is a test message to verify that Slack integration works correctly.
– OpsBot 
"""

send_slack_notification(message)