import os
from sp_api.api import Products
from sp_api.base import SellingApiCredentials, Marketplaces

credentials = SellingApiCredentials(
    refresh_token=os.getenv("LWA_REFRESH_TOKEN"),
    lwa_app_id=os.getenv("LWA_CLIENT_ID"),
    lwa_client_secret=os.getenv("LWA_CLIENT_SECRET"),
    aws_secret_key=os.getenv("SPAPI_AWS_SECRET_ACCESS_KEY"),
    aws_access_key=os.getenv("SPAPI_AWS_ACCESS_KEY_ID"),
    role_arn=os.getenv("SPAPI_ROLE_ARN"),
)

def get_product_pricing(asin: str):
    try:
        products = Products(credentials=credentials, marketplace=Marketplaces.US)
        response = products.get_product_pricing(ItemType='ASIN', ItemIds=[asin])
        return response.payload
    except Exception as e:
        return {"error": str(e)}
