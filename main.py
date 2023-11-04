from fastapi import FastAPI
from rutas.RutaCargador import ruta_cargador

app = FastAPI()

app.include_router(ruta_cargador)