from typing import Annotated

from fastapi import Depends

from app.context.appsec.repositories.appsec_repository import AppsecRepository

IAppsecRepository = Annotated[AppsecRepository, Depends()]
