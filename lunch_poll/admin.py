from django.contrib import admin

from .models import import Lunch, Location

admin.site.register(Lunch)
admin.site.register(Location)