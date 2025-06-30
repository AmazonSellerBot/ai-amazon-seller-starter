from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from amazon_sp_api_client import AmazonSPAPIClient
import os

app = FastAPI()

class ListingUpdateRequest(BaseModel):
    asin: str
    seller_sku: str
    bullet_point_5: str

@app.get("/")
def root():
    return {"message": "ChatZon API is Live"}

@app.post("/optimize-listing")
def optimize_listing(data: ListingUpdateRequest):
    client = AmazonSPAPIClient()
    result = client.update_listing(
        seller_sku=data.seller_sku,
        asin=data.asin,
        updated_bullet=data.bullet_point_5
    )
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return {"success": True, "response": result}
