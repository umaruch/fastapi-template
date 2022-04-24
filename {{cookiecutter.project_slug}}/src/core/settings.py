import pathlib
from typing import Dict, Any
from pydantic import BaseSettings, PostgresDsn, validator

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"


class DatabaseSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_HOST: str
    POSTGRES_NAME: str

    CONNECTION_URL: PostgresDsn|None = None

    @validator("CONNECTION_URL", pre=True)
    def get_db_connection_url(cls, v, values: Dict[str, Any]) -> PostgresDsn:
        if isinstance(v, PostgresDsn):
            return v
        
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASS"),
            host=values.get("POSTGRES_HOST"),
            path=f"/{values.get('POSTGRES_NAME')}"
        )

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"


class RedisSettings(BaseSettings):
    REDIS_HOST: str = "redis://localhost"
    REDIS_PASSWORD: str = ""

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"


class MailSettings(BaseSettings):
    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"


class ApplicationSettings(BaseSettings):
    APP_NAME: str = "default_application"
    API_URL: str = "/api/v1"
    DOCS_URL: str = "/docs"

    DEBUG: bool = False
    SECRET_KEY: str = "secret-key"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60*5

    # Конфиги подключаемых модулей
    database: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    mail: MailSettings = MailSettings()

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
