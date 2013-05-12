from django.contrib.gis.db import models

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class Dorm(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True, db_index=True)
    short_name = models.CharField(max_length=100)
    SLUG_LEN = 50
    slug = models.SlugField(max_length=SLUG_LEN+1, blank=True)
    dorm_type = models.CharField(max_length=40, null=True)
    has_ac = models.BooleanField()
    size = models.IntegerField(null=True)
    campus_side = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=60, null=True)
    dining = models.BooleanField()
    female_only = models.BooleanField()
    freshmen_only = models.BooleanField()
    open_gender = models.BooleanField()
    blurb = models.TextField(null=True)
    singles = models.IntegerField(null=True)
    doubles = models.IntegerField(null=True)
    triples = models.IntegerField(null=True)
    cost = models.FloatField(null=True)
    dist_to_tech = models.FloatField(null=True)
    dist_to_norris = models.FloatField(null=True)
    dist_to_bk = models.FloatField(null=True)
    dist_to_kresge = models.FloatField(null=True)
    room_dimensions = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # set the slug if empty
        if not self.slug:
            len = self.SLUG_LEN
            self.slug = slugify(self.short_name)[:len]

        super(Dorm, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('guide.views.detail', kwargs={'dorm_slug': self.slug})

    def get_quotes(self):
       return Quote.objects.filter(dorm=self)

    def get_slideshow(self):
       return SlideshowImage.objects.filter(dorm=self)

class Quote(models.Model):
    name = models.CharField(max_length=255)
    dorm = models.ForeignKey(Dorm, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.name

class SlideshowImage(models.Model):
    """For building slideshows and attaching them to stories"""
    name = models.CharField(max_length=50)
    dorm = models.ForeignKey(Dorm, null=True, blank=True)
    image = models.ImageField(upload_to='static/img/')
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
