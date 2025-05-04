from fastapi import FastAPI
import httpx

app = FastAPI()

MICROSERVICES = {
    "user_management": "http://microhubusermanagementcontainer:8000",
}

@app.get("/")
def root():
    return {"message":"hello world sss"}

@app.get("/user-management/sa1")
async def sa():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{MICROSERVICES['user_management']}/a1", timeout=5.0)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "Microservice reachable nahi hai!"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Microservice error: {exc.response.status_code}"}


@app.get("/user-management/sa2")
async def sa():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{MICROSERVICES['user_management']}/a2", timeout=5.0)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "Microservice reachable nahi hai!"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Microservice error: {exc.response.status_code}"}


@app.get("/user-management/sa3")
async def sa():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{MICROSERVICES['user_management']}/a3", timeout=5.0)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "Microservice reachable nahi hai!"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Microservice error: {exc.response.status_code}"}

@app.get("/user-management/sa4")
async def sa():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{MICROSERVICES['user_management']}/a4", timeout=5.0)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "Microservice reachable nahi hai!"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Microservice error: {exc.response.status_code}"}