from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import os
import boto3

# Optional: import your real Amazon SP-API logic here
import amazon_sp_api_client  # You must create this module

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"status": "AI Amazon Seller Bot is running!"}

# Check environment variables route
@app.get("/env")
def get_env():
    return {
        "SELLER_ID": os.getenv("SPAPI_SELLER_ID"),
        "ROLE_ARN": os.getenv("SPAPI_ROLE_ARN")
    }

# Data model for listing optimization
class ListingUpdateRequest(BaseModel):
    asin: str
    new_title: Optional[str] = None
    new_bullets: Optional[List[str]] = None
    new_search_terms: Optional[str] = None

# Main optimization route
@app.post("/optimize-listing")
def optimize_listing(data: ListingUpdateRequest):
    asin = data.asin
    updates = {}

    if data.new_title:
        updates["title"] = data.new_title
    if data.new_bullets:
        updates["bullet_points"] = data.new_bullets
    if data.new_search_terms:
