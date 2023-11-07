from pydantic import BaseModel

class Funcionamiento(BaseModel):
    horario_id: str
    autobus_id: str
    cargador_id: str
    
