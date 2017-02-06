from django.contrib import admin

from .models import Dummy
default_site = admin.site

default_site.register(Dummy)
