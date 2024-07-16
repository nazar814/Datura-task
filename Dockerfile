# Dockerfile

FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
