from fastapi import FastAPI
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from typing import List
import httpx

app = FastAPI()
    
@app.post("/mytest")
async def test():
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post('http://microhub-user-management:8000/a1', json={"abc":123},headers={"Content-Type": "application/json"}, timeout=None)
            res.raise_for_status()  # HTTP error raise karega agar status code 4xx/5xx ho
            return res.json()
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")



class EmpSchemaIn(BaseModel):
    emp_name: str = Field(example="Atul")
    email: EmailStr = Field(example="atul@comsysapp.com")
    mobile: str | None = Field(example="000000")
    status: int | None = Field(default=1)
    password: str = Field(example="aa")
    confirm_password:str = Field(example="aa")
    
@app.post("/mytest2")
async def mytest2(empm: EmpSchemaIn):
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post('http://microhub-user-management:8000/a2',json={"empm":empm.dict()},headers={"Content-Type": "application/json"}, timeout=None) # 422 Unprocessable Entity if json format is not same as user magangement service
            res.raise_for_status()  # HTTP error raise karega agar status code 4xx/5xx ho
            return res.json()
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")


@app.post("/mytest3")
async def mytest3(empm: EmpSchemaIn):
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post('http://microhub-user-management:8000/a3',json=empm.dict(),headers={"Content-Type": "application/json"}, timeout=None) # 422 Unprocessable Entity if json format is not same as user magangement service
            res.raise_for_status()  # HTTP error raise karega agar status code 4xx/5xx ho
            return res.json()
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
