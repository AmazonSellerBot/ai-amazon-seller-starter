from sp_api.api import Listings
from sp_api.base import Marketplaces
from sp_api.base.credentials import Credentials
import os

class AmazonSPAPIClient:
    def __init__(self):
        credentials = Credentials(
            refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
            lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
            lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
            aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
            aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
            role_arn=os.getenv("SPAPI_ROLE_ARN")
        )
        self.marketplace = Marketplaces.US
        self.credentials = credentials

    def get_listing(self, asin):
        result = Listings(credentials=self.credentials, marketplace=self.marketplace).get_catalog_item(asin)
        return result.payload
