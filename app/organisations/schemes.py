from typing import Optional
from pydantic import BaseModel


class OrganisationBase(BaseModel):
    name: Optional[str] = None


class OrganisationCreate(OrganisationBase):
    pass


class OrganisationUpdate(OrganisationBase):
    pass


class OrganisationResponse(OrganisationBase):
    id: int

    class Config:
        from_attributes = True
