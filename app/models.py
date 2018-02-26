# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Func

# Create your models here.



class Temperatura(models.Model):

    time = models.DateTimeField(auto_now_add=True, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    temperatura = models.FloatField(default=0.0)
    #humedad = models.FloatField(default=0.0)
    #id_sensor = models.CharField(max_length=50)

    def __unicode__(self):
        return str('Date: {0} - Temperatura: {1}').format(self.date, self.temperatura)

'''
class Humedad(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    humedad = models.FloatField(default=0.0)

    def __unicode__(self):
        return str('{0} - {1}').format(self.date, self.humedad)

'''



class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()