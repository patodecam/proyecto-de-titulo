from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Formularioreserva
from .models import Reserva
# Create your views here.

@login_required
def reserva(request):
    if request.method == 'POST':
        form = Formularioreserva(request.POST)
        if form.is_valid():
            cantidad_personas = form.cleaned_data['cantidad_personas']
            fecha = form.cleaned_data['fecha']
            aceptar_terminos = form.cleaned_data['aceptar_terminos']
            usuario = request.user
            reserva = Reserva(
                cantidad_personas=cantidad_personas, 
                fecha=fecha, 
                rut=usuario,
                terminosCondiciones=aceptar_terminos
            )
            reserva.save()
            messages.success(request, 'Tu reserva ha sido creada exitosamente.')
        else:
            print("Errores del formulario:", form.errors)
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = Formularioreserva()
    
    return render(request, 'reserva.html', {'form': form})
    