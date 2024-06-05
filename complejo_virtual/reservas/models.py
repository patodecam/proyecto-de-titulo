from django.db import models
from registro.models import Usuario
# Create your models here.

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    rut=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    cantidad_personas=models.IntegerField(verbose_name="Cantidad de personas")
    fecha=models.DateField(verbose_name="Fecha de reserva")
    terminosCondiciones = models.BooleanField(default=False, verbose_name="Términos y Condiciones")
    
    def __str__(self): 
         return f"Reserva #{self.id_reserva}"