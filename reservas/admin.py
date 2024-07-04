from django.contrib import admin
from .models import Reserva
# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id_reserva', 'rut', 'cantidad_personas', 'cantidad_dias', 'fecha_creacion', 'terminosCondiciones')
    search_fields = ('rut', 'fecha_creacion')
admin.site.register(Reserva)