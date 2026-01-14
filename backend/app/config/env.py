from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env.backend", env_file_encoding="utf-8")

    DATABASE_URL: str
    SECRET_KEY: str
    PROJECT_NAME: str
    API_VERSION: str

    # container d'auth
    TOKEN_ENDPOINT: str
    TOKEN_VALIDATE_ENDPOINT: str 


    # admin
    DEFAULT_ADMIN_LAST_NAME: str
    DEFAULT_ADMIN_FIRST_NAME: str
    DEFAULT_ADMIN_EMAIL: str
    DEFAULT_ADMIN_PASSWORD: str 
    
    KEY_INIT: str
    SERVER_MEDIA: str = "http://localhost:8071"
    AUTO_SETUP: bool = True

    GITHUB_API_URL: str="https://api.github.com"
    GITHUB_TOKEN: str
    GITHUB_USER: str


settings = Settings()

