
from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
# import aiohttp
from pydantic import BaseModel
import json

from models.UserYouTubeVideos import UserYouTubeVideos

# async def get_traffic_images():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.data.gov.sg/v1/transport/traffic-images') as response:

#             # print("Status:", response.status)
#             # print("Content-type:", response.headers['content-type'])

#             data = await response.json()
#             # print(data)
#             return data


@asynccontextmanager
async def lifespan(router: FastAPI):
    # Some task
    print("youtube lifespan")

    yield
    # Clean up and release resources



router = APIRouter(
    prefix="/youtube",
    lifespan=lifespan
)

class Video(BaseModel):
    videoId: str
    title: str
    description: str

@router.post("/add_new_video")
async def post_new_video(video: Video):
    video = UserYouTubeVideos(videoId=video.videoId, title=video.title, description=video.description)
    video.save()
    return 200

@router.get("/videos")
async def read_videos():
    videos = UserYouTubeVideos.objects().to_json()
    print(videos)
    return json.loads(videos)