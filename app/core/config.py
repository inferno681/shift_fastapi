from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_TITLE: str
    APP_DESCRIPTION: str
    SECRET: SecretStr
    DB_HOST: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_NAME: str
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


config = Settings()
