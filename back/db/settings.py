MONGO_HOST = 'server'
MONGO_PORT = 27017

MONGO_DBNAME = 'gustaf_db'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'gustaf_episodes': {
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
    },
    'shows': {
        'datasource': {
            'source': 'gustaf_episodes',
            'aggregation': {
                'pipeline': [
                    {'$group': {'_id':'$series'}}
                ]
            }
        }
    },
    'episodes': {
        'datasource': {
            'source': 'gustaf_episodes',
            
        }
    }
}

