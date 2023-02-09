from .forms import CamionesForm
from .models import Camiones
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Para Mostrar el contenido 
class CamionesListView(ListView):
    model = Camiones

# Para ir al detalle de cada empresa
class CamionesDetailView(DetailView):
    model = Camiones
    # receta = Receta.objects.get(pk=receta_id)
    # imagen = receta.imagen


# Para crear una nueva empresa
class CamionesCreateView(CreateView):
    model = Camiones
    form_class= CamionesForm    
    
    success_url = reverse_lazy('listado')
    
# Para modificar y borrar una empresa
class CamionesDeleteView(DeleteView):
    model = Camiones
    success_url = reverse_lazy('listado')

class CamionesUpdateView(UpdateView):
    model = Camiones
    fields = ['marca','modelo','imagen','descripcion', 'kilometros','precio', 'author', 'categorias']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')