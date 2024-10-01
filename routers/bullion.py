
from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
import aiohttp
from pydantic import BaseModel


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
    print("bullion lifespan")

    yield
    # Clean up and release resources


router = APIRouter(
    prefix="/bullion",
    lifespan=lifespan
)

'''
example@example.com

https://services.bullionstar.com

POST
https://www.bullionstar.com/auth/v1/initialize
email: example@example.com
machineId: rJlyVatyhuWmdnug9SzI
ignoreWarning: false
device: D

{
    "status": 0,
    "title": "",
    "message": "",
    "authToken": "eyJraWQiOiIxLjAuMCIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJidWxsaW9uc3RhciIsImV4cCI6MTcyNjg5MDIxMCwiaWF0IjoxNzI2ODg5OTEwLCJzdWIiOiJMUTFhZkxZfik1XSttRD0rWUxwci1rTF8rN3RDRmFLUlgpWVRHdFRuTnQpWGs5K1lUZD92JXF5Kmh9JX5RdE4zXXE2Zj90OUprcHowNV59ZmJ9bTB3VUoxdS1WUk5xWX1zeGk9e1widG9rZW5cIjpcIkpRRUhOTkZGRUpPQ05STVFUQVNKSVBISkxTTlRFR0hTXCIsXCJlbWFpbFwiOlwiXCIsXCJhY2NvdW50SWRcIjotMSxcInNhbHRcIjpcIjJseXpHclNnUm1DSU03S2ptTEoxWFg2TEJNbWdMclZGamNkRmdKMGhUVzJneGxTd1RJbXhmd0NrV2hUaHppVmhsU0MwQkllTWpjRVBwd1xcdTAwM2RcXHUwMDNkXCIsXCJtYWNoaW5lSWRcIjpcIlwiLFwiZXhwaXJlVGltZVwiOjE3MjY4OTcxMTAwNDd9In0.IMtcMmgDmhGoiCFAamptrLwQ4JAD2LFIyzwTCIye-NqMf-wXABjSmgtx4LfeMG1daESTH0OVb977qwwo5iGBwVt35UtR7aacZ4-HoSzfq_jNOfjYR1fmXHq8o3vSN4r0HOsrmcAC5rpXL0mlgFpc846NQaFeaU7bBKc9A_livabDTzTbeJrXddm1sOKnsgMXq3GiGjPHlIXz3VmY90Di9mruWhzZ7dGNs0_uFzrdUp1EVRje-RiOYSpMpsVIJlviu0OQEga7OlKlFc4nixsAi68NNqJgYZvNrK9PmcoPrvC1h0ARt4YRzDsGeolVOgWXPL0LNfJdlhB-1c55IulGkQ",
    "salt": "2lyzGrSgRmCIM7KjmLJ1XX6LBMmgLrVFjcdFgJ0hTW2gxlSwTImxfwCkWhThziVhlSC0BIeMjcEPpw==",
    "error": false,
    "success": true,
    "warning": false,
    "authenticationRequired": false,
    "accessDenied": false
}

POST
https://www.bullionstar.com/auth/v1/authenticate
authToken: eyJraWQiOiIxLjAuMCIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJidWxsaW9uc3RhciIsImV4cCI6MTcyNjg5MDIxMCwiaWF0IjoxNzI2ODg5OTEwLCJzdWIiOiJMUTFhZkxZfik1XSttRD0rWUxwci1rTF8rN3RDRmFLUlgpWVRHdFRuTnQpWGs5K1lUZD92JXF5Kmh9JX5RdE4zXXE2Zj90OUprcHowNV59ZmJ9bTB3VUoxdS1WUk5xWX1zeGk9e1widG9rZW5cIjpcIkpRRUhOTkZGRUpPQ05STVFUQVNKSVBISkxTTlRFR0hTXCIsXCJlbWFpbFwiOlwiXCIsXCJhY2NvdW50SWRcIjotMSxcInNhbHRcIjpcIjJseXpHclNnUm1DSU03S2ptTEoxWFg2TEJNbWdMclZGamNkRmdKMGhUVzJneGxTd1RJbXhmd0NrV2hUaHppVmhsU0MwQkllTWpjRVBwd1xcdTAwM2RcXHUwMDNkXCIsXCJtYWNoaW5lSWRcIjpcIlwiLFwiZXhwaXJlVGltZVwiOjE3MjY4OTcxMTAwNDd9In0.IMtcMmgDmhGoiCFAamptrLwQ4JAD2LFIyzwTCIye-NqMf-wXABjSmgtx4LfeMG1daESTH0OVb977qwwo5iGBwVt35UtR7aacZ4-HoSzfq_jNOfjYR1fmXHq8o3vSN4r0HOsrmcAC5rpXL0mlgFpc846NQaFeaU7bBKc9A_livabDTzTbeJrXddm1sOKnsgMXq3GiGjPHlIXz3VmY90Di9mruWhzZ7dGNs0_uFzrdUp1EVRje-RiOYSpMpsVIJlviu0OQEga7OlKlFc4nixsAi68NNqJgYZvNrK9PmcoPrvC1h0ARt4YRzDsGeolVOgWXPL0LNfJdlhB-1c55IulGkQ
encryptedPassword: 9ff756e8470258586efb67d88a9eb4ad
valuation: buy
locationId: 1
ignoreWarning: false
device: D

{
    "status": 1,
    "title": "Incorrect email or password",
    "message": "The email address or password you entered was incorrect.",
    "accessToken": null,
    "authenticateIp": false,
    "pendingDueDiligence": false,
    "twoFactorToken": null,
    "twoFactorMachineToken": null,
    "twoFactorGoogleAuthenticatorToken": null,
    "locked": false,
    "loggedIn": false,
    "accountInfo": null,
    "error": true,
    "warning": false,
    "success": false,
    "authenticationRequired": false,
    "accessDenied": false
}

'''
@router.get("/login")
async def post_login():
    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.bullionstar.com/auth/v1/initialize') as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            data = await response.json()
            # print(data)
            return data
    return 


