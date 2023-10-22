from django.shortcuts import render
from aplicaciones.cuenta.models import *
from django.db.models import Sum

# Create your views here.
def reporte(request):
    return render(request, 'reporte/reporte.html')

def balance(request):
    cuentas_debe = cuenta.objects.filter(categoria='Debe')
    cuentas_haber = cuenta.objects.filter(categoria='Haber')
    suma_monto_debe = cuentas_debe.aggregate(total_debe=Sum('monto'))['total_debe'] or 0
    suma_monto_haber = cuentas_haber.aggregate(total_haber=Sum('monto'))['total_haber'] or 0
    
    return render(request, 'reporte/balance.html', {
        'cuentas_debe': cuentas_debe, 
        'cuentas_haber': cuentas_haber,
        'suma_monto_debe': suma_monto_debe,
        'suma_monto_haber': suma_monto_haber,

        })


        