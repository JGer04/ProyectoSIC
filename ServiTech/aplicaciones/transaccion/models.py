from django.db import models
from django.utils import formats
# Create your models here.
class transaccion(models.Model):
    CLASIFICACIONES = (
        ('Servicio', 'Servicio'),
        ('Compra', 'Compra'),
    )
    tipo = models.CharField(max_length=50, choices=CLASIFICACIONES, default='') 
    codigo = models.CharField(max_length=10)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    cuenta_Debe = models.ForeignKey('cuenta.Cuenta', on_delete=models.CASCADE, related_name='transacción_abono')
    cuenta_Haber = models.ForeignKey('cuenta.Cuenta', on_delete=models.CASCADE, related_name='transacción_deuda')   
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"transaccion #{self.pk}"
    def fecha_formateada(self):
        return formats.date_format(self.fecha, "d-m-Y")