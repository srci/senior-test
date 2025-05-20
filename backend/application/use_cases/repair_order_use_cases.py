from domain.entities.repair_order import RepairOrder
from domain.repositories.repair_order_repository import RepairOrderRepository
from typing import List

class CreateRepairOrderUseCase:
    def __init__(self, repository: RepairOrderRepository):
        self.repository = repository

    def execute(self, id_vehiculo, fecha_inicio, fecha_fin, estado, mano_de_obra, prioridad, details=None):
        order = RepairOrder(
            id_vehiculo=id_vehiculo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            estado=estado,
            mano_de_obra=mano_de_obra,
            prioridad=prioridad,
            details=details or []
        )
        return self.repository.create(order)

class GetRepairOrderByIdUseCase:
    def __init__(self, repository: RepairOrderRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.get_by_id(id)

class UpdateRepairOrderUseCase:
    def __init__(self, repository: RepairOrderRepository):
        self.repository = repository

    def execute(self, order: RepairOrder):
        return self.repository.update(order)

class DeleteRepairOrderUseCase:
    def __init__(self, repository: RepairOrderRepository):
        self.repository = repository

    def execute(self, id: int):
        self.repository.delete(id)

class GetPendingRepairOrdersUseCase:
    def __init__(self, repository: RepairOrderRepository):
        self.repository = repository

    def execute(self) -> List[RepairOrder]:
        return self.repository.get_pending_orders()