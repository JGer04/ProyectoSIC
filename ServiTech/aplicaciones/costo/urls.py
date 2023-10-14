from django.urls import path
from . import views

urlpatterns = [
    path('costo/costo', views.reporte, name = 'costo'),
]
