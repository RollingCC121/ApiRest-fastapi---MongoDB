from pydantic import BaseModel
from typing import Optional, List

class CicloCarga(BaseModel):
    autobus_id: str
    hora_inicio: str
    hora_fin: str

class Cargador(BaseModel):
    estado: str
    ciclos_carga: List[CicloCarga]
