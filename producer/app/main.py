from fastapi import FastAPI
from pydantic import BaseModel

from .producer import router, settings

class IncomingMessage(BaseModel):
    msg: str

received_messages = []

@router.post("/send")
async def send(msg: IncomingMessage):
    await router.broker.publish(
        message=msg.msg,
        topic=settings.KAFKA_TOPIK_NAME,
    )
    return {"Message successfully sent"}

app = FastAPI()
app.include_router(router)