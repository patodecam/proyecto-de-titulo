# Generated by Django 5.0.6 on 2024-06-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_remove_reserva_fecha_reserva_cantidad_dias_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_creacion',
            field=models.DateField(verbose_name='Fecha de reserva'),
        ),
    ]
