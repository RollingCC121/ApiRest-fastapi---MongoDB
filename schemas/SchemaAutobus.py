
def autobusEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'estado': item['estado'],
    }