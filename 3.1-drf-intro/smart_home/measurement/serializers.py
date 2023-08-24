from rest_framework import serializers
from measurement.models import Sensor, Measurements

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['sensor', 'temperature', 'created_at']


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    ''' Информация о конкретном датчике. '''
    measurements = MeasurementsSerializer(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorsSerializer(serializers.ModelSerializer):
    ''' Информация о всех датчиках. '''
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

