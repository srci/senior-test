from abc import ABC, abstractmethod
from domain.entities.repair_order import RepairOrder
from typing import List

class RepairOrderRepository(ABC):
    @abstractmethod
    def create(self, order: RepairOrder) -> RepairOrder:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> RepairOrder:
        pass

    @abstractmethod
    def update(self, order: RepairOrder) -> RepairOrder:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def get_pending_orders(self) -> List[RepairOrder]:
        pass