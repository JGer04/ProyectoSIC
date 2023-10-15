from django.shortcuts import render
from.models import cuenta
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def cuentas(request):
    catalogo = cuenta.objects.all().order_by('id')

    return render(request, 'cuenta/cuenta.html',{
        'catalogo':catalogo
    })

# -------------------- CRUD DE CATALOGO DE CUENTAS  ------------------------------
class crear(CreateView):
    template_name = 'cuenta/crud/crear.html'
    model = cuenta
    fields = ['codigo','nombre','monto']
    success_url = reverse_lazy('cuenta')

class modificar(UpdateView):
    template_name = 'cuenta/crud/modificar.html'
    model = cuenta
    fields = ['codigo','nombre','monto']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('cuenta')

class eliminar(DeleteView):
    template_name = 'cuenta/crud/eliminar.html'
    model = cuenta
    fields = ['codigo','nombre','monto']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('cuenta')

