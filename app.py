from fastapi import FastAPI
from pydantic import BaseModel
from amazon_sp_api_client import get_product_pricing
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Amazon Seller Bot is live!"}

class PricingRequest(BaseModel):
    asin: str

@app.post("/pricing")
def fetch_pricing(request: PricingRequest):
    return get_product_pricing(request.asin)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
