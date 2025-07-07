from fastapi import FastAPI
from pydantic import BaseModel
from amazon_sp_api_client import get_product_pricing

app = FastAPI()

class PricingRequest(BaseModel):
    asin: str

@app.get("/")
def root():
    return {"message": "Amazon Seller Bot is running"}

@app.post("/pricing")
def pricing(data: PricingRequest):
    return get_product_pricing(data.asin)
