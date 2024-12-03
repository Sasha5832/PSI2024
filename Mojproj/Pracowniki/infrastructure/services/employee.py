from typing import List
from Pracowniki.core.domain.employee import Employee, EmployeeIn
from Pracowniki.core.repositories.iemployee import IEmployeeRepository

class EmployeeService:
    """Serwis zarządzania pracownikami."""

    def __init__(self, repository: IEmployeeRepository):
        self._repository = repository

    async def get_all_employees(self) -> List[Employee]:
        return await self._repository.get_all_employees()

    async def get_employee_by_id(self, employee_id: int) -> Employee | None:
        return await self._repository.get_by_id(employee_id)

    async def add_employee(self, employee_data: EmployeeIn) -> Employee:
        return await self._repository.add_employee(employee_data)

    async def update_employee(self, employee_id: int, employee_data: EmployeeIn) -> Employee | None:
        return await self._repository.update_employee(employee_id, employee_data)

    async def delete_employee(self, employee_id: int) -> bool:
        return await self._repository.delete_employee(employee_id)
