from sqlalchemy import Column, Integer, String, ForeignKey
from infrastructure.database.database import Base

class VehicleModel(Base):
    __tablename__ = 'vehiculos'

    id_vehiculo = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=False)
    marca = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    año = Column(Integer)
    vin = Column(String(17), unique=True)