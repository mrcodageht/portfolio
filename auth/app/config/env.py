from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    JWT_ALGORITHM: str 
    JWT_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    AUTH_PROJECT_NAME: str 
    AUTH_API_VERSION: str 

settings = Settings()

