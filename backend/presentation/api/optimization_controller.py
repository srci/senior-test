from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from application.use_cases.optimization_use_case import OptimizeRepairOrdersUseCase
from infrastructure.repositories.sql_repair_order_repository import SQLRepairOrderRepository
from infrastructure.repositories.sql_part_repository import SQLPartRepository
from infrastructure.database.database import get_session

router = APIRouter()

@router.get("/optimize/")
def optimize_repair_orders(session: Session = Depends(get_session)):
    order_repo = SQLRepairOrderRepository(session)
    part_repo = SQLPartRepository(session)
    use_case = OptimizeRepairOrdersUseCase(order_repo, part_repo)
    return use_case.execute()