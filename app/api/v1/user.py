from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.models.user import User
from app.schemas.salary import SalaryRead


router = APIRouter()


@router.get(
    '/employees',
    response_model_exclude={'is_active'},
    responses={
        200: {'model': SalaryRead},
        # 401: {'model': ErrorSchema},
        # 403: {'model': Error403Schema},
    },
)
async def get_employees(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):

    return user
