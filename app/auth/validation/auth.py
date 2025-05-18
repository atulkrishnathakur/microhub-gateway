from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from typing import List
from app.exception.custom_exception import CustomException
from fastapi import status,Depends
from typing_extensions import Annotated

class AuthCredentialIn(BaseModel):
    email:str = Field(example="hhjjj@yyeyeyeywww.com")
    password: str = Field(example="aa")
