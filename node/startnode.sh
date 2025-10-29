#!/bin/sh
# startnode.sh

exec uvicorn main:app --host 0.0.0.0 --port ${PAFKA_NODE_PORT}