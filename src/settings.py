import os
from functools import lru_cache

from pydantic import BaseSettings

from src.models.base import DataAccess


class SettingsEnviron(BaseSettings):
    BASE_DIR: str = os.path.dirname(os.path.dirname(__file__))
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return SettingsEnviron()


database = DataAccess(
    url_connection=get_settings().DATABASE_URL,
    connect_args={"check_same_thread": False},
)
