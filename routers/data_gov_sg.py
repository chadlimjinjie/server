'''

https://datamall.lta.gov.sg/content/datamall/en.html
https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf

'''

import os
from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
import aiohttp

headers = {"AccountKey": os.getenv("LTA_API_KEY")}

data_traffic_images = {}
data_taxi_availability = {}
data_platform_crowd_density = []

lines = {
    "CCL": "Circle Line",
    "CEL": "Circle Line Extension – BayFront, Marina Bay",
    "CGL": "Changi Extension – Expo, Changi Airport",
    "DTL": "Downtown Line",
    "EWL": "East West Line",
    "NEL": "North East Line",
    "NSL": "North South Line",
    "BPL": "Bukit Panjang LRT",
    "SLRT": "Sengkang LRT",
    "PLRT": "Punggol LRT",
}
lines_shorthand_list = list(lines.keys())

async def get_traffic_images():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.data.gov.sg/v1/transport/traffic-images') as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            data = await response.json()
            # print(data)
            return data


async def get_taxi_availability():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.data.gov.sg/v1/transport/taxi-availability') as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            data = await response.json()
            # print(data)
            return data

# Updates every 10 minutes
async def get_platform_crowd_density_real_time():
    values = []
    async with aiohttp.ClientSession() as session:
        for train_line in lines_shorthand_list:

            async with session.get(f'https://datamall2.mytransport.sg/ltaodataservice/PCDRealTime?TrainLine={train_line}', headers=headers) as response:

                # print("Status:", response.status)
                # print("Content-type:", response.headers['content-type'])

                data = await response.json()
                # print(data)

                value = data.get("value")
                print(value)
                values.extend(value)
        return values


@asynccontextmanager
async def lifespan(router: FastAPI):
    # Some task
    print("data_gov_sg lifespan")
    global data_traffic_images
    global data_taxi_availability
    global data_platform_crowd_density
    data_traffic_images = await get_traffic_images()
    data_taxi_availability = await get_taxi_availability()
    # data_platform_crowd_density = await get_platform_crowd_density_real_time()
    yield
    # Clean up and release resources



router = APIRouter(
    prefix="/data_gov_sg",
    lifespan=lifespan
)

@router.get("/traffic-images")
async def read_traffic_images():
    return data_traffic_images


@router.get("/taxi-availability")
def read_taxi_availability():
    return data_taxi_availability


@router.get("/platform-crowd-density")
def platform_crowd_density():
    print(data_platform_crowd_density)
    return data_platform_crowd_density


