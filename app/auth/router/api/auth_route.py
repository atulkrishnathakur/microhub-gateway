from fastapi import APIRouter,Depends,status,File,UploadFile,BackgroundTasks
from fastapi.responses import JSONResponse, ORJSONResponse
import os
import sys
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
#from app.auth.validation.auth import (AuthCredentialIn)
from app.utils.make_request import make_request
from app.utils.url_utils import get_api_url
from app.config.services_urls import services_base_urls,user_management_endpoint
from app.config.headers import service_req_header
from app.config.request_methods import req_method
from app.utils.token import create_access_token
from app.config.loadenv import envconst
from app.config.message import auth_message
from app.auth.validation.auth import (AuthCredentialIn,AuthOut, Logout,Status422Response,Status400Response,Status401Response)
from app.config.redis_session import RedisSession

router = APIRouter()
redisSession = RedisSession()

@router.post(
    "/login",
    response_model=AuthOut,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": Status422Response},
        status.HTTP_400_BAD_REQUEST: {"model": Status400Response},
        status.HTTP_401_UNAUTHORIZED: {"model": Status401Response}
    },
    name="login"
    )
async def login(credentials:AuthCredentialIn):
    try:
        baseurl = services_base_urls["user_management"]
        endpoint = user_management_endpoint["verify_auth_credentials"]
        service_url = get_api_url(base_url=baseurl, endpoint=endpoint)
        authemp = await make_request(
			method=req_method.post,
			url=service_url,
			jsondata=credentials.dict(),
			headers=service_req_header
		)
        if authemp["status_code"] == status.HTTP_200_OK:
            authemail = authemp["data"][0]["email"]
            #print(apidata["data"][0]["email"],flush=True)
            access_token_expires = timedelta(minutes=int(envconst.ACCESS_TOKEN_EXPIRE_MINUTES))
            access_token = create_access_token(
                data={"email": authemail}, expires_delta=access_token_expires
            )
            http_status_code = authemp["status_code"]
            datalist = list()
            datadict = {}
            datadict['id'] = authemp["data"][0]["id"]
            datadict['emp_name'] = authemp["data"][0]["emp_name"]
            datadict['email'] = authemp["data"][0]["email"]
            datadict['status'] = authemp["data"][0]["status"]
            datadict['mobile'] = authemp["data"][0]["mobile"]
            
            loginuserdict = {}
            loginuserdict['id'] = authemp["data"][0]["id"]
            loginuserdict['emp_name'] = authemp["data"][0]["emp_name"]
            loginuserdict['email'] = authemp["data"][0]["email"]
            
            redisSession.set_session("loginuserdata", loginuserdict)

            datalist.append(datadict)
            response_dict = {
                "status_code": http_status_code,
                "status":True,
                "message":auth_message.AUTH_SUCCESSFULL,
                "token_type":envconst.TOKEN_TYPE,
                "access_token":access_token,
                "data":datalist
            }

            response_data = AuthOut(**response_dict) 
            response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
            return response
        else:
            response = JSONResponse(content=authemp,status_code=authemp['status_code'])
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
