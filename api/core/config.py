from __future__ import annotations
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    # loading envs 
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    # api configs
    API_NAME:str = "Production ready API for hate-speech-classifier model"
    API_VERSION:str = "0.1.0"

settings = Settings()