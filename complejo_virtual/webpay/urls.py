# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('iniciar_pago/', views.iniciar_pago, name='iniciar_pago'),
    path('confirmar_pago/', views.confirmar_pago, name='confirmar_pago'),
]
