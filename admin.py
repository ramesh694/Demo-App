from django.contrib import admin
from . import models

# from .models import*

# Register your models here.

admin.site.register(models.student)
admin.site.register(models.course)

