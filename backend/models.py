from pydantic import BaseModel


class ChatRequest(BaseModel):
    name: str
    message: str