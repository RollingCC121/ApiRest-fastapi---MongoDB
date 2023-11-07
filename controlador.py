from fastapi import FastAPI
from repositorio.RutaCargador import ruta_cargador
from repositorio.RutaAutobus import ruta_autobus
from repositorio.RutaHorario import ruta_horario
from repositorio.RutaFuncionamiento import ruta_funcionamiento

app = FastAPI()

app.include_router(ruta_cargador)
app.include_router(ruta_autobus)
app.include_router(ruta_horario)
app.include_router(ruta_funcionamiento)