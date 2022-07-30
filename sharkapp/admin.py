from django.contrib import admin
from .models import Shark, Sighting

# Register your models here.
admin.site.register(Shark)
admin.site.register(Sighting)