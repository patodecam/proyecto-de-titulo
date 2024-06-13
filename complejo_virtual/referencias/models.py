# referencias/models.py
from django.db import models
from registro.models import Usuario

class Referencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    comentario = models.TextField()
    escala_servicio = models.PositiveSmallIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.primerNombre} {self.usuario.primerApellido}'
