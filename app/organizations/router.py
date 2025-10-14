from typing import List
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Organization
from app.organizations.schemes import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)
from app.database import async_session_maker

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("")
async def get_organizations():
    async with async_session_maker() as session:
        query = select(Organization)
        result = await session.execute(query)
        return result.scalars().all()


# @router.post("/", response_model=organizationResponse)
# async def create_organization(organization: organizationCreate):
#     """Создание новой организации"""
#     async with async_session_maker() as session:
#         db_organization = organization(**organization.model_dump())
#         session.add(db_organization)
#         await session.commit()
#         await session.refresh(db_organization)
#         return organizationResponse.model_validate(db_organization)


# @router.get("/", response_model=List[organizationResponse])
# async def get_organizations():
#     """Получение списка всех организаций"""
#     async with async_session_maker() as session:
#         query = select(organization).order_by(organization.id)
#         result = await session.execute(query)
#         organizations = result.scalars().all()
#         return [organizationResponse.model_validate(org) for org in organizations]


# @router.get("/{organization_id}", response_model=organizationResponse)
# async def get_organization(organization_id: int):
#     """Получение организации по ID"""
#     async with async_session_maker() as session:
#         query = select(organization).where(organization.id == organization_id)
#         result = await session.execute(query)
#         organization = result.scalar_one_or_none()

#         if not organization:
#             raise HTTPException(status_code=404, detail="organization not found")
#         return organizationResponse.model_validate(organization)


# @router.put("/{organization_id}", response_model=organizationResponse)
# async def update_organization(
#     organization_id: int, organization_update: organizationUpdate
# ):
#     """Обновление организации"""
#     async with async_session_maker() as session:
#         query = select(organization).where(organization.id == organization_id)
#         result = await session.execute(query)
#         db_organization = result.scalar_one_or_none()

#         if not db_organization:
#             raise HTTPException(status_code=404, detail="organization not found")

#         update_data = organization_update.model_dump(exclude_unset=True)
#         for field, value in update_data.items():
#             setattr(db_organization, field, value)

#         session.add(db_organization)
#         await session.commit()
#         await session.refresh(db_organization)
#         return organizationResponse.model_validate(db_organization)


# @router.delete("/{organization_id}")
# async def delete_organization(organization_id: int):
#     """Удаление организации"""
#     async with async_session_maker() as session:
#         query = select(organization).where(organization.id == organization_id)
#         result = await session.execute(query)
#         db_organization = result.scalar_one_or_none()

#         if not db_organization:
#             raise HTTPException(status_code=404, detail="organization not found")

#         await session.delete(db_organization)
#         await session.commit()
#         return {"message": "organization deleted successfully"}
