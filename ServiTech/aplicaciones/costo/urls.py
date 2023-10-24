from django.urls import path
from . import views

urlpatterns = [
    path('costo/costo', views.reporte, name = 'costo'),
    path('costo/servicio', views.servicio, name = 'servicio'),
    path('index/actividad', views.actividad, name='actividad'),
    path('index/costeo', views.costeo, name='costeo'),
]
