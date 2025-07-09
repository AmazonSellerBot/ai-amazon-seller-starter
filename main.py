from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🎉 Amazon Seller Bot is running!"}
