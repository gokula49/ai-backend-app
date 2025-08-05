import json
from kafka import KafkaConsumer

# Create Kafka consumer
consumer = KafkaConsumer(
    'greetings',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group'
)

print("🟢 Listening for messages on topic 'greetings'...")

# Consume messages
for message in consumer:
    print(f"✅ Received message: {message.value}")
