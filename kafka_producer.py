# kafka_producer.py

from kafka import KafkaProducer
import json

# Kafka producer config
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_message(topic: str, message: dict):
    try:
        producer.send(topic, message)
        producer.flush()
        print(f"✅ Message sent to topic '{topic}': {message}")
    except Exception as e:
        print(f"❌ Error sending message: {e}")

# Sample test
if __name__ == "__main__":
    test_message = {
        "user": "Gokula",
        "message": "Hello from FastAPI Kafka producer!"
    }
    send_message("greetings", test_message)
