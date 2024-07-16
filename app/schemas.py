from pydantic import BaseModel

class ResourceRequirements(BaseModel):
    cpu: str
    gpu: str
    ram: str
    storage: str

class TaskRequest(BaseModel):
    task_type: str
    code: str
    resources: ResourceRequirements
