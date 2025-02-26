import json
import time
from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Kafka with SASL
consumer = KafkaConsumer(
    'iot_topic',
    bootstrap_servers=[
        'kafka-controller-0.kafka-controller-headless.default.svc.cluster.local:9092',
        'kafka-controller-1.kafka-controller-headless.default.svc.cluster.local:9092',
        'kafka-controller-2.kafka-controller-headless.default.svc.cluster.local:9092'
    ],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='iot-consumer-group',
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username="user1",  #check whether you have the same username (user1 could be set as default)
    sasl_plain_password=""  # check and decrypt your password
)

# Konfiguracja InfluxDB
influxdb_url = "http://10.0.196.242:80" #check if this is correct IP
influxdb_token = "" #check your influxdb token
influxdb_org = "influxdata" #check if this is correct
influxdb_bucket = "iot_data" #check if this is correct for you

client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=influxdb_org)
write_api = client.write_api(write_options=SYNCHRONOUS)

print("Kafka consumer is working and connected to influxDB")

for message in consumer:
    data = message.value

    point = Point("iot_measurements") \
        .tag("device_id", str(data["device_id"])) \
        .field("temperature", float(data["temperature"])) \
        .field("humidity", float(data["humidity"])) \
        .time(int(time.time()), WritePrecision.S)

    write_api.write(bucket=influxdb_bucket, record=point)
    print(f"Sent to InfluxDB: {data}")
