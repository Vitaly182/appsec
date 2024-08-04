from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import RedirectResponse, HTMLResponse

from app.context.login.dependencies.services import ILoginService


router_login = APIRouter(tags=["login"])


@router_login.get("/", response_model=None, response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def home(service: ILoginService) -> RedirectResponse:
    return await service.home()


@router_login.get("/login", response_model=None, response_class=HTMLResponse)
async def login_form(service: ILoginService) -> str:
    return await service.login_form()


@router_login.post("/login", response_model=None, response_class=HTMLResponse)
async def login(service: ILoginService, data: OAuth2PasswordRequestForm = Depends()) -> str:
    return await service.login(data=data)