# Pafka Broker

Broker to manage nodes and information about everything.

Start the broker with the following commands:

```sh
# Build the image
podman build -t pafka-broker .

# Ensure the network is available.
podman network create pafka-network

# Run the container
podman run -e PAFKA_BROKER_IDENTIFIER="pafka-broker-1" -e PAFKA_BROKER_PORT=8000 --network="pafka-network" --name="pafka-broker-1" -p 8000:8000 pafka-broker
```