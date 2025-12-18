from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET: str = "SECRET_TO_CHANGE"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    AUTH_PROJECT_NAME: str = "Default Project Name"
    AUTH_API_VERSION: str = "0.0.0"
    EXPIRE: int = 30

settings = Settings()

