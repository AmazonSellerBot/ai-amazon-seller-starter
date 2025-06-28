from fastapi import FastAPI
from test_spapi import get_access_token, get_marketplace_participations

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Amazon Seller Bot is running"}

@app.get("/marketplaces")
def marketplaces():
    access_token = get_access_token()
    return get_marketplace_participations(access_token)
