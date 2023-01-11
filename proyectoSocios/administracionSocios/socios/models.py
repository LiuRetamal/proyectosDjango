from django.db import models

class Socios(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255) #VARCHAR 255

