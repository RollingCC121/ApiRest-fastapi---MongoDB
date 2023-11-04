from pydantic import BaseModel

class Cargador(BaseModel):
    estado: str
    autobus_id: str
    hora_inicio: str
    hora_fin: str

