from abc import ABC, abstractmethod
from domain.entities.part import Part
from typing import List

class PartRepository(ABC):
    @abstractmethod
    def create(self, part: Part) -> Part:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Part:
        pass

    @abstractmethod
    def update(self, part: Part) -> Part:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Part]:
        pass