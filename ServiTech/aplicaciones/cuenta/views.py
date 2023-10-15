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


