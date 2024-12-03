from fastapi import APIRouter, HTTPException
from typing import List
from Pracowniki.core.domain.employee import Employee, EmployeeIn
from Pracowniki.infrastructure.services.employee import EmployeeService
from Pracowniki.infrastructure.repositories.employeemock import EmployeeRepository

router = APIRouter()

employee_service = EmployeeService(EmployeeRepository())

@router.get("/employees", response_model=List[Employee])
async def get_employees():
    return await employee_service.get_all_employees()

@router.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int):
    employee = await employee_service.get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.post("/employees", response_model=Employee)
async def add_employee(employee_data: EmployeeIn):
    return await employee_service.add_employee(employee_data)

@router.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee_data: EmployeeIn):
    employee = await employee_service.update_employee(employee_id, employee_data)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.delete("/employees/{employee_id}", response_model=bool)
async def delete_employee(employee_id: int):
    success = await employee_service.delete_employee(employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return success
