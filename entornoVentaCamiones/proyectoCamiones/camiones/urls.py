from django.urls import path
from .views import CamionesListView, CamionesDetailView, CamionesCreateView, CamionesDeleteView, CamionesUpdateView

urlpatterns = [
    path('', CamionesListView.as_view(), name='listado'),
    path('camiones/<int:pk>', CamionesDetailView.as_view(), name='detalle'),
    path('crearCamiones', CamionesCreateView.as_view(), name='crear'),
    path('borrarCamiones/<int:pk>', CamionesDeleteView.as_view(), name='borrar'),
    path('modificarCamiones/<int:pk>', CamionesUpdateView.as_view(), name='modificar'),
]