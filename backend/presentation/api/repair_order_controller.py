from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.use_cases.repair_order_use_cases import (
    CreateRepairOrderUseCase,
    GetRepairOrderByIdUseCase,
    UpdateRepairOrderUseCase,
    DeleteRepairOrderUseCase,
    GetPendingRepairOrdersUseCase
)
from infrastructure.repositories.sql_repair_order_repository import SQLRepairOrderRepository
from infrastructure.database.database import get_session
from domain.entities.repair_order import RepairOrder
from pydantic import BaseModel
from datetime import date
from typing import List

router = APIRouter()

class RepairOrderCreate(BaseModel):
    id_vehiculo: int
    fecha_inicio: date
    fecha_fin: date | None = None
    estado: str
    mano_de_obra: float
    prioridad: int
    details: List[dict] | None = None  # Lista de {id_parte, cantidad}

class RepairOrderUpdate(BaseModel):
    id_vehiculo: int | None = None
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
    estado: str | None = None
    mano_de_obra: float | None = None
    prioridad: int | None = None

@router.post("/repair-orders/")
def create_repair_order(order: RepairOrderCreate, session: Session = Depends(get_session)):
    repository = SQLRepairOrderRepository(session)
    use_case = CreateRepairOrderUseCase(repository)
    created_order = use_case.execute(
        id_vehiculo=order.id_vehiculo,
        fecha_inicio=order.fecha_inicio,
        fecha_fin=order.fecha_fin,
        estado=order.estado,
        mano_de_obra=order.mano_de_obra,
        prioridad=order.prioridad,
        details=order.details
    )
    return created_order

@router.get("/repair-orders/{id}")
def get_repair_order(id: int, session: Session = Depends(get_session)):
    repository = SQLRepairOrderRepository(session)
    use_case = GetRepairOrderByIdUseCase(repository)
    order = use_case.execute(id)
    if not order:
        raise HTTPException(status_code=404, detail="Repair order not found")
    return order

@router.put("/repair-orders/{id}")
def update_repair_order(id: int, order: RepairOrderUpdate, session: Session = Depends(get_session)):
    repository = SQLRepairOrderRepository(session)
    use_case = UpdateRepairOrderUseCase(repository)
    existing_order = GetRepairOrderByIdUseCase(repository).execute(id)
    if not existing_order:
        raise HTTPException(status_code=404, detail="Repair order not found")
    updated_order = RepairOrder(
        id=id,
        id_vehiculo=order.id_vehiculo or existing_order.id_vehiculo,
        fecha_inicio=order.fecha_inicio or existing_order.fecha_inicio,
        fecha_fin=order.fecha_fin or existing_order.fecha_fin,
        estado=order.estado or existing_order.estado,
        mano_de_obra=order.mano_de_obra or existing_order.mano_de_obra,
        prioridad=order.prioridad or existing_order.prioridad,
        details=existing_order.details
    )
    return use_case.execute(updated_order)

@router.delete("/repair-orders/{id}")
def delete_repair_order(id: int, session: Session = Depends(get_session)):
    repository = SQLRepairOrderRepository(session)
    use_case = DeleteRepairOrderUseCase(repository)
    use_case.execute(id)
    return {"message": "Repair order deleted"}

@router.get("/repair-orders/pending/")
def get_pending_repair_orders(session: Session = Depends(get_session)):
    repository = SQLRepairOrderRepository(session)
    use_case = GetPendingRepairOrdersUseCase(repository)
    return use_case.execute()