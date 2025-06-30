# amazon_sp_api_client.py
import os
from sp_api.base import Marketplaces, SellingApiCredentials
from sp_api.api.listings.items import ListingsItems

class AmazonSPAPIClient:
    def __init__(self):
        self.credentials = SellingApiCredentials(
            refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
            lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
            lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
            aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
            aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
            role_arn=os.getenv("SPAPI_ROLE_ARN"),
        )
        self.marketplace = Marketplaces.US
        self.seller_id = os.getenv("SPAPI_SELLER_ID")

    def get_listing(self, asin):
        listings = ListingsItems(credentials=self.credentials)
        return listings.get_listing_item(
            sellerId=self.seller_id,
            asin=asin,
            marketplaceIds=[self.marketplace.marketplace_id]
        ).payload
