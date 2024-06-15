import datetime
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordContextMixin
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import Formularioregistro, Formulariologin, Formulariorecuperacion,Formulariodecambio
from core.email_sender import enviar_correo


User = get_user_model()
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
 
def password_reset_request(request):
    if request.method == 'POST':
        form = Formulariorecuperacion(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['email']
            asunto = 'Recuperación de contraseña'
            plantilla = 'core/plantilla_recuperacion_contraseña.html'
            try:
                usuario = User.objects.get(correo=correo)
                primernombre = usuario.primerNombre     
                primerapellido = usuario.primerApellido  
                nombrecompleto = f"{primernombre} {primerapellido}"
                
                uidb64 = urlsafe_base64_encode(force_bytes(usuario.pk))
                token = default_token_generator.make_token(usuario)
                enlace_recuperacion = request.build_absolute_uri(
                    reverse_lazy('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                )
                
                contexto = {
                    'nombre': nombrecompleto,
                    'enlace_recuperacion': enlace_recuperacion,
                }

                enviar_correo(correo, asunto, plantilla, contexto)
                messages.success(request, 'Se ha enviado un correo con las instrucciones para restablecer tu contraseña.')
            except User.DoesNotExist:
                messages.error(request, 'No existe ningún usuario registrado con este correo electrónico.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al enviar el correo de recuperación: {str(e)}')
            
            return redirect('password_reset_done')
    else:
        form = Formulariorecuperacion()
        
    return render(request, 'password_reset_form.html', {'form': form})

def password_reset_done(request): 
    return render(request, 'password_reset_done.html')


