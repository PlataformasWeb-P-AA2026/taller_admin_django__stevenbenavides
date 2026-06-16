from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Museo (models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    ciudad = models.CharField(max_length=150)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre

class Guia_museo (models.Model):
    nombre_completo = models.CharField(max_length=100)
    anios_experiencia_guia = models.CharField(max_length=100)
    idiomas_hablados = models.ForeignKey(Estudiante, on_delete=models.CASCADE, \
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
