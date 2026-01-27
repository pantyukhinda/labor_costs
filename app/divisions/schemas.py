from typing import Optional
from pydantic import BaseModel


class DivisionsLevels(BaseModel):
    level_01: str = ""
    level_02: str = ""
    level_03: str = ""
    level_04: str = ""


class DivisionBase(BaseModel):
    division: Optional[DivisionsLevels]
    organization_id: int

    class Config:
        from_attributes = True


class DivisionCreate(DivisionBase):
    pass


class DivisionUpdate(DivisionBase):
    pass


class DivisionResponse(DivisionBase):
    id: int
