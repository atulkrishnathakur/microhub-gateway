from fastapi import FastAPI
import httpx
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from typing import List

app = FastAPI()

MICROSERVICES = {
    "user_management": "http://microhubusermanagementcontainer:8000",
}

@app.get("/")
def root():
    return {"message":"hello world sss"}

@app.get("/abc")
def root():
    return {"message":"hello world abc test qqqq abc"}


class EmpSchemaIn(BaseModel):
    emp_name: str = Field(example="Atul")
    email: EmailStr = Field(example="atul@comsysapp.com")
    mobile: str | None = Field(example="000000")
    status: int | None = Field(default=1)
    password: str = Field(example="aa")
    confirm_password:str = Field(example="aa")
    
@app.post("/user-management/emp-save")
async def empsave(empm: EmpSchemaIn):
    async with httpx.AsyncClient() as client:
        try:
            url = f"{MICROSERVICES['user_management']}/api/emp-save"
            payload = {"emp_name": "Atul","email": "atul9@yopmail.com","mobile": "000000","status": 1,"password": "aa","confirm_password": "aa"}
            response = await client.post('http://microhubusermanagementcontainer:8000/api/a1',json=payload, timeout=None)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "Microservice is not reachable"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Microservice error: {exc.response.status_code}"}

@app.post("/user-management/a1")
async def a1():
    async with httpx.AsyncClient() as client:
        try:
            url = f"{MICROSERVICES['user_management']}/api/emp-save"
            reqjson = {"emp_name": "Atul","email": "atul9@yopmail.com","mobile": "000000","status": 1,"password": "aa","confirm_password": "aa"}
            response = await client.get('http://microhubusermanagementcontainer:8000/api/a1', timeout=None)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "Microservice is not reachable"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Microservice error: {exc.response.status_code}"}

@app.post("/user-management/posta1")
async def a1():
    async with httpx.AsyncClient() as client:
        try:
            url = f"{MICROSERVICES['user_management']}/api/emp-save"
            payload = {"emp_name": "Atul","email": "atul9@yopmail.com","mobile": "000000","status": 1,"password": "aa","confirm_password": "aa"}
            response = await client.post('http://microhubusermanagementcontainer:8000/api/posta1', timeout=None)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "Microservice is not reachable"}
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
