from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import current_user, get_async_session
from app.models import User
from app.schemas import SalaryRead


router = APIRouter()


@router.get(
    "/salary",
    response_model=SalaryRead,
)
async def get_salary(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Эндпоинт для получения данных о текущей зарплате
    и дате следующего повышения"""
    return user
