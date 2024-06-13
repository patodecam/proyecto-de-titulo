from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
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
            totalPago = cantidad_personas * 5000

            reserva = Reserva.objects.create(
                cantidad_personas=cantidad_personas,
                fecha=fecha,
                rut=usuario,
                terminosCondiciones=aceptar_terminos,
                monto=totalPago
            )
            reserva.save()
            
            destinatario = request.user.correo
            primernombre = request.user.primerNombre     
            primerapellido = request.user.primerApellido  
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
                return redirect('iniciar_pago', reserva_id=reserva.id_reserva)
            except Exception as e:
                messages.error(request, f'Error al enviar el correo de confirmación: {str(e)}')
        else:
            print("Errores del formulario:", form.errors)
            messages.error(request, 'Esta fecha ya se encuentra reservada.')
    else:
        form = Formularioreserva()
    
    return render(request, 'reserva.html', {'form': form})


@login_required
def lista_reservas(request):
    if request.user.usuarioAdministrador:
        reservas = Reserva.objects.all().order_by('fecha') 
    else:
        reservas = Reserva.objects.filter(rut=request.user).order_by('fecha')

    return render(request, 'mis_reservas.html', {'reservas': reservas})

@login_required
def eliminar_reserva(request,id_reserva):
    if not request.user.usuarioAdministrador:
        return redirect('lista_reservas')
    reserva = get_object_or_404(Reserva, id_reserva=id_reserva)
    reserva.delete()
    messages.success(request, 'Reserva eliminada exitosamente.')
    return redirect('lista_reservas')


@login_required
def modificar_reserva(request, id_reserva):
    if not request.user.usuarioAdministrador:
        return redirect('listar_reservas')
    reserva = get_object_or_404(Reserva, id_reserva=id_reserva)
    if request.method == 'POST':
        form = Formularioreserva(request.POST, id_reserva=id_reserva, is_edit=True)
        if form.is_valid():
            nueva_fecha = form.cleaned_data['fecha']
            if nueva_fecha != reserva.fecha:
                if Reserva.objects.filter(fecha=nueva_fecha).exists():
                    form.add_error('fecha', 'Esta fecha ya está reservada.')
                else:
                    reserva.cantidad_personas = form.cleaned_data['cantidad_personas']
                    reserva.fecha = nueva_fecha
                    reserva.save()
                    messages.success(request, 'Reserva actualizada exitosamente.')
                    return redirect('lista_reservas')
            else:
                reserva.cantidad_personas = form.cleaned_data['cantidad_personas']
                reserva.save()
                messages.success(request, 'Reserva actualizada exitosamente.')
                return redirect('lista_reservas')
    else:
        form = Formularioreserva(id_reserva=id_reserva, is_edit=True)
    
    return render(request, 'editar_reserva.html', {'form': form, 'reserva': reserva})