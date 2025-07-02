from sp_api.api import CatalogItems
from sp_api.base import Marketplaces, SellingApiException
from dotenv import load_dotenv
import os

load_dotenv()

class AmazonSPAPIClient:
    def __init__(self):
        self.marketplace = Marketplaces.US

    def get_product_by_asin(self, asin: str):
        try:
            result = CatalogItems(marketplace=self.marketplace).get_catalog_item(asin)
            return result.payload
        except SellingApiException as e:
            return {"error": str(e)}
