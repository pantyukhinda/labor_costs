from asyncio import sleep
from sqlalchemy import insert, select, delete
from sqlalchemy.exc import SQLAlchemyError

from app.database import database


class BaseDAO:
    """Implements basic CRUD operations"""

    model = None

    @classmethod
    async def add(cls, **data):
        query = (
            insert(cls.model)
            .values(**data)
            .returning(
                cls.model.__table__.columns,
            )
        )
        async with database.session_factory() as session:
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with database.session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with database.session_factory() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def update(cls, id: int, **data):
        async with database.session_factory() as session:
            query = select(cls.model).where(cls.model.__table__.columns.id == id)
            result = await session.execute(query)
            data_update = result.scalars().first()
            if data_update:
                for field, value in data.items():
                    setattr(data_update, field, value)

                # session.add(data_update)
                await session.commit()
                await session.refresh(data_update)
                return data_update
            return None

    @classmethod
    async def delete(cls, **filter_by):
        async with database.session_factory() as session:
            query = (
                delete(cls.model)
                .filter_by(**filter_by)
                .returning(cls.model.__table__.columns)
            )
            result = await session.execute(query)
            await session.commit()
            return result.mappings().one_or_none()
