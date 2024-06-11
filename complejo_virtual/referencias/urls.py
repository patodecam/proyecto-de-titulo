from django.urls import path
from . import views

urlpatterns = [
    # otras rutas
    path('referencia', views.referencias, name='referencia'),
]
