from __future__ import annotations

from functools import lru_cache
from typing import List

from dotenv import find_dotenv
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, validator


class _Settings(BaseSettings):
    class Config:
        env_file_encoding = "utf-8"


class Config(_Settings):
    # Debug
    TEST_MODE: bool

    # Backend
    BACKEND_PROJECT_NAME: str
    BACKEND_API_V1_PREFIX: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    ## Backend VK settings
    BACKEND_VK_SECRET_KEY: str
    BACKEND_VK_SERVICE_KEY: str

    ## Telegram bot settings
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str

    ## Sentry settings
    BACKEND_SENTRY_DSN: HttpUrl

    # Postgres
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


@lru_cache()
def get_config(env_file: str = ".env") -> Config:
    return Config(_env_file=find_dotenv(env_file))
