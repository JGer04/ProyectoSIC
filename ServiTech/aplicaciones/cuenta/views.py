from django.shortcuts import render
from.models import cuenta
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum

# Create your views here.
def cuentas(request):
    catalogo = cuenta.objects.all().order_by('codigo')

    return render(request, 'cuenta/cuenta.html',{
        'catalogo':catalogo
    })

def cuentas_view(request):
    cuentas_debe = cuenta.objects.filter(categoria='Debe')
    cuentas_haber = cuenta.objects.filter(categoria='Haber')
    suma_monto_debe = cuentas_debe.aggregate(total_debe=Sum('monto'))['total_debe'] or 0
    suma_monto_haber = cuentas_haber.aggregate(total_haber=Sum('monto'))['total_haber'] or 0
    
    return render(request, 'cuenta/mostrar_cuentas.html', {
        'cuentas_debe': cuentas_debe, 
        'cuentas_haber': cuentas_haber,
        'suma_monto_debe': suma_monto_debe,
        'suma_monto_haber': suma_monto_haber,

        })



# -------------------- CRUD DE CATALOGO DE CUENTAS  ------------------------------
class crear(CreateView):
    template_name = 'cuenta/crud/crear.html'
    model = cuenta
    fields = ['codigo','nombre','monto','categoria']
    success_url = reverse_lazy('cuenta')

class modificar(UpdateView):
    template_name = 'cuenta/crud/modificar.html'
    model = cuenta
    fields = ['codigo','nombre','monto','categoria']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('cuenta')

class eliminar(DeleteView):
    template_name = 'cuenta/crud/eliminar.html'
    model = cuenta
    fields = ['codigo','nombre','monto', 'categoria']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('cuenta')



