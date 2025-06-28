from fastapi import FastAPI
from test_spapi import get_access_token, get_marketplace_participations

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Amazon Seller Bot is running."}

@app.get("/marketplaces")
def read_marketplaces():
    token = get_access_token()
    marketplaces = get_marketplace_participations(token)
    return marketplaces
