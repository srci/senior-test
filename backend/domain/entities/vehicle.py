from dataclasses import dataclass

@dataclass
class Vehicle:
    id_cliente: int
    marca: str
    modelo: str
    id: int | None = None
    año: int | None = None
    vin: str | None = None