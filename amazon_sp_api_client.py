import os
from sp_api.api.listings.listings import Listings
from sp_api.base import Marketplaces, SellingApiException
from dotenv import load_dotenv

load_dotenv()

class AmazonSPAPIClient:
    def __init__(self):
        self.marketplace = Marketplaces.US
        self.listings = Listings(
            credentials=dict(
                refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
                lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
                lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
                aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
                aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
                role_arn=os.getenv("SPAPI_ROLE_ARN"),
            ),
            marketplace=self.marketplace
        )

    def get_catalog_item(self, asin):
        try:
            result = self.listings.get_listings_item(sellerId=os.getenv("SELLER_ID"), sku=asin)
            return result.payload
        except SellingApiException as ex:
            return {"error": str(ex)}
