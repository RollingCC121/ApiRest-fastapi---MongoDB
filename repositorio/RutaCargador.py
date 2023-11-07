from fastapi import APIRouter, HTTPException, Path, Body
from contexto.db import conn
from datos.schemas import cargadorEntity
from modelo.ModelCargador import  Cargador
from bson import ObjectId




ruta_cargador = APIRouter()

@ruta_cargador.get("/cargador/")
def find_all_cargador():
    cursor = conn.local.cargador.find()
    return [cargadorEntity(item) for item in list(cursor)]
    
@ruta_cargador.get("/cargador/{cargador_id}", response_model=Cargador)
async def get_cargador_by_id(cargador_id: str):
    try:
        cargador = conn.local.cargador.find_one({"_id": ObjectId(cargador_id)})
        if cargador:
            return cargadorEntity(cargador)
        else:
            raise HTTPException(status_code=404, detail="Cargador not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@ruta_cargador.post("/cargador/")
async def create_cargador(cargador_data: Cargador):
    cargador_dict = cargador_data.dict()
    result = conn.local.cargador.insert_one(cargador_dict)

    if result.acknowledged:
        return {"message": "Datos de cargador insertados con éxito"}
    else:
        raise HTTPException(status_code=500, detail="Error al insertar datos de cargador")

@ruta_cargador.put("/cargador/{cargador_id}")
async def update_cargador(
    cargador_id: str = Path(..., title="El _id del cargador que deseas actualizar"),
    cargador_data: Cargador = Body(..., title="Datos del cargador que deseas actualizar")
):
    try:
        cargador_object_id = ObjectId(cargador_id)

        result = conn.local.cargador.update_one(
            {"_id": cargador_object_id},
            {"$set": cargador_data.dict(exclude_unset=True)}
        )

        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Cargador no encontrado")

        return {"message": "Cargador actualizado exitosamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@ruta_cargador.delete("/cargadores/{cargador_id}")
async def delete_cargador(cargador_id: str):
    # Eliminar un documento por _id
    result = conn.local.cargador.delete_one({"_id": ObjectId(cargador_id)})
    if result.deleted_count == 1:
        return {"message": "Cargador eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Cargador no encontrado")
