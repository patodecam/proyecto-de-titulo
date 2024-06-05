from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, rut,dv,primerNombre,primerApellido,correo,password=None ):
        if not rut:
            raise ValueError('El usuario debe tener rut chileno .')
        if not dv:
            raise ValueError('El usuario debe ingresar el digito verificador correcto .')
        if not correo:
            raise ValueError('El usuario debe ingresar su correo electronico.')
        if not primerNombre:
            raise  ValueError('El usuario debe ingresar su nombre.')
        if not primerApellido:
             raise  ValueError('El usuario debe ingresar su apellido.')
        
         
         
        usuario=self.model(
            rut=rut,
            dv=dv,
            correo=self.normalize_email(correo),
            primerNombre=primerNombre,
            primerApellido=primerApellido,
            
            
        )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, rut,dv,primerNombre,primerApellido,correo,password):
        usuario=self.create_user(
            rut=rut,
            dv=dv,
            correo=correo,
            primerNombre=primerNombre,
            primerApellido=primerApellido,
            password=password,
            
            
        )
        usuario.usuarioAdministrador=True
        usuario.save()
        return usuario
            

class Usuario(AbstractBaseUser):
    rut = models.IntegerField(primary_key=True, verbose_name="RUT")
    dv = models.CharField(max_length=1,verbose_name="Dígito Verificador")
    primerNombre = models.CharField(max_length=20, verbose_name="Primer Nombre")
    segundoNombre = models.CharField(max_length=20, blank=True, verbose_name="Segundo Nombre")
    primerApellido = models.CharField(max_length=20, verbose_name="Primer Apellido")
    segundoApellido = models.CharField(max_length=20, blank=True, verbose_name="Segundo Apellido")
    correo = models.EmailField(max_length=50, unique=True, verbose_name="Correo")
    terminosCondiciones = models.BooleanField(default=False, verbose_name="Términos y Condiciones")
    fechaRegistro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    usuarioAdministrador=models.BooleanField(default=False, verbose_name="Administrador")
    usuarioActivo = models.BooleanField(default=True)
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['rut','dv','primerNombre', 'primerApellido']
    
    def __str__(self): 
        return f'{self.rut}'
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuarioAdministrador
