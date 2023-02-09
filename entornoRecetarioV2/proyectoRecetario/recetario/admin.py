from django.contrib import admin

# Register your models here.
from .models import Receta, Categorias

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display= ('nombre','subnombre','author')
    ordering =('nombre','author')
    search_fields =('nombre','subnombre','author__username','categorias__nombre')

admin.site.register(Receta,RecetaAdmin)
admin.site.register(Categorias)