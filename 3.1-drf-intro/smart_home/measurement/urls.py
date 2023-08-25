from django.urls import path

from measurement.views import SensorsView, SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view())
]