from django.shortcuts import render, redirect
from aplicaciones.cuenta.models import *
from django.db.models import Sum
from django.db.models.functions import Length

# Create your views here.
def reporte(request):
    return render(request, 'reporte/reporte.html')

def balance(request):
    subcuenta = cuenta.objects.annotate(
        cuenta_length = Length('codigo')
    )

    subcuenta = subcuenta.filter(cuenta_length__gt = 2)

    cuentas_debe = cuenta.objects.filter(categoria='Debe')
    cuentas_haber = cuenta.objects.filter(categoria='Haber')

    suma_monto_debe = cuentas_debe.aggregate(total_debe=Sum('monto'))['total_debe'] or 0
    suma_monto_haber = cuentas_haber.aggregate(total_haber=Sum('monto'))['total_haber'] or 0
    
    return render(request, 'reporte/balance.html', {
        
        'cuentas_debe': cuentas_debe, 
        'cuentas_haber': cuentas_haber,
        'subcuenta':subcuenta,
        'suma_monto_debe': suma_monto_debe,
        'suma_monto_haber': suma_monto_haber,

        })

def capital(request):
    capital = cuenta.objects.get(codigo = 3101)
    utilidad = cuenta.objects.get(codigo = 3102)

    total = capital.monto + utilidad.monto

    return render(request, 'reporte/capital.html',{
        'capital':capital,
        'utilidad':utilidad,
        'total':total,
    })






        