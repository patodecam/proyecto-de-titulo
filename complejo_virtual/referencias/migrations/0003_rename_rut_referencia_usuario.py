# Generated by Django 5.0.6 on 2024-06-11 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referencias', '0002_remove_referencia_nombre_referencia_rut'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referencia',
            old_name='rut',
            new_name='usuario',
        ),
    ]
