from datetime import date

from fastapi_users import schemas
from pydantic import BaseModel, condecimal, PositiveInt


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    middle_name: str | None = None
    position_id: PositiveInt
    salary: condecimal(gt=0, max_digits=10, decimal_places=2)
    next_promotion: date


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(BaseModel):
    password: str | None = None


