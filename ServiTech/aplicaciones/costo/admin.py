from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(actividad)
class actividad(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')

@admin.register(inductor)
class inductor(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'costo_indirecto_asociado')

@admin.register(costo_indirectos)
class costo_indirectos(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'monto')

@admin.register(puesto)
class puesto(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'salario_por_hora')