from django.urls import path
from . import views
    
urlpatterns = [    
    path('', views.compras, name='compras'), 
    path('nuevo', views.nuevo, name='nuevo'),    
    
    path('comprado/<int:identificador>', views.comprado, name='comprado'),
    path('anadir/<int:identificador>', views.anadir, name='anadir'),
    path('eliminar/<int:identificador>', views.eliminar, name='eliminar'),
]
