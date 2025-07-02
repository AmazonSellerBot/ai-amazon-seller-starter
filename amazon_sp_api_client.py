from sp_api.api.listings import Listings
from sp_api.base import Marketplaces, SellingApiException

class AmazonSPAPIClient:
    def __init__(self):
        self.marketplace = Marketplaces.US

    def get_listings_items(self, seller_id, sku):
        try:
            listings = Listings(marketplace=self.marketplace)
            result = listings.get_listings_item(seller_id=seller_id, sku=sku)
            return result.payload
        except SellingApiException as e:
            return {"error": str(e)}
