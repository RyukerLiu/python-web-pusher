from pywebpush import webpush
import json
import sys

def web_push(subscription_info, data):
    subscription_info = json.loads(subscription_info)

    webpush(
        subscription_info,
        data,
        vapid_private_key="PTdnI92OWhybCbYC6Qh1A3_NIyah9UsOyEdB2aMCLoQ",
        vapid_claims={"sub": "mailto:allen@test.com"}
    )

if __name__ == "__main__":
    subscription_info = sys.argv[1]
    data = sys.argv[2]
    web_push(subscription_info, data)