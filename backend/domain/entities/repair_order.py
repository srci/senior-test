from dataclasses import dataclass
from datetime import date
from typing import List
from domain.entities.order_detail import OrderDetail

@dataclass
class RepairOrder:
    id_vehiculo: int
    fecha_inicio: date
    estado: str
    mano_de_obra: float
    prioridad: int
    details: List[OrderDetail]
    id: int | None = None
    fecha_fin: date | None = None