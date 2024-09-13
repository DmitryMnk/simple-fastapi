import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str = os.environ.get("RESET_PASSWORD_TOKEN_SECRET")
    verification_token_secret: str = os.environ.get("VERIFICATION_TOKEN_SECRET")


class Settings(BaseSettings):
    api_v1_prefix:str = '/api/v1'

    DB_HOST: str = os.environ.get("POSTGRES_HOST")
    DB_PORT: int = os.environ.get("POSTGRES_PORT")
    DB_USER: str = os.environ.get("POSTGRES_USER")
    DB_PASS: str = os.environ.get("POSTGRES_PASSWORD")
    DB_NAME: str = os.environ.get("POSTGRES_DB")
    PRIVATE_KEY: str = os.environ.get("PRIVATE_KEY")
    PUBLIC_KEY: str = os.environ.get("PUBLIC_KEY")
    algorithm: str = 'RS256'
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30
    db_url: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    access_token: AccessToken = AccessToken()

settings = Settings()