import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Route Finder"
    PROJECT_VERSION: str = "1.0"

    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.environ.get("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    DB_URL = (f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
              f"@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}")
    

settings = Settings()