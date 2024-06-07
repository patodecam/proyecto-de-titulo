from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Formularioreserva
from .models import Reserva
from core.email_sender import enviar_correo
import datetime
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
            
            destinatario=request.user.correo
            primernombre = request.user.primerNombre     
            primerapellido =request.user.primerApellido  
            nombrecompleto = f"{primernombre} {primerapellido}"
            asunto = "Confirmación de Reserva"
            plantilla = 'core/plantilla_confirmacion_reserva.html'
            contexto = {
                    'nombre': nombrecompleto,
                    'fecha': fecha,
                    'cantidad_personas': cantidad_personas,
                    
                }
            
            try:
                enviar_correo(destinatario, asunto, plantilla, contexto)
                messages.success(request, 'Tu reserva ha sido creada exitosamente y se ha enviado un correo de confirmación.')
            except Exception as e:
                messages.error(request, f'Error al enviar el correo de confirmación: {str(e)}')
        else:
            print("Errores del formulario:", form.errors)
            messages.error(request, 'Esta fecha ya se encuentra reservada.')
    else:
        form = Formularioreserva()
    
    return render(request, 'reserva.html', {'form': form})
    