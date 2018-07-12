from flask_restplus import fields
from helloSuggestions import host, Tuple
from helloSuggestions.core import PlaceScore

placeDtoDescription = host.api.model('Geographical place name', {
    'name': fields.String(required=True, description='name of geographical point (utf8)'),
    'latitude': fields.String(required=True, description='latitude in decimal degrees (wgs84)'),
    'longitude': fields.String(required=True, description='longitude in decimal degrees (wgs84)'),
    'score': fields.Float(required=True, readOnly=True, description='relevance score of the result'),
})

suggestionsDtoDescription = host.api.model("Autocomplete suggestions", {
    'suggestions': fields.List(fields.Nested(placeDtoDescription), required=True, description='List of places ordered by score')
})

class PlaceDto(object):

    def __init__(self, name: str, latitude: str, longitude: str, score: float):
        self.name : str = name
        self.latitude : str = latitude
        self.longitude : str = longitude
        self.score: float = score

class PlaceDtoMapper(object):

    def toDto(self, entity: PlaceScore) -> PlaceDto:
        return PlaceDto(name=entity.place.name, 
                        latitude=str(entity.place.latitude), 
                        longitude=str(entity.place.longitude), 
                        score=entity.score)