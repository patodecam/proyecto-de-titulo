# Generated by Django 5.0.6 on 2024-06-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_remove_reserva_fecha_vencimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='monto',
            field=models.IntegerField(default=0, verbose_name='Monto'),
        ),
    ]
