from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Categorias(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion= models.TextField(null=True)
    created= models.DateTimeField(auto_now_add=True,verbose_name='Feha de creacion')
    update= models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural= "categorias"
        ordering= ['-created']

    def __str__(self):
        return self.nombre
        
class Receta(models.Model):
    nombre= models.CharField(max_length=200)
    subnombre= models.CharField(max_length=200,null=True)
    imagen= models.ImageField(verbose_name='Foto receta', upload_to='recetario')
    ingredientes= models.TextField(null=True)
    receta= models.TextField(null=True)
    created= models.DateTimeField(auto_now_add=True,verbose_name='Feha de creacion')
    update= models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')
    author= models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categorias,verbose_name="catergorias")
    
    class Meta:
        verbose_name = 'receta'
        verbose_name_plural= "recetas"
        ordering= ['-created']

    def __str__(self):
        return self.nombre