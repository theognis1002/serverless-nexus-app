import json

import requests


def ip_address_handler(event, context):
    response = requests.get("https://httpbin.org/ip")
    print(response.json())
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "status_code": f"{response.status_code}",
                "ip_address": f"{response.json()}"
            }
        ),
    }
