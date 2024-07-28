from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema
import json

def process_stream():
    env = StreamExecutionEnvironment.get_execution_environment()

    kafka_consumer = FlinkKafkaConsumer(
        topics='input-topic',
        deserialization_schema=SimpleStringSchema(),
        properties={'bootstrap.servers': 'localhost:9092', 'group.id': 'flink-group'}
    )

    kafka_producer = FlinkKafkaProducer(
        topic='output-topic',
        serialization_schema=SimpleStringSchema(),
        producer_config={'bootstrap.servers': 'localhost:9092'}
    )

    data_stream = env.add_source(kafka_consumer)

    processed_stream = data_stream.map(lambda message: json.dumps({"original": message, "processed": message.upper()}))

    processed_stream.add_sink(kafka_producer)

    env.execute('Flink Kafka Example')

if __name__ == '__main__':
    process_stream()
