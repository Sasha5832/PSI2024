from pydantic import BaseModel
from datetime import date

class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    position: str
    hire_date: date

class EmployeeIn(BaseModel):
    first_name: str
    last_name: str
    position: str
    hire_date: date
