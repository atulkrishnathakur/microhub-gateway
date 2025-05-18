from fastapi import APIRouter,Depends,status,File,UploadFile,BackgroundTasks
from fastapi.responses import JSONResponse, ORJSONResponse
import os
from typing import Annotated
from datetime import datetime
from typing import Dict
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
import httpx
from app.services.user_management.validation.emp_m import EmpSchemaIn
from app.utils.make_request import make_request
from app.utils.url_utils import get_api_url
from app.config.services_urls import services_base_urls,user_management_endpoint
from app.config.headers import service_req_header
from app.config.request_methods import req_method

router = APIRouter()

@router.post("/emp-m-save",name="empmsave")
async def empSave(empm: EmpSchemaIn):
    async with httpx.AsyncClient() as client:
        try:
            # 422 Unprocessable Entity if json format is not same as user magangement service
            # apidata = await client.post('http://microhub-user-management:8000/emp-m-save',json=empm.dict(),headers={"Content-Type": "application/json"}, timeout=None)

            #baseurl = services_base_urls["user_management"]
            #endpoint = user_management_endpoint["get_user"]
            #service_url = get_api_url(base_url=baseurl, endpoint=endpoint, query_params={"a": 10, "b": 20}, user_id=123, ss="xyz")
            # url will be "http://microhub-user-management:8000/users/123/abc/xyz?a=10&b=20"
            baseurl = services_base_urls["user_management"]
            endpoint = user_management_endpoint["emp_m_save"]
            service_url = get_api_url(base_url=baseurl, endpoint=endpoint)

            apidata = await make_request(
                method=req_method.post,
                url=service_url,
                jsondata=empm.dict(),
                headers=service_req_header
            )
            apiJsonData = apidata
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
            