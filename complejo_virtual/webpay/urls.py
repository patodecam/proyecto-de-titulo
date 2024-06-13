# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('pago/iniciar_pago/<int:reserva_id>/', iniciar_pago, name='iniciar_pago'),
    path('pago/confirmar_pago/', confirmar_pago, name='confirmar_pago'),
    # otras rutas
]
