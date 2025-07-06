import os
from sp_api.api import Products
from sp_api.base import Marketplaces
from sp_api.base.exceptions import SellingApiException

def get_product_pricing(asin: str):
    try:
        credentials = {
            "refresh_token": os.environ.get("LWA_REFRESH_TOKEN"),
            "lwa_app_id": os.environ.get("LWA_CLIENT_ID"),
            "lwa_client_secret": os.environ.get("LWA_CLIENT_SECRET"),
            "aws_access_key": os.environ.get("SPAPI_AWS_ACCESS_KEY_ID"),
            "aws_secret_key": os.environ.get("SPAPI_AWS_SECRET_ACCESS_KEY"),
            "role_arn": os.environ.get("SPAPI_ROLE_ARN"),
        }

        # Optional fallback: use SPAPI_SELLER_ID if needed
        seller_id = os.environ.get("SPAPI_SELLER_ID")

        products = Products(
            marketplace=Marketplaces.US,
            credentials=credentials,
        )

        response = products.get_product_pricing(ItemType="ASIN", ItemIds=[asin])
        return {"data": response.payload}
    
    except SellingApiException as e:
        return {"spapi_error": str(e), "details": e.response}
    except Exception as e:
        return {"unhandled_error": str(e)}
