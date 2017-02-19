from rest_framework_gis.serializers import GeoFeatureModelSerializer

from apps.noisedata.models import NoiseData

class NoiseDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = NoiseData
        geo_field = "center"
        
        fields = ('id', 'center', 'noise_mean_day')