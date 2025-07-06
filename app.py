from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class PricingRequest(BaseModel):
    asin: str

@app.get("/")
def root():
    return {"message": "Amazon Seller Bot is running"}

@app.post("/pricing")
def pricing(data: PricingRequest):
    return {
        "asin": data.asin,
        "mock": "This is a placeholder — app is running fine!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
