from django import forms
from .models import Reserva
from datetime import date, timedelta

class Formularioreserva(forms.Form):
    cantidad_personas = forms.IntegerField(
        label='Cantidad de personas',
        min_value=30,
        max_value=200,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la cantidad de personas',
                'id': 'cantidadpersonas',
                'required': 'required',
            }
        )
    )
    fecha = forms.DateField(
        label='Fecha de reserva',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seleccione la fecha de reserva',
                'id': 'fecha',
                'type': 'date',
                'required': 'required',
            }
        )
    )
    aceptar_terminos = forms.BooleanField(
        label='Acepto los términos y condiciones',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'terminosCondiciones',
            }
        )
    )

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        hoy = date.today()
        diadereserva = hoy + timedelta(days=5)
        if fecha <= diadereserva:
            raise forms.ValidationError('La fecha de reserva debe ser al menos con 5 días de anticipación.')
        if Reserva.objects.filter(fecha=fecha).exists():
            raise forms.ValidationError('Esta fecha ya está reservada.')
        return fecha

    def clean_cantidad_personas(self):
        cantidad_personas = self.cleaned_data.get('cantidad_personas')
        if not (30 <= cantidad_personas <= 200):
            raise forms.ValidationError('La cantidad de personas permitidas es entre 30 y 200.')
        return cantidad_personas
    
    def clean_aceptar_terminos(self):
        aceptar_terminos = self.cleaned_data.get('aceptar_terminos')
        if not aceptar_terminos:
            raise forms.ValidationError('Debe aceptar los términos y condiciones para continuar con el registro.')
        return aceptar_terminos