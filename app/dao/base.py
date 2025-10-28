from sqlalchemy import insert, select, delete
from sqlalchemy.exc import SQLAlchemyError

from app.database import database


class BaseDAO:
    model = None

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


# TODO: Добавить базовый метод для обновления данных в таблице
