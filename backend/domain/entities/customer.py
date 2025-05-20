from dataclasses import dataclass
from typing import Optional

@dataclass
class Customer:
    nombre: str
    apellido: str
    id: int | None = None
    direccion: str | None = None
    telefono: str | None = None
    email: str | None = None