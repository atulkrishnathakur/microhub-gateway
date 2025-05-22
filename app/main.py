from fastapi import FastAPI
from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from app.services.user_management.router.router_base import api_router
from app.auth.router_base import auth_router
from app.celery_app import celeryapp
from celery.result import AsyncResult


def include_router(app):
    app.include_router(api_router)
    app.include_router(auth_router)

def start_application():
    app = FastAPI(
        DEBUG=True,
        title="microhub-gateway",
        summary="gateway service",
        description="This is the gateway services",
        version="1.0.0",
        openapi_url="/microhub-gateway.json",
        docs_url="/microhub-gateway-docs",
        redoc_url="/microhub-gateway-redoc",
        root_path_in_servers=True,
        )
          
    include_router(app)
    return app

app = start_application()


@app.post("/tasks/")
def run_task(x: int, y: int):
    task = celeryapp.send_task("app.tasks.add", args=[x, y])
    return {"task_id": task.id}

@app.get("/tasks/{task_id}")
def get_task_result(task_id: str):
    result = AsyncResult(task_id, app=celeryapp)
    return {"task_id": task_id, "status": result.status, "result": result.result}
