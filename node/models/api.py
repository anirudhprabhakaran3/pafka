from pydantic import BaseModel

class RegisterTopicRequest(BaseModel):
    topic_name: str
    partition_id: int