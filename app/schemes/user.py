from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    patronymic: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    division_id: Optional[int] = None

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
