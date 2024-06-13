from django.shortcuts import render
from reservas.models import Reserva

def home(request):
    reservas = Reserva.objects.all()
    
    # Lista de imágenes para el carrusel
    infografias = [
        'img/img1.jpg',
        'img/img2.jpg',
        'img/img3.jpg',
        'img/img4.jpg',
        'img/img5.jpg',
        'img/img6.jpg',
    ]
    
    return render(request, 'home.html', {'reservas': reservas, 'infografias': infografias})

def servicios(request):
    return render(request, 'servicios.html')
