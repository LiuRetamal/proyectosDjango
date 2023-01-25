from django.urls import path
from . import views
    
urlpatterns = [    
    path('', views.propositos, name='propositos'), 
    path('nuevo', views.nuevo, name='nuevo'),    
    path('terminado/<int:identificador>', views.terminado, name='terminado'),
    path('anadir/<int:identificador>', views.anadir, name='anadir'),
    path('eliminar/<int:identificador>', views.eliminar, name='eliminar'),
    path('modificar/<int:identificador>', views.modificar, name='modificar'),
    path('modificar/modProposito/<int:identificador>', views.modProposito, name='modProposito'),
    path('cambiar/<int:identificador>', views.cambiar, name='cambiar'),
    path('cambiar/cambFecha/<int:identificador>', views.cambFecha, name='cambFecha'),
]