from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PricingRequest(BaseModel):
    asin: str

@app.get("/")
def root():
    return {"message": "Amazon Seller Bot is running"}

@app.post("/pricing")
def pricing(data: PricingRequest):
    return {"price": f"Fake price for {data.asin}"}  # placeholder
