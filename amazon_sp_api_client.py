import os
from sp_api.base import Marketplaces, SellingApiCredentials
from sp_api.api.listings.v2021_08_01 import Listings

# Your hardcoded Seller ID
SELLER_ID = "A2RY9NFQSHF0DY"

# Set up credentials using environment variables
credentials = SellingApiCredentials(
    refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
    lwa_app_id=os.getenv("SPAPI_LWA_APP_ID"),
    lwa_client_secret=os.getenv("SPAPI_LWA_CLIENT_SECRET"),
    aws_secret_access_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
    aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
    role_arn=os.getenv("SPAPI_ROLE_ARN"),
)

def update_listing_title(asin: str, new_title: str):
    listings_api = Listings(credentials=credentials, marketplace=Marketplaces.US)
    response = listings_api.patch_listing_item(
        sellerId=SELLER_ID,
        sku=asin,
        body={
            "productType": "PRODUCT",
            "patches": [
                {
                    "op": "replace",
                    "path": "/attributes/title",
                    "value": [ { "value": new_title } ],
                }
            ]
        }
    )
    return response.payload
