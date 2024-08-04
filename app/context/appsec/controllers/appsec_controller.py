from fastapi import APIRouter

from app.context.appsec.dependencies.services import IAppsec
from app.context.appsec.schemas.appsec_schema import GetAppsec, GetAppsecPractice

router_appsec = APIRouter(prefix="/appsec", tags=["appsec"])

@router_appsec.get("/", summary="Get appsec",  response_model=GetAppsecPractice | GetAppsec)
async def get_appsec(service: IAppsec, key: str) -> GetAppsecPractice | GetAppsec:
    return await service.get_appsec(key=key)