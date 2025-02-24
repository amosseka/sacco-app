from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from . import models

TokenAdmin.raw_id_fields = ['user']
admin.site.register(models.UserProfile)
