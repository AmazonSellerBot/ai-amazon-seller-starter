import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))  # safely cast to int with default
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
