from pydantic import BaseModel

class Autobus(BaseModel):
    nombre: str
    estado: str


