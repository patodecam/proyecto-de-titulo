from django import forms
from .models import Referencia

class ReferenciaForm(forms.ModelForm):
    class Meta:
        model = Referencia
        fields = ['comentario', 'escala_servicio']
        widgets = {
            'escala_servicio': forms.Select(choices=[(i, i) for i in range(1, 6)]), # Esto crea opciones del 1 al 5
        }
