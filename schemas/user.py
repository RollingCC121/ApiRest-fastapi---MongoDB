def userEntity(item) -> dict:
    return {
        'id': item['id'],
        'name': item['name'],
        'email': item['email'],
        'password': item['pasword']
    }

def usersEntity(entity) -> list:
    [userEntity(item) for item in entity]