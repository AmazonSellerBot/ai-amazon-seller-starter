from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import os
import boto3
import amazon_sp_api_client  # Ensure this file exists

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Amazon Seller Bot is running!"}

@app.get("/env")
def get_env():
    return {
        "SELLER_ID": os.getenv("SPAPI_SELLER_ID"),
        "ROLE_ARN": os.getenv("SPAPI_ROLE_ARN")
    }

class ListingUpdateRequest(BaseModel):
    asin: str
    new_title: Optional[str] = None
    new_bullets: Optional[List[str]] = None
    new_search_terms: Optional[str] = None

@app.post("/optimize-listing")
def optimize_listing(data: ListingUpdateRequest):
    asin = data.asin
    updates = {}

    if data.new_title:
        updates["title"] = data.new_title
    if data.new_bullets:
        updates["bullet_points"] = data.new_bullets
    if data.new_search_terms:
        updates["search_terms"] = data.new_search_terms

    if not updates:
        raise HTTPException(status_code=400, detail="No update fields provided.")

    try:
        result = amazon_sp_api_client.update_listing(asin, updates)
        return {
            "asin": asin,
            "updates_applied": updates,
            "amazon_response": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
