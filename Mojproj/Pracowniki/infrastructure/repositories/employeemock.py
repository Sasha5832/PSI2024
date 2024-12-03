from typing import List
from Pracowniki.core.domain.employee import Employee, EmployeeIn
from Pracowniki.core.repositories.iemployee import IEmployeeRepository

class EmployeeRepository(IEmployeeRepository):
    def __init__(self):
        self._employees = []
        self._next_id = 1

    async def get_all_employees(self) -> List[Employee]:
        return self._employees

    async def get_by_id(self, employee_id: int) -> Employee | None:
        return next((emp for emp in self._employees if emp.id == employee_id), None)

    async def add_employee(self, employee: EmployeeIn) -> Employee:
        new_employee = Employee(id=self._next_id, **employee.dict())
        self._employees.append(new_employee)
        self._next_id += 1
        return new_employee

    async def update_employee(self, employee_id: int, employee: EmployeeIn) -> Employee | None:
        existing_employee = await self.get_by_id(employee_id)
        if existing_employee:
            updated_employee = existing_employee.copy(update=employee.dict())
            self._employees = [updated_employee if emp.id == employee_id else emp for emp in self._employees]
            return updated_employee
        return None

    async def delete_employee(self, employee_id: int) -> bool:
        employee = await self.get_by_id(employee_id)
        if employee:
            self._employees = [emp for emp in self._employees if emp.id != employee_id]
            return True
        return False
