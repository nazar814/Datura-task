import docker
from app.schemas import TaskRequest
import asyncio

client = docker.from_env()

async def execute_task(task_request: TaskRequest):
    container = create_docker_container(task_request)
    container.start()
    exit_code, output = container.exec_run("python -c '{}'".format(task_request.code))
    container.stop()
    container.remove()
    return output.decode('utf-8')

def create_docker_container(task_request: TaskRequest):
    # Convert resource requirements to Docker resource limits
    cpu_shares = int(task_request.resources.cpu) * 1024
    mem_limit = task_request.resources.ram
    storage_opt = {"size": task_request.resources.storage}
    
    container = client.containers.create(
        image="python:3.9-slim",
        command="tail -f /dev/null",  # Keeps the container running
        cpu_shares=cpu_shares,
        mem_limit=mem_limit,
        storage_opt=storage_opt
    )
    return container
