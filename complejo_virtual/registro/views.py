from django.shortcuts import render,redirect
from django.contrib.auth import  login, logout, authenticate
from django.contrib import messages
from . forms import Formularioregistro,Formulariologin
from core.email_sender import enviar_correo
import datetime

# Create your views here.

def registro(request):    
    if request.method == 'POST':
        form = Formularioregistro(request.POST)
        if form.is_valid():
            form.save()
           
            destinatario = form.cleaned_data['correo']
            primernombre = form.cleaned_data['primerNombre']
            primerapellido = form.cleaned_data['primerApellido']
            nombrecompleto = f"{primernombre} {primerapellido}"
            asunto = "Confirmación de creación de la cuenta"
            plantilla = 'core/plantilla_bienvenida.html'
            contexto = {
                'nombre': nombrecompleto,  
                'fecha': str(datetime.date.today()),
            }
            try:
                enviar_correo(destinatario, asunto, plantilla, contexto)
                messages.success(request, "Tu cuenta ha sido creada exitosamente y se ha enviado un correo de confirmación.")
            except Exception as e:
                messages.error(request, f"Tu cuenta ha sido creada, pero ocurrió un error al enviar el correo de confirmación: {str(e)}")
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = Formularioregistro()

    return render(request, 'registro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return render (request , 'home.html' )


def logear(request):
    if request.method == 'POST':
        form = Formulariologin(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                print(messages)
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            print(messages)
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = Formulariologin()
    return render(request, 'login.html', {'form': form})
    