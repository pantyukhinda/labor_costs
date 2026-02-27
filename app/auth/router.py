from typing import List
from fastapi import APIRouter, HTTPException, Response, status

from users.schemas import (
    UserCreate,
    UserLogin,
    UserResponse,
)
from users.dao import UserDAO
from .auth_2 import auth_verifier


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
