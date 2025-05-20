from abc import ABC, abstractmethod
from domain.entities.order_detail import OrderDetail
from typing import List

class OrderDetailRepository(ABC):
    @abstractmethod
    def create(self, detail: OrderDetail) -> OrderDetail:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> OrderDetail:
        pass

    @abstractmethod
    def update(self, detail: OrderDetail) -> OrderDetail:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def get_by_order_id(self, order_id: int) -> List[OrderDetail]:
        pass