# Generated by Django 5.0.3 on 2024-05-17 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_usuario_dv_usuario_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='is_active',
            new_name='usuarioActivo',
        ),
    ]
