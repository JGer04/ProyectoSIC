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
    perdida_ganancia = total_ingreso - costos.monto 
    perGa = cuenta.objects.get(codigo = 3102)
    perGa.monto += perdida_ganancia


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

def balance_2(request):
    caja = cuenta.objects.get(codigo = 1101)
    banco = cuenta.objects.get(codigo = 1102)
    cuentas_cobrar = cuenta.objects.get(codigo = 1103)
    papel_utiles = cuenta.objects.get(codigo = 1104)
    iva_credito = cuenta.objects.get(codigo = 1105)
    inventario_servidores = cuenta.objects.get(codigo = 1106)
    equipo_servidores = cuenta.objects.get(codigo = 1201)
    edificio = cuenta.objects.get(codigo = 1202)
    mobiliario = cuenta.objects.get(codigo = 1203)
    vehiculo = cuenta.objects.get(codigo = 1204)

    cuentas_pagar = cuenta.objects.get(codigo = 2101)
    acreedores = cuenta.objects.get(codigo = 2102)
    iva_debito = cuenta.objects.get(codigo = 2103)
    interes = cuenta.objects.get(codigo = 2104)
    renta_cobrada = cuenta.objects.get(codigo = 2105)
    documentos = cuenta.objects.get(codigo = 2201)
    capital = cuenta.objects.get(codigo = 3101)
    utilidad = cuenta.objects.get(codigo = 3102)

    suma_activo = caja.monto + banco.monto + cuentas_cobrar.monto + papel_utiles.monto + iva_credito.monto + inventario_servidores.monto + equipo_servidores.monto + edificio.monto + mobiliario.monto + vehiculo.monto
    suma_pasivo_capital = cuentas_pagar.monto + acreedores.monto + iva_debito.monto + interes.monto + renta_cobrada.monto + documentos.monto + capital.monto + utilidad.monto

    return render(request, 'reporte/balance.html', {
        'caja':caja,
        'banco':banco,
        'cuentas_cobrar':cuentas_cobrar,
        'papel_utiles':papel_utiles,
        'iva_credito':iva_credito,
        'inventario_servidores':inventario_servidores,
        'equipo_servidores':equipo_servidores,
        'edificio':edificio,
        'mobiliario':mobiliario,
        'vehiculo':vehiculo,
        'cuentas_pagar':cuentas_pagar,
        'acreedores':acreedores,
        'iva_debito':iva_debito,
        'interes':interes,
        'renta_cobrada':renta_cobrada,
        'documentos':documentos,
        'capital':capital,
        'utilidad':utilidad,
        'suma_activo':suma_activo,
        'suma_pasivo_capital':suma_pasivo_capital,

    })

    


    
    






        