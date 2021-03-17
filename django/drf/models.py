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

class Powerline(models.Model):
    #id = models.IntegerField(primary_key=True)
    geom = models.MultiLineStringField(null=False)
    title = models.TextField(50,null=False)
    powerline = models.TextField(20,null=False)
    voltage = models.IntegerField(null=False)
    service_date = models.TextField(10,null=True)
    #MONTH_DAY_YEAR = '%m/%d/%Y'
    #MONTH_YEAR = '%m/%Y'
    #DATE_CHOICE= (
    #              (MONTH_DAY_YEAR, 'Month Day Year'),
    #              (MONTH_YEAR, 'Month Year')
    #             )
    #service_date = models.CharField('Date Choice', choices=DATE_CHOICE,  max_length=10, null=False)


class drf_mscnt(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.CharField(max_length=20)
    bore_id = models.CharField(max_length=20)
    instrument = models.CharField(max_length=20)
    chemical_id = models.CharField(max_length=20)
    measurement_value = models.CharField(max_length=20)
    units = models.CharField(max_length=20)
    timestamp = models.DateTimeField(null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    comment = models.CharField(max_length=1000, null=True, default="")
    geom = models.PointField(null=False)

    class Meta:
        managed = False
        db_table = "drf_mscnt"

class drf_mscnt_Timestamp(omodels.Model):
    id = models.DateTimeField(null=False,primary_key=True)
    label = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = "drf_mscnt_timestamp"

class drf_mscnt_Jobid(omodels.Model):
    id = models.TextField(10,null=False,primary_key=True)
    label = models.TextField(10,null=False)

    class Meta:
        managed = False
        db_table = "drf_mscnt_jobid"

class drf_gcmv(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.CharField(max_length=20)
    bore_id = models.CharField(max_length=20)
    instrument = models.CharField(max_length=20)
    chemical_id = models.CharField(max_length=20)
    measurement_value = models.CharField(max_length=20)
    units = models.CharField(max_length=20)
    timestamp = models.DateTimeField(null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    comment = models.CharField(max_length=1000, null=True, default="")
    geom = models.PointField(null=False)

    class Meta:
        managed = False
        db_table = "drf_gcmv"

class drf_gcmv_Timestamp(omodels.Model):
    id = models.DateTimeField(null=False,primary_key=True)
    label = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = "drf_gcmv_timestamp"

class drf_gcmv_Jobid(omodels.Model):
    id = models.TextField(10,null=False,primary_key=True)
    label = models.TextField(10,null=False)

    class Meta:
        managed = False
        db_table = "drf_gcmv_jobid"

