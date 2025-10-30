import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Connections:
    def __init__(self):
        self.connections = {}

    def list_connections(self):
        return self.connections
    
    def register_connection(self, node_identifier: str, node_ip: str):
        if node_identifier not in self.connections.keys():
            self.connections[node_identifier] = node_ip
            logger.info(f"Node {node_identifier} with ip {node_ip} registered.")
            return
        else:
            logger.warning(f"Node {node_identifier} has already been registered. Old IP: {self.connections[node_identifier]}, New IP: {node_ip}")