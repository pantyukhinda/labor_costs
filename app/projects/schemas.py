from typing import Optional
from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    completed: bool = False
    organization_id: Optional[int] = None

    class Config:
        from_attributes = True


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int
