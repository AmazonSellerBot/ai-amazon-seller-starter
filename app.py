from fastapi import FastAPI
from pydantic import BaseModel
from amazon_sp_api_client import AmazonSPAPIClient

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Amazon Seller Bot is running"}

class ListingUpdateRequest(BaseModel):
    asin: str
    title: str

@app.post("/optimize-listing")
def optimize_listing(request: ListingUpdateRequest):
    client = AmazonSPAPIClient()
    result = client.update_listing_title(request.asin, request.title)
    return {"status": "success", "result": result}
