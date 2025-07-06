from fastapi import FastAPI
from pydantic import BaseModel
import os
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

if __name__ == "__main__":
    import uvicorn
    print("ENV PORT:", os.environ.get("PORT"))
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
