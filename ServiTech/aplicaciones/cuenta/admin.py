from django.contrib import admin
from .models import cuenta
# Register your models here.
@admin.register(cuenta)
class cuenta(admin.ModelAdmin):
    list_display=('codigo', 'nombre', 'monto')