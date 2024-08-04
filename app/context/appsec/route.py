from fastapi import APIRouter

from .controllers import appsec_controller

appsec_router = APIRouter()
appsec_router.include_router(appsec_controller.router_appsec)