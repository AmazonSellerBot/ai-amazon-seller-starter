def get_marketplace_participations(access_token):
    region = os.environ.get("SPAPI_REGION", "na")
    host = "sellingpartnerapi-na.amazon.com" if region == "na" else "sellingpartnerapi-eu.amazon.com"
    endpoint = f"https://{host}/sellers/v1/marketplaceParticipations"

    # Prepare AWSRequest and sign it
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

    # Extract signed headers
    signed_headers = dict(aws_request.headers)

    # Send the request with requests
    response = requests.get(endpoint, headers=signed_headers)
    response.raise_for_status()
    return response.json()
