from kafka import KafkaConsumer
import json

def consume_messages():
    consumer = KafkaConsumer(
        'output-topic',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        print(f"Consumed message: {message.value}")

if __name__ == '__main__':
    consume_messages()
