from django.db import models
from registro.models import Usuario
from datetime import timedelta

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_personas = models.IntegerField(verbose_name="Cantidad de personas")
    cantidad_dias = models.SmallIntegerField(verbose_name="Cantidad de días", default=1)
    fecha_creacion = models.DateField(verbose_name="Fecha de reserva", auto_now=False, auto_now_add=False)
    monto = models.IntegerField(verbose_name="Monto",default=0)
    terminosCondiciones = models.BooleanField(default=False, verbose_name="Términos y Condiciones")
    
    def __str__(self): 
        return f"Reserva #{self.id_reserva}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
