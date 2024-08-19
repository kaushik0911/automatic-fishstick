import uuid
import logging
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'kaushik',
    'start_date': datetime.now()
}

def get_data():
    import requests

    logging.info("Fetching data from randomuser.me API")
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        logging.info("Data fetched successfully")
        return response.json()['results'][0]
    else:
        logging.error(f"Failed to fetch data. Status code: {response.status_code}")
        raise Exception("API request failed")

def format_data(response):
    logging.info("Formatting data")
    data = {}
    location = response['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = response['name']['first']
    data['last_name'] = response['name']['last']
    data['gender'] = response['gender']
    data['address'] = \
        f"{location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = response['email']
    data['username'] = response['login']['username']
    data['dob'] = response['dob']['date']
    data['registered_date'] = response['registered']['date']
    data['phone'] = response['phone']
    data['picture'] = response['picture']['medium']

    logging.info("Data formatted successfully")
    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time

    logging.info("Starting Kafka producer")
    producer = KafkaProducer(bootstrap_servers='localhost:9092', max_block_ms=5000)
    current_time = time.time()

    while True:
        if time.time() > current_time + 1:
            break
        try:
            response = format_data(get_data())
            logging.info(f"Sending data to Kafka: {response}")
            producer.send('user_created', json.dumps(response).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')

with DAG(
        dag_id='user_automation',
        default_args=default_args,
        schedule_interval='@daily',
        catchup=False
    ) as dag:

    streaming_task = PythonOperator(
        task_id='streaming_data_from_api',
        python_callable=stream_data
    )

    streaming_task
