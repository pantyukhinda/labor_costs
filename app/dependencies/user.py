from datetime import datetime, timezone
from fastapi import Depends, HTTPException, Request, status
from jose import jwt, JWTError
from core.config import settings
from users.dao import UserDAO

# from users.models import User


def get_token(request: Request):
    """Get the token from the request"""
    # token = request.cookies.get("labor_costs_access_token")
    if not (token := request.cookies.get("labor_costs_access_token")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    print(token)
    print(type(token))
    return token


async def get_current_user(token: str = Depends(get_token)):
    """Get the current user"""
    try:
        payload = jwt.decode(
            token,
            key=settings.auth.key,
            algorithms=settings.auth.algorithm,
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid JWT token",
        )

    expire = payload.get("exp")
    if not expire or int(expire) < datetime.now(timezone.utc).timestamp():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT token is outdated",
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User id not found",
        )

    user = UserDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user
