from fastapi import APIRouter

from .context.appsec.route import appsec_router
from .context.login.route import login_router


def get_apps_router() -> APIRouter:
    router = APIRouter()
    router.include_router(appsec_router)
    router.include_router(login_router)
    return router