from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import CheckConstraint, Column, Date, DateTime, DECIMAL, String

from app.core.constants import LENGTH_LIMITS_USER_FIELDS
from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """Модель пользователя"""

    created = Column(DateTime, default=datetime.now)
    first_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    last_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    middle_name = Column(String(LENGTH_LIMITS_USER_FIELDS))
    salary = Column(DECIMAL(precision=10, scale=2))
    next_promotion = Column(Date)

    __table_args__ = (
        CheckConstraint(salary > 0, name='salary_positive_check'),
    )
