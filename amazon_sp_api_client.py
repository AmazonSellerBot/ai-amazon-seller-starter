import os
from sp_api.api import Products
from sp_api.base import Marketplaces

def get_product_pricing(asin: str):
    try:
        credentials = dict(
            refresh_token=os.environ["LWA_REFRESH_TOKEN"],
            lwa_app_id=os.environ["LWA_CLIENT_ID"],
            lwa_client_secret=os.environ["LWA_CLIENT_SECRET"],
            aws_access_key=os.environ["SPAPI_AWS_ACCESS_KEY_ID"],
            aws_secret_key=os.environ["SPAPI_AWS_SECRET_ACCESS_KEY"],
            role_arn=os.environ["SPAPI_ROLE_ARN"],
        )

        products = Products(marketplace=Marketplaces.US, credentials=credentials)
        response = products.get_product_pricing(ItemType="ASIN", ItemIds=[asin])
        return {"result": response.payload}
    except Exception as e:
        return {"error": str(e)}
