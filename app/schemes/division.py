# Pydantic схемы
from pydantic import BaseModel
from typing import Optional, Any


class DivisionBase(BaseModel):
    division: Optional[Any]
    organization_id: Optional[int]

    class Config:
        from_attributes = True


class DivisionCreate(DivisionBase):
    pass


class DivisionUpdate(DivisionBase):
    pass


class DivisionResponse(DivisionBase):
    id: int
