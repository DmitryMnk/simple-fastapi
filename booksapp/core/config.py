import os

from pydantic_settings import BaseSettings

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
    db_url: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


settings = Settings()