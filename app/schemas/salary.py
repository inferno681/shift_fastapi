from datetime import date

from pydantic import BaseModel, condecimal

from app.core.constants import DECIMAL_PLACES, LENGTH_LIMITS_DECIMAL_FIELDS


class SalaryRead(BaseModel):
    salary: condecimal(
        gt=0,
        max_digits=LENGTH_LIMITS_DECIMAL_FIELDS,
        decimal_places=DECIMAL_PLACES,
    )
    next_promotion: date
