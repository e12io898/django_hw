from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView

from .models import Sensor, Measurements
from .serializers import SensorsSerializer, SensorSerializer, MeasurementSerializer


class SensorsView(ListCreateAPIView):
    ''' Все датчики + добавление. '''
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorView(RetrieveUpdateAPIView):
    ''' Информация о конкретном датчике + изменение. '''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementView(CreateAPIView):
    ''' Добавить измерение. '''
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer