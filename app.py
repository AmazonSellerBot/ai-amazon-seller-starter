from fastapi import FastAPI
from amazon_sp_api_client import AmazonSPAPIClient

app = FastAPI()
sp_api_client = AmazonSPAPIClient()

@app.get("/")
def root():
    return {"status": "Amazon Seller Bot is up and running!"}

@app.get("/listings/{seller_id}")
def get_listings(seller_id: str):
    return sp_api_client.get_listings_items(seller_id)
