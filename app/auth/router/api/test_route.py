from fastapi import APIRouter,Depends,status,HTTPException,Path,Depends
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
#from app.validation.emp_m import EmpSchemaOut
from fastapi.responses import JSONResponse, ORJSONResponse
from app.exception.custom_exception import CustomException
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from app.config.logconfig import loglogger
from app.utils.auth import getCurrentActiveEmp
from app.auth.validation.auth import EmpSchemaOut
router = APIRouter()

@router.get(
    "/test-auth",
    name="apitest"
    )
def testuser(
    current_user: Annotated[EmpSchemaOut, Depends(getCurrentActiveEmp)],
    ):
    try:
        return current_user
    except Exception as e:
        http_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        data = {
            "status_code": http_status_code,
            "status":False,
            "message":e.errors()
        }
        response = JSONResponse(content=data,status_code=http_status_code)
        loglogger.debug("RESPONSE:"+str(data))
        return response
