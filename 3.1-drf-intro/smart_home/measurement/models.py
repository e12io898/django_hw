from django.db import models

class Sensor(models.Model):
    name = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

class Measurements(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sensor)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'