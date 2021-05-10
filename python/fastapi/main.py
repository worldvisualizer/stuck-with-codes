import time
import asyncio
from fastapi import FastAPI, APIRouter
from router import router


app = FastAPI()
app.include_router(router)

count = 0

@app.get("/")
def home():
    return {"message": "hello world", "counter": count}


