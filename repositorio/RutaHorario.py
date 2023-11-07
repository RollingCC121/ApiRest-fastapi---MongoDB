from fastapi import APIRouter, HTTPException, Path, Body
from contexto.db import conn
from datos.schemas import horarioEntity
from modelo.ModeloHorario import  Horario
from bson import ObjectId
from servicio.ValidacionesHorario import HorarioValidations


ruta_horario = APIRouter()

@ruta_horario.get("/horario/")
def find_all_cargador():
    cursor = conn.local.horario.find()
    horarios = [horarioEntity(item) for item in cursor]
    return horarios
    
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

@ruta_horario.post("/horario", response_model=HorarioValidations)
async def create_horario(horario: HorarioValidations):
    try:
        horario_dict = horario.dict()
        resultado = conn.local.horario.insert_one(horario_dict)
        
        # Verifica que se haya insertado correctamente y devuelve el objeto insertado
        if resultado.acknowledged:
            return horario
        else:
            raise HTTPException(status_code=500, detail="No se pudo insertar el horario en la base de datos")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@ruta_horario.put("/horario/{horario_id}")
async def update_horario(
    horario_id: str = Path(..., title="El _id del horario que deseas actualizar"),
    horario_data: Horario = Body(..., title="Datos del horario que deseas actualizar")
):
    try:
        horario_object_id = ObjectId(horario_id)

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
