from datetime import datetime, timedelta, timezone
from typing import Annotated, Any, List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from core.config import settings
from users.schemas import (
    UserCreate,
    UserLogin,
    UserResponse,
)
from users.dao import UserDAO
from .auth_2 import auth_verifier
from .schemas import Token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(user: UserCreate):
    """Register new user"""
    existing_user = await UserDAO.find_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with the entered email already exists",
        )
    hashed_password = auth_verifier.get_password_hash(user.password)
    user.password = hashed_password
    new_user = await UserDAO.add(**user.model_dump())
    return UserResponse.model_validate(new_user)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(response: Response, user_data: UserLogin):
    """Login user"""
    user = await auth_verifier.authenticate_user(
        user_data.email,
        user_data.password,
    )
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = auth_verifier.create_access_token({"user_id": str(user.id)})
    response.set_cookie("labor_costs_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
)
async def logout_user(response: Response):
    """Logout user"""
    response.delete_cookie("labor_costs_access_token")
    return {"logout": True}


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await auth_verifier.authenticate_user(
        email=form_data.username,
        password=form_data.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.auth.access_token_expire_minutes,
    )
    access_token = auth_verifier.create_access_token(
        data={"user_id": user.id}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/")
async def read_users_me(
    current_user: Annotated[
        Any,
        Depends(auth_verifier.get_current_user),
    ],
):
    return current_user


# @router.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]
