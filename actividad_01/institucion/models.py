from django.db import models

class Museo (models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)
    ciudad = models.CharField(max_length=150)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre

class Guia_museo (models.Model):
    nombre_completo = models.CharField(max_length=200)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados =  models.CharField(max_length=200)
    
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, \
            related_name="guias")
    
    def __str__(self):
        return f"{self.nombre_completo} ({self.anios_experiencia_guia} años exp.)"

class Exposicion (models.Model):
    titulo_exhibicion = models.CharField(max_length=200)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=100, decimal_places=2)
    tematica = models.CharField(max_length=200)

    museo = models.ForeignKey(Guia_museo, on_delete=models.SET_NULL, null=True, \
            related_name="exposiciones")
    def __str__(self):
        return self.titulo_exhibicion

