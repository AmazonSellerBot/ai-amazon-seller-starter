from sp_api.api.listings.listings import Listings
from sp_api.base import Marketplaces, SellingApiException
import os

def update_listing(asin, updates):
    try:
        listings = Listings(
            marketplace=Marketplaces.US,
            refresh_token=os.getenv("SPAPI_REFRESH_TOKEN"),
            lwa_app_id=os.getenv("SPAPI_CLIENT_ID"),
            lwa_client_secret=os.getenv("SPAPI_CLIENT_SECRET"),
            aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
            aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
            role_arn=os.getenv("SPAPI_ROLE_ARN")
        )

        patch_data = {
            "productType": "PRODUCT",
            "patches": []
        }

        if "title" in updates:
            patch_data["patches"].append({
                "op": "replace",
                "path": "/attributes/title",
                "value": [{"value": updates["title"], "language_tag": "en_US"}]
            })

        if "bullet_points" in updates:
            patch_data["patches"].append({
                "op": "replace",
                "path": "/attributes/bullet_point",
                "value": [{"value": b, "language_tag": "en_US"} for b in updates["bullet_points"]]
            })

        if "search_terms" in updates:
            patch_data["patches"].append({
                "op": "replace",
                "path": "/attributes/generic_keyword",
                "value": [{"value": updates["search_terms"], "language_tag": "en_US"}]
            })

        response = listings.patch_listing_item(
            sellerId=os.getenv("SPAPI_SELLER_ID"),
            sku=asin,
            body=patch_data
        )

        return response.payload

    except SellingApiException as e:
        return {"error": str(e)}
