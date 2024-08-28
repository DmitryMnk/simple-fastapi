import os

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_v1_prefix:str = '/api/v1'
    DB_HOST: str = os.environ.get("POSTGRES_HOST")
    DB_PORT: int = os.environ.get("POSTGRES_PORT")
    DB_USER: str = os.environ.get("POSTGRES_USER")
    DB_PASS: str = os.environ.get("POSTGRES_PASSWORD")
    DB_NAME: str = os.environ.get("POSTGRES_DB")

    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()