from django import forms
from .models import Reserva
from datetime import date, timedelta

class Formularioreserva(forms.ModelForm):
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
    
    
    class Meta:
        model = Reserva
        fields = ['cantidad_personas', 'fecha']
        widgets = {
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','required': 'required',}),
        }

    def __init__(self, *args, **kwargs):
        self.is_edit = kwargs.pop('is_edit', False)
        self.id_reserva = kwargs.pop('id_reserva', None)
        super(Formularioreserva, self).__init__(*args, **kwargs)
        if self.id_reserva:
            reserva = Reserva.objects.get(pk=self.id_reserva)
            self.fields['cantidad_personas'].initial = reserva.cantidad_personas
            self.fields['fecha'].initial = reserva.fecha
            self.fields['aceptar_terminos'].initial = reserva.terminosCondiciones
        
        if self.is_edit:
            self.fields.pop('aceptar_terminos', None)

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        hoy = date.today()
        diadereserva = hoy + timedelta(days=5)
        if fecha <= diadereserva:
            raise forms.ValidationError('La fecha de reserva debe ser al menos con 5 días de anticipación.')
        if self.id_reserva:
            reserva_actual = Reserva.objects.get(pk=self.id_reserva)
            if fecha != reserva_actual.fecha and Reserva.objects.filter(fecha=fecha).exists():
                raise forms.ValidationError('Esta fecha ya está reservada.')
        else:
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