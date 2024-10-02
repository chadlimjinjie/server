from fastapi import FastAPI

from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(router: FastAPI):
    # Some task
    print("email lifespan")


    yield
    # Clean up and release resources


router = APIRouter(
    prefix="/auth",
    lifespan=lifespan
)


@router.get('')
async def read_root():
    return ''
