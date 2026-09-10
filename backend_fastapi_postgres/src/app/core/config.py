# from pydantic import SettingsConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    DATABASE_URL: str
    APP_ENV: str
    DEBUG: bool

model_config = SettingsConfigDict(env_file=".env")

settings = Setting()