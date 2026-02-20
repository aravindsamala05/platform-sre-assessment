apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{service_name}}
spec:
  replicas: 2
  template:
    spec:
      containers:
      - name: {{service_name}}
        image: {{image}}
