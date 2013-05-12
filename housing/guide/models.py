from django.contrib.gis.db import models

class Dorm(models.Model):
    name = models.CharField(max_length=255, null=True)
    short_name = models.CharField(max_length=100)
    dorm_type = models.CharField(max_length=40, null=True)
    has_ac = models.BooleanField()
    size = models.IntegerField(null=True)
    campus_side = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=60, null=True)
    dining = models.BooleanField()
    female_only = models.BooleanField()
    freshmen_only = models.BooleanField()
    open_gender = models.BooleanField()
    style = models.CharField(max_length=10, null=True)
    blurb = models.TextField(null=True)
    singles = models.IntegerField(null=True)
    doubles = models.IntegerField(null=True)
    cost = models.FloatField(null=True)
    master = models.CharField(max_length=40, null=True)
    dist_to_tech = models.FloatField(null=True)
    dist_to_norris = models.FloatField(null=True)
    dist_to_bk = models.FloatField(null=True)
    dist_to_kresge = models.FloatField(null=True)
    room_dimensions = models.CharField(max_length=255, null=True)

    @classmethod
    def get_quotes(self):
       return Quote.objects.filter(story=self)

    def get_slideshow(self):
       return SlideshowImage.objects.filter(story=self)

class Quote(models.Model):
    text = models.TextField()
    source = models.TextField()
    dorm = models.ForeignKey(Dorm, null=True, blank=True)
    def __unicode__(self):
        return self.name

class SlideshowImage(models.Model):
    """For building slideshows and attaching them to stories"""
    name = models.CharField(max_length=50)
    story = models.ForeignKey(Dorm, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    caption = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.name

class DormShapes(models.Model):
    """OSM shapefiles attributes"""
    osm_id = models.FloatField()
    name = models.CharField(max_length=255)

    """GeoDjango-specific overrides"""
    poly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s' % (self.name, self.poly)
