from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Tareas
from django.urls import reverse
 
def tareas(request):
    listaTareas = Tareas.objects.all().order_by('-id').values()
    template = loader.get_template('tareas.html')
    #return HttpResponse(template.render())
    contexto = {
        'tareas' : listaTareas,
    }
    return HttpResponse(template.render(contexto, request))

def realizada(request,identificador):
    tarea = Tareas.objects.get(id=identificador)
    tarea.realizada = True
    tarea.save()
    return HttpResponseRedirect(reverse('tareas'))

def nuevaTarea(request):
    d = request.GET['desc']
    tarea = Tareas(descripcion=d, realizada=False)
    tarea.save()
    return HttpResponseRedirect(reverse('tareas'))

def borrar(request,identificador):
    tarea = Tareas.objects.get(id=identificador)
    tarea.delete()
    return HttpResponseRedirect(reverse('tareas'))
