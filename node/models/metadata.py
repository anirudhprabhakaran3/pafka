from pydantic import BaseModel

class NodeMetadata(BaseModel):
    identifier: str
    broker: str
    host: str
    port: int
