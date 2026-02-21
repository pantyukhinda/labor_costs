from pydantic import BaseModel, EmailStr, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

# CONFIG_DIR = Path(__file__).resolve().parent
# ENV_FILE =


class DatabaseConfig(BaseModel):
    host: str
    name: str
    port: int
    user: str
    password: SecretStr

    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def async_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            database=self.name,
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password.get_secret_value(),
        )


class RunConfig(BaseModel):
    title: str
    host: str
    port: int
    reload: bool


class AuthenticateConfig(BaseModel):
    key: str
    algorithm: str


class PgAdminConfig(BaseModel):
    email: EmailStr
    password: SecretStr
    port: int


class AdminUserConfig(BaseModel):
    """Service superuser (id=0) created at bootstrap"""

    email: EmailStr
    password: SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_prefix="APP_CONFIG__",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_file=(
            "env.template",
            ".env",
        ),
    )
    db: DatabaseConfig
    run: RunConfig
    auth: AuthenticateConfig
    pgadmin: PgAdminConfig
    admin: AdminUserConfig


settings = Settings()
