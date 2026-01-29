from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    PROJECT_NAME: str
    API_VERSION: str

    # container d'auth
    AUTH_TOKEN_ENDPOINT: str
    AUTH_TOKEN_VALIDATE_ENDPOINT: str 


    # admin
    DEFAULT_ADMIN_LAST_NAME: str
    DEFAULT_ADMIN_FIRST_NAME: str
    DEFAULT_ADMIN_EMAIL: str
    DEFAULT_ADMIN_PASSWORD: str 
    
    KEY_INIT: str
    SERVER_MEDIA: str
    AUTO_SETUP: bool = True

    GITHUB_API_URL: str
    GITHUB_TOKEN: str
    GITHUB_USER: str
    
    GITLAB_API_URL: str
    GITLAB_TOKEN: str
    GITLAB_USER: str


settings = Settings()

