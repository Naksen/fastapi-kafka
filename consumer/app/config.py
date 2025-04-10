import os
from pydantic import BaseModel

class Settings(BaseModel):
    KAFKA_HOST: str
    KAFKA_USER: str
    KAFKA_PASS: str
    KAFKA_CERT_PATH: str
    KAFKA_TOPIK_NAME: str

    @classmethod
    def from_os(cls) -> "Settings":
        return Settings(**os.environ)