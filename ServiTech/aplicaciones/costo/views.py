from django.shortcuts import render

# Create your views here.
def reporte(request):
    return render(request, 'costo/costo.html')