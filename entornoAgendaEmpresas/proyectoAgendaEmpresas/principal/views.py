# from django.shortcuts import render, get_list_or_404
# from django.http import HttpResponse
# from django.template import loader
from .models import Empresas
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Para Mostrar el contenido 
class EmpresaListView(ListView):
    model = Empresas

# Para ir al detalle de cada empresa
class EmpresaDetailView(DetailView):
    model = Empresas

# Para crear una nueva empresa
class EmpresaCreateView(CreateView):
    model = Empresas
    fields = ['nombre','tipo','direccion','telefono','personaContacto']
    success_url = reverse_lazy('listado')
    
# Para modificar y borrar una empresa
class EmpresaDeleteView(DeleteView):
    model = Empresas
    success_url = reverse_lazy('listado')

class EmpresaUpdateView(UpdateView):
    model = Empresas
    fields = ['nombre','tipo','direccion','telefono','personaContacto']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')






# def listado(request):
#     #modelo
#     empresas = get_list_or_404(Empresas)
#     #contexto
#     context = {
#         'empresas': empresas,
#     }
#     #templates
#     listadoHTML = loader.get_template('principal/listado.html')
#     return HttpResponse(listadoHTML.render(context, request))

