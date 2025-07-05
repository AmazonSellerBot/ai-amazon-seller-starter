from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Amazon Seller Starter is live!"}

