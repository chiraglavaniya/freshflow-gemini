from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FreshFlow"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    data_gov_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    default_limit: int = 120
    cors_origins: list[str] = Field(default_factory=lambda: ["*"])

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
