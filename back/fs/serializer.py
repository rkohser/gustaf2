from json import JSONEncoder
from babelfish import Language

class GustafSerializer(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Language):
            return obj.alpha3
        return json.JSONEncoder.default(self, obj)