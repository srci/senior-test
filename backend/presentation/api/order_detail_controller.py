from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.use_cases.order_detail_use_cases import (
    CreateOrderDetailUseCase,
    GetOrderDetailByIdUseCase,
    UpdateOrderDetailUseCase,
    DeleteOrderDetailUseCase,
    GetOrderDetailsByOrderIdUseCase
)
from infrastructure.repositories.sql_order_detail_repository import SQLOrderDetailRepository
from infrastructure.database.database import get_session
from domain.entities.order_detail import OrderDetail
from pydantic import BaseModel

router = APIRouter()

class OrderDetailCreate(BaseModel):
    id_orden: int
    id_parte: int
    cantidad: int

class OrderDetailUpdate(BaseModel):
    id_orden: int | None = None
    id_parte: int | None = None
    cantidad: int | None = None

@router.post("/order-details/")
def create_order_detail(detail: OrderDetailCreate, session: Session = Depends(get_session)):
    repository = SQLOrderDetailRepository(session)
    use_case = CreateOrderDetailUseCase(repository)
    created_detail = use_case.execute(
        id_orden=detail.id_orden,
        id_parte=detail.id_parte,
        cantidad=detail.cantidad
    )
    return created_detail

@router.get("/order-details/{id}")
def get_order_detail(id: int, session: Session = Depends(get_session)):
    repository = SQLOrderDetailRepository(session)
    use_case = GetOrderDetailByIdUseCase(repository)
    detail = use_case.execute(id)
    if not detail:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return detail

@router.put("/order-details/{id}")
def update_order_detail(id: int, detail: OrderDetailUpdate, session: Session = Depends(get_session)):
    repository = SQLOrderDetailRepository(session)
    use_case = UpdateOrderDetailUseCase(repository)
    existing_detail = GetOrderDetailByIdUseCase(repository).execute(id)
    if not existing_detail:
        raise HTTPException(status_code=404, detail="Order detail not found")
    updated_detail = OrderDetail(
        id=id,
        id_orden=detail.id_orden or existing_detail.id_orden,
        id_parte=detail.id_parte or existing_detail.id_parte,
        cantidad=detail.cantidad or existing_detail.cantidad
    )
    return use_case.execute(updated_detail)

@router.delete("/order-details/{id}")
def delete_order_detail(id: int, session: Session = Depends(get_session)):
    repository = SQLOrderDetailRepository(session)
    use_case = DeleteOrderDetailUseCase(repository)
    use_case.execute(id)
    return {"message": "Order detail deleted"}

@router.get("/order-details/order/{order_id}")
def get_order_details_by_order_id(order_id: int, session: Session = Depends(get_session)):
    repository = SQLOrderDetailRepository(session)
    use_case = GetOrderDetailsByOrderIdUseCase(repository)
    return use_case.execute(order_id)