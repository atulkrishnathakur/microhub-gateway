from fastapi import APIRouter, FastAPI
from app.auth.router.api import auth_route
from app.auth.router.api import test_route

auth_router = APIRouter()

auth_router.include_router(auth_route.router, prefix="", tags=["Authentication"])
auth_router.include_router(test_route.router, prefix="", tags=["authtest"])
