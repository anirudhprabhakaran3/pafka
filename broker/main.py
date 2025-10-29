import os
import logging
from fastapi import FastAPI
from models.metadata import BrokerMetadata

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
metadata = BrokerMetadata(
    identifier=os.environ.get("PAFKA_BROKER_IDENTIFIER"),
    port=int(os.environ.get("PAFKA_BROKER_PORT"))
)

logger.info(f"Started broker with metadata: {metadata}")

@app.get("/health")
def health():
    return {
        "success": True,
        "payload": metadata
    }