from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    last_name: str
    first_name: str
    patronymic: Optional[str] = None
    email: EmailStr
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
