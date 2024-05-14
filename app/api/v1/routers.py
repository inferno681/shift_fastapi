from fastapi import APIRouter

from app.api.v1.endpoints import user_router


router = APIRouter()
router.include_router(user_router, tags=["user"])
