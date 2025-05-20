from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.use_cases.vehicle_use_cases import (
    CreateVehicleUseCase,
    GetVehicleByIdUseCase,
    UpdateVehicleUseCase,
    DeleteVehicleUseCase
)
from infrastructure.repositories.sql_vehicle_repository import SQLVehicleRepository
from infrastructure.database.database import get_session
from domain.entities.vehicle import Vehicle
from pydantic import BaseModel

router = APIRouter()

class VehicleCreate(BaseModel):
    id_cliente: int
    marca: str
    modelo: str
    año: int | None = None
    vin: str | None = None

class VehicleUpdate(BaseModel):
    id_cliente: int | None = None
    marca: str | None = None
    modelo: str | None = None
    año: int | None = None
    vin: str | None = None

@router.post("/vehicles/")
def create_vehicle(vehicle: VehicleCreate, session: Session = Depends(get_session)):
    repository = SQLVehicleRepository(session)
    use_case = CreateVehicleUseCase(repository)
    created_vehicle = use_case.execute(
        id_cliente=vehicle.id_cliente,
        marca=vehicle.marca,
        modelo=vehicle.modelo,
        año=vehicle.año,
        vin=vehicle.vin
    )
    return created_vehicle

@router.get("/vehicles/{id}")
def get_vehicle(id: int, session: Session = Depends(get_session)):
    repository = SQLVehicleRepository(session)
    use_case = GetVehicleByIdUseCase(repository)
    vehicle = use_case.execute(id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.put("/vehicles/{id}")
def update_vehicle(id: int, vehicle: VehicleUpdate, session: Session = Depends(get_session)):
    repository = SQLVehicleRepository(session)
    use_case = UpdateVehicleUseCase(repository)
    existing_vehicle = GetVehicleByIdUseCase(repository).execute(id)
    if not existing_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    updated_vehicle = Vehicle(
        id=id,
        id_cliente=vehicle.id_cliente or existing_vehicle.id_cliente,
        marca=vehicle.marca or existing_vehicle.marca,
        modelo=vehicle.modelo or existing_vehicle.modelo,
        año=vehicle.año or existing_vehicle.año,
        vin=vehicle.vin or existing_vehicle.vin
    )
    return use_case.execute(updated_vehicle)

@router.delete("/vehicles/{id}")
def delete_vehicle(id: int, session: Session = Depends(get_session)):
    repository = SQLVehicleRepository(session)
    use_case = DeleteVehicleUseCase(repository)
    use_case.execute(id)
    return {"message": "Vehicle deleted"}