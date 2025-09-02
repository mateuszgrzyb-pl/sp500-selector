from pathlib import Path
from pydantic_settings import BaseSettings

ENV_FILE_PATH = Path(__file__).resolve().parent.parent.parent / ".env"


class Settings(BaseSettings):
    environment: str
    log_level: str
    data_lake_root_path: str
    model_artifact_path: str

    class Config:
        env_file = ENV_FILE_PATH if ENV_FILE_PATH.exists() else None
        env_file_encoding = "utf-8"


settings = Settings()
