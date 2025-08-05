# AI Backend App

This is a sample FastAPI backend project that integrates:

- ✅ FastAPI (Python 3.13)
- ✅ Kafka Producer and Consumer
- ✅ Redis Cache

## Running locally

```bash
uvicorn main:app --reload


curl -X POST http://localhost:8000/send \
-H "Content-Type: application/json" \
-d '{"user": "Gokula", "message": "Hello from FastAPI Kafka producer!"}'
