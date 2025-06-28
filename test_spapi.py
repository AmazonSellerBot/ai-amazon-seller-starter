import os
import requests
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

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
    region = os.environ.get("SPAPI_REGION", "na")
    host = "sellingpartnerapi-na.amazon.com" if region == "na" else "sellingpartnerapi-eu.amazon.com"
    endpoint = f"https://{host}/sellers/v1/marketplaceParticipations"

    aws_request = AWSRequest(
        method="GET",
        url=endpoint,
        headers={
            "host": host,
            "x-amz-access-token": access_token
        }
    )

    credentials = boto3.Session().get_credentials()
    SigV4Auth(credentials, "execute-api", "us-east-1").add_auth(aws_request)

    signed_headers = dict(aws_request.headers)
    response = requests.get(endpoint, headers=signed_headers)
    response.raise_for_status()
    return response.json()
