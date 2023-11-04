from fastapi import FastAPI
from rutas.RutaCargador import ruta_cargador
from rutas.RutaAutobus import ruta_autobus
from rutas.RutaHorario import ruta_horario

app = FastAPI()

app.include_router(ruta_cargador)
app.include_router(ruta_autobus)
app.include_router(ruta_horario)