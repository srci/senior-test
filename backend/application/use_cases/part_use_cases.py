from domain.entities.part import Part
from domain.repositories.part_repository import PartRepository
from typing import List

class CreatePartUseCase:
    def __init__(self, repository: PartRepository):
        self.repository = repository

    def execute(self, numero_parte, descripcion, stock_actual, costo):
        part = Part(numero_parte=numero_parte, descripcion=descripcion, stock_actual=stock_actual, costo=costo)
        return self.repository.create(part)

class GetPartByIdUseCase:
    def __init__(self, repository: PartRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.get_by_id(id)

class UpdatePartUseCase:
    def __init__(self, repository: PartRepository):
        self.repository = repository

    def execute(self, part: Part):
        return self.repository.update(part)

class DeletePartUseCase:
    def __init__(self, repository: PartRepository):
        self.repository = repository

    def execute(self, id: int):
        self.repository.delete(id)

class GetAllPartsUseCase:
    def __init__(self, repository: PartRepository):
        self.repository = repository

    def execute(self) -> List[Part]:
        return self.repository.get_all()