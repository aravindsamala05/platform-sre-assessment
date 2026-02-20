from flask import Flask, request, jsonify
import time, uuid

app = Flask(__name__)
services = {}

@app.route("/register-service", methods=["POST"])
def register():
    data = request.json
    services[data["service_name"]] = {
        "team": data["team_name"],
        "repo": data["repo_url"],
        "status": "REGISTERED",
        "last_deploy": None
    }
    return jsonify({"message": "Service Registered"}), 201

@app.route("/deploy/<service>")
def deploy(service):
    build_id = str(uuid.uuid4())
    services[service]["status"] = "RUNNING"
    services[service]["last_deploy"] = time.time()
    return jsonify({"build_id": build_id, "status": "RUNNING"})

@app.route("/health/<service>")
def health(service):
    s = services.get(service)
    return jsonify({
        "service_name": service,
        "deployment_status": s["status"],
        "pod_count": 3,
        "cpu": "60%",
        "memory": "512Mi"
    })
