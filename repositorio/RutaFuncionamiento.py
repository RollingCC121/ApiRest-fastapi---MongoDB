from fastapi import APIRouter, HTTPException, Path, Body
from contexto.db import conn
from modelo.SchemaFuncionamiento import funcionamientoEntity
from modelo.ModelFuncionamiento import  Funcionamiento
from bson import ObjectId
from datetime import datetime



ruta_funcionamiento = APIRouter()

@ruta_funcionamiento.get("/funcionamiento/")
def find_all_funcionamiento():
    cursor = conn.local.funcionamiento.find()
    return [funcionamientoEntity(item) for item in list(cursor)]
    
@ruta_funcionamiento.get("/funcionamiento/{funcionamiento_id}", response_model=Funcionamiento)
async def get_funcionamiento_by_id(funcionamiento_id: str):
    try:
        funcionamiento = conn.local.funcionamiento.find_one({"_id": ObjectId(funcionamiento_id)})
        if funcionamiento:
            return funcionamientoEntity(funcionamiento)
        else:
            raise HTTPException(status_code=404, detail="Funcionamiento not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@ruta_funcionamiento.post("/funcionamiento/")
async def create_funcionamiento(funcionamiento_data: Funcionamiento):
    funcionamiento_dict = funcionamiento_data.dict()
    result = conn.local.funcionamiento.insert_one(funcionamiento_dict)

    if result.acknowledged:
        return {"message": "Datos de funcionamiento insertados con éxito"}
    else:
        raise HTTPException(status_code=500, detail="Error al insertar datos de funcionamiento")

@ruta_funcionamiento.put("/funcionamiento/{funcionamiento_id}")
async def update_funcionamiento(
    funcionamiento_id: str = Path(..., title="El _id del funcionamiento que deseas actualizar"),
    funcionamiento_data: Funcionamiento = Body(..., title="Datos del funcionamiento que deseas actualizar")
):
    try:
        funcionamiento_object_id = ObjectId(funcionamiento_id)

        result = conn.local.funcionamiento.update_one(
            {"_id": funcionamiento_object_id},
            {"$set": funcionamiento_data.dict(exclude_unset=True)}
        )

        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Funcionamiento encontrado")

        return {"message": "Funcionamiento actualizado exitosamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@ruta_funcionamiento.delete("/funcionamiento/{funcionamiento_id}")
async def delete_funcionamiento(funcionamiento_id: str):
    # Eliminar un documento por _id
    result = conn.local.funcionamiento.delete_one({"_id": ObjectId(funcionamiento_id)})
    if result.deleted_count == 1:
        return {"message": "Funcionamiento eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Funcionamiento no encontrado")
