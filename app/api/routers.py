from fastapi import APIRouter

from app.api.v1.user import router as user_router

router = APIRouter(prefix="/api")
router.include_router(user_router, prefix="/v1")
