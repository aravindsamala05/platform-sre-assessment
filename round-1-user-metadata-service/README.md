# User Metadata Service (Resilient Backend)

## APIs
### POST /user
Creates a user (idempotent).

### GET /user/{id}
Fetches user metadata.

## Reliability Features
- Idempotency using user_id
- Retry with exponential backoff + jitter
- Circuit breaker for DB failures
- Metrics (requests, success, failures, latency)
- Structured logging with request_id
- Dockerized service

## Run Locally
```bash
pip install -r requirements.txt
python app.py
