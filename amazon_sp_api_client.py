from sp_api.api.catalog import Catalog
from sp_api.base import Marketplaces, SellingApiCredentials

import os

class AmazonSPAPIClient:
    def __init__(self):
        self.catalog = Catalog(
            credentials=SellingApiCredentials(
                refresh_token=os.getenv("LWA_REFRESH_TOKEN"),
                lwa_app_id=os.getenv("LWA_APP_ID"),
                lwa_client_secret=os.getenv("LWA_CLIENT_SECRET"),
                aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
                aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
                role_arn=os.getenv("SPAPI_ROLE_ARN"),
            ),
            marketplace=Marketplaces.US
        )

    def get_catalog_item(self, asin):
        return self.catalog.get_catalog_item(asin).payload
