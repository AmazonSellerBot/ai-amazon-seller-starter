from fastapi import FastAPI
from pydantic import BaseModel
from amazon_sp_api_client import AmazonSPAPIClient

app = FastAPI()
sp_api_client = AmazonSPAPIClient()

class ASINRequest(BaseModel):
    asin: str

@app.get("/")
def root():
    return {"message": "Amazon Seller Bot is live!"}

@app.post("/get-listing")
def get_listing(request: ASINRequest):
    result = sp_api_client.get_listing(request.asin)
    return {"result": result}
