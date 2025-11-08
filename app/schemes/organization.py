from typing import Optional
from pydantic import BaseModel


class OrganizationBase(BaseModel):
    name: Optional[str] = None

    class Config:
        from_attributes = True


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(OrganizationBase):
    pass


class OrganizationResponse(OrganizationBase):
    id: int
