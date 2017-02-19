from django.conf.urls import include, url
from rest_framework import routers

from . import views


default_router = routers.DefaultRouter()
default_router.register(r'noisedata', views.NoiseDataViewSet)

urlpatterns = [
    url(r'^v1/', include(default_router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]