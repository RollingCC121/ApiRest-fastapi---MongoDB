from fastapi import FastAPI
from rutas.RutaCargador import user

app = FastAPI()

app.include_router(user)