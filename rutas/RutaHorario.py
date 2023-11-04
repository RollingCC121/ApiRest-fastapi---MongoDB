from fastapi import APIRouter, HTTPException, Path, Body
from config.db import conn
from schemas.SchemaHorario import horarioEntity
from models.ModeloHorario import  Horario
from bson import ObjectId
from datetime import datetime



ruta_horario = APIRouter()

@ruta_horario.get("/horario/")
def find_all_cargador():
    cursor = conn.local.horario.find()
    return [horarioEntity(item) for item in list(cursor)]
    
@ruta_horario.get("/horario/{horario_id}", response_model=Horario)
async def get_horario_by_id(horario_id: str):
    try:
        horario = conn.local.horario.find_one({"_id": ObjectId(horario_id)})
        if horario:
            return horarioEntity(horario)
        else:
            raise HTTPException(status_code=404, detail="Horario not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@ruta_horario.post("/horario")
async def create_horario(horario_data: Horario):
    # Convierte las cadenas de hora a objetos datetime
    hora_inicio = datetime.strptime(horario_data.hora_inicio, "%H:%M:%S")
    hora_fin = datetime.strptime(horario_data.hora_fin, "%H:%M:%S")
    horario_dict = horario_data.dict()
    result = conn.local.horario.insert_one(horario_dict)

    if result.acknowledged:
        return {"message": "Datos de horario insertados con éxito"}
    else:
        raise HTTPException(status_code=500, detail="Error al insertar datos de horario")

@ruta_horario.put("/horario/{horario_id}")
async def update_horario(
    horario_id: str = Path(..., title="El _id del horario que deseas actualizar"),
    horario_data: Horario = Body(..., title="Datos del horario que deseas actualizar")
):
    try:
        # Convierte el _id a tipo ObjectId de MongoDB
        horario_object_id = ObjectId(horario_id)

        # Actualiza el documento en la colección cargador
        result = conn.local.horario.update_one(
            {"_id": horario_object_id},
            {"$set": horario_data.dict(exclude_unset=True)}
        )

        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Horario no encontrado")

        return {"message": "Horario actualizado exitosamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@ruta_horario.delete("/horario/{horario_id}")
async def delete_horario(horario_id: str):
    # Eliminar un documento por _id
    result = conn.local.horario.delete_one({"_id": ObjectId(horario_id)})
    if result.deleted_count == 1:
        return {"message": "Horario eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
