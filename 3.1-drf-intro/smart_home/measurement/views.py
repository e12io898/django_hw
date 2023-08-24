# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurements
from .serializers import SensorsSerializer, SensorSerializer

class SensorsView(ListAPIView):
    ''' Все датчики. '''
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

class SensorView(RetrieveAPIView):
    ''' Информация о конкретном датчике. '''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer



