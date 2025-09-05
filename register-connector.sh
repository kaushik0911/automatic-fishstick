#!/bin/bash
# echo "Waiting for Kafka Connect to be ready..."
# until curl -s http://localhost:8083/connectors; do
#   echo "Kafka Connect not ready yet... retrying in 5s"
#   sleep 5
# done

echo "Registering Elasticsearch Sink Connector..."
curl -X POST -H "Content-Type: application/json" \
  --data register-connector.json \
  http://localhost:8083/connectors
