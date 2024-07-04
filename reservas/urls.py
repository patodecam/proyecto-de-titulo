from django.urls import path
from .views import *

urlpatterns = [
    path('reservar/',reserva, name='reserva'),
    path('reservas/', lista_reservas, name='lista_reservas'),
    path('reservas/eliminar/<id_reserva>/', eliminar_reserva, name='eliminar_reserva'),
    path('reservas/modificar/<id_reserva>/', modificar_reserva, name='modificar_reserva'),
    path('resumen_ejecutivo/', resumen_ejecutivo, name='resumen_ejecutivo'),
]
