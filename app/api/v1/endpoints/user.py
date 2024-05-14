from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import get_async_session
from app.core import current_user
from app.models import User
from app.schemas import SalaryRead


router = APIRouter()


@router.get(
    '/salary',
    response_model=SalaryRead,
)
async def get_salary(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return user
