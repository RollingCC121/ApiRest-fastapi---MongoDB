def funcionamientoEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'horario_id': item['horario_id'],
        'autobus_id': item['autobus_id'],
        'cargador_id': item['cargador_id']
        
    }