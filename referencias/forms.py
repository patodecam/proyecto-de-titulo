from django import forms
from .models import Referencia
import bleach

class ReferenciaForm(forms.ModelForm):
    class Meta:
        model = Referencia
        fields = ['comentario', 'escala_servicio']
        widgets = {
            'escala_servicio': forms.Select(choices=[(i, i) for i in range(1, 6)]), # Esto crea opciones del 1 al 5
        }

    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario')
        sanitized_comentario = bleach.clean(comentario, tags=[], attributes={}, strip=True)
        return sanitized_comentario
