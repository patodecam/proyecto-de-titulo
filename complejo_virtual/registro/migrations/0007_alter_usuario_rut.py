# Generated by Django 5.0.3 on 2024-05-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_alter_usuario_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='RUT'),
        ),
    ]
