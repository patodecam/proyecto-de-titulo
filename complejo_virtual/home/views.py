from django.shortcuts import render
from reservas.models import Reserva
from datetime import datetime, timedelta

def home(request):
    reservas = Reserva.objects.all()
    return render(request, 'home.html', {'reservas': reservas})

def servicios(request):
    return render(request, 'servicios.html')
