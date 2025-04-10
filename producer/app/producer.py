import ssl

from faststream.security import SASLPlaintext
from faststream.kafka.fastapi import KafkaRouter

from app.config import Settings

settings = Settings.from_os()

ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(cafile=settings.KAFKA_CERT_PATH)

security = SASLPlaintext(
    username=settings.KAFKA_USER,
    password=settings.KAFKA_PASS,
    ssl_context=ssl_context,
    use_ssl=True,
)

router = KafkaRouter(
    settings.KAFKA_HOST,
    security=security,
)