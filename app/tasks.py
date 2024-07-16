import docker
from docker.errors import DockerException
from app.schemas import TaskRequest
import asyncio

def get_docker_client():
    try:
        client = docker.from_env()
        return client
    except DockerException as e:
        raise RuntimeError(f"Failed to connect to Docker daemon: {str(e)}")
