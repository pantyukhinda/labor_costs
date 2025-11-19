from typing import List
from fastapi import APIRouter, HTTPException, status

from app.schemes.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)
from app.dao.user import UserDAO


router = APIRouter(prefix="/user", tags=["user"])


# @router.post(
#     "/add",
#     response_model=UserResponse,
#     status_code=status.HTTP_201_CREATED,
# )
# async def create_user(user: UserCreate):
#     """Create new user"""
#     new_user = await UserDAO.add(**user.model_dump())
#     return UserResponse.model_validate(new_user)
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: UserCreate):
    """Create new user"""
    new_user = await UserDAO.add(**user.model_dump())
    return UserResponse.model_validate(new_user)


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
