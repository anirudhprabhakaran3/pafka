# Pafka Node

Node that actually sends, receives, stores messages. You can start a node using the following:

```sh
# Build image for node
podman build -t pafka-node .

# Ensure that the network exists.
podman network create pafka-network

# Run the container
podman run -e PAFKA_NODE_IDENTIFIER="pafka-node-1" -e PAFKA_BROKER="pafka-broker-1:8000" -e PAFKA_NODE_HOST="pafka-node-1" -e PAFKA_NODE_PORT=8080 -p 8080:8080 --network="pafka-network" --name="pafka-node-1" pafka-node
```