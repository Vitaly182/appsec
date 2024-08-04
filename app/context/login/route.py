from fastapi import APIRouter

from .controllers import login_controller

login_router = APIRouter()
login_router.include_router(login_controller.router_login)