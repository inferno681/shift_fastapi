from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import CheckConstraint, Column, Date, DateTime, DECIMAL, String

from app.core.constants import LENGTH_LIMITS_USER_FIELDS
from app.core import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """Модель пользователя"""

    username = Column(
        String(LENGTH_LIMITS_USER_FIELDS), nullable=False, unique=True
    )
    first_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    last_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    middle_name = Column(String(LENGTH_LIMITS_USER_FIELDS))
    created = Column(DateTime, default=datetime.now)
    salary = Column(DECIMAL(precision=10, scale=2), default=1)
    next_promotion = Column(Date, default=datetime.now())

    __table_args__ = (
        CheckConstraint(salary > 0, name="salary_positive_check"),
    )
