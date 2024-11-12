from django.db import models

# Create your models here.

class Proveedores(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    gerente = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre