from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logging.info("🚀 App is starting...")

@app.get("/")
def root():
    return {"message": "AI Amazon Seller Starter is live!"}
