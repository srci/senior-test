from domain.entities.vehicle import Vehicle
from domain.repositories.vehicle_repository import VehicleRepository

class CreateVehicleUseCase:
    def __init__(self, repository: VehicleRepository):
        self.repository = repository

    def execute(self, id_cliente, marca, modelo, año, vin):
        vehicle = Vehicle(id_cliente=id_cliente, marca=marca, modelo=modelo, año=año, vin=vin)
        return self.repository.create(vehicle)

class GetVehicleByIdUseCase:
    def __init__(self, repository: VehicleRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.get_by_id(id)

class UpdateVehicleUseCase:
    def __init__(self, repository: VehicleRepository):
        self.repository = repository

    def execute(self, vehicle: Vehicle):
        return self.repository.update(vehicle)

class DeleteVehicleUseCase:
    def __init__(self, repository: VehicleRepository):
        self.repository = repository

    def execute(self, id: int):
        self.repository.delete(id)