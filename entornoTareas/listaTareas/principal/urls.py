from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.tareas, name='tareas'), 
    path('realizada/<int:identificador>', views.realizada, name='realizada'),
    path('nuevaTarea/', views.nuevaTarea, name='nuevaTarea'), 
    path('borrar/<int:identificador>', views.borrar, name='borrar'), 
]
