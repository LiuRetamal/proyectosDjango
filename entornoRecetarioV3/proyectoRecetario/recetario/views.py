from .forms import RecetaForm
from .models import Receta
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Para Mostrar el contenido 
class RecetaListView(ListView):
    model = Receta

# Para ir al detalle de cada empresa
class RecetaDetailView(DetailView):
    model = Receta
    # receta = Receta.objects.get(pk=receta_id)
    # imagen = receta.imagen

# Para crear una nueva empresa
class RecetaCreateView(CreateView):
    model = Receta
    form_class= RecetaForm    
    success_url = reverse_lazy('listado')
    
# Para modificar y borrar una empresa
class RecetaDeleteView(DeleteView):
    model = Receta
    success_url = reverse_lazy('listado')

class RecetaUpdateView(UpdateView):
    model = Receta
    fields = ['nombre','subnombre','ingredientes','imagen', 'receta', 'author', 'categorias']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

