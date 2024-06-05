from django.urls import path
from .views import reserva

urlpatterns = [
    path('reservar/',reserva, name='reserva'),
]