MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'gustaf'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'episodes': {
        'allow_unknown': True,
        'schema': {
            'title': {
                'type': 'string'
            },
            'season': {
                'type': 'integer'
            },
            'episode': {
                'type': [
                    'integer',
                    'list'
                ]
            },
            'subtitle_language': {
                'type': 'string'
            },
            'type': {
                'type': 'string'
            },
            'dir': {
                'type': 'string'
            },
            'filename': {
                'type': 'string'
            }
        }
    }
}

