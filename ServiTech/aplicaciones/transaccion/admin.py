from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(transaccion)
class transaccion(admin.ModelAdmin):
    list_display=('codigo','descripcion')
