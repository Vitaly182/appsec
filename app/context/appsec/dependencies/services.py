from typing import Annotated

from fastapi import Depends

from app.context.appsec.services.appsec_service import Appsec

IAppsec = Annotated[Appsec, Depends()]

