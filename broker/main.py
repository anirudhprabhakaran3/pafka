import os
import logging
from fastapi import FastAPI
from models.metadata import BrokerMetadata
from models.api import RegisterConnectionRequest
from connections import Connections

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
metadata = BrokerMetadata(
    identifier=os.environ.get("PAFKA_BROKER_IDENTIFIER"),
    port=int(os.environ.get("PAFKA_BROKER_PORT"))
)
connections = Connections()

logger.info(f"Started broker with metadata: {metadata}")

@app.get("/health")
def health():
    return {
        "success": True,
        "payload": metadata
    }

@app.get("/connections")
def list_connections():
    return {
        "success": True,
        "payload": connections.list_connections()
    }

@app.post("/connections/register")
def register_connection(register_request: RegisterConnectionRequest):
    connections.register_connection(register_request.node_identifier, register_request.node_ip)
    logger.info("Registered connection.")
    return {
        "success": True,
        "payload": register_request
    }