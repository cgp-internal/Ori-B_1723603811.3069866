from typing import Dict, Optional
from pydantic import BaseSettings

class AppConfig(BaseSettings):
    database_url: str
    database_username: str
    database_password: str
    database_port: int
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
        case_sensitive = True

app_config: AppConfig = AppConfig()

def get_app_config() -> AppConfig:
    return app_config