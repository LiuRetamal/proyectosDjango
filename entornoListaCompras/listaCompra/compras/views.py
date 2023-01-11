from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Compras
 
def compras(request):
    lc = Compras.objects.all()
    context = {
        'compras': lc,
    }
    plantilla = loader.get_template('compras.html')
    return HttpResponse(plantilla.render(context, request))

