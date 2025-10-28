from typing import List
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Organization
from app.schemes.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)
from app.dao.organization import OrganizationDAO


router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("/all", response_model=List[OrganizationResponse])
async def get_all_organizations():
    """Get all organizations"""
    all_organizations = await OrganizationDAO.find_all()
    if not all_organizations:
        raise HTTPException(status_code=404, detail="No organizations found")
    return [OrganizationResponse.model_validate(org) for org in all_organizations]


# @router.get("/nodao/{organization_id}", response_model=List[OrganizationResponse])
# async def get_organization_by_id(organization_id: int):
#     """Get organization by id"""
#     organization = await OrganizationDAO.find_organization_by_id(
#         organization_id=organization_id
#     )
#     if not organization:
#         raise HTTPException(status_code=404, detail="No organization found")
#     return [OrganizationResponse.model_validate(org) for org in organization]


@router.get("/{organization_id}", response_model=OrganizationResponse)
async def get_organization_by_id(organization_id: int):
    """Get organization by id"""

    organization = await OrganizationDAO.find_one_or_none(id=organization_id)
    if not organization:
        raise HTTPException(status_code=404, detail="No organization found")
    return OrganizationResponse.model_validate(organization)


@router.post("/add", response_model=OrganizationResponse)
async def create_organization(organization: OrganizationCreate):
    """Create new organization"""
    new_organization = await OrganizationDAO.add(**organization.model_dump())
    return OrganizationResponse.model_validate(new_organization)


###
# TODO: Реализовать обновление организации через DAO


# @router.put("/{organization_id}", response_model=OrganizationResponse)
# async def update_organization(
#     organization_id: int, organization_update: OrganizationUpdate
# ):
#     """Обновление организации"""
#     async with async_session_maker() as session:
#         query = select(Organization).where(Organization.id == organization_id)
#         result = await session.execute(query)
#         db_organization = result.scalar_one_or_none()
#         if not db_organization:
#             raise HTTPException(status_code=404, detail="Organization not found")

#         update_data = organization_update.model_dump(exclude_unset=True)
#         for field, value in update_data.items():
#             setattr(db_organization, field, value)

#         session.add(db_organization)
#         await session.commit()
#         await session.refresh(db_organization)
#         return OrganizationResponse.model_validate(db_organization)


@router.delete("/{organization_id}", response_model=OrganizationResponse)
async def delete_organization(organization_id: int):
    """Delete organization"""
    del_organization = await OrganizationDAO.delete(id=organization_id)
    if not del_organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return OrganizationResponse.model_validate(del_organization)
