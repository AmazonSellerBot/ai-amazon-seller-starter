from fastapi import FastAPI
from amazon_sp_api_client import AmazonSPAPIClient

app = FastAPI()
client = AmazonSPAPIClient()

@app.get("/")
def read_root():
    return {"message": "Amazon Seller Starter is running!"}

@app.get("/catalog/{asin}")
def get_catalog_info(asin: str):
    return client.get_product_by_asin(asin)
