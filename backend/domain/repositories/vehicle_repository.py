from abc import ABC, abstractmethod
from domain.entities.vehicle import Vehicle

class VehicleRepository(ABC):
    @abstractmethod
    def create(self, vehicle: Vehicle) -> Vehicle:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Vehicle:
        pass

    @abstractmethod
    def update(self, vehicle: Vehicle) -> Vehicle:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass