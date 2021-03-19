import time
import asyncio
from fastapi import FastAPI, APIRouter

router = APIRouter()
app = FastAPI()
count = 0

def counter():
    global count
    count += 1

def wait_function():
    while True:
        counter()

@app.get("/")
def home():
    return {"message": "hello world", "counter": counter}

asyncio.run(wait_function())
