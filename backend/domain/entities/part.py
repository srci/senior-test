from dataclasses import dataclass

@dataclass
class Part:
    numero_parte: str
    descripcion: str
    stock_actual: int
    costo: float
    id: int | None = None
    