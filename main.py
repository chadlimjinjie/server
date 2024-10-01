'''
https://github.com/MongoEngine/mongoengine
https://docs.aiohttp.org/en/stable/

https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/


'''
import os
# from typing import Union
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

import mongoengine

from routers import data_gov_sg, youtube

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://127.0.0.1:80",
# ]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Some task
    print("main lifespan")

    mongoengine.connect(
        db=os.getenv('DB_NAME'),
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_STRING')
    )
    yield
    # Clean up and release resources


app = FastAPI(
    lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data_gov_sg.router)
app.include_router(youtube.router)

@app.get("/")
def read_root():
    return RedirectResponse("/docs")


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
