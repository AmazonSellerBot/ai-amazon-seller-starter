from sp_api.api import ListingsItemsV20210801
from sp_api.base import Marketplaces
from sp_api.base.exceptions import SellingApiException

class AmazonSPAPIClient:
    def __init__(self):
        self.marketplace = Marketplaces.US

    def update_listing(self, seller_sku: str, asin: str, updated_bullet: str):
        try:
            response = ListingsItemsV20210801().patch_listing_item(
                seller_id='YOUR_SELLER_ID',
                sku=seller_sku,
                marketplace_ids=[self.marketplace.marketplace_id],
                body={
                    "productType": "PRODUCT",
                    "patches": [
                        {
                            "op": "replace",
                            "path": "/productDescription/bulletPoint5",
                            "value": updated_bullet
                        }
                    ]
                }
            )
            return response.payload
        except SellingApiException as e:
            return {"error": str(e)}
