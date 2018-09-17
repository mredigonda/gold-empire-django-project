from django.contrib import admin
from django.contrib.auth.models import User

from .models import Resource, Building, Unit, Attack

admin.site.register(Resource)
admin.site.register(Building)
admin.site.register(Unit)
admin.site.register(Attack)