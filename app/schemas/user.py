from datetime import date

from fastapi_users import schemas
from pydantic import BaseModel, condecimal


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    middle_name: str | None = None
    salary: condecimal(gt=0, max_digits=10, decimal_places=2)
    next_promotion: date


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    middle_name: str | None = None
    salary: condecimal(gt=0, max_digits=10, decimal_places=2)
    next_promotion: date


class UserUpdate(BaseModel):
    password: str | None = None
