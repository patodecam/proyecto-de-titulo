import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Usuario

User = get_user_model()

class Formularioregistro(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))
    password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente la contraseña',
            'id': 'password2',
            'required': 'required',
        }
    ))
    
    def clean_primerNombre(self):
        primerNombre = self.cleaned_data.get('primerNombre')
        if not re.match(r'^[a-zA-Z\s\'-]+$', primerNombre):
            raise forms.ValidationError("El primer nombre solo debe contener letras, espacios y apóstrofes.")
        return primerNombre

    def clean_segundoNombre(self):
        segundoNombre = self.cleaned_data.get('segundoNombre')
        if segundoNombre and not re.match(r'^[a-zA-Z\s\'-]+$', segundoNombre):
            raise forms.ValidationError("El segundo nombre solo debe contener letras, espacios y apóstrofes.")
        return segundoNombre

    def clean_primerApellido(self):
        primerApellido = self.cleaned_data.get('primerApellido')
        if not re.match(r'^[a-zA-Z\s\'-]+$', primerApellido):
            raise forms.ValidationError('El primer apellido solo debe contener letras, espacios y apóstrofes.')
        return primerApellido

    def clean_segundoApellido(self):
        segundoApellido = self.cleaned_data.get('segundoApellido')
        if segundoApellido and not re.match(r'^[a-zA-Z\s\'-]+$', segundoApellido):
            raise forms.ValidationError("El segundo apellido solo debe contener letras, espacios y apóstrofes.")
        return segundoApellido
    
    def validar_rut(self, rut, dv):
        rut = str(rut)
        dv = str(dv).upper()
        if not re.match(r'^\d{1,8}$', rut) or not re.match(r'^[0-9K]$', dv):
            return False
        digitos = list(map(int, reversed(rut)))
        factores = [2, 3, 4, 5, 6, 7]
        suma = 0
        for i, digito in enumerate(digitos):
            factor = factores[i % len(factores)]
            suma += digito * factor
        mod = 11 - (suma % 11)
        if mod == 10:
            dv_esperado = 'K'
        elif mod == 11:
            dv_esperado = '0'
        else:
            dv_esperado = str(mod)
        return dv == dv_esperado

    def clean_dv(self):
        dv = self.cleaned_data.get('dv')
        rut = self.cleaned_data.get('rut')
        if not re.match(r'^[0-9Kk]$', dv):
            raise forms.ValidationError('El dígito verificador debe ser un número entre 0 y 9 o una letra K.')
        if not self.validar_rut(rut, dv):
            raise forms.ValidationError('El rut ingresado no es válido.')
        return dv.upper()
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Usuario.objects.filter(correo=correo).exists():
            raise forms.ValidationError('Este correo ya se encuentra registrado.')
        return correo

    def clean_terminosCondiciones(self):
        terminosCondiciones = self.cleaned_data.get('terminosCondiciones')
        if not terminosCondiciones:
            raise forms.ValidationError('Debe aceptar los términos y condiciones para continuar con el registro.')
        return terminosCondiciones
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if  password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

    class Meta:
        model = Usuario
        fields = ['primerNombre', 'segundoNombre', 'primerApellido', 'segundoApellido', 'rut', 'dv', 'correo', 'terminosCondiciones']
        labels = {
            'primerNombre': "Primer nombre",
            'segundoNombre': "Segundo nombre",
            'primerApellido': "Primer apellido",
            'segundoApellido': "Segundo apellido",
            'rut': "Rut",
            'dv': "Dígito verificador",
            'correo': "Correo electrónico",
            'terminosCondiciones': "Términos y condiciones",
        }
        widgets = {
            'primerNombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su primer nombre',
                    'class': 'form-control',
                    'id': 'primernombre',
                    'required': 'required',
                }
            ),
            'segundoNombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su segundo nombre',
                    'class': 'form-control',
                    'id': 'segundonombre'
                }
            ),
            'primerApellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su primer apellido',
                    'class': 'form-control',
                    'id': 'primerapellido',
                    'required': 'required',
                }
            ),
            'segundoApellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su segundo apellido',
                    'class': 'form-control',
                    'id': 'segundoapellido'
                }
            ),
            'rut': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese su rut',
                    'class': 'form-control',
                    'id': 'rut',
                    'required': 'required',
                }
            ),
            'dv': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el dígito verificador',
                    'class': 'form-control',
                    'id': 'dv',
                    'maxlength': '1',
                    'pattern': '[0-9Kk]',
                    'title': 'El DV debe ser un número entre 0 y 9 o la letra K',
                    'required': 'required',
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'placeholder': 'Ingrese su correo electrónico',
                    'class': 'form-control',
                    'id': 'correo',
                    'required': 'required',
                }
            ),
            'terminosCondiciones': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'terminosCondiciones',
                    'required': 'required',
                }
            ),
        }

class Formulariologin(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico', max_length=254. ,widget=forms.EmailInput)
    password=forms.CharField(label='Contraseña',min_length=8,required=True ,widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Usuario o contraseña incorrectos.')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('Esta cuenta está inactiva.')
        return self.cleaned_data
 
class Formulariorecuperacion(PasswordResetForm):
    email= forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if not User.objects.filter(correo=correo).exists():
            raise forms.ValidationError('No existe ningún usuario registrado con este correo electrónico.')
        return correo

class Formulariodecambio(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label='Confirm new password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}),
    )     

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return new_password2
