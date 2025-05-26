from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from app.services.user_management.router.router_base import api_router
from app.auth.router_base import auth_router
from app.celery_tasks.router.celery_route import celery_router
from app.config.redis_session import RedisSession
import uuid

redisSession = RedisSession()

def include_router(app):
    app.include_router(api_router)
    app.include_router(auth_router)
    app.include_router(celery_router)

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


@app.post("/redis-session-set")
def session_test():
    redisSession.set_session("testsession", {"user": "atuluser"})
    return "session set"

@app.post("/redis-session-get")
def session_get():
    user_data = redisSession.get_session("testsession")
    return user_data
