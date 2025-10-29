#!/bin/sh
# startbroker.sh

exec uvicorn main:app --host 0.0.0.0 --port ${PAFKA_BROKER_PORT}