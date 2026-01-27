from typing import List
from fastapi import APIRouter, HTTPException, Request, Response, status

from app.auth.auth import auth_verifier
from app.schemes.user import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
)
from app.dao.user import UserDAO


router = APIRouter(prefix="/user", tags=["user & auth"])


# @router.get("/debug")
# async def get_debug_information(request: Request):
#     """Get debug information"""
#     return {
#         "user": request.cookies,
#         "headers": request.headers,
#         "base_url": request.base_url,
#         "client": request.client,
#     }


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
    access_token = auth_verifier.create_access_token({"sub": str(user.id)})
    response.set_cookie("labor_costs_access_token", access_token, httponly=True)


@router.get("/all", response_model=List[UserResponse])
async def get_all_users():
    """Get all users"""
    all_users = await UserDAO.find_all()
    if not all_users:
        raise HTTPException(status_code=404, detail="No users found")
    return [UserResponse.model_validate(a_type) for a_type in all_users]


@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int):
    """Get user by id"""

    user = await UserDAO.find_one_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No user found")
    return UserResponse.model_validate(user)


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate):
    """Update user"""
    update_a_type = await UserDAO.update(id=user_id, **user_update.model_dump())
    if not update_a_type:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse.model_validate(update_a_type)


@router.patch("/{user_id}", response_model=UserResponse)
async def partial_update_user(user_id: int, user_update: UserUpdate):
    """Partial update user"""
    update_a_type = await UserDAO.update(
        id=user_id, **user_update.model_dump(exclude_unset=True)
    )
    if not update_a_type:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse.model_validate(update_a_type)


@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    """Delete user"""
    del_user = await UserDAO.delete(id=user_id)
    if not del_user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(del_user)
