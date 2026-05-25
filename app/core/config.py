from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "api-teste-engine"
    app_version: str = "0.1.0"
    debug : bool = True

    auth_key : str = "DEVELOPMENT-KEY-TEST"
    encode : str = "HS256"
    token_expire : int = 10

    class Config:
        env_file = ".env"

settings = Settings()