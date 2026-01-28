from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from core.config import settings

# It's necessary to comment out when alembic migrations are generated
from activity_types.models import ActivityType
from divisions.models import Division
from organizations.models import Organization
from projects.models import Project
from tasks.models import Task
from users.models import User


class DataBase:
    """Provides access to the database"""

    def __init__(self):
        self.engine = create_async_engine(
            url=str(settings.db.async_url),
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
