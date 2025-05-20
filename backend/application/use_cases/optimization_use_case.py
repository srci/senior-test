from domain.repositories.repair_order_repository import RepairOrderRepository
from domain.repositories.part_repository import PartRepository
from domain.entities.repair_order import RepairOrder
from typing import List, Dict

class OptimizeRepairOrdersUseCase:
    def __init__(self, order_repo: RepairOrderRepository, part_repo: PartRepository):
        self.order_repo = order_repo
        self.part_repo = part_repo

    def execute(self) -> List[RepairOrder]:
        pending_orders = self.order_repo.get_pending_orders()
        pending_orders.sort(key=lambda x: x.prioridad, reverse=True)  # Ordenar por prioridad descendente

        parts_stock = {part.id: part.stock_actual for part in self.part_repo.get_all()}
        selected_orders = []

        for order in pending_orders:
            if self.can_fulfill_order(order, parts_stock):
                selected_orders.append(order)
                self.update_stock(order, parts_stock)

        return selected_orders

    def can_fulfill_order(self, order: RepairOrder, stock: Dict[int, int]) -> bool:
        for detail in order.details:
            if stock.get(detail.id_parte, 0) < detail.cantidad:
                return False
        return True

    def update_stock(self, order: RepairOrder, stock: Dict[int, int]) -> None:
        for detail in order.details:
            stock[detail.id_parte] -= detail.cantidad