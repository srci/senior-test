from domain.entities.order_detail import OrderDetail
from domain.repositories.order_detail_repository import OrderDetailRepository
from typing import List

class CreateOrderDetailUseCase:
    def __init__(self, repository: OrderDetailRepository):
        self.repository = repository

    def execute(self, id_orden, id_parte, cantidad):
        detail = OrderDetail(id_orden=id_orden, id_parte=id_parte, cantidad=cantidad)
        return self.repository.create(detail)

class GetOrderDetailByIdUseCase:
    def __init__(self, repository: OrderDetailRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.get_by_id(id)

class UpdateOrderDetailUseCase:
    def __init__(self, repository: OrderDetailRepository):
        self.repository = repository

    def execute(self, detail: OrderDetail):
        return self.repository.update(detail)

class DeleteOrderDetailUseCase:
    def __init__(self, repository: OrderDetailRepository):
        self.repository = repository

    def execute(self, id: int):
        self.repository.delete(id)

class GetOrderDetailsByOrderIdUseCase:
    def __init__(self, repository: OrderDetailRepository):
        self.repository = repository

    def execute(self, order_id: int) -> List[OrderDetail]:
        return self.repository.get_by_order_id(order_id)