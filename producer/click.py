from kafka import KafkaProducer
import json

def produce_messages():
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    for i in range(10):
        message = {'key': i, 'value': f'message {i}'}
        producer.send('input-topic', message)
    producer.flush()

if __name__ == '__main__':
    produce_messages()
