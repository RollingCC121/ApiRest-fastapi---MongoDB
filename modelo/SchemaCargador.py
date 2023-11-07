def cargadorEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'nombre':str(item['_id']),
        'estado': item['estado']
        
    }
