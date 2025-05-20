from infrastructure.database.models.vehicle_model import VehicleModel
from domain.entities.vehicle import Vehicle
from domain.repositories.vehicle_repository import VehicleRepository
from sqlalchemy.orm import Session

class SQLVehicleRepository(VehicleRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, vehicle: Vehicle) -> Vehicle:
        model = VehicleModel(
            id_cliente=vehicle.id_cliente,
            marca=vehicle.marca,
            modelo=vehicle.modelo,
            año=vehicle.año,
            vin=vehicle.vin
        )
        self.session.add(model)
        self.session.commit()
        vehicle.id = model.id_vehiculo
        return vehicle

    def get_by_id(self, id: int) -> Vehicle:
        model = self.session.query(VehicleModel).filter_by(id_vehiculo=id).first()
        if model:
            return Vehicle(
                id=model.id_vehiculo,
                id_cliente=model.id_cliente,
                marca=model.marca,
                modelo=model.modelo,
                año=model.año,
                vin=model.vin
            )
        return None

    def update(self, vehicle: Vehicle) -> Vehicle:
        model = self.session.query(VehicleModel).filter_by(id_vehiculo=vehicle.id).first()
        if model:
            model.id_cliente = vehicle.id_cliente
            model.marca = vehicle.marca
            model.modelo = vehicle.modelo
            model.año = vehicle.año
            model.vin = vehicle.vin
            self.session.commit()
            return vehicle
        return None

    def delete(self, id: int) -> None:
        model = self.session.query(VehicleModel).filter_by(id_vehiculo=id).first()
        if model:
            self.session.delete(model)
            self.session.commit()