import os
from dotenv import load_dotenv
from sp_api.api.listings import Listings
from sp_api.base import SellingApiCredentials, Marketplaces

load_dotenv()

class AmazonSPAPIClient:
    def __init__(self):
        self.credentials = SellingApiCredentials(
            refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
            lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
            lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
            aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
            aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
            role_arn=os.getenv("SPAPI_ROLE_ARN")
        )

    def get_my_listings(self):
        res = Listings(credentials=self.credentials, marketplace=Marketplaces.US).get_listings_items(sellerId=os.getenv("SELLER_ID"))
        return res.payload
