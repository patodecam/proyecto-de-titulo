from django.urls import path
from .views import reserva,lista_reservas,eliminar_reserva,modificar_reserva

urlpatterns = [
    path('reservar/',reserva, name='reserva'),
    path('reservas/', lista_reservas, name='lista_reservas'),
    path('reservas/eliminar/<id_reserva>/', eliminar_reserva, name='eliminar_reserva'),
    path('reservas/modificar/<id_reserva>/', modificar_reserva, name='modificar_reserva'),
]
