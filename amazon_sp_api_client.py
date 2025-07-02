import os
from sp_api.api.listings.listings import Listings
from sp_api.base import SellingApiException, Marketplaces
from sp_api.base.credentials import Credentials


class AmazonSPAPIClient:
    def __init__(self):
        self.marketplace = Marketplaces.US
        self.credentials = Credentials(
            refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
            lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
            lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
            aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
            aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
            role_arn=os.getenv("SPAPI_ROLE_ARN"),
        )

    def get_listing(self, asin):
        try:
            result = Listings(
                marketplace=self.marketplace,
                credentials=self.credentials
            ).get_listing(asin)
            return result.payload
        except SellingApiException as ex:
            print(f"Error getting listing for ASIN {asin}: {ex}")
            return None
