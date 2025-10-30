FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PAFKA_NODE_IDENTIFIER="node"
ENV PAFKA_BROKER="localhost:8000"
ENV PAFKA_NODE_HOST=localhost
ENV PAFKA_NODE_PORT=8000

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x startnode.sh
EXPOSE $PAFKA_NODE_PORT

CMD [ "/app/startnode.sh" ]