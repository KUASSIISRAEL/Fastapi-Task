import os
from typing import Any, Callable, Dict, List, Optional

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path=".env")

__all__ = ["settings"]


class Settings(BaseSettings):
    PROJECT_NAME: str = "Task simple project"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.environ.get("SECRET_KEY")

    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is not configured")

    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")

    POSTGRES_IS_READY: bool = all(
        [
            POSTGRES_DB,
            POSTGRES_USER,
            POSTGRES_PORT,
            POSTGRES_HOST,
            POSTGRES_PASSWORD,
        ]
    )

    if not POSTGRES_IS_READY:
        raise ValueError("POSTGRES database is not ready")

    # SQLALCHEMY_DATABASE
    SQLALCHEMY_DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    # CORS configurations
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://0.0.0.0:8080",
    ]


settings: Callable = Settings()
