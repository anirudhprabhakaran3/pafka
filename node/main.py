import os
from fastapi import FastAPI
from models.metadata import NodeMetadata
from models.api import RegisterTopicRequest
import logging
from storage import InMemoryStorage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
metadata = NodeMetadata(
    identifier=os.environ.get("PAFKA_NODE_IDENTIFIER"),
    broker=os.environ.get("PAFKA_BROKER"),
    port=int(os.environ.get("PAFKA_NODE_PORT")),
)
storage = InMemoryStorage()

logger.info(f"Initialized server with NodeMetadata: {metadata}")

@app.get("/health")
def health():
    return {
        "success": True,
        "payload": {
            "metadata": metadata
        },
    }

@app.get("/topics")
def list_topics():
    return {
        "success": True,
        "payload": storage.topic_partitions
    }

@app.post("/topics/register")
def register_topic(request: RegisterTopicRequest):
    storage.registerTopic(request.topic_name, request.partition_id)
    logger.info(f"Registered topic {request.topic_name}")
    return {
        "success": True,
        "payload": request
    }