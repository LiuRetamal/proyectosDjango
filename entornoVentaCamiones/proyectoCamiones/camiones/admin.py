from django.contrib import admin

# Register your models here.
from .models import Camiones, Categorias

admin.site.register(Camiones)
admin.site.register(Categorias)