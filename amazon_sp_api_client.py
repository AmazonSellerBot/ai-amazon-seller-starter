import os
from sp_api.api.listings.listings import Listings
from sp_api.base import Marketplaces, SellingApiException
from sp_api.base.credentials import Credentials


class AmazonSPAPIClient:
    def __init__(self):
        self.credentials = Credentials(
            refresh_token=os.environ['SPAPI_REFRESH_TOKEN'],
            lwa_app_id=os.environ['SPAPI_CLIENT_ID'],
            lwa_client_secret=os.environ['SPAPI_CLIENT_SECRET'],
            aws_secret_key=os.environ['SPAPI_AWS_SECRET_ACCESS_KEY'],
            aws_access_key=os.environ['SPAPI_AWS_ACCESS_KEY_ID'],
            role_arn=os.environ['SPAPI_ROLE_ARN']
        )
        self.marketplace = Marketplaces.US
        self.seller_id = os.environ['SPAPI_SELLER_ID']

    def get_listing_item(self, asin: str):
        try:
            result = Listings(
                credentials=self.credentials,
                marketplace=self.marketplace
            ).get_listing_item(seller_id=self.seller_id, sku=asin)
            return result.payload
        except SellingApiException as e:
            print("Error fetching listing item:", e)
            return None

    def patch_listing_item(self, asin: str, update_data: dict):
        try:
            result = Listings(
                credentials=self.credentials,
                marketplace=self.marketplace
            ).patch_listing_item(seller_id=self.seller_id, sku=asin, body=update_data)
            return result.payload
        except SellingApiException as e:
            print("Error updating listing:", e)
            return None
