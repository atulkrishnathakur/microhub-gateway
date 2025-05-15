from fastapi import APIRouter,Depends,status,File,UploadFile,BackgroundTasks
from fastapi.responses import JSONResponse, ORJSONResponse
import os
from typing import Annotated
from datetime import datetime
from typing import Dict
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
import httpx
from app.services.user_management.validation.emp_m import EmpSchemaIn

router = APIRouter()

@router.post("/emp-m-save",name="empmsave")
async def empSave(empm: EmpSchemaIn):
    async with httpx.AsyncClient() as client:
        try:
            # 422 Unprocessable Entity if json format is not same as user magangement service
            apidata = await client.post('http://microhub-user-management:8000/emp-m-save',json=empm.dict(),headers={"Content-Type": "application/json"}, timeout=None)
            apiJsonData = apidata.json()
            apiStatusCode = apiJsonData['status_code']
            response = JSONResponse(content=apiJsonData,status_code=apiStatusCode) 
            return response
        except httpx.HTTPStatusError as hse:
            http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            data = {
                "status_code": http_status_code,
                "status":False,
                "message":"Type:"+str(type(hse))+", Message:"+str(hse)
            }
            response = JSONResponse(content=data,status_code=http_status_code)
            return response
        except Exception as e:
            http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            data = {
                "status_code": http_status_code,
                "status":False,
                "message":"Type:"+str(type(e))+", Message:"+str(e)
            }
            response = JSONResponse(content=data,status_code=http_status_code)
            return response
