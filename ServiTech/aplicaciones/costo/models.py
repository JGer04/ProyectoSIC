from django.db import models

# Create your models here.

class actividad(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    costo_indirecto_asociado = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.codigo + " " + self.nombre + " " + self.costo_indirecto_asociado
    
class inductor(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.codigo + " " + self.nombre 

class costo_indirectos(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo + " " + self.nombre + " " +str(self.monto)
    
class puesto(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    salario_por_hora = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo + " " + self.nombre + " " +str(self.salario_por_hora)
