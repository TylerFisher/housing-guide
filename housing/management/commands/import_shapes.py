from django.contrib.gis.utils import LayerMapping
from guide.models import DormShapes

shape = 'shapes/osm/osm.shp'

mapping = {'osm_id' : 'osm_id', "name" : "name", 'poly' : 'MULTIPOLYGON'}

lm = LayerMapping(DormShapes, shape, mapping)
