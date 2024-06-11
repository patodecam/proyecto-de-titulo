# referencias/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Referencia
from .forms import ReferenciaForm

@login_required
def referencias(request):
    if request.method == 'POST':
        form = ReferenciaForm(request.POST)
        if form.is_valid():
            referencia = form.save(commit=False)
            referencia.usuario = request.user  # Asigna el usuario autenticado
            referencia.save()
    else:
        form = ReferenciaForm()

    referencias = Referencia.objects.all()
    return render(request, 'referencias.html', {'form': form, 'referencias': referencias})
