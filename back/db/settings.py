MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'gustaf'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'episode': {

    }
}

episode_schema = {
    'show': {
        'type': 'string'
    },
    'season_number': {
        'type': 'integer'
    },
    'episode_number': {
        'type': 'integer'
    },
    'path':{
        'type': 'string'
    },
    'subtitles': {
        'type': 'list',
        'schema': {
            'type': 'string'
        }
    }
}