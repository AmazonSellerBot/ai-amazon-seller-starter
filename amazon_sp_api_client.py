import os
from sp_api.api.listings import Listings
from sp_api.base import Marketplaces, SellingApiException

class AmazonSPAPIClient:
    def __init__(self):
        self.marketplace = Marketplaces.US

    def update_listing_title(self, asin: str, new_title: str):
        try:
            result = Listings(marketplace=self.marketplace).patch_listing_item(
                sellerId=os.getenv("SELLER_ID"),
                sku=asin,
                body={
                    "productType": "PRODUCT",
                    "patches": [
                        {
                            "op": "replace",
                            "path": "/attributes/title",
                            "value": [new_title]
                        }
                    ]
                }
            )
            return result.payload
        except SellingApiException as e:
            return {"error": str(e)}
