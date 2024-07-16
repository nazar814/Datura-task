# app/tasks.py

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

async def execute_task(task_request: TaskRequest):
    client = get_docker_client()
    container = create_docker_container(client, task_request)
    container.start()

    # Properly format the code for execution
    code_to_execute = f'python -c "{task_request.code}"'
    exit_code, output = container.exec_run(code_to_execute)

    container.stop()
    container.remove()
    return output.decode('utf-8')

def create_docker_container(client, task_request: TaskRequest):
    # Convert resource requirements to Docker resource limits
    cpu_shares = int(task_request.resources.cpu) * 1024
    mem_limit = task_request.resources.ram
    
    container = client.containers.create(
        image="python:3.9-slim",
        command="tail -f /dev/null",  # Keeps the container running
        cpu_shares=cpu_shares,
        mem_limit=mem_limit
    )
    return container
