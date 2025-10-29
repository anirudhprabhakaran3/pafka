from pydantic import BaseModel

class BrokerMetadata(BaseModel):
    identifier: str
    port: int