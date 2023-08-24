# Generated by Django 4.2.4 on 2023-08-24 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_sensor_name_measurements_sensor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurements',
            name='sensor_id',
        ),
        migrations.AddField(
            model_name='measurements',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='measurement.sensor', verbose_name='Датчик'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurements',
            name='temperature',
            field=models.FloatField(verbose_name='Температура'),
        ),
    ]
