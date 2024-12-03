from typing import List
from abc import ABC, abstractmethod
from Pracowniki.core.domain.employee import Employee, EmployeeIn

class IEmployeeRepository(ABC):
    @abstractmethod
    async def get_all_employees(self) -> List[Employee]:
        pass

    @abstractmethod
    async def get_by_id(self, employee_id: int) -> Employee | None:
        pass

    @abstractmethod
    async def add_employee(self, employee: EmployeeIn) -> Employee:
        pass

    @abstractmethod
    async def update_employee(self, employee_id: int, employee: EmployeeIn) -> Employee | None:
        pass

    @abstractmethod
    async def delete_employee(self, employee_id: int) -> bool:
        pass
