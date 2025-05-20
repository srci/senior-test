from dataclasses import dataclass

@dataclass
class OrderDetail:
    id_orden: int
    id_parte: int
    cantidad: int
    id: int | None = None