from fastapi import FastAPI
from faststream.kafka.fastapi import Logger
from pydantic import BaseModel

from .consumer import router, settings

class IncomingMessage(BaseModel):
    msg: str

received_messages = []

@router.subscriber(settings.KAFKA_TOPIK_NAME)
async def handle_message(msg: IncomingMessage, logger: Logger):
    logger.info(f"[Kafka] Received: {msg}")
    received_messages.append(msg)

@router.get("/messages")
async def get_messages() -> dict[str, list[IncomingMessage]]:
    return {"messages": received_messages[-10:]}

app = FastAPI()
app.include_router(router)