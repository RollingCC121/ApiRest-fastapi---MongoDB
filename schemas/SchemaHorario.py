def horarioEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'dia_semana': item['dia_semana'],
        'hora_inicio': item['hora_inicio'],
        'hora_fin': item['hora_fin'],
        'tipo_horario': item['tipo_horario']
    }