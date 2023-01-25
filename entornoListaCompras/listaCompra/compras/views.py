from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Compras
from django.urls import reverse
#Para mostrar el html basico
def compras(request):
    lc = Compras.objects.all()
    context = {
        'compras': lc,
    }
    plantilla = loader.get_template('compras.html')
    return HttpResponse(plantilla.render(context, request))

#Para añadir un nuevo elemento
def nuevo(request):
    prod = request.GET['producto']
    cant = request.GET['cantidad']
    unid = request.GET['unidad']

    compra = Compras(producto=prod,cantidad=cant,unidad=unid,comprado=False)
    compra.save()

    return HttpResponseRedirect(reverse('compras'))

def comprado(request,identificador):
    comp = Compras.objects.get(id=identificador)
    comp.comprado = True
    comp.save()
    return HttpResponseRedirect(reverse('compras'))
def anadir(request,identificador):
    comp = Compras.objects.get(id=identificador)
    comp.comprado = False
    comp.save()
    return HttpResponseRedirect(reverse('compras'))

def eliminar(request,identificador):
    compras = Compras.objects.get(id=identificador)
    compras.delete()
    return HttpResponseRedirect(reverse('compras'))