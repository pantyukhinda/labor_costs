from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from config import settings


class DataBase:
    """Provides access to the database"""

    def __init__(self):
        self.engine = create_async_engine(
            url=settings.db.async_url,
            echo=settings.db.echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


database = DataBase()
