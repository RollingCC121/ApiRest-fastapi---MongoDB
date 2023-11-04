from fastapi import APIRouter, HTTPException, Path, Body
from config.db import conn
from schemas.SchemaAutobus import autobusEntity
from models.ModelAutobus import  Autobus
from bson import ObjectId
from datetime import datetime



ruta_autobus = APIRouter()

@ruta_autobus.get("/autobus/")
def find_all_autobus():
    cursor = conn.local.autobus.find()
    return [autobusEntity(item) for item in list(cursor)]
    
@ruta_autobus.get("/autobus/{autobus_id}", response_model=Autobus)
async def get_autobus_by_id(autobus_id: str):
    try:
        autobus = conn.local.autobus.find_one({"_id": ObjectId(autobus_id)})
        if autobus:
            return autobusEntity(autobus)
        else:
            raise HTTPException(status_code=404, detail="Autobus not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@ruta_autobus.post("/autobus")
async def create_autobus(autobus_data: Autobus):
    # Convierte las cadenas de hora a objetos datetime
    autobus_dict = autobus_data.dict()
    result = conn.local.autobus.insert_one(autobus_dict)

    if result.acknowledged:
        return {"message": "Datos de autobus insertados con éxito"}
    else:
        raise HTTPException(status_code=500, detail="Error al insertar datos de autobus")

@ruta_autobus.put("/autobus/{autobus_id}")
async def update_autobus(
    autobus_id: str = Path(..., title="El _id del autobus que deseas actualizar"),
    autobus_data: Autobus = Body(..., title="Datos del autobus que deseas actualizar")
):
    try:
        # Convierte el _id a tipo ObjectId de MongoDB
        autobus_object_id = ObjectId(autobus_id)

        # Actualiza el documento en la colección cargador
        result = conn.local.autobus.update_one(
            {"_id": autobus_object_id},
            {"$set": autobus_data.dict(exclude_unset=True)}
        )

        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Autobus no encontrado")

        return {"message": "Autobus actualizado exitosamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@ruta_autobus.delete("/autobus/{autobus_id}")
async def delete_autobus(autobus_id: str):
    # Eliminar un documento por _id
    result = conn.local.autobus.delete_one({"_id": ObjectId(autobus_id)})
    if result.deleted_count == 1:
        return {"message": "Autobus eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Autobus no encontrado")
 