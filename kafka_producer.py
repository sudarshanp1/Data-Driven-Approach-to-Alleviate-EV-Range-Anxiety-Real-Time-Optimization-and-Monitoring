
from kafka import KafkaProducer
import json

def produce_data(topic, server='localhost:9092'):
    producer = KafkaProducer(
        bootstrap_servers=server,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    data = {"speed": 50, "acceleration": 1.2, "temperature": 30, "road_grade": 0.5}
    producer.send(topic, data)
    producer.close()

if __name__ == "__main__":
    produce_data('ev-telemetry')
            