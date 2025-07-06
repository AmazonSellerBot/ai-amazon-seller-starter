import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Amazon Seller Bot is running"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
