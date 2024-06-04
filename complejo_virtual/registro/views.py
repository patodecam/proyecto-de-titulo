from django.shortcuts import redirect, render
from django.contrib.auth import  login, logout, authenticate
from django.contrib import messages
from . forms import Formularioregistro,Formulariologin
# Create your views here.

def registro(request):
    if request.method=='POST':
        print(request.POST)
        form=Formularioregistro(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Formularioregistro()
    return render (request , 'registro.html', {'form': form} )

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
