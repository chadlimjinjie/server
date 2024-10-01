from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
import uuid

from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(router: FastAPI):
    # Some task
    print("meeting lifespan")

    # Mount the SocketIO app
    # router.mount("/ws", socket_app)

    yield
    # Clean up and release resources


router = APIRouter(
    prefix="/meeting",
    lifespan=lifespan
)


@router.get('')
async def read_root():
    return FileResponse("public/meeting.html")

# Create unique room id using uuid4
@router.get("/create-room")
async def create_room():
    room_id = str(uuid.uuid4())
    return {"room_id": room_id}

