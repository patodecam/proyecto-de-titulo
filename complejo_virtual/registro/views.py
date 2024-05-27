from django.shortcuts import render
from . forms import Formularioregistro
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