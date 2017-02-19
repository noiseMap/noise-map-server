from rest_framework import viewsets
from apps.noisedata.models import NoiseData
from .serializers import NoiseDataSerializer

class NoiseDataViewSet(viewsets.ModelViewSet):
    queryset = NoiseData.objects.all()
    serializer_class = NoiseDataSerializer