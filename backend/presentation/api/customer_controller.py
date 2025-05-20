from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.use_cases.customer_use_cases import (
    CreateCustomerUseCase,
    GetCustomerByIdUseCase,
    UpdateCustomerUseCase,
    DeleteCustomerUseCase
)
from infrastructure.repositories.sql_customer_repository import SQLCustomerRepository
from infrastructure.database.database import get_session
from domain.entities.customer import Customer
from pydantic import BaseModel

router = APIRouter()

class CustomerCreate(BaseModel):
    nombre: str
    apellido: str
    direccion: str | None = None
    telefono: str | None = None
    email: str | None = None

class CustomerUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    direccion: str | None = None
    telefono: str | None = None
    email: str | None = None

@router.post("/customers/")
def create_customer(customer: CustomerCreate, session: Session = Depends(get_session)):
    repository = SQLCustomerRepository(session)
    use_case = CreateCustomerUseCase(repository)
    created_customer = use_case.execute(
        nombre=customer.nombre,
        apellido=customer.apellido,
        direccion=customer.direccion,
        telefono=customer.telefono,
        email=customer.email
    )
    return created_customer

@router.get("/customers/{id}")
def get_customer(id: int, session: Session = Depends(get_session)):
    repository = SQLCustomerRepository(session)
    use_case = GetCustomerByIdUseCase(repository)
    customer = use_case.execute(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/customers/{id}")
def update_customer(id: int, customer: CustomerUpdate, session: Session = Depends(get_session)):
    repository = SQLCustomerRepository(session)
    use_case = UpdateCustomerUseCase(repository)
    existing_customer = GetCustomerByIdUseCase(repository).execute(id)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    updated_customer = Customer(
        id=id,
        nombre=customer.nombre or existing_customer.nombre,
        apellido=customer.apellido or existing_customer.apellido,
        direccion=customer.direccion or existing_customer.direccion,
        telefono=customer.telefono or existing_customer.telefono,
        email=customer.email or existing_customer.email
    )
    return use_case.execute(updated_customer)

@router.delete("/customers/{id}")
def delete_customer(id: int, session: Session = Depends(get_session)):
    repository = SQLCustomerRepository(session)
    use_case = DeleteCustomerUseCase(repository)
    use_case.execute(id)
    return {"message": "Customer deleted"}