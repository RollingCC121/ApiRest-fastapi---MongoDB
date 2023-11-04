def cargadorEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'estado': item['estado'],
        'autobus_id': item['autobus_id'],
        'hora_inicio': item['hora_inicio'],
        'hora_fin': item['hora_fin']
    }
