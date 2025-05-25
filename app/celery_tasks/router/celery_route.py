from fastapi import APIRouter,Depends,status,File,UploadFile,BackgroundTasks
from app.config.celery_app import celeryapp
from celery.result import AsyncResult

celery_router = APIRouter()

@celery_router.post("/tasks_a/")
def run_task(x:int, y:int, z:int):
    task = celeryapp.send_task("app.celery_tasks.arithmetic.add", args=[x, y,z])
    return {"task_id": task.id}

 
@celery_router.get("/tasks_a/{task_id}")
def get_task_result(task_id: str):
    result = AsyncResult(task_id, app=celeryapp)
    return {"task_id": task_id, "status": result.status, "result": result.result}

# create separate endpoint to get result.
# celery task is asynchronous. If you fetch result in same function then it give None or PENDING because task started execution just.
@celery_router.post("/tasks_c/")
def add_data(x:int, y:int, z:int):
    task = celeryapp.send_task("app.celery_tasks.arithmetic.add", args=[x, y,z])
    task_id = task.id
    result = AsyncResult(task_id, app=celeryapp)
    return {"task_id": task_id, "status": result.status, "result": result.result}


@celery_router.post("/tasks_m/")
def run_task(x:int, y:int, z:int):
    task = celeryapp.send_task("app.celery_tasks.arithmetic.add", args=[x, y,z])
    return {"task_id": task.id}

 
@celery_router.get("/tasks_n/{task_id}")
def get_task_result(task_id: str):
    result = AsyncResult(task_id, app=celeryapp)
    return {"task_id": task_id, "status": result.status, "result": result.result}
