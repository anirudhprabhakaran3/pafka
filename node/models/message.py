from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Message(BaseModel):
    timestamp: datetime
    topic: str
    client: str
    position: Optional[int] = None
    payload: dict