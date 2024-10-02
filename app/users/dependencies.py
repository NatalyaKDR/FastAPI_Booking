import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from app.exceptions import (IncorrectTokenFormatException,
                            TokenAbsentException, TokenExpiredException,
                            UserException)
from app.users.dao import UsersDAO
from app.users.models import Users

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')


def get_token(request:Request):
    token=request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str=Depends(get_token)):
    try:
        payload=jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str=payload.get('exp')
    if (not expire) or (int(expire)<datetime.now(timezone.utc).timestamp()):
        raise TokenExpiredException
    user_id: str=payload.get('sub')
    if not user_id:
        raise UserException 
    user=await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserException 
    
    return user


#Роли
async def get_current_admin_user(current_user: Users=Depends(get_current_user)):
    # if current_user.role !="admin":
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return current_user
    