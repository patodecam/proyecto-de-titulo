# inicio/forms.py

from django import forms
from .models import Infografia

class InfografiaForm(forms.ModelForm):
    class Meta:
        model = Infografia
        fields = ['titulo', 'imagen', 'descripcion']
