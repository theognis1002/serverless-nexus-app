import json

import requests


def user_agent_handler(event, context):
    response = requests.get("https://httpbin.org/user-agent")
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "status_code": f"{response.status_code}",
                "user_agent": f"{response.json()}"
            }
        ),
    }
