MONGO_HOST = 'server'
MONGO_PORT = 27017

MONGO_DBNAME = 'gustaf_db'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'episodes': {
        'allow_unknown': True,
        'default_sort': [('episode', 1)],
        'sorting': True,
        'schema': {
            'title': {
                'type': 'string'
            },
            'season': {
                'type': 'integer'
            },
            'episode': {
                'type': 'integer',
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
    },
    'shows': {
        'datasource': {
            'source': 'episodes',
            'aggregation': {
                'pipeline': [
                    {'$group': {'_id':'$title'}}
                ]
            }
        }
    }
}

