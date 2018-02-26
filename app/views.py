# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.db.models import Count, Avg, Max, Min
from django.http import HttpResponse

import urllib
import json

import numpy as np

from rest_framework import viewsets
from .serializers import TemperaturaSerializer

from .models import Temperatura, Month
from pruebas.time_to_ms import time_to_ms


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def home(request):


    #url = "https://api.thingspeak.com/channels/413456/fields/1.json?results=10"
    url = "https://api.thingspeak.com/channels/394387/fields/2.json?results=10"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data
    j = data['feeds']
    v = []
    for i in j:
        if i != None:
            print i['created_at']
            h = (i['created_at'].split("T"))[1]
            print i['field2']
            if i['field2']:
                v.append([h.replace("Z","") ,i['field2']] )



    # Grafico 1
    datos = Temperatura.objects.order_by('-time')[:8]
    tempU = []

    for i in datos:
        aux = str('{0}:{1}').format(i.time.hour-5, i.time.minute)
        tempU.append([aux,i.temperatura])
    tempU.reverse()


    # Grafico 2
    rangos = Temperatura.objects.values('date').annotate(promedio=Avg('temperatura'),minimo=Min('temperatura'),maximo=Max('temperatura'))
    tempRangos = []
    tempAverage = []

    for i in rangos:
        tempRangos.append([time_to_ms(i["date"].strftime('%Y-%m-%d')),i["minimo"] ,i['maximo']])
        tempAverage.append([time_to_ms(i["date"].strftime('%Y-%m-%d')),i["promedio"]])

    return render(request, 'home.html', {'tempU':tempU, 'tempRangos':tempRangos,'tempAverage':tempAverage,'v':v})


def grafico(request):
    if request.POST:
        url_since = request.POST['fechai']
        fechai = url_since.split("-")

        rangos = Temperatura.objects.filter(date__year=fechai[0],date__month=fechai[1],date__day=fechai[2])

        lista_temperatura = []
        box_plot = []

        if not rangos:
            box_plot = []
            return render(request, 'boxplot.html', {'box_plot': box_plot})

        for i in rangos:
            lista_temperatura.append(i.temperatura)

        lista_temperatura.sort()

        box_plot.append([lista_temperatura[0], np.percentile(lista_temperatura, 25), np.median(lista_temperatura),
                         np.percentile(lista_temperatura, 75), lista_temperatura[-1]])
    else:
        box_plot = []

    return render(request,'boxplot.html', {'box_plot':box_plot})




# Web Service
class TemperaturaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer





def whoami(request):

    sex = request.GET['sex']
    name = request.GET['name']

    response = 'You are ' + name + ' and of sex ' + sex
    a = Temperatura(temperatura = response)
    a.save()
    return HttpResponse(response)

'''
def temperaturas(request):
    temp = request.GET['temp']
    #humedad = request.GET['hum']
    response = 'Temperatura registrada en el servidor: '+temp
    a = Temperatura(temperatura = temp, humedad=0.0 )
    a.save()
    return HttpResponse(response)
'''
