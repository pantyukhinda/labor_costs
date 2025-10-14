from typing import Optional
from pydantic import BaseModel


class organizationBase(BaseModel):
    name: Optional[str] = None


class organizationCreate(organizationBase):
    pass


class organizationUpdate(organizationBase):
    pass


class organizationResponse(organizationBase):
    id: int

    class Config:
        from_attributes = True
