from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Propositos
from django.urls import reverse
from datetime import datetime,timedelta

#Para mostrar el html basico
def propositos(request):
    lc = Propositos.objects.all()
    fechaHoy = datetime.now().date()
    context = {
        'propositos': lc,
        'fechaHoy': fechaHoy,
    }
    plantilla = loader.get_template('propositos.html')
    return HttpResponse(plantilla.render(context, request))

#Para añadir un nuevo elemento
def nuevo(request):
    prop = request.GET['proposito']
    fech = request.GET['fechaObjetivo']

    propos = Propositos(proposito=prop,fechaObjetivo=fech,conseguido=False)
    propos.save()

    return HttpResponseRedirect(reverse('propositos'))

#Para marcar como terminado el Proposito
def terminado(request,identificador):
    propo = Propositos.objects.get(id=identificador)
    propo.conseguido = True
    propo.save()
    return HttpResponseRedirect(reverse('propositos'))

#Para volver a añadir el proposito
def anadir(request,identificador):
    propo = Propositos.objects.get(id=identificador)
    propo.conseguido = False
    propo.save()
    return HttpResponseRedirect(reverse('propositos'))

#Para borrar el proposito
def eliminar(request,identificador):
    props = Propositos.objects.get(id=identificador)
    props.delete()
    return HttpResponseRedirect(reverse('propositos'))

#Cambiar Descripcion del proposito
def modificar(request,identificador):
    mod = identificador
    
    context = {
        'identificador': mod,
    }
    plantilla = loader.get_template('modificar.html')
    return HttpResponse(plantilla.render(context, request))

def modProposito(request,identificador):
    desc = request.GET['proposito']

    propos = Propositos.objects.get(id=identificador)
    if desc != '':
        propos.proposito = desc
        propos.save()

    return HttpResponseRedirect(reverse('propositos'))

#Cambiar Fecha
def cambiar(request,identificador):
    cam = identificador
    
    context = {
        'identificador': cam,
    }
    plantilla = loader.get_template('cambiar.html')
    return HttpResponse(plantilla.render(context, request))

def cambFecha(request,identificador):
    fech = request.GET['fech']
    dias= int(fech)

    propos = Propositos.objects.get(id=identificador)
    if dias > 0:
        fechaObjetivo = propos.fechaObjetivo
        diasTotal = timedelta(days=dias)
        fechNueva = fechaObjetivo + diasTotal
        propos.fechaObjetivo = fechNueva
        propos.save()

    return HttpResponseRedirect(reverse('propositos'))