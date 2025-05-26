from typing import Annotated
from fastapi import Depends, status
import jwt
from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, Request
from app.utils.hashing import HashData
from app.config.message import auth_message
from app.auth.validation.auth import TokenData
from app.utils.httpbearer import get_api_token
from app.config.redis_session import RedisSession
from app.auth.validation.auth import EmpSchemaOut
from app.utils.token import blacklist
from app.config.loadenv import envconst

redisSession = RedisSession()

async def getCurrentEmp(token: Annotated[str, Depends(get_api_token)]):
    if token in blacklist:
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=False,
            message=auth_message.LOGIN_REQUIRED,
            data=[]
        )
    else:
        payload = jwt.decode(token, envconst.SECRET_KEY, algorithms=[envconst.ALGORITHM])
        email: str = payload.get("email")
        token_data = TokenData(email=email)
        currentEmp = redisSession.get_session("loginuserdata")
        return currentEmp

async def getCurrentActiveEmp(
    currentEmp: Annotated[EmpSchemaOut, Depends(getCurrentEmp)],
):
    if(currentEmp["status"] == 0):
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=False,
            message=auth_message.LOGIN_REQUIRED,
            data=[]
        )
    return currentEmp
