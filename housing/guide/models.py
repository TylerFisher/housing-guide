from django.db import models

class Dorm(models.Model):
    dorm_type = models.CharField(max_length=40)
    has_ac = models.BooleanField()
    size = models.IntegerField()
    campus_side = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    dining = models.BooleanField()
    female_only = models.BooleanField()
    freshmen_only = models.BooleanField()
    open_gender = models.BooleanField()
    percent_freshmen = models.FloatField()
    percent_sophomores = models.FloatField()
    percent_juniors = models.FloatField()
    percent_seniors = models.FloatField()
    style = models.CharField(max_length=10)
    blurb = models.TextField()
    singles = models.IntegerField()
    doubles = models.IntegerField()
    cost = models.FloatField()
    master = models.CharField(max_length=40)
    dist_to_tech = models.FloatField()
    dist_to_norris = models.FloatField()
    dist_to_bk = models.FloatField()
    dist_to_kresge = models.FloatField()

    @classmethod

    def get_quotes(self):
       return Quote.objects.filter(story=self)

class Quote(models.Model):
    text = models.TextField()
    source = models.TextField()
    dorm = models.ForeignKey(Dorm, null=True, blank=True)
    def __unicode__(self):
        return self.name

class Room(models.Model):
    room_type = models.CharField(max_length=10)
    dorm = models.ManyToManyField('Dorm')
    sq_ft = models.IntegerField()
    # shape = models.JSONField()

