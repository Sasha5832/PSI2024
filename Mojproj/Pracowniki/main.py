from fastapi import FastAPI
from Pracowniki.api.routers import employees

app = FastAPI()

app.include_router(employees.router)
