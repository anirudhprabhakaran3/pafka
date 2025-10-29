from pydantic import BaseModel

class NodeMetadata(BaseModel):
    identifier: str
    broker: str
    port: int