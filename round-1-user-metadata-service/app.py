
---

## `app.py` (Round-1 – COMPLETE & INTERVIEW READY)

```python
from flask import Flask, request, jsonify
import time, uuid, random

app = Flask(__name__)

db = {}
metrics = {
    "total_requests": 0,
    "success": 0,
    "failure": 0
}

failure_count = 0
CIRCUIT_OPEN = False
FAILURE_THRESHOLD = 3

def retry_with_backoff(func):
    delay = 0.5
    for i in range(3):
        try:
            return func()
        except Exception:
            time.sleep(delay * (2 ** i) + random.uniform(0, 0.2))
    raise Exception("DB failure after retries")

@app.route("/user", methods=["POST"])
def create_user():
    global failure_count, CIRCUIT_OPEN
    start = time.time()
    metrics["total_requests"] += 1
    request_id = str(uuid.uuid4())

    if CIRCUIT_OPEN:
        return jsonify({"error": "Circuit Open"}), 503

    data = request.json
    user_id = data["user_id"]

    try:
        if user_id in db:
            return jsonify(db[user_id]), 200  # Idempotent

        def db_write():
            if random.choice([True, False, True]):
                raise Exception("Simulated DB error")
            db[user_id] = {**data, "created_at": time.time()}
            return db[user_id]

        user = retry_with_backoff(db_write)
        metrics["success"] += 1
        return jsonify(user), 201

    except Exception as e:
        failure_count += 1
        metrics["failure"] += 1
        if failure_count >= FAILURE_THRESHOLD:
            CIRCUIT_OPEN = True
        return jsonify({"error": str(e), "request_id": request_id}), 500

@app.route("/user/<user_id>")
def get_user(user_id):
    return jsonify(db.get(user_id, {})), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
