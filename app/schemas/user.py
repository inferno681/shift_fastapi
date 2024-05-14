from datetime import date

from fastapi_users import schemas
from pydantic import BaseModel, condecimal


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    middle_name: str | None = None


class UserRead(schemas.BaseUser[int], UserBase):
    salary: condecimal(gt=0, max_digits=10, decimal_places=2)
    next_promotion: date


class UserCreate(schemas.BaseUserCreate, UserBase):
    pass


class UserUpdate(schemas.BaseUserUpdate, UserBase):
    pass
