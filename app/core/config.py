from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "api-teste-engine"
    app_version: str = "0.1.0"
    debug : bool = True

    class Config:
        env_file = ".env"

settings = Settings()