# admin.py in your Django app directory
from django.contrib import admin
from .models import APIKey

# Register your models here.
admin.site.register(APIKey)
