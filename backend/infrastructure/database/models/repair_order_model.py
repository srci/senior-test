from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from infrastructure.database.database import Base

class RepairOrderModel(Base):
    __tablename__ = 'ordenes_de_reparacion'

    id_orden = Column(Integer, primary_key=True, autoincrement=True)
    id_vehiculo = Column(Integer, ForeignKey('vehiculos.id_vehiculo'), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)
    estado = Column(String(20), nullable=False)
    mano_de_obra = Column(Float, nullable=False)
    prioridad = Column(Integer, nullable=False, default=1)