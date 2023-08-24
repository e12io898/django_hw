from django.contrib import admin
from .models import Sensor, Measurements

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    list_display = ['sensor_id', 'temperature', 'created_at']