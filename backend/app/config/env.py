from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    PROJECT_NAME: str
    API_VERSION: str
    TOKEN_ENDPOINT: str = "http://auth-portfolio:8070/token"
    TOKEN_VALIDATE_ENDPOINT: str = "http://auth-portfolio:8070/token/validate"


    # admin
    DEFAULT_ADMIN_LAST_NAME: str = "Default"
    DEFAULT_ADMIN_FIRST_NAME: str = "Admin"
    DEFAULT_ADMIN_EMAIL: str = "admin@example.com"
    DEFAULT_ADMIN_PASSWORD: str = "Admin@12345"
    
    KEY_INIT: str = "494c157c-0880-461f-826a-3a867cfa128a"


settings = Settings()

