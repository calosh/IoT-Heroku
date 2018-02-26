from .models import Temperatura
from rest_framework import serializers


class TemperaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperatura
        fields = ('url','date','time','temperatura')



'''
class TemperaturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperatura
        fields = ('date','temperatura','humedad')
'''

