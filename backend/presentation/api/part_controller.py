from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.use_cases.part_use_cases import (
    CreatePartUseCase,
    GetPartByIdUseCase,
    UpdatePartUseCase,
    DeletePartUseCase,
    GetAllPartsUseCase
)
from infrastructure.repositories.sql_part_repository import SQLPartRepository
from infrastructure.database.database import get_session
from domain.entities.part import Part
from pydantic import BaseModel

router = APIRouter()

class PartCreate(BaseModel):
    numero_parte: str
    descripcion: str
    stock_actual: int
    costo: float

class PartUpdate(BaseModel):
    numero_parte: str | None = None
    descripcion: str | None = None
    stock_actual: int | None = None
    costo: float | None = None

@router.post("/parts/")
def create_part(part: PartCreate, session: Session = Depends(get_session)):
    repository = SQLPartRepository(session)
    use_case = CreatePartUseCase(repository)
    created_part = use_case.execute(
        numero_parte=part.numero_parte,
        descripcion=part.descripcion,
        stock_actual=part.stock_actual,
        costo=part.costo
    )
    return created_part

@router.get("/parts/{id}")
def get_part(id: int, session: Session = Depends(get_session)):
    repository = SQLPartRepository(session)
    use_case = GetPartByIdUseCase(repository)
    part = use_case.execute(id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.put("/parts/{id}")
def update_part(id: int, part: PartUpdate, session: Session = Depends(get_session)):
    repository = SQLPartRepository(session)
    use_case = UpdatePartUseCase(repository)
    existing_part = GetPartByIdUseCase(repository).execute(id)
    if not existing_part:
        raise HTTPException(status_code=404, detail="Part not found")
    updated_part = Part(
        id=id,
        numero_parte=part.numero_parte or existing_part.numero_parte,
        descripcion=part.descripcion or existing_part.descripcion,
        stock_actual=part.stock_actual or existing_part.stock_actual,
        costo=part.costo or existing_part.costo
    )
    return use_case.execute(updated_part)

@router.delete("/parts/{id}")
def delete_part(id: int, session: Session = Depends(get_session)):
    repository = SQLPartRepository(session)
    use_case = DeletePartUseCase(repository)
    use_case.execute(id)
    return {"message": "Part deleted"}

@router.get("/parts/")
def get_all_parts(session: Session = Depends(get_session)):
    repository = SQLPartRepository(session)
    use_case = GetAllPartsUseCase(repository)
    return use_case.execute()