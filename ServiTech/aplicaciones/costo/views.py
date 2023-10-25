from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms
from decimal import Decimal, getcontext

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
    puestos = puesto.objects.all()

    actividad1 = actividad.objects.get(codigo = 10)
    actividad2 = actividad.objects.get(codigo = 11)
    actividad3 = actividad.objects.get(codigo = 12)
    actividad4 = actividad.objects.get(codigo = 13)

    inductor1 = inductor.objects.get(codigo = 30)
    inductor2 = inductor.objects.get(codigo = 31)
    inductor3 = inductor.objects.get(codigo = 32)
    inductor4 = inductor.objects.get(codigo = 33)

    Costo1 = costo_indirectos.objects.get(codigo = 20)
    Costo2 = costo_indirectos.objects.get(codigo = 21)
    Costo3 = costo_indirectos.objects.get(codigo = 22)
    Costo4 = costo_indirectos.objects.get(codigo = 23)
    Costo5 = costo_indirectos.objects.get(codigo = 24)

    puesto1 = puesto.objects.get(codigo = 40)
    puesto2 = puesto.objects.get(codigo = 41)
    puesto3 = puesto.objects.get(codigo = 42)

    consultoria_inicial = (Costo1.monto + (Decimal(0.5)*Costo3.monto) + (Decimal(0.75)*Costo4.monto)).quantize(Decimal('0.00'))
    seleccion_HS = ((Decimal(0.25)*Costo3.monto) + (Decimal(0.25)*Costo4.monto)).quantize(Decimal('0.00'))
    instalacion_configuracion =(Costo2.monto + (Decimal(0.12)*Costo3.monto) + (Decimal(0.60)*Costo5.monto)).quantize(Decimal('0.00'))
    capacitacion = ((Decimal(0.13)*Costo3.monto) + (Decimal(0.40)*Costo5.monto)).quantize(Decimal('0.00'))

    consultoria_inicial2 = (consultoria_inicial/Decimal(50)).quantize(Decimal('0.00'))
    seleccion_HS2 = (seleccion_HS/Decimal(125)).quantize(Decimal('0.00'))
    instalacion_configuracion2 = (instalacion_configuracion/Decimal(10)).quantize(Decimal('0.00'))
    capacitacion2 = (capacitacion/Decimal(200)).quantize(Decimal('0.00'))

    consultoria_inicial3 = (consultoria_inicial*consultoria_inicial2).quantize(Decimal('0.00'))
    seleccion_HS3 = (seleccion_HS*seleccion_HS2).quantize(Decimal('0.00'))
    instalacion_configuracion3 = (instalacion_configuracion*instalacion_configuracion2).quantize(Decimal('0.00'))
    capacitacion3 = (capacitacion*capacitacion2).quantize(Decimal('0.00'))

    mod1 = (puesto1.salario_por_hora*Decimal(50)).quantize(Decimal('0.00'))
    mod2 = (puesto2.salario_por_hora*Decimal(200)).quantize(Decimal('0.00'))
    mod3 = (puesto3.salario_por_hora*Decimal(125)).quantize(Decimal('0.00'))

    total_mod = (mod1+mod2+(Decimal(2)*mod3)).quantize(Decimal('0.00'))
    total_ci = consultoria_inicial+seleccion_HS+instalacion_configuracion+capacitacion

    costo_total = total_ci+total_mod
    costo_unitario = (costo_total/Decimal(10)).quantize(Decimal('0.00'))

        

    return render(request, 'costo/costeo.html', {
        'actividades':actividades,
        'inductores':inductores,
        'puestos':puestos,

        'Costo1':Costo1,
        'Costo2':Costo2,
        'Costo3':Costo3,
        'Costo4':Costo4,
        'Costo5':Costo5,

        'consultoria_inicial':consultoria_inicial,
        'seleccion_HS':seleccion_HS,
        'instalacion_configuracion':instalacion_configuracion,
        'capacitacion':capacitacion,

        'inductor1':inductor1,
        'inductor2':inductor2,
        'inductor3':inductor3,
        'inductor4':inductor4,

        'actividad1':actividad1,
        'actividad2':actividad2,
        'actividad3':actividad3,
        'actividad4':actividad4,

        'consultoria_inicial2':consultoria_inicial2,
        'seleccion_HS2':seleccion_HS2,
        'instalacion_configuracion2':instalacion_configuracion2,
        'capacitacion2':capacitacion2,

        'consultoria_inicial3':consultoria_inicial3,
        'seleccion_HS3':seleccion_HS3,
        'instalacion_configuracion3':instalacion_configuracion3,
        'capacitacion3':capacitacion3,

        'mod1':mod1,
        'mod2':mod2,
        'mod3':mod3,

        'puesto1':puesto1,
        'puesto2':puesto2,
        'puesto3':puesto3,

        'total_mod':total_mod,
        'total_ci':total_ci,
        'costo_total':costo_total,
        'costo_unitario':costo_unitario

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

