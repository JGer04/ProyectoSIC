from django.shortcuts import render

# Create your views here.
def reporte(request):
    return render(request, 'costo/costo.html')

def servicio(request):
    return render(request, 'costo/servicio.html')

def actividad(request):
    return render(request, 'costo/actividad.html')

def costeo(request):
    return render(request, 'costo/costeo.html')