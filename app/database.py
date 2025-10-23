from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.config.config import settings

# It's necessary to comment out when alembic migrations are generated
from app.models import *


class DataBase:
    """Provides access to the database"""

    def __init__(self):
        self.engine = create_async_engine(
            url=str(settings.DATABASE_URL),
            echo=settings.DB_ECHO,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


database = DataBase()
