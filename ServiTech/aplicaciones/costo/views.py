from django.shortcuts import render
from .models import *

# Create your views here.
def reporte(request):
    return render(request, 'costo/costo.html')

def servicio(request):
    return render(request, 'costo/servicio.html')

def TablaActividades(request):
    TablaActividad = actividad.objects.all().order_by('codigo')
    TablaInductor = inductor.objects.all().order_by('codigo')
    TablaCI = costo_indirectos.objects.all().order_by('codigo')
    TablaPuesto = puesto.objects.all().order_by('codigo')

    return render(request, 'costo/actividad.html', {
        'TablaActividad':TablaActividad,
        'TablaInductor':TablaInductor,
        'TablaCI':TablaCI,
        'TablaPuesto':TablaPuesto,
    })

def costeo(request):
    return render(request, 'costo/costeo.html')