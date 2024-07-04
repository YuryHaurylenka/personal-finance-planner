import os

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
    api_v1_prefix: str = "/api/v1"
    db_url: str = os.getenv("DB_URL")
    # echo: bool = False
    db_echo: bool = True


settings = Settings()
