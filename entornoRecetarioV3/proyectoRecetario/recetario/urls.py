from django.urls import path
from .views import RecetaListView, RecetaDetailView, RecetaCreateView, RecetaDeleteView, RecetaUpdateView

urlpatterns = [
    path('', RecetaListView.as_view(), name='listado'),
    path('receta/<int:pk>', RecetaDetailView.as_view(), name='detalle'),
    path('crearReceta', RecetaCreateView.as_view(), name='crear'),
    path('borrarReceta/<int:pk>', RecetaDeleteView.as_view(), name='borrar'),
    path('modificarReceta/<int:pk>', RecetaUpdateView.as_view(), name='modificar'),
]