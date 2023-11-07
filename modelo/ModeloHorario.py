from datetime import time
from typing import Optional
from pydantic import BaseModel
'''
class Horario(BaseModel):
    dia_semana: str
    hora_inicio: time
    hora_fin: time
    hora_pico: str
'''

class Horario(BaseModel):
    dia_semana: str
    hora_inicio: str
    hora_fin: str
    tipo_horario: Optional[str] = None

'''
    class Config:
        schema_extra = {
            "example": {
                "dia_semana": "lunes",
                "hora_inicio": "08:00:00",
                "hora_fin": "10:00:00"
            }
        }
    '''