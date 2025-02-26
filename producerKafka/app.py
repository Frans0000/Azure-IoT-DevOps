import time
import random
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=[
        'kafka-controller-0.kafka-controller-headless.default.svc.cluster.local:9092',
        'kafka-controller-1.kafka-controller-headless.default.svc.cluster.local:9092',
        'kafka-controller-2.kafka-controller-headless.default.svc.cluster.local:9092'
    ],
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='SCRAM-SHA-256',
    sasl_plain_username='user1',      # Make sure its correct username
    sasl_plain_password='', # find your password
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    data = {
        "device_id": random.randint(1, 100), #example data
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2)
    }
    return data

if __name__ == "__main__":
    topic = 'iot_topic'
    while True:
        data = generate_data()
        producer.send(topic, value=data)
        print(f"Sent data: {data}")
        time.sleep(2) #change how often you want it to be sent
