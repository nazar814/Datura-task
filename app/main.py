from fastapi import FastAPI, HTTPException
from .schemas import TaskRequest
from .tasks import execute_task

app = FastAPI()

@app.post("/execute")
async def execute(task_request: TaskRequest):
    try:
        result = await execute_task(task_request)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
