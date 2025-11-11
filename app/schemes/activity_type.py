from typing import Optional
from pydantic import BaseModel


class ActivityTypeBase(BaseModel):
    name: Optional[str] = None
    organization_id: Optional[int] = None
    visible: Optional[bool] = None

    class Config:
        from_attributes = True


class ActivityTypeCreate(ActivityTypeBase):
    pass


class ActivityTypeUpdate(ActivityTypeBase):
    pass


class ActivityTypeResponse(ActivityTypeBase):
    id: int
