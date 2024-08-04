import uvicorn
from fastapi import FastAPI

from app.routes import get_apps_router


app = FastAPI()
app.include_router(get_apps_router())


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=6000, reload=True)


