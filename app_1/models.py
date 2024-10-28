from django.db import models
from django.core.validators import MinValueValidator

class Habitat(models.Model):
    nombre = models.CharField(max_length=10)
    duracion_estancia = models.IntegerField(validators = [MinValueValidator(0)])
    fecha_ingreso = models.DateField()

# Create your models here.
