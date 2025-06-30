from sp_api.base import Marketplaces, SellingApiClient
from sp_api.api.listings import Listings
import os

class AmazonSPAPIClient:
    def __init__(self):
        self.client = SellingApiClient(
            credentials=dict(
                refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
                lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
                lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
                aws_secret_access_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
                aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
                role_arn=os.getenv("SPAPI_ROLE_ARN"),
            ),
            marketplace=Marketplaces.US,
        )

    def patch_listing(self, asin: str, new_bullet: str, bullet_index: int):
        listing_api = Listings(credentials=self.client.credentials)
        attributes = {f'bullet_point{bullet_index+1}': new_bullet}
        response = listing_api.patch_listing_item(
            sellerId=os.getenv("AMAZON_SELLER_ID"),
            asin=asin,
            body={
                "productType": "PRODUCT",
                "patches": [
                    {
                        "op": "replace",
                        "path": f"/attributes/bullet_point{bullet_index+1}",
                        "value": [new_bullet]
                    }
                ]
            },
            marketplaceIds=["ATVPDKIKX0DER"]
        )
        return response.payload
