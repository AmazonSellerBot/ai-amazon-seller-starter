from sp_api.api.listings.v2021_08_01 import Listings
from sp_api.base import SellingApiException, Marketplaces

class AmazonSPAPIClient:
    def __init__(self, credentials: dict):
        self.marketplace = Marketplaces.US
        self.listings = Listings(
            credentials=credentials,
            marketplace=self.marketplace,
        )

    def get_listing(self, asin: str):
        try:
            result = self.listings.get_listing_item(sellerId=credentials['seller_id'], sku=asin)
            return result.payload
        except SellingApiException as e:
            return {"error": str(e)}

    def update_listing(self, sku: str, listing_data: dict):
        try:
            result = self.listings.put_listing_item(
                sellerId=credentials['seller_id'],
                sku=sku,
                body=listing_data,
            )
            return result.payload
        except SellingApiException as e:
            return {"error": str(e)}
