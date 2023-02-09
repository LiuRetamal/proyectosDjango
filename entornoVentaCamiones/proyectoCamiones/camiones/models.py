from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
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
        
class Camiones(models.Model):
    marca= models.CharField(max_length=200)
    modelo= models.CharField(max_length=200)
    imagen= models.ImageField(verbose_name='Foto camion', upload_to='camiones', null=True)
    descripcion= models.TextField(null=True)
    kilometros= models.CharField(max_length=200)
    precio= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True,verbose_name='Feha de creacion')
    update= models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')
    author= models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categorias,verbose_name="catergorias")
    
    class Meta:
        verbose_name = 'camion'
        verbose_name_plural= "camiones"
        ordering= ['-created']

    # def __str__(self):
    #     return self.nombre