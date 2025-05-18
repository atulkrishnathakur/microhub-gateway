from fastapi import APIRouter, FastAPI
from app.auth.router.api import auth_route

auth_router = APIRouter()

auth_router.include_router(auth_route.router, prefix="", tags=["Authentication"])
