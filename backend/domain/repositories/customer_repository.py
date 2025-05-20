from abc import ABC, abstractmethod
from domain.entities.customer import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def create(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Customer:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass