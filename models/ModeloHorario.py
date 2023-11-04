from pydantic import BaseModel

class Horario(BaseModel):
    dia_semana: str
    hora_inicio: str
    hora_fin: str
    tipo_horario: str


    
    