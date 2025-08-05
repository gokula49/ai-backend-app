from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import redis
import json

app = FastAPI()

# Redis setup
r = redis.Redis(host='localhost', port=6379, db=0)

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define request model
class Message(BaseModel):
    user: str
    message: str

@app.get("/")
def read_root():
    return {"message": "Hello Gokula! Your FastAPI app is working 🚀"}

@app.post("/send")
def send_message(msg: Message):
    producer.send("greetings", msg.dict())
    r.set("last_message", msg.json())  # Save to Redis
    return {"status": "Message sent", "data": msg}

@app.get("/last")
def get_last_message():
    cached = r.get("last_message")
    if cached:
        return {"last_message": json.loads(cached)}
    return {"last_message": "No message cached yet"}
