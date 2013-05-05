from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand, CommandError

from guide.models import DormShapes

class Command(BaseCommand):
	shapefile = 'shapes/osm/osm.shp'
	
	mapping = {
		'osm_id' : 'osm_id', 
		"name" : "name", 
		'poly' : 'MULTIPOLYGON'}

	def handle(self, *args, **kwargs):
		lm = LayerMapping(DormShapes, self.shapefile, self.mapping)
		lm.save(verbose=True)