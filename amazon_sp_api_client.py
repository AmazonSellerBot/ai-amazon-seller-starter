from sp_api.api import Listings
from sp_api.base import Marketplaces, SellingApiException
import os

def get_listing(asin: str):
    try:
        result = Listings(marketplace=Marketplaces.US).get_listing(asin)
        return result.payload
    except SellingApiException as e:
        return {"error": str(e)}

def update_listing(asin: str, attribute_name: str, new_value: str):
    try:
        result = Listings(marketplace=Marketplaces.US).patch_listing(
            asin=asin,
            data={
                "productType": "PRODUCT",
                "patches": [
                    {
                        "op": "replace",
                        "path": f"/attributes/{attribute_name}/0/value",
                        "value": new_value
                    }
                ]
            }
        )
        return result.payload
    except SellingApiException as e:
        return {"error": str(e)}
