from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    postgres_db: str  # Название базы данных
    host: str  # имя или ip адрес устройства
    postgres_port: int  # порт базы данных
    postgres_user: str  # Username пользователя базы данных
    postgres_password: str  # Пароль к базе данных

    @property
    def postgres_url(self):  # Строка подключения к базе данных
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.host}:{self.postgres_port}/{self.postgres_db}",
        )


def load_db_config(path: str | None = None) -> DatabaseConfig:
    """Служит для управления конфигурацией подключения к БД postgresql"""
    env: Env = Env()
    env.read_env(path)

    return DatabaseConfig(
        postgres_db=env("POSTGRES_DB"),
        host=env("HOST"),
        postgres_port=env("POSTGRES_PORT"),
        postgres_user=env("POSTGRES_USER"),
        postgres_password=env("POSTGRES_PASSWORD"),
    )
