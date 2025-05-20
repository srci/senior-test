from sqlalchemy import Column, Integer, String, Float
from infrastructure.database.database import Base

class PartModel(Base):
    __tablename__ = 'partes'

    id_parte = Column(Integer, primary_key=True, autoincrement=True)
    numero_parte = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=False)
    stock_actual = Column(Integer, nullable=False)
    costo = Column(Float, nullable=False)