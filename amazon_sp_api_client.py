from sp_api.api import Listings
from sp_api.base import Marketplaces, SellingApiException
import os

class AmazonSPAPIClient:
    def __init__(self):
        self.client = Listings(
            marketplace=Marketplaces.US,
            refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
            lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
            lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
            aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
            aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
            role_arn=os.getenv("SPAPI_ROLE_ARN"),
        )

    def get_listings(self):
        try:
            result = self.client.get_listings_items(sellerId=os.getenv("SPAPI_SELLER_ID"))
            return result.payload
        except SellingApiException as e:
            return {"error": str(e)}
