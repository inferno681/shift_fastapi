from datetime import date

from pydantic import BaseModel, condecimal


class SalaryRead(BaseModel):
    salary: condecimal(gt=0, max_digits=10, decimal_places=2)
    next_promotion: date
