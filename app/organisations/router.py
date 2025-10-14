from typing import List
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organisation import Organisation
from app.organisations.schemes import (
    OrganisationCreate,
    OrganisationUpdate,
    OrganisationResponse,
)
from app.database import async_session_maker

router = APIRouter(prefix="/organisations", tags=["organisations"])


@router.get("")
async def get_organisations():
    async with async_session_maker() as session:
        query = select(Organisation)
        result = await session.execute(query)
        print(result.scalars().all())


# @router.post("/", response_model=OrganisationResponse)
# async def create_organisation(organisation: OrganisationCreate):
#     """Создание новой организации"""
#     async with async_session_maker() as session:
#         db_organisation = Organisation(**organisation.model_dump())
#         session.add(db_organisation)
#         await session.commit()
#         await session.refresh(db_organisation)
#         return OrganisationResponse.model_validate(db_organisation)


# @router.get("/", response_model=List[OrganisationResponse])
# async def get_organisations():
#     """Получение списка всех организаций"""
#     async with async_session_maker() as session:
#         query = select(Organisation).order_by(Organisation.id)
#         result = await session.execute(query)
#         organisations = result.scalars().all()
#         return [OrganisationResponse.model_validate(org) for org in organisations]


# @router.get("/{organisation_id}", response_model=OrganisationResponse)
# async def get_organisation(organisation_id: int):
#     """Получение организации по ID"""
#     async with async_session_maker() as session:
#         query = select(Organisation).where(Organisation.id == organisation_id)
#         result = await session.execute(query)
#         organisation = result.scalar_one_or_none()

#         if not organisation:
#             raise HTTPException(status_code=404, detail="Organisation not found")
#         return OrganisationResponse.model_validate(organisation)


# @router.put("/{organisation_id}", response_model=OrganisationResponse)
# async def update_organisation(
#     organisation_id: int, organisation_update: OrganisationUpdate
# ):
#     """Обновление организации"""
#     async with async_session_maker() as session:
#         query = select(Organisation).where(Organisation.id == organisation_id)
#         result = await session.execute(query)
#         db_organisation = result.scalar_one_or_none()

#         if not db_organisation:
#             raise HTTPException(status_code=404, detail="Organisation not found")

#         update_data = organisation_update.model_dump(exclude_unset=True)
#         for field, value in update_data.items():
#             setattr(db_organisation, field, value)

#         session.add(db_organisation)
#         await session.commit()
#         await session.refresh(db_organisation)
#         return OrganisationResponse.model_validate(db_organisation)


# @router.delete("/{organisation_id}")
# async def delete_organisation(organisation_id: int):
#     """Удаление организации"""
#     async with async_session_maker() as session:
#         query = select(Organisation).where(Organisation.id == organisation_id)
#         result = await session.execute(query)
#         db_organisation = result.scalar_one_or_none()

#         if not db_organisation:
#             raise HTTPException(status_code=404, detail="Organisation not found")

#         await session.delete(db_organisation)
#         await session.commit()
#         return {"message": "Organisation deleted successfully"}
