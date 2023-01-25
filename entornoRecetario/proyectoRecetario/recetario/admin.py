from django.contrib import admin

# Register your models here.
from .models import Receta, Categorias

admin.site.register(Receta)
admin.site.register(Categorias)