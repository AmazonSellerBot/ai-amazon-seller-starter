from sp_api.api import Listings
from sp_api.base import Marketplaces, SellingApiException

def update_listing(asin, updates):
    try:
        listings = Listings(marketplace=Marketplaces.US)

        patch_data = {}

        if "title" in updates:
            patch_data["productType"] = "PRODUCT"
            patch_data.setdefault("patches", []).append({
                "op": "replace",
                "path": "/attributes/title",
                "value": [{ "value": updates["title"], "language_tag": "en_US" }]
            })

        if "bullet_points" in updates:
            patch_data.setdefault("patches", []).append({
                "op": "replace",
                "path": "/attributes/bullet_point",
                "value": [{ "value": b, "language_tag": "en_US" } for b in updates["bullet_points"]]
            })

        if "search_terms" in updates:
            patch_data.setdefault("patches", []).append({
                "op": "replace",
                "path": "/attributes/generic_keyword",
                "value": [{ "value": updates["search_terms"], "language_tag": "en_US" }]
            })

        response = listings.patch_listing_item(
            sellerId=None,
            sku=asin,
            body=patch_data
        )

        return response.payload

    except SellingApiException as e:
        return {"error": str(e)}
