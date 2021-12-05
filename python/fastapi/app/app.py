import time
import asyncio
from fastapi import FastAPI, APIRouter
from app.router import router
import uvicorn

app = FastAPI()
app.include_router(router)

count = 0

@app.get("/")
def home():
    return {"message": "hello world", "counter": count}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=False)
