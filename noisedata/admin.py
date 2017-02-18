from django.contrib import admin

from .models import Dummy
from .models import NoiseData

default_site = admin.site

default_site.register(Dummy)
default_site.register(NoiseData)
