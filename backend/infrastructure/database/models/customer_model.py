# infrastructure/database/models/customer_model.py
from sqlalchemy import Column, Integer, String
from infrastructure.database.database import Base

class CustomerModel(Base):
    __tablename__ = 'clientes'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    direccion = Column(String(255))
    telefono = Column(String(50))
    email = Column(String(255))