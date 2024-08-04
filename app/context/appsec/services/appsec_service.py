from app.context.appsec.checks.appsec_check import check_practice
from app.context.appsec.dependencies.repositories import IAppsecRepository
from app.context.appsec.schemas.appsec_schema import GetAppsecPractice, GetAppsec


class Appsec:
    def __init__(self, repository: IAppsecRepository):
        self.repository = repository

    async def get_appsec(self, key: str) -> GetAppsecPractice | GetAppsec:
        check_practice(key)
        return await self.repository.get_practice(key)