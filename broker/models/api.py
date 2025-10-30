from pydantic import BaseModel

class RegisterConnectionRequest(BaseModel):
    node_identifier: str
    node_ip: str
