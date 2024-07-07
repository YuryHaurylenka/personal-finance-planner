import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent.parent

load_dotenv()


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class Settings(BaseModel):
    api_v1_prefix: str = "/api/v1"
    db_url: str = os.getenv("DB_URL")
    # echo: bool = False
    db_echo: bool = True

    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
