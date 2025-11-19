from typing import Optional, Any, Dict
from pydantic import BaseModel


class DivisionsLevels(BaseModel):
    level_01: Optional[str]
    level_02: Optional[str]
    level_03: Optional[str]
    level_04: Optional[str]


class DivisionBase(BaseModel):
    division: Optional[DivisionsLevels]
    organization_id: Optional[int]

    class Config:
        from_attributes = True


class DivisionCreate(DivisionBase):
    pass


class DivisionUpdate(DivisionBase):
    pass


class DivisionResponse(DivisionBase):
    id: int
