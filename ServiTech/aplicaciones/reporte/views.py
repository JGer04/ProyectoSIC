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

def resultados(request):
    costos = cuenta.objects.get(codigo = 4101)

    instalacion = cuenta.objects.get(codigo = 5101)
    mantenimiento = cuenta.objects.get(codigo = 5201)
    seguridad = cuenta.objects.get(codigo = 5301)

    total_ingreso = instalacion.monto + mantenimiento.monto + seguridad.monto
    perdida_ganancia = cuenta.objects.get(codigo = 3102)
    perdida_ganancia.monto = total_ingreso - costos.monto


    return render(request, 'reporte/resultados.html',{
        'costos':costos,
        'instalacion':instalacion,
        'mantenimiento':mantenimiento,
        'seguridad':seguridad,
        'total_ingreso':total_ingreso,
        'perdida_ganancia':perdida_ganancia,
    })

def capital(request):
    capital = cuenta.objects.get(codigo = 3101)
    perdida_ganancia = cuenta.objects.get(codigo=3102)

    capital_nuevo = perdida_ganancia.monto + capital.monto

    return render(request, 'reporte/capital.html', {
        'capital':capital,
        'perdida_ganancia':perdida_ganancia,
        'capital_nuevo':capital_nuevo,
    })


    
    






        