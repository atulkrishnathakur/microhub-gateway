from typing import Annotated
from fastapi import Depends, status
import jwt
from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, Request
from app.utils.hashing import HashData
from app.config.message import auth_message
from app.validation.auth import TokenData
from app.utils.httpbearer import get_api_token

async def getCurrentEmp(token: Annotated[str, Depends(get_api_token)], db: Annotated[Session, Depends(get_db)]):
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
        currentEmp = get_emp_for_login(db, email=token_data.email)
        return currentEmp

async def getCurrentActiveEmp(
    currentEmp: Annotated[EmpSchemaOut, Depends(getCurrentEmp)],
):
    if(currentEmp.status == 0):
        raise CustomException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            status=False,
            message=auth_message.LOGIN_REQUIRED,
            data=[]
        )
    return currentEmp