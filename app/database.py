from config.config import load_db_config, DatabaseConfig
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

db_config: DatabaseConfig = load_db_config(".env")

DATABASE_URL = str(db_config.postgres_url)

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
