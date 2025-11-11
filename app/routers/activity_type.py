from typing import List
from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemes.activity_type import (
    ActivityTypeCreate,
    ActivityTypeUpdate,
    ActivityTypeResponse,
)
from app.dao.activity_type import ActivityTypeDAO


router = APIRouter(prefix="/activity_type", tags=["activity_type"])


@router.post("/add", response_model=ActivityTypeResponse)
async def create_activity_type(activity_type: ActivityTypeCreate):
    """Create new activity type"""
    new_activity_type = await ActivityTypeDAO.add(**activity_type.model_dump())
    return ActivityTypeResponse.model_validate(new_activity_type)


@router.get("/all", response_model=List[ActivityTypeResponse])
async def get_all_activity_types():
    """Get all activity types"""
    all_activity_types = await ActivityTypeDAO.find_all()
    if not all_activity_types:
        raise HTTPException(status_code=404, detail="No activity types found")
    return [
        ActivityTypeResponse.model_validate(a_type) for a_type in all_activity_types
    ]


@router.get("/{activity_type_id}", response_model=ActivityTypeResponse)
async def get_activity_type_by_id(activity_type_id: int):
    """Get activity type by id"""

    activity_type = await ActivityTypeDAO.find_one_or_none(id=activity_type_id)
    if not activity_type:
        raise HTTPException(status_code=404, detail="No activity type found")
    return ActivityTypeResponse.model_validate(activity_type)


@router.put("/{activity_type_id}", response_model=ActivityTypeResponse)
async def update_activity_type(
    activity_type_id: int, activity_type_update: ActivityTypeUpdate
):
    """Update activity type"""
    update_a_type = await ActivityTypeDAO.update(
        id=activity_type_id, **activity_type_update.model_dump()
    )
    if not update_a_type:
        raise HTTPException(status_code=404, detail="Activity type not found")

    return ActivityTypeResponse.model_validate(update_a_type)


@router.delete("/{activity_type_id}", response_model=ActivityTypeResponse)
async def delete_activity_type(activity_type_id: int):
    """Delete activity type"""
    del_activity_type = await ActivityTypeDAO.delete(id=activity_type_id)
    if not del_activity_type:
        raise HTTPException(status_code=404, detail="Activity type not found")
    return ActivityTypeResponse.model_validate(del_activity_type)
