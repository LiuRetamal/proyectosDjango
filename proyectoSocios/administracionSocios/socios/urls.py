from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo/', views.nuevo, name='nuevo'),
    path('nuevo/nuevoregistro/', views.nuevoregistro, name='nuevoregistro'),
    path('borrar/<int:identificador>', views.borrar, name='borrar'),
    path('modificar/<int:identificador>', views.modificar, name='modificar'),
    path('modificar/modificaregistro/<int:identificador>', views.modificaregistro, name='modificaregistro'),
]