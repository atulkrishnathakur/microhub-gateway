from fastapi import APIRouter,Depends,status,File,UploadFile,BackgroundTasks
from fastapi.responses import JSONResponse, ORJSONResponse
import os
from typing import Annotated
from datetime import datetime
from typing import Dict
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
import httpx
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, status, Request, BackgroundTasks
from fastapi import APIRouter
from fastapi.responses import JSONResponse, ORJSONResponse
from app.auth.validation.auth import (AuthCredentialIn)
from app.utils.make_request import make_request
from app.utils.url_utils import get_api_url
from app.config.services_urls import services_base_urls,user_management_endpoint
from app.config.headers import service_req_header
from app.config.request_methods import req_method

router = APIRouter()

@router.post("/login",name="login")
async def login(credentials:AuthCredentialIn):
    try:
        baseurl = services_base_urls["user_management"]
        endpoint = user_management_endpoint["get_emp_by_email"]
        service_url = get_api_url(base_url=baseurl, endpoint=endpoint)

        apidata = await make_request(
			method=req_method.post,
			url=service_url,
			jsondata=credentials.dict(),
			headers=service_req_header
		)
        apiJsonData = apidata
        apiStatusCode = apiJsonData['status_code']
        response = JSONResponse(content=apiJsonData,status_code=apiStatusCode)
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
