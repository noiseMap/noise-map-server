from rest_framework.serializers import ModelSerializer

from apps.noisedata.models import NoiseData

class NoiseDataSerializer(ModelSerializer):
    # TODO: use for geo data
    # from rest_framework_gis.serializers import GeoFeatureModelSerializer
    
    class Meta:
        model = NoiseData
        #geo_field = "center"
        
        fields = '__all__'