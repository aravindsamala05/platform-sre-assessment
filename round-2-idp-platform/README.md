# Internal Developer Platform (IDP)

Self-service backend for microservice onboarding and deployments.

## Features
1. Register new microservice
2. Provision infra via Terraform
3. Generate CI/CD & K8s manifests
4. Simulate deployment trigger
5. Health dashboard API

## APIs
- POST /register-service
- POST /deploy/{service}
- GET /health/{service}
