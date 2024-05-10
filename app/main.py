import uvicorn
from fastapi import FastAPI

from app.api import api_router
from app.auth import auth_router
from app.core.config import config

tags_metadata = [
    {"name": "User", "description": "Запросы пользователя"},
]

app = FastAPI(
    title=config.app_title,
    description=config.description,
    openapi_tags=tags_metadata,
)

app.include_router(api_router)
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000, log_level="info")
