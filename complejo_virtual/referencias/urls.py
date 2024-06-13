from django.urls import path
from . import views

urlpatterns = [
    path('', views.referencias, name='referencias'),
    path('enviar/', views.enviar_referencia, name='enviar_referencia'),
]
