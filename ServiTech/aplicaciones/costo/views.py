from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms

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

#def costeo(request):
#    return render(request, 'costo/costeo.html')

def costeo(request):
    actividades = actividad.objects.all()
    inductores = inductor.objects.all()
    #inductor31 = inductor.objects.get(codigo=31)
    #inductor32 = inductor.objects.get(codigo=32)
    #inductor33 = inductor.objects.get(codigo=33)
    #CI_indirectos = costo_indirectos.objects.all()
    puestos = puesto.objects.all()

   
        

    return render(request, 'costo/costeo.html', {
        'actividades':actividades,
        'inductores':inductores,
        #'inductor31':inductor31,
        #'inductor32':inductor32,
        #'inductor33':inductor33,
        #'CI_indirectos':CI_indirectos,
        'puestos':puestos
    })         
    

# -------------------- CRUD DE ACTIVIDADES  ------------------------------
class crearAC(CreateView):
    template_name = 'costo/CRUD-actividad/crear.html'
    model = actividad
    fields = ['codigo','nombre']
    success_url = reverse_lazy('actividad')

class modificarAC(UpdateView):
    template_name = 'costo/CRUD-actividad/modificar.html'
    model = actividad
    fields = ['codigo','nombre']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('actividad')

# -------------------- CRUD DE INDUCTORES  ------------------------------
class crearIN(CreateView):
    template_name = 'costo/CRUD-inductor/crear.html'
    model = inductor
    fields = ['codigo','nombre','costo_indirecto_asociado']
    success_url = reverse_lazy('actividad')

class modificarIN(UpdateView):
    template_name = 'costo/CRUD-inductor/modificar.html'
    model = inductor
    fields = ['codigo','nombre', 'costo_indirecto_asociado']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('actividad')

# -------------------- CRUD DE CI  ------------------------------
class crearCI(CreateView):
    template_name = 'costo/CRUD-CI/crear.html'
    model = costo_indirectos
    fields = ['codigo','nombre','monto']
    success_url = reverse_lazy('actividad')

class modificarCI(UpdateView):
    template_name = 'costo/CRUD-CI/modificar.html'
    model = costo_indirectos
    fields = ['codigo','nombre', 'monto']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('actividad')

# -------------------- CRUD DE CI  ------------------------------
class crearPU(CreateView):
    template_name = 'costo/CRUD-puesto/crear.html'
    model = puesto
    fields = ['codigo','nombre','salario_por_hora']
    success_url = reverse_lazy('actividad')

class modificarPU(UpdateView):
    template_name = 'costo/CRUD-puesto/modificar.html'
    model = puesto
    fields = ['codigo','nombre', 'salario_por_hora']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('actividad')

