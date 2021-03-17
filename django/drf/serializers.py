#from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import ncwellwise_subset_20102019, triangle_tracts, ncwellwise_subset_20102019_geom, Powerline, drf_mscnt, drf_mscnt_Timestamp, drf_mscnt_Jobid, drf_gcmv, drf_gcmv_Timestamp, drf_gcmv_Jobid
from drf_queryfields import QueryFieldsMixin

class ncwellwise_subset_20102019_Serializer(QueryFieldsMixin,):
    class Meta:
        model = ncwellwise_subset_20102019
        id_field = 'id'
        fields = ('id', 'geoid10','arsenic_mean','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_minimum','manganese_maximum','manganese_std')

class triangle_tracts_Serializer(QueryFieldsMixin,):
    class Meta:
        model = triangle_tracts
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'statefp10', 'countyfp10', 'tractce10', 'geoid10', 'name10', 'namelsad10', 'mtfcc10', 'funcstat10', 'aland10', 'awater10', 'intptlat10', 'intptlon10', 'layer', 'path')

class ncwellwise_subset_20102019_geom_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ncwellwise_subset_20102019_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'geoid10','arsenic_mean','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_minimum','manganese_maximum','manganese_std')

class Powerline_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Powerline
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'title', 'powerline', 'voltage', 'service_date')

class drf_mscnt_Serializer(QueryFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = drf_mscnt
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'bore_id', 'job_id', 'instrument', 'chemical_id', 'measurement_value',
                  'units', 'timestamp', 'status', 'comment')

class drf_mscnt_Timestamp_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = drf_mscnt_Timestamp
        id_field = 'id'
        fields = ('__all__')

class drf_mscnt_Jobid_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = drf_mscnt_Jobid
        id_field = 'id'
        fields = ('__all__')

class drf_gcmv_Serializer(QueryFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = drf_gcmv
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'bore_id', 'job_id', 'instrument', 'chemical_id', 'measurement_value',
                  'units', 'timestamp', 'status', 'comment')

class drf_gcmv_Timestamp_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = drf_gcmv_Timestamp
        id_field = 'id'
        fields = ('__all__')

class drf_gcmv_Jobid_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = drf_gcmv_Jobid
        id_field = 'id'
        fields = ('__all__')

