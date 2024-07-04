from pathlib import Path

from pydantic import BaseModel
from sqlalchemy.orm import declarative_base

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"


class Settings(BaseModel):
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    # edcho: bool = False
    db_echo: bool = True


settings = Settings()
