import logging
from models.message import Message
from threading import Lock

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Functions to interact with the storage layer

class InMemoryStorage:
    """
    Store all data in this dict. It will look like:
    """
    storage: dict
    topic_positions: dict
    topic_partitions: dict
    lock: Lock

    def __init__(self):
        """
        Initialize the storage. We initialize with an empty dict.
        We currently have no long term storage, as we are keeping everything in memory.
        """
        self.storage = {}
        self.topic_positions = {}
        self.topic_partitions = {}
        self.lock = Lock()

    def checkTopic(self, topic_name: str):
        if topic_name in self.storage.keys():
            logger.debug(f"Topic {topic_name} was found in storage.")
            return True
        else:
            logger.error(f"Topic {topic_name} was not found in storage.")
            return False

    def registerTopic(self, topic_name: str, partition_id: int):
        """
        Add topic to the node. A node can only store data for one partition, which it gets from the broker.
        """

        if self.checkTopic(topic_name):
            logger.error(f"Topic {topic_name} already being stored, skipping registration...")
        else:
            self.storage[topic_name] = []
            self.topic_positions[topic_name] = 0
            self.topic_partitions[topic_name] = partition_id
            logger.info(f"Added topic {topic_name} and partitionID: {partition_id} to the storage.")

    def ingestMessage(self, topic_name: str, message: Message):
        """
        Add a message to the topic
        """
        
        if self.checkTopic(topic_name):
            with self.lock:
                message.position = self.topic_positions[topic_name] + 1
                self.topic_positions[topic_name] += 1
                self.storage[topic_name].append(message)
                logger.debug(f"Added message {message} to the storage.")
        else:
            logger.error(f"Cannot find the topic {topic_name} to ingest the message in storage.")