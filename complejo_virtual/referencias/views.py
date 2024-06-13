from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Referencia
from .forms import ReferenciaForm

def referencias(request):
    form = ReferenciaForm()
    referencias = Referencia.objects.all()
    return render(request, 'referencias.html', {'form': form, 'referencias': referencias})

@login_required
def enviar_referencia(request):
    if request.method == 'POST':
        form = ReferenciaForm(request.POST)
        if form.is_valid():
            referencia = form.save(commit=False)
            referencia.usuario = request.user  # Asigna el usuario autenticado
            referencia.save()
            return redirect('referencias')
    else:
        form = ReferenciaForm()
    return render(request, 'referencias.html', {'form': form, 'referencias': Referencia.objects.all()})
