FROM confluentinc/cp-kafka-connect:7.2.15

RUN confluent-hub install --no-prompt debezium/debezium-connector-mysql:3.1.2

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-elasticsearch:14.0.1
