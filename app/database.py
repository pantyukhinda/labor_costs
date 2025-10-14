from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config.config import settings

# It's necessary to comment out when alembic migrations are generated
from app.models import *


DATABASE_URL = str(settings.DATABASE_URL)

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
