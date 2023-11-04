from typing import Optional, List
from datetime import time 

def cargadorEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'estado': item['estado'],
        'autobus_id': item['autobus_id'],
        'hora_inicio': item['hora_inicio'],
        'hora_fin': item['hora_fin']
    }
'''
def cargadorEntity(item) -> dict:
    return {
        'estado': item['estado'],
        'autobus_id': item['autobus'],
        'hora_inicio': item['hora_inicio'],
        'hora_fin': item['hora_fin']
    }

def cargadoresEntity(entity) -> list:
    [cargadorEntity(item) for item in entity]
'''
