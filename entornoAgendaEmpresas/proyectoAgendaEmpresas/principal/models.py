from django.db import models

# Create your models here.
class Empresas(models.Model):
    nombre = models.CharField(max_length=255,verbose_name='nombre')
    tipo = models.CharField(max_length=255,verbose_name='tipo')
    direccion = models.CharField(max_length=255,verbose_name='direccion')
    telefono = models.CharField(max_length=255,verbose_name='telefono')
    personaContacto = models.CharField(max_length=255,verbose_name='persona de contacto')
    created = models.DateTimeField(auto_now_add=True ,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True ,verbose_name='Fecha de modificación')

    def __str__(self) -> str:
        return self.nombre
