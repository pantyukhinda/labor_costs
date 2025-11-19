from typing import List
from fastapi import APIRouter, HTTPException, status

from app.schemes.division import (
    DivisionCreate,
    DivisionUpdate,
    DivisionResponse,
)
from app.dao.division import DivisionDAO


router = APIRouter(prefix="/division", tags=["division"])


@router.post(
    "/add",
    response_model=DivisionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_division(division: DivisionCreate):
    """Create new division"""
    new_division = await DivisionDAO.add(**division.model_dump())
    return DivisionResponse.model_validate(new_division)


@router.get("/all", response_model=List[DivisionResponse])
async def get_all_divisions():
    """Get all divisions"""
    all_divisions = await DivisionDAO.find_all()
    if not all_divisions:
        raise HTTPException(status_code=404, detail="No divisions found")
    return [DivisionResponse.model_validate(a_type) for a_type in all_divisions]


# TODO:


@router.get("/{division_id}", response_model=DivisionResponse)
async def get_division_by_id(division_id: int):
    """Get division by id"""

    division = await DivisionDAO.find_one_or_none(id=division_id)
    if not division:
        raise HTTPException(status_code=404, detail="No division found")
    return DivisionResponse.model_validate(division)


@router.put("/{division_id}", response_model=DivisionResponse)
async def update_division(division_id: int, division_update: DivisionUpdate):
    """Update division"""
    update_a_type = await DivisionDAO.update(
        id=division_id, **division_update.model_dump()
    )
    if not update_a_type:
        raise HTTPException(status_code=404, detail="Division not found")

    return DivisionResponse.model_validate(update_a_type)


@router.delete("/{division_id}", response_model=DivisionResponse)
async def delete_division(division_id: int):
    """Delete division"""
    del_division = await DivisionDAO.delete(id=division_id)
    if not del_division:
        raise HTTPException(status_code=404, detail="Division not found")
    return DivisionResponse.model_validate(del_division)
