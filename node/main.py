import os
from fastapi import FastAPI
from models.metadata import NodeMetadata
from models.api import RegisterTopicRequest
import logging
from storage import InMemoryStorage
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
metadata = NodeMetadata(
    identifier=os.environ.get("PAFKA_NODE_IDENTIFIER"),
    broker=os.environ.get("PAFKA_BROKER"),
    host=os.environ.get("PAFKA_NODE_HOST"),
    port=int(os.environ.get("PAFKA_NODE_PORT")),
)
storage = InMemoryStorage()

# Register to Broker
broker_url = os.environ.get("PAFKA_BROKER")
broker_register_endpoint = f"http://{broker_url}/connections/register"
register_request_payload = {
    "node_identifier": metadata.identifier,
    "node_ip": metadata.host + ":" + str(metadata.port)
}
register_response = requests.post(broker_register_endpoint, json=register_request_payload)
logger.info(f"Sending register request to {broker_register_endpoint} with payload: {register_request_payload}")
if (register_response.status_code == 200):
    resp = register_response.json()
    logger.info(f"Request returned a response {resp}") 
else:
    logger.error(f"Unable to register with broker at {broker_register_endpoint} with payload {register_request_payload}")
    exit()

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