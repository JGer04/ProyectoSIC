from django.db import models

# Create your models here.
class cuenta(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=5, choices=[("Debe", "Debe"), ("Haber", "Haber")], default="")

    def __str__(self):
        return self.codigo + "  " + self.nombre