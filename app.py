from fastapi import FastAPI
from amazon_sp_api_client import AmazonSPAPIClient

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Amazon SP-API Client is running!"}

@app.get("/catalog")
def get_catalog_item():
    client = AmazonSPAPIClient()
    result = client.get_catalog_item("B0D951BRRP")
    return result
