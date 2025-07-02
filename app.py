from fastapi import FastAPI
from amazon_sp_api_client import AmazonSPAPIClient

app = FastAPI()
client = AmazonSPAPIClient()

@app.get("/")
def root():
    return {"message": "AI Amazon Seller Bot is live!"}

@app.get("/listings/{seller_id}/{sku}")
def get_listing(seller_id: str, sku: str):
    return client.get_listings_items(seller_id, sku)
