from pathlib import Path
from typing import Union

from dotenv import load_dotenv
from pydantic import BaseSettings, ConstrainedStr, Field, HttpUrl, PostgresDsn, constr

load_dotenv()

EmptyString: ConstrainedStr = constr(max_length=0)


class Settings(BaseSettings):
    ROOT_DIR = Path(__file__).parent.parent.parent

    environment: str = Field("dev", env="ENV")
    service_name: str = Field("local-user-service", env="SERVICE_NAME")
    service_port: int = Field(1881, env="SERVICE_PORT")
    pg_dsn: PostgresDsn = "postgresql://postgres:postgres@localhost:15455/user_service"


    class Config:
        fields = {
            "pg_dsn": {"env": "SERVICE_DATABASE_URL"},
        }
