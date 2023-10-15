from django.shortcuts import render, redirect
from .forms import TransaccionForm
from.models import *
from aplicaciones.cuenta.models import cuenta
from decimal import Decimal
# Create your views here.
def index(request):
    return render(request, 'transaccion/transaccion.html')

def ingresar_transaccion(request):
    cuentas = cuenta.objects.all()
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            transacción = form.save(commit=False)
            if 'calcular_iva' in request.POST:

                monto_float = float(transacción.monto)
                iva = 0.13 * monto_float
                transacción.monto += Decimal(iva)

            transacción.save()

            debe = transacción.cuenta_Debe
            haber = transacción.cuenta_Haber
            monto = transacción.monto

            debe.monto = debe.monto - monto
            debe.save()

            haber.monto = haber.monto - monto
            haber.save()

            return redirect('transaccion')
    else:
        form = TransaccionForm()
    return render(request, 'transaccion/ingresar_transaccion.html',{'form':form, 'cuentas':cuentas})

def TablaTransaccion(request):
    transaccionTabla = transaccion.objects.all().order_by('id')
    return render(request, 'transaccion/transaccion.html',{
        'transaccionTabla':transaccionTabla
    })