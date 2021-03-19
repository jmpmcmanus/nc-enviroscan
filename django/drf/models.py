from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.db import models as omodels

# Create your models here.
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

# Create your models here.
class ncwellwise_subset_20102019(models.Model):
    geoid10 = models.TextField(2,null=False)
    arsenic_mean = models.FloatField(null=True)
    arsenic_minimum = models.FloatField(null=True)
    arsenic_maximum = models.FloatField(null=True)
    arsenic_std = models.FloatField(null=True) 
    cadmium_mean = models.FloatField(null=True)
    cadmium_minimum = models.FloatField(null=True)
    cadmium_maximum = models.FloatField(null=True)
    cadmium_std = models.FloatField(null=True)
    lead_mean = models.FloatField(null=True)
    lead_minimum = models.FloatField(null=True)
    lead_maximum = models.FloatField(null=True)
    lead_std = models.FloatField(null=True)
    manganese_mean = models.FloatField(null=True)
    manganese_minimum = models.FloatField(null=True)
    manganese_maximum = models.FloatField(null=True)
    manganese_std = models.FloatField(null=True)

class triangle_tracts(models.Model):
    geom = models.MultiPolygonField(null=True)
    statefp10 = models.TextField(2,null=True)
    countyfp10 = models.TextField(3,null=True)
    tractce10 = models.TextField(6,null=True)
    geoid10 = models.TextField(11,null=True)
    name10 = models.TextField(7,null=True)
    namelsad10 = models.TextField(20,null=True)
    mtfcc10 = models.TextField(5,null=True)
    funcstat10 = models.TextField(1,null=True)
    aland10 = models.FloatField(null=True)
    awater10 = models.FloatField(null=True)
    intptlat10 = models.TextField(11,null=True)
    intptlon10 = models.TextField(12,null=True)
    layer = models.TextField(254,null=True)
    path = models.TextField(254,null=True)

class ncwellwise_subset_20102019_geom(models.Model):
    geoid10 = models.TextField(2,null=False)
    arsenic_mean = models.FloatField(null=True)
    arsenic_minimum = models.FloatField(null=True)
    arsenic_maximum = models.FloatField(null=True)
    arsenic_std = models.FloatField(null=True)
    cadmium_mean = models.FloatField(null=True)
    cadmium_minimum = models.FloatField(null=True)
    cadmium_maximum = models.FloatField(null=True)
    cadmium_std = models.FloatField(null=True)
    lead_mean = models.FloatField(null=True)
    lead_minimum = models.FloatField(null=True)
    lead_maximum = models.FloatField(null=True)
    lead_std = models.FloatField(null=True)
    manganese_mean = models.FloatField(null=True)
    manganese_minimum = models.FloatField(null=True)
    manganese_maximum = models.FloatField(null=True)
    manganese_std = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)

    class Meta:
        managed = False
        db_table = "drf_ncwellwise_subset_20102019_geom"

