# app.py
from fastapi import FastAPI
from test_spapi import get_access_token, get_marketplace_participations

app = FastAPI()

@app.get("/marketplaces")
def marketplaces():
    token = get_access_token()
    result = get_marketplace_participations(token)
    return result
