def horarioEntity(item) -> dict:
    _id = str(item['_id'])
    dia_semana = str(item['dia_semana'])
    hora_inicio = item['hora_inicio']
    hora_fin = item.get('hora_fin', None)  # Usa .get() para manejar documentos sin 'hora_fin'
    hora_pico = str(item.get('hora_pico', None))  # Usa .get() para manejar documentos sin 'hora_pico'

    return {
        '_id': _id,
        'dia_semana': dia_semana,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'hora_pico': hora_pico
    }

    