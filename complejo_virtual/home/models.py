from django.db import models

# Create your models here.
class Infografia(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='infografias/')
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo