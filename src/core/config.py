from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = Field(alias="APP_ENV")
    app_name: str = Field(alias="APP_NAME")
    api_url: str = Field(
        default="http://127.0.0.1:8000/api/v1/",
        alias="API_URL",
    )
    app_host: str = Field(alias="APP_HOST")
    app_port: str = Field(alias="APP_PORT")
    log_level: str = Field(alias="LOG_LEVEL")
    streamlit_port: str = Field(alias="STREAMLIT_PORT")
    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()