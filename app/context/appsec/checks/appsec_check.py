from fastapi import HTTPException

from app.context.appsec.repositories.appsec_repository import practice


def check_practice(key: str) -> None:
    print(key)
    if key != 'practice_main' and key not in practice:
        raise HTTPException(status_code=422,
                            detail="Введите корректные данные, такой практики не существует")