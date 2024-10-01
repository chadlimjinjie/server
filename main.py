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

from fastapi.staticfiles import StaticFiles
import socketio
import uvicorn

import mongoengine

from routers import data_gov_sg, youtube, meeting



origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:80",
]

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
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data_gov_sg.router)
app.include_router(youtube.router)
app.include_router(meeting.router)
app.mount("/public", StaticFiles(directory="public"), name="public")
#Socket io (sio) create a Socket.IO server
sio = socketio.AsyncServer(cors_allowed_origins='*',async_mode='asgi')
# wrap with ASGI application
socket_app = socketio.ASGIApp(sio)
app.mount("/", socket_app)

@app.get("/")
def read_root():
    return RedirectResponse("/docs")


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# Socket.IO events
@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
async def join(sid, data):
    room_id = data['room_id']
    await sio.enter_room(sid, room_id)
    # Notify existing users in the room that a new user has joined
    await sio.emit("user-joined", {"sid": sid}, room=room_id, skip_sid=sid)
    print(f"Client {sid} joined room {room_id}")

@sio.event
async def leave(sid, data):
    room_id = data['room_id']
    sio.leave_room(sid, room_id)
    await sio.emit("user-left", {"sid": sid}, room=room_id)
    print(f"Client {sid} left room {room_id}")

@sio.event
async def signal(sid, data):
    room_id = data['room_id']
    await sio.emit("signal", data, room=room_id, skip_sid=sid)

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
