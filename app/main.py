import uvicorn
from fastapi import FastAPI

from app.api.routers import router
from app.auth import auth_router
from app.core.config import config

tags_metadata = [
    {"name": "User", "description": "Запросы пользователя"},
]

app = FastAPI(
    title=config.APP_TITLE,
    description=config.APP_DESCRIPTION,
    openapi_tags=tags_metadata,
)

app.include_router(router)
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000, log_level="info")
