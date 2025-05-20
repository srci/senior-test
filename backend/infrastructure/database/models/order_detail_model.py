from sqlalchemy import Column, Integer, ForeignKey
from infrastructure.database.database import Base

class OrderDetailModel(Base):
    __tablename__ = 'detalles_orden'

    id_detalle = Column(Integer, primary_key=True, autoincrement=True)
    id_orden = Column(Integer, ForeignKey('ordenes_de_reparacion.id_orden'), nullable=False)
    id_parte = Column(Integer, ForeignKey('partes.id_parte'), nullable=False)
    cantidad = Column(Integer, nullable=False)