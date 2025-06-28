import os
import requests
import time
import json
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.httpsession import URLLib3Session


def get_access_token():
    url = "https://api.amazon.com/auth/o2/token"
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": os.environ["SPAPI_REFRESH_TOKEN"],
        "client_id": os.environ["SPAPI_CLIENT_ID"],
        "client_secret": os.environ["SPAPI_CLIENT_SECRET"]
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()["access_token"]

def get_marketplace_participations(access_token):
    region = os.environ["SPAPI_REGION"]
    host = "sellingpartnerapi-na.amazon.com" if region == "na" else "sellingpartnerapi-eu.amazon.com"
    endpoint = f"https://{host}/sellers/v1/marketplaceParticipations"

    aws_request = AWSRequest(
        method="GET",
        url=endpoint,
        headers={
            "x-amz-access-token": access_token,
            "host": host
        }
    )

    credentials = boto3.Session().get_credentials()
    SigV4Auth(credentials, "execute-api", "us-east-1").add_auth(aws_request)

    session = URLLib3Session()
    response = session.send(aws_request)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("[🔁] Requesting Access Token...")
    token = get_access_token()
    print("[✅] Access Token received!")
    print("[🌐] Sending test API call to Amazon...")

    try:
        result = get_marketplace_participations(token)
        print("[✅] Success! Your marketplaces:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print("[❌] Error talking to Amazon SP-API:")
        print(str(e))
