from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class for settings"""

    # Postgresql
    POSTGRES_DB: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    # pgAdmin
    PGADMIN_DEFAULT_EMAIL: str
    PGADMIN_DEFAULT_PASSWORD: str
    PGADMIN_PORT: int
    # Common
    HOST: str

    @property
    def DATABASE_URL(self):
        """Creating a database connection string"""
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
